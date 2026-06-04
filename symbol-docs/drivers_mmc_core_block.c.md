# drivers/mmc/core/block.c

Subsystem: drivers/mmc

## Functions (113)

### __mmc_blk_ioctl_cmd
- Return type: static int
- Signature: __mmc_blk_ioctl_cmd(struct mmc_card * card,struct mmc_blk_data * md,struct mmc_blk_ioc_data ** idatas,int i)
- Line: 480

### _mmc_blk_suspend
- Return type: static int
- Signature: _mmc_blk_suspend(struct mmc_card * card)
- Line: 3280

### alloc_idata
- Return type: static mmc_blk_ioc_data **
- Signature: alloc_idata(struct mmc_rpmb_data * rpmb,unsigned int cmd_count)
- Line: 2733

### force_ro_show
- Return type: static ssize_t
- Signature: force_ro_show(struct device * dev,struct device_attribute * attr,char * buf)
- Line: 302

### force_ro_store
- Return type: static ssize_t
- Signature: force_ro_store(struct device * dev,struct device_attribute * attr,const char * buf,size_t count)
- Line: 315

### free_idata
- Return type: static void
- Signature: free_idata(struct mmc_blk_ioc_data ** idata,unsigned int cmd_count)
- Line: 2724

### mmc_apply_rel_rw
- Return type: static void
- Signature: mmc_apply_rel_rw(struct mmc_blk_request * brq,struct mmc_card * card,struct request * req)
- Line: 1316

### mmc_blk_add_debugfs
- Return type: static void
- Signature: mmc_blk_add_debugfs(struct mmc_card * card,struct mmc_blk_data * md)
- Line: 3118

### mmc_blk_add_debugfs
- Return type: static void
- Signature: mmc_blk_add_debugfs(struct mmc_card * card,struct mmc_blk_data * md)
- Line: 3156

### mmc_blk_alloc
- Return type: static mmc_blk_data *
- Signature: mmc_blk_alloc(struct mmc_card * card)
- Line: 2599

### mmc_blk_alloc_part
- Return type: static int
- Signature: mmc_blk_alloc_part(struct mmc_card * card,struct mmc_blk_data * md,unsigned int part_type,sector_t size,bool default_ro,const char * subname,int area_type)
- Line: 2622

### mmc_blk_alloc_parts
- Return type: static int
- Signature: mmc_blk_alloc_parts(struct mmc_card * card,struct mmc_blk_data * md)
- Line: 2945

### mmc_blk_alloc_req
- Return type: static mmc_blk_data *
- Signature: mmc_blk_alloc_req(struct mmc_card * card,struct device * parent,sector_t size,bool default_ro,const char * subname,int area_type,unsigned int part_type)
- Line: 2477

### mmc_blk_alloc_rpmb_part
- Return type: static int
- Signature: mmc_blk_alloc_rpmb_part(struct mmc_card * card,struct mmc_blk_data * md,unsigned int part_index,sector_t size,const char * subname)
- Line: 2871

### mmc_blk_alternative_gpt_sector
- Return type: static int
- Signature: mmc_blk_alternative_gpt_sector(struct gendisk * disk,sector_t * sector)
- Line: 851

### mmc_blk_busy_cb
- Return type: static int
- Signature: mmc_blk_busy_cb(void * cb_data,bool * busy)
- Line: 1954

### mmc_blk_card_busy
- Return type: static int
- Signature: mmc_blk_card_busy(struct mmc_card * card,struct request * req)
- Line: 1971

### mmc_blk_check_blkdev
- Return type: static int
- Signature: mmc_blk_check_blkdev(struct block_device * bdev)
- Line: 795

### mmc_blk_check_sbc
- Return type: static void
- Signature: mmc_blk_check_sbc(struct mmc_queue_req * mq_rq)
- Line: 1083

### mmc_blk_clock_khz
- Return type: static unsigned int
- Signature: mmc_blk_clock_khz(struct mmc_host * host)
- Line: 1015

### mmc_blk_cmd_started
- Return type: static bool
- Signature: mmc_blk_cmd_started(struct mmc_blk_request * brq)
- Line: 1816

### mmc_blk_compat_ioctl
- Return type: static int
- Signature: mmc_blk_compat_ioctl(struct block_device * bdev,blk_mode_t mode,unsigned int cmd,unsigned long arg)
- Line: 844

