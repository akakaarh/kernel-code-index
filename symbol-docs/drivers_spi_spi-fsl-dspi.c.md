# drivers/spi/spi-fsl-dspi.c

Subsystem: drivers/spi

## Functions (49)

### dspi_16on32_dev_to_host
- Return type: static void
- Signature: dspi_16on32_dev_to_host(struct fsl_dspi * dspi,u32 rxdata)
- Line: 451

### dspi_16on32_host_to_dev
- Return type: static void
- Signature: dspi_16on32_host_to_dev(struct fsl_dspi * dspi,u32 * txdata)
- Line: 442

### dspi_8on16_dev_to_host
- Return type: static void
- Signature: dspi_8on16_dev_to_host(struct fsl_dspi * dspi,u32 rxdata)
- Line: 436

### dspi_8on16_host_to_dev
- Return type: static void
- Signature: dspi_8on16_host_to_dev(struct fsl_dspi * dspi,u32 * txdata)
- Line: 430

### dspi_8on32_dev_to_host
- Return type: static void
- Signature: dspi_8on32_dev_to_host(struct fsl_dspi * dspi,u32 rxdata)
- Line: 424

### dspi_8on32_host_to_dev
- Return type: static void
- Signature: dspi_8on32_host_to_dev(struct fsl_dspi * dspi,u32 * txdata)
- Line: 418

### dspi_assert_cs
- Return type: static void
- Signature: dspi_assert_cs(struct spi_device * spi,bool * cs)
- Line: 1134

### dspi_cleanup
- Return type: static void
- Signature: dspi_cleanup(struct spi_device * spi)
- Line: 1382

### dspi_deassert_cs
- Return type: static void
- Signature: dspi_deassert_cs(struct spi_device * spi,bool * cs)
- Line: 1143

### dspi_dma_max_datawords
- Return type: static size_t
- Signature: dspi_dma_max_datawords(struct fsl_dspi * dspi)
- Line: 509

### dspi_dma_transfer_size
- Return type: static size_t
- Signature: dspi_dma_transfer_size(struct fsl_dspi * dspi)
- Line: 527

### dspi_dma_xfer
- Return type: static void
- Signature: dspi_dma_xfer(struct fsl_dspi * dspi)
- Line: 643

### dspi_dma_xfer
- Return type: static void
- Signature: dspi_dma_xfer(struct fsl_dspi * dspi)
- Line: 788

### dspi_fifo_error
- Return type: static int
- Signature: dspi_fifo_error(struct fsl_dspi * dspi,u32 spi_sr)
- Line: 483

### dspi_fifo_read
- Return type: static void
- Signature: dspi_fifo_read(struct fsl_dspi * dspi)
- Line: 944

### dspi_fifo_write
- Return type: static void
- Signature: dspi_fifo_write(struct fsl_dspi * dspi)
- Line: 1014

### dspi_init
- Return type: static int
- Signature: dspi_init(struct fsl_dspi * dspi)
- Line: 1428

### dspi_interrupt
- Return type: static irqreturn_t
- Signature: dspi_interrupt(int irq,void * dev_id)
- Line: 1105

### dspi_native_dev_to_host
- Return type: static void
- Signature: dspi_native_dev_to_host(struct fsl_dspi * dspi,u32 rxdata)
- Line: 402

### dspi_native_host_to_dev
- Return type: static void
- Signature: dspi_native_host_to_dev(struct fsl_dspi * dspi,u32 * txdata)
- Line: 386

### dspi_next_xfer_dma_submit
- Return type: static int
- Signature: dspi_next_xfer_dma_submit(struct fsl_dspi * dspi)
- Line: 561

### dspi_poll
- Return type: static void
- Signature: dspi_poll(struct fsl_dspi * dspi)
- Line: 1079

### dspi_pop_tx
- Return type: static u32
- Signature: dspi_pop_tx(struct fsl_dspi * dspi)
- Line: 465

### dspi_pop_tx_pushr
- Return type: static u32
- Signature: dspi_pop_tx_pushr(struct fsl_dspi * dspi)
- Line: 497

### dspi_popr_read
- Return type: static u32
- Signature: dspi_popr_read(struct fsl_dspi * dspi)
- Line: 936

### dspi_probe
- Return type: static int
- Signature: dspi_probe(struct platform_device * pdev)
- Line: 1528

### dspi_push_rx
- Return type: static void
- Signature: dspi_push_rx(struct fsl_dspi * dspi,u32 rxdata)
- Line: 476

### dspi_pushr_cmd_write
- Return type: static void
- Signature: dspi_pushr_cmd_write(struct fsl_dspi * dspi,u16 cmd)
- Line: 877

### dspi_pushr_txdata_write
- Return type: static void
- Signature: dspi_pushr_txdata_write(struct fsl_dspi * dspi,u16 txdata)
- Line: 894

### dspi_release_dma
- Return type: static void
- Signature: dspi_release_dma(struct fsl_dspi * dspi)
- Line: 797

### dspi_release_dma
- Return type: static void
- Signature: dspi_release_dma(struct fsl_dspi * dspi)
- Line: 766

