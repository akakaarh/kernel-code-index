# drivers/spi/spi.c

Subsystem: drivers/spi

## Functions (148)

### __devm_spi_alloc_controller
- Return type: spi_controller *
- Signature: __devm_spi_alloc_controller(struct device * dev,unsigned int size,bool target)
- Line: 3300

### __spi_add_device
- Return type: static int
- Signature: __spi_add_device(struct spi_device * spi,struct spi_device * parent)
- Line: 674

### __spi_alloc_controller
- Return type: spi_controller *
- Signature: __spi_alloc_controller(struct device * dev,unsigned int size,bool target)
- Line: 3235

### __spi_async
- Return type: static int
- Signature: __spi_async(struct spi_device * spi,struct spi_message * message)
- Line: 4555

### __spi_check_suspended
- Return type: static int
- Signature: __spi_check_suspended(const struct spi_controller * ctlr)
- Line: 3672

### __spi_map_msg
- Return type: static int
- Signature: __spi_map_msg(struct spi_controller * ctlr,struct spi_message * msg)
- Line: 1348

### __spi_map_msg
- Return type: static int
- Signature: __spi_map_msg(struct spi_controller * ctlr,struct spi_message * msg)
- Line: 1233

### __spi_mark_resumed
- Return type: static void
- Signature: __spi_mark_resumed(struct spi_controller * ctlr)
- Line: 3684

### __spi_mark_suspended
- Return type: static void
- Signature: __spi_mark_suspended(struct spi_controller * ctlr)
- Line: 3677

### __spi_optimize_message
- Return type: static int
- Signature: __spi_optimize_message(struct spi_device * spi,struct spi_message * msg)
- Line: 4443

### __spi_pump_messages
- Return type: static void
- Signature: __spi_pump_messages(struct spi_controller * ctlr,bool in_kthread)
- Line: 1851

### __spi_pump_transfer_message
- Return type: static int
- Signature: __spi_pump_transfer_message(struct spi_controller * ctlr,struct spi_message * msg,bool was_busy)
- Line: 1737

### __spi_queued_transfer
- Return type: static int
- Signature: __spi_queued_transfer(struct spi_device * spi,struct spi_message * msg,bool need_pump)
- Line: 2264

### __spi_register_driver
- Return type: int
- Signature: __spi_register_driver(struct module * owner,struct spi_driver * sdrv)
- Line: 472

### __spi_replace_transfers_release
- Return type: static void
- Signature: __spi_replace_transfers_release(struct spi_controller * ctlr,struct spi_message * msg,void * res)
- Line: 3726

### __spi_setup
- Return type: static int
- Signature: __spi_setup(struct spi_device * spi,bool initial_setup)
- Line: 4054

### __spi_split_transfer_maxsize
- Return type: static int
- Signature: __spi_split_transfer_maxsize(struct spi_controller * ctlr,struct spi_message * msg,struct spi_transfer ** xferp,size_t maxsize)
- Line: 3857

### __spi_sync
- Return type: static int
- Signature: __spi_sync(struct spi_device * spi,struct spi_message * message)
- Line: 4708

### __spi_transfer_message_noqueue
- Return type: static void
- Signature: __spi_transfer_message_noqueue(struct spi_controller * ctlr,struct spi_message * msg)
- Line: 4664

### __spi_unmap_msg
- Return type: static int
- Signature: __spi_unmap_msg(struct spi_controller * ctlr,struct spi_message * msg)
- Line: 1354

### __spi_unmap_msg
- Return type: static int
- Signature: __spi_unmap_msg(struct spi_controller * ctlr,struct spi_message * msg)
- Line: 1300

### __spi_unoptimize_message
- Return type: static void
- Signature: __spi_unoptimize_message(struct spi_message * msg)
- Line: 2117

### __spi_validate
- Return type: static int
- Signature: __spi_validate(struct spi_device * spi,struct spi_message * message)
- Line: 4238

### __spi_validate_bits_per_word
- Return type: static int
- Signature: __spi_validate_bits_per_word(struct spi_controller * ctlr,u8 bits_per_word)
- Line: 4010

### __unregister
- Return type: static int
- Signature: __unregister(struct device * dev,void * null)
- Line: 3610

### _spi_transfer_cs_change_delay
- Return type: static void
- Signature: _spi_transfer_cs_change_delay(struct spi_message * msg,struct spi_transfer * xfer)
- Line: 1566

### _spi_transfer_delay_ns
- Return type: static void
- Signature: _spi_transfer_delay_ns(u32 ns)
- Line: 1495

