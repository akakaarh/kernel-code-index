# drivers/mmc/core/mmc_test.c

Subsystem: drivers/mmc

## Functions (122)

### __mmc_test_cmds_during_tfr
- Return type: static int
- Signature: __mmc_test_cmds_during_tfr(struct mmc_test_card * test,unsigned long sz,int use_sbc,int write,int use_areq)
- Line: 2456

### __mmc_test_prepare
- Return type: static int
- Signature: __mmc_test_prepare(struct mmc_test_card * test,int write,int val)
- Line: 618

### __mmc_test_register_dbgfs_file
- Return type: static int
- Signature: __mmc_test_register_dbgfs_file(struct mmc_card * card,const char * name,umode_t mode,const struct file_operations * fops)
- Line: 3162

### mmc_test_align_multi_read
- Return type: static int
- Signature: mmc_test_align_multi_read(struct mmc_test_card * test)
- Line: 1218

### mmc_test_align_multi_write
- Return type: static int
- Signature: mmc_test_align_multi_write(struct mmc_test_card * test)
- Line: 1191

### mmc_test_align_read
- Return type: static int
- Signature: mmc_test_align_read(struct mmc_test_card * test)
- Line: 1176

### mmc_test_align_write
- Return type: static int
- Signature: mmc_test_align_write(struct mmc_test_card * test)
- Line: 1161

### mmc_test_alloc_mem
- Return type: static mmc_test_mem *
- Signature: mmc_test_alloc_mem(unsigned long min_sz,unsigned long max_sz,unsigned int max_segs,unsigned int max_seg_sz)
- Line: 333

### mmc_test_area_cleanup
- Return type: static int
- Signature: mmc_test_area_cleanup(struct mmc_test_card * test)
- Line: 1515

### mmc_test_area_erase
- Return type: static int
- Signature: mmc_test_area_erase(struct mmc_test_card * test)
- Line: 1501

### mmc_test_area_fill
- Return type: static int
- Signature: mmc_test_area_fill(struct mmc_test_card * test)
- Line: 1491

### mmc_test_area_init
- Return type: static int
- Signature: mmc_test_area_init(struct mmc_test_card * test,int erase,int fill)
- Line: 1533

### mmc_test_area_io
- Return type: static int
- Signature: mmc_test_area_io(struct mmc_test_card * test,unsigned long sz,unsigned int dev_addr,int write,int max_scatter,int timed)
- Line: 1480

### mmc_test_area_io_seq
- Return type: static int
- Signature: mmc_test_area_io_seq(struct mmc_test_card * test,unsigned long sz,unsigned int dev_addr,int write,int max_scatter,int timed,int count,bool nonblock,int min_sg_len)
- Line: 1429

### mmc_test_area_map
- Return type: static int
- Signature: mmc_test_area_map(struct mmc_test_card * test,unsigned long sz,int max_scatter,int min_sg_len,bool nonblock)
- Line: 1375

### mmc_test_area_prepare
- Return type: static int
- Signature: mmc_test_area_prepare(struct mmc_test_card * test)
- Line: 1611

### mmc_test_area_prepare_erase
- Return type: static int
- Signature: mmc_test_area_prepare_erase(struct mmc_test_card * test)
- Line: 1619

### mmc_test_area_prepare_fill
- Return type: static int
- Signature: mmc_test_area_prepare_fill(struct mmc_test_card * test)
- Line: 1627

### mmc_test_area_transfer
- Return type: static int
- Signature: mmc_test_area_transfer(struct mmc_test_card * test,unsigned int dev_addr,int write)
- Line: 1417

### mmc_test_basic_read
- Return type: static int
- Signature: mmc_test_basic_read(struct mmc_test_card * test)
- Line: 1015

### mmc_test_basic_write
- Return type: static int
- Signature: mmc_test_basic_write(struct mmc_test_card * test)
- Line: 1001

### mmc_test_best_performance
- Return type: static int
- Signature: mmc_test_best_performance(struct mmc_test_card * test,int write,int max_scatter)
- Line: 1640

### mmc_test_best_read_perf_max_scatter
- Return type: static int
- Signature: mmc_test_best_read_perf_max_scatter(struct mmc_test_card * test)
- Line: 1668

### mmc_test_best_read_performance
- Return type: static int
- Signature: mmc_test_best_read_performance(struct mmc_test_card * test)
- Line: 1652

### mmc_test_best_write_perf_max_scatter
- Return type: static int
- Signature: mmc_test_best_write_perf_max_scatter(struct mmc_test_card * test)
- Line: 1676

### mmc_test_best_write_performance
- Return type: static int
- Signature: mmc_test_best_write_performance(struct mmc_test_card * test)
- Line: 1660

