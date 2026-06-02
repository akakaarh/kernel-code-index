# drivers/i2c/i2c-core-acpi.c

Subsystem: drivers/i2c

## Functions (24)

### acpi_gsb_i2c_read_bytes
- Return type: static int
- Signature: acpi_gsb_i2c_read_bytes(struct i2c_client * client,u8 cmd,u8 * data,u8 data_len)
- Line: 590

### acpi_gsb_i2c_write_bytes
- Return type: static int
- Signature: acpi_gsb_i2c_write_bytes(struct i2c_client * client,u8 cmd,u8 * data,u8 data_len)
- Line: 633

### i2c_acpi_add_device
- Return type: static acpi_status
- Signature: i2c_acpi_add_device(acpi_handle handle,u32 level,void * data,void ** return_value)
- Line: 295

### i2c_acpi_add_irq_resource
- Return type: static int
- Signature: i2c_acpi_add_irq_resource(struct acpi_resource * ares,void * data)
- Line: 176

### i2c_acpi_client_count
- Return type: int
- Signature: i2c_acpi_client_count(struct acpi_device * adev)
- Line: 90

### i2c_acpi_do_lookup
- Return type: static int
- Signature: i2c_acpi_do_lookup(struct acpi_device * adev,struct i2c_acpi_lookup * lookup)
- Line: 145

### i2c_acpi_fill_info
- Return type: static int
- Signature: i2c_acpi_fill_info(struct acpi_resource * ares,void * data)
- Line: 104

### i2c_acpi_find_adapter_by_adev
- Return type: static i2c_adapter *
- Signature: i2c_acpi_find_adapter_by_adev(struct acpi_device * adev)
- Line: 472

### i2c_acpi_find_adapter_by_handle
- Return type: i2c_adapter *
- Signature: i2c_acpi_find_adapter_by_handle(acpi_handle handle)
- Line: 450

### i2c_acpi_find_bus_speed
- Return type: u32
- Signature: i2c_acpi_find_bus_speed(struct device * dev)
- Line: 412

### i2c_acpi_find_client_by_adev
- Return type: static i2c_client *
- Signature: i2c_acpi_find_client_by_adev(struct acpi_device * adev)
- Line: 467

### i2c_acpi_get_i2c_resource
- Return type: bool
- Signature: i2c_acpi_get_i2c_resource(struct acpi_resource * ares,struct acpi_resource_i2c_serialbus ** i2c)
- Line: 55

### i2c_acpi_get_info
- Return type: static int
- Signature: i2c_acpi_get_info(struct acpi_device * adev,struct i2c_board_info * info,struct i2c_adapter * adapter,acpi_handle * adapter_handle)
- Line: 232

### i2c_acpi_get_irq
- Return type: int
- Signature: i2c_acpi_get_irq(struct i2c_client * client,bool * wake_capable)
- Line: 202

### i2c_acpi_install_space_handler
- Return type: int
- Signature: i2c_acpi_install_space_handler(struct i2c_adapter * adapter)
- Line: 783

### i2c_acpi_lookup_speed
- Return type: static acpi_status
- Signature: i2c_acpi_lookup_speed(acpi_handle handle,u32 level,void * data,void ** return_value)
- Line: 379

### i2c_acpi_new_device_by_fwnode
- Return type: i2c_client *
- Signature: i2c_acpi_new_device_by_fwnode(struct fwnode_handle * fwnode,int index,struct i2c_board_info * info)
- Line: 542

### i2c_acpi_notify
- Return type: static int
- Signature: i2c_acpi_notify(struct notifier_block * nb,unsigned long value,void * arg)
- Line: 477

### i2c_acpi_register_device
- Return type: static void
- Signature: i2c_acpi_register_device(struct i2c_adapter * adapter,struct acpi_device * adev,struct i2c_board_info * info)
- Line: 277

