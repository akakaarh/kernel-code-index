"""Export kernel symbols to markdown files for qmd vector indexing.

Each source file gets one .md with structured descriptions of all its symbols,
including call graph relationships.
"""

import sqlite3
import sys
from collections import defaultdict
from pathlib import Path

DB_PATH = Path(__file__).parent / "kernel_index.db"
OUTPUT_DIR = Path(__file__).parent / "symbol-docs"

KIND_ORDER = ["function", "struct", "enum", "union", "typedef", "variable", "macro", "enumerator", "member"]


def clean_typeref(typeref: str) -> str:
    """Remove ctags typeref prefixes like 'typename:' and 'struct:'."""
    if not typeref:
        return ""
    for prefix in ("typename:", "struct:", "union:", "enum:"):
        if typeref.startswith(prefix):
            return typeref[len(prefix):]
    return typeref


def get_conn(db_path: Path = DB_PATH) -> sqlite3.Connection:
    conn = sqlite3.connect(str(db_path))
    conn.row_factory = sqlite3.Row
    return conn


def build_call_maps(conn):
    """Build caller->callees and callee->callers maps."""
    rows = conn.execute("""
        SELECT caller.name AS caller, callee.name AS callee, f.path, cr.call_site_line
        FROM call_relations cr
        JOIN symbols caller ON cr.caller_id = caller.id
        JOIN symbols callee ON cr.callee_id = callee.id
        JOIN files f ON cr.call_site_file_id = f.id
    """).fetchall()

    callees_of = defaultdict(set)  # caller_name -> {callee_name, ...}
    callers_of = defaultdict(set)  # callee_name -> {caller_name, ...}

    for r in rows:
        callees_of[r["caller"]].add(r["callee"])
        callers_of[r["callee"]].add(r["caller"])

    return callees_of, callers_of


def build_member_map(conn):
    """Build struct/union -> members map from ctags member kind."""
    rows = conn.execute("""
        SELECT s.name AS struct_name, m.name AS member_name, m.typeref, m.line
        FROM symbols m
        JOIN symbols s ON m.file_id = s.file_id AND s.kind IN ('struct', 'union')
        WHERE m.kind = 'member'
        ORDER BY s.name, m.line
    """).fetchall()

    # Simple heuristic: associate members with the nearest preceding struct/union
    # This is imperfect but works for ctags output where members follow their struct
    struct_members = defaultdict(list)
    for r in rows:
        struct_members[r["struct_name"]].append({
            "name": r["member_name"],
            "typeref": r["typeref"] or "",
            "line": r["line"],
        })

    return struct_members


