# drivers/spi/spi-sun6i.c

Subsystem: drivers/spi

## Functions (18)

### sun6i_spi_can_dma
- Return type: static bool
- Signature: sun6i_spi_can_dma(struct spi_controller * host,struct spi_device * spi,struct spi_transfer * xfer)
- Line: 615

### sun6i_spi_disable_interrupt
- Return type: static void
- Signature: sun6i_spi_disable_interrupt(struct sun6i_spi * sspi,u32 mask)
- Line: 141

### sun6i_spi_dma_rx_cb
- Return type: static void
- Signature: sun6i_spi_dma_rx_cb(void * param)
- Line: 204

### sun6i_spi_drain_fifo
- Return type: static void
- Signature: sun6i_spi_drain_fifo(struct sun6i_spi * sspi)
- Line: 149

### sun6i_spi_fill_fifo
- Return type: static void
- Signature: sun6i_spi_fill_fifo(struct sun6i_spi * sspi)
- Line: 164

### sun6i_spi_get_rx_fifo_count
- Return type: static u32
- Signature: sun6i_spi_get_rx_fifo_count(struct sun6i_spi * sspi)
- Line: 127

### sun6i_spi_get_tx_fifo_count
- Return type: static u32
- Signature: sun6i_spi_get_tx_fifo_count(struct sun6i_spi * sspi)
- Line: 134

### sun6i_spi_handler
- Return type: static irqreturn_t
- Signature: sun6i_spi_handler(int irq,void * dev_id)
- Line: 529

### sun6i_spi_max_transfer_size
- Return type: static size_t
- Signature: sun6i_spi_max_transfer_size(struct spi_device * spi)
- Line: 199

### sun6i_spi_prepare_dma
- Return type: static int
- Signature: sun6i_spi_prepare_dma(struct sun6i_spi * sspi,struct spi_transfer * tfr)
- Line: 211

### sun6i_spi_probe
- Return type: static int
- Signature: sun6i_spi_probe(struct platform_device * pdev)
- Line: 629

### sun6i_spi_read
- Return type: static u32
- Signature: sun6i_spi_read(struct sun6i_spi * sspi,u32 reg)
- Line: 117

### sun6i_spi_remove
- Return type: static void
- Signature: sun6i_spi_remove(struct platform_device * pdev)
- Line: 767

### sun6i_spi_runtime_resume
- Return type: static int
- Signature: sun6i_spi_runtime_resume(struct device * dev)
- Line: 566

### sun6i_spi_runtime_suspend
- Return type: static int
- Signature: sun6i_spi_runtime_suspend(struct device * dev)
- Line: 603

### sun6i_spi_set_cs
- Return type: static void
- Signature: sun6i_spi_set_cs(struct spi_device * spi,bool enable)
- Line: 182

### sun6i_spi_transfer_one
- Return type: static int
- Signature: sun6i_spi_transfer_one(struct spi_controller * host,struct spi_device * spi,struct spi_transfer * tfr)
- Line: 275

### sun6i_spi_write
- Return type: static void
- Signature: sun6i_spi_write(struct sun6i_spi * sspi,u32 reg,u32 value)
- Line: 122

## Structs (2)

### sun6i_spi
- Line: 99
- Members:
  - fifo_depth: unsigned long
  - has_clk_ctl: bool
  - mode_bits: u32
  - host: spi_controller *
  - base_addr: void __iomem *
  - dma_addr_rx: dma_addr_t
  - dma_addr_tx: dma_addr_t
  - hclk: clk *
  - mclk: clk *
  - rstc: reset_control *
  - done: completion
  - dma_rx_done: completion
  - tx_buf: const u8 *
  - rx_buf: u8 *
  - len: int
  - cfg: const struct sun6i_spi_cfg *

### sun6i_spi_cfg
- Line: 93
- Members:
  - fifo_depth: unsigned long
  - has_clk_ctl: bool
  - mode_bits: u32
  - host: spi_controller *
  - base_addr: void __iomem *
  - dma_addr_rx: dma_addr_t
  - dma_addr_tx: dma_addr_t
  - hclk: clk *
  - mclk: clk *
  - rstc: reset_control *
  - done: completion
  - dma_rx_done: completion
  - tx_buf: const u8 *
  - rx_buf: u8 *
  - len: int
  - cfg: const struct sun6i_spi_cfg *

## Variables (6)