### _spi_xfer_word_delay_update
- Return type: static int
- Signature: _spi_xfer_word_delay_update(struct spi_transfer * xfer,struct spi_device * spi)
- Line: 4218

### acpi_register_spi_device
- Return type: static acpi_status
- Signature: acpi_register_spi_device(struct spi_controller * ctlr,struct acpi_device * adev)
- Line: 3020

### acpi_register_spi_devices
- Return type: static void
- Signature: acpi_register_spi_devices(struct spi_controller * ctlr)
- Line: 3095

### acpi_register_spi_devices
- Return type: static void
- Signature: acpi_register_spi_devices(struct spi_controller * ctlr)
- Line: 3079

### acpi_spi_add_device
- Return type: static acpi_status
- Signature: acpi_spi_add_device(acpi_handle handle,u32 level,void * data,void ** return_value)
- Line: 3065

### acpi_spi_add_resource
- Return type: static int
- Signature: acpi_spi_add_resource(struct acpi_resource * ares,void * data)
- Line: 2865

### acpi_spi_count
- Return type: static int
- Signature: acpi_spi_count(struct acpi_resource * ares,void * data)
- Line: 2796

### acpi_spi_count_resources
- Return type: int
- Signature: acpi_spi_count_resources(struct acpi_device * adev)
- Line: 2820

### acpi_spi_device_alloc
- Return type: spi_device *
- Signature: acpi_spi_device_alloc(struct spi_controller * ctlr,struct acpi_device * adev,int index)
- Line: 2959

### acpi_spi_find_controller_by_adev
- Return type: spi_controller *
- Signature: acpi_spi_find_controller_by_adev(struct acpi_device * adev)
- Line: 5056

### acpi_spi_find_device_by_adev
- Return type: static spi_device *
- Signature: acpi_spi_find_device_by_adev(struct acpi_device * adev)
- Line: 5072

### acpi_spi_notify
- Return type: static int
- Signature: acpi_spi_notify(struct notifier_block * nb,unsigned long value,void * arg)
- Line: 5080

### acpi_spi_parse_apple_properties
- Return type: static void
- Signature: acpi_spi_parse_apple_properties(struct acpi_device * dev,struct acpi_spi_lookup * lookup)
- Line: 2836

### devm_spi_new_ancillary_device
- Return type: spi_device *
- Signature: devm_spi_new_ancillary_device(struct spi_device * spi,u8 chip_select)
- Line: 2765

### devm_spi_optimize_message
- Return type: int
- Signature: devm_spi_optimize_message(struct device * dev,struct spi_device * spi,struct spi_message * msg)
- Line: 4597

### devm_spi_register_controller
- Return type: int
- Signature: devm_spi_register_controller(struct device * dev,struct spi_controller * ctlr)
- Line: 3585

### devm_spi_release_controller
- Return type: static void
- Signature: devm_spi_release_controller(void * ctlr)
- Line: 3280

### devm_spi_unoptimize_message
- Return type: static void
- Signature: devm_spi_unoptimize_message(void * msg)
- Line: 4582

### devm_spi_unregister_controller
- Return type: static void
- Signature: devm_spi_unregister_controller(void * ctlr)
- Line: 3567

### devm_spi_unregister_device
- Return type: static void
- Signature: devm_spi_unregister_device(void * spi)
- Line: 2744

### driver_override_show
- Return type: static ssize_t
- Signature: driver_override_show(struct device * dev,struct device_attribute * a,char * buf)
- Line: 86

### driver_override_store
- Return type: static ssize_t
- Signature: driver_override_store(struct device * dev,struct device_attribute * a,const char * buf,size_t count)
- Line: 73

### modalias_show
- Return type: static ssize_t
- Signature: modalias_show(struct device * dev,struct device_attribute * a,char * buf)
- Line: 60

### of_find_spi_controller_by_node
- Return type: spi_controller *
- Signature: of_find_spi_controller_by_node(struct device_node * node)
- Line: 4963

### of_find_spi_device_by_node
- Return type: static spi_device *
- Signature: of_find_spi_device_by_node(struct device_node * node)
- Line: 4981

### of_register_spi_device
- Return type: static spi_device *
- Signature: of_register_spi_device(struct spi_controller * ctlr,struct device_node * nc)
- Line: 2614

### of_register_spi_devices
- Return type: static void
- Signature: of_register_spi_devices(struct spi_controller * ctlr)
- Line: 2684

