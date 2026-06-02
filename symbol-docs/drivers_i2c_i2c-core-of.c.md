# drivers/i2c/i2c-core-of.c

Subsystem: drivers/i2c

## Functions (6)

### i2c_of_match_device
- Return type: const struct of_device_id *
- Signature: i2c_of_match_device(const struct of_device_id * matches,struct i2c_client * client)
- Line: 145

### i2c_of_match_device_sysfs
- Return type: static const struct of_device_id *
- Signature: i2c_of_match_device_sysfs(const struct of_device_id * matches,struct i2c_client * client)
- Line: 116

### of_i2c_get_board_info
- Return type: int
- Signature: of_i2c_get_board_info(struct device * dev,struct device_node * node,struct i2c_board_info * info)
- Line: 22

### of_i2c_notify
- Return type: static int
- Signature: of_i2c_notify(struct notifier_block * nb,unsigned long action,void * arg)
- Line: 161

### of_i2c_register_device
- Return type: static i2c_client *
- Signature: of_i2c_register_device(struct i2c_adapter * adap,struct device_node * node)
- Line: 64

### of_i2c_register_devices
- Return type: void
- Signature: of_i2c_register_devices(struct i2c_adapter * adap)
- Line: 84

## Variables (1)

- **i2c_of_notifier** : notifier_block (line 215)
