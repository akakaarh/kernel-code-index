# drivers/i2c/busses/i2c-powermac.c

Subsystem: drivers/i2c

## Functions (10)

### i2c_powermac_add_missing
- Return type: static void
- Signature: i2c_powermac_add_missing(struct i2c_adapter * adap,struct pmac_i2c_bus * bus,bool found_onyx)
- Line: 243

### i2c_powermac_create_one
- Return type: static void
- Signature: i2c_powermac_create_one(struct i2c_adapter * adap,const char * type,u32 addr)
- Line: 227

### i2c_powermac_func
- Return type: static u32
- Signature: i2c_powermac_func(struct i2c_adapter * adapter)
- Line: 173

### i2c_powermac_get_addr
- Return type: static u32
- Signature: i2c_powermac_get_addr(struct i2c_adapter * adap,struct pmac_i2c_bus * bus,struct device_node * node)
- Line: 199

### i2c_powermac_get_type
- Return type: static bool
- Signature: i2c_powermac_get_type(struct i2c_adapter * adap,struct device_node * node,u32 addr,char * type,int type_size)
- Line: 269

### i2c_powermac_probe
- Return type: static int
- Signature: i2c_powermac_probe(struct platform_device * dev)
- Line: 372

### i2c_powermac_register_devices
- Return type: static void
- Signature: i2c_powermac_register_devices(struct i2c_adapter * adap,struct pmac_i2c_bus * bus)
- Line: 306

### i2c_powermac_remove
- Return type: static void
- Signature: i2c_powermac_remove(struct platform_device * dev)
- Line: 191

### i2c_powermac_smbus_xfer
- Return type: static s32
- Signature: i2c_powermac_smbus_xfer(struct i2c_adapter * adap,u16 addr,unsigned short flags,char read_write,u8 command,int size,union i2c_smbus_data * data)
- Line: 28

### i2c_powermac_xfer
- Return type: static int
- Signature: i2c_powermac_xfer(struct i2c_adapter * adap,struct i2c_msg * msgs,int num)
- Line: 134

## Variables (3)

- static **i2c_powermac_algorithm** : const struct i2c_algorithm (line 181)
- static **i2c_powermac_driver** : platform_driver (line 438)
- static **i2c_powermac_quirks** : const struct i2c_adapter_quirks (line 187)

## Macros (1)

- **ONYX_REG_CONTROL** (line 251)
