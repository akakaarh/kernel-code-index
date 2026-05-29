"""Kernel Code Index - Query interface for the symbol database."""

import sqlite3
import sys
from pathlib import Path

DB_PATH = Path(__file__).parent / "kernel_index.db"


def get_conn(db_path: Path = DB_PATH) -> sqlite3.Connection:
    conn = sqlite3.connect(str(db_path))
    conn.row_factory = sqlite3.Row
    return conn


def find_symbol(conn: sqlite3.Connection, name: str, exact: bool = False):
    """Find symbols by name (substring or exact match)."""
    if exact:
        rows = conn.execute(
            """SELECT s.name, s.kind, s.line, s.typeref, s.signature, s.is_static,
                      f.path
               FROM symbols s JOIN files f ON s.file_id = f.id
               WHERE s.name = ?
               ORDER BY s.kind, f.path""",
            (name,),
        ).fetchall()
    else:
        pattern = f"%{name}%"
        rows = conn.execute(
            """SELECT s.name, s.kind, s.line, s.typeref, s.signature, s.is_static,
                      f.path
               FROM symbols s JOIN files f ON s.file_id = f.id
               WHERE s.name LIKE ?
               ORDER BY s.name, s.kind, f.path""",
            (pattern,),
        ).fetchall()
    return rows


def list_functions_in_file(conn: sqlite3.Connection, filepath: str):
    """List all functions in a given file."""
    rows = conn.execute(
        """SELECT s.name, s.line, s.typeref, s.signature, s.is_static
           FROM symbols s JOIN files f ON s.file_id = f.id
           WHERE f.path LIKE ? AND s.kind = 'function'
           ORDER BY s.line""",
        (f"%{filepath}%",),
    ).fetchall()
    return rows


def symbols_by_kind(conn: sqlite3.Connection, kind: str, subsystem: str = None):
    """List all symbols of a given kind, optionally filtered by subsystem."""
    if subsystem:
        rows = conn.execute(
            """SELECT s.name, s.line, f.path
               FROM symbols s JOIN files f ON s.file_id = f.id
               WHERE s.kind = ? AND f.subsystem = ?
               ORDER BY s.name
               LIMIT 100""",
            (kind, subsystem),
        ).fetchall()
    else:
        rows = conn.execute(
            """SELECT s.name, s.line, f.path
               FROM symbols s JOIN files f ON s.file_id = f.id
               WHERE s.kind = ?
               ORDER BY s.name
               LIMIT 100""",
            (kind,),
        ).fetchall()
    return rows


def file_summary(conn: sqlite3.Connection, filepath: str):
    """Get summary of symbols in a file."""
    rows = conn.execute(
        """SELECT s.kind, COUNT(*) as cnt
           FROM symbols s JOIN files f ON s.file_id = f.id
           WHERE f.path LIKE ?
           GROUP BY s.kind ORDER BY cnt DESC""",
        (f"%{filepath}%",),
    ).fetchall()
    return rows


