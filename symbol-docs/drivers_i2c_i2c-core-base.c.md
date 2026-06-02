# drivers/i2c/i2c-core-base.c

Subsystem: drivers/i2c

## Functions (101)

### __i2c_add_numbered_adapter
- Return type: static int
- Signature: __i2c_add_numbered_adapter(struct i2c_adapter * adap)
- Line: 1625

### __i2c_check_addr_busy
- Return type: static int
- Signature: __i2c_check_addr_busy(struct device * dev,void * addrp)
- Line: 785

### __i2c_transfer
- Return type: int
- Signature: __i2c_transfer(struct i2c_adapter * adap,struct i2c_msg * msgs,int num)
- Line: 2220

### __process_new_adapter
- Return type: static int
- Signature: __process_new_adapter(struct device_driver * d,void * data)
- Line: 1432

### __process_new_driver
- Return type: static int
- Signature: __process_new_driver(struct device * dev,void * data)
- Line: 1990

### __process_removed_adapter
- Return type: static int
- Signature: __process_removed_adapter(struct device_driver * d,void * data)
- Line: 1740

### __process_removed_driver
- Return type: static int
- Signature: __process_removed_driver(struct device * dev,void * data)
- Line: 2031

### __unregister_client
- Return type: static int
- Signature: __unregister_client(struct device * dev,void * dummy)
- Line: 1725

### __unregister_dummy
- Return type: static int
- Signature: __unregister_dummy(struct device * dev,void * dummy)
- Line: 1733

### delete_device_store
- Return type: static ssize_t
- Signature: delete_device_store(struct device * dev,struct device_attribute * attr,const char * buf,size_t count)
- Line: 1331

### devm_i2c_add_adapter
- Return type: int
- Signature: devm_i2c_add_adapter(struct device * dev,struct i2c_adapter * adapter)
- Line: 1840

### devm_i2c_del_adapter
- Return type: static void
- Signature: devm_i2c_del_adapter(void * adapter)
- Line: 1826

### devm_i2c_new_dummy_device
- Return type: i2c_client *
- Signature: devm_i2c_new_dummy_device(struct device * dev,struct i2c_adapter * adapter,u16 address)
- Line: 1168

### devm_i2c_release_dummy
- Return type: static void
- Signature: devm_i2c_release_dummy(void * client)
- Line: 1153

### dummy_probe
- Return type: static int
- Signature: dummy_probe(struct i2c_client * client)
- Line: 1114

### get_scl_gpio_value
- Return type: static int
- Signature: get_scl_gpio_value(struct i2c_adapter * adap)
- Line: 179

### get_sda_gpio_value
- Return type: static int
- Signature: get_sda_gpio_value(struct i2c_adapter * adap)
- Line: 189

### i2c_adapter_depth
- Return type: unsigned int
- Signature: i2c_adapter_depth(struct i2c_adapter * adapter)
- Line: 1236

### i2c_adapter_dev_release
- Return type: static void
- Signature: i2c_adapter_dev_release(struct device * dev)
- Line: 1230

### i2c_adapter_lock_bus
- Return type: static void
- Signature: i2c_adapter_lock_bus(struct i2c_adapter * adapter,unsigned int flags)
- Line: 845

### i2c_adapter_trylock_bus
- Return type: static int
- Signature: i2c_adapter_trylock_bus(struct i2c_adapter * adapter,unsigned int flags)
- Line: 857

### i2c_adapter_unlock_bus
- Return type: static void
- Signature: i2c_adapter_unlock_bus(struct i2c_adapter * adapter,unsigned int flags)
- Line: 869

### i2c_add_adapter
- Return type: int
- Signature: i2c_add_adapter(struct i2c_adapter * adapter)
- Line: 1652

### i2c_add_numbered_adapter
- Return type: int
- Signature: i2c_add_numbered_adapter(struct i2c_adapter * adap)
- Line: 1699

### i2c_check_7bit_addr_validity_strict
- Return type: int
- Signature: i2c_check_7bit_addr_validity_strict(unsigned short addr)
- Line: 768

### i2c_check_addr_busy
- Return type: static int
- Signature: i2c_check_addr_busy(struct i2c_adapter * adapter,int addr)
- Line: 824

### i2c_check_addr_validity
- Return type: static int
- Signature: i2c_check_addr_validity(unsigned int addr,unsigned short flags)
- Line: 750

### i2c_check_for_quirks
- Return type: static int
- Signature: i2c_check_for_quirks(struct i2c_adapter * adap,struct i2c_msg * msgs,int num)
- Line: 2154

