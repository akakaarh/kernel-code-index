# drivers/i2c/busses/i2c-kempld.c

Subsystem: drivers/i2c

## Functions (8)

### kempld_i2c_device_init
- Return type: static void
- Signature: kempld_i2c_device_init(struct kempld_i2c_data * i2c)
- Line: 222

### kempld_i2c_func
- Return type: static u32
- Signature: kempld_i2c_func(struct i2c_adapter * adap)
- Line: 273

### kempld_i2c_probe
- Return type: static int
- Signature: kempld_i2c_probe(struct platform_device * pdev)
- Line: 290

### kempld_i2c_process
- Return type: static int
- Signature: kempld_i2c_process(struct kempld_i2c_data * i2c)
- Line: 82

### kempld_i2c_remove
- Return type: static void
- Signature: kempld_i2c_remove(struct platform_device * pdev)
- Line: 331

### kempld_i2c_resume
- Return type: static int
- Signature: kempld_i2c_resume(struct device * dev)
- Line: 367

### kempld_i2c_suspend
- Return type: static int
- Signature: kempld_i2c_suspend(struct device * dev)
- Line: 352

### kempld_i2c_xfer
- Return type: static int
- Signature: kempld_i2c_xfer(struct i2c_adapter * adap,struct i2c_msg * msgs,int num)
- Line: 186

## Structs (1)

### kempld_i2c_data
- Line: 55
- Members:
  - dev: device *
  - pld: kempld_device_data *
  - adap: i2c_adapter
  - msg: i2c_msg *
  - pos: int
  - nmsgs: int
  - state: int
  - was_active: bool

## Enums (1)

### __anond488e2670103
- Line: 44

## Variables (6)

- static **bus_frequency** : unsigned int (line 66)
- static **i2c_bus** : int (line 71)
- static **i2c_gpio_mux** : bool (line 75)
- static **kempld_i2c_adapter** : const struct i2c_adapter (line 283)
- static **kempld_i2c_algorithm** : const struct i2c_algorithm (line 278)
- static **kempld_i2c_driver** : platform_driver (line 382)

## Macros (22)

- **I2C_CMD_IACK** (line 39)
- **I2C_CMD_READ** (line 35)
- **I2C_CMD_READ_ACK** (line 37)
- **I2C_CMD_READ_NACK** (line 38)
- **I2C_CMD_START** (line 33)
- **I2C_CMD_STOP** (line 34)
- **I2C_CMD_WRITE** (line 36)
- **I2C_CTRL_EN** (line 23)
- **I2C_CTRL_IEN** (line 22)
- **I2C_STAT_ARBLOST** (line 28)
- **I2C_STAT_BUSY** (line 29)
- **I2C_STAT_IF** (line 26)
- **I2C_STAT_NACK** (line 30)
- **I2C_STAT_TIP** (line 27)
- **KEMPLD_I2C_CMD** (line 32)
- **KEMPLD_I2C_CTRL** (line 21)
- **KEMPLD_I2C_DATA** (line 19)
- **KEMPLD_I2C_FREQ_MAX** (line 41)
- **KEMPLD_I2C_FREQ_STD** (line 42)
- **KEMPLD_I2C_PREHIGH** (line 18)
- **KEMPLD_I2C_PRELOW** (line 17)
- **KEMPLD_I2C_STAT** (line 25)
