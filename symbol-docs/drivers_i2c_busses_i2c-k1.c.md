# drivers/i2c/busses/i2c-k1.c

Subsystem: drivers/i2c

## Functions (29)

### spacemit_i2c_calc_timeout
- Return type: static void
- Signature: spacemit_i2c_calc_timeout(struct spacemit_i2c_dev * i2c)
- Line: 610

### spacemit_i2c_check_bus_release
- Return type: static void
- Signature: spacemit_i2c_check_bus_release(struct spacemit_i2c_dev * i2c)
- Line: 244

### spacemit_i2c_clear_int_status
- Return type: static void
- Signature: spacemit_i2c_clear_int_status(struct spacemit_i2c_dev * i2c,u32 mask)
- Line: 254

### spacemit_i2c_complete
- Return type: static void
- Signature: spacemit_i2c_complete(struct spacemit_i2c_dev * i2c)
- Line: 352

### spacemit_i2c_conditionally_reset_bus
- Return type: static void
- Signature: spacemit_i2c_conditionally_reset_bus(struct spacemit_i2c_dev * i2c)
- Line: 188

### spacemit_i2c_delay
- Return type: static void
- Signature: spacemit_i2c_delay(struct spacemit_i2c_dev * i2c,unsigned int us)
- Line: 180

### spacemit_i2c_disable
- Return type: static void
- Signature: spacemit_i2c_disable(struct spacemit_i2c_dev * i2c)
- Line: 147

### spacemit_i2c_enable
- Return type: static void
- Signature: spacemit_i2c_enable(struct spacemit_i2c_dev * i2c)
- Line: 138

### spacemit_i2c_err_check
- Return type: static void
- Signature: spacemit_i2c_err_check(struct spacemit_i2c_dev * i2c)
- Line: 412

### spacemit_i2c_func
- Return type: static u32
- Signature: spacemit_i2c_func(struct i2c_adapter * adap)
- Line: 677

### spacemit_i2c_handle_err
- Return type: static int
- Signature: spacemit_i2c_handle_err(struct spacemit_i2c_dev * i2c)
- Line: 163

### spacemit_i2c_handle_read
- Return type: static void
- Signature: spacemit_i2c_handle_read(struct spacemit_i2c_dev * i2c)
- Line: 382

### spacemit_i2c_handle_start
- Return type: static void
- Signature: spacemit_i2c_handle_start(struct spacemit_i2c_dev * i2c)
- Line: 405

### spacemit_i2c_handle_state
- Return type: static void
- Signature: spacemit_i2c_handle_state(struct spacemit_i2c_dev * i2c)
- Line: 439

### spacemit_i2c_handle_write
- Return type: static void
- Signature: spacemit_i2c_handle_write(struct spacemit_i2c_dev * i2c)
- Line: 363

### spacemit_i2c_init
- Return type: static void
- Signature: spacemit_i2c_init(struct spacemit_i2c_dev * i2c)
- Line: 259

### spacemit_i2c_irq_handler
- Return type: static irqreturn_t
- Signature: spacemit_i2c_irq_handler(int irq,void * devid)
- Line: 592

### spacemit_i2c_is_last_msg
- Return type: static bool
- Signature: spacemit_i2c_is_last_msg(struct spacemit_i2c_dev * i2c)
- Line: 341

### spacemit_i2c_pio_xfer_atomic
- Return type: static int
- Signature: spacemit_i2c_pio_xfer_atomic(struct i2c_adapter * adapt,struct i2c_msg * msgs,int num)
- Line: 672

### spacemit_i2c_probe
- Return type: static int
- Signature: spacemit_i2c_probe(struct platform_device * pdev)
- Line: 688

### spacemit_i2c_remove
- Return type: static void
- Signature: spacemit_i2c_remove(struct platform_device * pdev)
- Line: 767

### spacemit_i2c_reset
- Return type: static void
- Signature: spacemit_i2c_reset(struct spacemit_i2c_dev * i2c)
- Line: 156

### spacemit_i2c_start
- Return type: static void
- Signature: spacemit_i2c_start(struct spacemit_i2c_dev * i2c)
- Line: 314

### spacemit_i2c_wait_bus_idle
- Return type: static int
- Signature: spacemit_i2c_wait_bus_idle(struct spacemit_i2c_dev * i2c)
- Line: 220

### spacemit_i2c_wait_pio_xfer
- Return type: static int
- Signature: spacemit_i2c_wait_pio_xfer(struct spacemit_i2c_dev * i2c)
- Line: 492

### spacemit_i2c_wait_xfer_complete
- Return type: static int
- Signature: spacemit_i2c_wait_xfer_complete(struct spacemit_i2c_dev * i2c)
- Line: 552

### spacemit_i2c_xfer
- Return type: static int
- Signature: spacemit_i2c_xfer(struct i2c_adapter * adapt,struct i2c_msg * msgs,int num)
- Line: 667