def generate_file_markdown(file_path, subsystem, symbols, callees_of, callers_of, struct_members):
    """Generate markdown content for a single source file."""
    lines = []
    lines.append(f"# {file_path}")
    lines.append("")
    lines.append(f"Subsystem: {subsystem}")
    lines.append("")

    # Group symbols by kind
    by_kind = defaultdict(list)
    for sym in symbols:
        by_kind[sym["kind"]].append(sym)

    # Functions section
    funcs = by_kind.get("function", [])
    if funcs:
        lines.append(f"## Functions ({len(funcs)})")
        lines.append("")
        for sym in sorted(funcs, key=lambda s: s["name"]):
            name = sym["name"]
            ret = clean_typeref(sym["typeref"]) or "void"
            sig = sym["signature"] or "()"
            static = "static " if sym["is_static"] else ""
            lines.append(f"### {name}")
            lines.append(f"- Return type: {static}{ret}")
            lines.append(f"- Signature: {name}{sig}")
            lines.append(f"- Line: {sym['line']}")

            callees = sorted(callees_of.get(name, set()))
            if callees:
                lines.append(f"- Calls: {', '.join(callees)}")

            callers = sorted(callers_of.get(name, set()))
            if callers:
                lines.append(f"- Called by: {', '.join(callers)}")

            lines.append("")

    # Structs section
    structs = by_kind.get("struct", [])
    if structs:
        lines.append(f"## Structs ({len(structs)})")
        lines.append("")
        for sym in sorted(structs, key=lambda s: s["name"]):
            name = sym["name"]
            lines.append(f"### {name}")
            lines.append(f"- Line: {sym['line']}")
            members = struct_members.get(name, [])
            if members:
                lines.append("- Members:")
                for m in members:
                    typ = f": {clean_typeref(m['typeref'])}" if m['typeref'] else ""
                    lines.append(f"  - {m['name']}{typ}")
            lines.append("")

    # Enums section
    enums = by_kind.get("enum", [])
    if enums:
        lines.append(f"## Enums ({len(enums)})")
        lines.append("")
        for sym in sorted(enums, key=lambda s: s["name"]):
            lines.append(f"### {sym['name']}")
            lines.append(f"- Line: {sym['line']}")
            # Find enumerators belonging to this enum
            enumerators = [e for e in by_kind.get("enumerator", []) if (e["typeref"] or "").endswith(sym["name"])]
            if enumerators:
                lines.append("- Values:")
                for e in enumerators:
                    lines.append(f"  - {e['name']}")
            lines.append("")

    # Unions section
    unions = by_kind.get("union", [])
    if unions:
        lines.append(f"## Unions ({len(unions)})")
        lines.append("")
        for sym in sorted(unions, key=lambda s: s["name"]):
            lines.append(f"### {sym['name']}")
            lines.append(f"- Line: {sym['line']}")
            members = struct_members.get(sym["name"], [])
            if members:
                lines.append("- Members:")
                for m in members:
                    typ = f": {clean_typeref(m['typeref'])}" if m['typeref'] else ""
                    lines.append(f"  - {m['name']}{typ}")
            lines.append("")

    # Typedefs section
    typedefs = by_kind.get("typedef", [])
    if typedefs:
        lines.append(f"## Typedefs ({len(typedefs)})")
        lines.append("")
        for sym in sorted(typedefs, key=lambda s: s["name"]):
            ref = clean_typeref(sym["typeref"])
            lines.append(f"- **{sym['name']}** → {ref} (line {sym['line']})")
        lines.append("")

    # Variables section
    variables = by_kind.get("variable", [])
    if variables:
        lines.append(f"## Variables ({len(variables)})")
        lines.append("")
        for sym in sorted(variables, key=lambda s: s["name"]):
            static = "static " if sym["is_static"] else ""
            ref = clean_typeref(sym["typeref"])
            lines.append(f"- {static}**{sym['name']}** : {ref} (line {sym['line']})")
        lines.append("")

    # Macros section
    macros = by_kind.get("macro", [])
    if macros:
        lines.append(f"## Macros ({len(macros)})")
        lines.append("")
        for sym in sorted(macros, key=lambda s: s["name"]):
            sig = sym["signature"] or ""
            lines.append(f"- **{sym['name']}**{sig} (line {sym['line']})")
        lines.append("")

    return "\n".join(lines)


def export(db_path: Path = DB_PATH, output_dir: Path = OUTPUT_DIR):
    """Main export function."""
    conn = get_conn(db_path)

    print("[*] Building call graph maps...")
    callees_of, callers_of = build_call_maps(conn)

    print("[*] Building member maps...")
    struct_members = build_member_map(conn)

    # Get all files
    files = conn.execute("SELECT id, path, subsystem FROM files ORDER BY path").fetchall()
    print(f"[*] Found {len(files)} files to export")

    # Get all symbols grouped by file_id
    symbols_by_file = defaultdict(list)
    symbols = conn.execute(
        "SELECT name, kind, file_id, line, typeref, signature, is_static FROM symbols ORDER BY file_id, kind, name"
    ).fetchall()
    for sym in symbols:
        symbols_by_file[sym["file_id"]].append(sym)

    # Create output directory
    output_dir.mkdir(parents=True, exist_ok=True)

    total_files = 0
    total_symbols = 0

    for f in files:
        file_path = f["path"]
        subsystem = f["subsystem"] or ""
        syms = symbols_by_file.get(f["id"], [])

        if not syms:
            continue

        # Generate filename: drivers/gpio/gpiolib.c -> drivers_gpio_gpiolib.c.md
        doc_name = file_path.replace("/", "_").replace("\\", "_") + ".md"
        doc_path = output_dir / doc_name

        content = generate_file_markdown(
            file_path, subsystem, syms, callees_of, callers_of, struct_members
        )
        doc_path.write_text(content, encoding="utf-8")

        total_files += 1
        total_symbols += len(syms)

    conn.close()

    print(f"\n[===] Export Summary ===")
    print(f"  Files exported:  {total_files}")
    print(f"  Symbols written: {total_symbols}")
    print(f"  Output dir:      {output_dir}")

    return total_files, total_symbols


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Export kernel symbols to markdown")
    parser.add_argument("--db", default=str(DB_PATH), help="SQLite database path")
    parser.add_argument("--output", default=str(OUTPUT_DIR), help="Output directory")
    args = parser.parse_args()

    export(Path(args.db), Path(args.output))
