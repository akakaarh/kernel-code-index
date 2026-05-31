# drivers/gpio/gpio-max7300.c

Subsystem: drivers/gpio

## Functions (6)

### max7300_exit
- Return type: static void __exit
- Signature: max7300_exit(void)
- Line: 76

### max7300_i2c_read
- Return type: static int
- Signature: max7300_i2c_read(struct device * dev,unsigned int reg)
- Line: 24

### max7300_i2c_write
- Return type: static int
- Signature: max7300_i2c_write(struct device * dev,unsigned int reg,unsigned int val)
- Line: 16

### max7300_init
- Return type: static int __init
- Signature: max7300_init(void)
- Line: 70

### max7300_probe
- Return type: static int
- Signature: max7300_probe(struct i2c_client * client)
- Line: 31
- Calls: __max730x_probe

### max7300_remove
- Return type: static void
- Signature: max7300_remove(struct i2c_client * client)
- Line: 50
- Calls: __max730x_remove

## Variables (2)

- static **max7300_driver** : i2c_driver (line 61)
- static **max7300_id** : const struct i2c_device_id[] (line 55)