### mmc_test_broken_transfer
- Return type: static int
- Signature: mmc_test_broken_transfer(struct mmc_test_card * test,unsigned blocks,unsigned blksz,int write)
- Line: 891

### mmc_test_buffer_transfer
- Return type: static int
- Signature: mmc_test_buffer_transfer(struct mmc_test_card * test,u8 * buffer,unsigned addr,unsigned blksz,int write)
- Line: 289

### mmc_test_busy
- Return type: static int
- Signature: mmc_test_busy(struct mmc_command * cmd)
- Line: 249

### mmc_test_capacity
- Return type: static unsigned int
- Signature: mmc_test_capacity(struct mmc_card * card)
- Line: 602

### mmc_test_check_broken_result
- Return type: static int
- Signature: mmc_test_check_broken_result(struct mmc_test_card * test,struct mmc_request * mrq)
- Line: 714

### mmc_test_check_result
- Return type: static int
- Signature: mmc_test_check_result(struct mmc_test_card * test,struct mmc_request * mrq)
- Line: 683

### mmc_test_cleanup
- Return type: static int
- Signature: mmc_test_cleanup(struct mmc_test_card * test)
- Line: 652

### mmc_test_cmds_during_read
- Return type: static int
- Signature: mmc_test_cmds_during_read(struct mmc_test_card * test)
- Line: 2498

### mmc_test_cmds_during_read_cmd23
- Return type: static int
- Signature: mmc_test_cmds_during_read_cmd23(struct mmc_test_card * test)
- Line: 2514

### mmc_test_cmds_during_read_cmd23_nonblock
- Return type: static int
- Signature: mmc_test_cmds_during_read_cmd23_nonblock(struct mmc_test_card * test)
- Line: 2530

### mmc_test_cmds_during_tfr
- Return type: static int
- Signature: mmc_test_cmds_during_tfr(struct mmc_test_card * test,int use_sbc,int write,int use_areq)
- Line: 2479

### mmc_test_cmds_during_write
- Return type: static int
- Signature: mmc_test_cmds_during_write(struct mmc_test_card * test)
- Line: 2506

### mmc_test_cmds_during_write_cmd23
- Return type: static int
- Signature: mmc_test_cmds_during_write_cmd23(struct mmc_test_card * test)
- Line: 2522

### mmc_test_cmds_during_write_cmd23_nonblock
- Return type: static int
- Signature: mmc_test_cmds_during_write_cmd23_nonblock(struct mmc_test_card * test)
- Line: 2538

### mmc_test_exit
- Return type: static void __exit
- Signature: mmc_test_exit(void)
- Line: 3261

### mmc_test_free_dbgfs_file
- Return type: static void
- Signature: mmc_test_free_dbgfs_file(struct mmc_card * card)
- Line: 3145

### mmc_test_free_mem
- Return type: static void
- Signature: mmc_test_free_mem(struct mmc_test_mem * mem)
- Line: 317

### mmc_test_free_result
- Return type: static void
- Signature: mmc_test_free_result(struct mmc_card * card)
- Line: 3016

### mmc_test_init
- Return type: static int __init
- Signature: mmc_test_init(void)
- Line: 3256

### mmc_test_large_seq_perf
- Return type: static int
- Signature: mmc_test_large_seq_perf(struct mmc_test_card * test,int write)
- Line: 2043

### mmc_test_large_seq_read_perf
- Return type: static int
- Signature: mmc_test_large_seq_read_perf(struct mmc_test_card * test)
- Line: 2069

### mmc_test_large_seq_write_perf
- Return type: static int
- Signature: mmc_test_large_seq_write_perf(struct mmc_test_card * test)
- Line: 2077

### mmc_test_map_sg
- Return type: static int
- Signature: mmc_test_map_sg(struct mmc_test_mem * mem,unsigned long size,struct scatterlist * sglist,int repeat,unsigned int max_segs,unsigned int max_seg_sz,unsigned int * sg_len,int min_sg_len)
- Line: 403

### mmc_test_map_sg_max_scatter
- Return type: static int
- Signature: mmc_test_map_sg_max_scatter(struct mmc_test_mem * mem,unsigned long sz,struct scatterlist * sglist,unsigned int max_segs,unsigned int max_seg_sz,unsigned int * sg_len)
- Line: 454

### mmc_test_multi_read
- Return type: static int
- Signature: mmc_test_multi_read(struct mmc_test_card * test)
- Line: 1068

### mmc_test_multi_read_high
- Return type: static int
- Signature: mmc_test_multi_read_high(struct mmc_test_card * test)
- Line: 1339

### mmc_test_multi_write
- Return type: static int
- Signature: mmc_test_multi_write(struct mmc_test_card * test)
- Line: 1047

### mmc_test_multi_write_high
- Return type: static int
- Signature: mmc_test_multi_write_high(struct mmc_test_card * test)
- Line: 1317