### mmc_blk_cqe_complete_rq
- Return type: static void
- Signature: mmc_blk_cqe_complete_rq(struct mmc_queue * mq,struct request * req)
- Line: 1525

### mmc_blk_cqe_issue_flush
- Return type: static int
- Signature: mmc_blk_cqe_issue_flush(struct mmc_queue * mq,struct request * req)
- Line: 1635

### mmc_blk_cqe_issue_rw_rq
- Return type: static int
- Signature: mmc_blk_cqe_issue_rw_rq(struct mmc_queue * mq,struct request * req)
- Line: 1667

### mmc_blk_cqe_prep_dcmd
- Return type: static mmc_request *
- Signature: mmc_blk_cqe_prep_dcmd(struct mmc_queue_req * mqrq,struct request * req)
- Line: 1622

### mmc_blk_cqe_recovery
- Return type: void
- Signature: mmc_blk_cqe_recovery(struct mmc_queue * mq)
- Line: 1580

### mmc_blk_cqe_req_done
- Return type: static void
- Signature: mmc_blk_cqe_req_done(struct mmc_request * mrq)
- Line: 1596

### mmc_blk_cqe_start_req
- Return type: static int
- Signature: mmc_blk_cqe_start_req(struct mmc_host * host,struct mmc_request * mrq)
- Line: 1614

### mmc_blk_data_prep
- Return type: static void
- Signature: mmc_blk_data_prep(struct mmc_queue * mq,struct mmc_queue_req * mqrq,int recovery_mode,bool * do_rel_wr_p,bool * do_data_tag_p)
- Line: 1386

### mmc_blk_data_timeout_ms
- Return type: static unsigned int
- Signature: mmc_blk_data_timeout_ms(struct mmc_host * host,struct mmc_data * data)
- Line: 1029

### mmc_blk_eval_resp_error
- Return type: static void
- Signature: mmc_blk_eval_resp_error(struct mmc_blk_request * brq)
- Line: 1344

### mmc_blk_exit
- Return type: static void __exit
- Signature: mmc_blk_exit(void)
- Line: 3376

### mmc_blk_fix_state
- Return type: static int
- Signature: mmc_blk_fix_state(struct mmc_card * card,struct request * req)
- Line: 1766

### mmc_blk_get
- Return type: static mmc_blk_data *
- Signature: mmc_blk_get(struct gendisk * disk)
- Line: 193

### mmc_blk_get_partitions_node
- Return type: static fwnode_handle *
- Signature: mmc_blk_get_partitions_node(struct device * mmc_dev,const char * subname)
- Line: 2444

### mmc_blk_getgeo
- Return type: static int
- Signature: mmc_blk_getgeo(struct gendisk * disk,struct hd_geometry * geo)
- Line: 400

### mmc_blk_hsq_issue_rw_rq
- Return type: static int
- Signature: mmc_blk_hsq_issue_rw_rq(struct mmc_queue * mq,struct request * req)
- Line: 1650

### mmc_blk_hsq_req_done
- Return type: static void
- Signature: mmc_blk_hsq_req_done(struct mmc_request * mrq)
- Line: 2053

### mmc_blk_init
- Return type: static int __init
- Signature: mmc_blk_init(void)
- Line: 3337

### mmc_blk_ioctl
- Return type: static int
- Signature: mmc_blk_ioctl(struct block_device * bdev,blk_mode_t mode,unsigned int cmd,unsigned long arg)
- Line: 807

### mmc_blk_ioctl_cmd
- Return type: static int
- Signature: mmc_blk_ioctl_cmd(struct mmc_blk_data * md,struct mmc_ioc_cmd __user * ic_ptr,struct mmc_rpmb_data * rpmb)
- Line: 666

### mmc_blk_ioctl_copy_from_user
- Return type: static mmc_blk_ioc_data *
- Signature: mmc_blk_ioctl_copy_from_user(struct mmc_ioc_cmd __user * user)
- Line: 419

### mmc_blk_ioctl_copy_to_user
- Return type: static int
- Signature: mmc_blk_ioctl_copy_to_user(struct mmc_ioc_cmd __user * ic_ptr,struct mmc_blk_ioc_data * idata)
- Line: 462

### mmc_blk_ioctl_multi_cmd
- Return type: static int
- Signature: mmc_blk_ioctl_multi_cmd(struct mmc_blk_data * md,struct mmc_ioc_multi_cmd __user * user,struct mmc_rpmb_data * rpmb)
- Line: 716

