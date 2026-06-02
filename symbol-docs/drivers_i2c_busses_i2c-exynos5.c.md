# drivers/i2c/busses/i2c-exynos5.c

Subsystem: drivers/i2c

## Functions (19)

### exynos5_hsi2c_clock_setup
- Return type: static int
- Signature: exynos5_hsi2c_clock_setup(struct exynos5_i2c * i2c)
- Line: 438

### exynos5_i2c_bus_check
- Return type: static void
- Signature: exynos5_i2c_bus_check(struct exynos5_i2c * i2c)
- Line: 671

### exynos5_i2c_bus_recover
- Return type: static void
- Signature: exynos5_i2c_bus_recover(struct exynos5_i2c * i2c)
- Line: 646

### exynos5_i2c_clr_pend_irq
- Return type: static void
- Signature: exynos5_i2c_clr_pend_irq(struct exynos5_i2c * i2c)
- Line: 272

### exynos5_i2c_func
- Return type: static u32
- Signature: exynos5_i2c_func(struct i2c_adapter * adap)
- Line: 876

### exynos5_i2c_init
- Return type: static void
- Signature: exynos5_i2c_init(struct exynos5_i2c * i2c)
- Line: 453

### exynos5_i2c_irq
- Return type: static irqreturn_t
- Signature: exynos5_i2c_irq(int irqno,void * dev_id)
- Line: 501

### exynos5_i2c_message_start
- Return type: static void
- Signature: exynos5_i2c_message_start(struct exynos5_i2c * i2c,int stop)
- Line: 707

### exynos5_i2c_poll_irqs_timeout
- Return type: static bool
- Signature: exynos5_i2c_poll_irqs_timeout(struct exynos5_i2c * i2c,unsigned long timeout)
- Line: 774

### exynos5_i2c_probe
- Return type: static int
- Signature: exynos5_i2c_probe(struct platform_device * pdev)
- Line: 887

### exynos5_i2c_remove
- Return type: static void
- Signature: exynos5_i2c_remove(struct platform_device * pdev)
- Line: 980

### exynos5_i2c_reset
- Return type: static void
- Signature: exynos5_i2c_reset(struct exynos5_i2c * i2c)
- Line: 475

### exynos5_i2c_resume_noirq
- Return type: static int
- Signature: exynos5_i2c_resume_noirq(struct device * dev)
- Line: 1001

### exynos5_i2c_set_timing
- Return type: static int
- Signature: exynos5_i2c_set_timing(struct exynos5_i2c * i2c,bool hs_timings)
- Line: 288

### exynos5_i2c_suspend_noirq
- Return type: static int
- Signature: exynos5_i2c_suspend_noirq(struct device * dev)
- Line: 990

### exynos5_i2c_wait_bus_idle
- Return type: static int
- Signature: exynos5_i2c_wait_bus_idle(struct exynos5_i2c * i2c)
- Line: 628

### exynos5_i2c_xfer
- Return type: static int
- Signature: exynos5_i2c_xfer(struct i2c_adapter * adap,struct i2c_msg * msgs,int num)
- Line: 834

### exynos5_i2c_xfer_atomic
- Return type: static int
- Signature: exynos5_i2c_xfer_atomic(struct i2c_adapter * adap,struct i2c_msg * msgs,int num)
- Line: 861

### exynos5_i2c_xfer_msg
- Return type: static int
- Signature: exynos5_i2c_xfer_msg(struct exynos5_i2c * i2c,struct i2c_msg * msgs,int stop)
- Line: 790

## Structs (2)

### exynos5_i2c
- Line: 174
- Members:
  - adap: i2c_adapter
  - msg: i2c_msg *
  - msg_complete: completion
  - msg_ptr: unsigned int
  - irq: unsigned int
  - regs: void __iomem *
  - clk: clk *
  - pclk: clk *
  - dev: device *
  - state: int
  - lock: spinlock_t
  - trans_done: int
  - atomic: unsigned int
  - op_clock: unsigned int
  - variant: const struct exynos_hsi2c_variant *
  - fifo_depth: unsigned int
  - hw: i2c_type_exynos

