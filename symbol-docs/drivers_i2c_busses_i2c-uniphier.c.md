# drivers/i2c/busses/i2c-uniphier.c

Subsystem: drivers/i2c

## Functions (20)

### uniphier_i2c_check_bus_busy
- Return type: static int
- Signature: uniphier_i2c_check_bus_busy(struct i2c_adapter * adap)
- Line: 192

### uniphier_i2c_functionality
- Return type: static u32
- Signature: uniphier_i2c_functionality(struct i2c_adapter * adap)
- Line: 235

### uniphier_i2c_get_scl
- Return type: static int
- Signature: uniphier_i2c_get_scl(struct i2c_adapter * adap)
- Line: 253

### uniphier_i2c_get_sda
- Return type: static int
- Signature: uniphier_i2c_get_sda(struct i2c_adapter * adap)
- Line: 269

### uniphier_i2c_hw_init
- Return type: static void
- Signature: uniphier_i2c_hw_init(struct uniphier_i2c_priv * priv)
- Line: 290

### uniphier_i2c_interrupt
- Return type: static irqreturn_t
- Signature: uniphier_i2c_interrupt(int irq,void * dev_id)
- Line: 47

### uniphier_i2c_probe
- Return type: static int
- Signature: uniphier_i2c_probe(struct platform_device * pdev)
- Line: 307

### uniphier_i2c_remove
- Return type: static void
- Signature: uniphier_i2c_remove(struct platform_device * pdev)
- Line: 362

### uniphier_i2c_reset
- Return type: static void
- Signature: uniphier_i2c_reset(struct uniphier_i2c_priv * priv,bool reset_on)
- Line: 245

### uniphier_i2c_resume
- Return type: static int __maybe_unused
- Signature: uniphier_i2c_resume(struct device * dev)
- Line: 378

### uniphier_i2c_rx
- Return type: static int
- Signature: uniphier_i2c_rx(struct i2c_adapter * adap,u16 addr,u16 len,u8 * buf)
- Line: 123

### uniphier_i2c_send_byte
- Return type: static int
- Signature: uniphier_i2c_send_byte(struct i2c_adapter * adap,u32 txdata)
- Line: 84

### uniphier_i2c_set_scl
- Return type: static void
- Signature: uniphier_i2c_set_scl(struct i2c_adapter * adap,int val)
- Line: 261

### uniphier_i2c_stop
- Return type: static int
- Signature: uniphier_i2c_stop(struct i2c_adapter * adap)
- Line: 149

### uniphier_i2c_suspend
- Return type: static int __maybe_unused
- Signature: uniphier_i2c_suspend(struct device * dev)
- Line: 369

### uniphier_i2c_tx
- Return type: static int
- Signature: uniphier_i2c_tx(struct i2c_adapter * adap,u16 addr,u16 len,const u8 * buf)
- Line: 102

### uniphier_i2c_unprepare_recovery
- Return type: static void
- Signature: uniphier_i2c_unprepare_recovery(struct i2c_adapter * adap)
- Line: 277

### uniphier_i2c_xfer
- Return type: static int
- Signature: uniphier_i2c_xfer(struct i2c_adapter * adap,struct i2c_msg * msgs,int num)
- Line: 214

### uniphier_i2c_xfer_byte
- Return type: static int
- Signature: uniphier_i2c_xfer_byte(struct i2c_adapter * adap,u32 txdata,u32 * rxdatap)
- Line: 61

### uniphier_i2c_xfer_one
- Return type: static int
- Signature: uniphier_i2c_xfer_one(struct i2c_adapter * adap,struct i2c_msg * msg,bool stop)
- Line: 155

## Structs (1)

### uniphier_i2c_priv
- Line: 38
- Members:
  - comp: completion
  - adap: i2c_adapter
  - membase: void __iomem *
  - clk: clk *
  - busy_cnt: unsigned int
  - clk_cycle: unsigned int

## Variables (5)

- static **uniphier_i2c_algo** : const struct i2c_algorithm (line 240)
- static **uniphier_i2c_bus_recovery_info** : i2c_bus_recovery_info (line 282)
- static **uniphier_i2c_drv** : platform_driver (line 402)
- static **uniphier_i2c_match** : const struct of_device_id[] (line 396)
- static **uniphier_i2c_pm_ops** : const struct dev_pm_ops (line 392)

## Macros (24)

- **UNIPHIER_I2C_BRST** (line 28)
- **UNIPHIER_I2C_BRST_FOEN** (line 29)
- **UNIPHIER_I2C_BRST_RSCL** (line 30)
- **UNIPHIER_I2C_BSTS** (line 32)
- **UNIPHIER_I2C_BSTS_SCL** (line 34)
- **UNIPHIER_I2C_BSTS_SDA** (line 33)
- **UNIPHIER_I2C_CLK** (line 27)
- **UNIPHIER_I2C_DREC** (line 19)
- **UNIPHIER_I2C_DREC_BBN** (line 25)
- **UNIPHIER_I2C_DREC_LAB** (line 24)
- **UNIPHIER_I2C_DREC_LRB** (line 23)
- **UNIPHIER_I2C_DREC_MST** (line 20)
- **UNIPHIER_I2C_DREC_STS** (line 22)
- **UNIPHIER_I2C_DREC_TX** (line 21)
- **UNIPHIER_I2C_DTRM** (line 13)
- **UNIPHIER_I2C_DTRM_IRQEN** (line 14)
- **UNIPHIER_I2C_DTRM_NACK** (line 17)
- **UNIPHIER_I2C_DTRM_RD** (line 18)
- **UNIPHIER_I2C_DTRM_STA** (line 15)
- **UNIPHIER_I2C_DTRM_STO** (line 16)
- **UNIPHIER_I2C_HOLD** (line 31)
- **UNIPHIER_I2C_MYAD** (line 26)
- **UNIPHIER_I2C_NOISE** (line 35)
- **UNIPHIER_I2C_SETUP** (line 36)
