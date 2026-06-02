# drivers/spi/spi-pxa2xx.c

Subsystem: drivers/spi

## Functions (56)

### __lpss_ssp_read_priv
- Return type: static u32
- Signature: __lpss_ssp_read_priv(struct driver_data * drv_data,unsigned offset)
- Line: 312

### __lpss_ssp_update_priv
- Return type: static bool
- Signature: __lpss_ssp_update_priv(struct driver_data * drv_data,unsigned int offset,u32 mask,u32 value)
- Line: 325

### __lpss_ssp_write_priv
- Return type: static void
- Signature: __lpss_ssp_write_priv(struct driver_data * drv_data,unsigned offset,u32 value)
- Line: 318

### cleanup
- Return type: static void
- Signature: cleanup(struct spi_device * spi)
- Line: 1239

### cs_assert
- Return type: static void
- Signature: cs_assert(struct spi_device * spi)
- Line: 418

### cs_deassert
- Return type: static void
- Signature: cs_deassert(struct spi_device * spi)
- Line: 432

### handle_bad_msg
- Return type: static void
- Signature: handle_bad_msg(struct driver_data * drv_data)
- Line: 708

### int_error_stop
- Return type: static void
- Signature: int_error_stop(struct driver_data * drv_data,const char * msg,int err)
- Line: 611

### int_stop_and_reset
- Return type: static void
- Signature: int_stop_and_reset(struct driver_data * drv_data)
- Line: 600

### int_transfer_complete
- Return type: static void
- Signature: int_transfer_complete(struct driver_data * drv_data)
- Line: 623

### interrupt_transfer
- Return type: static irqreturn_t
- Signature: interrupt_transfer(struct driver_data * drv_data)
- Line: 630

### is_lpss_ssp
- Return type: static bool
- Signature: is_lpss_ssp(const struct driver_data * drv_data)
- Line: 177

### is_mmp2_ssp
- Return type: static bool
- Signature: is_mmp2_ssp(const struct driver_data * drv_data)
- Line: 197

### is_mrfld_ssp
- Return type: static bool
- Signature: is_mrfld_ssp(const struct driver_data * drv_data)
- Line: 202

### is_quark_x1000_ssp
- Return type: static bool
- Signature: is_quark_x1000_ssp(const struct driver_data * drv_data)
- Line: 192

### lpss_get_config
- Return type: static const struct lpss_config *
- Signature: lpss_get_config(const struct driver_data * drv_data)
- Line: 172

### lpss_ssp_cs_control
- Return type: static void
- Signature: lpss_ssp_cs_control(struct spi_device * spi,bool enable)
- Line: 389

### lpss_ssp_select_cs
- Return type: static void
- Signature: lpss_ssp_select_cs(struct spi_device * spi,const struct lpss_config * config)
- Line: 369

### lpss_ssp_setup
- Return type: static void
- Signature: lpss_ssp_setup(struct driver_data * drv_data)
- Line: 346

### null_reader
- Return type: static int
- Signature: null_reader(struct driver_data * drv_data)
- Line: 495

### null_writer
- Return type: static int
- Signature: null_writer(struct driver_data * drv_data)
- Line: 481

### pxa2xx_configure_sscr0
- Return type: static u32
- Signature: pxa2xx_configure_sscr0(const struct driver_data * drv_data,u32 clk_div,u8 bits)
- Line: 292

### pxa2xx_spi_can_dma
- Return type: static bool
- Signature: pxa2xx_spi_can_dma(struct spi_controller * controller,struct spi_device * spi,struct spi_transfer * xfer)
- Line: 922

### pxa2xx_spi_clear_rx_thre
- Return type: static void
- Signature: pxa2xx_spi_clear_rx_thre(const struct driver_data * drv_data,u32 * sccr1_reg)
- Line: 257

### pxa2xx_spi_flush
- Return type: int
- Signature: pxa2xx_spi_flush(struct driver_data * drv_data)
- Line: 459

### pxa2xx_spi_fw_translate_cs
- Return type: static int
- Signature: pxa2xx_spi_fw_translate_cs(struct spi_controller * controller,unsigned int cs)
- Line: 1246

### pxa2xx_spi_get_rx_default_thre
- Return type: static u32
- Signature: pxa2xx_spi_get_rx_default_thre(const struct driver_data * drv_data)
- Line: 226

### pxa2xx_spi_get_ssrc1_change_mask
- Return type: static u32
- Signature: pxa2xx_spi_get_ssrc1_change_mask(const struct driver_data * drv_data)
- Line: 213

### pxa2xx_spi_handle_err
- Return type: static void
- Signature: pxa2xx_spi_handle_err(struct spi_controller * controller,struct spi_message * msg)
- Line: 1098

### pxa2xx_spi_max_dma_transfer_size
- Return type: static size_t
- Signature: pxa2xx_spi_max_dma_transfer_size(struct spi_device * spi)
- Line: 1266

### pxa2xx_spi_off
- Return type: static void
- Signature: pxa2xx_spi_off(struct driver_data * drv_data)
- Line: 472

