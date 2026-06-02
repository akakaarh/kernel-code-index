# drivers/spi/spi-rzv2m-csi.c

Subsystem: drivers/spi

## Functions (25)

### rzv2m_csi_calc_current_transfer
- Return type: static void
- Signature: rzv2m_csi_calc_current_transfer(struct rzv2m_csi_priv * csi)
- Line: 214

### rzv2m_csi_clear_all_irqs
- Return type: static void
- Signature: rzv2m_csi_clear_all_irqs(struct rzv2m_csi_priv * csi)
- Line: 279

### rzv2m_csi_clear_irqs
- Return type: static void
- Signature: rzv2m_csi_clear_irqs(struct rzv2m_csi_priv * csi,u32 irqs)
- Line: 274

### rzv2m_csi_disable_all_irqs
- Return type: static void
- Signature: rzv2m_csi_disable_all_irqs(struct rzv2m_csi_priv * csi)
- Line: 267

### rzv2m_csi_disable_irqs
- Return type: static void
- Signature: rzv2m_csi_disable_irqs(const struct rzv2m_csi_priv * csi,u32 enable_bits)
- Line: 259

### rzv2m_csi_empty_rxfifo
- Return type: static void
- Signature: rzv2m_csi_empty_rxfifo(struct rzv2m_csi_priv * csi)
- Line: 206

### rzv2m_csi_enable_irqs
- Return type: static void
- Signature: rzv2m_csi_enable_irqs(struct rzv2m_csi_priv * csi,u32 enable_bits)
- Line: 286

### rzv2m_csi_enable_rx_trigger
- Return type: static void
- Signature: rzv2m_csi_enable_rx_trigger(struct rzv2m_csi_priv * csi,bool enable)
- Line: 253

### rzv2m_csi_fill_txfifo
- Return type: static int
- Signature: rzv2m_csi_fill_txfifo(struct rzv2m_csi_priv * csi)
- Line: 156

### rzv2m_csi_irq_handler
- Return type: static irqreturn_t
- Signature: rzv2m_csi_irq_handler(int irq,void * data)
- Line: 335

### rzv2m_csi_pio_transfer
- Return type: static int
- Signature: rzv2m_csi_pio_transfer(struct rzv2m_csi_priv * csi)
- Line: 444

### rzv2m_csi_probe
- Return type: static int
- Signature: rzv2m_csi_probe(struct platform_device * pdev)
- Line: 573

### rzv2m_csi_read_rxfifo
- Return type: static int
- Signature: rzv2m_csi_read_rxfifo(struct rzv2m_csi_priv * csi)
- Line: 181

### rzv2m_csi_reg_write_bit
- Return type: static void
- Signature: rzv2m_csi_reg_write_bit(const struct rzv2m_csi_priv * csi,int reg_offs,int bit_mask,u32 value)
- Line: 114

### rzv2m_csi_remove
- Return type: static void
- Signature: rzv2m_csi_remove(struct platform_device * pdev)
- Line: 667

### rzv2m_csi_set_rx_fifo_trigger_level
- Return type: static void
- Signature: rzv2m_csi_set_rx_fifo_trigger_level(struct rzv2m_csi_priv * csi)
- Line: 247

### rzv2m_csi_setup
- Return type: static int
- Signature: rzv2m_csi_setup(struct spi_device * spi)
- Line: 397

### rzv2m_csi_setup_clock
- Return type: static void
- Signature: rzv2m_csi_setup_clock(struct rzv2m_csi_priv * csi,u32 spi_hz)
- Line: 352

### rzv2m_csi_setup_operating_mode
- Return type: static void
- Signature: rzv2m_csi_setup_operating_mode(struct rzv2m_csi_priv * csi,struct spi_transfer * t)
- Line: 382

### rzv2m_csi_start_stop_operation
- Return type: static int
- Signature: rzv2m_csi_start_stop_operation(const struct rzv2m_csi_priv * csi,int enable,bool wait)
- Line: 141

### rzv2m_csi_sw_reset
- Return type: static int
- Signature: rzv2m_csi_sw_reset(struct rzv2m_csi_priv * csi,int assert)
- Line: 127

### rzv2m_csi_target_abort
- Return type: static int
- Signature: rzv2m_csi_target_abort(struct spi_controller * ctlr)
- Line: 563