### mmc_test_multi_xfersize_read
- Return type: static int
- Signature: mmc_test_multi_xfersize_read(struct mmc_test_card * test)
- Line: 1281

### mmc_test_multi_xfersize_write
- Return type: static int
- Signature: mmc_test_multi_xfersize_write(struct mmc_test_card * test)
- Line: 1267

### mmc_test_no_highmem
- Return type: static int
- Signature: mmc_test_no_highmem(struct mmc_test_card * test)
- Line: 1363

### mmc_test_nonblock_transfer
- Return type: static int
- Signature: mmc_test_nonblock_transfer(struct mmc_test_card * test,unsigned int dev_addr,int write,int count)
- Line: 817

### mmc_test_ongoing_transfer
- Return type: static int
- Signature: mmc_test_ongoing_transfer(struct mmc_test_card * test,unsigned int dev_addr,int use_sbc,int repeat_cmd,int write,int use_areq)
- Line: 2342

### mmc_test_pow2_read
- Return type: static int
- Signature: mmc_test_pow2_read(struct mmc_test_card * test)
- Line: 1107

### mmc_test_pow2_write
- Return type: static int
- Signature: mmc_test_pow2_write(struct mmc_test_card * test)
- Line: 1089

### mmc_test_prepare_broken_mrq
- Return type: static void
- Signature: mmc_test_prepare_broken_mrq(struct mmc_test_card * test,struct mmc_request * mrq,int write)
- Line: 664

### mmc_test_prepare_mrq
- Return type: static void
- Signature: mmc_test_prepare_mrq(struct mmc_test_card * test,struct mmc_request * mrq,struct scatterlist * sg,unsigned sg_len,unsigned dev_addr,unsigned blocks,unsigned blksz,int write)
- Line: 209

### mmc_test_prepare_read
- Return type: static int
- Signature: mmc_test_prepare_read(struct mmc_test_card * test)
- Line: 647

### mmc_test_prepare_sbc
- Return type: static void
- Signature: mmc_test_prepare_sbc(struct mmc_test_card * test,struct mmc_request * mrq,unsigned int blocks)
- Line: 189

### mmc_test_prepare_write
- Return type: static int
- Signature: mmc_test_prepare_write(struct mmc_test_card * test)
- Line: 642

### mmc_test_print_avg_rate
- Return type: static void
- Signature: mmc_test_print_avg_rate(struct mmc_test_card * test,uint64_t bytes,unsigned int count,struct timespec64 * ts1,struct timespec64 * ts2)
- Line: 577

### mmc_test_print_rate
- Return type: static void
- Signature: mmc_test_print_rate(struct mmc_test_card * test,uint64_t bytes,struct timespec64 * ts1,struct timespec64 * ts2)
- Line: 553

### mmc_test_probe
- Return type: static int
- Signature: mmc_test_probe(struct mmc_card * card)
- Line: 3207

### mmc_test_profile_mult_read_blocking_perf
- Return type: static int
- Signature: mmc_test_profile_mult_read_blocking_perf(struct mmc_test_card * test)
- Line: 2206

### mmc_test_profile_mult_read_nonblock_perf
- Return type: static int
- Signature: mmc_test_profile_mult_read_nonblock_perf(struct mmc_test_card * test)
- Line: 2223

### mmc_test_profile_mult_write_blocking_perf
- Return type: static int
- Signature: mmc_test_profile_mult_write_blocking_perf(struct mmc_test_card * test)
- Line: 2172

### mmc_test_profile_mult_write_nonblock_perf
- Return type: static int
- Signature: mmc_test_profile_mult_write_nonblock_perf(struct mmc_test_card * test)
- Line: 2189

### mmc_test_profile_read_perf
- Return type: static int
- Signature: mmc_test_profile_read_perf(struct mmc_test_card * test)
- Line: 1684

### mmc_test_profile_seq_read_perf
- Return type: static int
- Signature: mmc_test_profile_seq_read_perf(struct mmc_test_card * test)
- Line: 1789

### mmc_test_profile_seq_trim_perf
- Return type: static int
- Signature: mmc_test_profile_seq_trim_perf(struct mmc_test_card * test)
- Line: 1849

### mmc_test_profile_seq_write_perf
- Return type: static int
- Signature: mmc_test_profile_seq_write_perf(struct mmc_test_card * test)
- Line: 1831

### mmc_test_profile_sglen_r_blocking_perf
- Return type: static int
- Signature: mmc_test_profile_sglen_r_blocking_perf(struct mmc_test_card * test)
- Line: 2274

### mmc_test_profile_sglen_r_nonblock_perf
- Return type: static int
- Signature: mmc_test_profile_sglen_r_nonblock_perf(struct mmc_test_card * test)
- Line: 2291