### of_register_spi_devices
- Return type: static void
- Signature: of_register_spi_devices(struct spi_controller * ctlr)
- Line: 2667

### of_spi_notify
- Return type: static int
- Signature: of_spi_notify(struct notifier_block * nb,unsigned long action,void * arg)
- Line: 4988

### of_spi_parse_dt
- Return type: static int
- Signature: of_spi_parse_dt(struct spi_controller * ctlr,struct spi_device * spi,struct device_node * nc)
- Line: 2365

### of_spi_parse_dt_cs_delay
- Return type: static void
- Signature: of_spi_parse_dt_cs_delay(struct device_node * nc,struct spi_delay * delay,const char * prop)
- Line: 2349

### slave_show
- Return type: static ssize_t
- Signature: slave_show(struct device * dev,struct device_attribute * attr,char * buf)
- Line: 3130

### slave_store
- Return type: static ssize_t
- Signature: slave_store(struct device * dev,struct device_attribute * attr,const char * buf,size_t count)
- Line: 3145

### spi_acpi_controller_match
- Return type: static int
- Signature: spi_acpi_controller_match(struct device * dev,const void * data)
- Line: 5051

### spi_add_device
- Return type: int
- Signature: spi_add_device(struct spi_device * spi)
- Line: 777

### spi_alloc_device
- Return type: spi_device *
- Signature: spi_alloc_device(struct spi_controller * ctlr)
- Line: 558

### spi_alloc_pcpu_stats
- Return type: static spi_statistics __percpu *
- Signature: spi_alloc_pcpu_stats(void)
- Line: 94

### spi_async
- Return type: int
- Signature: spi_async(struct spi_device * spi,struct spi_message * message)
- Line: 4641

### spi_bus_lock
- Return type: int
- Signature: spi_bus_lock(struct spi_controller * ctlr)
- Line: 4840

### spi_bus_unlock
- Return type: int
- Signature: spi_bus_unlock(struct spi_controller * ctlr)
- Line: 4869

### spi_cleanup
- Return type: static void
- Signature: spi_cleanup(struct spi_device * spi)
- Line: 668

### spi_complete
- Return type: static void
- Signature: spi_complete(void * arg)
- Line: 4703

### spi_controller_check_ops
- Return type: static int
- Signature: spi_controller_check_ops(struct spi_controller * ctlr)
- Line: 3396

### spi_controller_id_alloc
- Return type: static int
- Signature: spi_controller_id_alloc(struct spi_controller * ctlr,int start,int end)
- Line: 3416

### spi_controller_initialize_queue
- Return type: static int
- Signature: spi_controller_initialize_queue(struct spi_controller * ctlr)
- Line: 2301

### spi_controller_release
- Return type: static void
- Signature: spi_controller_release(struct device * dev)
- Line: 3098

### spi_controller_resume
- Return type: int
- Signature: spi_controller_resume(struct spi_controller * ctlr)
- Line: 3707

### spi_controller_suspend
- Return type: int
- Signature: spi_controller_suspend(struct spi_controller * ctlr)
- Line: 3691

### spi_delay_exec
- Return type: int
- Signature: spi_delay_exec(struct spi_delay * _delay,struct spi_transfer * xfer)
- Line: 1547

### spi_delay_to_ns
- Return type: int
- Signature: spi_delay_to_ns(struct spi_delay * _delay,struct spi_transfer * xfer)
- Line: 1508

### spi_destroy_queue
- Return type: static int
- Signature: spi_destroy_queue(struct spi_controller * ctlr)
- Line: 2242

### spi_dev_check
- Return type: static int
- Signature: spi_dev_check(struct device * dev,void * data)
- Line: 643

### spi_dev_check_cs
- Return type: static int
- Signature: spi_dev_check_cs(struct device * dev,struct spi_device * spi,u8 idx,struct spi_device * new_spi,u8 new_idx)
- Line: 620

### spi_dev_set_name
- Return type: static void
- Signature: spi_dev_set_name(struct spi_device * spi)
- Line: 590

### spi_dma_sync_for_cpu
- Return type: static void
- Signature: spi_dma_sync_for_cpu(struct spi_controller * ctlr,struct spi_transfer * xfer)
- Line: 1336

### spi_dma_sync_for_cpu
- Return type: static void
- Signature: spi_dma_sync_for_cpu(struct spi_controller * ctrl,struct spi_transfer * xfer)
- Line: 1365

