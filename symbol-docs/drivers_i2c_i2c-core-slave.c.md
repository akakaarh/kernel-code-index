# drivers/i2c/i2c-core-slave.c

Subsystem: drivers/i2c

## Functions (4)

### i2c_detect_slave_mode
- Return type: bool
- Signature: i2c_detect_slave_mode(struct device * dev)
- Line: 110

### i2c_slave_event
- Return type: int
- Signature: i2c_slave_event(struct i2c_client * client,enum i2c_slave_event event,u8 * val)
- Line: 86

### i2c_slave_register
- Return type: int
- Signature: i2c_slave_register(struct i2c_client * client,i2c_slave_cb_t slave_cb)
- Line: 21

### i2c_slave_unregister
- Return type: int
- Signature: i2c_slave_unregister(struct i2c_client * client)
- Line: 61

## Macros (1)

- **CREATE_TRACE_POINTS** (line 18)
