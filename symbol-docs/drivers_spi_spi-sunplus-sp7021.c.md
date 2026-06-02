# drivers/spi/spi-sunplus-sp7021.c

Subsystem: drivers/spi

## Functions (19)

### sp7021_prep_transfer
- Return type: static void
- Signature: sp7021_prep_transfer(struct spi_controller * ctlr,struct spi_device * spi)
- Line: 241

### sp7021_spi_controller_prepare_message
- Return type: static int
- Signature: sp7021_spi_controller_prepare_message(struct spi_controller * ctlr,struct spi_message * msg)
- Line: 251

### sp7021_spi_controller_probe
- Return type: static int
- Signature: sp7021_spi_controller_probe(struct platform_device * pdev)
- Line: 397

### sp7021_spi_controller_remove
- Return type: static void
- Signature: sp7021_spi_controller_remove(struct platform_device * pdev)
- Line: 493

### sp7021_spi_controller_resume
- Return type: static int __maybe_unused
- Signature: sp7021_spi_controller_resume(struct device * dev)
- Line: 510

### sp7021_spi_controller_suspend
- Return type: static int __maybe_unused
- Signature: sp7021_spi_controller_suspend(struct device * dev)
- Line: 502

### sp7021_spi_host_irq
- Return type: static irqreturn_t
- Signature: sp7021_spi_host_irq(int irq,void * dev)
- Line: 180

### sp7021_spi_host_rb
- Return type: static void
- Signature: sp7021_spi_host_rb(struct sp7021_spi_ctlr * pspim,unsigned int len)
- Line: 158

### sp7021_spi_host_transfer_one
- Return type: static int
- Signature: sp7021_spi_host_transfer_one(struct spi_controller * ctlr,struct spi_device * spi,struct spi_transfer * xfer)
- Line: 298

### sp7021_spi_host_wb
- Return type: static void
- Signature: sp7021_spi_host_wb(struct sp7021_spi_ctlr * pspim,unsigned int len)
- Line: 169

### sp7021_spi_reset_control_assert
- Return type: static void
- Signature: sp7021_spi_reset_control_assert(void * data)
- Line: 392

### sp7021_spi_runtime_resume
- Return type: static int
- Signature: sp7021_spi_runtime_resume(struct device * dev)
- Line: 528

### sp7021_spi_runtime_suspend
- Return type: static int
- Signature: sp7021_spi_runtime_suspend(struct device * dev)
- Line: 520

### sp7021_spi_setup_clk
- Return type: static void
- Signature: sp7021_spi_setup_clk(struct spi_controller * ctlr,struct spi_transfer * xfer)
- Line: 284

### sp7021_spi_target_abort
- Return type: static int
- Signature: sp7021_spi_target_abort(struct spi_controller * ctlr)
- Line: 111

### sp7021_spi_target_irq
- Return type: static irqreturn_t
- Signature: sp7021_spi_target_irq(int irq,void * dev)
- Line: 99

### sp7021_spi_target_rx
- Return type: static int
- Signature: sp7021_spi_target_rx(struct spi_device * spi,struct spi_transfer * xfer)
- Line: 140

### sp7021_spi_target_transfer_one
- Return type: static int
- Signature: sp7021_spi_target_transfer_one(struct spi_controller * ctlr,struct spi_device * spi,struct spi_transfer * xfer)
- Line: 362

### sp7021_spi_target_tx
- Return type: static int
- Signature: sp7021_spi_target_tx(struct spi_device * spi,struct spi_transfer * xfer)
- Line: 120

## Structs (1)

### sp7021_spi_ctlr
- Line: 77
- Members:
  - dev: device *
  - ctlr: spi_controller *
  - m_base: void __iomem *
  - s_base: void __iomem *
  - xfer_conf: u32
  - mode: int
  - m_irq: int
  - s_irq: int
  - spi_clk: clk *
  - rstc: reset_control *
  - buf_lock: mutex
  - isr_done: completion
  - target_isr: completion
  - rx_cur_len: unsigned int
  - tx_cur_len: unsigned int
  - data_unit: unsigned int
  - tx_buf: const u8 *
  - rx_buf: u8 *

## Enums (1)

### __anona52ebc560103
- Line: 72

## Variables (3)

- static **sp7021_spi_controller_driver** : platform_driver (line 550)
- static **sp7021_spi_controller_ids** : const struct of_device_id[] (line 544)
- static **sp7021_spi_pm_ops** : const struct dev_pm_ops (line 537)

## Macros (46)

- **SP7021_CLEAN_FLUG_MASK** (line 63)
- **SP7021_CLEAN_RW_BYTE** (line 62)
- **SP7021_CLK_MASK** (line 64)
- **SP7021_CLR_MASTER_INT** (line 67)
- **SP7021_CPHA_R** (line 51)
- **SP7021_CPHA_W** (line 52)
- **SP7021_CPOL_FD** (line 50)
- **SP7021_CS_POR** (line 54)
- **SP7021_DATA_RDY_REG** (line 17)
- **SP7021_DMA_CTRL_REG** (line 34)
- **SP7021_FD_SEL** (line 55)
- **SP7021_FD_SW_RST** (line 37)
- **SP7021_FIFO_DATA_LEN** (line 70)
- **SP7021_FIFO_REG** (line 30)
- **SP7021_FINISH_FLAG** (line 41)
- **SP7021_FINISH_FLAG_MASK** (line 61)
- **SP7021_GET_LEN_MASK** (line 46)
- **SP7021_INT_BUSY_REG** (line 33)
- **SP7021_INT_BYPASS** (line 66)
- **SP7021_LSB_SEL** (line 53)
- **SP7021_RX_CNT_MASK** (line 44)
- **SP7021_RX_EMP_FLAG** (line 39)
- **SP7021_RX_FULL_FLAG** (line 40)
- **SP7021_RX_FULL_FLAG_MASK** (line 60)
- **SP7021_RX_UNIT** (line 57)
- **SP7021_SET_TX_LEN** (line 47)
- **SP7021_SET_XFER_LEN** (line 48)
- **SP7021_SLAVE_CLR_INT** (line 25)
- **SP7021_SLAVE_DATA_RDY** (line 22)
- **SP7021_SLAVE_DMA_ADDR_REG** (line 20)
- **SP7021_SLAVE_DMA_CMD** (line 28)
- **SP7021_SLAVE_DMA_CTRL_REG** (line 18)
- **SP7021_SLAVE_DMA_EN** (line 26)
- **SP7021_SLAVE_DMA_LENGTH_REG** (line 19)
- **SP7021_SLAVE_DMA_RW** (line 27)
- **SP7021_SLAVE_SW_RST** (line 23)
- **SP7021_SLA_DMA_W_INT** (line 24)
- **SP7021_SPI_CONFIG_REG** (line 32)
- **SP7021_SPI_DATA_SIZE** (line 69)
- **SP7021_SPI_START_FD** (line 36)
- **SP7021_SPI_STATUS_REG** (line 31)
- **SP7021_TX_CNT_MASK** (line 43)
- **SP7021_TX_EMP_FLAG** (line 38)
- **SP7021_TX_EMP_FLAG_MASK** (line 59)
- **SP7021_TX_LEN_MASK** (line 45)
- **SP7021_TX_UNIT** (line 58)
