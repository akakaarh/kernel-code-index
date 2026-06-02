# drivers/spi/spi-atmel.c

Subsystem: drivers/spi

## Functions (44)

### atmel_get_caps
- Return type: static void
- Signature: atmel_get_caps(struct atmel_spi * as)
- Line: 1470

### atmel_get_version
- Return type: static unsigned int
- Signature: atmel_get_version(struct atmel_spi * as)
- Line: 1465

### atmel_spi_can_dma
- Return type: static bool
- Signature: atmel_spi_can_dma(struct spi_controller * host,struct spi_device * spi,struct spi_transfer * xfer)
- Line: 491

### atmel_spi_cleanup
- Return type: static void
- Signature: atmel_spi_cleanup(struct spi_device * spi)
- Line: 1454

### atmel_spi_configure_dma
- Return type: static int
- Signature: atmel_spi_configure_dma(struct spi_controller * host,struct atmel_spi * as)
- Line: 562

### atmel_spi_disable_pdc_transfer
- Return type: static void
- Signature: atmel_spi_disable_pdc_transfer(struct atmel_spi * as)
- Line: 1025

### atmel_spi_dma_map_xfer
- Return type: static int
- Signature: atmel_spi_dma_map_xfer(struct atmel_spi * as,struct spi_transfer * xfer)
- Line: 983

### atmel_spi_dma_slave_config
- Return type: static int
- Signature: atmel_spi_dma_slave_config(struct atmel_spi * as,u8 bits_per_word)
- Line: 505

### atmel_spi_dma_unmap_xfer
- Return type: static void
- Signature: atmel_spi_dma_unmap_xfer(struct spi_controller * host,struct spi_transfer * xfer)
- Line: 1014

### atmel_spi_init
- Return type: static void
- Signature: atmel_spi_init(struct atmel_spi * as)
- Line: 1482

### atmel_spi_is_v2
- Return type: static bool
- Signature: atmel_spi_is_v2(struct atmel_spi * as)
- Line: 318

### atmel_spi_is_vmalloc_xfer
- Return type: static bool
- Signature: atmel_spi_is_vmalloc_xfer(struct spi_transfer * xfer)
- Line: 480

### atmel_spi_lock
- Return type: static void
- Signature: atmel_spi_lock(struct atmel_spi * as)
- Line: 470

### atmel_spi_next_xfer_data
- Return type: static void
- Signature: atmel_spi_next_xfer_data(struct spi_controller * host,struct spi_transfer * xfer,dma_addr_t * tx_dma,dma_addr_t * rx_dma,u32 * plen)
- Line: 852

### atmel_spi_next_xfer_dma_submit
- Return type: static int
- Signature: atmel_spi_next_xfer_dma_submit(struct spi_controller * host,struct spi_transfer * xfer,u32 * plen)
- Line: 759

### atmel_spi_next_xfer_fifo
- Return type: static void
- Signature: atmel_spi_next_xfer_fifo(struct spi_controller * host,struct spi_transfer * xfer)
- Line: 675

### atmel_spi_next_xfer_pio
- Return type: static void
- Signature: atmel_spi_next_xfer_pio(struct spi_controller * host,struct spi_transfer * xfer)
- Line: 745

### atmel_spi_next_xfer_single
- Return type: static void
- Signature: atmel_spi_next_xfer_single(struct spi_controller * host,struct spi_transfer * xfer)
- Line: 643

### atmel_spi_one_transfer
- Return type: static int
- Signature: atmel_spi_one_transfer(struct spi_controller * host,struct spi_device * spi,struct spi_transfer * xfer)
- Line: 1339

### atmel_spi_pdc_interrupt
- Return type: static irqreturn_t
- Signature: atmel_spi_pdc_interrupt(int irq,void * dev_id)
- Line: 1165

### atmel_spi_pdc_next_xfer
- Return type: static void
- Signature: atmel_spi_pdc_next_xfer(struct spi_controller * host,struct spi_transfer * xfer)
- Line: 916

### atmel_spi_pio_interrupt
- Return type: static irqreturn_t
- Signature: atmel_spi_pio_interrupt(int irq,void * dev_id)
- Line: 1107