### mmc_test_profile_sglen_wr_blocking_perf
- Return type: static int
- Signature: mmc_test_profile_sglen_wr_blocking_perf(struct mmc_test_card * test)
- Line: 2240

### mmc_test_profile_sglen_wr_nonblock_perf
- Return type: static int
- Signature: mmc_test_profile_sglen_wr_nonblock_perf(struct mmc_test_card * test)
- Line: 2257

### mmc_test_profile_trim_perf
- Return type: static int
- Signature: mmc_test_profile_trim_perf(struct mmc_test_card * test)
- Line: 1732

### mmc_test_profile_write_perf
- Return type: static int
- Signature: mmc_test_profile_write_perf(struct mmc_test_card * test)
- Line: 1705

### mmc_test_random_perf
- Return type: static int
- Signature: mmc_test_random_perf(struct mmc_test_card * test,int write)
- Line: 1934

### mmc_test_random_read_perf
- Return type: static int
- Signature: mmc_test_random_read_perf(struct mmc_test_card * test)
- Line: 1983

### mmc_test_random_write_perf
- Return type: static int
- Signature: mmc_test_random_write_perf(struct mmc_test_card * test)
- Line: 1991

### mmc_test_rate
- Return type: static unsigned int
- Signature: mmc_test_rate(uint64_t bytes,struct timespec64 * ts)
- Line: 505

### mmc_test_read_high
- Return type: static int
- Signature: mmc_test_read_high(struct mmc_test_card * test)
- Line: 1307

### mmc_test_register_dbgfs_file
- Return type: static int
- Signature: mmc_test_register_dbgfs_file(struct mmc_card * card)
- Line: 3185

### mmc_test_remove
- Return type: static void
- Signature: mmc_test_remove(struct mmc_card * card)
- Line: 3237

### mmc_test_req_alloc
- Return type: static mmc_test_req *
- Signature: mmc_test_req_alloc(void)
- Line: 767

### mmc_test_req_reset
- Return type: static void
- Signature: mmc_test_req_reset(struct mmc_test_req * rq)
- Line: 758

### mmc_test_reset
- Return type: static int
- Signature: mmc_test_reset(struct mmc_test_card * test)
- Line: 2308

### mmc_test_retuning
- Return type: static int
- Signature: mmc_test_retuning(struct mmc_test_card * test)
- Line: 1969

### mmc_test_rnd_num
- Return type: static unsigned int
- Signature: mmc_test_rnd_num(unsigned int rnd_cnt)
- Line: 1888

### mmc_test_rnd_perf
- Return type: static int
- Signature: mmc_test_rnd_perf(struct mmc_test_card * test,int write,int print,unsigned long sz,int secs,int force_retuning)
- Line: 1897

### mmc_test_run
- Return type: static void
- Signature: mmc_test_run(struct mmc_test_card * test,int testcase)
- Line: 2926

### mmc_test_rw_multiple
- Return type: static int
- Signature: mmc_test_rw_multiple(struct mmc_test_card * test,struct mmc_test_multiple_rw * tdata,unsigned int reqsize,unsigned int size,int min_sg_len)
- Line: 2082

### mmc_test_rw_multiple_sg_len
- Return type: static int
- Signature: mmc_test_rw_multiple_sg_len(struct mmc_test_card * test,struct mmc_test_multiple_rw * rw)
- Line: 2154

### mmc_test_rw_multiple_size
- Return type: static int
- Signature: mmc_test_rw_multiple_size(struct mmc_test_card * test,struct mmc_test_multiple_rw * rw)
- Line: 2132

### mmc_test_save_transfer_result
- Return type: static void
- Signature: mmc_test_save_transfer_result(struct mmc_test_card * test,unsigned int count,unsigned int sectors,struct timespec64 ts,unsigned int rate,unsigned int iops)
- Line: 528

### mmc_test_send_status
- Return type: static int
- Signature: mmc_test_send_status(struct mmc_test_card * test,struct mmc_command * cmd)
- Line: 2329

### mmc_test_seq_perf
- Return type: static int
- Signature: mmc_test_seq_perf(struct mmc_test_card * test,int write,unsigned int tot_sz,int max_scatter)
- Line: 1996

### mmc_test_seq_read_perf
- Return type: static int
- Signature: mmc_test_seq_read_perf(struct mmc_test_card * test,unsigned long sz)
- Line: 1765

### mmc_test_seq_write_perf
- Return type: static int
- Signature: mmc_test_seq_write_perf(struct mmc_test_card * test,unsigned long sz)
- Line: 1804

### mmc_test_set_blksize
- Return type: static int
- Signature: mmc_test_set_blksize(struct mmc_test_card * test,unsigned size)
- Line: 184

