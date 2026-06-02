# drivers/i2c/busses/i2c-axxia.c

Subsystem: drivers/i2c

## Functions (25)

### axxia_i2c_empty_rx_fifo
- Return type: static int
- Signature: axxia_i2c_empty_rx_fifo(struct axxia_i2c_dev * idev)
- Line: 267

### axxia_i2c_fill_tx_fifo
- Return type: static int
- Signature: axxia_i2c_fill_tx_fifo(struct axxia_i2c_dev * idev)
- Line: 299

### axxia_i2c_func
- Return type: static u32
- Signature: axxia_i2c_func(struct i2c_adapter * adap)
- Line: 654

### axxia_i2c_get_scl
- Return type: static int
- Signature: axxia_i2c_get_scl(struct i2c_adapter * adap)
- Line: 621

### axxia_i2c_get_sda
- Return type: static int
- Signature: axxia_i2c_get_sda(struct i2c_adapter * adap)
- Line: 640

### axxia_i2c_handle_seq_nak
- Return type: static int
- Signature: axxia_i2c_handle_seq_nak(struct axxia_i2c_dev * idev)
- Line: 453

### axxia_i2c_init
- Return type: static int
- Signature: axxia_i2c_init(struct axxia_i2c_dev * idev)
- Line: 178

### axxia_i2c_isr
- Return type: static irqreturn_t
- Signature: axxia_i2c_isr(int irq,void * _dev)
- Line: 359

### axxia_i2c_probe
- Return type: static int
- Signature: axxia_i2c_probe(struct platform_device * pdev)
- Line: 720

### axxia_i2c_reg_slave
- Return type: static int
- Signature: axxia_i2c_reg_slave(struct i2c_client * slave)
- Line: 661

### axxia_i2c_remove
- Return type: static void
- Signature: axxia_i2c_remove(struct platform_device * pdev)
- Line: 794

### axxia_i2c_sequence_ok
- Return type: static bool
- Signature: axxia_i2c_sequence_ok(struct i2c_msg msgs[],int num)
- Line: 592

### axxia_i2c_set_addr
- Return type: static void
- Signature: axxia_i2c_set_addr(struct axxia_i2c_dev * idev,struct i2c_msg * msg)
- Line: 433

### axxia_i2c_set_scl
- Return type: static void
- Signature: axxia_i2c_set_scl(struct i2c_adapter * adap,int val)
- Line: 628

### axxia_i2c_slv_fifo_event
- Return type: static void
- Signature: axxia_i2c_slv_fifo_event(struct axxia_i2c_dev * idev)
- Line: 312

### axxia_i2c_slv_isr
- Return type: static irqreturn_t
- Signature: axxia_i2c_slv_isr(struct axxia_i2c_dev * idev)
- Line: 335

### axxia_i2c_unreg_slave
- Return type: static int
- Signature: axxia_i2c_unreg_slave(struct i2c_client * slave)
- Line: 693

### axxia_i2c_xfer
- Return type: static int
- Signature: axxia_i2c_xfer(struct i2c_adapter * adap,struct i2c_msg msgs[],int num)
- Line: 600

### axxia_i2c_xfer_msg
- Return type: static int
- Signature: axxia_i2c_xfer_msg(struct axxia_i2c_dev * idev,struct i2c_msg * msg,bool last)
- Line: 511

### axxia_i2c_xfer_seq
- Return type: static int
- Signature: axxia_i2c_xfer_seq(struct axxia_i2c_dev * idev,struct i2c_msg msgs[])
- Line: 466

### i2c_int_disable
- Return type: static void
- Signature: i2c_int_disable(struct axxia_i2c_dev * idev,u32 mask)
- Line: 154

### i2c_int_enable
- Return type: static void
- Signature: i2c_int_enable(struct axxia_i2c_dev * idev,u32 mask)
- Line: 162

### i2c_m_rd
- Return type: static int
- Signature: i2c_m_rd(const struct i2c_msg * msg)
- Line: 253

### i2c_m_recv_len
- Return type: static int
- Signature: i2c_m_recv_len(const struct i2c_msg * msg)
- Line: 258

### ns_to_clk
- Return type: static u32
- Signature: ns_to_clk(u64 ns,u32 clk_mhz)
- Line: 173

## Structs (1)

### axxia_i2c_dev
- Line: 137
- Members:
  - base: void __iomem *
  - msg: i2c_msg *
  - msg_r: i2c_msg *
  - msg_xfrd: size_t
  - msg_xfrd_r: size_t
  - msg_err: int
  - msg_complete: completion
  - dev: device *
  - adapter: i2c_adapter
  - i2c_clk: clk *
  - bus_clk_rate: u32
  - last: bool
  - slave: i2c_client *
  - irq: int

## Variables (5)

- static **axxia_i2c_algo** : const struct i2c_algorithm (line 708)
- static **axxia_i2c_driver** : platform_driver (line 810)
- static **axxia_i2c_of_match** : const struct of_device_id[] (line 803)
- static **axxia_i2c_quirks** : const struct i2c_adapter_quirks (line 715)
- static **axxia_i2c_recovery_info** : i2c_bus_recovery_info (line 647)

