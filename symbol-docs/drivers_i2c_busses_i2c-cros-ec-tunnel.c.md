# drivers/i2c/busses/i2c-cros-ec-tunnel.c

Subsystem: drivers/i2c

## Functions (8)

### ec_i2c_construct_message
- Return type: static int
- Signature: ec_i2c_construct_message(u8 * buf,const struct i2c_msg i2c_msgs[],int num,u16 bus_num)
- Line: 73

### ec_i2c_count_message
- Return type: static int
- Signature: ec_i2c_count_message(const struct i2c_msg i2c_msgs[],int num)
- Line: 46

### ec_i2c_count_response
- Return type: static int
- Signature: ec_i2c_count_response(struct i2c_msg i2c_msgs[],int num)
- Line: 115

### ec_i2c_functionality
- Return type: static u32
- Signature: ec_i2c_functionality(struct i2c_adapter * adap)
- Line: 232

### ec_i2c_parse_response
- Return type: static int
- Signature: ec_i2c_parse_response(const u8 * buf,struct i2c_msg i2c_msgs[],int * num)
- Line: 140

### ec_i2c_probe
- Return type: static int
- Signature: ec_i2c_probe(struct platform_device * pdev)
- Line: 242

### ec_i2c_remove
- Return type: static void
- Signature: ec_i2c_remove(struct platform_device * dev)
- Line: 289

### ec_i2c_xfer
- Return type: static int
- Signature: ec_i2c_xfer(struct i2c_adapter * adap,struct i2c_msg i2c_msgs[],int num)
- Line: 174

## Structs (1)

### ec_i2c_device
- Line: 27
- Members:
  - dev: device *
  - adap: i2c_adapter
  - ec: cros_ec_device *
  - remote_bus: u16
  - request_buf: u8[256]
  - response_buf: u8[256]

## Variables (4)

- static **cros_ec_i2c_of_match** : const struct of_device_id[]__maybe_unused (line 296)
- static **cros_ec_i2c_tunnel_acpi_id** : const struct acpi_device_id[]__maybe_unused (line 302)
- static **ec_i2c_algorithm** : const struct i2c_algorithm (line 237)
- static **ec_i2c_tunnel_driver** : platform_driver (line 308)

## Macros (1)

- **I2C_MAX_RETRIES** (line 14)
