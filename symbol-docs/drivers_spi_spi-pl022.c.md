# drivers/spi/spi-pl022.c

Subsystem: drivers/spi

## Functions (41)

### calculate_effective_freq
- Return type: static int
- Signature: calculate_effective_freq(struct pl022 * pl022,int freq,struct ssp_clock_params * clk_freq)
- Line: 1486

### configure_dma
- Return type: static int
- Signature: configure_dma(struct pl022 * pl022)
- Line: 1099

### configure_dma
- Return type: static int
- Signature: configure_dma(struct pl022 * pl022)
- Line: 795

### dma_callback
- Return type: static void
- Signature: dma_callback(void * data)
- Line: 695

### do_interrupt_dma_transfer
- Return type: static int
- Signature: do_interrupt_dma_transfer(struct pl022 * pl022)
- Line: 1237

### do_polling_transfer
- Return type: static int
- Signature: do_polling_transfer(struct pl022 * pl022)
- Line: 1294

### flush
- Return type: static int
- Signature: flush(struct pl022 * pl022)
- Line: 452

### internal_cs_control
- Return type: static void
- Signature: internal_cs_control(struct pl022 * pl022,bool enable)
- Line: 429

### load_ssp_default_config
- Return type: static void
- Signature: load_ssp_default_config(struct pl022 * pl022)
- Line: 561

### pl022_cleanup
- Return type: static void
- Signature: pl022_cleanup(struct spi_device * spi)
- Line: 1820

### pl022_cs_control
- Return type: static void
- Signature: pl022_cs_control(struct spi_device * spi,bool enable)
- Line: 441

### pl022_dma_autoprobe
- Return type: static int
- Signature: pl022_dma_autoprobe(struct pl022 * pl022)
- Line: 1104

### pl022_dma_autoprobe
- Return type: static int
- Signature: pl022_dma_autoprobe(struct pl022 * pl022)
- Line: 1033

### pl022_dma_probe
- Return type: static int
- Signature: pl022_dma_probe(struct pl022 * pl022)
- Line: 1109

### pl022_dma_probe
- Return type: static int
- Signature: pl022_dma_probe(struct pl022 * pl022)
- Line: 985

### pl022_dma_remove
- Return type: static void
- Signature: pl022_dma_remove(struct pl022 * pl022)
- Line: 1118

### pl022_dma_remove
- Return type: static void
- Signature: pl022_dma_remove(struct pl022 * pl022)
- Line: 1088

### pl022_exit
- Return type: static void __exit
- Signature: pl022_exit(void)
- Line: 2187

### pl022_handle_err
- Return type: static void
- Signature: pl022_handle_err(struct spi_controller * ctlr,struct spi_message * message)
- Line: 1346

### pl022_init
- Return type: static int __init
- Signature: pl022_init(void)
- Line: 2181

### pl022_interrupt_handler
- Return type: static irqreturn_t
- Signature: pl022_interrupt_handler(int irq,void * dev_id)
- Line: 1136

### pl022_platform_data_dt_get
- Return type: static pl022_ssp_controller *
- Signature: pl022_platform_data_dt_get(struct device * dev)
- Line: 1829

### pl022_probe
- Return type: static int
- Signature: pl022_probe(struct amba_device * adev,const struct amba_id * id)
- Line: 1851

### pl022_remove
- Return type: static void
- Signature: pl022_remove(struct amba_device * adev)
- Line: 1993

### pl022_resume
- Return type: static int
- Signature: pl022_resume(struct device * dev)
- Line: 2041

### pl022_runtime_resume
- Return type: static int
- Signature: pl022_runtime_resume(struct device * dev)
- Line: 2070

### pl022_runtime_suspend
- Return type: static int
- Signature: pl022_runtime_suspend(struct device * dev)
- Line: 2060

### pl022_setup
- Return type: static int
- Signature: pl022_setup(struct spi_device * spi)
- Line: 1590

### pl022_suspend
- Return type: static int
- Signature: pl022_suspend(struct device * dev)
- Line: 2020

