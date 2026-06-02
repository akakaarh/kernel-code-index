# drivers/i2c/busses/i2c-sprd.c

Subsystem: drivers/i2c

## Functions (30)

### sprd_i2c_clear_ack
- Return type: static void
- Signature: sprd_i2c_clear_ack(struct sprd_i2c * i2c_dev)
- Line: 115

### sprd_i2c_clear_irq
- Return type: static void
- Signature: sprd_i2c_clear_irq(struct sprd_i2c * i2c_dev)
- Line: 122

### sprd_i2c_clear_start
- Return type: static void
- Signature: sprd_i2c_clear_start(struct sprd_i2c * i2c_dev)
- Line: 108

### sprd_i2c_clk_init
- Return type: static int
- Signature: sprd_i2c_clk_init(struct sprd_i2c * i2c_dev)
- Line: 445

### sprd_i2c_data_transfer
- Return type: static void
- Signature: sprd_i2c_data_transfer(struct sprd_i2c * i2c_dev)
- Line: 211

### sprd_i2c_enable
- Return type: static void
- Signature: sprd_i2c_enable(struct sprd_i2c * i2c_dev)
- Line: 350

### sprd_i2c_func
- Return type: static u32
- Signature: sprd_i2c_func(struct i2c_adapter * adap)
- Line: 310

### sprd_i2c_handle_msg
- Return type: static int
- Signature: sprd_i2c_handle_msg(struct i2c_adapter * i2c_adap,struct i2c_msg * msg,bool is_last_msg)
- Line: 244

### sprd_i2c_isr
- Return type: static irqreturn_t
- Signature: sprd_i2c_isr(int irq,void * dev_id)
- Line: 411

### sprd_i2c_isr_thread
- Return type: static irqreturn_t
- Signature: sprd_i2c_isr_thread(int irq,void * dev_id)
- Line: 367

### sprd_i2c_opt_mode
- Return type: static void
- Signature: sprd_i2c_opt_mode(struct sprd_i2c * i2c_dev,int rw)
- Line: 204

### sprd_i2c_opt_start
- Return type: static void
- Signature: sprd_i2c_opt_start(struct sprd_i2c * i2c_dev)
- Line: 197

### sprd_i2c_probe
- Return type: static int
- Signature: sprd_i2c_probe(struct platform_device * pdev)
- Line: 481

### sprd_i2c_read_bytes
- Return type: static void
- Signature: sprd_i2c_read_bytes(struct sprd_i2c * i2c_dev,u8 * buf,u32 len)
- Line: 147

### sprd_i2c_remove
- Return type: static void
- Signature: sprd_i2c_remove(struct platform_device * pdev)
- Line: 571

### sprd_i2c_reset_fifo
- Return type: static void
- Signature: sprd_i2c_reset_fifo(struct sprd_i2c * i2c_dev)
- Line: 129

### sprd_i2c_resume_noirq
- Return type: static int __maybe_unused
- Signature: sprd_i2c_resume_noirq(struct device * dev)
- Line: 597

### sprd_i2c_runtime_resume
- Return type: static int __maybe_unused
- Signature: sprd_i2c_runtime_resume(struct device * dev)
- Line: 614

### sprd_i2c_runtime_suspend
- Return type: static int __maybe_unused
- Signature: sprd_i2c_runtime_suspend(struct device * dev)
- Line: 605

### sprd_i2c_send_stop
- Return type: static void
- Signature: sprd_i2c_send_stop(struct sprd_i2c * i2c_dev,int stop)
- Line: 98

### sprd_i2c_set_clk
- Return type: static void
- Signature: sprd_i2c_set_clk(struct sprd_i2c * i2c_dev,u32 freq)
- Line: 320

### sprd_i2c_set_count
- Return type: static void
- Signature: sprd_i2c_set_count(struct sprd_i2c * i2c_dev,u32 count)
- Line: 93

### sprd_i2c_set_devaddr
- Return type: static void
- Signature: sprd_i2c_set_devaddr(struct sprd_i2c * i2c_dev,struct i2c_msg * m)
- Line: 134