### rzv2m_csi_transfer_one
- Return type: static int
- Signature: rzv2m_csi_transfer_one(struct spi_controller * controller,struct spi_device * spi,struct spi_transfer * transfer)
- Line: 531

### rzv2m_csi_wait_for_interrupt
- Return type: static int
- Signature: rzv2m_csi_wait_for_interrupt(struct rzv2m_csi_priv * csi,u32 wait_mask,u32 enable_bits)
- Line: 293

### rzv2m_csi_wait_for_rx_ready
- Return type: static int
- Signature: rzv2m_csi_wait_for_rx_ready(struct rzv2m_csi_priv * csi)
- Line: 320

## Structs (1)

### rzv2m_csi_priv
- Line: 93
- Members:
  - base: void __iomem *
  - csiclk: clk *
  - pclk: clk *
  - dev: device *
  - controller: spi_controller *
  - txbuf: const void *
  - rxbuf: void *
  - buffer_len: unsigned int
  - bytes_sent: unsigned int
  - bytes_received: unsigned int
  - bytes_to_transfer: unsigned int
  - words_to_transfer: unsigned int
  - bytes_per_word: unsigned int
  - wait: wait_queue_head_t
  - errors: u32
  - status: u32
  - target_aborted: bool
  - use_ss_pin: bool

## Variables (2)

- static **rzv2m_csi_drv** : platform_driver (line 682)
- static **rzv2m_csi_match** : const struct of_device_id[] (line 676)

## Macros (50)

- **CSI_CKS_MAX** (line 80)
- **CSI_CLKSEL** (line 23)
- **CSI_CLKSEL_CKP** (line 45)
- **CSI_CLKSEL_CKS** (line 49)
- **CSI_CLKSEL_DAP** (line 46)
- **CSI_CLKSEL_MODE** (line 47)
- **CSI_CLKSEL_SLAVE** (line 48)
- **CSI_CLKSEL_SS** (line 44)
- **CSI_CLKSEL_SS_DISABLED** (line 89)
- **CSI_CLKSEL_SS_ENA** (line 42)
- **CSI_CLKSEL_SS_ENABLED_ACTIVE_HIGH** (line 91)
- **CSI_CLKSEL_SS_ENABLED_ACTIVE_LOW** (line 90)
- **CSI_CLKSEL_SS_POL** (line 43)
- **CSI_CNT** (line 24)
- **CSI_CNT_CSIEND_E** (line 57)
- **CSI_CNT_CSIRST** (line 52)
- **CSI_CNT_OVERF_E** (line 55)
- **CSI_CNT_R_TRGEN** (line 53)
- **CSI_CNT_R_TRGR_E** (line 59)
- **CSI_CNT_TREND_E** (line 56)
- **CSI_CNT_T_TRGR_E** (line 58)
- **CSI_CNT_UNDER_E** (line 54)
- **CSI_EN_DIS_TIMEOUT_US** (line 74)
- **CSI_FIFOTRG** (line 30)
- **CSI_FIFOTRG_R_TRG** (line 70)
- **CSI_FIFO_HALF_SIZE** (line 73)
- **CSI_FIFO_SIZE_BYTES** (line 72)
- **CSI_IFIFO** (line 28)
- **CSI_IFIFOL** (line 26)
- **CSI_INT** (line 25)
- **CSI_INT_CSIEND** (line 65)
- **CSI_INT_OVERF** (line 63)
- **CSI_INT_R_TRGR** (line 67)
- **CSI_INT_TREND** (line 64)
- **CSI_INT_T_TRGR** (line 66)
- **CSI_INT_UNDER** (line 62)
- **CSI_MAX_SPI_SCKO** (line 87)
- **CSI_MODE** (line 22)
- **CSI_MODE_CCL** (line 35)
- **CSI_MODE_CSIE** (line 33)
- **CSI_MODE_CSOT** (line 37)
- **CSI_MODE_DIR** (line 36)
- **CSI_MODE_SETUP** (line 39)
- **CSI_MODE_TRMD** (line 34)
- **CSI_OFIFO** (line 29)
- **CSI_OFIFOL** (line 27)
- **OVERFLOW_ERROR** (line 83)
- **RX_TIMEOUT_ERROR** (line 85)
- **TX_TIMEOUT_ERROR** (line 84)
- **UNDERRUN_ERROR** (line 82)