### pl022_transfer_one
- Return type: static int
- Signature: pl022_transfer_one(struct spi_controller * host,struct spi_device * spi,struct spi_transfer * transfer)
- Line: 1326

### pl022_unprepare_transfer_hardware
- Return type: static int
- Signature: pl022_unprepare_transfer_hardware(struct spi_controller * host)
- Line: 1355

### print_current_status
- Return type: static void
- Signature: print_current_status(struct pl022 * pl022)
- Line: 1270

### readwriter
- Return type: static void
- Signature: readwriter(struct pl022 * pl022)
- Line: 583

### restore_state
- Return type: static void
- Signature: restore_state(struct pl022 * pl022)
- Line: 471

### set_up_next_transfer
- Return type: static int
- Signature: set_up_next_transfer(struct pl022 * pl022,struct spi_transfer * transfer)
- Line: 1211

### setup_dma_scatter
- Return type: static void
- Signature: setup_dma_scatter(struct pl022 * pl022,void * buffer,unsigned int length,struct sg_table * sgtab)
- Line: 745

### spi_rate
- Return type: static u32
- Signature: spi_rate(u32 rate,u16 cpsdvsr,u16 scr)
- Line: 1481

### terminate_dma
- Return type: static void
- Signature: terminate_dma(struct pl022 * pl022)
- Line: 1114

### terminate_dma
- Return type: static void
- Signature: terminate_dma(struct pl022 * pl022)
- Line: 1074

### unmap_free_dma_scatter
- Return type: static void
- Signature: unmap_free_dma_scatter(struct pl022 * pl022)
- Line: 684

### verify_controller_parameters
- Return type: static int
- Signature: verify_controller_parameters(struct pl022 * pl022,struct pl022_config_chip const * chip_info)
- Line: 1366

## Structs (3)

### chip_data
- Line: 408
- Members:
  - cr1: u32
  - dds_rate: u32
  - threshold: u32
  - lpss_rx_threshold: u16
  - lpss_tx_threshold: u16
  - offset: unsigned
  - reg_general: int
  - reg_ssp: int
  - reg_cs_ctrl: int
  - reg_capabilities: int
  - rx_threshold: u32
  - tx_threshold_lo: u32
  - tx_threshold_hi: u32
  - cs_sel_shift: unsigned
  - cs_sel_mask: unsigned
  - cs_clk_stays_gated: unsigned:1
  - ctar_val: u32
  - trans_mode: dspi_trans_mode
  - max_clock_factor: u8
  - fifo_size: int
  - regmap: const struct regmap_config *
  - tx_dma_buf: u32 *
  - chan_tx: dma_chan *
  - fifodepth: int
  - max_bpw: int
  - tx_dma_phys: dma_addr_t
  - cmd_tx_complete: completion
  - unidir: bool
  - extended_cr: bool
  - tx_desc: dma_async_tx_descriptor *
  - pl023: bool
  - loopback: bool
  - rx_dma_buf: u32 *
  - chan_rx: dma_chan *
  - internal_cs_ctrl: bool
  - rx_dma_phys: dma_addr_t
  - cmd_rx_complete: completion
  - rx_desc: dma_async_tx_descriptor *
  - bufsize: size_t
  - ctlr: spi_controller *
  - pdev: platform_device *
  - regmap: regmap *
  - regmap_pushr: regmap *
  - irq: int
  - clk: clk *
  - cur_transfer: spi_transfer *
  - cur_msg: spi_message *
  - cur_chip: chip_data *
  - progress: size_t
  - len: size_t
  - tx: const void *
  - rx: void *
  - tx_cmd: u16
  - mtf_enabled: bool
  - devtype_data: const struct fsl_dspi_devtype_data *
  - xfer_done: completion
  - dma: fsl_dspi_dma *
  - adev: amba_device *
  - oper_word_size: int
  - oper_bits_per_word: int
  - vendor: vendor_data *
  - phybase: resource_size_t
  - virtbase: void __iomem *
  - words_in_flight: int
  - clk: clk *
  - host: spi_controller *
  - host_info: pl022_ssp_controller *
  - cur_transfer: spi_transfer *
  - cur_chip: chip_data *
  - pushr_cmd: int
  - tx: void *
  - pushr_tx: int
  - tx_end: void *
  - rx: void *
  - host_to_dev: void (*)(struct fsl_dspi * dspi,u32 * txdata)
  - rx_end: void *
  - dev_to_host: void (*)(struct fsl_dspi * dspi,u32 rxdata)
  - read: ssp_reading
  - write: ssp_writing
  - exp_fifo_level: u32
  - rx_lev_trig: ssp_rx_level_trig
  - tx_lev_trig: ssp_tx_level_trig
  - dma_rx_channel: dma_chan *
  - dma_tx_channel: dma_chan *
  - sgt_rx: sg_table
  - sgt_tx: sg_table
  - dummypage: char *
  - dma_running: bool
  - cur_cs: int
  - cr0: u32
  - cr1: u16
  - dmacr: u16
  - cpsr: u16
  - n_bytes: u8
  - enable_dma: bool
  - read: ssp_reading
  - write: ssp_writing
  - xfer_type: int

