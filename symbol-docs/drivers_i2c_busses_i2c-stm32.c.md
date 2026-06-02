# drivers/i2c/busses/i2c-stm32.c

Subsystem: drivers/i2c

## Functions (3)

### stm32_i2c_dma_free
- Return type: void
- Signature: stm32_i2c_dma_free(struct stm32_i2c_dma * dma)
- Line: 84

### stm32_i2c_dma_request
- Return type: stm32_i2c_dma *
- Signature: stm32_i2c_dma_request(struct device * dev,dma_addr_t phy_addr,u32 txdr_offset,u32 rxdr_offset)
- Line: 12

### stm32_i2c_prep_dma_xfer
- Return type: int
- Signature: stm32_i2c_prep_dma_xfer(struct device * dev,struct stm32_i2c_dma * dma,bool rd_wr,u32 len,u8 * buf,dma_async_tx_callback callback,void * dma_async_param)
- Line: 98
