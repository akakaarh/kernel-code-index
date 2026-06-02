# drivers/i2c/busses/i2c-st.c

Subsystem: drivers/i2c

## Functions (23)

### st_i2c_clr_bits
- Return type: static void
- Signature: st_i2c_clr_bits(void __iomem * reg,u32 mask)
- Line: 204

### st_i2c_flush_rx_fifo
- Return type: static void
- Signature: st_i2c_flush_rx_fifo(struct st_i2c_dev * i2c_dev)
- Line: 237

### st_i2c_func
- Return type: static u32
- Signature: st_i2c_func(struct i2c_adapter * adap)
- Line: 757

### st_i2c_handle_read
- Return type: static void
- Signature: st_i2c_handle_read(struct st_i2c_dev * i2c_dev)
- Line: 524

### st_i2c_handle_write
- Return type: static void
- Signature: st_i2c_handle_write(struct st_i2c_dev * i2c_dev)
- Line: 507

### st_i2c_hw_config
- Return type: static void
- Signature: st_i2c_hw_config(struct st_i2c_dev * i2c_dev)
- Line: 272

### st_i2c_isr_thread
- Return type: static irqreturn_t
- Signature: st_i2c_isr_thread(int irq,void * data)
- Line: 559

### st_i2c_of_get_deglitch
- Return type: static int
- Signature: st_i2c_of_get_deglitch(struct device_node * np,struct st_i2c_dev * i2c_dev)
- Line: 771

### st_i2c_probe
- Return type: static int
- Signature: st_i2c_probe(struct platform_device * pdev)
- Line: 793

### st_i2c_rd_fill_tx_fifo
- Return type: static void
- Signature: st_i2c_rd_fill_tx_fifo(struct st_i2c_dev * i2c_dev,u32 max)
- Line: 440

### st_i2c_read_rx_fifo
- Return type: static void
- Signature: st_i2c_read_rx_fifo(struct st_i2c_dev * i2c_dev)
- Line: 458

### st_i2c_recover_bus
- Return type: static int
- Signature: st_i2c_recover_bus(struct i2c_adapter * i2c_adap)
- Line: 339

### st_i2c_remove
- Return type: static void
- Signature: st_i2c_remove(struct platform_device * pdev)
- Line: 869

### st_i2c_resume
- Return type: static int
- Signature: st_i2c_resume(struct device * dev)
- Line: 746

### st_i2c_set_bits
- Return type: static void
- Signature: st_i2c_set_bits(void __iomem * reg,u32 mask)
- Line: 199

### st_i2c_soft_reset
- Return type: static void
- Signature: st_i2c_soft_reset(struct st_i2c_dev * i2c_dev)
- Line: 256

### st_i2c_suspend
- Return type: static int
- Signature: st_i2c_suspend(struct device * dev)
- Line: 734

### st_i2c_terminate_xfer
- Return type: static void
- Signature: st_i2c_terminate_xfer(struct st_i2c_dev * i2c_dev)
- Line: 487

### st_i2c_wait_free_bus
- Return type: static int
- Signature: st_i2c_wait_free_bus(struct st_i2c_dev * i2c_dev)
- Line: 371

### st_i2c_wr_fill_tx_fifo
- Return type: static void
- Signature: st_i2c_wr_fill_tx_fifo(struct st_i2c_dev * i2c_dev)
- Line: 414

### st_i2c_write_tx_fifo
- Return type: static void
- Signature: st_i2c_write_tx_fifo(struct st_i2c_dev * i2c_dev,u8 byte)
- Line: 400

### st_i2c_xfer
- Return type: static int
- Signature: st_i2c_xfer(struct i2c_adapter * i2c_adap,struct i2c_msg msgs[],int num)
- Line: 704

### st_i2c_xfer_msg
- Return type: static int
- Signature: st_i2c_xfer_msg(struct st_i2c_dev * i2c_dev,struct i2c_msg * msg,bool is_first,bool is_last)
- Line: 639

## Structs (3)

### st_i2c_client
- Line: 162
- Members:
  - rate: u32
  - rep_start_hold: u32
  - rep_start_setup: u32
  - start_hold: u32
  - data_setup_time: u32
  - stop_setup_time: u32
  - bus_free_time: u32
  - sda_pulse_min_limit: u32
  - addr: u8
  - count: u32
  - xfered: u32
  - buf: u8 *
  - result: int
  - stop: bool
  - adap: i2c_adapter
  - dev: device *
  - base: void __iomem *
  - complete: completion
  - irq: int
  - clk: clk *
  - mode: int
  - scl_min_width_us: u32
  - sda_min_width_us: u32
  - client: st_i2c_client
  - busy: bool

### st_i2c_dev
- Line: 185
- Members:
  - rate: u32
  - rep_start_hold: u32
  - rep_start_setup: u32
  - start_hold: u32
  - data_setup_time: u32
  - stop_setup_time: u32
  - bus_free_time: u32
  - sda_pulse_min_limit: u32
  - addr: u8
  - count: u32
  - xfered: u32
  - buf: u8 *
  - result: int
  - stop: bool
  - adap: i2c_adapter
  - dev: device *
  - base: void __iomem *
  - complete: completion
  - irq: int
  - clk: clk *
  - mode: int
  - scl_min_width_us: u32
  - sda_min_width_us: u32
  - client: st_i2c_client
  - busy: bool

