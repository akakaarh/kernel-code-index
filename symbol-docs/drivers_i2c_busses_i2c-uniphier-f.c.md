# drivers/i2c/busses/i2c-uniphier-f.c

Subsystem: drivers/i2c

## Functions (24)

### uniphier_fi2c_check_bus_busy
- Return type: static int
- Signature: uniphier_fi2c_check_bus_busy(struct i2c_adapter * adap)
- Line: 384

### uniphier_fi2c_clear_irqs
- Return type: static void
- Signature: uniphier_fi2c_clear_irqs(struct uniphier_fi2c_priv * priv,u32 mask)
- Line: 133

### uniphier_fi2c_drain_rxfifo
- Return type: static void
- Signature: uniphier_fi2c_drain_rxfifo(struct uniphier_fi2c_priv * priv)
- Line: 114

### uniphier_fi2c_fill_txfifo
- Return type: static void
- Signature: uniphier_fi2c_fill_txfifo(struct uniphier_fi2c_priv * priv,bool first)
- Line: 93

### uniphier_fi2c_functionality
- Return type: static u32
- Signature: uniphier_fi2c_functionality(struct i2c_adapter * adap)
- Line: 429

### uniphier_fi2c_get_scl
- Return type: static int
- Signature: uniphier_fi2c_get_scl(struct i2c_adapter * adap)
- Line: 439

### uniphier_fi2c_get_sda
- Return type: static int
- Signature: uniphier_fi2c_get_sda(struct i2c_adapter * adap)
- Line: 455

### uniphier_fi2c_hw_init
- Return type: static void
- Signature: uniphier_fi2c_hw_init(struct uniphier_fi2c_priv * priv)
- Line: 476

### uniphier_fi2c_interrupt
- Return type: static irqreturn_t
- Signature: uniphier_fi2c_interrupt(int irq,void * dev_id)
- Line: 147

### uniphier_fi2c_prepare_operation
- Return type: static void
- Signature: uniphier_fi2c_prepare_operation(struct uniphier_fi2c_priv * priv)
- Line: 301

### uniphier_fi2c_probe
- Return type: static int
- Signature: uniphier_fi2c_probe(struct platform_device * pdev)
- Line: 512

### uniphier_fi2c_recover
- Return type: static void
- Signature: uniphier_fi2c_recover(struct uniphier_fi2c_priv * priv)
- Line: 307

### uniphier_fi2c_remove
- Return type: static void
- Signature: uniphier_fi2c_remove(struct platform_device * pdev)
- Line: 568

### uniphier_fi2c_reset
- Return type: static void
- Signature: uniphier_fi2c_reset(struct uniphier_fi2c_priv * priv)
- Line: 296

### uniphier_fi2c_resume
- Return type: static int __maybe_unused
- Signature: uniphier_fi2c_resume(struct device * dev)
- Line: 584

### uniphier_fi2c_rx_init
- Return type: static void
- Signature: uniphier_fi2c_rx_init(struct uniphier_fi2c_priv * priv,u16 addr)
- Line: 266

### uniphier_fi2c_set_irqs
- Return type: static void
- Signature: uniphier_fi2c_set_irqs(struct uniphier_fi2c_priv * priv)
- Line: 128

### uniphier_fi2c_set_scl
- Return type: static void
- Signature: uniphier_fi2c_set_scl(struct i2c_adapter * adap,int val)
- Line: 447

### uniphier_fi2c_stop
- Return type: static void
- Signature: uniphier_fi2c_stop(struct uniphier_fi2c_priv * priv)
- Line: 139

### uniphier_fi2c_suspend
- Return type: static int __maybe_unused
- Signature: uniphier_fi2c_suspend(struct device * dev)
- Line: 575

### uniphier_fi2c_tx_init
- Return type: static void
- Signature: uniphier_fi2c_tx_init(struct uniphier_fi2c_priv * priv,u16 addr,bool repeat)
- Line: 247

### uniphier_fi2c_unprepare_recovery
- Return type: static void
- Signature: uniphier_fi2c_unprepare_recovery(struct i2c_adapter * adap)
- Line: 463

### uniphier_fi2c_xfer
- Return type: static int
- Signature: uniphier_fi2c_xfer(struct i2c_adapter * adap,struct i2c_msg * msgs,int num)
- Line: 405

### uniphier_fi2c_xfer_one
- Return type: static int
- Signature: uniphier_fi2c_xfer_one(struct i2c_adapter * adap,struct i2c_msg * msg,bool repeat,bool stop)
- Line: 313

## Structs (1)

