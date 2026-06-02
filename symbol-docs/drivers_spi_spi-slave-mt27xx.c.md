# drivers/spi/spi-slave-mt27xx.c

Subsystem: drivers/spi

## Functions (16)

### mtk_spi_slave_disable_dma
- Return type: static void
- Signature: mtk_spi_slave_disable_dma(struct mtk_spi_slave * mdata)
- Line: 98

### mtk_spi_slave_disable_xfer
- Return type: static void
- Signature: mtk_spi_slave_disable_xfer(struct mtk_spi_slave * mdata)
- Line: 108

### mtk_spi_slave_dma_transfer
- Return type: static int
- Signature: mtk_spi_slave_dma_transfer(struct spi_controller * ctlr,struct spi_device * spi,struct spi_transfer * xfer)
- Line: 199

### mtk_spi_slave_fifo_transfer
- Return type: static int
- Signature: mtk_spi_slave_fifo_transfer(struct spi_controller * ctlr,struct spi_device * spi,struct spi_transfer * xfer)
- Line: 162

### mtk_spi_slave_interrupt
- Return type: static irqreturn_t
- Signature: mtk_spi_slave_interrupt(int irq,void * dev_id)
- Line: 327

### mtk_spi_slave_prepare_message
- Return type: static int
- Signature: mtk_spi_slave_prepare_message(struct spi_controller * ctlr,struct spi_message * msg)
- Line: 129

### mtk_spi_slave_probe
- Return type: static int
- Signature: mtk_spi_slave_probe(struct platform_device * pdev)
- Line: 384

### mtk_spi_slave_remove
- Return type: static void
- Signature: mtk_spi_slave_remove(struct platform_device * pdev)
- Line: 474

### mtk_spi_slave_resume
- Return type: static int
- Signature: mtk_spi_slave_resume(struct device * dev)
- Line: 504

### mtk_spi_slave_runtime_resume
- Return type: static int
- Signature: mtk_spi_slave_runtime_resume(struct device * dev)
- Line: 537

### mtk_spi_slave_runtime_suspend
- Return type: static int
- Signature: mtk_spi_slave_runtime_suspend(struct device * dev)
- Line: 527

### mtk_spi_slave_setup
- Return type: static int
- Signature: mtk_spi_slave_setup(struct spi_device * spi)
- Line: 298

### mtk_spi_slave_suspend
- Return type: static int
- Signature: mtk_spi_slave_suspend(struct device * dev)
- Line: 488

### mtk_spi_slave_transfer_one
- Return type: static int
- Signature: mtk_spi_slave_transfer_one(struct spi_controller * ctlr,struct spi_device * spi,struct spi_transfer * xfer)
- Line: 282

### mtk_spi_slave_wait_for_completion
- Return type: static int
- Signature: mtk_spi_slave_wait_for_completion(struct mtk_spi_slave * mdata)
- Line: 118

### mtk_target_abort
- Return type: static int
- Signature: mtk_target_abort(struct spi_controller * ctlr)
- Line: 317

## Structs (2)

### mtk_spi_compatible
- Line: 76
- Members:
  - dev: device *
  - base: void __iomem *
  - spi_clk: clk *
  - xfer_done: completion
  - cur_transfer: spi_transfer *
  - target_aborted: bool
  - dev_comp: const struct mtk_spi_compatible *
  - max_fifo_size: const u32
  - must_rx: bool
  - need_pad_sel: bool
  - must_tx: bool
  - enhance_timing: bool
  - dma_ext: bool
  - no_need_unprepare: bool
  - ipm_design: bool
  - base: void __iomem *
  - state: u32
  - pad_num: int
  - pad_sel: u32 *
  - parent_clk: clk *
  - sel_clk: clk *
  - spi_clk: clk *
  - spi_hclk: clk *
  - cur_transfer: spi_transfer *
  - xfer_len: u32
  - num_xfered: u32
  - rx_sgl: scatterlist *
  - tx_sgl: scatterlist *
  - rx_sgl_len: u32
  - tx_sgl_len: u32
  - dev_comp: const struct mtk_spi_compatible *
  - qos_request: pm_qos_request
  - spi_clk_hz: u32
  - spimem_done: completion
  - use_spimem: bool
  - dev: device *
  - tx_dma: dma_addr_t
  - rx_dma: dma_addr_t

### mtk_spi_slave
- Line: 66
- Members:
  - dev: device *
  - base: void __iomem *
  - spi_clk: clk *
  - xfer_done: completion
  - cur_transfer: spi_transfer *
  - target_aborted: bool
  - dev_comp: const struct mtk_spi_compatible *
  - max_fifo_size: const u32
  - must_rx: bool

## Variables (5)

- static **mt2712_compat** : const struct mtk_spi_compatible (line 81)
- static **mt8195_compat** : const struct mtk_spi_compatible (line 84)
- static **mtk_spi_slave_driver** : platform_driver (line 559)
- static **mtk_spi_slave_of_match** : const struct of_device_id[] (line 89)
- static **mtk_spi_slave_pm** : const struct dev_pm_ops (line 553)

## Macros (37)

- **CMD_INVALID_EN** (line 32)
- **CMD_INVALID_MASK** (line 44)
- **CMD_INVALID_ST** (line 38)
- **DATA_DONE_EN** (line 30)
- **DATA_DONE_MASK** (line 42)
- **DATA_DONE_ST** (line 36)
- **DMA_DONE_EN** (line 29)
- **DMA_DONE_MASK** (line 41)
- **DMA_DONE_ST** (line 35)
- **RSTA_DONE_EN** (line 31)
- **RSTA_DONE_MASK** (line 43)
- **RSTA_DONE_ST** (line 37)
- **RX_DMA_EN** (line 59)
- **SPIS_CFG_REG** (line 20)
- **SPIS_CPHA** (line 51)
- **SPIS_CPOL** (line 52)
- **SPIS_DMA_ADDR_EN** (line 63)
- **SPIS_DMA_CFG_REG** (line 25)
- **SPIS_IRQ_CLR_REG** (line 17)
- **SPIS_IRQ_EN_REG** (line 16)
- **SPIS_IRQ_MASK_REG** (line 19)
- **SPIS_IRQ_ST_REG** (line 18)
- **SPIS_RXMSBF** (line 50)
- **SPIS_RX_DATA_REG** (line 21)
- **SPIS_RX_DST_REG** (line 23)
- **SPIS_RX_EN** (line 54)
- **SPIS_RX_ENDIAN** (line 48)
- **SPIS_SOFT_RST** (line 64)
- **SPIS_SOFT_RST_REG** (line 26)
- **SPIS_TXMSBF** (line 49)
- **SPIS_TX_DATA_REG** (line 22)
- **SPIS_TX_EN** (line 53)
- **SPIS_TX_ENDIAN** (line 47)
- **SPIS_TX_SRC_REG** (line 24)
- **TX_DMA_EN** (line 58)
- **TX_DMA_LEN** (line 60)
- **TX_DMA_TRIG_EN** (line 57)