### dspi_remove
- Return type: static void
- Signature: dspi_remove(struct platform_device * pdev)
- Line: 1700

### dspi_request_dma
- Return type: static int
- Signature: dspi_request_dma(struct fsl_dspi * dspi,phys_addr_t phy_addr)
- Line: 670

### dspi_request_dma
- Return type: static int
- Signature: dspi_request_dma(struct fsl_dspi * dspi,phys_addr_t phy_addr)
- Line: 792

### dspi_resume
- Return type: static int
- Signature: dspi_resume(struct device * dev)
- Line: 1478

### dspi_rx_dma_callback
- Return type: static void
- Signature: dspi_rx_dma_callback(void * arg)
- Line: 543

### dspi_rxtx
- Return type: static bool
- Signature: dspi_rxtx(struct fsl_dspi * dspi)
- Line: 1066

### dspi_set_mtf
- Return type: static int
- Signature: dspi_set_mtf(struct fsl_dspi * dspi)
- Line: 1261

### dspi_setup
- Return type: static int
- Signature: dspi_setup(struct spi_device * spi)
- Line: 1275

### dspi_setup_accel
- Return type: static void
- Signature: dspi_setup_accel(struct fsl_dspi * dspi)
- Line: 953

### dspi_shutdown
- Return type: static void
- Signature: dspi_shutdown(struct platform_device * pdev)
- Line: 1720

### dspi_suspend
- Return type: static int
- Signature: dspi_suspend(struct device * dev)
- Line: 1464

### dspi_target_abort
- Return type: static int
- Signature: dspi_target_abort(struct spi_controller * host)
- Line: 1507

### dspi_transfer_one_message
- Return type: static int
- Signature: dspi_transfer_one_message(struct spi_controller * ctlr,struct spi_message * message)
- Line: 1152

### dspi_tx_dma_callback
- Return type: static void
- Signature: dspi_tx_dma_callback(void * arg)
- Line: 532

### dspi_xspi_fifo_write
- Return type: static void
- Signature: dspi_xspi_fifo_write(struct fsl_dspi * dspi,int num_words)
- Line: 899

### hz_to_spi_baud
- Return type: static void
- Signature: hz_to_spi_baud(char * pbr,char * br,int speed_hz,unsigned long clkrate,bool mtf_enabled)
- Line: 800

### is_s32g_dspi
- Return type: static bool
- Signature: is_s32g_dspi(struct fsl_dspi * data)
- Line: 380

### ns_delay_scale
- Return type: static void
- Signature: ns_delay_scale(char * psc,char * sc,int delay_ns,unsigned long clkrate)
- Line: 843

## Structs (4)

### chip_data
- Line: 118
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

### fsl_dspi
- Line: 338
- Members:
  - ctar_val: u32
  - trans_mode: dspi_trans_mode
  - max_clock_factor: u8
  - fifo_size: int
  - regmap: const struct regmap_config *
  - tx_dma_buf: u32 *
  - chan_tx: dma_chan *
  - tx_dma_phys: dma_addr_t
  - cmd_tx_complete: completion
  - tx_desc: dma_async_tx_descriptor *
  - rx_dma_buf: u32 *
  - chan_rx: dma_chan *
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
  - oper_word_size: int
  - oper_bits_per_word: int
  - words_in_flight: int
  - pushr_cmd: int
  - pushr_tx: int
  - host_to_dev: void (*)(struct fsl_dspi * dspi,u32 * txdata)
  - dev_to_host: void (*)(struct fsl_dspi * dspi,u32 rxdata)

### fsl_dspi_devtype_data
- Line: 127
- Members:
  - ctar_val: u32
  - trans_mode: dspi_trans_mode
  - max_clock_factor: u8
  - fifo_size: int
  - regmap: const struct regmap_config *
  - tx_dma_buf: u32 *
  - chan_tx: dma_chan *
  - tx_dma_phys: dma_addr_t
  - cmd_tx_complete: completion
  - tx_desc: dma_async_tx_descriptor *
  - rx_dma_buf: u32 *
  - chan_rx: dma_chan *
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
  - oper_word_size: int
  - oper_bits_per_word: int
  - words_in_flight: int
  - pushr_cmd: int
  - pushr_tx: int
  - host_to_dev: void (*)(struct fsl_dspi * dspi,u32 * txdata)
  - dev_to_host: void (*)(struct fsl_dspi * dspi,u32 rxdata)

### fsl_dspi_dma
- Line: 322
- Members:
  - ctar_val: u32
  - trans_mode: dspi_trans_mode
  - max_clock_factor: u8
  - fifo_size: int
  - regmap: const struct regmap_config *
  - tx_dma_buf: u32 *
  - chan_tx: dma_chan *
  - tx_dma_phys: dma_addr_t
  - cmd_tx_complete: completion
  - tx_desc: dma_async_tx_descriptor *
  - rx_dma_buf: u32 *
  - chan_rx: dma_chan *
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
  - oper_word_size: int
  - oper_bits_per_word: int
  - words_in_flight: int
  - pushr_cmd: int
  - pushr_tx: int
  - host_to_dev: void (*)(struct fsl_dspi * dspi,u32 * txdata)
  - dev_to_host: void (*)(struct fsl_dspi * dspi,u32 rxdata)