### pxa2xx_spi_probe
- Return type: int
- Signature: pxa2xx_spi_probe(struct device * dev,struct ssp_device * ssp,struct pxa2xx_spi_controller * platform_info)
- Line: 1271

### pxa2xx_spi_remove
- Return type: void
- Signature: pxa2xx_spi_remove(struct device * dev)
- Line: 1462

### pxa2xx_spi_resume
- Return type: static int
- Signature: pxa2xx_spi_resume(struct device * dev)
- Line: 1500

### pxa2xx_spi_runtime_resume
- Return type: static int
- Signature: pxa2xx_spi_runtime_resume(struct device * dev)
- Line: 1525

### pxa2xx_spi_runtime_suspend
- Return type: static int
- Signature: pxa2xx_spi_runtime_suspend(struct device * dev)
- Line: 1517

### pxa2xx_spi_set_cs
- Return type: static void
- Signature: pxa2xx_spi_set_cs(struct spi_device * spi,bool level)
- Line: 451

### pxa2xx_spi_set_rx_thre
- Return type: static void
- Signature: pxa2xx_spi_set_rx_thre(const struct driver_data * drv_data,u32 * sccr1_reg,u32 threshold)
- Line: 276

### pxa2xx_spi_suspend
- Return type: static int
- Signature: pxa2xx_spi_suspend(struct device * dev)
- Line: 1482

### pxa2xx_spi_target_abort
- Return type: static int
- Signature: pxa2xx_spi_target_abort(struct spi_controller * controller)
- Line: 1089

### pxa2xx_spi_transfer_one
- Return type: static int
- Signature: pxa2xx_spi_transfer_one(struct spi_controller * controller,struct spi_device * spi,struct spi_transfer * transfer)
- Line: 933

### pxa2xx_spi_txfifo_full
- Return type: static bool
- Signature: pxa2xx_spi_txfifo_full(const struct driver_data * drv_data)
- Line: 238

### pxa2xx_spi_unprepare_transfer
- Return type: static int
- Signature: pxa2xx_spi_unprepare_transfer(struct spi_controller * controller)
- Line: 1119

### pxa2xx_spi_update
- Return type: static void
- Signature: pxa2xx_spi_update(const struct driver_data * drv_data,u32 reg,u32 mask,u32 value)
- Line: 207

### pxa2xx_ssp_get_clk_div
- Return type: static unsigned int
- Signature: pxa2xx_ssp_get_clk_div(struct driver_data * drv_data,u32 rate)
- Line: 905

### quark_x1000_get_clk_div
- Return type: static unsigned int
- Signature: quark_x1000_get_clk_div(u32 rate,u32 * dds)
- Line: 799

### reset_sccr1
- Return type: static void
- Signature: reset_sccr1(struct driver_data * drv_data)
- Line: 573

### setup
- Return type: static int
- Signature: setup(struct spi_device * spi)
- Line: 1129

### ssp_get_clk_div
- Return type: static unsigned int
- Signature: ssp_get_clk_div(struct driver_data * drv_data,u32 rate)
- Line: 888

### ssp_int
- Return type: static irqreturn_t
- Signature: ssp_int(int irq,void * dev_id)
- Line: 716

### u16_reader
- Return type: static int
- Signature: u16_reader(struct driver_data * drv_data)
- Line: 541

### u16_writer
- Return type: static int
- Signature: u16_writer(struct driver_data * drv_data)
- Line: 529

### u32_reader
- Return type: static int
- Signature: u32_reader(struct driver_data * drv_data)
- Line: 563

### u32_writer
- Return type: static int
- Signature: u32_writer(struct driver_data * drv_data)
- Line: 551

### u8_reader
- Return type: static int
- Signature: u8_reader(struct driver_data * drv_data)
- Line: 519

### u8_writer
- Return type: static int
- Signature: u8_writer(struct driver_data * drv_data)
- Line: 507

## Structs (2)

### chip_data
- Line: 61
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

### lpss_config
- Line: 80
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

## Variables (1)

- static **lpss_platforms** : const struct lpss_config[] (line 100)

## Macros (13)

- **CE4100_SSCR1_CHANGE_MASK** (line 54)
- **LPSS_CAPS_CS_EN_MASK** (line 73)
- **LPSS_CAPS_CS_EN_SHIFT** (line 72)
- **LPSS_CS_CONTROL_CS_HIGH** (line 71)
- **LPSS_CS_CONTROL_SW_MODE** (line 70)
- **LPSS_GENERAL_REG_RXTO_HOLDOFF_DISABLE** (line 69)
- **LPSS_PRIV_CLOCK_GATE** (line 75)
- **LPSS_PRIV_CLOCK_GATE_CLK_CTL_FORCE_OFF** (line 78)
- **LPSS_PRIV_CLOCK_GATE_CLK_CTL_FORCE_ON** (line 77)
- **LPSS_PRIV_CLOCK_GATE_CLK_CTL_MASK** (line 76)
- **QUARK_X1000_SSCR1_CHANGE_MASK** (line 48)
- **SSCR1_CHANGE_MASK** (line 41)
- **TIMOUT_DFLT** (line 32)