### exynos_hsi2c_variant
- Line: 219
- Members:
  - adap: i2c_adapter
  - msg: i2c_msg *
  - msg_complete: completion
  - msg_ptr: unsigned int
  - irq: unsigned int
  - regs: void __iomem *
  - clk: clk *
  - pclk: clk *
  - dev: device *
  - state: int
  - lock: spinlock_t
  - trans_done: int
  - atomic: unsigned int
  - op_clock: unsigned int
  - variant: const struct exynos_hsi2c_variant *
  - fifo_depth: unsigned int
  - hw: i2c_type_exynos

## Enums (1)

### i2c_type_exynos
- Line: 167

## Variables (9)

- static **exynos5250_hsi2c_data** : const struct exynos_hsi2c_variant (line 224)
- static **exynos5260_hsi2c_data** : const struct exynos_hsi2c_variant (line 229)
- static **exynos5_i2c_algorithm** : const struct i2c_algorithm (line 881)
- static **exynos5_i2c_dev_pm_ops** : const struct dev_pm_ops (line 1032)
- static **exynos5_i2c_driver** : platform_driver (line 1037)
- static **exynos5_i2c_match** : const struct of_device_id[] (line 249)
- static **exynos7_hsi2c_data** : const struct exynos_hsi2c_variant (line 234)
- static **exynos8895_hsi2c_data** : const struct exynos_hsi2c_variant (line 244)
- static **exynosautov9_hsi2c_data** : const struct exynos_hsi2c_variant (line 239)

## Macros (95)

