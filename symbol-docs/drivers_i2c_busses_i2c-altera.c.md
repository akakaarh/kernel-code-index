# drivers/i2c/busses/i2c-altera.c

Subsystem: drivers/i2c

## Functions (17)

### altr_i2c_core_disable
- Return type: static void
- Signature: altr_i2c_core_disable(struct altr_i2c_dev * idev)
- Line: 112

### altr_i2c_core_enable
- Return type: static void
- Signature: altr_i2c_core_enable(struct altr_i2c_dev * idev)
- Line: 119

### altr_i2c_empty_rx_fifo
- Return type: static void
- Signature: altr_i2c_empty_rx_fifo(struct altr_i2c_dev * idev)
- Line: 192

### altr_i2c_fill_tx_fifo
- Return type: static int
- Signature: altr_i2c_fill_tx_fifo(struct altr_i2c_dev * idev)
- Line: 207

### altr_i2c_func
- Return type: static u32
- Signature: altr_i2c_func(struct i2c_adapter * adap)
- Line: 373

### altr_i2c_init
- Return type: static void
- Signature: altr_i2c_init(struct altr_i2c_dev * idev)
- Line: 137

### altr_i2c_int_clear
- Return type: static void
- Signature: altr_i2c_int_clear(struct altr_i2c_dev * idev,u32 mask)
- Line: 105

### altr_i2c_int_enable
- Return type: static void
- Signature: altr_i2c_int_enable(struct altr_i2c_dev * idev,u32 mask,bool enable)
- Line: 92

### altr_i2c_isr
- Return type: static irqreturn_t
- Signature: altr_i2c_isr(int irq,void * _dev)
- Line: 235

### altr_i2c_isr_quick
- Return type: static irqreturn_t
- Signature: altr_i2c_isr_quick(int irq,void * _dev)
- Line: 222

### altr_i2c_probe
- Return type: static int
- Signature: altr_i2c_probe(struct platform_device * pdev)
- Line: 383

### altr_i2c_remove
- Return type: static void
- Signature: altr_i2c_remove(struct platform_device * pdev)
- Line: 468

### altr_i2c_reset
- Return type: static void
- Signature: altr_i2c_reset(struct altr_i2c_dev * idev)
- Line: 126

### altr_i2c_stop
- Return type: static void
- Signature: altr_i2c_stop(struct altr_i2c_dev * idev)
- Line: 132

### altr_i2c_transfer
- Return type: static void
- Signature: altr_i2c_transfer(struct altr_i2c_dev * idev,u32 data)
- Line: 179

### altr_i2c_xfer
- Return type: static int
- Signature: altr_i2c_xfer(struct i2c_adapter * adap,struct i2c_msg * msgs,int num)
- Line: 360

### altr_i2c_xfer_msg
- Return type: static int
- Signature: altr_i2c_xfer_msg(struct altr_i2c_dev * idev,struct i2c_msg * msg)
- Line: 305

## Structs (1)

### altr_i2c_dev
- Line: 74
- Members:
  - base: void __iomem *
  - msg: i2c_msg *
  - msg_len: size_t
  - msg_err: int
  - msg_complete: completion
  - dev: device *
  - adapter: i2c_adapter
  - i2c_clk: clk *
  - bus_clk_rate: u32
  - buf: u8 *
  - fifo_size: u32
  - isr_mask: u32
  - isr_status: u32
  - isr_mutex: mutex

## Variables (3)

- static **altr_i2c_algo** : const struct i2c_algorithm (line 378)
- static **altr_i2c_driver** : platform_driver (line 483)
- static **altr_i2c_of_match** : const struct of_device_id[] (line 477)

## Macros (34)

- **ALTR_I2C_ALL_IRQ** (line 48)
- **ALTR_I2C_CTRL** (line 23)
- **ALTR_I2C_CTRL_BSPEED** (line 26)
- **ALTR_I2C_CTRL_EN** (line 27)
- **ALTR_I2C_CTRL_RXT_SHFT** (line 24)
- **ALTR_I2C_CTRL_TCT_SHFT** (line 25)
- **ALTR_I2C_DFLT_FIFO_SZ** (line 53)
- **ALTR_I2C_ISER** (line 28)
- **ALTR_I2C_ISER_ARB_EN** (line 30)
- **ALTR_I2C_ISER_NACK_EN** (line 31)
- **ALTR_I2C_ISER_RXOF_EN** (line 29)
- **ALTR_I2C_ISER_RXRDY_EN** (line 32)
- **ALTR_I2C_ISER_TXRDY_EN** (line 33)
- **ALTR_I2C_ISR** (line 34)
- **ALTR_I2C_ISR_ARB** (line 36)
- **ALTR_I2C_ISR_NACK** (line 37)
- **ALTR_I2C_ISR_RXOF** (line 35)
- **ALTR_I2C_ISR_RXRDY** (line 38)
- **ALTR_I2C_ISR_TXRDY** (line 39)
- **ALTR_I2C_RX_DATA** (line 22)
- **ALTR_I2C_RX_FIFO_LVL** (line 43)
- **ALTR_I2C_SCL_HIGH** (line 45)
- **ALTR_I2C_SCL_LOW** (line 44)
- **ALTR_I2C_SDA_HOLD** (line 46)
- **ALTR_I2C_STATUS** (line 40)
- **ALTR_I2C_STAT_CORE** (line 41)
- **ALTR_I2C_TC_FIFO_LVL** (line 42)
- **ALTR_I2C_TFR_CMD** (line 18)
- **ALTR_I2C_TFR_CMD_RW_D** (line 21)
- **ALTR_I2C_TFR_CMD_STA** (line 19)
- **ALTR_I2C_TFR_CMD_STO** (line 20)
- **ALTR_I2C_THRESHOLD** (line 52)
- **ALTR_I2C_TIMEOUT** (line 54)
- **ALTR_I2C_XFER_TIMEOUT** (line 55)
