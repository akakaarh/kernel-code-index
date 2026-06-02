# drivers/i2c/busses/i2c-owl.c

Subsystem: drivers/i2c

## Functions (12)

### owl_i2c_check_bus_busy
- Return type: static int
- Signature: owl_i2c_check_bus_busy(struct i2c_adapter * adap)
- Line: 235

### owl_i2c_func
- Return type: static u32
- Signature: owl_i2c_func(struct i2c_adapter * adap)
- Line: 230

### owl_i2c_interrupt
- Return type: static irqreturn_t
- Signature: owl_i2c_interrupt(int irq,void * _dev)
- Line: 212

### owl_i2c_probe
- Return type: static int
- Signature: owl_i2c_probe(struct platform_device * pdev)
- Line: 436

### owl_i2c_reset
- Return type: static void
- Signature: owl_i2c_reset(struct owl_i2c_dev * i2c_dev)
- Line: 121

### owl_i2c_reset_fifo
- Return type: static int
- Signature: owl_i2c_reset_fifo(struct owl_i2c_dev * i2c_dev)
- Line: 133

### owl_i2c_set_freq
- Return type: static void
- Signature: owl_i2c_set_freq(struct owl_i2c_dev * i2c_dev)
- Line: 158

### owl_i2c_update_reg
- Return type: static void
- Signature: owl_i2c_update_reg(void __iomem * reg,unsigned int val,bool state)
- Line: 107

### owl_i2c_xfer
- Return type: static int
- Signature: owl_i2c_xfer(struct i2c_adapter * adap,struct i2c_msg * msgs,int num)
- Line: 410

### owl_i2c_xfer_atomic
- Return type: static int
- Signature: owl_i2c_xfer_atomic(struct i2c_adapter * adap,struct i2c_msg * msgs,int num)
- Line: 416

### owl_i2c_xfer_common
- Return type: static int
- Signature: owl_i2c_xfer_common(struct i2c_adapter * adap,struct i2c_msg * msgs,int num,bool atomic)
- Line: 252

### owl_i2c_xfer_data
- Return type: static void
- Signature: owl_i2c_xfer_data(struct owl_i2c_dev * i2c_dev)
- Line: 168

## Structs (1)

### owl_i2c_dev
- Line: 94
- Members:
  - adap: i2c_adapter
  - msg: i2c_msg *
  - msg_complete: completion
  - clk: clk *
  - lock: spinlock_t
  - base: void __iomem *
  - clk_rate: unsigned long
  - bus_freq: u32
  - msg_ptr: u32
  - err: int

## Variables (4)

- static **owl_i2c_algorithm** : const struct i2c_algorithm (line 422)
- static **owl_i2c_driver** : platform_driver (line 509)
- static **owl_i2c_of_match** : const struct of_device_id[] (line 501)
- static **owl_i2c_quirks** : const struct i2c_adapter_quirks (line 428)

## Macros (55)

- **OWL_I2C_CMD_AS**(x) (line 72)
- **OWL_I2C_CMD_DE** (line 65)
- **OWL_I2C_CMD_MSS** (line 68)
- **OWL_I2C_CMD_NS** (line 66)
- **OWL_I2C_CMD_RBE** (line 64)
- **OWL_I2C_CMD_SAS**(x) (line 73)
- **OWL_I2C_CMD_SBE** (line 63)
- **OWL_I2C_CMD_SE** (line 67)
- **OWL_I2C_CMD_SECL** (line 70)
- **OWL_I2C_CMD_WRS** (line 69)
- **OWL_I2C_CTL_AE** (line 44)
- **OWL_I2C_CTL_EN** (line 43)
- **OWL_I2C_CTL_GBCC**(x) (line 37)
- **OWL_I2C_CTL_GBCC_NONE** (line 38)
- **OWL_I2C_CTL_GBCC_RSTART** (line 41)
- **OWL_I2C_CTL_GBCC_START** (line 39)
- **OWL_I2C_CTL_GBCC_STOP** (line 40)
- **OWL_I2C_CTL_IRQE** (line 42)
- **OWL_I2C_CTL_RB** (line 36)
- **OWL_I2C_CTL_SHSM** (line 45)
- **OWL_I2C_DIV_FACTOR**(x) (line 47)
- **OWL_I2C_FIFOCTL_NIB** (line 76)
- **OWL_I2C_FIFOCTL_RFR** (line 77)
- **OWL_I2C_FIFOCTL_TFR** (line 78)
- **OWL_I2C_FIFOSTAT_CECB** (line 81)
- **OWL_I2C_FIFOSTAT_RFD** (line 86)
- **OWL_I2C_FIFOSTAT_RFE** (line 83)
- **OWL_I2C_FIFOSTAT_RNB** (line 82)
- **OWL_I2C_FIFOSTAT_TFD** (line 85)
- **OWL_I2C_FIFOSTAT_TFF** (line 84)
- **OWL_I2C_MAX_RETRIES** (line 92)
- **OWL_I2C_REG_ADDR** (line 26)
- **OWL_I2C_REG_CLKDIV** (line 24)
- **OWL_I2C_REG_CMD** (line 29)
- **OWL_I2C_REG_CTL** (line 23)
- **OWL_I2C_REG_DATCNT** (line 32)
- **OWL_I2C_REG_FIFOCTL** (line 30)
- **OWL_I2C_REG_FIFOSTAT** (line 31)
- **OWL_I2C_REG_RCNT** (line 33)
- **OWL_I2C_REG_RXDAT** (line 28)
- **OWL_I2C_REG_STAT** (line 25)
- **OWL_I2C_REG_TXDAT** (line 27)
- **OWL_I2C_STAT_BBB** (line 56)
- **OWL_I2C_STAT_BEB** (line 51)
- **OWL_I2C_STAT_IRQP** (line 52)
- **OWL_I2C_STAT_LAB** (line 53)
- **OWL_I2C_STAT_LBST** (line 58)
- **OWL_I2C_STAT_RACK** (line 50)
- **OWL_I2C_STAT_SAMB** (line 59)
- **OWL_I2C_STAT_SRGC** (line 60)
- **OWL_I2C_STAT_STAD** (line 55)
- **OWL_I2C_STAT_STPD** (line 54)
- **OWL_I2C_STAT_TCB** (line 57)
- **OWL_I2C_TIMEOUT** (line 90)
- **OWL_I2C_TIMEOUT_MS** (line 89)
