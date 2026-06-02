# drivers/spi/spi-omap2-mcspi.c

Subsystem: drivers/spi

## Functions (39)

### mcspi_bytes_per_word
- Return type: static int
- Signature: mcspi_bytes_per_word(int word_len)
- Line: 196

### mcspi_cached_chconf0
- Return type: static u32
- Signature: mcspi_cached_chconf0(const struct spi_device * spi)
- Line: 180

### mcspi_read_cs_reg
- Return type: static u32
- Signature: mcspi_read_cs_reg(const struct spi_device * spi,int idx)
- Line: 173

### mcspi_read_reg
- Return type: static u32
- Signature: mcspi_read_reg(struct spi_controller * ctlr,int idx)
- Line: 158

### mcspi_wait_for_completion
- Return type: static int
- Signature: mcspi_wait_for_completion(struct omap2_mcspi * mcspi,struct completion * x)
- Line: 379

### mcspi_wait_for_reg_bit
- Return type: static int
- Signature: mcspi_wait_for_reg_bit(void __iomem * reg,unsigned long bit)
- Line: 362

### mcspi_write_chconf0
- Return type: static void
- Signature: mcspi_write_chconf0(const struct spi_device * spi,u32 val)
- Line: 187

### mcspi_write_cs_reg
- Return type: static void
- Signature: mcspi_write_cs_reg(const struct spi_device * spi,int idx,u32 val)
- Line: 165

### mcspi_write_reg
- Return type: static void
- Signature: mcspi_write_reg(struct spi_controller * ctlr,int idx,u32 val)
- Line: 150

### omap2_mcspi_calc_divisor
- Return type: static u32
- Signature: omap2_mcspi_calc_divisor(u32 speed_hz,u32 ref_clk_hz)
- Line: 898

### omap2_mcspi_can_dma
- Return type: static bool
- Signature: omap2_mcspi_can_dma(struct spi_controller * ctlr,struct spi_device * spi,struct spi_transfer * xfer)
- Line: 1341

### omap2_mcspi_cleanup
- Return type: static void
- Signature: omap2_mcspi_cleanup(struct spi_device * spi)
- Line: 1063

### omap2_mcspi_controller_setup
- Return type: static int
- Signature: omap2_mcspi_controller_setup(struct omap2_mcspi * mcspi)
- Line: 1373

### omap2_mcspi_irq_handler
- Return type: static irqreturn_t
- Signature: omap2_mcspi_irq_handler(int irq,void * data)
- Line: 1116

### omap2_mcspi_max_xfer_size
- Return type: static size_t
- Signature: omap2_mcspi_max_xfer_size(struct spi_device * spi)
- Line: 1361

### omap2_mcspi_prepare_message
- Return type: static int
- Signature: omap2_mcspi_prepare_message(struct spi_controller * ctlr,struct spi_message * msg)
- Line: 1265

### omap2_mcspi_probe
- Return type: static int
- Signature: omap2_mcspi_probe(struct platform_device * pdev)
- Line: 1475

### omap2_mcspi_release_dma
- Return type: static void
- Signature: omap2_mcspi_release_dma(struct spi_controller * ctlr)
- Line: 1043

### omap2_mcspi_remove
- Return type: static void
- Signature: omap2_mcspi_remove(struct platform_device * pdev)
- Line: 1611

### omap2_mcspi_request_dma
- Return type: static int
- Signature: omap2_mcspi_request_dma(struct omap2_mcspi * mcspi,struct omap2_mcspi_dma * mcspi_dma)
- Line: 1014

### omap2_mcspi_resume
- Return type: static int __maybe_unused
- Signature: omap2_mcspi_resume(struct device * dev)
- Line: 1651

### omap2_mcspi_rx_callback
- Return type: static void
- Signature: omap2_mcspi_rx_callback(void * data)
- Line: 393

### omap2_mcspi_rx_dma
- Return type: static unsigned
- Signature: omap2_mcspi_rx_dma(struct spi_device * spi,struct spi_transfer * xfer,struct dma_slave_config cfg,unsigned es)
- Line: 446

### omap2_mcspi_set_cs
- Return type: static void
- Signature: omap2_mcspi_set_cs(struct spi_device * spi,bool enable)
- Line: 242

### omap2_mcspi_set_dma_req
- Return type: static void
- Signature: omap2_mcspi_set_dma_req(const struct spi_device * spi,int is_read,int enable)
- Line: 206

### omap2_mcspi_set_enable
- Return type: static void
- Signature: omap2_mcspi_set_enable(const struct spi_device * spi,int enable)
- Line: 226

### omap2_mcspi_set_fifo
- Return type: static void
- Signature: omap2_mcspi_set_fifo(const struct spi_device * spi,struct spi_transfer * t,int enable)
- Line: 306

### omap2_mcspi_set_mode
- Return type: static void
- Signature: omap2_mcspi_set_mode(struct spi_controller * ctlr)
- Line: 279

### omap2_mcspi_setup
- Return type: static int
- Signature: omap2_mcspi_setup(struct spi_device * spi)
- Line: 1076

