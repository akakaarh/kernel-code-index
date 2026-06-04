# drivers/mmc/host/jz4740_mmc.c

Subsystem: drivers/mmc

## Functions (35)

### jz4740_mmc_acquire_dma_channels
- Return type: static int
- Signature: jz4740_mmc_acquire_dma_channels(struct jz4740_mmc_host * host)
- Line: 228

### jz4740_mmc_clock_disable
- Return type: static void
- Signature: jz4740_mmc_clock_disable(struct jz4740_mmc_host * host)
- Line: 433

### jz4740_mmc_clock_enable
- Return type: static void
- Signature: jz4740_mmc_clock_enable(struct jz4740_mmc_host * host,bool start_transfer)
- Line: 422

### jz4740_mmc_dma_unmap
- Return type: static void
- Signature: jz4740_mmc_dma_unmap(struct jz4740_mmc_host * host,struct mmc_data * data)
- Line: 286

### jz4740_mmc_enable_sdio_irq
- Return type: static void
- Signature: jz4740_mmc_enable_sdio_irq(struct mmc_host * mmc,int enable)
- Line: 995

### jz4740_mmc_get_dma_chan
- Return type: static dma_chan *
- Signature: jz4740_mmc_get_dma_chan(struct jz4740_mmc_host * host,struct mmc_data * data)
- Line: 277

### jz4740_mmc_poll_irq
- Return type: static unsigned int
- Signature: jz4740_mmc_poll_irq(struct jz4740_mmc_host * host,unsigned int irq)
- Line: 470

### jz4740_mmc_post_request
- Return type: static void
- Signature: jz4740_mmc_post_request(struct mmc_host * mmc,struct mmc_request * mrq,int err)
- Line: 388

### jz4740_mmc_pre_request
- Return type: static void
- Signature: jz4740_mmc_pre_request(struct mmc_host * mmc,struct mmc_request * mrq)
- Line: 374

### jz4740_mmc_prepare_dma_data
- Return type: static int
- Signature: jz4740_mmc_prepare_dma_data(struct jz4740_mmc_host * host,struct mmc_data * data,int cookie)
- Line: 299

### jz4740_mmc_probe
- Return type: static int
- Signature: jz4740_mmc_probe(struct platform_device * pdev)
- Line: 1040

### jz4740_mmc_read_data
- Return type: static bool
- Signature: jz4740_mmc_read_data(struct jz4740_mmc_host * host,struct mmc_data * data)
- Line: 571

### jz4740_mmc_read_irq_reg
- Return type: static uint32_t
- Signature: jz4740_mmc_read_irq_reg(struct jz4740_mmc_host * host)
- Line: 207

### jz4740_mmc_read_response
- Return type: static void
- Signature: jz4740_mmc_read_response(struct jz4740_mmc_host * host,struct mmc_command * cmd)
- Line: 656

### jz4740_mmc_release_dma_channels
- Return type: static void
- Signature: jz4740_mmc_release_dma_channels(struct jz4740_mmc_host * host)
- Line: 218

### jz4740_mmc_remove
- Return type: static void
- Signature: jz4740_mmc_remove(struct platform_device * pdev)
- Line: 1150

### jz4740_mmc_request
- Return type: static void
- Signature: jz4740_mmc_request(struct mmc_host * mmc,struct mmc_request * req)
- Line: 924

### jz4740_mmc_request_done
- Return type: static void
- Signature: jz4740_mmc_request_done(struct jz4740_mmc_host * host)
- Line: 456

### jz4740_mmc_reset
- Return type: static void
- Signature: jz4740_mmc_reset(struct jz4740_mmc_host * host)
- Line: 444

### jz4740_mmc_resume
- Return type: static int
- Signature: jz4740_mmc_resume(struct device * dev)
- Line: 1171

### jz4740_mmc_send_command
- Return type: static void
- Signature: jz4740_mmc_send_command(struct jz4740_mmc_host * host,struct mmc_command * cmd)
- Line: 679

### jz4740_mmc_set_clock_rate
- Return type: static int
- Signature: jz4740_mmc_set_clock_rate(struct jz4740_mmc_host * host,int rate)
- Line: 889

