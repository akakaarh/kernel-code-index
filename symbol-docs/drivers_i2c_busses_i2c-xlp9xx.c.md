# drivers/i2c/busses/i2c-xlp9xx.c

Subsystem: drivers/i2c

## Functions (18)

### xlp9xx_i2c_check_bus_status
- Return type: static int
- Signature: xlp9xx_i2c_check_bus_status(struct xlp9xx_i2c_dev * priv)
- Line: 284

### xlp9xx_i2c_drain_rx_fifo
- Return type: static void
- Signature: xlp9xx_i2c_drain_rx_fifo(struct xlp9xx_i2c_dev * priv)
- Line: 180

### xlp9xx_i2c_fill_tx_fifo
- Return type: static void
- Signature: xlp9xx_i2c_fill_tx_fifo(struct xlp9xx_i2c_dev * priv)
- Line: 147

### xlp9xx_i2c_functionality
- Return type: static u32
- Signature: xlp9xx_i2c_functionality(struct i2c_adapter * adapter)
- Line: 448

### xlp9xx_i2c_get_frequency
- Return type: static int
- Signature: xlp9xx_i2c_get_frequency(struct platform_device * pdev,struct xlp9xx_i2c_dev * priv)
- Line: 459

### xlp9xx_i2c_init
- Return type: static int
- Signature: xlp9xx_i2c_init(struct xlp9xx_i2c_dev * priv)
- Line: 304

### xlp9xx_i2c_isr
- Return type: static irqreturn_t
- Signature: xlp9xx_i2c_isr(int irq,void * dev_id)
- Line: 235

### xlp9xx_i2c_mask_irq
- Return type: static void
- Signature: xlp9xx_i2c_mask_irq(struct xlp9xx_i2c_dev * priv,u32 mask)
- Line: 113

### xlp9xx_i2c_probe
- Return type: static int
- Signature: xlp9xx_i2c_probe(struct platform_device * pdev)
- Line: 506

### xlp9xx_i2c_remove
- Return type: static void
- Signature: xlp9xx_i2c_remove(struct platform_device * pdev)
- Line: 560

### xlp9xx_i2c_smbus_setup
- Return type: static int
- Signature: xlp9xx_i2c_smbus_setup(struct xlp9xx_i2c_dev * priv,struct platform_device * pdev)
- Line: 489

### xlp9xx_i2c_unmask_irq
- Return type: static void
- Signature: xlp9xx_i2c_unmask_irq(struct xlp9xx_i2c_dev * priv,u32 mask)
- Line: 121

### xlp9xx_i2c_update_rlen
- Return type: static void
- Signature: xlp9xx_i2c_update_rlen(struct xlp9xx_i2c_dev * priv)
- Line: 159

### xlp9xx_i2c_update_rx_fifo_thres
- Return type: static void
- Signature: xlp9xx_i2c_update_rx_fifo_thres(struct xlp9xx_i2c_dev * priv)
- Line: 129

### xlp9xx_i2c_xfer
- Return type: static int
- Signature: xlp9xx_i2c_xfer(struct i2c_adapter * adap,struct i2c_msg * msgs,int num)
- Line: 425

### xlp9xx_i2c_xfer_msg
- Return type: static int
- Signature: xlp9xx_i2c_xfer_msg(struct xlp9xx_i2c_dev * priv,struct i2c_msg * msg,int last_msg)
- Line: 323

### xlp9xx_read_i2c_reg
- Return type: static u32
- Signature: xlp9xx_read_i2c_reg(struct xlp9xx_i2c_dev * priv,unsigned long reg)
- Line: 107

### xlp9xx_write_i2c_reg
- Return type: static void
- Signature: xlp9xx_write_i2c_reg(struct xlp9xx_i2c_dev * priv,unsigned long reg,u32 val)
- Line: 101

## Structs (1)

### xlp9xx_i2c_dev
- Line: 82
- Members:
  - dev: device *
  - adapter: i2c_adapter
  - msg_complete: completion
  - alert_data: i2c_smbus_alert_setup
  - ara: i2c_client *
  - irq: int
  - msg_read: bool
  - len_recv: bool
  - client_pec: bool
  - base: u32 __iomem *
  - msg_buf_remaining: u32
  - msg_len: u32
  - ip_clk_hz: u32
  - clk_hz: u32
  - msg_err: u32
  - msg_buf: u8 *

