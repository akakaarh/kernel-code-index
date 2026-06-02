# drivers/i2c/busses/i2c-hisi.c

Subsystem: drivers/i2c

## Functions (15)

### hisi_i2c_clear_int
- Return type: static void
- Signature: hisi_i2c_clear_int(struct hisi_i2c_controller * ctlr,u32 mask)
- Line: 124

### hisi_i2c_clear_tx_int
- Return type: static void
- Signature: hisi_i2c_clear_tx_int(struct hisi_i2c_controller * ctlr,u32 mask)
- Line: 129

### hisi_i2c_configure_bus
- Return type: static void
- Signature: hisi_i2c_configure_bus(struct hisi_i2c_controller * ctlr)
- Line: 415

### hisi_i2c_disable_int
- Return type: static void
- Signature: hisi_i2c_disable_int(struct hisi_i2c_controller * ctlr,u32 mask)
- Line: 119

### hisi_i2c_enable_int
- Return type: static void
- Signature: hisi_i2c_enable_int(struct hisi_i2c_controller * ctlr,u32 mask)
- Line: 114

### hisi_i2c_functionality
- Return type: static u32
- Signature: hisi_i2c_functionality(struct i2c_adapter * adap)
- Line: 233

### hisi_i2c_handle_errors
- Return type: static void
- Signature: hisi_i2c_handle_errors(struct hisi_i2c_controller * ctlr)
- Line: 134

### hisi_i2c_irq
- Return type: static irqreturn_t
- Signature: hisi_i2c_irq(int irq,void * context)
- Line: 338

### hisi_i2c_probe
- Return type: static int
- Signature: hisi_i2c_probe(struct platform_device * pdev)
- Line: 458

### hisi_i2c_read_rx_fifo
- Return type: static int
- Signature: hisi_i2c_read_rx_fifo(struct hisi_i2c_controller * ctlr)
- Line: 243

### hisi_i2c_reset_xfer
- Return type: static void
- Signature: hisi_i2c_reset_xfer(struct hisi_i2c_controller * ctlr)
- Line: 184

### hisi_i2c_set_scl
- Return type: static void
- Signature: hisi_i2c_set_scl(struct hisi_i2c_controller * ctlr,u32 divide,u32 divisor,u32 reg_hcnt,u32 reg_lcnt)
- Line: 389

### hisi_i2c_start_xfer
- Return type: static int
- Signature: hisi_i2c_start_xfer(struct hisi_i2c_controller * ctlr)
- Line: 155

### hisi_i2c_xfer
- Return type: static int
- Signature: hisi_i2c_xfer(struct i2c_adapter * adap,struct i2c_msg * msgs,int num)
- Line: 200

### hisi_i2c_xfer_msg
- Return type: static void
- Signature: hisi_i2c_xfer_msg(struct hisi_i2c_controller * ctlr)
- Line: 275

## Structs (1)

### hisi_i2c_controller
- Line: 90
- Members:
  - adapter: i2c_adapter
  - iobase: void __iomem *
  - dev: device *
  - clk: clk *
  - irq: int
  - completion: completion *
  - msgs: i2c_msg *
  - msg_num: int
  - msg_tx_idx: int
  - buf_tx_idx: int
  - msg_rx_idx: int
  - buf_rx_idx: int
  - tar_addr: u16
  - xfer_err: u32
  - t: i2c_timings
  - clk_rate_khz: u32
  - spk_len: u32

## Variables (4)

- static **hisi_i2c_acpi_ids** : const struct acpi_device_id[] (line 519)
- static **hisi_i2c_algo** : const struct i2c_algorithm (line 238)
- static **hisi_i2c_driver** : platform_driver (line 531)
- static **hisi_i2c_dts_ids** : const struct of_device_id[] (line 525)

## Macros (62)