### uniphier_fi2c_priv
- Line: 78
- Members:
  - comp: completion
  - adap: i2c_adapter
  - membase: void __iomem *
  - clk: clk *
  - len: unsigned int
  - buf: u8 *
  - enabled_irqs: u32
  - error: int
  - flags: unsigned int
  - busy_cnt: unsigned int
  - clk_cycle: unsigned int
  - lock: spinlock_t

## Variables (5)

- static **uniphier_fi2c_algo** : const struct i2c_algorithm (line 434)
- static **uniphier_fi2c_bus_recovery_info** : i2c_bus_recovery_info (line 468)
- static **uniphier_fi2c_drv** : platform_driver (line 608)
- static **uniphier_fi2c_match** : const struct of_device_id[] (line 602)
- static **uniphier_fi2c_pm_ops** : const struct dev_pm_ops (line 598)

## Macros (58)

- **UNIPHIER_FI2C_BM** (line 51)
- **UNIPHIER_FI2C_BM_SCLO** (line 54)
- **UNIPHIER_FI2C_BM_SCLS** (line 55)
- **UNIPHIER_FI2C_BM_SDAO** (line 52)
- **UNIPHIER_FI2C_BM_SDAS** (line 53)
- **UNIPHIER_FI2C_BRST** (line 61)
- **UNIPHIER_FI2C_BRST_FOEN** (line 62)
- **UNIPHIER_FI2C_BRST_RSCL** (line 63)
- **UNIPHIER_FI2C_BYTE_WISE** (line 73)
- **UNIPHIER_FI2C_CR** (line 14)
- **UNIPHIER_FI2C_CR_MST** (line 15)
- **UNIPHIER_FI2C_CR_NACK** (line 18)
- **UNIPHIER_FI2C_CR_STA** (line 16)
- **UNIPHIER_FI2C_CR_STO** (line 17)
- **UNIPHIER_FI2C_CYC** (line 24)
- **UNIPHIER_FI2C_DEFER_STOP_COMP** (line 74)
- **UNIPHIER_FI2C_DSUT** (line 27)
- **UNIPHIER_FI2C_DTRX** (line 22)
- **UNIPHIER_FI2C_DTTX** (line 19)
- **UNIPHIER_FI2C_DTTX_CMD** (line 20)
- **UNIPHIER_FI2C_DTTX_RD** (line 21)
- **UNIPHIER_FI2C_FIFO_SIZE** (line 76)
- **UNIPHIER_FI2C_IC** (line 30)
- **UNIPHIER_FI2C_IE** (line 29)
- **UNIPHIER_FI2C_INT** (line 28)
- **UNIPHIER_FI2C_INT_AL** (line 38)
- **UNIPHIER_FI2C_INT_FAULTS** (line 65)
- **UNIPHIER_FI2C_INT_NA** (line 37)
- **UNIPHIER_FI2C_INT_RB** (line 36)
- **UNIPHIER_FI2C_INT_RC** (line 34)
- **UNIPHIER_FI2C_INT_RF** (line 32)
- **UNIPHIER_FI2C_INT_STOP** (line 67)
- **UNIPHIER_FI2C_INT_TB** (line 35)
- **UNIPHIER_FI2C_INT_TC** (line 33)
- **UNIPHIER_FI2C_INT_TE** (line 31)
- **UNIPHIER_FI2C_LCTL** (line 25)
- **UNIPHIER_FI2C_MANUAL_NACK** (line 72)
- **UNIPHIER_FI2C_NOISE** (line 56)
- **UNIPHIER_FI2C_RBC** (line 58)
- **UNIPHIER_FI2C_RBCM** (line 60)
- **UNIPHIER_FI2C_RD** (line 70)
- **UNIPHIER_FI2C_RST** (line 47)
- **UNIPHIER_FI2C_RST_RBRST** (line 49)
- **UNIPHIER_FI2C_RST_RST** (line 50)
- **UNIPHIER_FI2C_RST_TBRST** (line 48)
- **UNIPHIER_FI2C_SLAD** (line 23)
- **UNIPHIER_FI2C_SR** (line 39)
- **UNIPHIER_FI2C_SR_BB** (line 42)
- **UNIPHIER_FI2C_SR_DB** (line 40)
- **UNIPHIER_FI2C_SR_RFF** (line 43)
- **UNIPHIER_FI2C_SR_RNE** (line 44)
- **UNIPHIER_FI2C_SR_STS** (line 41)
- **UNIPHIER_FI2C_SR_TFE** (line 46)
- **UNIPHIER_FI2C_SR_TNF** (line 45)
- **UNIPHIER_FI2C_SSUT** (line 26)
- **UNIPHIER_FI2C_STOP** (line 71)
- **UNIPHIER_FI2C_TBC** (line 57)
- **UNIPHIER_FI2C_TBCM** (line 59)