- **EXYNOS5_I2C_TIMEOUT** (line 165)
- **HSI2C_10BIT_ADDR_MODE** (line 114)
- **HSI2C_ADDR** (line 60)
- **HSI2C_AUTO_CONF** (line 49)
- **HSI2C_AUTO_MODE** (line 113)
- **HSI2C_CLK_CTL** (line 40)
- **HSI2C_CLK_SLOT** (line 41)
- **HSI2C_CMD_READ_DATA** (line 127)
- **HSI2C_CMD_SEND_STOP** (line 128)
- **HSI2C_CONF** (line 48)
- **HSI2C_CTL** (line 37)
- **HSI2C_ERR_STATUS** (line 44)
- **HSI2C_FIFO_CTL** (line 38)
- **HSI2C_FIFO_STATUS** (line 45)
- **HSI2C_FUNC_MODE_I2C** (line 63)
- **HSI2C_HS_MODE** (line 115)
- **HSI2C_INT_ENABLE** (line 42)
- **HSI2C_INT_I2C** (line 91)
- **HSI2C_INT_I2C_TRANS** (line 98)
- **HSI2C_INT_NO_DEV** (line 96)
- **HSI2C_INT_NO_DEV_ACK** (line 95)
- **HSI2C_INT_RX_ALMOSTFULL** (line 85)
- **HSI2C_INT_RX_ALMOSTFULL_EN** (line 80)
- **HSI2C_INT_RX_OVERRUN** (line 89)
- **HSI2C_INT_RX_UNDERRUN** (line 88)
- **HSI2C_INT_STATUS** (line 43)
- **HSI2C_INT_TIMEOUT** (line 97)
- **HSI2C_INT_TRAILING** (line 90)
- **HSI2C_INT_TRAILING_EN** (line 81)
- **HSI2C_INT_TRANS_ABORT** (line 94)
- **HSI2C_INT_TRANS_DONE** (line 93)
- **HSI2C_INT_TX_ALMOSTEMPTY** (line 84)
- **HSI2C_INT_TX_ALMOSTEMPTY_EN** (line 79)
- **HSI2C_INT_TX_OVERRUN** (line 87)
- **HSI2C_INT_TX_UNDERRUN** (line 86)
- **HSI2C_MANUAL_CMD** (line 51)
- **HSI2C_MASTER** (line 64)
- **HSI2C_MASTER_BUSY** (line 131)
- **HSI2C_MASTER_ID**(x) (line 162)
- **HSI2C_MASTER_RUN** (line 120)
- **HSI2C_MASTER_ST_ADDR0** (line 148)
- **HSI2C_MASTER_ST_ADDR1** (line 149)
- **HSI2C_MASTER_ST_ADDR2** (line 150)
- **HSI2C_MASTER_ST_ADDR_SR** (line 151)
- **HSI2C_MASTER_ST_IDLE** (line 143)
- **HSI2C_MASTER_ST_LOSE** (line 155)
- **HSI2C_MASTER_ST_MASK** (line 142)
- **HSI2C_MASTER_ST_MASTER_ID** (line 147)
- **HSI2C_MASTER_ST_NO_ACK** (line 154)
- **HSI2C_MASTER_ST_READ** (line 152)
- **HSI2C_MASTER_ST_RESTART** (line 145)
- **HSI2C_MASTER_ST_START** (line 144)
- **HSI2C_MASTER_ST_STOP** (line 146)
- **HSI2C_MASTER_ST_WAIT** (line 156)
- **HSI2C_MASTER_ST_WAIT_CMD** (line 157)
- **HSI2C_MASTER_ST_WRITE** (line 153)
- **HSI2C_NO_DEV** (line 136)
- **HSI2C_NO_DEV_ACK** (line 137)
- **HSI2C_READ_WRITE** (line 118)
- **HSI2C_RXCHON** (line 65)
- **HSI2C_RXFIFO_EN** (line 70)
- **HSI2C_RXFIFO_TRIGGER_LEVEL**(x) (line 72)
- **HSI2C_RX_DATA** (line 47)
- **HSI2C_RX_FIFO_EMPTY** (line 105)
- **HSI2C_RX_FIFO_FULL** (line 106)
- **HSI2C_RX_FIFO_LVL**(x) (line 107)
- **HSI2C_SLAVE_BUSY** (line 132)
- **HSI2C_SLV_ADDR_MAS**(x) (line 161)
- **HSI2C_SLV_ADDR_SLV**(x) (line 160)
- **HSI2C_STOP_AFTER_TRANS** (line 119)
- **HSI2C_SW_RST** (line 67)
- **HSI2C_TIMEOUT** (line 50)
- **HSI2C_TIMEOUT_AUTO** (line 135)
- **HSI2C_TIMEOUT_EN** (line 123)
- **HSI2C_TIMEOUT_MASK** (line 124)
- **HSI2C_TIMING_FS1** (line 56)
- **HSI2C_TIMING_FS2** (line 57)
- **HSI2C_TIMING_FS3** (line 58)
- **HSI2C_TIMING_HS1** (line 53)
- **HSI2C_TIMING_HS2** (line 54)
- **HSI2C_TIMING_HS3** (line 55)
- **HSI2C_TIMING_SLA** (line 59)
- **HSI2C_TRAILIG_CTL** (line 39)
- **HSI2C_TRAILING_COUNT** (line 76)
- **HSI2C_TRANS_ABORT** (line 138)
- **HSI2C_TRANS_DONE** (line 139)
- **HSI2C_TRANS_STATUS** (line 52)
- **HSI2C_TXCHON** (line 66)
- **HSI2C_TXFIFO_EN** (line 71)
- **HSI2C_TXFIFO_TRIGGER_LEVEL**(x) (line 73)
- **HSI2C_TX_DATA** (line 46)
- **HSI2C_TX_FIFO_EMPTY** (line 108)
- **HSI2C_TX_FIFO_FULL** (line 109)
- **HSI2C_TX_FIFO_LVL**(x) (line 110)
- **MASTER_ID**(x) (line 163)
