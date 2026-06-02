# drivers/spi/spi-pxa2xx-dma.c

Subsystem: drivers/spi

## Functions (9)

### pxa2xx_spi_dma_callback
- Return type: static void
- Signature: pxa2xx_spi_dma_callback(void * data)
- Line: 61

### pxa2xx_spi_dma_prepare
- Return type: int
- Signature: pxa2xx_spi_dma_prepare(struct driver_data * drv_data,struct spi_transfer * xfer)
- Line: 136

### pxa2xx_spi_dma_prepare_one
- Return type: static dma_async_tx_descriptor *
- Signature: pxa2xx_spi_dma_prepare_one(struct driver_data * drv_data,enum dma_transfer_direction dir,struct spi_transfer * xfer)
- Line: 67

### pxa2xx_spi_dma_release
- Return type: void
- Signature: pxa2xx_spi_dma_release(struct driver_data * drv_data)
- Line: 211

### pxa2xx_spi_dma_setup
- Return type: int
- Signature: pxa2xx_spi_dma_setup(struct driver_data * drv_data)
- Line: 185

### pxa2xx_spi_dma_start
- Return type: void
- Signature: pxa2xx_spi_dma_start(struct driver_data * drv_data)
- Line: 170

### pxa2xx_spi_dma_stop
- Return type: void
- Signature: pxa2xx_spi_dma_stop(struct driver_data * drv_data)
- Line: 178

### pxa2xx_spi_dma_transfer
- Return type: irqreturn_t
- Signature: pxa2xx_spi_dma_transfer(struct driver_data * drv_data)
- Line: 118

### pxa2xx_spi_dma_transfer_complete
- Return type: static void
- Signature: pxa2xx_spi_dma_transfer_complete(struct driver_data * drv_data,bool error)
- Line: 25
