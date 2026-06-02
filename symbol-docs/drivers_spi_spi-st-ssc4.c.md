# drivers/spi/spi-st-ssc4.c

Subsystem: drivers/spi

## Functions (11)

### spi_st_irq
- Return type: static irqreturn_t
- Signature: spi_st_irq(int irq,void * dev_id)
- Line: 250

### spi_st_probe
- Return type: static int
- Signature: spi_st_probe(struct platform_device * pdev)
- Line: 274

### spi_st_remove
- Return type: static void
- Signature: spi_st_remove(struct platform_device * pdev)
- Line: 369

### spi_st_resume
- Return type: static int
- Signature: spi_st_resume(struct device * dev)
- Line: 424

### spi_st_runtime_resume
- Return type: static int
- Signature: spi_st_runtime_resume(struct device * dev)
- Line: 400

### spi_st_runtime_suspend
- Return type: static int
- Signature: spi_st_runtime_suspend(struct device * dev)
- Line: 387

### spi_st_setup
- Return type: static int
- Signature: spi_st_setup(struct spi_device * spi)
- Line: 175

### spi_st_suspend
- Return type: static int
- Signature: spi_st_suspend(struct device * dev)
- Line: 412

### spi_st_transfer_one
- Return type: static int
- Signature: spi_st_transfer_one(struct spi_controller * host,struct spi_device * spi,struct spi_transfer * t)
- Line: 118

### ssc_read_rx_fifo
- Return type: static void
- Signature: ssc_read_rx_fifo(struct spi_st * spi_st)
- Line: 93

### ssc_write_tx_fifo
- Return type: static void
- Signature: ssc_write_tx_fifo(struct spi_st * spi_st)
- Line: 69

## Structs (1)

### spi_st
- Line: 53
- Members:
  - base: void __iomem *
  - clk: clk *
  - dev: device *
  - tx_ptr: const u8 *
  - rx_ptr: u8 *
  - bytes_per_word: u16
  - words_remaining: unsigned int
  - baud: unsigned int
  - done: completion

## Variables (3)

- static **spi_st_driver** : platform_driver (line 447)
- static **spi_st_pm** : const struct dev_pm_ops (line 436)
- static **stm_spi_match** : const struct of_device_id[] (line 441)

## Macros (22)

- **FIFO_SIZE** (line 51)
- **MODEBITS** (line 174)
- **SSC_BRG** (line 26)
- **SSC_CTL** (line 29)
- **SSC_CTL_BM** (line 36)
- **SSC_CTL_DATA_WIDTH_9** (line 34)
- **SSC_CTL_DATA_WIDTH_MSK** (line 35)
- **SSC_CTL_EN** (line 42)
- **SSC_CTL_EN_CLST_RX** (line 46)
- **SSC_CTL_EN_RX_FIFO** (line 45)
- **SSC_CTL_EN_TX_FIFO** (line 44)
- **SSC_CTL_HB** (line 37)
- **SSC_CTL_LPB** (line 43)
- **SSC_CTL_MS** (line 41)
- **SSC_CTL_PH** (line 38)
- **SSC_CTL_PO** (line 39)
- **SSC_CTL_SR** (line 40)
- **SSC_I2C** (line 31)
- **SSC_IEN** (line 30)
- **SSC_IEN_TEEN** (line 49)
- **SSC_RBUF** (line 28)
- **SSC_TBUF** (line 27)