### jz4740_mmc_set_ios
- Return type: static void
- Signature: jz4740_mmc_set_ios(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 940

### jz4740_mmc_set_irq_enabled
- Return type: static void
- Signature: jz4740_mmc_set_irq_enabled(struct jz4740_mmc_host * host,unsigned int irq,bool enabled)
- Line: 407

### jz4740_mmc_start_dma_transfer
- Return type: static int
- Signature: jz4740_mmc_start_dma_transfer(struct jz4740_mmc_host * host,struct mmc_data * data)
- Line: 327

### jz4740_mmc_suspend
- Return type: static int
- Signature: jz4740_mmc_suspend(struct device * dev)
- Line: 1166

### jz4740_mmc_timeout
- Return type: static void
- Signature: jz4740_mmc_timeout(struct timer_list * t)
- Line: 642

### jz4740_mmc_transfer_check_state
- Return type: static void
- Signature: jz4740_mmc_transfer_check_state(struct jz4740_mmc_host * host,struct mmc_data * data)
- Line: 491

### jz4740_mmc_write_data
- Return type: static bool
- Signature: jz4740_mmc_write_data(struct jz4740_mmc_host * host,struct mmc_data * data)
- Line: 516

### jz4740_mmc_write_irq_mask
- Return type: static void
- Signature: jz4740_mmc_write_irq_mask(struct jz4740_mmc_host * host,uint32_t val)
- Line: 189

### jz4740_mmc_write_irq_reg
- Return type: static void
- Signature: jz4740_mmc_write_irq_reg(struct jz4740_mmc_host * host,uint32_t val)
- Line: 198

### jz4740_voltage_switch
- Return type: static int
- Signature: jz4740_voltage_switch(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 1001

### jz_mmc_irq
- Return type: static irqreturn_t
- Signature: jz_mmc_irq(int irq,void * devid)
- Line: 840

### jz_mmc_irq_worker
- Return type: static irqreturn_t
- Signature: jz_mmc_irq_worker(int irq,void * devid)
- Line: 757

### jz_mmc_prepare_data_transfer
- Return type: static void
- Signature: jz_mmc_prepare_data_transfer(struct jz4740_mmc_host * host)
- Line: 742

## Structs (1)

### jz4740_mmc_host
- Line: 149
- Members:
  - mmc: mmc_host *
  - pdev: platform_device *
  - clk: clk *
  - version: jz4740_mmc_version
  - irq: int
  - base: void __iomem *
  - mem_res: resource *
  - req: mmc_request *
  - cmd: mmc_command *
  - vqmmc_enabled: bool
  - waiting: unsigned long
  - cmdat: uint32_t
  - irq_mask: uint32_t
  - lock: spinlock_t
  - timeout_timer: timer_list
  - miter: sg_mapping_iter
  - state: jz4740_mmc_state
  - dma_rx: dma_chan *
  - dma_tx: dma_chan *
  - use_dma: bool

## Enums (3)

### jz4740_mmc_state
- Line: 123

### jz4740_mmc_version
- Line: 115

### jz4780_cookie
- Line: 143

## Variables (3)

- static **jz4740_mmc_driver** : platform_driver (line 1179)
- static **jz4740_mmc_of_match** : const struct of_device_id[] (line 1029)
- static **jz4740_mmc_ops** : const struct mmc_host_ops (line 1018)

## Macros (75)

- **JZ4740_MMC_FIFO_HALF_SIZE** (line 186)
- **JZ_MMC_CLK_RATE** (line 112)
- **JZ_MMC_CMDAT_BUSY** (line 87)
- **JZ_MMC_CMDAT_BUS_WIDTH_4BIT** (line 82)
- **JZ_MMC_CMDAT_BUS_WIDTH_8BIT** (line 83)
- **JZ_MMC_CMDAT_BUS_WIDTH_MASK** (line 84)
- **JZ_MMC_CMDAT_DATA_EN** (line 90)
- **JZ_MMC_CMDAT_DMA_EN** (line 85)
- **JZ_MMC_CMDAT_INIT** (line 86)
- **JZ_MMC_CMDAT_IO_ABORT** (line 81)
- **JZ_MMC_CMDAT_RESPONSE_FORMAT** (line 91)
- **JZ_MMC_CMDAT_RSP_R1** (line 92)
- **JZ_MMC_CMDAT_RSP_R2** (line 93)
- **JZ_MMC_CMDAT_RSP_R3** (line 94)
- **JZ_MMC_CMDAT_STREAM** (line 88)
- **JZ_MMC_CMDAT_WRITE** (line 89)
- **JZ_MMC_DMAC_DMA_EN** (line 104)
- **JZ_MMC_DMAC_DMA_SEL** (line 103)
- **JZ_MMC_IRQ_DATA_TRAN_DONE** (line 101)
- **JZ_MMC_IRQ_END_CMD_RES** (line 99)
- **JZ_MMC_IRQ_PRG_DONE** (line 100)
- **JZ_MMC_IRQ_RXFIFO_RD_REQ** (line 98)
- **JZ_MMC_IRQ_SDIO** (line 96)
- **JZ_MMC_IRQ_TXFIFO_WR_REQ** (line 97)
- **JZ_MMC_LPM_DRV_RISING** (line 106)
- **JZ_MMC_LPM_DRV_RISING_1NS_DLY** (line 108)
- **JZ_MMC_LPM_DRV_RISING_QTR_PHASE_DLY** (line 107)
- **JZ_MMC_LPM_LOW_POWER_MODE_EN** (line 110)
- **JZ_MMC_LPM_SMP_RISING_QTR_OR_HALF_PHASE_DLY** (line 109)
- **JZ_MMC_REQ_TIMEOUT_MS** (line 113)
- **JZ_MMC_STATUS_CLK_EN** (line 67)
- **JZ_MMC_STATUS_CRC_READ_ERROR** (line 71)
- **JZ_MMC_STATUS_CRC_RES_ERR** (line 70)
- **JZ_MMC_STATUS_CRC_WRITE_ERROR** (line 73)
- **JZ_MMC_STATUS_DATA_FIFO_AFULL** (line 65)
- **JZ_MMC_STATUS_DATA_FIFO_EMPTY** (line 69)
- **JZ_MMC_STATUS_DATA_FIFO_FULL** (line 68)
- **JZ_MMC_STATUS_DATA_TRAN_DONE** (line 63)
- **JZ_MMC_STATUS_END_CMD_RES** (line 64)
- **JZ_MMC_STATUS_IS_READWAIT** (line 66)
- **JZ_MMC_STATUS_IS_RESETTING** (line 60)
- **JZ_MMC_STATUS_PRG_DONE** (line 62)
- **JZ_MMC_STATUS_READ_ERROR_MASK** (line 77)
- **JZ_MMC_STATUS_SDIO_INT_ACTIVE** (line 61)
- **JZ_MMC_STATUS_TIMEOUT_READ** (line 75)
- **JZ_MMC_STATUS_TIMEOUT_RES** (line 74)
- **JZ_MMC_STATUS_TIMEOUT_WRITE** (line 72)
- **JZ_MMC_STATUS_WRITE_ERROR_MASK** (line 78)
- **JZ_MMC_STRPCL_CLOCK_CONTROL** (line 55)
- **JZ_MMC_STRPCL_CLOCK_START** (line 57)
- **JZ_MMC_STRPCL_CLOCK_STOP** (line 56)
- **JZ_MMC_STRPCL_EXIT_MULTIPLE** (line 49)
- **JZ_MMC_STRPCL_EXIT_TRANSFER** (line 50)
- **JZ_MMC_STRPCL_RESET** (line 53)
- **JZ_MMC_STRPCL_START_OP** (line 54)
- **JZ_MMC_STRPCL_START_READWAIT** (line 51)
- **JZ_MMC_STRPCL_STOP_READWAIT** (line 52)
- **JZ_REG_MMC_ARG** (line 42)
- **JZ_REG_MMC_BLKLEN** (line 36)
- **JZ_REG_MMC_CLKRT** (line 32)
- **JZ_REG_MMC_CMD** (line 41)
- **JZ_REG_MMC_CMDAT** (line 33)
- **JZ_REG_MMC_DMAC** (line 47)
- **JZ_REG_MMC_IMASK** (line 39)
- **JZ_REG_MMC_IREG** (line 40)
- **JZ_REG_MMC_LPM** (line 46)
- **JZ_REG_MMC_NOB** (line 37)
- **JZ_REG_MMC_RDTO** (line 35)
- **JZ_REG_MMC_RESP_FIFO** (line 43)
- **JZ_REG_MMC_RESTO** (line 34)
- **JZ_REG_MMC_RXFIFO** (line 44)
- **JZ_REG_MMC_SNOB** (line 38)
- **JZ_REG_MMC_STATUS** (line 31)
- **JZ_REG_MMC_STRPCL** (line 30)
- **JZ_REG_MMC_TXFIFO** (line 45)