def show_result(rows, fields):
    """Pretty-print query results."""
    if not rows:
        print("  (no results)")
        return
    for row in rows:
        parts = []
        for f in fields:
            val = row[f]
            if val is None:
                val = ""
            parts.append(f"{f}={val}")
        print(f"  {' | '.join(parts)}")


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Kernel Code Index Query Tool")
    sub = parser.add_subparsers(dest="cmd")

    # find: search symbol by name
    p_find = sub.add_parser("find", help="Find symbol by name")
    p_find.add_argument("name", help="Symbol name (substring match)")
    p_find.add_argument("--exact", action="store_true", help="Exact match only")

    # funcs: list functions in file
    p_funcs = sub.add_parser("funcs", help="List functions in a file")
    p_funcs.add_argument("file", help="File path (substring match)")

    # kind: list symbols by kind
    p_kind = sub.add_parser("kind", help="List symbols by kind")
    p_kind.add_argument("kind", help="Symbol kind (function, macro, struct, etc.)")
    p_kind.add_argument("--subsystem", help="Filter by subsystem")

    # summary: file symbol summary
    p_summary = sub.add_parser("summary", help="Symbol summary for a file")
    p_summary.add_argument("file", help="File path (substring match)")

    # stats: overall statistics
    sub.add_parser("stats", help="Show database statistics")

    # callers: find callers of a function
    p_callers = sub.add_parser("callers", help="Find callers of a function")
    p_callers.add_argument("name", help="Function name (exact match)")

    # callees: find callees of a function
    p_callees = sub.add_parser("callees", help="Find callees of a function")
    p_callees.add_argument("name", help="Function name (exact match)")

    # callstats: call graph statistics
    sub.add_parser("callstats", help="Show call graph statistics")

    args = parser.parse_args()
    if not args.cmd:
        parser.print_help()
        return

    conn = get_conn()

    if args.cmd == "find":
        rows = find_symbol(conn, args.name, args.exact)
        print(f"Symbols matching '{args.name}':")
        show_result(rows, ["name", "kind", "typeref", "signature", "path", "line", "is_static"])

    elif args.cmd == "funcs":
        rows = list_functions_in_file(conn, args.file)
        print(f"Functions in '{args.file}':")
        show_result(rows, ["name", "typeref", "signature", "line", "is_static"])

    elif args.cmd == "kind":
        rows = symbols_by_kind(conn, args.kind, args.subsystem)
        label = f" ({args.subsystem})" if args.subsystem else ""
        print(f"{args.kind} symbols{label}:")
        show_result(rows, ["name", "path", "line"])

    elif args.cmd == "summary":
        rows = file_summary(conn, args.file)
        print(f"Symbol summary for '{args.file}':")
        for row in rows:
            print(f"  {row['kind']:15s} {row['cnt']:>5d}")

    elif args.cmd == "stats":
        for row in conn.execute("SELECT kind, COUNT(*) as cnt FROM symbols GROUP BY kind ORDER BY cnt DESC"):
            print(f"  {row['kind']:15s} {row['cnt']:>6d}")
        total = conn.execute("SELECT COUNT(*) FROM symbols").fetchone()[0]
        files = conn.execute("SELECT COUNT(*) FROM files").fetchone()[0]
        print(f"  {'TOTAL':15s} {total:>6d}  ({files} files)")

    elif args.cmd == "callers":
        rows = conn.execute("""
            SELECT caller.name, f.path, cr.call_site_line
            FROM call_relations cr
            JOIN symbols caller ON cr.caller_id = caller.id
            JOIN symbols callee ON cr.callee_id = callee.id
            JOIN files f ON cr.call_site_file_id = f.id
            WHERE callee.name = ?
            ORDER BY caller.name, f.path, cr.call_site_line
        """, (args.name,)).fetchall()
        print(f"Callers of {args.name} ({len(rows)} found):")
        show_result(rows, ["name", "path", "call_site_line"])

    elif args.cmd == "callees":
        rows = conn.execute("""
            SELECT callee.name, f.path, cr.call_site_line
            FROM call_relations cr
            JOIN symbols caller ON cr.caller_id = caller.id
            JOIN symbols callee ON cr.callee_id = callee.id
            JOIN files f ON cr.call_site_file_id = f.id
            WHERE caller.name = ?
            ORDER BY callee.name, f.path, cr.call_site_line
        """, (args.name,)).fetchall()
        print(f"Callees of {args.name} ({len(rows)} found):")
        show_result(rows, ["name", "path", "call_site_line"])

    elif args.cmd == "callstats":
        total = conn.execute("SELECT COUNT(*) FROM call_relations").fetchone()[0]
        callers = conn.execute("SELECT COUNT(DISTINCT caller_id) FROM call_relations").fetchone()[0]
        callees = conn.execute("SELECT COUNT(DISTINCT callee_id) FROM call_relations").fetchone()[0]
        print(f"Call graph statistics:")
        print(f"  Total call relations:  {total}")
        print(f"  Unique callers:        {callers}")
        print(f"  Unique callees:        {callees}")

        print(f"\n  Most called (top 10):")
        for row in conn.execute("""
            SELECT s.name, COUNT(DISTINCT cr.caller_id) as callers
            FROM call_relations cr JOIN symbols s ON cr.callee_id = s.id
            GROUP BY s.name ORDER BY callers DESC LIMIT 10
        """):
            print(f"    {row['name']:40s} {row['callers']:>4d} callers")

        print(f"\n  Most calling (top 10):")
        for row in conn.execute("""
            SELECT s.name, COUNT(DISTINCT cr.callee_id) as callees
            FROM call_relations cr JOIN symbols s ON cr.caller_id = s.id
            GROUP BY cr.caller_id ORDER BY callees DESC LIMIT 10
        """):
            print(f"    {row['name']:40s} {row['callees']:>4d} callees")

    conn.close()


if __name__ == "__main__":
    main()