## Variables (3)

- static **xlp9xx_i2c_acpi_ids** : const struct acpi_device_id[] (line 572)
- static **xlp9xx_i2c_algo** : const struct i2c_algorithm (line 454)
- static **xlp9xx_i2c_driver** : platform_driver (line 580)

## Macros (50)

- **XLP9XX_I2C_BUSY_TIMEOUT** (line 76)
- **XLP9XX_I2C_CMD** (line 24)
- **XLP9XX_I2C_CMD_ACK** (line 47)
- **XLP9XX_I2C_CMD_READ** (line 45)
- **XLP9XX_I2C_CMD_START** (line 43)
- **XLP9XX_I2C_CMD_STOP** (line 44)
- **XLP9XX_I2C_CMD_WRITE** (line 46)
- **XLP9XX_I2C_CTRL** (line 23)
- **XLP9XX_I2C_CTRL_ADDMODE** (line 55)
- **XLP9XX_I2C_CTRL_EN** (line 52)
- **XLP9XX_I2C_CTRL_FIFORD** (line 54)
- **XLP9XX_I2C_CTRL_MASTER** (line 53)
- **XLP9XX_I2C_CTRL_MCTLEN_MASK** (line 50)
- **XLP9XX_I2C_CTRL_MCTLEN_SHIFT** (line 49)
- **XLP9XX_I2C_CTRL_RST** (line 51)
- **XLP9XX_I2C_DIV** (line 22)
- **XLP9XX_I2C_FIFOWCNT** (line 34)
- **XLP9XX_I2C_FIFO_SIZE** (line 74)
- **XLP9XX_I2C_FIFO_WCNT_MASK** (line 78)
- **XLP9XX_I2C_GENCALLADDR** (line 39)
- **XLP9XX_I2C_INTEN** (line 35)
- **XLP9XX_I2C_INTEN_ARLOST** (line 60)
- **XLP9XX_I2C_INTEN_BUSERR** (line 64)
- **XLP9XX_I2C_INTEN_DATADONE** (line 59)
- **XLP9XX_I2C_INTEN_MFIFOEMTY** (line 62)
- **XLP9XX_I2C_INTEN_MFIFOFULL** (line 61)
- **XLP9XX_I2C_INTEN_MFIFOHI** (line 63)
- **XLP9XX_I2C_INTEN_NACKADDR** (line 57)
- **XLP9XX_I2C_INTEN_SADDR** (line 58)
- **XLP9XX_I2C_INTST** (line 36)
- **XLP9XX_I2C_IP_CLK_FREQ** (line 73)
- **XLP9XX_I2C_MFIFOCTRL** (line 28)
- **XLP9XX_I2C_MFIFOCTRL_HITH_SHIFT** (line 66)
- **XLP9XX_I2C_MFIFOCTRL_LOTH_SHIFT** (line 67)
- **XLP9XX_I2C_MFIFOCTRL_RST** (line 68)
- **XLP9XX_I2C_MRXFIFO** (line 27)
- **XLP9XX_I2C_MTXFIFO** (line 26)
- **XLP9XX_I2C_OWNADDR** (line 33)
- **XLP9XX_I2C_SFIFOCTRL** (line 31)
- **XLP9XX_I2C_SLAVEADDR** (line 32)
- **XLP9XX_I2C_SLAVEADDR_ADDR_SHIFT** (line 71)
- **XLP9XX_I2C_SLAVEADDR_RW** (line 70)
- **XLP9XX_I2C_SRXFIFO** (line 30)
- **XLP9XX_I2C_STATUS** (line 25)
- **XLP9XX_I2C_STATUS_BUSY** (line 41)
- **XLP9XX_I2C_STATUS_ERRMASK** (line 79)
- **XLP9XX_I2C_STXFIFO** (line 29)
- **XLP9XX_I2C_TIMEOUT** (line 38)
- **XLP9XX_I2C_TIMEOUT_MS** (line 75)
- **XLP9XX_I2C_WAITCNT** (line 37)