### mmc_test_simple_transfer
- Return type: static int
- Signature: mmc_test_simple_transfer(struct mmc_test_card * test,struct scatterlist * sg,unsigned sg_len,unsigned dev_addr,unsigned blocks,unsigned blksz,int write)
- Line: 865

### mmc_test_start_areq
- Return type: static int
- Signature: mmc_test_start_areq(struct mmc_test_card * test,struct mmc_request * mrq,struct mmc_request * prev_mrq)
- Line: 782

### mmc_test_transfer
- Return type: static int
- Signature: mmc_test_transfer(struct mmc_test_card * test,struct scatterlist * sg,unsigned sg_len,unsigned dev_addr,unsigned blocks,unsigned blksz,int write)
- Line: 922

### mmc_test_verify_read
- Return type: static int
- Signature: mmc_test_verify_read(struct mmc_test_card * test)
- Line: 1038

### mmc_test_verify_write
- Return type: static int
- Signature: mmc_test_verify_write(struct mmc_test_card * test)
- Line: 1029

### mmc_test_wait_busy
- Return type: static int
- Signature: mmc_test_wait_busy(struct mmc_test_card * test)
- Line: 258

### mmc_test_wait_done
- Return type: static void
- Signature: mmc_test_wait_done(struct mmc_request * mrq)
- Line: 777

### mmc_test_weird_read
- Return type: static int
- Signature: mmc_test_weird_read(struct mmc_test_card * test)
- Line: 1143

### mmc_test_weird_write
- Return type: static int
- Signature: mmc_test_weird_write(struct mmc_test_card * test)
- Line: 1125

### mmc_test_write_high
- Return type: static int
- Signature: mmc_test_write_high(struct mmc_test_card * test)
- Line: 1297

### mmc_test_xfersize_read
- Return type: static int
- Signature: mmc_test_xfersize_read(struct mmc_test_card * test)
- Line: 1256

### mmc_test_xfersize_write
- Return type: static int
- Signature: mmc_test_xfersize_write(struct mmc_test_card * test)
- Line: 1245

### mtf_test_open
- Return type: static int
- Signature: mtf_test_open(struct inode * inode,struct file * file)
- Line: 3069

### mtf_test_show
- Return type: static int
- Signature: mtf_test_show(struct seq_file * sf,void * data)
- Line: 3042

### mtf_test_write
- Return type: static ssize_t
- Signature: mtf_test_write(struct file * file,const char __user * buf,size_t count,loff_t * pos)
- Line: 3074

### mtf_testlist_show
- Return type: static int
- Signature: mtf_testlist_show(struct seq_file * sf,void * data)
- Line: 3128

## Structs (10)

### mmc_test_area
- Line: 75
- Members:
  - page: page *
  - order: unsigned int
  - cnt: unsigned int
  - max_sz: unsigned long
  - dev_addr: unsigned int
  - max_tfr: unsigned int
  - max_segs: unsigned int
  - max_seg_sz: unsigned int
  - blocks: unsigned int
  - sg_len: unsigned int
  - mem: mmc_test_mem *
  - sg: scatterlist *
  - sg_areq: scatterlist *
  - link: list_head
  - count: unsigned int
  - sectors: unsigned int
  - ts: timespec64
  - rate: unsigned int
  - iops: unsigned int
  - link: list_head
  - card: mmc_card *
  - testcase: int
  - result: int
  - tr_lst: list_head
  - link: list_head
  - card: mmc_card *
  - file: dentry *
  - card: mmc_card *
  - scratch: u8[]
  - highmem: page *
  - area: mmc_test_area
  - gr: mmc_test_general_result *
  - buffer: u8[]
  - sg_len: unsigned int *
  - bs: unsigned int *
  - len: unsigned int
  - size: unsigned int
  - do_write: bool
  - do_nonblock_req: bool
  - prepare: mmc_test_prep_media
  - mrq: mmc_request
  - sbc: mmc_command
  - cmd: mmc_command
  - stop: mmc_command
  - status: mmc_command
  - data: mmc_data
  - name: const char *
  - prepare: int (*)(struct mmc_test_card *)
  - run: int (*)(struct mmc_test_card *)
  - cleanup: int (*)(struct mmc_test_card *)