### st_i2c_timings
- Line: 142
- Members:
  - rate: u32
  - rep_start_hold: u32
  - rep_start_setup: u32
  - start_hold: u32
  - data_setup_time: u32
  - stop_setup_time: u32
  - bus_free_time: u32
  - sda_pulse_min_limit: u32
  - addr: u8
  - count: u32
  - xfered: u32
  - buf: u8 *
  - result: int
  - stop: bool
  - adap: i2c_adapter
  - dev: device *
  - base: void __iomem *
  - complete: completion
  - irq: int
  - clk: clk *
  - mode: int
  - scl_min_width_us: u32
  - sda_min_width_us: u32
  - client: st_i2c_client
  - busy: bool

## Enums (1)

### st_i2c_mode
- Line: 125

## Variables (5)

- static **i2c_timings** : st_i2c_timings[] (line 216)
- static **st_i2c_algo** : const struct i2c_algorithm (line 762)
- static **st_i2c_driver** : platform_driver (line 883)
- static **st_i2c_match** : const struct of_device_id[] (line 876)
- static **st_i2c_recovery_info** : i2c_bus_recovery_info (line 767)

## Macros (80)

- **SSC_BRG** (line 26)
- **SSC_BUS_FREE** (line 39)
- **SSC_CLR** (line 43)
- **SSC_CLR_NACK** (line 115)
- **SSC_CLR_REPSTRT** (line 116)
- **SSC_CLR_SSCAAS** (line 112)
- **SSC_CLR_SSCARBL** (line 114)
- **SSC_CLR_SSCSTOP** (line 113)
- **SSC_CTL** (line 29)
- **SSC_CTL_BM** (line 52)
- **SSC_CTL_DATA_WIDTH_9** (line 50)
- **SSC_CTL_DATA_WIDTH_MSK** (line 51)
- **SSC_CTL_EN** (line 58)
- **SSC_CTL_EN_CLST_RX** (line 62)
- **SSC_CTL_EN_RX_FIFO** (line 61)
- **SSC_CTL_EN_TX_FIFO** (line 60)
- **SSC_CTL_HB** (line 53)
- **SSC_CTL_LPB** (line 59)
- **SSC_CTL_MS** (line 57)
- **SSC_CTL_PH** (line 54)
- **SSC_CTL_PO** (line 55)
- **SSC_CTL_SR** (line 56)
- **SSC_DATA_SETUP** (line 37)
- **SSC_I2C** (line 32)
- **SSC_I2C_ACKG** (line 99)
- **SSC_I2C_AD10** (line 100)
- **SSC_I2C_I2CM** (line 96)
- **SSC_I2C_REPSTRTG** (line 102)
- **SSC_I2C_SLAVE_DISABLE** (line 103)
- **SSC_I2C_STOPG** (line 98)
- **SSC_I2C_STRTG** (line 97)
- **SSC_I2C_TXENB** (line 101)
- **SSC_IEN** (line 30)
- **SSC_IEN_AASEN** (line 70)
- **SSC_IEN_ARBLEN** (line 72)
- **SSC_IEN_NACKEN** (line 73)
- **SSC_IEN_PEEN** (line 69)
- **SSC_IEN_REEN** (line 68)
- **SSC_IEN_REPSTRTEN** (line 74)
- **SSC_IEN_RIEN** (line 65)
- **SSC_IEN_RX_FIFO_HALF_FULL** (line 76)
- **SSC_IEN_STOPEN** (line 71)
- **SSC_IEN_TEEN** (line 67)
- **SSC_IEN_TIEN** (line 66)
- **SSC_IEN_TX_FIFO_HALF** (line 75)
- **SSC_NOISE_SUPP_WIDTH** (line 44)
- **SSC_NOISE_SUPP_WIDTH_DATAOUT** (line 46)
- **SSC_PRE_SCALER_BRG** (line 42)
- **SSC_PRSCALER** (line 45)
- **SSC_PRSCALER_DATAOUT** (line 47)
- **SSC_PRSC_VALUE** (line 119)
- **SSC_RBUF** (line 28)
- **SSC_REP_START_HOLD** (line 34)
- **SSC_REP_START_SETUP** (line 36)
- **SSC_RXFIFO_SIZE** (line 123)
- **SSC_RX_FSTAT** (line 41)
- **SSC_RX_FSTAT_STATUS** (line 109)
- **SSC_SLAD** (line 33)
- **SSC_STA** (line 31)
- **SSC_START_HOLD** (line 35)
- **SSC_STA_AAS** (line 85)
- **SSC_STA_ARBL** (line 87)
- **SSC_STA_BUSY** (line 88)
- **SSC_STA_CLST** (line 84)
- **SSC_STA_NACK** (line 89)
- **SSC_STA_PE** (line 83)
- **SSC_STA_RE** (line 82)
- **SSC_STA_REPSTRT** (line 90)
- **SSC_STA_RIR** (line 79)
- **SSC_STA_RX_FIFO_HALF** (line 93)
- **SSC_STA_STOP** (line 86)
- **SSC_STA_TE** (line 81)
- **SSC_STA_TIR** (line 80)
- **SSC_STA_TX_FIFO_FULL** (line 92)
- **SSC_STA_TX_FIFO_HALF** (line 91)
- **SSC_STOP_SETUP** (line 38)
- **SSC_TBUF** (line 27)
- **SSC_TXFIFO_SIZE** (line 122)
- **SSC_TX_FSTAT** (line 40)
- **SSC_TX_FSTAT_STATUS** (line 106)
