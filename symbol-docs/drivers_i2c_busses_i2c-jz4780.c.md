# drivers/i2c/busses/i2c-jz4780.c

Subsystem: drivers/i2c

## Functions (18)

### jz4780_i2c_cleanup
- Return type: static int
- Signature: jz4780_i2c_cleanup(struct jz4780_i2c * i2c)
- Line: 361

### jz4780_i2c_disable
- Return type: static int
- Signature: jz4780_i2c_disable(struct jz4780_i2c * i2c)
- Line: 183

### jz4780_i2c_enable
- Return type: static int
- Signature: jz4780_i2c_enable(struct jz4780_i2c * i2c)
- Line: 202

### jz4780_i2c_functionality
- Return type: static u32
- Signature: jz4780_i2c_functionality(struct i2c_adapter * adap)
- Line: 727

### jz4780_i2c_irq
- Return type: static irqreturn_t
- Signature: jz4780_i2c_irq(int irqno,void * dev_id)
- Line: 434

### jz4780_i2c_prepare
- Return type: static int
- Signature: jz4780_i2c_prepare(struct jz4780_i2c * i2c)
- Line: 406

### jz4780_i2c_probe
- Return type: static int
- Signature: jz4780_i2c_probe(struct platform_device * pdev)
- Line: 761

### jz4780_i2c_readw
- Return type: static unsigned short
- Signature: jz4780_i2c_readw(struct jz4780_i2c * i2c,unsigned long offset)
- Line: 171

### jz4780_i2c_remove
- Return type: static void
- Signature: jz4780_i2c_remove(struct platform_device * pdev)
- Line: 841

### jz4780_i2c_send_rcmd
- Return type: static void
- Signature: jz4780_i2c_send_rcmd(struct jz4780_i2c * i2c,int cmd_count,int cmd_left)
- Line: 412

### jz4780_i2c_set_speed
- Return type: static int
- Signature: jz4780_i2c_set_speed(struct jz4780_i2c * i2c)
- Line: 247

### jz4780_i2c_set_target
- Return type: static int
- Signature: jz4780_i2c_set_target(struct jz4780_i2c * i2c,unsigned char address)
- Line: 221

### jz4780_i2c_trans_done
- Return type: static void
- Signature: jz4780_i2c_trans_done(struct jz4780_i2c * i2c)
- Line: 428

### jz4780_i2c_txabrt
- Return type: static void
- Signature: jz4780_i2c_txabrt(struct jz4780_i2c * i2c,int src)
- Line: 557

### jz4780_i2c_writew
- Return type: static void
- Signature: jz4780_i2c_writew(struct jz4780_i2c * i2c,unsigned long offset,unsigned short val)
- Line: 177

### jz4780_i2c_xfer
- Return type: static int
- Signature: jz4780_i2c_xfer(struct i2c_adapter * adap,struct i2c_msg * msg,int count)
- Line: 690

### jz4780_i2c_xfer_read
- Return type: static int
- Signature: jz4780_i2c_xfer_read(struct jz4780_i2c * i2c,unsigned char * buf,int len,int cnt,int idx)
- Line: 563

### jz4780_i2c_xfer_write
- Return type: static int
- Signature: jz4780_i2c_xfer_write(struct jz4780_i2c * i2c,unsigned char * buf,int len,int cnt,int idx)
- Line: 624

## Structs (2)

### ingenic_i2c_config
- Line: 132
- Members:
  - version: ingenic_i2c_version
  - fifosize: int
  - tx_level: int
  - rx_level: int
  - iomem: void __iomem *
  - irq: int
  - clk: clk *
  - adap: i2c_adapter
  - cdata: const struct ingenic_i2c_config *
  - lock: spinlock_t
  - rbuf: unsigned char *
  - rd_total_len: int
  - rd_data_xfered: int
  - rd_cmd_xfered: int
  - wbuf: unsigned char *
  - wt_len: int
  - is_write: int
  - stop_hold: int
  - speed: int
  - data_buf: int[]
  - cmd_buf: int[]
  - cmd: int
  - trans_waitq: completion

### jz4780_i2c
- Line: 140
- Members:
  - version: ingenic_i2c_version
  - fifosize: int
  - tx_level: int
  - rx_level: int
  - iomem: void __iomem *
  - irq: int
  - clk: clk *
  - adap: i2c_adapter
  - cdata: const struct ingenic_i2c_config *
  - lock: spinlock_t
  - rbuf: unsigned char *
  - rd_total_len: int
  - rd_data_xfered: int
  - rd_cmd_xfered: int
  - wbuf: unsigned char *
  - wt_len: int
  - is_write: int
  - stop_hold: int
  - speed: int
  - data_buf: int[]
  - cmd_buf: int[]
  - cmd: int
  - trans_waitq: completion

## Enums (1)

### ingenic_i2c_version
- Line: 126

## Variables (5)

- static **jz4780_i2c_algorithm** : const struct i2c_algorithm (line 732)
- static **jz4780_i2c_config** : const struct ingenic_i2c_config (line 737)
- static **jz4780_i2c_driver** : platform_driver (line 848)
- static **jz4780_i2c_of_matches** : const struct of_device_id[] (line 753)
- static **x1000_i2c_config** : const struct ingenic_i2c_config (line 745)

## Macros (85)

