# drivers/mmc/host/bcm2835.c

Subsystem: drivers/mmc

## Functions (36)

### bcm2835_add_host
- Return type: static int
- Signature: bcm2835_add_host(struct bcm2835_host * host)
- Line: 1259

### bcm2835_block_irq
- Return type: static void
- Signature: bcm2835_block_irq(struct bcm2835_host * host)
- Line: 953

### bcm2835_busy_irq
- Return type: static void
- Signature: bcm2835_busy_irq(struct bcm2835_host * host)
- Line: 895

### bcm2835_check_cmd_error
- Return type: static bool
- Signature: bcm2835_check_cmd_error(struct bcm2835_host * host,u32 intmask)
- Line: 854

### bcm2835_check_data_error
- Return type: static void
- Signature: bcm2835_check_data_error(struct bcm2835_host * host,u32 intmask)
- Line: 885

### bcm2835_data_irq
- Return type: static void
- Signature: bcm2835_data_irq(struct bcm2835_host * host,u32 intmask)
- Line: 911

### bcm2835_data_threaded_irq
- Return type: static void
- Signature: bcm2835_data_threaded_irq(struct bcm2835_host * host)
- Line: 945

### bcm2835_dma_complete
- Return type: static void
- Signature: bcm2835_dma_complete(void * param)
- Line: 323

### bcm2835_dma_complete_work
- Return type: static void
- Signature: bcm2835_dma_complete_work(struct work_struct * work)
- Line: 1049

### bcm2835_dumpcmd
- Return type: static void
- Signature: bcm2835_dumpcmd(struct bcm2835_host * host,struct mmc_command * cmd,const char * label)
- Line: 194

### bcm2835_dumpregs
- Return type: static void
- Signature: bcm2835_dumpregs(struct bcm2835_host * host)
- Line: 209

### bcm2835_finish_command
- Return type: static void
- Signature: bcm2835_finish_command(struct bcm2835_host * host)
- Line: 739

### bcm2835_finish_data
- Return type: static void
- Signature: bcm2835_finish_data(struct bcm2835_host * host)
- Line: 713

### bcm2835_finish_request
- Return type: static void
- Signature: bcm2835_finish_request(struct bcm2835_host * host)
- Line: 592

### bcm2835_irq
- Return type: static irqreturn_t
- Signature: bcm2835_irq(int irq,void * dev_id)
- Line: 971

### bcm2835_prepare_data
- Return type: static void
- Signature: bcm2835_prepare_data(struct bcm2835_host * host,struct mmc_command * cmd)
- Line: 542

### bcm2835_prepare_dma
- Return type: static void
- Signature: bcm2835_prepare_dma(struct bcm2835_host * host,struct mmc_data * data)
- Line: 449

### bcm2835_probe
- Return type: static int
- Signature: bcm2835_probe(struct platform_device * pdev)
- Line: 1366

### bcm2835_read_wait_sdcmd
- Return type: static u32
- Signature: bcm2835_read_wait_sdcmd(struct bcm2835_host * host,u32 max_ms)
- Line: 573

### bcm2835_remove
- Return type: static void
- Signature: bcm2835_remove(struct platform_device * pdev)
- Line: 1458

### bcm2835_request
- Return type: static void
- Signature: bcm2835_request(struct mmc_host * mmc,struct mmc_request * mrq)
- Line: 1154

### bcm2835_reset
- Return type: static void
- Signature: bcm2835_reset(struct mmc_host * mmc)
- Line: 273

### bcm2835_reset_internal
- Return type: static void
- Signature: bcm2835_reset_internal(struct bcm2835_host * host)
- Line: 244

### bcm2835_resume
- Return type: static int
- Signature: bcm2835_resume(struct device * dev)
- Line: 1356

### bcm2835_send_command
- Return type: static bool
- Signature: bcm2835_send_command(struct bcm2835_host * host,struct mmc_command * cmd)
- Line: 621

### bcm2835_set_clock
- Return type: static void
- Signature: bcm2835_set_clock(struct bcm2835_host * host,unsigned int clock)
- Line: 1094

