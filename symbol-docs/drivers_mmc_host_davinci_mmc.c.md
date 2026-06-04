# drivers/mmc/host/davinci_mmc.c

Subsystem: drivers/mmc

## Functions (32)

### calculate_clk_divider
- Return type: static void
- Signature: calculate_clk_divider(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 630

### calculate_freq_for_card
- Return type: static unsigned int
- Signature: calculate_freq_for_card(struct mmc_davinci_host * host,unsigned int mmc_req_freq)
- Line: 602

### davinci_abort_data
- Return type: static void
- Signature: davinci_abort_data(struct mmc_davinci_host * host,struct mmc_data * data)
- Line: 833

### davinci_abort_dma
- Return type: static void
- Signature: davinci_abort_dma(struct mmc_davinci_host * host)
- Line: 377

### davinci_acquire_dma_channels
- Return type: static int
- Signature: davinci_acquire_dma_channels(struct mmc_davinci_host * host)
- Line: 484

### davinci_fifo_data_trans
- Return type: static void
- Signature: davinci_fifo_data_trans(struct mmc_davinci_host * host,unsigned int n)
- Line: 209

### davinci_mmcsd_probe
- Return type: static int
- Signature: davinci_mmcsd_probe(struct platform_device * pdev)
- Line: 1184

### davinci_mmcsd_remove
- Return type: static void
- Signature: davinci_mmcsd_remove(struct platform_device * pdev)
- Line: 1340

### davinci_mmcsd_resume
- Return type: static int
- Signature: davinci_mmcsd_resume(struct device * dev)
- Line: 1361

### davinci_mmcsd_suspend
- Return type: static int
- Signature: davinci_mmcsd_suspend(struct device * dev)
- Line: 1350

### davinci_release_dma_channels
- Return type: static void
- Signature: davinci_release_dma_channels(struct mmc_davinci_host * host)
- Line: 475

### init_mmcsd_host
- Return type: static void
- Signature: init_mmcsd_host(struct mmc_davinci_host * host)
- Line: 1101

### mmc_davinci_cmd_done
- Return type: static void
- Signature: mmc_davinci_cmd_done(struct mmc_davinci_host * host,struct mmc_command * cmd)
- Line: 790

### mmc_davinci_cpufreq_deregister
- Return type: static void
- Signature: mmc_davinci_cpufreq_deregister(struct mmc_davinci_host * host)
- Line: 1086

### mmc_davinci_cpufreq_deregister
- Return type: static void
- Signature: mmc_davinci_cpufreq_deregister(struct mmc_davinci_host * host)
- Line: 1097

### mmc_davinci_cpufreq_register
- Return type: static int
- Signature: mmc_davinci_cpufreq_register(struct mmc_davinci_host * host)
- Line: 1078

### mmc_davinci_cpufreq_register
- Return type: static int
- Signature: mmc_davinci_cpufreq_register(struct mmc_davinci_host * host)
- Line: 1092

### mmc_davinci_cpufreq_transition
- Return type: static int
- Signature: mmc_davinci_cpufreq_transition(struct notifier_block * nb,unsigned long val,void * data)
- Line: 1056

### mmc_davinci_enable_sdio_irq
- Return type: static void
- Signature: mmc_davinci_enable_sdio_irq(struct mmc_host * mmc,int enable)
- Line: 1025

### mmc_davinci_get_cd
- Return type: static int
- Signature: mmc_davinci_get_cd(struct mmc_host * mmc)
- Line: 1003

### mmc_davinci_get_ro
- Return type: static int
- Signature: mmc_davinci_get_ro(struct mmc_host * mmc)
- Line: 1014

### mmc_davinci_irq
- Return type: static irqreturn_t
- Signature: mmc_davinci_irq(int irq,void * dev_id)
- Line: 856

### mmc_davinci_parse_pdata
- Return type: static int
- Signature: mmc_davinci_parse_pdata(struct mmc_host * mmc)
- Line: 1140

### mmc_davinci_prepare_data
- Return type: static void
- Signature: mmc_davinci_prepare_data(struct mmc_davinci_host * host,struct mmc_request * req)
- Line: 505

### mmc_davinci_request
- Return type: static void
- Signature: mmc_davinci_request(struct mmc_host * mmc,struct mmc_request * req)
- Line: 575

### mmc_davinci_reset_ctrl
- Return type: static void
- Signature: mmc_davinci_reset_ctrl(struct mmc_davinci_host * host,int val)
- Line: 817

### mmc_davinci_sdio_irq
- Return type: static irqreturn_t
- Signature: mmc_davinci_sdio_irq(int irq,void * dev_id)
- Line: 841

### mmc_davinci_send_dma_request
- Return type: static int
- Signature: mmc_davinci_send_dma_request(struct mmc_davinci_host * host,struct mmc_data * data)
- Line: 389

### mmc_davinci_set_ios
- Return type: static void
- Signature: mmc_davinci_set_ios(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 676

### mmc_davinci_start_command
- Return type: static void
- Signature: mmc_davinci_start_command(struct mmc_davinci_host * host,struct mmc_command * cmd)
- Line: 257

### mmc_davinci_start_dma_transfer
- Return type: static int
- Signature: mmc_davinci_start_dma_transfer(struct mmc_davinci_host * host,struct mmc_data * data)
- Line: 449

### mmc_davinci_xfer_done
- Return type: static void
- Signature: mmc_davinci_xfer_done(struct mmc_davinci_host * host,struct mmc_data * data)
- Line: 756

## Structs (1)

### mmc_davinci_host
- Line: 166
- Members:
  - cmd: mmc_command *
  - data: mmc_data *
  - mmc: mmc_host *
  - clk: clk *
  - mmc_input_clk: unsigned int
  - base: void __iomem *
  - mem_res: resource *
  - mmc_irq: int
  - sdio_irq: int
  - bus_mode: unsigned char
  - data_dir: unsigned char
  - bytes_left: u32
  - dma_tx: dma_chan *
  - dma_rx: dma_chan *
  - use_dma: bool
  - do_dma: bool
  - sdio_int: bool
  - active_request: bool
  - sg_miter: sg_mapping_iter
  - sg_len: unsigned int
  - version: u8
  - ns_in_one_cycle: unsigned
  - nr_sg: u8
  - freq_transition: notifier_block

## Variables (8)

- static **davinci_mmc_devtype** : const struct platform_device_id[] (line 1115)
- static **davinci_mmc_dt_ids** : const struct of_device_id[] (line 1127)
- static **davinci_mmcsd_driver** : platform_driver (line 1378)
- static **mmc_davinci_ops** : const struct mmc_host_ops (line 1045)
- static **poll_loopcount** : unsigned (line 157)
- static **poll_threshold** : unsigned (line 152)
- static **rw_threshold** : unsigned (line 147)
- static **use_dma** : unsigned (line 162)

## Macros (88)

- **DAVINCI_MMCARGHL** (line 44)
- **DAVINCI_MMCBLEN** (line 38)
- **DAVINCI_MMCBLNC** (line 55)
- **DAVINCI_MMCCIDX** (line 51)
- **DAVINCI_MMCCKC** (line 52)
- **DAVINCI_MMCCLK** (line 32)
- **DAVINCI_MMCCMD** (line 43)
- **DAVINCI_MMCCTL** (line 31)
- **DAVINCI_MMCDRR** (line 41)
- **DAVINCI_MMCDRSP** (line 49)
- **DAVINCI_MMCDXR** (line 42)
- **DAVINCI_MMCETOK** (line 50)
- **DAVINCI_MMCFIFOCTL** (line 60)
- **DAVINCI_MMCIM** (line 35)
- **DAVINCI_MMCNBLC** (line 40)
- **DAVINCI_MMCNBLK** (line 39)
- **DAVINCI_MMCRSP01** (line 45)
- **DAVINCI_MMCRSP23** (line 46)
- **DAVINCI_MMCRSP45** (line 47)
- **DAVINCI_MMCRSP67** (line 48)
- **DAVINCI_MMCST0** (line 33)
- **DAVINCI_MMCST1** (line 34)
- **DAVINCI_MMCTOD** (line 37)
- **DAVINCI_MMCTODC** (line 54)
- **DAVINCI_MMCTOR** (line 36)
- **DAVINCI_MMCTORC** (line 53)
- **DAVINCI_MMC_DATADIR_NONE** (line 177)
- **DAVINCI_MMC_DATADIR_READ** (line 178)
- **DAVINCI_MMC_DATADIR_WRITE** (line 179)
- **DAVINCI_SDIOCTL** (line 56)
- **DAVINCI_SDIOIEN** (line 58)
- **DAVINCI_SDIOIST** (line 59)
- **DAVINCI_SDIOST0** (line 57)
- **MAX_CCNT** (line 143)
- **MAX_NR_SG** (line 145)
- **MMCCLK_CLKEN** (line 77)
- **MMCCLK_CLKRT_MASK** (line 78)
- **MMCCMD_BSYEXP** (line 100)
- **MMCCMD_CMD_MASK** (line 98)
- **MMCCMD_DCLR** (line 110)
- **MMCCMD_DMATRIG** (line 111)
- **MMCCMD_DTRW** (line 106)
- **MMCCMD_INITCK** (line 109)
- **MMCCMD_PPLEN** (line 99)
- **MMCCMD_RSPFMT_MASK** (line 101)
- **MMCCMD_RSPFMT_NONE** (line 102)
- **MMCCMD_RSPFMT_R1456** (line 103)
- **MMCCMD_RSPFMT_R2** (line 104)
- **MMCCMD_RSPFMT_R3** (line 105)
- **MMCCMD_STRMTP** (line 107)
- **MMCCMD_WDATX** (line 108)
- **MMCCTL_CMDRST** (line 64)
- **MMCCTL_DATEG_BOTH** (line 70)
- **MMCCTL_DATEG_DISABLED** (line 67)
- **MMCCTL_DATEG_FALLING** (line 69)
- **MMCCTL_DATEG_RISING** (line 68)
- **MMCCTL_DATRST** (line 63)
- **MMCCTL_PERMDR_BE** (line 72)
- **MMCCTL_PERMDR_LE** (line 71)
- **MMCCTL_PERMDX_BE** (line 74)
- **MMCCTL_PERMDX_LE** (line 73)
- **MMCCTL_WIDTH_4_BIT** (line 66)
- **MMCCTL_WIDTH_8_BIT** (line 65)
- **MMCFIFOCTL_ACCWD_1** (line 121)
- **MMCFIFOCTL_ACCWD_2** (line 120)
- **MMCFIFOCTL_ACCWD_3** (line 119)
- **MMCFIFOCTL_ACCWD_4** (line 118)
- **MMCFIFOCTL_FIFODIR_RD** (line 116)
- **MMCFIFOCTL_FIFODIR_WR** (line 115)
- **MMCFIFOCTL_FIFOLEV** (line 117)
- **MMCFIFOCTL_FIFORST** (line 114)
- **MMCSD_INIT_CLOCK** (line 133)
- **MMCST0_BSYDNE** (line 82)
- **MMCST0_CRCRD** (line 87)
- **MMCST0_CRCRS** (line 88)
- **MMCST0_CRCWR** (line 86)
- **MMCST0_DATDNE** (line 81)
- **MMCST0_DATED** (line 91)
- **MMCST0_DRRDY** (line 90)
- **MMCST0_DXRDY** (line 89)
- **MMCST0_RSPDNE** (line 83)
- **MMCST0_TOUTRD** (line 84)
- **MMCST0_TOUTRS** (line 85)
- **MMCST0_TRNDNE** (line 92)
- **MMCST1_BUSY** (line 95)
- **SDIOIEN_IOINTEN** (line 127)
- **SDIOIST_IOINT** (line 130)
- **SDIOST0_DAT1_HI** (line 124)