### atmel_spi_probe
- Return type: static int
- Signature: atmel_spi_probe(struct platform_device * pdev)
- Line: 1510

### atmel_spi_pump_fifo_data
- Return type: static void
- Signature: atmel_spi_pump_fifo_data(struct atmel_spi * as,struct spi_transfer * xfer)
- Line: 1055

### atmel_spi_pump_pio_data
- Return type: static void
- Signature: atmel_spi_pump_pio_data(struct atmel_spi * as,struct spi_transfer * xfer)
- Line: 1095

### atmel_spi_pump_single_data
- Return type: static void
- Signature: atmel_spi_pump_single_data(struct atmel_spi * as,struct spi_transfer * xfer)
- Line: 1031

### atmel_spi_release_dma
- Return type: static void
- Signature: atmel_spi_release_dma(struct spi_controller * host)
- Line: 614

### atmel_spi_remove
- Return type: static void
- Signature: atmel_spi_remove(struct platform_device * pdev)
- Line: 1686

### atmel_spi_resume
- Return type: static int
- Signature: atmel_spi_resume(struct device * dev)
- Line: 1776

### atmel_spi_runtime_resume
- Return type: static int
- Signature: atmel_spi_runtime_resume(struct device * dev)
- Line: 1740

### atmel_spi_runtime_suspend
- Return type: static int
- Signature: atmel_spi_runtime_suspend(struct device * dev)
- Line: 1727

### atmel_spi_send_dummy
- Return type: static void
- Signature: atmel_spi_send_dummy(struct atmel_spi * as,struct spi_device * spi,int chip_select)
- Line: 329

### atmel_spi_set_cs
- Return type: static void
- Signature: atmel_spi_set_cs(struct spi_device * spi,bool enable)
- Line: 1322

### atmel_spi_set_xfer_speed
- Return type: static int
- Signature: atmel_spi_set_xfer_speed(struct atmel_spi * as,struct spi_device * spi,struct spi_transfer * xfer)
- Line: 864

### atmel_spi_setup
- Return type: static int
- Signature: atmel_spi_setup(struct spi_device * spi)
- Line: 1247

### atmel_spi_stop_dma
- Return type: static void
- Signature: atmel_spi_stop_dma(struct spi_controller * host)
- Line: 606

### atmel_spi_suspend
- Return type: static int
- Signature: atmel_spi_suspend(struct device * dev)
- Line: 1760

### atmel_spi_unlock
- Return type: static void
- Signature: atmel_spi_unlock(struct atmel_spi * as)
- Line: 475

### atmel_spi_use_dma
- Return type: static bool
- Signature: atmel_spi_use_dma(struct atmel_spi * as,struct spi_transfer * xfer)
- Line: 485

### atmel_word_delay_csr
- Return type: static int
- Signature: atmel_word_delay_csr(struct spi_device * spi,struct atmel_spi * as)
- Line: 1201

### cs_activate
- Return type: static void
- Signature: cs_activate(struct atmel_spi * as,struct spi_device * spi)
- Line: 383

### cs_deactivate
- Return type: static void
- Signature: cs_deactivate(struct atmel_spi * as,struct spi_device * spi)
- Line: 445

### dma_callback
- Return type: static void
- Signature: dma_callback(void * data)
- Line: 627

### initialize_native_cs_for_gpio
- Return type: static void
- Signature: initialize_native_cs_for_gpio(struct atmel_spi * as)
- Line: 1219

## Structs (3)

### atmel_spi
- Line: 251
- Members:
  - is_spi2: bool
  - has_wdrbt: bool
  - has_dma_support: bool
  - has_pdc_support: bool
  - lock: spinlock_t
  - flags: unsigned long
  - phybase: phys_addr_t
  - regs: void __iomem *
  - irq: int
  - clk: clk *
  - gclk: clk *
  - pdev: platform_device *
  - spi_clk: unsigned long
  - current_transfer: spi_transfer *
  - current_remaining_bytes: int
  - done_status: int
  - dma_addr_rx_bbuf: dma_addr_t
  - dma_addr_tx_bbuf: dma_addr_t
  - addr_rx_bbuf: void *
  - addr_tx_bbuf: void *
  - xfer_completion: completion
  - caps: atmel_spi_caps
  - use_dma: bool
  - use_pdc: bool
  - keep_cs: bool
  - fifo_size: u32
  - last_polarity: bool
  - native_cs_free: u8
  - native_cs_for_gpio: u8
  - csr: u32