### i2c_acpi_register_devices
- Return type: void
- Signature: i2c_acpi_register_devices(struct i2c_adapter * adap)
- Line: 320

### i2c_acpi_remove_space_handler
- Return type: void
- Signature: i2c_acpi_remove_space_handler(struct i2c_adapter * adapter)
- Line: 823

### i2c_acpi_resource_count
- Return type: static int
- Signature: i2c_acpi_resource_count(struct acpi_resource * ares,void * data)
- Line: 72

### i2c_acpi_space_handler
- Return type: static acpi_status
- Signature: i2c_acpi_space_handler(u32 function,acpi_physical_address command,u32 bits,u64 * value64,void * handler_context,void * region_context)
- Line: 667

### i2c_acpi_waive_d0_probe
- Return type: bool
- Signature: i2c_acpi_waive_d0_probe(struct device * dev)
- Line: 579

## Structs (4)

### gsb_buffer
- Line: 23
- Members:
  - info: acpi_connection_info
  - adapter: i2c_adapter *
  - status: u8
  - len: u8
  - wdata: u16
  - bdata: u8
  - info: i2c_board_info *
  - adapter_handle: acpi_handle
  - device_handle: acpi_handle
  - search_handle: acpi_handle
  - n: int
  - index: int
  - speed: u32
  - min_speed: u32
  - force_speed: u32
  - irq: int
  - wake_capable: bool

### i2c_acpi_handler_data
- Line: 18
- Members:
  - info: acpi_connection_info
  - adapter: i2c_adapter *
  - status: u8
  - len: u8
  - wdata: u16
  - bdata: u8
  - info: i2c_board_info *
  - adapter_handle: acpi_handle
  - device_handle: acpi_handle
  - search_handle: acpi_handle
  - n: int
  - index: int
  - speed: u32
  - min_speed: u32
  - force_speed: u32
  - irq: int
  - wake_capable: bool

### i2c_acpi_irq_context
- Line: 140
- Members:
  - info: acpi_connection_info
  - adapter: i2c_adapter *
  - status: u8
  - len: u8
  - wdata: u16
  - bdata: u8
  - info: i2c_board_info *
  - adapter_handle: acpi_handle
  - device_handle: acpi_handle
  - search_handle: acpi_handle
  - n: int
  - index: int
  - speed: u32
  - min_speed: u32
  - force_speed: u32
  - irq: int
  - wake_capable: bool

### i2c_acpi_lookup
- Line: 33
- Members:
  - info: acpi_connection_info
  - adapter: i2c_adapter *
  - status: u8
  - len: u8
  - wdata: u16
  - bdata: u8
  - info: i2c_board_info *
  - adapter_handle: acpi_handle
  - device_handle: acpi_handle
  - search_handle: acpi_handle
  - n: int
  - index: int
  - speed: u32
  - min_speed: u32
  - force_speed: u32
  - irq: int
  - wake_capable: bool

## Unions (1)

### __anon584fd2f9010a
- Line: 26
- Members:
  - info: acpi_connection_info
  - adapter: i2c_adapter *
  - status: u8
  - len: u8
  - wdata: u16
  - bdata: u8
  - info: i2c_board_info *
  - adapter_handle: acpi_handle
  - device_handle: acpi_handle
  - search_handle: acpi_handle
  - n: int
  - index: int
  - speed: u32
  - min_speed: u32
  - force_speed: u32
  - irq: int
  - wake_capable: bool

## Variables (5)

- **__packed** : gsb_buffer (line 31)
- static **i2c_acpi_force_100khz_device_ids** : const struct acpi_device_id[] (line 358)
- static **i2c_acpi_force_400khz_device_ids** : const struct acpi_device_id[] (line 345)
- static **i2c_acpi_ignored_device_ids** : const struct acpi_device_id[] (line 131)
- **i2c_acpi_notifier** : notifier_block (line 520)

## Macros (1)

- **I2C_ACPI_MAX_SCAN_DEPTH** (line 310)