- **HISI_I2C_CMD_TXDATA** (line 28)
- **HISI_I2C_CMD_TXDATA_DATA** (line 29)
- **HISI_I2C_CMD_TXDATA_P_EN** (line 31)
- **HISI_I2C_CMD_TXDATA_RW** (line 30)
- **HISI_I2C_CMD_TXDATA_SR_EN** (line 32)
- **HISI_I2C_FAST_SPEED_MODE** (line 79)
- **HISI_I2C_FIFO_CTRL** (line 41)
- **HISI_I2C_FIFO_RX_AF_THRESH** (line 44)
- **HISI_I2C_FIFO_RX_CLR** (line 42)
- **HISI_I2C_FIFO_STATE** (line 46)
- **HISI_I2C_FIFO_STATE_RX_EMPTY** (line 49)
- **HISI_I2C_FIFO_STATE_RX_RERR** (line 47)
- **HISI_I2C_FIFO_STATE_RX_WERR** (line 48)
- **HISI_I2C_FIFO_STATE_TX_FULL** (line 52)
- **HISI_I2C_FIFO_STATE_TX_RERR** (line 50)
- **HISI_I2C_FIFO_STATE_TX_WERR** (line 51)
- **HISI_I2C_FIFO_TX_AE_THRESH** (line 45)
- **HISI_I2C_FIFO_TX_CLR** (line 43)
- **HISI_I2C_FRAME_CTRL** (line 21)
- **HISI_I2C_FRAME_CTRL_ADDR_TEN** (line 23)
- **HISI_I2C_FRAME_CTRL_SPEED_MODE** (line 22)
- **HISI_I2C_FS_SCL_HCNT** (line 37)
- **HISI_I2C_FS_SCL_LCNT** (line 38)
- **HISI_I2C_FS_SPK_LEN** (line 56)
- **HISI_I2C_FS_SPK_LEN_CNT** (line 57)
- **HISI_I2C_HIGH_SPEED_MODE** (line 80)
- **HISI_I2C_HS_SCL_HCNT** (line 39)
- **HISI_I2C_HS_SCL_LCNT** (line 40)
- **HISI_I2C_HS_SPK_LEN** (line 58)
- **HISI_I2C_HS_SPK_LEN_CNT** (line 59)
- **HISI_I2C_INT_ALL** (line 69)
- **HISI_I2C_INT_CLR** (line 63)
- **HISI_I2C_INT_ERR** (line 75)
- **HISI_I2C_INT_FIFO_ERR** (line 72)
- **HISI_I2C_INT_MASK** (line 64)
- **HISI_I2C_INT_MSTAT** (line 62)
- **HISI_I2C_INT_RX_FULL** (line 73)
- **HISI_I2C_INT_TRANS_CPLT** (line 70)
- **HISI_I2C_INT_TRANS_ERR** (line 71)
- **HISI_I2C_INT_TX_EMPTY** (line 74)
- **HISI_I2C_RXDATA** (line 33)
- **HISI_I2C_RXDATA_DATA** (line 34)
- **HISI_I2C_RX_FIFO_DEPTH** (line 83)
- **HISI_I2C_RX_F_AF_THRESH** (line 85)
- **HISI_I2C_SDA_HOLD** (line 53)
- **HISI_I2C_SDA_HOLD_RX** (line 55)
- **HISI_I2C_SDA_HOLD_TX** (line 54)
- **HISI_I2C_SLV_ADDR** (line 24)
- **HISI_I2C_SLV_ADDR_GC_S_EN** (line 27)
- **HISI_I2C_SLV_ADDR_GC_S_MODE** (line 26)
- **HISI_I2C_SLV_ADDR_VAL** (line 25)
- **HISI_I2C_SS_SCL_HCNT** (line 35)
- **HISI_I2C_SS_SCL_LCNT** (line 36)
- **HISI_I2C_STD_SPEED_MODE** (line 78)
- **HISI_I2C_TRANS_ERR** (line 66)
- **HISI_I2C_TRANS_STATE** (line 65)
- **HISI_I2C_TX_AEMPTY_INT** (line 61)
- **HISI_I2C_TX_FIFO_DEPTH** (line 82)
- **HISI_I2C_TX_F_AE_THRESH** (line 84)
- **HISI_I2C_TX_INT_CLR** (line 60)
- **HISI_I2C_VERSION** (line 67)
- **NSEC_TO_CYCLES**(ns,clk_rate_khz) (line 87)