- static **sun50i_r329_spi_cfg** : const struct sun6i_spi_cfg (line 795)
- static **sun6i_a31_spi_cfg** : const struct sun6i_spi_cfg (line 785)
- static **sun6i_spi_driver** : platform_driver (line 819)
- static **sun6i_spi_match** : const struct of_device_id[] (line 800)
- static **sun6i_spi_pm_ops** : const struct dev_pm_ops (line 814)
- static **sun8i_h3_spi_cfg** : const struct sun6i_spi_cfg (line 790)

## Macros (54)

- **SUN6I_AUTOSUSPEND_TIMEOUT** (line 25)
- **SUN6I_BURST_CNT_REG** (line 81)
- **SUN6I_BURST_CTL_CNT_DRM** (line 87)
- **SUN6I_BURST_CTL_CNT_QUAD_EN** (line 88)
- **SUN6I_BURST_CTL_CNT_REG** (line 85)
- **SUN6I_BURST_CTL_CNT_STC_MASK** (line 86)
- **SUN6I_CLK_CTL_CDR1**(div) (line 76)
- **SUN6I_CLK_CTL_CDR1_MASK** (line 75)
- **SUN6I_CLK_CTL_CDR2**(div) (line 74)
- **SUN6I_CLK_CTL_CDR2_MASK** (line 73)
- **SUN6I_CLK_CTL_DRS** (line 77)
- **SUN6I_CLK_CTL_REG** (line 72)
- **SUN6I_FIFO_CTL_REG** (line 58)
- **SUN6I_FIFO_CTL_RF_DRQ_EN** (line 60)
- **SUN6I_FIFO_CTL_RF_RDY_TRIG_LEVEL_BITS** (line 61)
- **SUN6I_FIFO_CTL_RF_RDY_TRIG_LEVEL_MASK** (line 59)
- **SUN6I_FIFO_CTL_RF_RST** (line 62)
- **SUN6I_FIFO_CTL_TF_DRQ_EN** (line 65)
- **SUN6I_FIFO_CTL_TF_ERQ_TRIG_LEVEL_BITS** (line 64)
- **SUN6I_FIFO_CTL_TF_ERQ_TRIG_LEVEL_MASK** (line 63)
- **SUN6I_FIFO_CTL_TF_RST** (line 66)
- **SUN6I_FIFO_DEPTH** (line 27)
- **SUN6I_FIFO_STA_REG** (line 68)
- **SUN6I_FIFO_STA_RF_CNT_MASK** (line 69)
- **SUN6I_FIFO_STA_TF_CNT_MASK** (line 70)
- **SUN6I_GBL_CTL_BUS_ENABLE** (line 31)
- **SUN6I_GBL_CTL_MASTER** (line 32)
- **SUN6I_GBL_CTL_REG** (line 30)
- **SUN6I_GBL_CTL_RST** (line 34)
- **SUN6I_GBL_CTL_TP** (line 33)
- **SUN6I_INT_CTL_REG** (line 50)
- **SUN6I_INT_CTL_RF_OVF** (line 53)
- **SUN6I_INT_CTL_RF_RDY** (line 51)
- **SUN6I_INT_CTL_TC** (line 54)
- **SUN6I_INT_CTL_TF_ERQ** (line 52)
- **SUN6I_INT_STA_REG** (line 56)
- **SUN6I_MAX_XFER_SIZE** (line 79)
- **SUN6I_RXDATA_REG** (line 91)
- **SUN6I_TFR_CTL_CPHA** (line 37)
- **SUN6I_TFR_CTL_CPOL** (line 38)
- **SUN6I_TFR_CTL_CS**(cs) (line 41)
- **SUN6I_TFR_CTL_CS_LEVEL** (line 43)
- **SUN6I_TFR_CTL_CS_MANUAL** (line 42)
- **SUN6I_TFR_CTL_CS_MASK** (line 40)
- **SUN6I_TFR_CTL_DHB** (line 44)
- **SUN6I_TFR_CTL_FBS** (line 46)
- **SUN6I_TFR_CTL_REG** (line 36)
- **SUN6I_TFR_CTL_SDC** (line 45)
- **SUN6I_TFR_CTL_SDM** (line 47)
- **SUN6I_TFR_CTL_SPOL** (line 39)
- **SUN6I_TFR_CTL_XCH** (line 48)
- **SUN6I_TXDATA_REG** (line 90)
- **SUN6I_XMIT_CNT_REG** (line 83)
- **SUN8I_FIFO_DEPTH** (line 28)