### spi_dma_sync_for_device
- Return type: static void
- Signature: spi_dma_sync_for_device(struct spi_controller * ctlr,struct spi_transfer * xfer)
- Line: 1324

### spi_dma_sync_for_device
- Return type: static void
- Signature: spi_dma_sync_for_device(struct spi_controller * ctrl,struct spi_transfer * xfer)
- Line: 1360

### spi_emit_pcpu_stats
- Return type: static ssize_t
- Signature: spi_emit_pcpu_stats(struct spi_statistics __percpu * stat,char * buf,size_t offset)
- Line: 113

### spi_finalize_current_message
- Return type: void
- Signature: spi_finalize_current_message(struct spi_controller * ctlr)
- Line: 2151

### spi_finalize_current_transfer
- Return type: void
- Signature: spi_finalize_current_transfer(struct spi_controller * ctlr)
- Line: 1724

### spi_flush_queue
- Return type: void
- Signature: spi_flush_queue(struct spi_controller * ctlr)
- Line: 2340

### spi_get_device_id
- Return type: const struct spi_device_id *
- Signature: spi_get_device_id(const struct spi_device * sdev)
- Line: 347

### spi_get_device_match_data
- Return type: const void *
- Signature: spi_get_device_match_data(const struct spi_device * sdev)
- Line: 355

### spi_get_gpio_descs
- Return type: static int
- Signature: spi_get_gpio_descs(struct spi_controller * ctlr)
- Line: 3325

### spi_get_next_queued_message
- Return type: spi_message *
- Signature: spi_get_next_queued_message(struct spi_controller * ctlr)
- Line: 2091

### spi_idle_runtime_pm
- Return type: static void
- Signature: spi_idle_runtime_pm(struct spi_controller * ctlr)
- Line: 1730

### spi_init
- Return type: static int __init
- Signature: spi_init(void)
- Line: 5119

### spi_init_queue
- Return type: static int
- Signature: spi_init_queue(struct spi_controller * ctlr)
- Line: 2054

### spi_is_last_cs
- Return type: static bool
- Signature: spi_is_last_cs(struct spi_device * spi)
- Line: 1037

### spi_map_buf
- Return type: int
- Signature: spi_map_buf(struct spi_controller * ctlr,struct device * dev,struct sg_table * sgt,void * buf,size_t len,enum dma_data_direction dir)
- Line: 1209

### spi_map_buf_attrs
- Return type: static int
- Signature: spi_map_buf_attrs(struct spi_controller * ctlr,struct device * dev,struct sg_table * sgt,void * buf,size_t len,enum dma_data_direction dir,unsigned long attrs)
- Line: 1132

### spi_map_msg
- Return type: static int
- Signature: spi_map_msg(struct spi_controller * ctlr,struct spi_message * msg)
- Line: 1390

### spi_match_controller_to_boardinfo
- Return type: static void
- Signature: spi_match_controller_to_boardinfo(struct spi_controller * ctlr,struct spi_board_info * bi)
- Line: 892

### spi_match_device
- Return type: static int
- Signature: spi_match_device(struct device * dev,const struct device_driver * drv)
- Line: 367

### spi_match_id
- Return type: static const struct spi_device_id *
- Signature: spi_match_id(const struct spi_device_id * id,const char * name)
- Line: 337

### spi_maybe_optimize_message
- Return type: static int
- Signature: spi_maybe_optimize_message(struct spi_device * spi,struct spi_message * msg)
- Line: 4476

### spi_maybe_unoptimize_message
- Return type: static void
- Signature: spi_maybe_unoptimize_message(struct spi_message * msg)
- Line: 2137

### spi_new_ancillary_device
- Return type: spi_device *
- Signature: spi_new_ancillary_device(struct spi_device * spi,u8 chip_select)
- Line: 2699

### spi_new_device
- Return type: spi_device *
- Signature: spi_new_device(struct spi_controller * ctlr,struct spi_board_info * chip)
- Line: 806

### spi_optimize_message
- Return type: int
- Signature: spi_optimize_message(struct spi_device * spi,struct spi_message * msg)
- Line: 4510

### spi_probe
- Return type: static int
- Signature: spi_probe(struct device * dev)
- Line: 404

### spi_pump_messages
- Return type: static void
- Signature: spi_pump_messages(struct kthread_work * work)
- Line: 1940

### spi_queued_transfer
- Return type: static int
- Signature: spi_queued_transfer(struct spi_device * spi,struct spi_message * msg)
- Line: 2296