### bcm2835_set_ios
- Return type: static void
- Signature: bcm2835_set_ios(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 1227

### bcm2835_set_transfer_irqs
- Return type: static void
- Signature: bcm2835_set_transfer_irqs(struct bcm2835_host * host)
- Line: 524

### bcm2835_start_dma
- Return type: static void
- Signature: bcm2835_start_dma(struct bcm2835_host * host)
- Line: 518

### bcm2835_suspend
- Return type: static int
- Signature: bcm2835_suspend(struct device * dev)
- Line: 1347

### bcm2835_threaded_irq
- Return type: static irqreturn_t
- Signature: bcm2835_threaded_irq(int irq,void * dev_id)
- Line: 1018

### bcm2835_timeout
- Return type: static void
- Signature: bcm2835_timeout(struct work_struct * work)
- Line: 823

### bcm2835_transfer_block_pio
- Return type: static void
- Signature: bcm2835_transfer_block_pio(struct bcm2835_host * host,bool is_read)
- Line: 330

### bcm2835_transfer_complete
- Return type: static void
- Signature: bcm2835_transfer_complete(struct bcm2835_host * host)
- Line: 688

### bcm2835_transfer_pio
- Return type: static void
- Signature: bcm2835_transfer_pio(struct bcm2835_host * host)
- Line: 424

### bcm2835_wait_transfer_complete
- Return type: static void
- Signature: bcm2835_wait_transfer_complete(struct bcm2835_host * host)
- Line: 285

## Structs (1)

### bcm2835_host
- Line: 145
- Members:
  - lock: spinlock_t
  - mutex: mutex
  - ioaddr: void __iomem *
  - phys_addr: u32
  - clk: clk *
  - pdev: platform_device *
  - clock: unsigned int
  - max_clk: unsigned int
  - dma_work: work_struct
  - timeout_work: delayed_work
  - sg_miter: sg_mapping_iter
  - blocks: unsigned int
  - irq: int
  - ns_per_fifo_word: u32
  - hcfg: u32
  - cdiv: u32
  - mrq: mmc_request *
  - cmd: mmc_command *
  - data: mmc_data *
  - data_complete: bool:1
  - use_busy: bool:1
  - use_sbc: bool:1
  - irq_block: bool
  - irq_busy: bool
  - irq_data: bool
  - dma_chan_rxtx: dma_chan *
  - dma_chan: dma_chan *
  - dma_cfg_rx: dma_slave_config
  - dma_cfg_tx: dma_slave_config
  - dma_desc: dma_async_tx_descriptor *
  - dma_dir: u32
  - drain_words: u32
  - drain_page: page *
  - drain_offset: u32
  - use_dma: bool

## Variables (3)

- static **bcm2835_driver** : platform_driver (line 1484)
- static **bcm2835_match** : const struct of_device_id[] (line 1478)
- static **bcm2835_ops** : const struct mmc_host_ops (line 1253)

## Macros (72)

- **FIFO_READ_THRESHOLD** (line 139)
- **FIFO_WRITE_THRESHOLD** (line 140)
- **PIO_THRESHOLD** (line 143)
- **SDARG** (line 54)
- **SDCDIV** (line 56)
- **SDCDIV_MAX_CDIV** (line 78)
- **SDCMD** (line 53)
- **SDCMD_BUSYWAIT** (line 71)
- **SDCMD_CMD_MASK** (line 76)
- **SDCMD_FAIL_FLAG** (line 70)
- **SDCMD_LONG_RESPONSE** (line 73)
- **SDCMD_NEW_FLAG** (line 69)
- **SDCMD_NO_RESPONSE** (line 72)
- **SDCMD_READ_CMD** (line 75)
- **SDCMD_WRITE_CMD** (line 74)
- **SDDATA** (line 66)
- **SDDATA_FIFO_PIO_BURST** (line 141)
- **SDDATA_FIFO_WORDS** (line 137)
- **SDEDM** (line 63)
- **SDEDM_BYPASS** (line 114)
- **SDEDM_CLOCK_PULSE** (line 113)
- **SDEDM_FORCE_DATA_MODE** (line 112)
- **SDEDM_FSM_DATAMODE** (line 122)
- **SDEDM_FSM_GENPULSES** (line 133)
- **SDEDM_FSM_IDENTMODE** (line 121)
- **SDEDM_FSM_MASK** (line 120)
- **SDEDM_FSM_POWERDOWN** (line 129)
- **SDEDM_FSM_POWERUP** (line 130)
- **SDEDM_FSM_READCRC** (line 126)
- **SDEDM_FSM_READDATA** (line 123)
- **SDEDM_FSM_READWAIT** (line 125)
- **SDEDM_FSM_STARTPOWDOWN** (line 135)
- **SDEDM_FSM_WRITECRC** (line 127)
- **SDEDM_FSM_WRITEDATA** (line 124)
- **SDEDM_FSM_WRITESTART1** (line 131)
- **SDEDM_FSM_WRITESTART2** (line 132)
- **SDEDM_FSM_WRITEWAIT1** (line 128)
- **SDEDM_FSM_WRITEWAIT2** (line 134)
- **SDEDM_READ_THRESHOLD_SHIFT** (line 117)
- **SDEDM_THRESHOLD_MASK** (line 118)
- **SDEDM_WRITE_THRESHOLD_SHIFT** (line 116)
- **SDHBCT** (line 65)
- **SDHBLC** (line 67)
- **SDHCFG** (line 64)
- **SDHCFG_BLOCK_IRPT_EN** (line 101)
- **SDHCFG_BUSY_IRPT_EN** (line 100)
- **SDHCFG_DATA_IRPT_EN** (line 103)
- **SDHCFG_REL_CMD_LINE** (line 107)
- **SDHCFG_SDIO_IRPT_EN** (line 102)
- **SDHCFG_SLOW_CARD** (line 104)
- **SDHCFG_WIDE_EXT_BUS** (line 105)
- **SDHCFG_WIDE_INT_BUS** (line 106)
- **SDHSTS** (line 61)
- **SDHSTS_BLOCK_IRPT** (line 81)
- **SDHSTS_BUSY_IRPT** (line 80)
- **SDHSTS_CMD_TIME_OUT** (line 84)
- **SDHSTS_CRC16_ERROR** (line 85)
- **SDHSTS_CRC7_ERROR** (line 86)
- **SDHSTS_DATA_FLAG** (line 90)
- **SDHSTS_ERROR_MASK** (line 97)
- **SDHSTS_FIFO_ERROR** (line 87)
- **SDHSTS_REW_TIME_OUT** (line 83)
- **SDHSTS_SDIO_IRPT** (line 82)
- **SDHSTS_TRANSFER_ERROR_MASK** (line 92)
- **SDRSP0** (line 57)
- **SDRSP1** (line 58)
- **SDRSP2** (line 59)
- **SDRSP3** (line 60)
- **SDTOUT** (line 55)
- **SDVDD** (line 62)
- **SDVDD_POWER_OFF** (line 109)
- **SDVDD_POWER_ON** (line 110)