### omap2_mcspi_setup_transfer
- Return type: static int
- Signature: omap2_mcspi_setup_transfer(struct spi_device * spi,struct spi_transfer * t)
- Line: 910

### omap2_mcspi_suspend
- Return type: static int __maybe_unused
- Signature: omap2_mcspi_suspend(struct device * dev)
- Line: 1632

### omap2_mcspi_target_abort
- Return type: static int
- Signature: omap2_mcspi_target_abort(struct spi_controller * ctlr)
- Line: 1133

### omap2_mcspi_transfer_one
- Return type: static int
- Signature: omap2_mcspi_transfer_one(struct spi_controller * ctlr,struct spi_device * spi,struct spi_transfer * t)
- Line: 1146

### omap2_mcspi_tx_callback
- Return type: static void
- Signature: omap2_mcspi_tx_callback(void * data)
- Line: 405

### omap2_mcspi_tx_dma
- Return type: static void
- Signature: omap2_mcspi_tx_dma(struct spi_device * spi,struct spi_transfer * xfer,struct dma_slave_config cfg)
- Line: 417

### omap2_mcspi_txrx_dma
- Return type: static unsigned
- Signature: omap2_mcspi_txrx_dma(struct spi_device * spi,struct spi_transfer * xfer)
- Line: 593

### omap2_mcspi_txrx_pio
- Return type: static unsigned
- Signature: omap2_mcspi_txrx_pio(struct spi_device * spi,struct spi_transfer * xfer)
- Line: 702

### omap_mcspi_runtime_resume
- Return type: static int
- Signature: omap_mcspi_runtime_resume(struct device * dev)
- Line: 1408

### omap_mcspi_runtime_suspend
- Return type: static int
- Signature: omap_mcspi_runtime_suspend(struct device * dev)
- Line: 1392

## Structs (4)

### omap2_mcspi
- Line: 120
- Members:
  - dma_tx: dma_chan *
  - dma_rx: dma_chan *
  - dma_tx_completion: completion
  - dma_rx_completion: completion
  - dma_rx_ch_name: char[14]
  - dma_tx_ch_name: char[14]
  - modulctrl: u32
  - wakeupenable: u32
  - cs: list_head
  - txdone: completion
  - ctlr: spi_controller *
  - base: void __iomem *
  - phys: unsigned long
  - dma_channels: omap2_mcspi_dma *
  - dev: device *
  - ctx: omap2_mcspi_regs
  - ref_clk: clk *
  - fifo_depth: int
  - target_aborted: bool
  - pin_dir: unsigned int:1
  - max_xfer_len: size_t
  - ref_clk_hz: u32
  - use_multi_mode: bool
  - last_msg_kept_cs: bool
  - base: void __iomem *
  - phys: unsigned long
  - word_len: int
  - mode: u16
  - node: list_head
  - chconf0: u32
  - chctrl0: u32

### omap2_mcspi_cs
- Line: 140
- Members:
  - dma_tx: dma_chan *
  - dma_rx: dma_chan *
  - dma_tx_completion: completion
  - dma_rx_completion: completion
  - dma_rx_ch_name: char[14]
  - dma_tx_ch_name: char[14]
  - modulctrl: u32
  - wakeupenable: u32
  - cs: list_head
  - txdone: completion
  - ctlr: spi_controller *
  - base: void __iomem *
  - phys: unsigned long
  - dma_channels: omap2_mcspi_dma *
  - dev: device *
  - ctx: omap2_mcspi_regs
  - ref_clk: clk *
  - fifo_depth: int
  - target_aborted: bool
  - pin_dir: unsigned int:1
  - max_xfer_len: size_t
  - ref_clk_hz: u32
  - use_multi_mode: bool
  - last_msg_kept_cs: bool
  - base: void __iomem *
  - phys: unsigned long
  - word_len: int
  - mode: u16
  - node: list_head
  - chconf0: u32
  - chctrl0: u32

### omap2_mcspi_dma
- Line: 93
- Members:
  - dma_tx: dma_chan *
  - dma_rx: dma_chan *
  - dma_tx_completion: completion
  - dma_rx_completion: completion
  - dma_rx_ch_name: char[14]
  - dma_tx_ch_name: char[14]
  - modulctrl: u32
  - wakeupenable: u32
  - cs: list_head
  - txdone: completion
  - ctlr: spi_controller *
  - base: void __iomem *
  - phys: unsigned long
  - dma_channels: omap2_mcspi_dma *
  - dev: device *
  - ctx: omap2_mcspi_regs
  - ref_clk: clk *
  - fifo_depth: int
  - target_aborted: bool
  - pin_dir: unsigned int:1
  - max_xfer_len: size_t
  - ref_clk_hz: u32
  - use_multi_mode: bool
  - last_msg_kept_cs: bool
  - base: void __iomem *
  - phys: unsigned long
  - word_len: int
  - mode: u16
  - node: list_head
  - chconf0: u32
  - chctrl0: u32

