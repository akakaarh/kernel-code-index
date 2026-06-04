# drivers/mmc/host/loongson2-mmc.c

Subsystem: drivers/mmc

## Functions (27)

### loongson2_mmc_ack_sdio_irq
- Return type: static void
- Signature: loongson2_mmc_ack_sdio_irq(struct mmc_host * mmc)
- Line: 596

### loongson2_mmc_dll_mode_init
- Return type: static void
- Signature: loongson2_mmc_dll_mode_init(struct loongson2_mmc_host * host)
- Line: 493

### loongson2_mmc_enable_sdio_irq
- Return type: static void
- Signature: loongson2_mmc_enable_sdio_irq(struct mmc_host * mmc,int enable)
- Line: 589

### loongson2_mmc_irq
- Return type: static irqreturn_t
- Signature: loongson2_mmc_irq(int irq,void * devid)
- Line: 413

### loongson2_mmc_irq_worker
- Return type: static irqreturn_t
- Signature: loongson2_mmc_irq_worker(int irq,void * devid)
- Line: 360

### loongson2_mmc_prepare_dma
- Return type: static int
- Signature: loongson2_mmc_prepare_dma(struct loongson2_mmc_host * host,struct mmc_data * data)
- Line: 315

### loongson2_mmc_prepare_external_dma
- Return type: static int
- Signature: loongson2_mmc_prepare_external_dma(struct loongson2_mmc_host * host,struct mmc_data * data)
- Line: 653

### loongson2_mmc_prepare_internal_dma
- Return type: static int
- Signature: loongson2_mmc_prepare_internal_dma(struct loongson2_mmc_host * host,struct mmc_data * data)
- Line: 785

### loongson2_mmc_probe
- Return type: static int
- Signature: loongson2_mmc_probe(struct platform_device * pdev)
- Line: 940

### loongson2_mmc_release_external_dma
- Return type: static void
- Signature: loongson2_mmc_release_external_dma(struct loongson2_mmc_host * host,struct device * dev)
- Line: 689

### loongson2_mmc_release_internal_dma
- Return type: static void
- Signature: loongson2_mmc_release_internal_dma(struct loongson2_mmc_host * host,struct device * dev)
- Line: 849

### loongson2_mmc_remove
- Return type: static void
- Signature: loongson2_mmc_remove(struct platform_device * pdev)
- Line: 1003

### loongson2_mmc_request
- Return type: static void
- Signature: loongson2_mmc_request(struct mmc_host * mmc,struct mmc_request * mrq)
- Line: 574

### loongson2_mmc_resource_request
- Return type: static int
- Signature: loongson2_mmc_resource_request(struct platform_device * pdev,struct loongson2_mmc_host * host)
- Line: 893

### loongson2_mmc_resume
- Return type: static int
- Signature: loongson2_mmc_resume(struct device * dev)
- Line: 1031

### loongson2_mmc_send_command
- Return type: static void
- Signature: loongson2_mmc_send_command(struct loongson2_mmc_host * host,struct mmc_command * cmd)
- Line: 263

### loongson2_mmc_send_request
- Return type: static void
- Signature: loongson2_mmc_send_request(struct mmc_host * mmc)
- Line: 332

### loongson2_mmc_set_clk
- Return type: static void
- Signature: loongson2_mmc_set_clk(struct loongson2_mmc_host * host,struct mmc_ios * ios)
- Line: 525