### spi_register_board_info
- Return type: int
- Signature: spi_register_board_info(struct spi_board_info const * info,unsigned n)
- Line: 927

### spi_register_controller
- Return type: int
- Signature: spi_register_controller(struct spi_controller * ctlr)
- Line: 3452

### spi_remove
- Return type: static void
- Signature: spi_remove(struct device * dev)
- Line: 435

### spi_replace_transfers
- Return type: static spi_replaced_transfers *
- Signature: spi_replace_transfers(struct spi_message * msg,struct spi_transfer * xfer_first,size_t remove,size_t insert,spi_replaced_release_t release,size_t extradatasize,gfp_t gfp)
- Line: 3760

### spi_res_add
- Return type: static void
- Signature: spi_res_add(struct spi_message * message,void * res)
- Line: 1005

### spi_res_alloc
- Return type: static void *
- Signature: spi_res_alloc(struct spi_device * spi,spi_res_release_t release,size_t size,gfp_t gfp)
- Line: 973

### spi_res_free
- Return type: static void
- Signature: spi_res_free(void * res)
- Line: 992

### spi_res_release
- Return type: static void
- Signature: spi_res_release(struct spi_controller * ctlr,struct spi_message * message)
- Line: 1018

### spi_set_cs
- Return type: static void
- Signature: spi_set_cs(struct spi_device * spi,bool enable,bool force)
- Line: 1073

### spi_set_cs_timing
- Return type: static int
- Signature: spi_set_cs_timing(struct spi_device * spi)
- Line: 4030

### spi_set_thread_rt
- Return type: static void
- Signature: spi_set_thread_rt(struct spi_controller * ctlr)
- Line: 2047

### spi_setup
- Return type: int
- Signature: spi_setup(struct spi_device * spi)
- Line: 4212

### spi_shutdown
- Return type: static void
- Signature: spi_shutdown(struct device * dev)
- Line: 443

### spi_split_transfers
- Return type: static int
- Signature: spi_split_transfers(struct spi_message * msg)
- Line: 4394

### spi_split_transfers_maxsize
- Return type: int
- Signature: spi_split_transfers_maxsize(struct spi_controller * ctlr,struct spi_message * msg,size_t maxsize)
- Line: 3931

### spi_split_transfers_maxwords
- Return type: int
- Signature: spi_split_transfers_maxwords(struct spi_controller * ctlr,struct spi_message * msg,size_t maxwords)
- Line: 3973

### spi_start_queue
- Return type: static int
- Signature: spi_start_queue(struct spi_controller * ctlr)
- Line: 2197

### spi_statistics_add_transfer_stats
- Return type: static void
- Signature: spi_statistics_add_transfer_stats(struct spi_statistics __percpu * pcpu_stats,struct spi_transfer * xfer,struct spi_message * msg)
- Line: 306

### spi_stop_queue
- Return type: static int
- Signature: spi_stop_queue(struct spi_controller * ctlr)
- Line: 2217

### spi_sync
- Return type: int
- Signature: spi_sync(struct spi_device * spi,struct spi_message * message)
- Line: 4791

### spi_sync_locked
- Return type: int
- Signature: spi_sync_locked(struct spi_device * spi,struct spi_message * message)
- Line: 4819

### spi_take_timestamp_post
- Return type: void
- Signature: spi_take_timestamp_post(struct spi_controller * ctlr,struct spi_transfer * xfer,size_t progress,bool irqs_off)
- Line: 2005

### spi_take_timestamp_pre
- Return type: void
- Signature: spi_take_timestamp_pre(struct spi_controller * ctlr,struct spi_transfer * xfer,size_t progress,bool irqs_off)
- Line: 1968

### spi_target_abort
- Return type: int
- Signature: spi_target_abort(struct spi_device * spi)
- Line: 3119

### spi_toggle_csgpiod
- Return type: static void
- Signature: spi_toggle_csgpiod(struct spi_device * spi,u8 idx,bool enable,bool activate)
- Line: 1049

### spi_transfer_cs_change_delay_exec
- Return type: void
- Signature: spi_transfer_cs_change_delay_exec(struct spi_message * msg,struct spi_transfer * xfer)
- Line: 1590

### spi_transfer_one_message
- Return type: static int
- Signature: spi_transfer_one_message(struct spi_controller * ctlr,struct spi_message * msg)
- Line: 1604

### spi_transfer_wait
- Return type: static int
- Signature: spi_transfer_wait(struct spi_controller * ctlr,struct spi_message * msg,struct spi_transfer * xfer)
- Line: 1442