## Enums (3)

### __anonf73229c40103
- Line: 134

### __anonf73229c40203
- Line: 189

### dspi_trans_mode
- Line: 122

## Variables (10)

- static **devtype_data** : const struct fsl_dspi_devtype_data[] (line 243)
- static **dspi_access_table** : const struct regmap_access_table (line 167)
- static **dspi_regmap_config** : const struct regmap_config[] (line 197)
- static **dspi_volatile_ranges** : const struct regmap_range[] (line 177)
- static **dspi_volatile_table** : const struct regmap_access_table (line 184)
- static **dspi_yes_ranges** : const struct regmap_range[] (line 149)
- static **fsl_dspi_driver** : platform_driver (line 1725)
- static **fsl_dspi_dt_ids** : const struct of_device_id[] (line 1392)
- static **s32g_dspi_access_table** : const struct regmap_access_table (line 172)
- static **s32g_dspi_yes_ranges** : const struct regmap_range[] (line 158)

## Macros (74)

- **DMA_COMPLETION_TIMEOUT** (line 114)
- **DRIVER_NAME** (line 23)
- **SPI_25MHZ** (line 116)
- **SPI_CTAR**(x) (line 39)
- **SPI_CTAR0_SLAVE** (line 55)
- **SPI_CTARE**(x) (line 105)
- **SPI_CTARE_DTCP**(x) (line 107)
- **SPI_CTARE_FMSZE**(x) (line 106)
- **SPI_CTAR_ASC**(x) (line 50)
- **SPI_CTAR_BR**(x) (line 52)
- **SPI_CTAR_CPHA** (line 43)
- **SPI_CTAR_CPOL** (line 42)
- **SPI_CTAR_CSSCK**(x) (line 49)
- **SPI_CTAR_DBR** (line 41)
- **SPI_CTAR_DT**(x) (line 51)
- **SPI_CTAR_FMSZ**(x) (line 40)
- **SPI_CTAR_LSBFE** (line 44)
- **SPI_CTAR_PASC**(x) (line 46)
- **SPI_CTAR_PBR**(x) (line 48)
- **SPI_CTAR_PCSSCK**(x) (line 45)
- **SPI_CTAR_PDT**(x) (line 47)
- **SPI_CTAR_SCALE_BITS** (line 53)
- **SPI_FRAME_BITS**(bits) (line 111)
- **SPI_FRAME_EBITS**(bits) (line 112)
- **SPI_MCR** (line 25)
- **SPI_MCR_CLR_RXF** (line 30)
- **SPI_MCR_CLR_TXF** (line 29)
- **SPI_MCR_DIS_RXF** (line 33)
- **SPI_MCR_DIS_TXF** (line 32)
- **SPI_MCR_HALT** (line 34)
- **SPI_MCR_HOST** (line 26)
- **SPI_MCR_MTFE** (line 27)
- **SPI_MCR_PCSIS**(x) (line 28)
- **SPI_MCR_XSPI** (line 31)
- **SPI_POPR** (line 92)
- **SPI_PUSHR** (line 83)
- **SPI_PUSHR_CMD_CONT** (line 84)
- **SPI_PUSHR_CMD_CTAS**(x) (line 85)
- **SPI_PUSHR_CMD_CTCNT** (line 87)
- **SPI_PUSHR_CMD_EOQ** (line 86)
- **SPI_PUSHR_CMD_PCS**(x) (line 88)
- **SPI_PUSHR_SLAVE** (line 90)
- **SPI_RSER** (line 79)
- **SPI_RSER_CMDTCFE** (line 81)
- **SPI_RSER_RFDFD** (line 77)
- **SPI_RSER_RFDFE** (line 76)
- **SPI_RSER_TCFQE** (line 80)
- **SPI_RSER_TFFFD** (line 75)
- **SPI_RSER_TFFFE** (line 74)
- **SPI_RXFR0** (line 99)
- **SPI_RXFR1** (line 100)
- **SPI_RXFR2** (line 101)
- **SPI_RXFR3** (line 102)
- **SPI_RXFR4** (line 103)
- **SPI_SR** (line 57)
- **SPI_SREX** (line 109)
- **SPI_SR_CLEAR** (line 68)
- **SPI_SR_CMDFFF** (line 66)
- **SPI_SR_CMDTCF** (line 61)
- **SPI_SR_RFDF** (line 65)
- **SPI_SR_RFOF** (line 63)
- **SPI_SR_SPEF** (line 62)
- **SPI_SR_TCFQF** (line 58)
- **SPI_SR_TFFF** (line 60)
- **SPI_SR_TFIWF** (line 64)
- **SPI_SR_TFUF** (line 59)
- **SPI_SR_TXRXS** (line 67)
- **SPI_TCR** (line 36)
- **SPI_TCR_GET_TCNT**(x) (line 37)
- **SPI_TXFR0** (line 94)
- **SPI_TXFR1** (line 95)
- **SPI_TXFR2** (line 96)
- **SPI_TXFR3** (line 97)
- **SPI_TXFR4** (line 98)