- **BUFSIZE** (line 124)
- **JZ4780_I2CFHCNT_ADJUST**(n) (line 115)
- **JZ4780_I2CFLCNT_ADJUST**(n) (line 116)
- **JZ4780_I2CSHCNT_ADJUST**(n) (line 113)
- **JZ4780_I2CSLCNT_ADJUST**(n) (line 114)
- **JZ4780_I2C_ACKGC** (line 57)
- **JZ4780_I2C_CACT** (line 46)
- **JZ4780_I2C_CGC** (line 49)
- **JZ4780_I2C_CINTR** (line 39)
- **JZ4780_I2C_CRXDONE** (line 45)
- **JZ4780_I2C_CRXOF** (line 41)
- **JZ4780_I2C_CRXREQ** (line 43)
- **JZ4780_I2C_CRXUF** (line 40)
- **JZ4780_I2C_CSTP** (line 47)
- **JZ4780_I2C_CSTT** (line 48)
- **JZ4780_I2C_CTRL** (line 27)
- **JZ4780_I2C_CTRL_MATP** (line 65)
- **JZ4780_I2C_CTRL_MD** (line 69)
- **JZ4780_I2C_CTRL_REST** (line 64)
- **JZ4780_I2C_CTRL_SATP** (line 66)
- **JZ4780_I2C_CTRL_SLVDIS** (line 63)
- **JZ4780_I2C_CTRL_SPDF** (line 67)
- **JZ4780_I2C_CTRL_SPDS** (line 68)
- **JZ4780_I2C_CTRL_STPHLD** (line 62)
- **JZ4780_I2C_CTXABRT** (line 44)
- **JZ4780_I2C_CTXOF** (line 42)
- **JZ4780_I2C_DC** (line 30)
- **JZ4780_I2C_DC_READ** (line 107)
- **JZ4780_I2C_DMACR** (line 53)
- **JZ4780_I2C_DMARDLR** (line 55)
- **JZ4780_I2C_DMATDLR** (line 54)
- **JZ4780_I2C_ENB** (line 50)
- **JZ4780_I2C_ENB_I2C** (line 111)
- **JZ4780_I2C_ENSTA** (line 58)
- **JZ4780_I2C_FHCNT** (line 33)
- **JZ4780_I2C_FIFO_LEN** (line 118)
- **JZ4780_I2C_FLCNT** (line 34)
- **JZ4780_I2C_INTM** (line 36)
- **JZ4780_I2C_INTM_MIACT** (line 97)
- **JZ4780_I2C_INTM_MIGC** (line 94)
- **JZ4780_I2C_INTM_MISTP** (line 96)
- **JZ4780_I2C_INTM_MISTT** (line 95)
- **JZ4780_I2C_INTM_MRDREQ** (line 100)
- **JZ4780_I2C_INTM_MRXDN** (line 98)
- **JZ4780_I2C_INTM_MRXFL** (line 103)
- **JZ4780_I2C_INTM_MRXOF** (line 104)
- **JZ4780_I2C_INTM_MRXUF** (line 105)
- **JZ4780_I2C_INTM_MTXABT** (line 99)
- **JZ4780_I2C_INTM_MTXEMP** (line 101)
- **JZ4780_I2C_INTM_MTXOF** (line 102)
- **JZ4780_I2C_INTST** (line 35)
- **JZ4780_I2C_INTST_IACT** (line 84)
- **JZ4780_I2C_INTST_IGC** (line 81)
- **JZ4780_I2C_INTST_ISTP** (line 83)
- **JZ4780_I2C_INTST_ISTT** (line 82)
- **JZ4780_I2C_INTST_RDREQ** (line 87)
- **JZ4780_I2C_INTST_RXDN** (line 85)
- **JZ4780_I2C_INTST_RXFL** (line 90)
- **JZ4780_I2C_INTST_RXOF** (line 91)
- **JZ4780_I2C_INTST_RXUF** (line 92)
- **JZ4780_I2C_INTST_TXABT** (line 86)
- **JZ4780_I2C_INTST_TXEMP** (line 88)
- **JZ4780_I2C_INTST_TXOF** (line 89)
- **JZ4780_I2C_RXTL** (line 37)
- **JZ4780_I2C_SAR** (line 29)
- **JZ4780_I2C_SDAHD** (line 59)
- **JZ4780_I2C_SDAHD_HDENB** (line 109)
- **JZ4780_I2C_SDASU** (line 56)
- **JZ4780_I2C_SHCNT** (line 31)
- **JZ4780_I2C_SLCNT** (line 32)
- **JZ4780_I2C_STA** (line 51)
- **JZ4780_I2C_STA_ACT** (line 77)
- **JZ4780_I2C_STA_MSTACT** (line 72)
- **JZ4780_I2C_STA_RFF** (line 73)
- **JZ4780_I2C_STA_RFNE** (line 74)
- **JZ4780_I2C_STA_SLVACT** (line 71)
- **JZ4780_I2C_STA_TFE** (line 75)
- **JZ4780_I2C_STA_TFNF** (line 76)
- **JZ4780_I2C_TAR** (line 28)
- **JZ4780_I2C_TIMEOUT** (line 122)
- **JZ4780_I2C_TXABRT** (line 52)
- **JZ4780_I2C_TXTL** (line 38)
- **X1000_I2C_DC_STOP** (line 79)
- **X1000_I2C_FIFO_LEN** (line 120)
- **X1000_I2C_SDAHD** (line 60)