### atmel_spi_caps
- Line: 239
- Members:
  - is_spi2: bool
  - has_wdrbt: bool
  - has_dma_support: bool
  - has_pdc_support: bool
  - lock: spinlock_t
  - flags: unsigned long
  - phybase: phys_addr_t
  - regs: void __iomem *
  - irq: int
  - clk: clk *
  - gclk: clk *
  - pdev: platform_device *
  - spi_clk: unsigned long
  - current_transfer: spi_transfer *
  - current_remaining_bytes: int
  - done_status: int
  - dma_addr_rx_bbuf: dma_addr_t
  - dma_addr_tx_bbuf: dma_addr_t
  - addr_rx_bbuf: void *
  - addr_tx_bbuf: void *
  - xfer_completion: completion
  - caps: atmel_spi_caps
  - use_dma: bool
  - use_pdc: bool
  - keep_cs: bool
  - fifo_size: u32
  - last_polarity: bool
  - native_cs_free: u8
  - native_cs_for_gpio: u8
  - csr: u32

### atmel_spi_device
- Line: 287
- Members:
  - is_spi2: bool
  - has_wdrbt: bool
  - has_dma_support: bool
  - has_pdc_support: bool
  - lock: spinlock_t
  - flags: unsigned long
  - phybase: phys_addr_t
  - regs: void __iomem *
  - irq: int
  - clk: clk *
  - gclk: clk *
  - pdev: platform_device *
  - spi_clk: unsigned long
  - current_transfer: spi_transfer *
  - current_remaining_bytes: int
  - done_status: int
  - dma_addr_rx_bbuf: dma_addr_t
  - dma_addr_tx_bbuf: dma_addr_t
  - addr_rx_bbuf: void *
  - addr_tx_bbuf: void *
  - xfer_completion: completion
  - caps: atmel_spi_caps
  - use_dma: bool
  - use_pdc: bool
  - keep_cs: bool
  - fifo_size: u32
  - last_polarity: bool
  - native_cs_free: u8
  - native_cs_for_gpio: u8
  - csr: u32

## Variables (3)

- static **atmel_spi_driver** : platform_driver (line 1820)
- static **atmel_spi_dt_ids** : const struct of_device_id[] (line 1813)
- static **atmel_spi_pm_ops** : const struct dev_pm_ops (line 1807)

## Macros (168)