### mmc_test_card
- Line: 143
- Members:
  - page: page *
  - order: unsigned int
  - cnt: unsigned int
  - max_sz: unsigned long
  - dev_addr: unsigned int
  - max_tfr: unsigned int
  - max_segs: unsigned int
  - max_seg_sz: unsigned int
  - blocks: unsigned int
  - sg_len: unsigned int
  - mem: mmc_test_mem *
  - sg: scatterlist *
  - sg_areq: scatterlist *
  - link: list_head
  - count: unsigned int
  - sectors: unsigned int
  - ts: timespec64
  - rate: unsigned int
  - iops: unsigned int
  - link: list_head
  - card: mmc_card *
  - testcase: int
  - result: int
  - tr_lst: list_head
  - link: list_head
  - card: mmc_card *
  - file: dentry *
  - card: mmc_card *
  - scratch: u8[]
  - highmem: page *
  - area: mmc_test_area
  - gr: mmc_test_general_result *
  - buffer: u8[]
  - sg_len: unsigned int *
  - bs: unsigned int *
  - len: unsigned int
  - size: unsigned int
  - do_write: bool
  - do_nonblock_req: bool
  - prepare: mmc_test_prep_media
  - mrq: mmc_request
  - sbc: mmc_command
  - cmd: mmc_command
  - stop: mmc_command
  - status: mmc_command
  - data: mmc_data
  - name: const char *
  - prepare: int (*)(struct mmc_test_card *)
  - run: int (*)(struct mmc_test_card *)
  - cleanup: int (*)(struct mmc_test_card *)

### mmc_test_case
- Line: 993
- Members:
  - page: page *
  - order: unsigned int
  - cnt: unsigned int
  - max_sz: unsigned long
  - dev_addr: unsigned int
  - max_tfr: unsigned int
  - max_segs: unsigned int
  - max_seg_sz: unsigned int
  - blocks: unsigned int
  - sg_len: unsigned int
  - mem: mmc_test_mem *
  - sg: scatterlist *
  - sg_areq: scatterlist *
  - link: list_head
  - count: unsigned int
  - sectors: unsigned int
  - ts: timespec64
  - rate: unsigned int
  - iops: unsigned int
  - link: list_head
  - card: mmc_card *
  - testcase: int
  - result: int
  - tr_lst: list_head
  - link: list_head
  - card: mmc_card *
  - file: dentry *
  - card: mmc_card *
  - scratch: u8[]
  - highmem: page *
  - area: mmc_test_area
  - gr: mmc_test_general_result *
  - buffer: u8[]
  - sg_len: unsigned int *
  - bs: unsigned int *
  - len: unsigned int
  - size: unsigned int
  - do_write: bool
  - do_nonblock_req: bool
  - prepare: mmc_test_prep_media
  - mrq: mmc_request
  - sbc: mmc_command
  - cmd: mmc_command
  - stop: mmc_command
  - status: mmc_command
  - data: mmc_data
  - name: const char *
  - prepare: int (*)(struct mmc_test_card *)
  - run: int (*)(struct mmc_test_card *)
  - cleanup: int (*)(struct mmc_test_card *)

### mmc_test_dbgfs_file
- Line: 128
- Members:
  - page: page *
  - order: unsigned int
  - cnt: unsigned int
  - max_sz: unsigned long
  - dev_addr: unsigned int
  - max_tfr: unsigned int
  - max_segs: unsigned int
  - max_seg_sz: unsigned int
  - blocks: unsigned int
  - sg_len: unsigned int
  - mem: mmc_test_mem *
  - sg: scatterlist *
  - sg_areq: scatterlist *
  - link: list_head
  - count: unsigned int
  - sectors: unsigned int
  - ts: timespec64
  - rate: unsigned int
  - iops: unsigned int
  - link: list_head
  - card: mmc_card *
  - testcase: int
  - result: int
  - tr_lst: list_head
  - link: list_head
  - card: mmc_card *
  - file: dentry *
  - card: mmc_card *
  - scratch: u8[]
  - highmem: page *
  - area: mmc_test_area
  - gr: mmc_test_general_result *
  - buffer: u8[]
  - sg_len: unsigned int *
  - bs: unsigned int *
  - len: unsigned int
  - size: unsigned int
  - do_write: bool
  - do_nonblock_req: bool
  - prepare: mmc_test_prep_media
  - mrq: mmc_request
  - sbc: mmc_command
  - cmd: mmc_command
  - stop: mmc_command
  - status: mmc_command
  - data: mmc_data
  - name: const char *
  - prepare: int (*)(struct mmc_test_card *)
  - run: int (*)(struct mmc_test_card *)
  - cleanup: int (*)(struct mmc_test_card *)