### pl022
- Line: 361
- Members:
  - fifodepth: int
  - max_bpw: int
  - unidir: bool
  - extended_cr: bool
  - pl023: bool
  - loopback: bool
  - internal_cs_ctrl: bool
  - adev: amba_device *
  - vendor: vendor_data *
  - phybase: resource_size_t
  - virtbase: void __iomem *
  - clk: clk *
  - host: spi_controller *
  - host_info: pl022_ssp_controller *
  - cur_transfer: spi_transfer *
  - cur_chip: chip_data *
  - tx: void *
  - tx_end: void *
  - rx: void *
  - rx_end: void *
  - read: ssp_reading
  - write: ssp_writing
  - exp_fifo_level: u32
  - rx_lev_trig: ssp_rx_level_trig
  - tx_lev_trig: ssp_tx_level_trig
  - dma_rx_channel: dma_chan *
  - dma_tx_channel: dma_chan *
  - sgt_rx: sg_table
  - sgt_tx: sg_table
  - dummypage: char *
  - dma_running: bool
  - cur_cs: int
  - cr0: u32
  - cr1: u16
  - dmacr: u16
  - cpsr: u16
  - n_bytes: u8
  - enable_dma: bool
  - read: ssp_reading
  - write: ssp_writing
  - xfer_type: int

### vendor_data
- Line: 323
- Members:
  - fifodepth: int
  - max_bpw: int
  - unidir: bool
  - extended_cr: bool
  - pl023: bool
  - loopback: bool
  - internal_cs_ctrl: bool
  - adev: amba_device *
  - vendor: vendor_data *
  - phybase: resource_size_t
  - virtbase: void __iomem *
  - clk: clk *
  - host: spi_controller *
  - host_info: pl022_ssp_controller *
  - cur_transfer: spi_transfer *
  - cur_chip: chip_data *
  - tx: void *
  - tx_end: void *
  - rx: void *
  - rx_end: void *
  - read: ssp_reading
  - write: ssp_writing
  - exp_fifo_level: u32
  - rx_lev_trig: ssp_rx_level_trig
  - tx_lev_trig: ssp_tx_level_trig
  - dma_rx_channel: dma_chan *
  - dma_tx_channel: dma_chan *
  - sgt_rx: sg_table
  - sgt_tx: sg_table
  - dummypage: char *
  - dma_running: bool
  - cur_cs: int
  - cr0: u32
  - cr1: u16
  - dmacr: u16
  - cpsr: u16
  - n_bytes: u8
  - enable_dma: bool
  - read: ssp_reading
  - write: ssp_writing
  - xfer_type: int

## Enums (2)

### ssp_reading
- Line: 294

### ssp_writing
- Line: 304

## Variables (8)