### i2c_check_mux_children
- Return type: static int
- Signature: i2c_check_mux_children(struct device * dev,void * addrp)
- Line: 811

### i2c_check_mux_parents
- Return type: static int
- Signature: i2c_check_mux_parents(struct i2c_adapter * adapter,int addr)
- Line: 796

### i2c_client_dev_release
- Return type: static void
- Signature: i2c_client_dev_release(struct device * dev)
- Line: 659

### i2c_client_get_device_id
- Return type: const struct i2c_device_id *
- Signature: i2c_client_get_device_id(const struct i2c_client * client)
- Line: 2391

### i2c_clients_command
- Return type: void
- Signature: i2c_clients_command(struct i2c_adapter * adap,unsigned int cmd,void * arg)
- Line: 2074

### i2c_cmd
- Return type: static int
- Signature: i2c_cmd(struct device * dev,void * _arg)
- Line: 2059

### i2c_default_probe
- Return type: static int
- Signature: i2c_default_probe(struct i2c_adapter * adap,unsigned short addr)
- Line: 2417

### i2c_del_adapter
- Return type: void
- Signature: i2c_del_adapter(struct i2c_adapter * adap)
- Line: 1754

### i2c_del_driver
- Return type: void
- Signature: i2c_del_driver(struct i2c_driver * driver)
- Line: 2043

### i2c_detect
- Return type: static int
- Signature: i2c_detect(struct i2c_adapter * adapter,struct i2c_driver * driver)
- Line: 2507

### i2c_detect_address
- Return type: static int
- Signature: i2c_detect_address(struct i2c_client * temp_client,struct i2c_driver * driver)
- Line: 2445

### i2c_dev_irq_from_resources
- Return type: int
- Signature: i2c_dev_irq_from_resources(const struct resource * resources,unsigned int num_resources)
- Line: 895

### i2c_dev_or_parent_fwnode_match
- Return type: static int
- Signature: i2c_dev_or_parent_fwnode_match(struct device * dev,const void * data)
- Line: 1852

### i2c_dev_set_name
- Return type: static void
- Signature: i2c_dev_set_name(struct i2c_adapter * adap,struct i2c_client * client,struct i2c_board_info const * info)
- Line: 875

### i2c_device_match
- Return type: static int
- Signature: i2c_device_match(struct device * dev,const struct device_driver * drv)
- Line: 139

### i2c_device_probe
- Return type: static int
- Signature: i2c_device_probe(struct device * dev)
- Line: 490

### i2c_device_remove
- Return type: static void
- Signature: i2c_device_remove(struct device * dev)
- Line: 621

### i2c_device_shutdown
- Return type: static void
- Signature: i2c_device_shutdown(struct device * dev)
- Line: 645

### i2c_device_uevent
- Return type: static int
- Signature: i2c_device_uevent(const struct device * dev,struct kobj_uevent_env * env)
- Line: 162

### i2c_do_add_adapter
- Return type: static int
- Signature: i2c_do_add_adapter(struct i2c_driver * driver,struct i2c_adapter * adap)
- Line: 1423

### i2c_do_del_adapter
- Return type: static void
- Signature: i2c_do_del_adapter(struct i2c_driver * driver,struct i2c_adapter * adapter)
- Line: 1708

### i2c_encode_flags_to_addr
- Return type: static unsigned short
- Signature: i2c_encode_flags_to_addr(struct i2c_client * client)
- Line: 734

### i2c_exit
- Return type: static void __exit
- Signature: i2c_exit(void)
- Line: 2120

### i2c_find_adapter_by_fwnode
- Return type: i2c_adapter *
- Signature: i2c_find_adapter_by_fwnode(struct fwnode_handle * fwnode)
- Line: 1872

### i2c_find_device_by_fwnode
- Return type: i2c_client *
- Signature: i2c_find_device_by_fwnode(struct fwnode_handle * fwnode)
- Line: 1087

### i2c_for_each_dev
- Return type: int
- Signature: i2c_for_each_dev(void * data,int (* fn)(struct device * dev,void * data))
- Line: 1978

### i2c_freq_mode_string
- Return type: const char *
- Signature: i2c_freq_mode_string(u32 bus_freq_hz)
- Line: 84

### i2c_generic_bus_free
- Return type: static int
- Signature: i2c_generic_bus_free(struct i2c_adapter * adap)
- Line: 199

### i2c_generic_scl_recovery
- Return type: int
- Signature: i2c_generic_scl_recovery(struct i2c_adapter * adap)
- Line: 223