### loongson2_mmc_set_ios
- Return type: static void
- Signature: loongson2_mmc_set_ios(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 543

### loongson2_mmc_setup_data
- Return type: static int
- Signature: loongson2_mmc_setup_data(struct loongson2_mmc_host * host,struct mmc_data * data)
- Line: 292

### loongson2_mmc_suspend
- Return type: static int
- Signature: loongson2_mmc_suspend(struct device * dev)
- Line: 1021

### ls2k0500_mmc_reorder_cmd_data
- Return type: static void
- Signature: ls2k0500_mmc_reorder_cmd_data(struct loongson2_mmc_host * host,struct mmc_command * cmd)
- Line: 626

### ls2k0500_mmc_set_external_dma
- Return type: static int
- Signature: ls2k0500_mmc_set_external_dma(struct loongson2_mmc_host * host,struct platform_device * pdev)
- Line: 695

### ls2k1000_mmc_set_external_dma
- Return type: static int
- Signature: ls2k1000_mmc_set_external_dma(struct loongson2_mmc_host * host,struct platform_device * pdev)
- Line: 719

### ls2k2000_mmc_fix_data_timeout
- Return type: static void
- Signature: ls2k2000_mmc_fix_data_timeout(struct loongson2_mmc_host * host,struct mmc_command * cmd)
- Line: 772

### ls2k2000_mmc_reorder_cmd_data
- Return type: static void
- Signature: ls2k2000_mmc_reorder_cmd_data(struct loongson2_mmc_host * host,struct mmc_command * cmd)
- Line: 750

### ls2k2000_mmc_set_internal_dma
- Return type: static int
- Signature: ls2k2000_mmc_set_internal_dma(struct loongson2_mmc_host * host,struct platform_device * pdev)
- Line: 838

## Structs (3)

### loongson2_dma_desc
- Line: 221
- Members:
  - ndesc_addr: u32
  - mem_addr: u32
  - apb_addr: u32
  - len: u32
  - step_len: u32
  - step_times: u32
  - cmd: u32
  - stats: u32
  - high_ndesc_addr: u32
  - high_mem_addr: u32
  - reserved: u32[2]
  - dev: device *
  - mrq: mmc_request *
  - regmap: regmap *
  - res: resource *
  - clk: clk *
  - current_clk: u32
  - sg_cpu: void *
  - sg_dma: dma_addr_t
  - dma_complete: int
  - chan: dma_chan *
  - cmd_is_stop: int
  - bus_width: int
  - lock: spinlock_t
  - state: loongson2_mmc_state
  - pdata: const struct loongson2_mmc_pdata *
  - flags: u32
  - regmap_config: const struct regmap_config *
  - reorder_cmd_data: void (*)(struct loongson2_mmc_host * host,struct mmc_command * cmd)
  - fix_data_timeout: void (*)(struct loongson2_mmc_host * host,struct mmc_command * cmd)
  - setting_dma: int (*)(struct loongson2_mmc_host * host,struct platform_device * pdev)
  - prepare_dma: int (*)(struct loongson2_mmc_host * host,struct mmc_data * data)
  - release_dma: void (*)(struct loongson2_mmc_host * host,struct device * dev)

### loongson2_mmc_host
- Line: 235
- Members:
  - ndesc_addr: u32
  - mem_addr: u32
  - apb_addr: u32
  - len: u32
  - step_len: u32
  - step_times: u32
  - cmd: u32
  - stats: u32
  - high_ndesc_addr: u32
  - high_mem_addr: u32
  - reserved: u32[2]
  - dev: device *
  - mrq: mmc_request *
  - regmap: regmap *
  - res: resource *
  - clk: clk *
  - current_clk: u32
  - sg_cpu: void *
  - sg_dma: dma_addr_t
  - dma_complete: int
  - chan: dma_chan *
  - cmd_is_stop: int
  - bus_width: int
  - lock: spinlock_t
  - state: loongson2_mmc_state
  - pdata: const struct loongson2_mmc_pdata *
  - flags: u32
  - regmap_config: const struct regmap_config *
  - reorder_cmd_data: void (*)(struct loongson2_mmc_host * host,struct mmc_command * cmd)
  - fix_data_timeout: void (*)(struct loongson2_mmc_host * host,struct mmc_command * cmd)
  - setting_dma: int (*)(struct loongson2_mmc_host * host,struct platform_device * pdev)
  - prepare_dma: int (*)(struct loongson2_mmc_host * host,struct mmc_data * data)
  - release_dma: void (*)(struct loongson2_mmc_host * host,struct device * dev)

### loongson2_mmc_pdata
- Line: 253
- Members:
  - ndesc_addr: u32
  - mem_addr: u32
  - apb_addr: u32
  - len: u32
  - step_len: u32
  - step_times: u32
  - cmd: u32
  - stats: u32
  - high_ndesc_addr: u32
  - high_mem_addr: u32
  - reserved: u32[2]
  - dev: device *
  - mrq: mmc_request *
  - regmap: regmap *
  - res: resource *
  - clk: clk *
  - current_clk: u32
  - sg_cpu: void *
  - sg_dma: dma_addr_t
  - dma_complete: int
  - chan: dma_chan *
  - cmd_is_stop: int
  - bus_width: int
  - lock: spinlock_t
  - state: loongson2_mmc_state
  - pdata: const struct loongson2_mmc_pdata *
  - flags: u32
  - regmap_config: const struct regmap_config *
  - reorder_cmd_data: void (*)(struct loongson2_mmc_host * host,struct mmc_command * cmd)
  - fix_data_timeout: void (*)(struct loongson2_mmc_host * host,struct mmc_command * cmd)
  - setting_dma: int (*)(struct loongson2_mmc_host * host,struct platform_device * pdev)
  - prepare_dma: int (*)(struct loongson2_mmc_host * host,struct mmc_data * data)
  - release_dma: void (*)(struct loongson2_mmc_host * host,struct device * dev)

## Enums (1)

### loongson2_mmc_state
- Line: 212

## Variables (11)

- **__packed** : loongson2_dma_desc (line 233)
- static **loongson2_mmc_driver** : platform_driver (line 1041)
- static **loongson2_mmc_of_ids** : const struct of_device_id[] (line 1012)
- static **loongson2_mmc_ops** : mmc_host_ops (line 601)
- static **loongson2_reorder_cmd_list** : int[] (line 617)
- static **ls2k0300_mmc_pdata** : loongson2_mmc_pdata (line 855)
- static **ls2k0500_mmc_pdata** : loongson2_mmc_pdata (line 865)
- static **ls2k0500_mmc_regmap_config** : const struct regmap_config (line 610)
- static **ls2k1000_mmc_pdata** : loongson2_mmc_pdata (line 874)
- static **ls2k2000_mmc_pdata** : loongson2_mmc_pdata (line 883)
- static **ls2k2000_mmc_regmap_config** : const struct regmap_config (line 743)

## Macros (130)

- **LOONGSON2_MMC_BSIZE** (line 93)
- **LOONGSON2_MMC_CCTL_ABORT** (line 74)
- **LOONGSON2_MMC_CCTL_CHECK** (line 75)
- **LOONGSON2_MMC_CCTL_CMD6** (line 77)
- **LOONGSON2_MMC_CCTL_HOST** (line 70)
- **LOONGSON2_MMC_CCTL_INDEX** (line 69)
- **LOONGSON2_MMC_CCTL_LONG_RSP** (line 73)
- **LOONGSON2_MMC_CCTL_SDIO** (line 76)
- **LOONGSON2_MMC_CCTL_START** (line 71)
- **LOONGSON2_MMC_CCTL_WAIT_RSP** (line 72)
- **LOONGSON2_MMC_CMD48_QUIRK** (line 196)
- **LOONGSON2_MMC_CSTS_AUTO_STOP** (line 86)
- **LOONGSON2_MMC_CSTS_CRC_ERR** (line 85)
- **LOONGSON2_MMC_CSTS_END** (line 84)
- **LOONGSON2_MMC_CSTS_FIN** (line 87)
- **LOONGSON2_MMC_CSTS_INDEX** (line 80)
- **LOONGSON2_MMC_CSTS_ON** (line 81)
- **LOONGSON2_MMC_CSTS_RSP** (line 82)
- **LOONGSON2_MMC_CSTS_TIMEOUT** (line 83)
- **LOONGSON2_MMC_CTL_ENCLK** (line 60)
- **LOONGSON2_MMC_CTL_EXTCLK** (line 61)
- **LOONGSON2_MMC_CTL_RESET** (line 62)
- **LOONGSON2_MMC_DCNT_BNUM** (line 107)
- **LOONGSON2_MMC_DCNT_BYTE** (line 108)
- **LOONGSON2_MMC_DCTL_8BIT_BUS** (line 104)
- **LOONGSON2_MMC_DCTL_BNUM** (line 96)
- **LOONGSON2_MMC_DCTL_ENDMA** (line 98)
- **LOONGSON2_MMC_DCTL_IO_RESUME** (line 102)
- **LOONGSON2_MMC_DCTL_IO_SUSPEND** (line 101)
- **LOONGSON2_MMC_DCTL_RWAIT** (line 100)
- **LOONGSON2_MMC_DCTL_RW_RESUME** (line 103)
- **LOONGSON2_MMC_DCTL_START** (line 97)
- **LOONGSON2_MMC_DCTL_WIDE** (line 99)
- **LOONGSON2_MMC_DELAY_PAD** (line 165)
- **LOONGSON2_MMC_DELAY_RD** (line 166)
- **LOONGSON2_MMC_DLLCTL_CLK_MODE** (line 161)
- **LOONGSON2_MMC_DLLCTL_INCRE** (line 159)
- **LOONGSON2_MMC_DLLCTL_START** (line 160)
- **LOONGSON2_MMC_DLLCTL_START_BIT** (line 162)
- **LOONGSON2_MMC_DLLCTL_TIME** (line 158)
- **LOONGSON2_MMC_DLLCTL_TIME_BPASS** (line 163)
- **LOONGSON2_MMC_DLLVAL_DONE** (line 155)
- **LOONGSON2_MMC_DLLVAL_TIMEOUT_US** (line 189)
- **LOONGSON2_MMC_DMA_64BIT_EN** (line 174)
- **LOONGSON2_MMC_DMA_ASK_VALID** (line 176)
- **LOONGSON2_MMC_DMA_CONFIG_MASK** (line 179)
- **LOONGSON2_MMC_DMA_DATA_DIR** (line 187)
- **LOONGSON2_MMC_DMA_DESC_ADDR_LOW** (line 183)
- **LOONGSON2_MMC_DMA_DESC_EN** (line 182)
- **LOONGSON2_MMC_DMA_INT** (line 186)
- **LOONGSON2_MMC_DMA_START** (line 177)
- **LOONGSON2_MMC_DMA_STOP** (line 178)
- **LOONGSON2_MMC_DMA_UNCOHERENT_EN** (line 175)
- **LOONGSON2_MMC_DSTS_BUSYFIN** (line 114)
- **LOONGSON2_MMC_DSTS_DTIMEOUT** (line 116)
- **LOONGSON2_MMC_DSTS_IRQ** (line 119)
- **LOONGSON2_MMC_DSTS_RESUME** (line 121)
- **LOONGSON2_MMC_DSTS_RXCRC** (line 117)
- **LOONGSON2_MMC_DSTS_RXON** (line 111)
- **LOONGSON2_MMC_DSTS_SBITERR** (line 113)
- **LOONGSON2_MMC_DSTS_START** (line 120)
- **LOONGSON2_MMC_DSTS_SUSPEND** (line 122)
- **LOONGSON2_MMC_DSTS_TXCRC** (line 118)
- **LOONGSON2_MMC_DSTS_TXON** (line 112)
- **LOONGSON2_MMC_DSTS_XFERFIN** (line 115)
- **LOONGSON2_MMC_DTIMR** (line 90)
- **LOONGSON2_MMC_FSTS_TXFULL** (line 125)
- **LOONGSON2_MMC_IEN_ALL** (line 151)
- **LOONGSON2_MMC_IEN_BUSYEND** (line 149)
- **LOONGSON2_MMC_IEN_CSENT** (line 146)
- **LOONGSON2_MMC_IEN_CTIMEOUT** (line 147)
- **LOONGSON2_MMC_IEN_DFIN** (line 140)
- **LOONGSON2_MMC_IEN_DTIMEOUT** (line 141)
- **LOONGSON2_MMC_IEN_PROGERR** (line 144)
- **LOONGSON2_MMC_IEN_RESPCRC** (line 148)
- **LOONGSON2_MMC_IEN_RXCRC** (line 142)
- **LOONGSON2_MMC_IEN_SDIOIRQ** (line 145)
- **LOONGSON2_MMC_IEN_TXCRC** (line 143)
- **LOONGSON2_MMC_INT_BUSYEND** (line 137)
- **LOONGSON2_MMC_INT_CLEAR** (line 152)
- **LOONGSON2_MMC_INT_CSENT** (line 134)
- **LOONGSON2_MMC_INT_CTIMEOUT** (line 135)
- **LOONGSON2_MMC_INT_DFIN** (line 128)
- **LOONGSON2_MMC_INT_DTIMEOUT** (line 129)
- **LOONGSON2_MMC_INT_PROGERR** (line 132)
- **LOONGSON2_MMC_INT_RESPCRC** (line 136)
- **LOONGSON2_MMC_INT_RXCRC** (line 130)
- **LOONGSON2_MMC_INT_SDIOIRQ** (line 133)
- **LOONGSON2_MMC_INT_TXCRC** (line 131)
- **LOONGSON2_MMC_PRE** (line 65)
- **LOONGSON2_MMC_PRE_EN** (line 66)
- **LOONGSON2_MMC_REG_BSIZE** (line 38)
- **LOONGSON2_MMC_REG_CARG** (line 30)
- **LOONGSON2_MMC_REG_CCTL** (line 31)
- **LOONGSON2_MMC_REG_CSTS** (line 32)
- **LOONGSON2_MMC_REG_CTL** (line 28)
- **LOONGSON2_MMC_REG_DATA** (line 44)
- **LOONGSON2_MMC_REG_DCNT** (line 40)
- **LOONGSON2_MMC_REG_DCTL** (line 39)
- **LOONGSON2_MMC_REG_DELAY** (line 50)
- **LOONGSON2_MMC_REG_DLLCTL** (line 49)
- **LOONGSON2_MMC_REG_DLLVAL** (line 48)
- **LOONGSON2_MMC_REG_DSTS** (line 41)
- **LOONGSON2_MMC_REG_FSTS** (line 42)
- **LOONGSON2_MMC_REG_IEN** (line 45)
- **LOONGSON2_MMC_REG_INT** (line 43)
- **LOONGSON2_MMC_REG_PRE** (line 29)
- **LOONGSON2_MMC_REG_RDMA_HI** (line 57)
- **LOONGSON2_MMC_REG_RDMA_LO** (line 56)
- **LOONGSON2_MMC_REG_RSP0** (line 33)
- **LOONGSON2_MMC_REG_RSP1** (line 34)
- **LOONGSON2_MMC_REG_RSP2** (line 35)
- **LOONGSON2_MMC_REG_RSP3** (line 36)
- **LOONGSON2_MMC_REG_SEL** (line 51)
- **LOONGSON2_MMC_REG_TIMER** (line 37)
- **LOONGSON2_MMC_REG_WDMA_HI** (line 55)
- **LOONGSON2_MMC_REG_WDMA_LO** (line 54)
- **LOONGSON2_MMC_SEL_BUS** (line 169)
- **LOONGSON2_MMC_SEL_DATA** (line 168)
- **LOONGSON2_MMC_TXFULL_TIMEOUT_US** (line 190)
- **LS2K0500_DMA0_CONF** (line 208)
- **LS2K0500_DMA1_CONF** (line 209)
- **LS2K0500_DMA2_CONF** (line 210)
- **LS2K0500_SDIO_DMA_MASK** (line 207)
- **LS2K1000_DMA0_CONF** (line 200)
- **LS2K1000_DMA1_CONF** (line 201)
- **LS2K1000_DMA2_CONF** (line 202)
- **LS2K1000_DMA3_CONF** (line 203)
- **LS2K1000_DMA4_CONF** (line 204)
- **LS2K1000_SDIO_DMA_MASK** (line 199)
