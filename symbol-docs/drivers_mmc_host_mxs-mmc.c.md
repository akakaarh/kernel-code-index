# drivers/mmc/host/mxs-mmc.c

Subsystem: drivers/mmc

## Functions (19)

### mxs_mmc_ac
- Return type: static void
- Signature: mxs_mmc_ac(struct mxs_mmc_host * host)
- Line: 282

### mxs_mmc_adtc
- Return type: static void
- Signature: mxs_mmc_adtc(struct mxs_mmc_host * host)
- Line: 343

### mxs_mmc_bc
- Return type: static void
- Signature: mxs_mmc_bc(struct mxs_mmc_host * host)
- Line: 248

### mxs_mmc_dma_irq_callback
- Return type: static void
- Signature: mxs_mmc_dma_irq_callback(void * param)
- Line: 168

### mxs_mmc_enable_sdio_irq
- Return type: static void
- Signature: mxs_mmc_enable_sdio_irq(struct mmc_host * mmc,int enable)
- Line: 509

### mxs_mmc_get_cd
- Return type: static int
- Signature: mxs_mmc_get_cd(struct mmc_host * mmc)
- Line: 61

### mxs_mmc_irq_handler
- Return type: static irqreturn_t
- Signature: mxs_mmc_irq_handler(int irq,void * dev_id)
- Line: 175

### mxs_mmc_prep_dma
- Return type: static dma_async_tx_descriptor *
- Signature: mxs_mmc_prep_dma(struct mxs_mmc_host * host,unsigned long flags)
- Line: 213

### mxs_mmc_probe
- Return type: static int
- Signature: mxs_mmc_probe(struct platform_device * pdev)
- Line: 559

### mxs_mmc_regulator_disable
- Return type: static void
- Signature: mxs_mmc_regulator_disable(void * regulator)
- Line: 554

### mxs_mmc_remove
- Return type: static void
- Signature: mxs_mmc_remove(struct platform_device * pdev)
- Line: 669

### mxs_mmc_request
- Return type: static void
- Signature: mxs_mmc_request(struct mmc_host * mmc,struct mmc_request * mrq)
- Line: 481

### mxs_mmc_request_done
- Return type: static void
- Signature: mxs_mmc_request_done(struct mxs_mmc_host * host)
- Line: 123

### mxs_mmc_reset
- Return type: static int
- Signature: mxs_mmc_reset(struct mxs_mmc_host * host)
- Line: 84

### mxs_mmc_resume
- Return type: static int
- Signature: mxs_mmc_resume(struct device * dev)
- Line: 693

### mxs_mmc_set_ios
- Return type: static void
- Signature: mxs_mmc_set_ios(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 494

### mxs_mmc_start_cmd
- Return type: static void
- Signature: mxs_mmc_start_cmd(struct mxs_mmc_host * host,struct mmc_command * cmd)
- Line: 456

### mxs_mmc_suspend
- Return type: static int
- Signature: mxs_mmc_suspend(struct device * dev)
- Line: 683

### mxs_ns_to_ssp_ticks
- Return type: static unsigned short
- Signature: mxs_ns_to_ssp_ticks(unsigned clock_rate,unsigned ns)
- Line: 327

## Structs (1)

### mxs_mmc_host
- Line: 47
- Members:
  - ssp: mxs_ssp
  - mmc: mmc_host *
  - mrq: mmc_request *
  - cmd: mmc_command *
  - data: mmc_data *
  - bus_width: unsigned char
  - lock: spinlock_t
  - sdio_irq_en: int
  - broken_cd: bool

## Variables (3)

- static **mxs_mmc_driver** : platform_driver (line 704)
- static **mxs_mmc_dt_ids** : const struct of_device_id[] (line 547)
- static **mxs_mmc_ops** : const struct mmc_host_ops (line 539)

## Macros (3)

- **DRIVER_NAME** (line 33)
- **MXS_MMC_DETECT_TIMEOUT** (line 45)
- **MXS_MMC_IRQ_BITS** (line 35)