### mmc_blk_issue_discard_rq
- Return type: static void
- Signature: mmc_blk_issue_discard_rq(struct mmc_queue * mq,struct request * req)
- Line: 1216

### mmc_blk_issue_drv_op
- Return type: static void
- Signature: mmc_blk_issue_drv_op(struct mmc_queue * mq,struct request * req)
- Line: 1102

### mmc_blk_issue_erase_rq
- Return type: static void
- Signature: mmc_blk_issue_erase_rq(struct mmc_queue * mq,struct request * req,int type,unsigned int erase_arg)
- Line: 1172

### mmc_blk_issue_flush
- Return type: static void
- Signature: mmc_blk_issue_flush(struct mmc_queue * mq,struct request * req)
- Line: 1299

### mmc_blk_issue_secdiscard_rq
- Return type: static void
- Signature: mmc_blk_issue_secdiscard_rq(struct mmc_queue * mq,struct request * req)
- Line: 1228

### mmc_blk_issue_trim_rq
- Return type: static void
- Signature: mmc_blk_issue_trim_rq(struct mmc_queue * mq,struct request * req)
- Line: 1211

### mmc_blk_kref_release
- Return type: static void
- Signature: mmc_blk_kref_release(struct kref * ref)
- Line: 212

### mmc_blk_mq_complete
- Return type: void
- Signature: mmc_blk_mq_complete(struct request * req)
- Line: 2088

### mmc_blk_mq_complete_prev_req
- Return type: static void
- Signature: mmc_blk_mq_complete_prev_req(struct mmc_queue * mq,struct request ** prev_req)
- Line: 2178

### mmc_blk_mq_complete_rq
- Return type: static void
- Signature: mmc_blk_mq_complete_rq(struct mmc_queue * mq,struct request * req)
- Line: 2016

### mmc_blk_mq_complete_work
- Return type: void
- Signature: mmc_blk_mq_complete_work(struct work_struct * work)
- Line: 2202

### mmc_blk_mq_dec_in_flight
- Return type: static void
- Signature: mmc_blk_mq_dec_in_flight(struct mmc_queue * mq,enum mmc_issue_type issue_type)
- Line: 2116

### mmc_blk_mq_issue_rq
- Return type: mmc_issued
- Signature: mmc_blk_mq_issue_rq(struct mmc_queue * mq,struct request * req)
- Line: 2351

### mmc_blk_mq_issue_rw_rq
- Return type: static int
- Signature: mmc_blk_mq_issue_rw_rq(struct mmc_queue * mq,struct request * req)
- Line: 2304

### mmc_blk_mq_poll_completion
- Return type: static void
- Signature: mmc_blk_mq_poll_completion(struct mmc_queue * mq,struct request * req)
- Line: 2099

### mmc_blk_mq_post_req
- Return type: static void
- Signature: mmc_blk_mq_post_req(struct mmc_queue * mq,struct request * req,bool can_sleep)
- Line: 2133

### mmc_blk_mq_recovery
- Return type: void
- Signature: mmc_blk_mq_recovery(struct mmc_queue * mq)
- Line: 2159

### mmc_blk_mq_req_done
- Return type: static void
- Signature: mmc_blk_mq_req_done(struct mmc_request * mrq)
- Line: 2210

### mmc_blk_mq_rw_recovery
- Return type: static void
- Signature: mmc_blk_mq_rw_recovery(struct mmc_queue * mq,struct request * req)
- Line: 1838

### mmc_blk_oor_valid
- Return type: static bool
- Signature: mmc_blk_oor_valid(struct mmc_blk_request * brq)
- Line: 1784

### mmc_blk_open
- Return type: static int
- Signature: mmc_blk_open(struct gendisk * disk,blk_mode_t mode)
- Line: 372

### mmc_blk_part_switch
- Return type: static int
- Signature: mmc_blk_part_switch(struct mmc_card * card,unsigned int part_type)
- Line: 918

### mmc_blk_part_switch_post
- Return type: static int
- Signature: mmc_blk_part_switch_post(struct mmc_card * card,unsigned int part_type)
- Line: 902

### mmc_blk_part_switch_pre
- Return type: static int
- Signature: mmc_blk_part_switch_pre(struct mmc_card * card,unsigned int part_type)
- Line: 883

### mmc_blk_probe
- Return type: static int
- Signature: mmc_blk_probe(struct mmc_card * card)
- Line: 3203