### omap2_mcspi_regs
- Line: 114
- Members:
  - dma_tx: dma_chan *
  - dma_rx: dma_chan *
  - dma_tx_completion: completion
  - dma_rx_completion: completion
  - dma_rx_ch_name: char[14]
  - dma_tx_ch_name: char[14]
  - modulctrl: u32
  - wakeupenable: u32
  - cs: list_head
  - txdone: completion
  - ctlr: spi_controller *
  - base: void __iomem *
  - phys: unsigned long
  - dma_channels: omap2_mcspi_dma *
  - dev: device *
  - ctx: omap2_mcspi_regs
  - ref_clk: clk *
  - fifo_depth: int
  - target_aborted: bool
  - pin_dir: unsigned int:1
  - max_xfer_len: size_t
  - ref_clk_hz: u32
  - use_multi_mode: bool
  - last_msg_kept_cs: bool
  - base: void __iomem *
  - phys: unsigned long
  - word_len: int
  - mode: u16
  - node: list_head
  - chconf0: u32
  - chctrl0: u32

## Variables (6)

- static **am654_pdata** : omap2_mcspi_platform_config (line 1453)
- static **omap2_mcspi_driver** : platform_driver (line 1672)
- static **omap2_mcspi_pm_ops** : const struct dev_pm_ops (line 1665)
- static **omap2_pdata** : omap2_mcspi_platform_config (line 1445)
- static **omap4_pdata** : omap2_mcspi_platform_config (line 1449)
- static **omap_mcspi_of_match** : const struct of_device_id[] (line 1458)

## Macros (48)

- **DMA_MIN_BYTES** (line 107)
- **OMAP2_MCSPI_CHCONF0** (line 50)
- **OMAP2_MCSPI_CHCONF_CLKD_MASK** (line 65)
- **OMAP2_MCSPI_CHCONF_CLKG** (line 80)
- **OMAP2_MCSPI_CHCONF_DMAR** (line 72)
- **OMAP2_MCSPI_CHCONF_DMAW** (line 71)
- **OMAP2_MCSPI_CHCONF_DPE0** (line 73)
- **OMAP2_MCSPI_CHCONF_DPE1** (line 74)
- **OMAP2_MCSPI_CHCONF_EPOL** (line 66)
- **OMAP2_MCSPI_CHCONF_FFER** (line 79)
- **OMAP2_MCSPI_CHCONF_FFET** (line 78)
- **OMAP2_MCSPI_CHCONF_FORCE** (line 77)
- **OMAP2_MCSPI_CHCONF_IS** (line 75)
- **OMAP2_MCSPI_CHCONF_PHA** (line 63)
- **OMAP2_MCSPI_CHCONF_POL** (line 64)
- **OMAP2_MCSPI_CHCONF_TRM_MASK** (line 70)
- **OMAP2_MCSPI_CHCONF_TRM_RX_ONLY** (line 68)
- **OMAP2_MCSPI_CHCONF_TRM_TX_ONLY** (line 69)
- **OMAP2_MCSPI_CHCONF_TURBO** (line 76)
- **OMAP2_MCSPI_CHCONF_WL_MASK** (line 67)
- **OMAP2_MCSPI_CHCTRL0** (line 52)
- **OMAP2_MCSPI_CHCTRL_EN** (line 87)
- **OMAP2_MCSPI_CHCTRL_EXTCLK_MASK** (line 88)
- **OMAP2_MCSPI_CHSTAT0** (line 51)
- **OMAP2_MCSPI_CHSTAT_EOT** (line 84)
- **OMAP2_MCSPI_CHSTAT_RXS** (line 82)
- **OMAP2_MCSPI_CHSTAT_TXFFE** (line 85)
- **OMAP2_MCSPI_CHSTAT_TXS** (line 83)
- **OMAP2_MCSPI_IRQENABLE** (line 43)
- **OMAP2_MCSPI_IRQSTATUS** (line 42)
- **OMAP2_MCSPI_IRQSTATUS_EOW** (line 57)
- **OMAP2_MCSPI_MAX_DIVIDER** (line 35)
- **OMAP2_MCSPI_MAX_FIFODEPTH** (line 36)
- **OMAP2_MCSPI_MAX_FIFOWCNT** (line 37)
- **OMAP2_MCSPI_MAX_FREQ** (line 34)
- **OMAP2_MCSPI_MODULCTRL** (line 46)
- **OMAP2_MCSPI_MODULCTRL_MS** (line 60)
- **OMAP2_MCSPI_MODULCTRL_SINGLE** (line 59)
- **OMAP2_MCSPI_MODULCTRL_STEST** (line 61)
- **OMAP2_MCSPI_REVISION** (line 40)
- **OMAP2_MCSPI_RX0** (line 54)
- **OMAP2_MCSPI_SYSSTATUS** (line 41)
- **OMAP2_MCSPI_SYST** (line 45)
- **OMAP2_MCSPI_TX0** (line 53)
- **OMAP2_MCSPI_WAKEUPENABLE** (line 44)
- **OMAP2_MCSPI_WAKEUPENABLE_WKEN** (line 90)
- **OMAP2_MCSPI_XFERLEVEL** (line 47)
- **SPI_AUTOSUSPEND_TIMEOUT** (line 38)