- **AUTOSUSPEND_TIMEOUT** (line 237)
- **DMA_MIN_BYTES** (line 235)
- **DUMMY_MSG** (line 308)
- **DUMMY_MSG_FREQUENCY** (line 302)
- **INVALID_DMA_ADDRESS** (line 292)
- **SPI_BF**(name,value) (line 216)
- **SPI_BFEXT**(name,value) (line 218)
- **SPI_BFINS**(name,value,old) (line 220)
- **SPI_BIT**(name) (line 214)
- **SPI_BITS_10_BPT** (line 202)
- **SPI_BITS_11_BPT** (line 203)
- **SPI_BITS_12_BPT** (line 204)
- **SPI_BITS_13_BPT** (line 205)
- **SPI_BITS_14_BPT** (line 206)
- **SPI_BITS_15_BPT** (line 207)
- **SPI_BITS_16_BPT** (line 208)
- **SPI_BITS_8_BPT** (line 200)
- **SPI_BITS_9_BPT** (line 201)
- **SPI_BITS_OFFSET** (line 148)
- **SPI_BITS_SIZE** (line 149)
- **SPI_CPOL_OFFSET** (line 142)
- **SPI_CPOL_SIZE** (line 143)
- **SPI_CR** (line 29)
- **SPI_CSAAT_OFFSET** (line 146)
- **SPI_CSAAT_SIZE** (line 147)
- **SPI_CSR0** (line 37)
- **SPI_CSR1** (line 38)
- **SPI_CSR2** (line 39)
- **SPI_CSR3** (line 40)
- **SPI_DLYBCS_OFFSET** (line 90)
- **SPI_DLYBCS_SIZE** (line 91)
- **SPI_DLYBCT_OFFSET** (line 154)
- **SPI_DLYBCT_SIZE** (line 155)
- **SPI_DLYBS_OFFSET** (line 152)
- **SPI_DLYBS_SIZE** (line 153)
- **SPI_ENDRX_OFFSET** (line 110)
- **SPI_ENDRX_SIZE** (line 111)
- **SPI_ENDTX_OFFSET** (line 112)
- **SPI_ENDTX_SIZE** (line 113)
- **SPI_FDIV_OFFSET** (line 80)
- **SPI_FDIV_SIZE** (line 81)
- **SPI_FIFODIS_OFFSET** (line 70)
- **SPI_FIFODIS_SIZE** (line 71)
- **SPI_FIFOEN_OFFSET** (line 68)
- **SPI_FIFOEN_SIZE** (line 69)
- **SPI_FLR** (line 42)
- **SPI_FMR** (line 41)
- **SPI_FOUR_DATA** (line 211)
- **SPI_IDR** (line 35)
- **SPI_IER** (line 34)
- **SPI_IMR** (line 36)
- **SPI_LASTXFER_OFFSET** (line 62)
- **SPI_LASTXFER_SIZE** (line 63)
- **SPI_LLB_OFFSET** (line 86)
- **SPI_LLB_SIZE** (line 87)
- **SPI_MAX_DMA_XFER** (line 291)
- **SPI_MODFDIS_OFFSET** (line 82)
- **SPI_MODFDIS_SIZE** (line 83)
- **SPI_MODF_OFFSET** (line 106)
- **SPI_MODF_SIZE** (line 107)
- **SPI_MR** (line 30)
- **SPI_MSTR_OFFSET** (line 74)
- **SPI_MSTR_SIZE** (line 75)
- **SPI_NCPHA_OFFSET** (line 144)
- **SPI_NCPHA_SIZE** (line 145)
- **SPI_NSSR_OFFSET** (line 118)
- **SPI_NSSR_SIZE** (line 119)
- **SPI_ONE_DATA** (line 209)
- **SPI_OVRES_OFFSET** (line 108)
- **SPI_OVRES_SIZE** (line 109)
- **SPI_PCSDEC_OFFSET** (line 78)
- **SPI_PCSDEC_SIZE** (line 79)
- **SPI_PCS_OFFSET** (line 88)
- **SPI_PCS_SIZE** (line 89)
- **SPI_PS_OFFSET** (line 76)
- **SPI_PS_SIZE** (line 77)
- **SPI_PTCR** (line 52)
- **SPI_PTSR** (line 53)
- **SPI_RCR** (line 45)
- **SPI_RDR** (line 31)
- **SPI_RDRF_OFFSET** (line 102)
- **SPI_RDRF_SIZE** (line 103)
- **SPI_RD_OFFSET** (line 94)
- **SPI_RD_SIZE** (line 95)
- **SPI_RNCR** (line 49)
- **SPI_RNPR** (line 48)
- **SPI_RPR** (line 44)
- **SPI_RXBUFF_OFFSET** (line 114)
- **SPI_RXBUFF_SIZE** (line 115)
- **SPI_RXCTR_OFFSET** (line 158)
- **SPI_RXCTR_SIZE** (line 159)
- **SPI_RXFCLR_OFFSET** (line 66)
- **SPI_RXFCLR_SIZE** (line 67)
- **SPI_RXFEF_OFFSET** (line 130)
- **SPI_RXFEF_SIZE** (line 131)
- **SPI_RXFFF_OFFSET** (line 132)
- **SPI_RXFFF_SIZE** (line 133)
- **SPI_RXFL_OFFSET** (line 196)
- **SPI_RXFL_SIZE** (line 197)
- **SPI_RXFPTEF_OFFSET** (line 138)
- **SPI_RXFPTEF_SIZE** (line 139)
- **SPI_RXFTHF_OFFSET** (line 134)
- **SPI_RXFTHF_SIZE** (line 135)
- **SPI_RXFTHRES_OFFSET** (line 190)
- **SPI_RXFTHRES_SIZE** (line 191)
- **SPI_RXNCR_OFFSET** (line 166)
- **SPI_RXNCR_SIZE** (line 167)
- **SPI_RXRDYM_OFFSET** (line 186)
- **SPI_RXRDYM_SIZE** (line 187)
- **SPI_RXTDIS_OFFSET** (line 176)
- **SPI_RXTDIS_SIZE** (line 177)
- **SPI_RXTEN_OFFSET** (line 174)
- **SPI_RXTEN_SIZE** (line 175)
- **SPI_SCBR_OFFSET** (line 150)
- **SPI_SCBR_SIZE** (line 151)
- **SPI_SPIDIS_OFFSET** (line 58)
- **SPI_SPIDIS_SIZE** (line 59)
- **SPI_SPIENS_OFFSET** (line 122)
- **SPI_SPIENS_SIZE** (line 123)
- **SPI_SPIEN_OFFSET** (line 56)
- **SPI_SPIEN_SIZE** (line 57)
- **SPI_SR** (line 33)
- **SPI_SWRST_OFFSET** (line 60)
- **SPI_SWRST_SIZE** (line 61)
- **SPI_TCR** (line 47)
- **SPI_TDR** (line 32)
- **SPI_TDRE_OFFSET** (line 104)
- **SPI_TDRE_SIZE** (line 105)
- **SPI_TD_OFFSET** (line 98)
- **SPI_TD_SIZE** (line 99)
- **SPI_TNCR** (line 51)
- **SPI_TNPR** (line 50)
- **SPI_TPR** (line 46)
- **SPI_TWO_DATA** (line 210)
- **SPI_TXBUFE_OFFSET** (line 116)
- **SPI_TXBUFE_SIZE** (line 117)
- **SPI_TXCTR_OFFSET** (line 162)
- **SPI_TXCTR_SIZE** (line 163)
- **SPI_TXEMPTY_OFFSET** (line 120)
- **SPI_TXEMPTY_SIZE** (line 121)
- **SPI_TXFCLR_OFFSET** (line 64)
- **SPI_TXFCLR_SIZE** (line 65)
- **SPI_TXFEF_OFFSET** (line 124)
- **SPI_TXFEF_SIZE** (line 125)
- **SPI_TXFFF_OFFSET** (line 126)
- **SPI_TXFFF_SIZE** (line 127)
- **SPI_TXFL_OFFSET** (line 194)
- **SPI_TXFL_SIZE** (line 195)
- **SPI_TXFPTEF_OFFSET** (line 136)
- **SPI_TXFPTEF_SIZE** (line 137)
- **SPI_TXFTHF_OFFSET** (line 128)
- **SPI_TXFTHF_SIZE** (line 129)
- **SPI_TXFTHRES_OFFSET** (line 188)
- **SPI_TXFTHRES_SIZE** (line 189)
- **SPI_TXNCR_OFFSET** (line 170)
- **SPI_TXNCR_SIZE** (line 171)
- **SPI_TXRDYM_OFFSET** (line 184)
- **SPI_TXRDYM_SIZE** (line 185)
- **SPI_TXTDIS_OFFSET** (line 180)
- **SPI_TXTDIS_SIZE** (line 181)
- **SPI_TXTEN_OFFSET** (line 178)
- **SPI_TXTEN_SIZE** (line 179)
- **SPI_VERSION** (line 43)
- **SPI_WDRBT_OFFSET** (line 84)
- **SPI_WDRBT_SIZE** (line 85)
- **spi_readl**(port,reg) (line 225)
- **spi_writel**(port,reg,value) (line 227)
- **spi_writew**(port,reg,value) (line 229)