### mmc_blk_put
- Return type: static void
- Signature: mmc_blk_put(struct mmc_blk_data * md)
- Line: 228

### mmc_blk_readonly
- Return type: static int
- Signature: mmc_blk_readonly(struct mmc_card * card)
- Line: 2421

### mmc_blk_release
- Return type: static void
- Signature: mmc_blk_release(struct gendisk * disk)
- Line: 390

### mmc_blk_remove
- Return type: static void
- Signature: mmc_blk_remove(struct mmc_card * card)
- Line: 3261

### mmc_blk_remove_debugfs
- Return type: static void
- Signature: mmc_blk_remove_debugfs(struct mmc_card * card,struct mmc_blk_data * md)
- Line: 3141

### mmc_blk_remove_debugfs
- Return type: static void
- Signature: mmc_blk_remove_debugfs(struct mmc_card * card,struct mmc_blk_data * md)
- Line: 3160

### mmc_blk_remove_parts
- Return type: static void
- Signature: mmc_blk_remove_parts(struct mmc_card * card,struct mmc_blk_data * md)
- Line: 2992

### mmc_blk_remove_req
- Return type: static void
- Signature: mmc_blk_remove_req(struct mmc_blk_data * md)
- Line: 2981

### mmc_blk_remove_rpmb_part
- Return type: static void
- Signature: mmc_blk_remove_rpmb_part(struct mmc_rpmb_data * rpmb)
- Line: 2932

### mmc_blk_reset
- Return type: static int
- Signature: mmc_blk_reset(struct mmc_blk_data * md,struct mmc_host * host,int type)
- Line: 1049

### mmc_blk_reset_success
- Return type: static void
- Signature: mmc_blk_reset_success(struct mmc_blk_data * md,int type)
- Line: 1078

### mmc_blk_resume
- Return type: static int
- Signature: mmc_blk_resume(struct device * dev)
- Line: 3306

### mmc_blk_rpmb_add
- Return type: static void
- Signature: mmc_blk_rpmb_add(struct mmc_card * card)
- Line: 3167

### mmc_blk_rpmb_device_release
- Return type: static void
- Signature: mmc_blk_rpmb_device_release(struct device * dev)
- Line: 2714

### mmc_blk_rq_error
- Return type: static bool
- Signature: mmc_blk_rq_error(struct mmc_blk_request * brq)
- Line: 1921

### mmc_blk_rw_reset_success
- Return type: static void
- Signature: mmc_blk_rw_reset_success(struct mmc_queue * mq,struct request * req)
- Line: 2008

### mmc_blk_rw_rq_prep
- Return type: static void
- Signature: mmc_blk_rw_rq_prep(struct mmc_queue_req * mqrq,struct mmc_card * card,int recovery_mode,struct mmc_queue * mq)
- Line: 1680

### mmc_blk_rw_wait
- Return type: static int
- Signature: mmc_blk_rw_wait(struct mmc_queue * mq,struct request ** prev_req)
- Line: 2292

### mmc_blk_rw_wait_cond
- Return type: static bool
- Signature: mmc_blk_rw_wait_cond(struct mmc_queue * mq,int * err)
- Line: 2270

### mmc_blk_send_stop
- Return type: static int
- Signature: mmc_blk_send_stop(struct mmc_card * card,unsigned int timeout)
- Line: 1754

### mmc_blk_shutdown
- Return type: static void
- Signature: mmc_blk_shutdown(struct mmc_card * card)
- Line: 3294

### mmc_blk_status_error
- Return type: static bool
- Signature: mmc_blk_status_error(struct request * req,u32 status)
- Line: 1798

### mmc_blk_stop_err_bits
- Return type: static u32
- Signature: mmc_blk_stop_err_bits(struct mmc_blk_request * brq)
- Line: 1789

### mmc_blk_suspend
- Return type: static int
- Signature: mmc_blk_suspend(struct device * dev)
- Line: 3299

### mmc_blk_urgent_bkops
- Return type: static void
- Signature: mmc_blk_urgent_bkops(struct mmc_queue * mq,struct mmc_queue_req * mqrq)
- Line: 2046

### mmc_blk_urgent_bkops_needed
- Return type: static bool
- Signature: mmc_blk_urgent_bkops_needed(struct mmc_queue * mq,struct mmc_queue_req * mqrq)
- Line: 2038

