# drivers/spi/spi-mt65xx.c

Subsystem: drivers/spi

## Functions (31)

### mtk_spi_can_dma
- Return type: static bool
- Signature: mtk_spi_can_dma(struct spi_controller * host,struct spi_device * spi,struct spi_transfer * xfer)
- Line: 768

### mtk_spi_dma_transfer
- Return type: static int
- Signature: mtk_spi_dma_transfer(struct spi_controller * host,struct spi_device * spi,struct spi_transfer * xfer)
- Line: 694

### mtk_spi_enable_transfer
- Return type: static void
- Signature: mtk_spi_enable_transfer(struct spi_controller * host)
- Line: 582

### mtk_spi_fifo_transfer
- Return type: static int
- Signature: mtk_spi_fifo_transfer(struct spi_controller * host,struct spi_device * spi,struct spi_transfer * xfer)
- Line: 664

### mtk_spi_get_mult_delta
- Return type: static int
- Signature: mtk_spi_get_mult_delta(struct mtk_spi * mdata,u32 xfer_len)
- Line: 595

### mtk_spi_hw_init
- Return type: static int
- Signature: mtk_spi_hw_init(struct spi_controller * host,struct spi_device * spi)
- Line: 365

### mtk_spi_interrupt
- Return type: static irqreturn_t
- Signature: mtk_spi_interrupt(int irq,void * dev_id)
- Line: 882

### mtk_spi_interrupt_thread
- Return type: static irqreturn_t
- Signature: mtk_spi_interrupt_thread(int irq,void * dev_id)
- Line: 792

### mtk_spi_mem_adjust_op_size
- Return type: static int
- Signature: mtk_spi_mem_adjust_op_size(struct spi_mem * mem,struct spi_mem_op * op)
- Line: 903

### mtk_spi_mem_exec_op
- Return type: static int
- Signature: mtk_spi_mem_exec_op(struct spi_mem * mem,const struct spi_mem_op * op)
- Line: 997

### mtk_spi_mem_setup_dma_xfer
- Return type: static void
- Signature: mtk_spi_mem_setup_dma_xfer(struct spi_controller * host,const struct spi_mem_op * op)
- Line: 943

### mtk_spi_mem_supports_op
- Return type: static bool
- Signature: mtk_spi_mem_supports_op(struct spi_mem * mem,const struct spi_mem_op * op)
- Line: 920

### mtk_spi_prepare_message
- Return type: static int
- Signature: mtk_spi_prepare_message(struct spi_controller * host,struct spi_message * msg)
- Line: 471

### mtk_spi_prepare_transfer
- Return type: static void
- Signature: mtk_spi_prepare_transfer(struct spi_controller * host,u32 speed_hz)
- Line: 506

### mtk_spi_probe
- Return type: static int
- Signature: mtk_spi_probe(struct platform_device * pdev)
- Line: 1175

### mtk_spi_remove
- Return type: static void
- Signature: mtk_spi_remove(struct platform_device * pdev)
- Line: 1337

### mtk_spi_reset
- Return type: static void
- Signature: mtk_spi_reset(struct mtk_spi * mdata)
- Line: 284

### mtk_spi_resume
- Return type: static int
- Signature: mtk_spi_resume(struct device * dev)
- Line: 1391

### mtk_spi_runtime_resume
- Return type: static int
- Signature: mtk_spi_runtime_resume(struct device * dev)
- Line: 1441

### mtk_spi_runtime_suspend
- Return type: static int
- Signature: mtk_spi_runtime_suspend(struct device * dev)
- Line: 1425

### mtk_spi_set_cs
- Return type: static void
- Signature: mtk_spi_set_cs(struct spi_device * spi,bool enable)
- Line: 486

### mtk_spi_set_hw_cs_timing
- Return type: static int
- Signature: mtk_spi_set_hw_cs_timing(struct spi_device * spi)
- Line: 298

### mtk_spi_set_nbit
- Return type: u32
- Signature: mtk_spi_set_nbit(u32 nbit)
- Line: 566

