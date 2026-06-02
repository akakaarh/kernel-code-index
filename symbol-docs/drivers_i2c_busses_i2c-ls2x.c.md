# drivers/i2c/busses/i2c-ls2x.c

Subsystem: drivers/i2c

## Functions (15)

### ls2x_i2c_adjust_bus_speed
- Return type: static void
- Signature: ls2x_i2c_adjust_bus_speed(struct ls2x_i2c_priv * priv)
- Line: 96

### ls2x_i2c_func
- Return type: static unsigned int
- Signature: ls2x_i2c_func(struct i2c_adapter * adap)
- Line: 277

### ls2x_i2c_init
- Return type: static void
- Signature: ls2x_i2c_init(struct ls2x_i2c_priv * priv)
- Line: 120

### ls2x_i2c_isr
- Return type: static irqreturn_t
- Signature: ls2x_i2c_isr(int this_irq,void * dev_id)
- Line: 77

### ls2x_i2c_probe
- Return type: static int
- Signature: ls2x_i2c_probe(struct platform_device * pdev)
- Line: 287

### ls2x_i2c_resume
- Return type: static int
- Signature: ls2x_i2c_resume(struct device * dev)
- Line: 342

### ls2x_i2c_rx
- Return type: static int
- Signature: ls2x_i2c_rx(struct ls2x_i2c_priv * priv,struct i2c_msg * msg)
- Line: 188

### ls2x_i2c_send_byte
- Return type: static int
- Signature: ls2x_i2c_send_byte(struct ls2x_i2c_priv * priv,u8 txdata)
- Line: 152

### ls2x_i2c_start
- Return type: static int
- Signature: ls2x_i2c_start(struct ls2x_i2c_priv * priv,struct i2c_msg * msgs)
- Line: 180

### ls2x_i2c_stop
- Return type: static int
- Signature: ls2x_i2c_stop(struct ls2x_i2c_priv * priv)
- Line: 170

### ls2x_i2c_suspend
- Return type: static int
- Signature: ls2x_i2c_suspend(struct device * dev)
- Line: 331

### ls2x_i2c_tx
- Return type: static int
- Signature: ls2x_i2c_tx(struct ls2x_i2c_priv * priv,struct i2c_msg * msg)
- Line: 212

### ls2x_i2c_xfer
- Return type: static int
- Signature: ls2x_i2c_xfer(struct i2c_adapter * adap,struct i2c_msg * msgs,int num)
- Line: 262

### ls2x_i2c_xfer_byte
- Return type: static int
- Signature: ls2x_i2c_xfer_byte(struct ls2x_i2c_priv * priv,u8 txdata,u8 * rxdatap)
- Line: 133

### ls2x_i2c_xfer_one
- Return type: static int
- Signature: ls2x_i2c_xfer_one(struct ls2x_i2c_priv * priv,struct i2c_msg * msg,bool stop)
- Line: 234

## Structs (1)

### ls2x_i2c_priv
- Line: 66
- Members:
  - adapter: i2c_adapter
  - base: void __iomem *
  - i2c_t: i2c_timings
  - cmd_complete: completion

## Variables (4)

- static **ls2x_i2c_acpi_match** : const struct acpi_device_id[] (line 358)
- static **ls2x_i2c_algo** : const struct i2c_algorithm (line 282)
- static **ls2x_i2c_driver** : platform_driver (line 364)
- static **ls2x_i2c_id_table** : const struct of_device_id[] (line 351)

## Macros (25)

- **CTR_FREQ_MASK** (line 57)
- **CTR_READY_MASK** (line 58)
- **I2C_LS2X_CR** (line 35)
- **I2C_LS2X_CTR** (line 32)
- **I2C_LS2X_PRER_HI** (line 31)
- **I2C_LS2X_PRER_LO** (line 30)
- **I2C_LS2X_RXR** (line 34)
- **I2C_LS2X_SR** (line 36)
- **I2C_LS2X_TXR** (line 33)
- **LS2X_CR_ACK** (line 43)
- **LS2X_CR_IACK** (line 44)
- **LS2X_CR_READ** (line 41)
- **LS2X_CR_START** (line 39)
- **LS2X_CR_STOP** (line 40)
- **LS2X_CR_WRITE** (line 42)
- **LS2X_CTR_EN** (line 54)
- **LS2X_CTR_IEN** (line 55)
- **LS2X_CTR_MST** (line 56)
- **LS2X_I2C_FREQ_STD** (line 64)
- **LS2X_I2C_PCLK_FREQ** (line 61)
- **LS2X_SR_AL** (line 49)
- **LS2X_SR_BUSY** (line 48)
- **LS2X_SR_IF** (line 51)
- **LS2X_SR_NOACK** (line 47)
- **LS2X_SR_TIP** (line 50)