### mmc_blk_wait_for_idle
- Return type: static int
- Signature: mmc_blk_wait_for_idle(struct mmc_queue * mq,struct mmc_host * host)
- Line: 2343

### mmc_dbg_card_status_get
- Return type: static int
- Signature: mmc_dbg_card_status_get(void * data,u64 * val)
- Line: 3015

### mmc_disk_attrs_is_visible
- Return type: static umode_t
- Signature: mmc_disk_attrs_is_visible(struct kobject * kobj,struct attribute * a,int n)
- Line: 342

### mmc_ext_csd_open
- Return type: static int
- Signature: mmc_ext_csd_open(struct inode * inode,struct file * filp)
- Line: 3045

### mmc_ext_csd_read
- Return type: static ssize_t
- Signature: mmc_ext_csd_read(struct file * filp,char __user * ubuf,size_t cnt,loff_t * ppos)
- Line: 3096

### mmc_ext_csd_release
- Return type: static int
- Signature: mmc_ext_csd_release(struct inode * inode,struct file * file)
- Line: 3105

### mmc_get_devidx
- Return type: static int
- Signature: mmc_get_devidx(struct gendisk * disk)
- Line: 206

### mmc_route_rpmb_frames
- Return type: static int
- Signature: mmc_route_rpmb_frames(struct device * dev,u8 * req,unsigned int req_len,u8 * resp,unsigned int resp_len)
- Line: 2773

### mmc_rpmb_chrdev_open
- Return type: static int
- Signature: mmc_rpmb_chrdev_open(struct inode * inode,struct file * filp)
- Line: 2683

### mmc_rpmb_chrdev_release
- Return type: static int
- Signature: mmc_rpmb_chrdev_release(struct inode * inode,struct file * filp)
- Line: 2694

### mmc_rpmb_ioctl
- Return type: static long
- Signature: mmc_rpmb_ioctl(struct file * filp,unsigned int cmd,unsigned long arg)
- Line: 2650

### mmc_rpmb_ioctl_compat
- Return type: static long
- Signature: mmc_rpmb_ioctl_compat(struct file * filp,unsigned int cmd,unsigned long arg)
- Line: 2676

### mmc_sd_num_wr_blocks
- Return type: static int
- Signature: mmc_sd_num_wr_blocks(struct mmc_card * card,u32 * written_blocks)
- Line: 954

### mmc_spi_err_check
- Return type: static int
- Signature: mmc_spi_err_check(struct mmc_card * card)
- Line: 1929

### power_ro_lock_show
- Return type: static ssize_t
- Signature: power_ro_lock_show(struct device * dev,struct device_attribute * attr,char * buf)
- Line: 233

### power_ro_lock_store
- Return type: static ssize_t
- Signature: power_ro_lock_store(struct device * dev,struct device_attribute * attr,const char * buf,size_t count)
- Line: 253

### set_idata
- Return type: static void
- Signature: set_idata(struct mmc_blk_ioc_data * idata,u32 opcode,int write_flag,u8 * buf,unsigned int buf_bytes)
- Line: 2755

## Structs (4)

### mmc_blk_busy_data
- Line: 106
- Members:
  - card: mmc_card *
  - status: u32
  - parent: device *
  - disk: gendisk *
  - queue: mmc_queue
  - part: list_head
  - rpmbs: list_head
  - flags: unsigned int
  - kref: kref
  - read_only: unsigned int
  - part_type: unsigned int
  - reset_done: unsigned int
  - part_curr: unsigned int
  - area_type: int
  - status_dentry: dentry *
  - ext_csd_dentry: dentry *
  - dev: device
  - chrdev: cdev
  - id: int
  - part_index: unsigned int
  - md: mmc_blk_data *
  - rdev: rpmb_dev *
  - node: list_head
  - ic: mmc_ioc_cmd
  - buf: unsigned char *
  - buf_bytes: u64
  - flags: unsigned int
  - rpmb: mmc_rpmb_data *

### mmc_blk_data
- Line: 114
- Members:
  - card: mmc_card *
  - status: u32
  - parent: device *
  - disk: gendisk *
  - queue: mmc_queue
  - part: list_head
  - rpmbs: list_head
  - flags: unsigned int
  - kref: kref
  - read_only: unsigned int
  - part_type: unsigned int
  - reset_done: unsigned int
  - part_curr: unsigned int
  - area_type: int
  - status_dentry: dentry *
  - ext_csd_dentry: dentry *
  - dev: device
  - chrdev: cdev
  - id: int
  - part_index: unsigned int
  - md: mmc_blk_data *
  - rdev: rpmb_dev *
  - node: list_head
  - ic: mmc_ioc_cmd
  - buf: unsigned char *
  - buf_bytes: u64
  - flags: unsigned int
  - rpmb: mmc_rpmb_data *