- static **pl022_default_chip_info** : const struct pl022_config_chip (line 1566)
- static **pl022_dev_pm_ops** : const struct dev_pm_ops (line 2081)
- static **pl022_driver** : amba_driver (line 2171)
- static **pl022_ids** : const struct amba_id[] (line 2126)
- static **vendor_arm** : vendor_data (line 2086)
- static **vendor_lsi** : vendor_data (line 2116)
- static **vendor_st** : vendor_data (line 2096)
- static **vendor_st_pl023** : vendor_data (line 2106)

## Macros (124)

- **CLEAR_ALL_INTERRUPTS** (line 287)
- **CPSDVR_MAX** (line 271)
- **CPSDVR_MIN** (line 270)
- **DEFAULT_SSP_REG_CPSR** (line 548)
- **DEFAULT_SSP_REG_CR0** (line 489)
- **DEFAULT_SSP_REG_CR0_ST** (line 498)
- **DEFAULT_SSP_REG_CR0_ST_PL023** (line 509)
- **DEFAULT_SSP_REG_CR1** (line 516)
- **DEFAULT_SSP_REG_CR1_ST** (line 524)
- **DEFAULT_SSP_REG_CR1_ST_PL023** (line 537)
- **DEFAULT_SSP_REG_DMACR** (line 552)
- **DEFAULT_SSP_REG_IMSC** (line 278)
- **DISABLE_ALL_INTERRUPTS** (line 279)
- **DO_NOT_DRIVE_TX** (line 55)
- **DO_NOT_QUEUE_DMA** (line 57)
- **DRIVE_TX** (line 54)
- **ENABLE_ALL_INTERRUPTS** (line 280)
- **GEN_MASK_BITS**(val,mask,sb) (line 51)
- **ITIP_MASK_RXDMAC** (line 210)
- **ITIP_MASK_SSPCLKIN** (line 209)
- **ITIP_MASK_SSPFSSIN** (line 208)
- **ITIP_MASK_SSPRXD** (line 207)
- **ITIP_MASK_SSPTXDIN** (line 212)
- **ITIP_MASK_TXDMAC** (line 211)
- **ITOP_MASK_INTR** (line 226)
- **ITOP_MASK_RORINTR** (line 222)
- **ITOP_MASK_RTINTR** (line 223)
- **ITOP_MASK_RXDMABREQ** (line 227)
- **ITOP_MASK_RXDMASREQ** (line 228)
- **ITOP_MASK_RXINTR** (line 224)
- **ITOP_MASK_SSPCLKOUT** (line 219)
- **ITOP_MASK_SSPCTLOEn** (line 221)
- **ITOP_MASK_SSPFSSOUT** (line 218)
- **ITOP_MASK_SSPOEn** (line 220)
- **ITOP_MASK_SSPTXD** (line 217)
- **ITOP_MASK_TXDMABREQ** (line 229)
- **ITOP_MASK_TXDMASREQ** (line 230)
- **ITOP_MASK_TXINTR** (line 225)
- **QUEUE_DMA** (line 58)
- **RX_TRANSFER** (line 60)
- **SCR_MAX** (line 273)
- **SCR_MIN** (line 272)
- **SPI_POLLING_TIMEOUT** (line 289)
- **SSP_CID0**(r) (line 87)
- **SSP_CID1**(r) (line 88)
- **SSP_CID2**(r) (line 89)
- **SSP_CID3**(r) (line 90)
- **SSP_CPSR**(r) (line 70)
- **SSP_CPSR_MASK_CPSDVSR** (line 142)
- **SSP_CR0**(r) (line 66)
- **SSP_CR0_MASK_CSS_ST** (line 107)
- **SSP_CR0_MASK_DSS** (line 95)
- **SSP_CR0_MASK_DSS_ST** (line 105)
- **SSP_CR0_MASK_FRF** (line 96)
- **SSP_CR0_MASK_FRF_ST** (line 108)
- **SSP_CR0_MASK_HALFDUP_ST** (line 106)
- **SSP_CR0_MASK_SCR** (line 99)
- **SSP_CR0_MASK_SPH** (line 98)
- **SSP_CR0_MASK_SPO** (line 97)
- **SSP_CR1**(r) (line 67)
- **SSP_CR1_MASK_FBCLKDEL_ST** (line 128)
- **SSP_CR1_MASK_LBM** (line 113)
- **SSP_CR1_MASK_MS** (line 115)
- **SSP_CR1_MASK_MWAIT_ST** (line 124)
- **SSP_CR1_MASK_RENDN_ST** (line 122)
- **SSP_CR1_MASK_RXIFLSEL_ST** (line 125)
- **SSP_CR1_MASK_SOD** (line 116)
- **SSP_CR1_MASK_SSE** (line 114)
- **SSP_CR1_MASK_TENDN_ST** (line 123)
- **SSP_CR1_MASK_TXIFLSEL_ST** (line 126)
- **SSP_CSR**(r) (line 76)
- **SSP_CSR_CSVALUE_MASK** (line 196)
- **SSP_DEFAULT_CLKRATE** (line 264)
- **SSP_DEFAULT_PRESCALE** (line 265)
- **SSP_DISABLED** (line 252)
- **SSP_DMACR**(r) (line 75)
- **SSP_DMACR_MASK_RXDMAE** (line 188)
- **SSP_DMACR_MASK_TXDMAE** (line 190)
- **SSP_DMA_DISABLED** (line 258)
- **SSP_DMA_ENABLED** (line 259)
- **SSP_DR**(r) (line 68)
- **SSP_ENABLED** (line 253)
- **SSP_ICR**(r) (line 74)
- **SSP_ICR_MASK_RORIC** (line 180)
- **SSP_ICR_MASK_RTIC** (line 182)
- **SSP_IMSC**(r) (line 71)
- **SSP_IMSC_MASK_RORIM** (line 147)
- **SSP_IMSC_MASK_RTIM** (line 148)
- **SSP_IMSC_MASK_RXIM** (line 149)
- **SSP_IMSC_MASK_TXIM** (line 150)
- **SSP_ITCR**(r) (line 77)
- **SSP_ITCR_MASK_ITEN** (line 201)
- **SSP_ITCR_MASK_TESTFIFO** (line 202)
- **SSP_ITIP**(r) (line 78)
- **SSP_ITOP**(r) (line 79)
- **SSP_MIS**(r) (line 73)
- **SSP_MIS_MASK_RORMIS** (line 168)
- **SSP_MIS_MASK_RTMIS** (line 170)
- **SSP_MIS_MASK_RXMIS** (line 172)
- **SSP_MIS_MASK_TXMIS** (line 174)
- **SSP_PID0**(r) (line 82)
- **SSP_PID1**(r) (line 83)
- **SSP_PID2**(r) (line 84)
- **SSP_PID3**(r) (line 85)
- **SSP_RIS**(r) (line 72)
- **SSP_RIS_MASK_RORRIS** (line 156)
- **SSP_RIS_MASK_RTRIS** (line 158)
- **SSP_RIS_MASK_RXRIS** (line 160)
- **SSP_RIS_MASK_TXRIS** (line 162)
- **SSP_SR**(r) (line 69)
- **SSP_SR_MASK_BSY** (line 137)
- **SSP_SR_MASK_RFF** (line 136)
- **SSP_SR_MASK_RNE** (line 135)
- **SSP_SR_MASK_TFE** (line 133)
- **SSP_SR_MASK_TNF** (line 134)
- **SSP_TDR**(r) (line 80)
- **SSP_WRITE_BITS**(reg,val,mask,sb) (line 43)
- **STATE_DONE** (line 245)
- **STATE_ERROR** (line 246)
- **STATE_RUNNING** (line 244)
- **STATE_START** (line 243)
- **STATE_TIMEOUT** (line 247)
- **TDR_MASK_TESTDATA** (line 235)
- **TX_TRANSFER** (line 61)
