# drivers/i2c/busses/i2c-lpc2k.c

Subsystem: drivers/i2c

## Functions (11)

### i2c_lpc2k_clear_arb
- Return type: static int
- Signature: i2c_lpc2k_clear_arb(struct lpc2k_i2c * i2c)
- Line: 91

### i2c_lpc2k_functionality
- Return type: static u32
- Signature: i2c_lpc2k_functionality(struct i2c_adapter * adap)
- Line: 334

### i2c_lpc2k_handler
- Return type: static irqreturn_t
- Signature: i2c_lpc2k_handler(int irq,void * dev_id)
- Line: 322

### i2c_lpc2k_probe
- Return type: static int
- Signature: i2c_lpc2k_probe(struct platform_device * pdev)
- Line: 345

### i2c_lpc2k_pump_msg
- Return type: static void
- Signature: i2c_lpc2k_pump_msg(struct lpc2k_i2c * i2c)
- Line: 115

### i2c_lpc2k_remove
- Return type: static void
- Signature: i2c_lpc2k_remove(struct platform_device * dev)
- Line: 426

### i2c_lpc2k_reset
- Return type: static void
- Signature: i2c_lpc2k_reset(struct lpc2k_i2c * i2c)
- Line: 83

### i2c_lpc2k_resume
- Return type: static int
- Signature: i2c_lpc2k_resume(struct device * dev)
- Line: 442

### i2c_lpc2k_suspend
- Return type: static int
- Signature: i2c_lpc2k_suspend(struct device * dev)
- Line: 433

### i2c_lpc2k_xfer
- Return type: static int
- Signature: i2c_lpc2k_xfer(struct i2c_adapter * adap,struct i2c_msg * msgs,int msg_num)
- Line: 292

### lpc2k_process_msg
- Return type: static int
- Signature: lpc2k_process_msg(struct lpc2k_i2c * i2c,int msgidx)
- Line: 251

## Structs (1)

### lpc2k_i2c
- Line: 71
- Members:
  - base: void __iomem *
  - clk: clk *
  - irq: int
  - wait: wait_queue_head_t
  - adap: i2c_adapter
  - msg: i2c_msg *
  - msg_idx: int
  - msg_status: int
  - is_last: int

## Enums (1)

### __anon73feada60103
- Line: 55

## Variables (4)

- static **i2c_lpc2k_algorithm** : const struct i2c_algorithm (line 340)
- static **i2c_lpc2k_dev_pm_ops** : const struct dev_pm_ops (line 457)
- static **i2c_lpc2k_driver** : platform_driver (line 468)
- static **lpc2k_i2c_match** : const struct of_device_id[] (line 462)

## Macros (17)

- **I2C_FAST_MODE_DUTY** (line 48)
- **I2C_FAST_MODE_PLUS_DUTY** (line 49)
- **I2C_STD_MODE_DUTY** (line 47)
- **LPC24XX_AA** (line 36)
- **LPC24XX_CLEAR_ALL** (line 43)
- **LPC24XX_I2ADDR** (line 31)
- **LPC24XX_I2CONCLR** (line 34)
- **LPC24XX_I2CONSET** (line 28)
- **LPC24XX_I2DAT** (line 30)
- **LPC24XX_I2EN** (line 40)
- **LPC24XX_I2SCLH** (line 32)
- **LPC24XX_I2SCLL** (line 33)
- **LPC24XX_I2STAT** (line 29)
- **LPC24XX_SI** (line 37)
- **LPC24XX_STA** (line 39)
- **LPC24XX_STO** (line 38)
- **LPC24XX_STO_AA** (line 42)