### spi_uevent
- Return type: static int
- Signature: spi_uevent(const struct device * dev,struct kobj_uevent_env * env)
- Line: 392

### spi_unmap_buf
- Return type: void
- Signature: spi_unmap_buf(struct spi_controller * ctlr,struct device * dev,struct sg_table * sgt,enum dma_data_direction dir)
- Line: 1227

### spi_unmap_buf_attrs
- Return type: static void
- Signature: spi_unmap_buf_attrs(struct spi_controller * ctlr,struct device * dev,struct sg_table * sgt,enum dma_data_direction dir,unsigned long attrs)
- Line: 1216

### spi_unmap_msg
- Return type: static int
- Signature: spi_unmap_msg(struct spi_controller * ctlr,struct spi_message * msg)
- Line: 1371

### spi_unoptimize_message
- Return type: void
- Signature: spi_unoptimize_message(struct spi_message * msg)
- Line: 4545

### spi_unregister_controller
- Return type: void
- Signature: spi_unregister_controller(struct spi_controller * ctlr)
- Line: 3629

### spi_unregister_device
- Return type: void
- Signature: spi_unregister_device(struct spi_device * spi)
- Line: 871

### spi_write_then_read
- Return type: int
- Signature: spi_write_then_read(struct spi_device * spi,const void * txbuf,unsigned n_tx,void * rxbuf,unsigned n_rx)
- Line: 4904

### spidev_release
- Return type: static void
- Signature: spidev_release(struct device * dev)
- Line: 50

## Structs (3)

### acpi_spi_lookup
- Line: 2785
- Members:
  - list: list_head
  - board_info: spi_board_info
  - new_spi: spi_device *
  - parent: spi_device *
  - ctlr: spi_controller *
  - max_speed_hz: u32
  - mode: u32
  - irq: int
  - bits_per_word: u8
  - chip_select: u8
  - n: int
  - index: int

### boardinfo
- Line: 526
- Members:
  - list: list_head
  - board_info: spi_board_info
  - new_spi: spi_device *
  - parent: spi_device *
  - ctlr: spi_controller *
  - max_speed_hz: u32
  - mode: u32
  - irq: int
  - bits_per_word: u8
  - chip_select: u8
  - n: int
  - index: int

### spi_dev_check_info
- Line: 638
- Members:
  - list: list_head
  - board_info: spi_board_info
  - new_spi: spi_device *
  - parent: spi_device *
  - ctlr: spi_controller *
  - max_speed_hz: u32
  - mode: u32
  - irq: int
  - bits_per_word: u8
  - chip_select: u8
  - n: int
  - index: int

## Variables (17)

- static **buf** : u8 * (line 4882)
- static **spi_acpi_notifier** : notifier_block (line 5112)
- **spi_bus_type** : const struct bus_type (line 453)
- static **spi_controller_class** : const struct class (line 3108)
- static **spi_controller_groups** : const struct attribute_group * [] (line 301)
- static **spi_controller_statistics_attrs** : attribute * [] (line 264)
- static **spi_controller_statistics_group** : const struct attribute_group (line 296)
- static **spi_dev_attrs** : attribute * [] (line 211)
- static **spi_dev_group** : const struct attribute_group (line 217)
- static **spi_dev_groups** : const struct attribute_group * [] (line 258)
- static **spi_device_statistics_attrs** : attribute * [] (line 221)
- static **spi_device_statistics_group** : const struct attribute_group (line 253)
- static **spi_of_notifier** : notifier_block (line 5043)
- static **spi_target_attrs** : attribute * [] (line 3186)
- static **spi_target_class** : const struct class (line 3201)
- static **spi_target_group** : const struct attribute_group (line 3191)
- static **spi_target_groups** : const struct attribute_group * [] (line 3195)

## Macros (9)

- **CREATE_TRACE_POINTS** (line 39)
- **SPI_ACPI_ENUMERATE_MAX_DEPTH** (line 3077)
- **SPI_BUFSIZ** (line 4880)
- **SPI_INVALID_CS** (line 618)
- **SPI_STATISTICS_ATTRS**(field,file) (line 136)
- **SPI_STATISTICS_SHOW**(field) (line 170)
- **SPI_STATISTICS_SHOW_NAME**(name,file,field) (line 161)
- **SPI_STATISTICS_TRANSFER_BYTES_HISTO**(index,number) (line 187)
- **spi_for_each_valid_cs**(spi,idx) (line 1033)
