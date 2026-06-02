# drivers/spi/spi-dw-dma.c

Subsystem: drivers/spi

## Functions (27)

### dw_spi_can_dma
- Return type: static bool
- Signature: dw_spi_can_dma(struct spi_controller * ctlr,struct spi_device * spi,struct spi_transfer * xfer)
- Line: 245

### dw_spi_dma_caps_init
- Return type: static int
- Signature: dw_spi_dma_caps_init(struct dw_spi * dws)
- Line: 75

### dw_spi_dma_chan_filter
- Return type: static bool
- Signature: dw_spi_dma_chan_filter(struct dma_chan * chan,void * param)
- Line: 26

### dw_spi_dma_config_rx
- Return type: static int
- Signature: dw_spi_dma_config_rx(struct dw_spi * dws)
- Line: 425

### dw_spi_dma_config_tx
- Return type: static int
- Signature: dw_spi_dma_config_tx(struct dw_spi * dws)
- Line: 324

### dw_spi_dma_convert_width
- Return type: static dma_slave_buswidth
- Signature: dw_spi_dma_convert_width(u8 n_bytes)
- Line: 231

### dw_spi_dma_exit
- Return type: static void
- Signature: dw_spi_dma_exit(struct dw_spi * dws)
- Line: 209

### dw_spi_dma_init_generic
- Return type: static int
- Signature: dw_spi_dma_init_generic(struct device * dev,struct dw_spi * dws)
- Line: 168

### dw_spi_dma_init_mfld
- Return type: static int
- Signature: dw_spi_dma_init_mfld(struct device * dev,struct dw_spi * dws)
- Line: 111

### dw_spi_dma_maxburst_init
- Return type: static void
- Signature: dw_spi_dma_maxburst_init(struct dw_spi * dws)
- Line: 37

### dw_spi_dma_rx_busy
- Return type: static bool
- Signature: dw_spi_dma_rx_busy(struct dw_spi * dws)
- Line: 367

### dw_spi_dma_rx_done
- Return type: static void
- Signature: dw_spi_dma_rx_done(void * arg)
- Line: 414

### dw_spi_dma_setup
- Return type: static int
- Signature: dw_spi_dma_setup(struct dw_spi * dws,struct spi_transfer * xfer)
- Line: 468

### dw_spi_dma_setup_generic
- Return type: void
- Signature: dw_spi_dma_setup_generic(struct dw_spi * dws)
- Line: 707

### dw_spi_dma_setup_mfld
- Return type: void
- Signature: dw_spi_dma_setup_mfld(struct dw_spi * dws)
- Line: 692

### dw_spi_dma_stop
- Return type: static void
- Signature: dw_spi_dma_stop(struct dw_spi * dws)
- Line: 671

### dw_spi_dma_submit_rx
- Return type: static int
- Signature: dw_spi_dma_submit_rx(struct dw_spi * dws,struct scatterlist * sgl,unsigned int nents)
- Line: 440

### dw_spi_dma_submit_tx
- Return type: static int
- Signature: dw_spi_dma_submit_tx(struct dw_spi * dws,struct scatterlist * sgl,unsigned int nents)
- Line: 339

### dw_spi_dma_transfer
- Return type: static int
- Signature: dw_spi_dma_transfer(struct dw_spi * dws,struct spi_transfer * xfer)
- Line: 638

### dw_spi_dma_transfer_all
- Return type: static int
- Signature: dw_spi_dma_transfer_all(struct dw_spi * dws,struct spi_transfer * xfer)
- Line: 506

### dw_spi_dma_transfer_handler
- Return type: static irqreturn_t
- Signature: dw_spi_dma_transfer_handler(struct dw_spi * dws)
- Line: 222

### dw_spi_dma_transfer_one
- Return type: static int
- Signature: dw_spi_dma_transfer_one(struct dw_spi * dws,struct spi_transfer * xfer)
- Line: 569

### dw_spi_dma_tx_busy
- Return type: static bool
- Signature: dw_spi_dma_tx_busy(struct dw_spi * dws)
- Line: 282

### dw_spi_dma_tx_done
- Return type: static void
- Signature: dw_spi_dma_tx_done(void * arg)
- Line: 313

### dw_spi_dma_wait
- Return type: static int
- Signature: dw_spi_dma_wait(struct dw_spi * dws,unsigned int len,u32 speed)
- Line: 259

### dw_spi_dma_wait_rx_done
- Return type: static int
- Signature: dw_spi_dma_wait_rx_done(struct dw_spi * dws)
- Line: 372

### dw_spi_dma_wait_tx_done
- Return type: static int
- Signature: dw_spi_dma_wait_tx_done(struct dw_spi * dws,struct spi_transfer * xfer)
- Line: 287

## Variables (2)

- static **dw_spi_dma_generic_ops** : const struct dw_spi_dma_ops (line 698)
- static **dw_spi_dma_mfld_ops** : const struct dw_spi_dma_ops (line 683)

## Macros (4)

- **DW_SPI_RX_BURST_LEVEL** (line 22)
- **DW_SPI_RX_BUSY** (line 21)
- **DW_SPI_TX_BURST_LEVEL** (line 24)
- **DW_SPI_TX_BUSY** (line 23)
