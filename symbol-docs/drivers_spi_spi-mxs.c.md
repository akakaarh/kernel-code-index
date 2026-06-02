# drivers/spi/spi-mxs.c

Subsystem: drivers/spi

## Functions (14)

### mxs_spi_cs_to_reg
- Return type: static u32
- Signature: mxs_spi_cs_to_reg(unsigned cs)
- Line: 105

### mxs_spi_probe
- Return type: static int
- Signature: mxs_spi_probe(struct platform_device * pdev)
- Line: 528

### mxs_spi_remove
- Return type: static void
- Signature: mxs_spi_remove(struct platform_device * pdev)
- Line: 643

### mxs_spi_resume
- Return type: static int
- Signature: mxs_spi_resume(struct device * dev)
- Line: 497

### mxs_spi_runtime_resume
- Return type: static int
- Signature: mxs_spi_runtime_resume(struct device * dev)
- Line: 464

### mxs_spi_runtime_suspend
- Return type: static int
- Signature: mxs_spi_runtime_suspend(struct device * dev)
- Line: 443

### mxs_spi_setup_transfer
- Return type: static int
- Signature: mxs_spi_setup_transfer(struct spi_device * dev,const struct spi_transfer * t)
- Line: 64

### mxs_spi_suspend
- Return type: static int
- Signature: mxs_spi_suspend(struct device * dev)
- Line: 482

### mxs_spi_transfer_one
- Return type: static int
- Signature: mxs_spi_transfer_one(struct spi_controller * host,struct spi_message * m)
- Line: 361

### mxs_spi_txrx_dma
- Return type: static int
- Signature: mxs_spi_txrx_dma(struct mxs_spi * spi,unsigned char * buf,int len,unsigned int flags)
- Line: 164

### mxs_spi_txrx_pio
- Return type: static int
- Signature: mxs_spi_txrx_pio(struct mxs_spi * spi,unsigned char * buf,int len,unsigned int flags)
- Line: 299

### mxs_ssp_dma_irq_callback
- Return type: static void
- Signature: mxs_ssp_dma_irq_callback(void * param)
- Line: 146

### mxs_ssp_irq_handler
- Return type: static irqreturn_t
- Signature: mxs_ssp_irq_handler(int irq,void * dev_id)
- Line: 153

### mxs_ssp_wait
- Return type: static int
- Signature: mxs_ssp_wait(struct mxs_spi * spi,int offset,int mask,bool set)
- Line: 125

## Structs (2)

### __anon45e5e35a0108
- Line: 177
- Members:
  - ssp: mxs_ssp
  - c: completion
  - sck: unsigned int
  - pio: u32[4]
  - sg: scatterlist

### mxs_spi
- Line: 58
- Members:
  - ssp: mxs_ssp
  - c: completion
  - sck: unsigned int
  - pio: u32[4]
  - sg: scatterlist

## Variables (3)

- static **mxs_spi_driver** : platform_driver (line 666)
- static **mxs_spi_dt_ids** : const struct of_device_id[] (line 521)
- static **mxs_spi_pm** : const struct dev_pm_ops (line 516)

## Macros (5)

- **DRIVER_NAME** (line 44)
- **SG_MAXLEN** (line 49)
- **SSP_TIMEOUT** (line 47)
- **TXRX_DEASSERT_CS** (line 56)
- **TXRX_WRITE** (line 55)