### mmc_blk_ioc_data
- Line: 408
- Members:
  - card: mmc_card *
  - status: u32
  - parent: device *
  - disk: gendisk *
  - queue: mmc_queue
  - part: list_head
  - rpmbs: list_head
  - flags: unsigned int
  - kref: kref
  - read_only: unsigned int
  - part_type: unsigned int
  - reset_done: unsigned int
  - part_curr: unsigned int
  - area_type: int
  - status_dentry: dentry *
  - ext_csd_dentry: dentry *
  - dev: device
  - chrdev: cdev
  - id: int
  - part_index: unsigned int
  - md: mmc_blk_data *
  - rdev: rpmb_dev *
  - node: list_head
  - ic: mmc_ioc_cmd
  - buf: unsigned char *
  - buf_bytes: u64
  - flags: unsigned int
  - rpmb: mmc_rpmb_data *

### mmc_rpmb_data
- Line: 168
- Members:
  - card: mmc_card *
  - status: u32
  - parent: device *
  - disk: gendisk *
  - queue: mmc_queue
  - part: list_head
  - rpmbs: list_head
  - flags: unsigned int
  - kref: kref
  - read_only: unsigned int
  - part_type: unsigned int
  - reset_done: unsigned int
  - part_curr: unsigned int
  - area_type: int
  - status_dentry: dentry *
  - ext_csd_dentry: dentry *
  - dev: device
  - chrdev: cdev
  - id: int
  - part_index: unsigned int
  - md: mmc_blk_data *
  - rdev: rpmb_dev *
  - node: list_head
  - ic: mmc_ioc_cmd
  - buf: unsigned char *
  - buf_bytes: u64
  - flags: unsigned int
  - rpmb: mmc_rpmb_data *

## Variables (11)

- static **max_devices** : int (line 99)
- static **mmc_bdops** : const struct block_device_operations (line 871)
- static **mmc_dbg_ext_csd_fops** : const struct file_operations (line 3111)
- static **mmc_disk_attr_group** : const struct attribute_group (line 362)
- static **mmc_disk_attr_groups** : const struct attribute_group * [] (line 367)
- static **mmc_disk_attrs** : attribute * [] (line 336)
- static **mmc_driver** : mmc_driver (line 3327)
- static **mmc_rpmb_bus_type** : const struct bus_type (line 154)
- static **mmc_rpmb_devt** : dev_t (line 151)
- static **mmc_rpmb_fileops** : const struct file_operations (line 2704)
- static **perdev_minors** : int (line 92)

## Macros (26)

- **CHECK_SIZE_ALIGNED**(val) (line 84)
- **CHECK_SIZE_NEQ**(val) (line 83)
- **CMD_ERRORS** (line 1340)
- **CMD_ERRORS_EXCL_OOR** (line 1332)
- **EXT_CSD_STR_LEN** (line 3043)
- **MAX_DEVICES** (line 101)
- **MMC_BLK_CMD23** (line 122)
- **MMC_BLK_CQE_RECOVERY** (line 133)
- **MMC_BLK_DISCARD** (line 131)
- **MMC_BLK_IOC_DROP** (line 413)
- **MMC_BLK_IOC_SBC** (line 414)
- **MMC_BLK_PART_INVALID** (line 142)
- **MMC_BLK_READ** (line 129)
- **MMC_BLK_REL_WR** (line 123)
- **MMC_BLK_SECDISCARD** (line 132)
- **MMC_BLK_TIMEOUT_MS** (line 78)
- **MMC_BLK_TRIM** (line 134)
- **MMC_BLK_WRITE** (line 130)
- **MMC_CQE_RETRIES** (line 1523)
- **MMC_DATA_RETRIES** (line 1751)
- **MMC_EXTRACT_INDEX_FROM_ARG**(x) (line 79)
- **MMC_EXTRACT_VALUE_FROM_ARG**(x) (line 80)
- **MMC_MAX_RETRIES** (line 1750)
- **MMC_NO_RETRIES** (line 1752)
- **MODULE_PARAM_PREFIX** (line 70)
- **RPMB_FRAME_SIZE** (line 82)
