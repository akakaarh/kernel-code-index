# drivers/i2c/busses/i2c-versatile.c

Subsystem: drivers/i2c

## Functions (8)

### i2c_versatile_exit
- Return type: static void __exit
- Signature: i2c_versatile_exit(void)
- Line: 124

### i2c_versatile_getscl
- Return type: static int
- Signature: i2c_versatile_getscl(void * data)
- Line: 49

### i2c_versatile_getsda
- Return type: static int
- Signature: i2c_versatile_getsda(void * data)
- Line: 43

### i2c_versatile_init
- Return type: static int __init
- Signature: i2c_versatile_init(void)
- Line: 119

### i2c_versatile_probe
- Return type: static int
- Signature: i2c_versatile_probe(struct platform_device * dev)
- Line: 64

### i2c_versatile_remove
- Return type: static void
- Signature: i2c_versatile_remove(struct platform_device * dev)
- Line: 97

### i2c_versatile_setscl
- Return type: static void
- Signature: i2c_versatile_setscl(void * data,int state)
- Line: 36

### i2c_versatile_setsda
- Return type: static void
- Signature: i2c_versatile_setsda(void * data,int state)
- Line: 29

## Structs (1)

### i2c_versatile
- Line: 23
- Members:
  - adap: i2c_adapter
  - algo: i2c_algo_bit_data
  - base: void __iomem *

## Variables (3)

- static **i2c_versatile_algo** : const struct i2c_algo_bit_data (line 55)
- static **i2c_versatile_driver** : platform_driver (line 110)
- static **i2c_versatile_match** : const struct of_device_id[] (line 104)

## Macros (5)

- **I2C_CONTROL** (line 17)
- **I2C_CONTROLC** (line 19)
- **I2C_CONTROLS** (line 18)
- **SCL** (line 20)
- **SDA** (line 21)
