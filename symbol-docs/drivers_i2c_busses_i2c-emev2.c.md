# drivers/i2c/busses/i2c-emev2.c

Subsystem: drivers/i2c

## Functions (13)

### __em_i2c_xfer
- Return type: static int
- Signature: __em_i2c_xfer(struct i2c_adapter * adap,struct i2c_msg * msg,int stop)
- Line: 138

### em_clear_set_bit
- Return type: static void
- Signature: em_clear_set_bit(struct em_i2c_device * priv,u8 clear,u8 set,u8 reg)
- Line: 74

### em_i2c_func
- Return type: static u32
- Signature: em_i2c_func(struct i2c_adapter * adap)
- Line: 311

### em_i2c_irq_handler
- Return type: static irqreturn_t
- Signature: em_i2c_irq_handler(int this_irq,void * dev_id)
- Line: 299

### em_i2c_probe
- Return type: static int
- Signature: em_i2c_probe(struct platform_device * pdev)
- Line: 360

### em_i2c_reg_slave
- Return type: static int
- Signature: em_i2c_reg_slave(struct i2c_client * slave)
- Line: 316

### em_i2c_remove
- Return type: static void
- Signature: em_i2c_remove(struct platform_device * dev)
- Line: 414

### em_i2c_reset
- Return type: static void
- Signature: em_i2c_reset(struct i2c_adapter * adap)
- Line: 104

### em_i2c_slave_irq
- Return type: static bool
- Signature: em_i2c_slave_irq(struct em_i2c_device * priv)
- Line: 227

### em_i2c_stop
- Return type: static void
- Signature: em_i2c_stop(struct em_i2c_device * priv)
- Line: 95

### em_i2c_unreg_slave
- Return type: static int
- Signature: em_i2c_unreg_slave(struct i2c_client * slave)
- Line: 334

### em_i2c_wait_for_event
- Return type: static int
- Signature: em_i2c_wait_for_event(struct em_i2c_device * priv)
- Line: 79

### em_i2c_xfer
- Return type: static int
- Signature: em_i2c_xfer(struct i2c_adapter * adap,struct i2c_msg * msgs,int num)
- Line: 208

## Structs (1)

### em_i2c_device
- Line: 66
- Members:
  - base: void __iomem *
  - adap: i2c_adapter
  - msg_done: completion
  - slave: i2c_client *
  - irq: int

## Variables (3)

- static **em_i2c_algo** : const struct i2c_algorithm (line 353)
- static **em_i2c_driver** : platform_driver (line 426)
- static **em_i2c_ids** : const struct of_device_id[] (line 421)

## Macros (31)

- **I2C_BIT_ACKD0** (line 56)
- **I2C_BIT_ACKE0** (line 42)
- **I2C_BIT_ALD0** (line 52)
- **I2C_BIT_COI0** (line 54)
- **I2C_BIT_DFC0** (line 48)
- **I2C_BIT_EXC0** (line 53)
- **I2C_BIT_IICBSY** (line 62)
- **I2C_BIT_IICE0** (line 35)
- **I2C_BIT_IICRSV** (line 64)
- **I2C_BIT_LREL0** (line 38)
- **I2C_BIT_MSTS0** (line 51)
- **I2C_BIT_SMC0** (line 47)
- **I2C_BIT_SPD0** (line 58)
- **I2C_BIT_SPIE0** (line 40)
- **I2C_BIT_SPT0** (line 44)
- **I2C_BIT_STCEN** (line 63)
- **I2C_BIT_STCF** (line 61)
- **I2C_BIT_STD0** (line 57)
- **I2C_BIT_STT0** (line 43)
- **I2C_BIT_TRC0** (line 55)
- **I2C_BIT_WREL0** (line 39)
- **I2C_BIT_WTIM0** (line 41)
- **I2C_OFS_IIC0** (line 25)
- **I2C_OFS_IICACT0** (line 24)
- **I2C_OFS_IICC0** (line 26)
- **I2C_OFS_IICCL0** (line 28)
- **I2C_OFS_IICF0** (line 32)
- **I2C_OFS_IICS0** (line 30)
- **I2C_OFS_IICSE0** (line 31)
- **I2C_OFS_IICX0** (line 29)
- **I2C_OFS_SVA0** (line 27)