### mmc_test_general_result
- Line: 114
- Members:
  - page: page *
  - order: unsigned int
  - cnt: unsigned int
  - max_sz: unsigned long
  - dev_addr: unsigned int
  - max_tfr: unsigned int
  - max_segs: unsigned int
  - max_seg_sz: unsigned int
  - blocks: unsigned int
  - sg_len: unsigned int
  - mem: mmc_test_mem *
  - sg: scatterlist *
  - sg_areq: scatterlist *
  - link: list_head
  - count: unsigned int
  - sectors: unsigned int
  - ts: timespec64
  - rate: unsigned int
  - iops: unsigned int
  - link: list_head
  - card: mmc_card *
  - testcase: int
  - result: int
  - tr_lst: list_head
  - link: list_head
  - card: mmc_card *
  - file: dentry *
  - card: mmc_card *
  - scratch: u8[]
  - highmem: page *
  - area: mmc_test_area
  - gr: mmc_test_general_result *
  - buffer: u8[]
  - sg_len: unsigned int *
  - bs: unsigned int *
  - len: unsigned int
  - size: unsigned int
  - do_write: bool
  - do_nonblock_req: bool
  - prepare: mmc_test_prep_media
  - mrq: mmc_request
  - sbc: mmc_command
  - cmd: mmc_command
  - stop: mmc_command
  - status: mmc_command
  - data: mmc_data
  - name: const char *
  - prepare: int (*)(struct mmc_test_card *)
  - run: int (*)(struct mmc_test_card *)
  - cleanup: int (*)(struct mmc_test_card *)

### mmc_test_mem
- Line: 57
- Members:
  - page: page *
  - order: unsigned int
  - cnt: unsigned int
  - max_sz: unsigned long
  - dev_addr: unsigned int
  - max_tfr: unsigned int
  - max_segs: unsigned int
  - max_seg_sz: unsigned int
  - blocks: unsigned int
  - sg_len: unsigned int
  - mem: mmc_test_mem *
  - sg: scatterlist *
  - sg_areq: scatterlist *
  - link: list_head
  - count: unsigned int
  - sectors: unsigned int
  - ts: timespec64
  - rate: unsigned int
  - iops: unsigned int
  - link: list_head
  - card: mmc_card *
  - testcase: int
  - result: int
  - tr_lst: list_head
  - link: list_head
  - card: mmc_card *
  - file: dentry *
  - card: mmc_card *
  - scratch: u8[]
  - highmem: page *
  - area: mmc_test_area
  - gr: mmc_test_general_result *
  - buffer: u8[]
  - sg_len: unsigned int *
  - bs: unsigned int *
  - len: unsigned int
  - size: unsigned int
  - do_write: bool
  - do_nonblock_req: bool
  - prepare: mmc_test_prep_media
  - mrq: mmc_request
  - sbc: mmc_command
  - cmd: mmc_command
  - stop: mmc_command
  - status: mmc_command
  - data: mmc_data
  - name: const char *
  - prepare: int (*)(struct mmc_test_card *)
  - run: int (*)(struct mmc_test_card *)
  - cleanup: int (*)(struct mmc_test_card *)

### mmc_test_multiple_rw
- Line: 162
- Members:
  - page: page *
  - order: unsigned int
  - cnt: unsigned int
  - max_sz: unsigned long
  - dev_addr: unsigned int
  - max_tfr: unsigned int
  - max_segs: unsigned int
  - max_seg_sz: unsigned int
  - blocks: unsigned int
  - sg_len: unsigned int
  - mem: mmc_test_mem *
  - sg: scatterlist *
  - sg_areq: scatterlist *
  - link: list_head
  - count: unsigned int
  - sectors: unsigned int
  - ts: timespec64
  - rate: unsigned int
  - iops: unsigned int
  - link: list_head
  - card: mmc_card *
  - testcase: int
  - result: int
  - tr_lst: list_head
  - link: list_head
  - card: mmc_card *
  - file: dentry *
  - card: mmc_card *
  - scratch: u8[]
  - highmem: page *
  - area: mmc_test_area
  - gr: mmc_test_general_result *
  - buffer: u8[]
  - sg_len: unsigned int *
  - bs: unsigned int *
  - len: unsigned int
  - size: unsigned int
  - do_write: bool
  - do_nonblock_req: bool
  - prepare: mmc_test_prep_media
  - mrq: mmc_request
  - sbc: mmc_command
  - cmd: mmc_command
  - stop: mmc_command
  - status: mmc_command
  - data: mmc_data
  - name: const char *
  - prepare: int (*)(struct mmc_test_card *)
  - run: int (*)(struct mmc_test_card *)
  - cleanup: int (*)(struct mmc_test_card *)

### mmc_test_pages
- Line: 47
- Members:
  - page: page *
  - order: unsigned int
  - cnt: unsigned int
  - max_sz: unsigned long
  - dev_addr: unsigned int
  - max_tfr: unsigned int
  - max_segs: unsigned int
  - max_seg_sz: unsigned int
  - blocks: unsigned int
  - sg_len: unsigned int
  - mem: mmc_test_mem *
  - sg: scatterlist *
  - sg_areq: scatterlist *
  - link: list_head
  - count: unsigned int
  - sectors: unsigned int
  - ts: timespec64
  - rate: unsigned int
  - iops: unsigned int
  - link: list_head
  - card: mmc_card *
  - testcase: int
  - result: int
  - tr_lst: list_head
  - link: list_head
  - card: mmc_card *
  - file: dentry *
  - card: mmc_card *
  - scratch: u8[]
  - highmem: page *
  - area: mmc_test_area
  - gr: mmc_test_general_result *
  - buffer: u8[]
  - sg_len: unsigned int *
  - bs: unsigned int *
  - len: unsigned int
  - size: unsigned int
  - do_write: bool
  - do_nonblock_req: bool
  - prepare: mmc_test_prep_media
  - mrq: mmc_request
  - sbc: mmc_command
  - cmd: mmc_command
  - stop: mmc_command
  - status: mmc_command
  - data: mmc_data
  - name: const char *
  - prepare: int (*)(struct mmc_test_card *)
  - run: int (*)(struct mmc_test_card *)
  - cleanup: int (*)(struct mmc_test_card *)