### sprd_i2c_set_empty_thld
- Return type: static void
- Signature: sprd_i2c_set_empty_thld(struct sprd_i2c * i2c_dev,u32 empty_thld)
- Line: 164

### sprd_i2c_set_fifo_empty_int
- Return type: static void
- Signature: sprd_i2c_set_fifo_empty_int(struct sprd_i2c * i2c_dev,int enable)
- Line: 185

### sprd_i2c_set_fifo_full_int
- Return type: static void
- Signature: sprd_i2c_set_fifo_full_int(struct sprd_i2c * i2c_dev,int enable)
- Line: 173

### sprd_i2c_set_full_thld
- Return type: static void
- Signature: sprd_i2c_set_full_thld(struct sprd_i2c * i2c_dev,u32 full_thld)
- Line: 155

### sprd_i2c_suspend_noirq
- Return type: static int __maybe_unused
- Signature: sprd_i2c_suspend_noirq(struct device * dev)
- Line: 589

### sprd_i2c_write_bytes
- Return type: static void
- Signature: sprd_i2c_write_bytes(struct sprd_i2c * i2c_dev,u8 * buf,u32 len)
- Line: 139

### sprd_i2c_xfer
- Return type: static int
- Signature: sprd_i2c_xfer(struct i2c_adapter * i2c_adap,struct i2c_msg * msgs,int num)
- Line: 286

## Structs (1)

### sprd_i2c
- Line: 78
- Members:
  - adap: i2c_adapter
  - dev: device *
  - base: void __iomem *
  - msg: i2c_msg *
  - clk: clk *
  - src_clk: u32
  - bus_freq: u32
  - complete: completion
  - buf: u8 *
  - count: u32
  - irq: int
  - err: int

## Variables (4)

- static **sprd_i2c_algo** : const struct i2c_algorithm (line 315)
- static **sprd_i2c_driver** : platform_driver (line 642)
- static **sprd_i2c_of_match** : const struct of_device_id[] (line 636)
- static **sprd_i2c_pm_ops** : const struct dev_pm_ops (line 628)

## Macros (44)

- **ADDR_DVD0** (line 28)
- **ADDR_DVD1** (line 29)
- **ADDR_RST** (line 31)
- **ADDR_STA0_DVD** (line 30)
- **EMPTY_INTEN** (line 41)
- **FIFO_AE_LVL** (line 38)
- **FIFO_AE_LVL_MASK** (line 37)
- **FIFO_AF_LVL** (line 36)
- **FIFO_AF_LVL_MASK** (line 35)
- **FIFO_EMPTY** (line 55)
- **FIFO_FULL** (line 54)
- **FULL_INTEN** (line 40)
- **I2C_ADDR_CFG** (line 21)
- **I2C_ADDR_DVD0_CALC**(high,low) (line 67)
- **I2C_ADDR_DVD1_CALC**(high,low) (line 69)
- **I2C_BUSY** (line 58)
- **I2C_COUNT** (line 22)
- **I2C_CTL** (line 20)
- **I2C_DATA_STEP** (line 66)
- **I2C_DMA_EN** (line 39)
- **I2C_DVD_OPT** (line 42)
- **I2C_EN** (line 47)
- **I2C_FIFO_DEEP** (line 63)
- **I2C_FIFO_EMPTY_THLD** (line 65)
- **I2C_FIFO_FULL_THLD** (line 64)
- **I2C_HSMODE_CFG** (line 26)
- **I2C_HS_MODE** (line 45)
- **I2C_INT** (line 56)
- **I2C_INT_EN** (line 48)
- **I2C_MODE** (line 46)
- **I2C_OUT_OPT** (line 43)
- **I2C_RST** (line 61)
- **I2C_RX** (line 23)
- **I2C_RX_ACK** (line 57)
- **I2C_START** (line 49)
- **I2C_STATUS** (line 25)
- **I2C_TRIM_OPT** (line 44)
- **I2C_TX** (line 24)
- **I2C_VERSION** (line 27)
- **I2C_XFER_TIMEOUT** (line 75)
- **SCL_IN** (line 53)
- **SDA_IN** (line 52)
- **SPRD_I2C_PM_TIMEOUT** (line 73)
- **STP_EN** (line 34)