### i2c_get_adapter
- Return type: i2c_adapter *
- Signature: i2c_get_adapter(int nr)
- Line: 2601

### i2c_get_adapter_by_fwnode
- Return type: i2c_adapter *
- Signature: i2c_get_adapter_by_fwnode(struct fwnode_handle * fwnode)
- Line: 1904

### i2c_get_device_id
- Return type: int
- Signature: i2c_get_device_id(const struct i2c_client * client,struct i2c_device_identity * id)
- Line: 2361

### i2c_get_dma_safe_msg_buf
- Return type: u8 *
- Signature: i2c_get_dma_safe_msg_buf(struct i2c_msg * msg,unsigned int threshold)
- Line: 2644

### i2c_get_match_data
- Return type: const void *
- Signature: i2c_get_match_data(const struct i2c_client * client)
- Line: 120

### i2c_gpio_init_generic_recovery
- Return type: static int
- Signature: i2c_gpio_init_generic_recovery(struct i2c_adapter * adap)
- Line: 351

### i2c_gpio_init_pinctrl_recovery
- Return type: static void
- Signature: i2c_gpio_init_pinctrl_recovery(struct i2c_adapter * adap)
- Line: 304

### i2c_gpio_init_recovery
- Return type: static int
- Signature: i2c_gpio_init_recovery(struct i2c_adapter * adap)
- Line: 419

### i2c_handle_smbus_host_notify
- Return type: int
- Signature: i2c_handle_smbus_host_notify(struct i2c_adapter * adap,unsigned short addr)
- Line: 1499

### i2c_host_notify_irq_map
- Return type: static int
- Signature: i2c_host_notify_irq_map(struct irq_domain * h,unsigned int virq,irq_hw_number_t hw_irq_num)
- Line: 1458

### i2c_host_notify_irq_teardown
- Return type: static void
- Signature: i2c_host_notify_irq_teardown(struct i2c_adapter * adap)
- Line: 1443

### i2c_init
- Return type: static int __init
- Signature: i2c_init(void)
- Line: 2084

### i2c_init_recovery
- Return type: static int
- Signature: i2c_init_recovery(struct i2c_adapter * adap)
- Line: 425

### i2c_lock_addr
- Return type: static int
- Signature: i2c_lock_addr(struct i2c_adapter * adap,unsigned short addr,unsigned short flags)
- Line: 925

### i2c_match_id
- Return type: const struct i2c_device_id *
- Signature: i2c_match_id(const struct i2c_device_id * id,const struct i2c_client * client)
- Line: 105

### i2c_new_ancillary_device
- Return type: i2c_client *
- Signature: i2c_new_ancillary_device(struct i2c_client * client,const char * name,u16 default_addr)
- Line: 1209

### i2c_new_client_device
- Return type: i2c_client *
- Signature: i2c_new_client_device(struct i2c_adapter * adap,struct i2c_board_info const * info)
- Line: 959

### i2c_new_dummy_device
- Return type: i2c_client *
- Signature: i2c_new_dummy_device(struct i2c_adapter * adapter,u16 address)
- Line: 1143

### i2c_new_scanned_device
- Return type: i2c_client *
- Signature: i2c_new_scanned_device(struct i2c_adapter * adap,struct i2c_board_info * info,unsigned short const * addr_list,int (* probe)(struct i2c_adapter * adap,unsigned short addr))
- Line: 2560

### i2c_parse_fw_timings
- Return type: void
- Signature: i2c_parse_fw_timings(struct device * dev,struct i2c_timings * t,bool use_defaults)
- Line: 1949

### i2c_parse_timing
- Return type: static void
- Signature: i2c_parse_timing(struct device * dev,char * prop_name,u32 * cur_val_p,u32 def_val,bool use_def)
- Line: 1921

### i2c_probe_func_quick_read
- Return type: int
- Signature: i2c_probe_func_quick_read(struct i2c_adapter * adap,unsigned short addr)
- Line: 2552

### i2c_put_adapter
- Return type: void
- Signature: i2c_put_adapter(struct i2c_adapter * adap)
- Line: 2621

### i2c_put_dma_safe_msg_buf
- Return type: void
- Signature: i2c_put_dma_safe_msg_buf(u8 * buf,struct i2c_msg * msg,bool xferred)
- Line: 2672

### i2c_quirk_error
- Return type: static int
- Signature: i2c_quirk_error(struct i2c_adapter * adap,struct i2c_msg * msg,char * err_msg)
- Line: 2146