### mmc_test_req
- Line: 746
- Members:
  - page: page *
  - order: unsigned int
  - cnt: unsigned int
  - max_sz: unsigned long
  - dev_addr: unsigned int
  - max_tfr: unsigned int
  - max_segs: unsigned int
  - max_seg_sz: unsigned int
  - blocks: unsigned int
  - sg_len: unsigned int
  - mem: mmc_test_mem *
  - sg: scatterlist *
  - sg_areq: scatterlist *
  - link: list_head
  - count: unsigned int
  - sectors: unsigned int
  - ts: timespec64
  - rate: unsigned int
  - iops: unsigned int
  - link: list_head
  - card: mmc_card *
  - testcase: int
  - result: int
  - tr_lst: list_head
  - link: list_head
  - card: mmc_card *
  - file: dentry *
  - card: mmc_card *
  - scratch: u8[]
  - highmem: page *
  - area: mmc_test_area
  - gr: mmc_test_general_result *
  - buffer: u8[]
  - sg_len: unsigned int *
  - bs: unsigned int *
  - len: unsigned int
  - size: unsigned int
  - do_write: bool
  - do_nonblock_req: bool
  - prepare: mmc_test_prep_media
  - mrq: mmc_request
  - sbc: mmc_command
  - cmd: mmc_command
  - stop: mmc_command
  - status: mmc_command
  - data: mmc_data
  - name: const char *
  - prepare: int (*)(struct mmc_test_card *)
  - run: int (*)(struct mmc_test_card *)
  - cleanup: int (*)(struct mmc_test_card *)

### mmc_test_transfer_result
- Line: 97
- Members:
  - page: page *
  - order: unsigned int
  - cnt: unsigned int
  - max_sz: unsigned long
  - dev_addr: unsigned int
  - max_tfr: unsigned int
  - max_segs: unsigned int
  - max_seg_sz: unsigned int
  - blocks: unsigned int
  - sg_len: unsigned int
  - mem: mmc_test_mem *
  - sg: scatterlist *
  - sg_areq: scatterlist *
  - link: list_head
  - count: unsigned int
  - sectors: unsigned int
  - ts: timespec64
  - rate: unsigned int
  - iops: unsigned int
  - link: list_head
  - card: mmc_card *
  - testcase: int
  - result: int
  - tr_lst: list_head
  - link: list_head
  - card: mmc_card *
  - file: dentry *
  - card: mmc_card *
  - scratch: u8[]
  - highmem: page *
  - area: mmc_test_area
  - gr: mmc_test_general_result *
  - buffer: u8[]
  - sg_len: unsigned int *
  - bs: unsigned int *
  - len: unsigned int
  - size: unsigned int
  - do_write: bool
  - do_nonblock_req: bool
  - prepare: mmc_test_prep_media
  - mrq: mmc_request
  - sbc: mmc_command
  - cmd: mmc_command
  - stop: mmc_command
  - status: mmc_command
  - data: mmc_data
  - name: const char *
  - prepare: int (*)(struct mmc_test_card *)
  - run: int (*)(struct mmc_test_card *)
  - cleanup: int (*)(struct mmc_test_card *)

## Enums (1)

### mmc_test_prep_media
- Line: 156

## Variables (6)

- static **bs** : unsigned int[] (line 172)
- static **mmc_driver** : mmc_driver (line 3248)
- static **mmc_test_cases** : const struct mmc_test_case[] (line 2543)
- static **mmc_test_fops_test** : const struct file_operations (line 3120)
- static **rnd_next** : unsigned int (line 1886)
- static **sg_len** : unsigned int[] (line 175)

## Macros (8)

- **BUFFER_ORDER** (line 31)
- **BUFFER_SIZE** (line 32)
- **RESULT_FAIL** (line 27)
- **RESULT_OK** (line 26)
- **RESULT_UNSUP_CARD** (line 29)
- **RESULT_UNSUP_HOST** (line 28)
- **TEST_ALIGN_END** (line 34)
- **TEST_AREA_MAX_SIZE** (line 40)
