# drivers/spi/spi-meson-spicc.c

Subsystem: drivers/spi

## Functions (29)

### meson_spicc_auto_io_delay
- Return type: static void
- Signature: meson_spicc_auto_io_delay(struct meson_spicc_device * spicc)
- Line: 490

### meson_spicc_calc_dma_len
- Return type: static u32
- Signature: meson_spicc_calc_dma_len(struct meson_spicc_device * spicc,u32 len,u32 * dma_burst_len)
- Line: 270

### meson_spicc_cleanup
- Return type: static void
- Signature: meson_spicc_cleanup(struct spi_device * spi)
- Line: 754

### meson_spicc_dma_irq
- Return type: static irqreturn_t
- Signature: meson_spicc_dma_irq(struct meson_spicc_device * spicc)
- Line: 357

### meson_spicc_dma_map
- Return type: static int
- Signature: meson_spicc_dma_map(struct meson_spicc_device * spicc,struct spi_transfer * t)
- Line: 233

### meson_spicc_dma_unmap
- Return type: static void
- Signature: meson_spicc_dma_unmap(struct meson_spicc_device * spicc,struct spi_transfer * t)
- Line: 255

### meson_spicc_enh_clk_init
- Return type: static int
- Signature: meson_spicc_enh_clk_init(struct meson_spicc_device * spicc)
- Line: 893

### meson_spicc_irq
- Return type: static irqreturn_t
- Signature: meson_spicc_irq(int irq,void * data)
- Line: 460

### meson_spicc_oen_enable
- Return type: static void
- Signature: meson_spicc_oen_enable(struct meson_spicc_device * spicc)
- Line: 206

### meson_spicc_pow2_clk_init
- Return type: static int
- Signature: meson_spicc_pow2_clk_init(struct meson_spicc_device * spicc)
- Line: 829

### meson_spicc_pow2_determine_rate
- Return type: static int
- Signature: meson_spicc_pow2_determine_rate(struct clk_hw * hw,struct clk_rate_request * req)
- Line: 799

### meson_spicc_pow2_recalc_rate
- Return type: static unsigned long
- Signature: meson_spicc_pow2_recalc_rate(struct clk_hw * hw,unsigned long parent_rate)
- Line: 787

### meson_spicc_pow2_set_rate
- Return type: static int
- Signature: meson_spicc_pow2_set_rate(struct clk_hw * hw,unsigned long rate,unsigned long parent_rate)
- Line: 811

### meson_spicc_prepare_message
- Return type: static int
- Signature: meson_spicc_prepare_message(struct spi_controller * host,struct spi_message * message)
- Line: 652

### meson_spicc_probe
- Return type: static int
- Signature: meson_spicc_probe(struct platform_device * pdev)
- Line: 979

### meson_spicc_pull_data
- Return type: static u32
- Signature: meson_spicc_pull_data(struct meson_spicc_device * spicc)
- Line: 387

### meson_spicc_push_data
- Return type: static void
- Signature: meson_spicc_push_data(struct meson_spicc_device * spicc,u32 data)
- Line: 404

### meson_spicc_remove
- Return type: static void
- Signature: meson_spicc_remove(struct platform_device * pdev)
- Line: 1098

### meson_spicc_reset_fifo
- Return type: static void
- Signature: meson_spicc_reset_fifo(struct meson_spicc_device * spicc)
- Line: 557

### meson_spicc_rx
- Return type: static void
- Signature: meson_spicc_rx(struct meson_spicc_device * spicc)
- Line: 420

### meson_spicc_rxready
- Return type: static bool
- Signature: meson_spicc_rxready(struct meson_spicc_device * spicc)
- Line: 381

### meson_spicc_setup
- Return type: static int
- Signature: meson_spicc_setup(struct spi_device * spi)
- Line: 738

### meson_spicc_setup_burst
- Return type: static void
- Signature: meson_spicc_setup_burst(struct meson_spicc_device * spicc)
- Line: 438

### meson_spicc_setup_dma
- Return type: static void
- Signature: meson_spicc_setup_dma(struct meson_spicc_device * spicc)
- Line: 303

### meson_spicc_setup_xfer
- Return type: static void
- Signature: meson_spicc_setup_xfer(struct meson_spicc_device * spicc,struct spi_transfer * xfer)
- Line: 533

### meson_spicc_transfer_one
- Return type: static int
- Signature: meson_spicc_transfer_one(struct spi_controller * host,struct spi_device * spi,struct spi_transfer * xfer)
- Line: 575

### meson_spicc_tx
- Return type: static void
- Signature: meson_spicc_tx(struct meson_spicc_device * spicc)
- Line: 429