### spacemit_i2c_xfer_common
- Return type: static int
- Signature: spacemit_i2c_xfer_common(struct i2c_adapter * adapt,struct i2c_msg * msgs,int num,bool use_pio)
- Line: 633

### spacemit_i2c_xfer_msg
- Return type: static int
- Signature: spacemit_i2c_xfer_msg(struct spacemit_i2c_dev * i2c)
- Line: 561

## Structs (1)

### spacemit_i2c_dev
- Line: 113
- Members:
  - dev: device *
  - adapt: i2c_adapter
  - base: void __iomem *
  - irq: int
  - clock_freq: u32
  - msgs: i2c_msg *
  - msg_num: u32
  - msg_idx: u32
  - msg_buf: u8 *
  - unprocessed: u32
  - state: spacemit_i2c_state
  - read: bool
  - use_pio: bool
  - complete: completion
  - status: u32

## Enums (1)

### spacemit_i2c_state
- Line: 105

## Variables (3)

- static **spacemit_i2c_algo** : const struct i2c_algorithm (line 682)
- static **spacemit_i2c_driver** : platform_driver (line 780)
- static **spacemit_i2c_of_match** : const struct of_device_id[] (line 774)

## Macros (57)

- **SPACEMIT_BMR_SCL** (line 89)
- **SPACEMIT_BMR_SDA** (line 88)
- **SPACEMIT_BUS_RESET_CLK_CNT_MAX** (line 99)
- **SPACEMIT_CR_ACKNAK** (line 25)
- **SPACEMIT_CR_ALDIE** (line 36)
- **SPACEMIT_CR_BEIE** (line 40)
- **SPACEMIT_CR_DRFIE** (line 38)
- **SPACEMIT_CR_DTEIE** (line 37)
- **SPACEMIT_CR_GCD** (line 39)
- **SPACEMIT_CR_IUE** (line 34)
- **SPACEMIT_CR_MODE_FAST** (line 28)
- **SPACEMIT_CR_MSDE** (line 43)
- **SPACEMIT_CR_MSDIE** (line 42)
- **SPACEMIT_CR_RSTREQ** (line 31)
- **SPACEMIT_CR_RXFIE** (line 47)
- **SPACEMIT_CR_RXHFIE** (line 46)
- **SPACEMIT_CR_RXOVIE** (line 48)
- **SPACEMIT_CR_SCLE** (line 33)
- **SPACEMIT_CR_START** (line 23)
- **SPACEMIT_CR_STOP** (line 24)
- **SPACEMIT_CR_TB** (line 26)
- **SPACEMIT_CR_TXDONEIE** (line 44)
- **SPACEMIT_CR_TXEIE** (line 45)
- **SPACEMIT_CR_UR** (line 30)
- **SPACEMIT_I2C_BUS_BUSY_TIMEOUT** (line 92)
- **SPACEMIT_I2C_INT_CTRL_MASK** (line 50)
- **SPACEMIT_I2C_INT_STATUS_MASK** (line 77)
- **SPACEMIT_I2C_MAX_FAST_MODE_FREQ** (line 95)
- **SPACEMIT_I2C_MAX_STANDARD_MODE_FREQ** (line 94)
- **SPACEMIT_IBMR** (line 20)
- **SPACEMIT_ICR** (line 16)
- **SPACEMIT_IDBR** (line 18)
- **SPACEMIT_IRCR** (line 19)
- **SPACEMIT_ISR** (line 17)
- **SPACEMIT_POLL_INTERVAL** (line 103)
- **SPACEMIT_POLL_TIMEOUT** (line 102)
- **SPACEMIT_RCR_FIELD_RST_CYC** (line 85)
- **SPACEMIT_RCR_SDA_GLITCH_NOFIX** (line 83)
- **SPACEMIT_SR_ACKNAK** (line 58)
- **SPACEMIT_SR_ALD** (line 62)
- **SPACEMIT_SR_BED** (line 66)
- **SPACEMIT_SR_EBB** (line 61)
- **SPACEMIT_SR_ERR** (line 97)
- **SPACEMIT_SR_GCAD** (line 65)
- **SPACEMIT_SR_IBB** (line 60)
- **SPACEMIT_SR_IRF** (line 64)
- **SPACEMIT_SR_ITE** (line 63)
- **SPACEMIT_SR_MSD** (line 70)
- **SPACEMIT_SR_RXF** (line 74)
- **SPACEMIT_SR_RXHF** (line 73)
- **SPACEMIT_SR_RXOV** (line 75)
- **SPACEMIT_SR_SAD** (line 67)
- **SPACEMIT_SR_SSD** (line 68)
- **SPACEMIT_SR_TXDONE** (line 71)
- **SPACEMIT_SR_TXE** (line 72)
- **SPACEMIT_SR_UB** (line 59)
- **SPACEMIT_WAIT_TIMEOUT** (line 101)
