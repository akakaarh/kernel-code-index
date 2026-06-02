# drivers/i2c/busses/i2c-opal.c

Subsystem: drivers/i2c

## Functions (9)

### i2c_opal_exit
- Return type: static void __exit
- Signature: i2c_opal_exit(void)
- Line: 268

### i2c_opal_func
- Return type: static u32
- Signature: i2c_opal_func(struct i2c_adapter * adapter)
- Line: 174

### i2c_opal_init
- Return type: static int __init
- Signature: i2c_opal_init(void)
- Line: 259

### i2c_opal_probe
- Return type: static int
- Signature: i2c_opal_probe(struct platform_device * pdev)
- Line: 196

### i2c_opal_remove
- Return type: static void
- Signature: i2c_opal_remove(struct platform_device * pdev)
- Line: 235

### i2c_opal_send_request
- Return type: static int
- Signature: i2c_opal_send_request(u32 bus_id,struct opal_i2c_request * req)
- Line: 39

### i2c_opal_smbus_xfer
- Return type: static int
- Signature: i2c_opal_smbus_xfer(struct i2c_adapter * adap,u16 addr,unsigned short flags,char read_write,u8 command,int size,union i2c_smbus_data * data)
- Line: 112

### i2c_opal_translate_error
- Return type: static int
- Signature: i2c_opal_translate_error(int rc)
- Line: 19

### i2c_opal_xfer
- Return type: static int
- Signature: i2c_opal_xfer(struct i2c_adapter * adap,struct i2c_msg * msgs,int num)
- Line: 73

## Variables (4)

- static **i2c_opal_algo** : const struct i2c_algorithm (line 181)
- static **i2c_opal_driver** : platform_driver (line 250)
- static **i2c_opal_of_match** : const struct of_device_id[] (line 242)
- static **i2c_opal_quirks** : const struct i2c_adapter_quirks (line 191)