## Macros (93)

- **BM_SCLC** (line 45)
- **BM_SCLS** (line 47)
- **BM_SDAC** (line 44)
- **BM_SDAS** (line 46)
- **CMD_AUTO** (line 52)
- **CMD_BUSY** (line 50)
- **CMD_MANUAL** (line 51)
- **CMD_SEQUENCE** (line 53)
- **FIFO_SIZE** (line 25)
- **GLOBAL_CONTROL** (line 28)
- **GLOBAL_IBML_EN** (line 31)
- **GLOBAL_MST_EN** (line 29)
- **GLOBAL_SLV_EN** (line 30)
- **I2C_BUS_MONITOR** (line 43)
- **I2C_STOP_TIMEOUT** (line 24)
- **I2C_XFER_TIMEOUT** (line 23)
- **IBML_LOW_MEXT** (line 40)
- **IBML_LOW_SEXT** (line 41)
- **IBML_TIMEOUT** (line 39)
- **INTERRUPT_ENABLE** (line 33)
- **INTERRUPT_STATUS** (line 32)
- **INT_MST** (line 35)
- **INT_SLV** (line 34)
- **MST_ADDR_1** (line 56)
- **MST_ADDR_2** (line 57)
- **MST_COMMAND** (line 49)
- **MST_DATA** (line 58)
- **MST_INT_ENABLE** (line 61)
- **MST_INT_STATUS** (line 62)
- **MST_RX_BYTES_XFRD** (line 79)
- **MST_RX_FIFO** (line 60)
- **MST_RX_XFER** (line 54)
- **MST_STATUS_AL** (line 70)
- **MST_STATUS_ERR** (line 75)
- **MST_STATUS_IP** (line 68)
- **MST_STATUS_NA** (line 72)
- **MST_STATUS_NAK** (line 73)
- **MST_STATUS_ND** (line 71)
- **MST_STATUS_RFL** (line 63)
- **MST_STATUS_SCC** (line 67)
- **MST_STATUS_SNS** (line 65)
- **MST_STATUS_SS** (line 66)
- **MST_STATUS_TFL** (line 64)
- **MST_STATUS_TSS** (line 69)
- **MST_TX_BYTES_XFRD** (line 78)
- **MST_TX_FIFO** (line 59)
- **MST_TX_XFER** (line 55)
- **SCL_HIGH_PERIOD** (line 114)
- **SCL_LOW_PERIOD** (line 115)
- **SCL_WAIT_TIMEOUT_NS** (line 22)
- **SDA_HOLD_TIME** (line 118)
- **SDA_SETUP_TIME** (line 117)
- **SEQ_LEN** (line 26)
- **SLV_ADDR_1** (line 87)
- **SLV_ADDR_2** (line 88)
- **SLV_ADDR_DEC_CTL** (line 80)
- **SLV_ADDR_DEC_GCE** (line 81)
- **SLV_ADDR_DEC_OGCE** (line 82)
- **SLV_ADDR_DEC_SA1E** (line 83)
- **SLV_ADDR_DEC_SA1M** (line 84)
- **SLV_ADDR_DEC_SA2E** (line 85)
- **SLV_ADDR_DEC_SA2M** (line 86)
- **SLV_DATA** (line 93)
- **SLV_FIFO_AS** (line 97)
- **SLV_FIFO_DV** (line 102)
- **SLV_FIFO_DV1** (line 95)
- **SLV_FIFO_DV2** (line 96)
- **SLV_FIFO_RSC** (line 100)
- **SLV_FIFO_STPC** (line 101)
- **SLV_FIFO_STRC** (line 99)
- **SLV_FIFO_TNAK** (line 98)
- **SLV_INT_ENABLE** (line 103)
- **SLV_INT_STATUS** (line 104)
- **SLV_READ_DUMMY** (line 113)
- **SLV_RX_ACGCA** (line 92)
- **SLV_RX_ACSA1** (line 90)
- **SLV_RX_ACSA2** (line 91)
- **SLV_RX_CTL** (line 89)
- **SLV_RX_FIFO** (line 94)
- **SLV_STATUS_RFH** (line 105)
- **SLV_STATUS_SRAT1** (line 111)
- **SLV_STATUS_SRC1** (line 110)
- **SLV_STATUS_SRDRE1** (line 112)
- **SLV_STATUS_SRND1** (line 109)
- **SLV_STATUS_SRRS1** (line 108)
- **SLV_STATUS_SRS1** (line 107)
- **SLV_STATUS_WTC** (line 106)
- **SOFT_RESET** (line 48)
- **SPIKE_FLTR_LEN** (line 116)
- **TIMER_CLOCK_DIV** (line 42)
- **WAIT_TIMER_CONTROL** (line 36)
- **WT_EN** (line 37)
- **WT_VALUE**(_x) (line 38)
