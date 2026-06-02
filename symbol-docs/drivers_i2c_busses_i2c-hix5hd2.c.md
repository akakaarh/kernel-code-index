# drivers/i2c/busses/i2c-hix5hd2.c

Subsystem: drivers/i2c

## Functions (22)

### hix5hd2_i2c_clr_all_irq
- Return type: static void
- Signature: hix5hd2_i2c_clr_all_irq(struct hix5hd2_i2c_priv * priv)
- Line: 104

### hix5hd2_i2c_clr_pend_irq
- Return type: static u32
- Signature: hix5hd2_i2c_clr_pend_irq(struct hix5hd2_i2c_priv * priv)
- Line: 95

### hix5hd2_i2c_disable_irq
- Return type: static void
- Signature: hix5hd2_i2c_disable_irq(struct hix5hd2_i2c_priv * priv)
- Line: 109

### hix5hd2_i2c_drv_setrate
- Return type: static void
- Signature: hix5hd2_i2c_drv_setrate(struct hix5hd2_i2c_priv * priv)
- Line: 120

### hix5hd2_i2c_enable_irq
- Return type: static void
- Signature: hix5hd2_i2c_enable_irq(struct hix5hd2_i2c_priv * priv)
- Line: 114

### hix5hd2_i2c_func
- Return type: static u32
- Signature: hix5hd2_i2c_func(struct i2c_adapter * adap)
- Line: 380

### hix5hd2_i2c_init
- Return type: static void
- Signature: hix5hd2_i2c_init(struct hix5hd2_i2c_priv * priv)
- Line: 142

### hix5hd2_i2c_irq
- Return type: static irqreturn_t
- Signature: hix5hd2_i2c_irq(int irqno,void * dev_id)
- Line: 243

### hix5hd2_i2c_message_start
- Return type: static void
- Signature: hix5hd2_i2c_message_start(struct hix5hd2_i2c_priv * priv,int stop)
- Line: 299

### hix5hd2_i2c_probe
- Return type: static int
- Signature: hix5hd2_i2c_probe(struct platform_device * pdev)
- Line: 390

### hix5hd2_i2c_remove
- Return type: static void
- Signature: hix5hd2_i2c_remove(struct platform_device * pdev)
- Line: 468

### hix5hd2_i2c_reset
- Return type: static void
- Signature: hix5hd2_i2c_reset(struct hix5hd2_i2c_priv * priv)
- Line: 150

### hix5hd2_i2c_runtime_resume
- Return type: static int
- Signature: hix5hd2_i2c_runtime_resume(struct device * dev)
- Line: 486

### hix5hd2_i2c_runtime_suspend
- Return type: static int
- Signature: hix5hd2_i2c_runtime_suspend(struct device * dev)
- Line: 477

### hix5hd2_i2c_wait_bus_idle
- Return type: static int
- Signature: hix5hd2_i2c_wait_bus_idle(struct hix5hd2_i2c_priv * priv)
- Line: 158

### hix5hd2_i2c_xfer
- Return type: static int
- Signature: hix5hd2_i2c_xfer(struct i2c_adapter * adap,struct i2c_msg * msgs,int num)
- Line: 354

### hix5hd2_i2c_xfer_msg
- Return type: static int
- Signature: hix5hd2_i2c_xfer_msg(struct hix5hd2_i2c_priv * priv,struct i2c_msg * msgs,int stop)
- Line: 314

### hix5hd2_read_handle
- Return type: static void
- Signature: hix5hd2_read_handle(struct hix5hd2_i2c_priv * priv)
- Line: 197

### hix5hd2_rw_handle_stop
- Return type: static void
- Signature: hix5hd2_rw_handle_stop(struct hix5hd2_i2c_priv * priv)
- Line: 187

### hix5hd2_rw_over
- Return type: static void
- Signature: hix5hd2_rw_over(struct hix5hd2_i2c_priv * priv)
- Line: 176

### hix5hd2_rw_preprocess
- Return type: static int
- Signature: hix5hd2_rw_preprocess(struct hix5hd2_i2c_priv * priv)
- Line: 223

### hix5hd2_write_handle
- Return type: static void
- Signature: hix5hd2_write_handle(struct hix5hd2_i2c_priv * priv)
- Line: 210

## Structs (1)

### hix5hd2_i2c_priv
- Line: 79
- Members:
  - adap: i2c_adapter
  - msg: i2c_msg *
  - msg_complete: completion
  - msg_idx: unsigned int
  - msg_len: unsigned int
  - stop: int
  - regs: void __iomem *
  - clk: clk *
  - dev: device *
  - lock: spinlock_t
  - err: int
  - freq: unsigned int
  - state: hix5hd2_i2c_state

## Enums (1)

### hix5hd2_i2c_state
- Line: 71

## Variables (4)

- static **hix5hd2_i2c_algorithm** : const struct i2c_algorithm (line 385)
- static **hix5hd2_i2c_driver** : platform_driver (line 508)
- static **hix5hd2_i2c_match** : const struct of_device_id[] (line 502)
- static **hix5hd2_i2c_pm_ops** : const struct dev_pm_ops (line 496)

## Macros (39)

- **HIX5I2C_COM** (line 21)
- **HIX5I2C_CTRL** (line 20)
- **HIX5I2C_ICR** (line 22)
- **HIX5I2C_RXR** (line 27)
- **HIX5I2C_SCL_H** (line 24)
- **HIX5I2C_SCL_L** (line 25)
- **HIX5I2C_SR** (line 23)
- **HIX5I2C_TXR** (line 26)
- **I2C_ACK_INTR** (line 67)
- **I2C_ARBITRATE_INTR** (line 68)
- **I2C_BUSY** (line 62)
- **I2C_CLEAR_ACK** (line 53)
- **I2C_CLEAR_ALL** (line 56)
- **I2C_CLEAR_ARBITRATE** (line 54)
- **I2C_CLEAR_END** (line 50)
- **I2C_CLEAR_OVER** (line 55)
- **I2C_CLEAR_RECEIVE** (line 52)
- **I2C_CLEAR_SEND** (line 51)
- **I2C_CLEAR_START** (line 49)
- **I2C_ENABLE** (line 30)
- **I2C_END_INTR** (line 64)
- **I2C_NO_ACK** (line 42)
- **I2C_OVER_INTR** (line 69)
- **I2C_READ** (line 44)
- **I2C_RECEIVE_INTR** (line 66)
- **I2C_SEND_INTR** (line 65)
- **I2C_START** (line 43)
- **I2C_START_INTR** (line 63)
- **I2C_STOP** (line 46)
- **I2C_UNMASK_ACK** (line 36)
- **I2C_UNMASK_ALL** (line 39)
- **I2C_UNMASK_ARBITRATE** (line 37)
- **I2C_UNMASK_END** (line 33)
- **I2C_UNMASK_OVER** (line 38)
- **I2C_UNMASK_RECEIVE** (line 35)
- **I2C_UNMASK_SEND** (line 34)
- **I2C_UNMASK_START** (line 32)
- **I2C_UNMASK_TOTAL** (line 31)
- **I2C_WRITE** (line 45)