### i2c_recover_bus
- Return type: int
- Signature: i2c_recover_bus(struct i2c_adapter * adap)
- Line: 294

### i2c_register_adapter
- Return type: static int
- Signature: i2c_register_adapter(struct i2c_adapter * adap)
- Line: 1518

### i2c_register_driver
- Return type: int
- Signature: i2c_register_driver(struct module * owner,struct i2c_driver * driver)
- Line: 2002

### i2c_scan_static_board_info
- Return type: static void
- Signature: i2c_scan_static_board_info(struct i2c_adapter * adapter)
- Line: 1408

### i2c_setup_host_notify_irq_domain
- Return type: static int
- Signature: i2c_setup_host_notify_irq_domain(struct i2c_adapter * adap)
- Line: 1471

### i2c_smbus_host_notify_to_irq
- Return type: static int
- Signature: i2c_smbus_host_notify_to_irq(const struct i2c_client * client)
- Line: 474

### i2c_transfer
- Return type: int
- Signature: i2c_transfer(struct i2c_adapter * adap,struct i2c_msg * msgs,int num)
- Line: 2292

### i2c_transfer_buffer_flags
- Return type: int
- Signature: i2c_transfer_buffer_flags(const struct i2c_client * client,char * buf,int count,u16 flags)
- Line: 2333

### i2c_transfer_trace_reg
- Return type: int
- Signature: i2c_transfer_trace_reg(void)
- Line: 73

### i2c_transfer_trace_unreg
- Return type: void
- Signature: i2c_transfer_trace_unreg(void)
- Line: 79

### i2c_unlock_addr
- Return type: static void
- Signature: i2c_unlock_addr(struct i2c_adapter * adap,unsigned short addr,unsigned short flags)
- Line: 935

### i2c_unregister_device
- Return type: void
- Signature: i2c_unregister_device(struct i2c_client * client)
- Line: 1053

### i2c_verify_adapter
- Return type: i2c_adapter *
- Signature: i2c_verify_adapter(struct device * dev)
- Line: 1400

### i2c_verify_client
- Return type: i2c_client *
- Signature: i2c_verify_client(struct device * dev)
- Line: 724

### modalias_show
- Return type: static ssize_t
- Signature: modalias_show(struct device * dev,struct device_attribute * attr,char * buf)
- Line: 673

### name_show
- Return type: static ssize_t
- Signature: name_show(struct device * dev,struct device_attribute * attr,char * buf)
- Line: 665

### new_device_store
- Return type: static ssize_t
- Signature: new_device_store(struct device * dev,struct device_attribute * attr,const char * buf,size_t count)
- Line: 1263

### set_scl_gpio_value
- Return type: static void
- Signature: set_scl_gpio_value(struct i2c_adapter * adap,int val)
- Line: 184

### set_sda_gpio_value
- Return type: static void
- Signature: set_sda_gpio_value(struct i2c_adapter * adap,int val)
- Line: 194

## Structs (1)

### i2c_cmd_arg
- Line: 2054
- Members:
  - cmd: unsigned
  - arg: void *

## Variables (11)

- static **dummy_driver** : i2c_driver (line 1119)
- static **dummy_id** : const struct i2c_device_id[] (line 1108)
- static **i2c_adapter_attrs** : attribute * [] (line 1377)
- static **i2c_adapter_lock_ops** : const struct i2c_lock_operations (line 1437)
- **i2c_adapter_type** : const struct device_type (line 1385)
- **i2c_bus_type** : const struct bus_type (line 698)
- **i2c_client_type** : const struct device_type (line 707)
- static **i2c_debugfs_root** : dentry * (line 71)
- static **i2c_dev_attrs** : attribute * [] (line 690)
- static **i2c_host_notify_irq_ops** : const struct irq_domain_ops (line 1467)
- static **is_registered** : bool (line 69)

## Macros (10)

- **CREATE_TRACE_POINTS** (line 48)
- **I2C_ADDR_7BITS_COUNT** (line 55)
- **I2C_ADDR_7BITS_MAX** (line 54)
- **I2C_ADDR_DEVICE_ID** (line 57)
- **I2C_ADDR_OFFSET_SLAVE** (line 52)
- **I2C_ADDR_OFFSET_TEN_BIT** (line 51)
- **RECOVERY_CLK_CNT** (line 221)
- **RECOVERY_NDELAY** (line 220)
- **i2c_quirk_exceeded**(val,quirk) (line 2144)
- **pr_fmt**(fmt) (line 13)