### meson_spicc_txfull
- Return type: static bool
- Signature: meson_spicc_txfull(struct meson_spicc_device * spicc)
- Line: 375

### meson_spicc_unprepare_transfer
- Return type: static int
- Signature: meson_spicc_unprepare_transfer(struct spi_controller * host)
- Line: 719

## Structs (2)

### meson_spicc_data
- Line: 169
- Members:
  - max_speed_hz: unsigned int
  - min_speed_hz: unsigned int
  - fifo_size: unsigned int
  - has_oen: bool
  - has_enhance_clk_div: bool
  - has_pclk: bool
  - host: spi_controller *
  - pdev: platform_device *
  - base: void __iomem *
  - core: clk *
  - pclk: clk *
  - pow2_div: clk_divider
  - clk: clk *
  - message: spi_message *
  - xfer: spi_transfer *
  - done: completion
  - data: const struct meson_spicc_data *
  - tx_buf: u8 *
  - rx_buf: u8 *
  - bytes_per_word: unsigned int
  - tx_remain: unsigned long
  - rx_remain: unsigned long
  - xfer_remain: unsigned long
  - pinctrl: pinctrl *
  - pins_idle_high: pinctrl_state *
  - pins_idle_low: pinctrl_state *
  - tx_dma: dma_addr_t
  - rx_dma: dma_addr_t
  - using_dma: bool

### meson_spicc_device
- Line: 178
- Members:
  - max_speed_hz: unsigned int
  - min_speed_hz: unsigned int
  - fifo_size: unsigned int
  - has_oen: bool
  - has_enhance_clk_div: bool
  - has_pclk: bool
  - host: spi_controller *
  - pdev: platform_device *
  - base: void __iomem *
  - core: clk *
  - pclk: clk *
  - pow2_div: clk_divider
  - clk: clk *
  - message: spi_message *
  - xfer: spi_transfer *
  - done: completion
  - data: const struct meson_spicc_data *
  - tx_buf: u8 *
  - rx_buf: u8 *
  - bytes_per_word: unsigned int
  - tx_remain: unsigned long
  - rx_remain: unsigned long
  - xfer_remain: unsigned long
  - pinctrl: pinctrl *
  - pins_idle_high: pinctrl_state *
  - pins_idle_low: pinctrl_state *
  - tx_dma: dma_addr_t
  - rx_dma: dma_addr_t
  - using_dma: bool

## Variables (6)

- static **meson_spicc_axg_data** : const struct meson_spicc_data (line 1118)
- static **meson_spicc_driver** : platform_driver (line 1152)
- static **meson_spicc_g12a_data** : const struct meson_spicc_data (line 1126)
- static **meson_spicc_gx_data** : const struct meson_spicc_data (line 1112)
- static **meson_spicc_of_match** : const struct of_device_id[] (line 1135)
- static **meson_spicc_pow2_clk_ops** : const struct clk_ops (line 823)

## Macros (107)