### mtk_spi_setup
- Return type: static int
- Signature: mtk_spi_setup(struct spi_device * spi)
- Line: 778

### mtk_spi_setup_dma_addr
- Return type: static void
- Signature: mtk_spi_setup_dma_addr(struct spi_controller * host,struct spi_transfer * xfer)
- Line: 638

### mtk_spi_setup_packet
- Return type: static void
- Signature: mtk_spi_setup_packet(struct spi_controller * host)
- Line: 539

### mtk_spi_suspend
- Return type: static int
- Signature: mtk_spi_suspend(struct device * dev)
- Line: 1371

### mtk_spi_transfer_one
- Return type: static int
- Signature: mtk_spi_transfer_one(struct spi_controller * host,struct spi_device * spi,struct spi_transfer * xfer)
- Line: 739

### mtk_spi_transfer_wait
- Return type: static int
- Signature: mtk_spi_transfer_wait(struct spi_mem * mem,const struct spi_mem_op * op)
- Line: 967

### mtk_spi_unprepare_message
- Return type: static int
- Signature: mtk_spi_unprepare_message(struct spi_controller * host,struct spi_message * message)
- Line: 477

### mtk_spi_update_mdata_len
- Return type: static void
- Signature: mtk_spi_update_mdata_len(struct spi_controller * host)
- Line: 610

## Structs (2)

### mtk_spi
- Line: 159
- Members:
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

### mtk_spi_compatible
- Line: 124
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

## Variables (15)

- static **mt2712_compat** : const struct mtk_spi_compatible (line 182)
- static **mt6765_compat** : const struct mtk_spi_compatible (line 192)
- static **mt6893_compat** : const struct mtk_spi_compatible (line 215)
- static **mt6991_compat** : const struct mtk_spi_compatible (line 223)
- static **mt7622_compat** : const struct mtk_spi_compatible (line 199)
- static **mt8173_compat** : const struct mtk_spi_compatible (line 204)
- static **mt8183_compat** : const struct mtk_spi_compatible (line 209)
- static **mtk_common_compat** : const struct mtk_spi_compatible (line 180)
- static **mtk_default_chip_info** : const struct mtk_chip_config (line 235)
- static **mtk_ipm_compat** : const struct mtk_spi_compatible (line 186)
- static **mtk_spi_driver** : platform_driver (line 1484)
- static **mtk_spi_mem_caps** : const struct spi_controller_mem_caps (line 1171)
- static **mtk_spi_mem_ops** : const struct spi_controller_mem_ops (line 1165)
- static **mtk_spi_of_match** : const struct of_device_id[] (line 240)
- static **mtk_spi_pm** : const struct dev_pm_ops (line 1478)

## Macros (74)