- **DMA_ADDR_LOAD_FROM_LD_ADDR** (line 147)
- **DMA_BURST_COUNT_MAX** (line 153)
- **DMA_BURST_LEN_DEFAULT** (line 152)
- **DMA_EN_SET_BY_VSYNC** (line 141)
- **DMA_RADDR_LOAD_BY_VSYNC** (line 145)
- **DMA_READ_COUNTER** (line 150)
- **DMA_READ_COUNTER_EN** (line 143)
- **DMA_WADDR_LOAD_BY_VSYNC** (line 146)
- **DMA_WRITE_COUNTER** (line 151)
- **DMA_WRITE_COUNTER_EN** (line 144)
- **SPICC_BITLENGTH_MASK** (line 72)
- **SPICC_BURSTLENGTH_MASK** (line 73)
- **SPICC_CAP_AHEAD_1_CYCLE** (line 129)
- **SPICC_CAP_AHEAD_2_CYCLE** (line 128)
- **SPICC_CAP_DELAY_1_CYCLE** (line 131)
- **SPICC_CAP_NO_DELAY** (line 130)
- **SPICC_CONREG** (line 53)
- **SPICC_CS_MASK** (line 66)
- **SPICC_DATARATE_DIV16** (line 70)
- **SPICC_DATARATE_DIV32** (line 71)
- **SPICC_DATARATE_DIV4** (line 68)
- **SPICC_DATARATE_DIV8** (line 69)
- **SPICC_DATARATE_MASK** (line 67)
- **SPICC_DLYCTL_RO_MASK** (line 116)
- **SPICC_DMAREG** (line 85)
- **SPICC_DMA_BURSTNUM_MASK** (line 93)
- **SPICC_DMA_ENABLE** (line 86)
- **SPICC_DMA_THREADID_MASK** (line 92)
- **SPICC_DMA_URGENT** (line 91)
- **SPICC_DRADDR** (line 135)
- **SPICC_DRCTL_FALLING** (line 64)
- **SPICC_DRCTL_IGNORE** (line 63)
- **SPICC_DRCTL_LOWLEVEL** (line 65)
- **SPICC_DRCTL_MASK** (line 62)
- **SPICC_DWADDR** (line 137)
- **SPICC_ENABLE** (line 54)
- **SPICC_ENH_CLK_CS_DELAY_EN** (line 163)
- **SPICC_ENH_CLK_CS_DELAY_MASK** (line 157)
- **SPICC_ENH_CLK_OEN** (line 161)
- **SPICC_ENH_CS_OEN** (line 162)
- **SPICC_ENH_CTL0** (line 156)
- **SPICC_ENH_DATARATE_EN** (line 159)
- **SPICC_ENH_DATARATE_MASK** (line 158)
- **SPICC_ENH_MAIN_CLK_AO** (line 164)
- **SPICC_ENH_MOSI_OEN** (line 160)
- **SPICC_FIFORST_RO_MASK** (line 132)
- **SPICC_FIFORST_W1_MASK** (line 133)
- **SPICC_INTREG** (line 75)
- **SPICC_LBC_RO** (line 112)
- **SPICC_LBC_W1** (line 113)
- **SPICC_LD_CNTL0** (line 139)
- **SPICC_LD_CNTL1** (line 149)
- **SPICC_MAX_BURST** (line 46)
- **SPICC_MI_CAP_DELAY_MASK** (line 127)
- **SPICC_MI_DELAY_1_CYCLE** (line 124)
- **SPICC_MI_DELAY_2_CYCLE** (line 125)
- **SPICC_MI_DELAY_3_CYCLE** (line 126)
- **SPICC_MI_DELAY_MASK** (line 122)
- **SPICC_MI_NO_DELAY** (line 123)
- **SPICC_MODE_MASTER** (line 55)
- **SPICC_MO_DELAY_1_CYCLE** (line 119)
- **SPICC_MO_DELAY_2_CYCLE** (line 120)
- **SPICC_MO_DELAY_3_CYCLE** (line 121)
- **SPICC_MO_DELAY_MASK** (line 117)
- **SPICC_MO_NO_DELAY** (line 118)
- **SPICC_PERIOD** (line 106)
- **SPICC_PERIODREG** (line 105)
- **SPICC_PHA** (line 59)
- **SPICC_POL** (line 58)
- **SPICC_READ_BURST_MASK** (line 89)
- **SPICC_RF** (line 101)
- **SPICC_RF_EN** (line 81)
- **SPICC_RH** (line 100)
- **SPICC_RH_EN** (line 80)
- **SPICC_RO** (line 102)
- **SPICC_RO_EN** (line 82)
- **SPICC_RR** (line 99)
- **SPICC_RR_EN** (line 79)
- **SPICC_RXCNT_MASK** (line 110)
- **SPICC_RXDATA** (line 49)
- **SPICC_RXFIFO_THRESHOLD_MASK** (line 88)
- **SPICC_SMC** (line 57)
- **SPICC_SMSTATUS_MASK** (line 111)
- **SPICC_SSCTL** (line 60)
- **SPICC_SSPOL** (line 61)
- **SPICC_STATREG** (line 95)
- **SPICC_SWAP_RO** (line 114)
- **SPICC_SWAP_W1** (line 115)
- **SPICC_TC** (line 103)
- **SPICC_TC_EN** (line 83)
- **SPICC_TE** (line 96)
- **SPICC_TESTREG** (line 108)
- **SPICC_TE_EN** (line 76)
- **SPICC_TF** (line 98)
- **SPICC_TF_EN** (line 78)
- **SPICC_TH** (line 97)
- **SPICC_TH_EN** (line 77)
- **SPICC_TXCNT_MASK** (line 109)
- **SPICC_TXDATA** (line 51)
- **SPICC_TXFIFO_THRESHOLD_MASK** (line 87)
- **SPICC_WRITE_BURST_MASK** (line 90)
- **SPICC_XCH** (line 56)
- **SPI_BURST_LEN_MAX** (line 154)
- **VSYNC_IRQ_SRC_SELECT** (line 140)
- **XCH_EN_SET_BY_VSYNC** (line 142)
- **pow2_clk_to_spicc**(_div) (line 204)
- **writel_bits_relaxed**(mask,val,addr) (line 166)