- **DMA_ADDR_DEF_BITS** (line 113)
- **DMA_ADDR_EXT_BITS** (line 112)
- **MT8173_SPI_MAX_PAD_SEL** (line 98)
- **MTK_SPI_32BITS_MASK** (line 110)
- **MTK_SPI_IDLE** (line 107)
- **MTK_SPI_IPM_PACKET_LOOP** (line 105)
- **MTK_SPI_IPM_PACKET_SIZE** (line 104)
- **MTK_SPI_MAX_FIFO_SIZE** (line 102)
- **MTK_SPI_PACKET_SIZE** (line 103)
- **MTK_SPI_PAUSED** (line 108)
- **MTK_SPI_PAUSE_INT_STATUS** (line 100)
- **PIN_MODE_CFG**(x) (line 85)
- **SPI_ADJUST_CFG0_CS_HOLD_OFFSET** (line 43)
- **SPI_ADJUST_CFG0_CS_SETUP_OFFSET** (line 44)
- **SPI_CFG0_CS_HOLD_OFFSET** (line 41)
- **SPI_CFG0_CS_SETUP_OFFSET** (line 42)
- **SPI_CFG0_REG** (line 25)
- **SPI_CFG0_SCK_HIGH_OFFSET** (line 39)
- **SPI_CFG0_SCK_LOW_OFFSET** (line 40)
- **SPI_CFG1_CS_IDLE_MASK** (line 55)
- **SPI_CFG1_CS_IDLE_OFFSET** (line 46)
- **SPI_CFG1_GET_TICK_DLY_MASK** (line 52)
- **SPI_CFG1_GET_TICK_DLY_MASK_V1** (line 53)
- **SPI_CFG1_GET_TICK_DLY_OFFSET** (line 49)
- **SPI_CFG1_GET_TICK_DLY_OFFSET_V1** (line 50)
- **SPI_CFG1_IPM_PACKET_LENGTH_MASK** (line 58)
- **SPI_CFG1_PACKET_LENGTH_MASK** (line 57)
- **SPI_CFG1_PACKET_LENGTH_OFFSET** (line 48)
- **SPI_CFG1_PACKET_LOOP_MASK** (line 56)
- **SPI_CFG1_PACKET_LOOP_OFFSET** (line 47)
- **SPI_CFG1_REG** (line 26)
- **SPI_CFG2_REG** (line 34)
- **SPI_CFG2_SCK_HIGH_OFFSET** (line 59)
- **SPI_CFG2_SCK_LOW_OFFSET** (line 60)
- **SPI_CFG3_IPM_ADDR_BYTELEN_MASK** (line 96)
- **SPI_CFG3_IPM_ADDR_BYTELEN_OFFSET** (line 92)
- **SPI_CFG3_IPM_CMD_BYTELEN_MASK** (line 95)
- **SPI_CFG3_IPM_CMD_BYTELEN_OFFSET** (line 91)
- **SPI_CFG3_IPM_CMD_PIN_MODE_MASK** (line 94)
- **SPI_CFG3_IPM_HALF_DUPLEX_DIR** (line 87)
- **SPI_CFG3_IPM_HALF_DUPLEX_EN** (line 88)
- **SPI_CFG3_IPM_NODATA_FLAG** (line 90)
- **SPI_CFG3_IPM_REG** (line 37)
- **SPI_CFG3_IPM_XMODE_EN** (line 89)
- **SPI_CMD_ACT** (line 62)
- **SPI_CMD_CPHA** (line 69)
- **SPI_CMD_CPOL** (line 70)
- **SPI_CMD_CS_POL** (line 68)
- **SPI_CMD_DEASSERT** (line 66)
- **SPI_CMD_FINISH_IE** (line 77)
- **SPI_CMD_IPM_GET_TICKDLY_MASK** (line 83)
- **SPI_CMD_IPM_GET_TICKDLY_OFFSET** (line 81)
- **SPI_CMD_IPM_NONIDLE_MODE** (line 79)
- **SPI_CMD_IPM_SPIM_LOOP** (line 80)
- **SPI_CMD_PAUSE_EN** (line 65)
- **SPI_CMD_PAUSE_IE** (line 78)
- **SPI_CMD_REG** (line 31)
- **SPI_CMD_RESUME** (line 63)
- **SPI_CMD_RST** (line 64)
- **SPI_CMD_RXMSBF** (line 74)
- **SPI_CMD_RX_DMA** (line 71)
- **SPI_CMD_RX_ENDIAN** (line 75)
- **SPI_CMD_SAMPLE_SEL** (line 67)
- **SPI_CMD_TXMSBF** (line 73)
- **SPI_CMD_TX_DMA** (line 72)
- **SPI_CMD_TX_ENDIAN** (line 76)
- **SPI_PAD_SEL_REG** (line 33)
- **SPI_RX_DATA_REG** (line 30)
- **SPI_RX_DST_REG** (line 28)
- **SPI_RX_DST_REG_64** (line 36)
- **SPI_STATUS0_REG** (line 32)
- **SPI_TX_DATA_REG** (line 29)
- **SPI_TX_SRC_REG** (line 27)
- **SPI_TX_SRC_REG_64** (line 35)
