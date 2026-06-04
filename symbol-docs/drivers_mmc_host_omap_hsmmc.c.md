# drivers/mmc/host/omap_hsmmc.c

Subsystem: drivers/mmc

## Functions (59)

### calc_divisor
- Return type: static u16
- Signature: calc_divisor(struct omap_hsmmc_host * host,struct mmc_ios * ios)
- Line: 520

### hsmmc_command_incomplete
- Return type: static void
- Signature: hsmmc_command_incomplete(struct omap_hsmmc_host * host,int err,int end_cmd)
- Line: 999

### mmc_regs_show
- Return type: static int
- Signature: mmc_regs_show(struct seq_file * s,void * data)
- Line: 1632

### of_get_hsmmc_pdata
- Return type: static omap_hsmmc_platform_data *
- Signature: of_get_hsmmc_pdata(struct device * dev)
- Line: 1755

### of_get_hsmmc_pdata
- Return type: static omap_hsmmc_platform_data *
- Signature: of_get_hsmmc_pdata(struct device * dev)
- Line: 1724

### omap_hsmmc_cmd_done
- Return type: static void
- Signature: omap_hsmmc_cmd_done(struct omap_hsmmc_host * host,struct mmc_command * cmd)
- Line: 870

### omap_hsmmc_conf_bus_power
- Return type: static void
- Signature: omap_hsmmc_conf_bus_power(struct omap_hsmmc_host * host)
- Line: 1587

### omap_hsmmc_configure_wake_irq
- Return type: static int
- Signature: omap_hsmmc_configure_wake_irq(struct omap_hsmmc_host * host)
- Line: 1536

### omap_hsmmc_context_restore
- Return type: static int
- Signature: omap_hsmmc_context_restore(struct omap_hsmmc_host * host)
- Line: 627

### omap_hsmmc_context_save
- Return type: static void
- Signature: omap_hsmmc_context_save(struct omap_hsmmc_host * host)
- Line: 694

### omap_hsmmc_context_save
- Return type: static void
- Signature: omap_hsmmc_context_save(struct omap_hsmmc_host * host)
- Line: 704

### omap_hsmmc_dbg_report_irq
- Return type: static void
- Signature: omap_hsmmc_dbg_report_irq(struct omap_hsmmc_host * host,u32 status)
- Line: 956

### omap_hsmmc_dbg_report_irq
- Return type: static void
- Signature: omap_hsmmc_dbg_report_irq(struct omap_hsmmc_host * host,u32 status)
- Line: 931

### omap_hsmmc_debugfs
- Return type: static void
- Signature: omap_hsmmc_debugfs(struct mmc_host * mmc)
- Line: 1672

### omap_hsmmc_debugfs
- Return type: static void
- Signature: omap_hsmmc_debugfs(struct mmc_host * mmc)
- Line: 1681

### omap_hsmmc_disable_boot_regulator
- Return type: static int
- Signature: omap_hsmmc_disable_boot_regulator(struct regulator * reg)
- Line: 361

### omap_hsmmc_disable_boot_regulators
- Return type: static int
- Signature: omap_hsmmc_disable_boot_regulators(struct omap_hsmmc_host * host)
- Line: 381

### omap_hsmmc_disable_irq
- Return type: static void
- Signature: omap_hsmmc_disable_irq(struct omap_hsmmc_host * host)
- Line: 504

### omap_hsmmc_disable_supply
- Return type: static int
- Signature: omap_hsmmc_disable_supply(struct mmc_host * mmc)
- Line: 247

### omap_hsmmc_dma_callback
- Return type: static void
- Signature: omap_hsmmc_dma_callback(void * param)
- Line: 1157

### omap_hsmmc_dma_cleanup
- Return type: static void
- Signature: omap_hsmmc_dma_cleanup(struct omap_hsmmc_host * host,int errno)
- Line: 902

### omap_hsmmc_do_irq
- Return type: static void
- Signature: omap_hsmmc_do_irq(struct omap_hsmmc_host * host,int status)
- Line: 1015

### omap_hsmmc_enable_irq
- Return type: static void
- Signature: omap_hsmmc_enable_irq(struct omap_hsmmc_host * host,struct mmc_command * cmd)
- Line: 480

### omap_hsmmc_enable_sdio_irq
- Return type: static void
- Signature: omap_hsmmc_enable_sdio_irq(struct mmc_host * mmc,int enable)
- Line: 1501

### omap_hsmmc_enable_supply
- Return type: static int
- Signature: omap_hsmmc_enable_supply(struct mmc_host * mmc)
- Line: 216

### omap_hsmmc_get_dma_chan
- Return type: static dma_chan *
- Signature: omap_hsmmc_get_dma_chan(struct omap_hsmmc_host * host,struct mmc_data * data)
- Line: 809

### omap_hsmmc_irq
- Return type: static irqreturn_t
- Signature: omap_hsmmc_irq(int irq,void * dev_id)
- Line: 1065

### omap_hsmmc_multi_io_quirk
- Return type: static int
- Signature: omap_hsmmc_multi_io_quirk(struct mmc_card * card,unsigned int direction,int blk_size)
- Line: 1610

### omap_hsmmc_post_req
- Return type: static void
- Signature: omap_hsmmc_post_req(struct mmc_host * mmc,struct mmc_request * mrq,int err)
- Line: 1384

### omap_hsmmc_pre_dma_transfer
- Return type: static int
- Signature: omap_hsmmc_pre_dma_transfer(struct omap_hsmmc_host * host,struct mmc_data * data,struct omap_hsmmc_next * next,struct dma_chan * chan)
- Line: 1190

### omap_hsmmc_pre_req
- Return type: static void
- Signature: omap_hsmmc_pre_req(struct mmc_host * mmc,struct mmc_request * mrq)
- Line: 1399

### omap_hsmmc_prepare_data
- Return type: static int
- Signature: omap_hsmmc_prepare_data(struct omap_hsmmc_host * host,struct mmc_request * req)
- Line: 1350

### omap_hsmmc_probe
- Return type: static int
- Signature: omap_hsmmc_probe(struct platform_device * pdev)
- Line: 1761

### omap_hsmmc_reg_get
- Return type: static int
- Signature: omap_hsmmc_reg_get(struct omap_hsmmc_host * host)
- Line: 414

### omap_hsmmc_remove
- Return type: static void
- Signature: omap_hsmmc_remove(struct platform_device * pdev)
- Line: 1974

### omap_hsmmc_request
- Return type: static void
- Signature: omap_hsmmc_request(struct mmc_host * mmc,struct mmc_request * req)
- Line: 1420

### omap_hsmmc_request_done
- Return type: static void
- Signature: omap_hsmmc_request_done(struct omap_hsmmc_host * host,struct mmc_request * mrq)
- Line: 815

### omap_hsmmc_reset_controller_fsm
- Return type: static void
- Signature: omap_hsmmc_reset_controller_fsm(struct omap_hsmmc_host * host,unsigned long bit)
- Line: 969

### omap_hsmmc_resume
- Return type: static int
- Signature: omap_hsmmc_resume(struct device * dev)
- Line: 2016

### omap_hsmmc_runtime_resume
- Return type: static int
- Signature: omap_hsmmc_runtime_resume(struct device * dev)
- Line: 2076

### omap_hsmmc_runtime_suspend
- Return type: static int
- Signature: omap_hsmmc_runtime_suspend(struct device * dev)
- Line: 2034

### omap_hsmmc_set_bus_mode
- Return type: static void
- Signature: omap_hsmmc_set_bus_mode(struct omap_hsmmc_host * host)
- Line: 611

### omap_hsmmc_set_bus_width
- Return type: static void
- Signature: omap_hsmmc_set_bus_width(struct omap_hsmmc_host * host)
- Line: 583

### omap_hsmmc_set_clock
- Return type: static void
- Signature: omap_hsmmc_set_clock(struct omap_hsmmc_host * host)
- Line: 533

### omap_hsmmc_set_ios
- Return type: static void
- Signature: omap_hsmmc_set_ios(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 1451

### omap_hsmmc_set_pbias
- Return type: static int
- Signature: omap_hsmmc_set_pbias(struct omap_hsmmc_host * host,bool power_on)
- Line: 280

### omap_hsmmc_set_power
- Return type: static int
- Signature: omap_hsmmc_set_power(struct omap_hsmmc_host * host,int power_on)
- Line: 310

### omap_hsmmc_setup_dma_transfer
- Return type: static int
- Signature: omap_hsmmc_setup_dma_transfer(struct omap_hsmmc_host * host,struct mmc_request * req)
- Line: 1231

### omap_hsmmc_show_slot_name
- Return type: static ssize_t
- Signature: omap_hsmmc_show_slot_name(struct device * dev,struct device_attribute * attr,char * buf)
- Line: 740

### omap_hsmmc_start_clock
- Return type: static void
- Signature: omap_hsmmc_start_clock(struct omap_hsmmc_host * host)
- Line: 463

### omap_hsmmc_start_command
- Return type: static void
- Signature: omap_hsmmc_start_command(struct omap_hsmmc_host * host,struct mmc_command * cmd,struct mmc_data * data)
- Line: 755

### omap_hsmmc_start_dma_transfer
- Return type: static void
- Signature: omap_hsmmc_start_dma_transfer(struct omap_hsmmc_host * host)
- Line: 1331

### omap_hsmmc_stop_clock
- Return type: static void
- Signature: omap_hsmmc_stop_clock(struct omap_hsmmc_host * host)
- Line: 472

### omap_hsmmc_suspend
- Return type: static int
- Signature: omap_hsmmc_suspend(struct device * dev)
- Line: 1992

### omap_hsmmc_switch_opcond
- Return type: static int
- Signature: omap_hsmmc_switch_opcond(struct omap_hsmmc_host * host,int vdd)
- Line: 1105

### omap_hsmmc_xfer_done
- Return type: static void
- Signature: omap_hsmmc_xfer_done(struct omap_hsmmc_host * host,struct mmc_data * data)
- Line: 837

### send_init_stream
- Return type: static void
- Signature: send_init_stream(struct omap_hsmmc_host * host)
- Line: 714

### set_data_timeout
- Return type: static void
- Signature: set_data_timeout(struct omap_hsmmc_host * host,unsigned long long timeout_ns,unsigned int timeout_clks)
- Line: 1293

### set_sd_bus_power
- Return type: static void
- Signature: set_sd_bus_power(struct omap_hsmmc_host * host)
- Line: 1085

## Structs (3)

### omap_hsmmc_host
- Line: 169
- Members:
  - dma_len: unsigned int
  - cookie: s32
  - dev: device *
  - mmc: mmc_host *
  - mrq: mmc_request *
  - cmd: mmc_command *
  - data: mmc_data *
  - fclk: clk *
  - dbclk: clk *
  - pbias: regulator *
  - pbias_enabled: bool
  - base: void __iomem *
  - vqmmc_enabled: bool
  - mapbase: resource_size_t
  - irq_lock: spinlock_t
  - dma_len: unsigned int
  - dma_sg_idx: unsigned int
  - bus_mode: unsigned char
  - power_mode: unsigned char
  - suspended: int
  - con: u32
  - hctl: u32
  - sysctl: u32
  - capa: u32
  - irq: int
  - wake_irq: int
  - dma_ch: int
  - use_dma: int
  - tx_chan: dma_chan *
  - rx_chan: dma_chan *
  - response_busy: int
  - context_loss: int
  - reqs_blocked: int
  - req_in_progress: int
  - clk_rate: unsigned long
  - flags: unsigned int
  - next_data: omap_hsmmc_next
  - pdata: omap_hsmmc_platform_data *
  - reg_offset: u32
  - controller_flags: u8

### omap_hsmmc_next
- Line: 164
- Members:
  - dma_len: unsigned int
  - cookie: s32
  - dev: device *
  - mmc: mmc_host *
  - mrq: mmc_request *
  - cmd: mmc_command *
  - data: mmc_data *
  - fclk: clk *
  - dbclk: clk *
  - pbias: regulator *
  - pbias_enabled: bool
  - base: void __iomem *
  - vqmmc_enabled: bool
  - mapbase: resource_size_t
  - irq_lock: spinlock_t
  - dma_len: unsigned int
  - dma_sg_idx: unsigned int
  - bus_mode: unsigned char
  - power_mode: unsigned char
  - suspended: int
  - con: u32
  - hctl: u32
  - sysctl: u32
  - capa: u32
  - irq: int
  - wake_irq: int
  - dma_ch: int
  - use_dma: int
  - tx_chan: dma_chan *
  - rx_chan: dma_chan *
  - response_busy: int
  - context_loss: int
  - reqs_blocked: int
  - req_in_progress: int
  - clk_rate: unsigned long
  - flags: unsigned int
  - next_data: omap_hsmmc_next
  - pdata: omap_hsmmc_platform_data *
  - reg_offset: u32
  - controller_flags: u8

### omap_mmc_of_data
- Line: 209
- Members:
  - dma_len: unsigned int
  - cookie: s32
  - dev: device *
  - mmc: mmc_host *
  - mrq: mmc_request *
  - cmd: mmc_command *
  - data: mmc_data *
  - fclk: clk *
  - dbclk: clk *
  - pbias: regulator *
  - pbias_enabled: bool
  - base: void __iomem *
  - vqmmc_enabled: bool
  - mapbase: resource_size_t
  - irq_lock: spinlock_t
  - dma_len: unsigned int
  - dma_sg_idx: unsigned int
  - bus_mode: unsigned char
  - power_mode: unsigned char
  - suspended: int
  - con: u32
  - hctl: u32
  - sysctl: u32
  - capa: u32
  - irq: int
  - wake_irq: int
  - dma_ch: int
  - use_dma: int
  - tx_chan: dma_chan *
  - rx_chan: dma_chan *
  - response_busy: int
  - context_loss: int
  - reqs_blocked: int
  - req_in_progress: int
  - clk_rate: unsigned long
  - flags: unsigned int
  - next_data: omap_hsmmc_next
  - pdata: omap_hsmmc_platform_data *
  - reg_offset: u32
  - controller_flags: u8

## Variables (7)

- static **am33xx_mmc_of_data** : const struct omap_mmc_of_data (line 1696)
- static **omap3_pre_es3_mmc_of_data** : const struct omap_mmc_of_data (line 1688)
- static **omap4_mmc_of_data** : const struct omap_mmc_of_data (line 1693)
- static **omap_hsmmc_dev_pm_ops** : const struct dev_pm_ops (line 2102)
- static **omap_hsmmc_driver** : platform_driver (line 2107)
- static **omap_hsmmc_ops** : mmc_host_ops (line 1620)
- static **omap_mmc_of_match** : const struct of_device_id[] (line 1701)

## Macros (95)

- **ACCE** (line 137)
- **ACEB** (line 136)
- **ACEN_ACMD23** (line 88)
- **ACE_EN** (line 126)
- **ACIE** (line 135)
- **ACNE** (line 139)
- **ACTO** (line 138)
- **AUTOIDLE** (line 76)
- **AUTO_CMD23** (line 203)
- **BADA_EN** (line 128)
- **BCE** (line 93)
- **BRR_EN** (line 116)
- **BWR_EN** (line 115)
- **CCRC_EN** (line 120)
- **CC_EN** (line 113)
- **CEB_EN** (line 121)
- **CEN** (line 81)
- **CERR_EN** (line 127)
- **CIE_EN** (line 122)
- **CIRQ_EN** (line 117)
- **CLKD_MASK** (line 83)
- **CLKD_MAX** (line 82)
- **CLKD_SHIFT** (line 84)
- **CLKEXTFREE** (line 98)
- **CNI** (line 134)
- **CTO_EN** (line 119)
- **CTPL** (line 99)
- **DCRC_EN** (line 124)
- **DDIR** (line 90)
- **DDR** (line 97)
- **DEB_EN** (line 125)
- **DLEV_DAT**(x) (line 110)
- **DMAE** (line 91)
- **DP_SELECT** (line 89)
- **DRIVER_NAME** (line 146)
- **DTO** (line 78)
- **DTO_EN** (line 123)
- **DTO_MASK** (line 85)
- **DTO_SHIFT** (line 86)
- **DUAL_VOLT_OCR_BIT** (line 104)
- **DW8** (line 100)
- **ERR_EN** (line 118)
- **FOUR_BIT** (line 94)
- **HSMMC_SDIO_IRQ_ENABLED** (line 204)
- **HSPE** (line 95)
- **HSS** (line 69)
- **ICE** (line 79)
- **ICS** (line 80)
- **INIT_STREAM** (line 87)
- **INIT_STREAM_CMD** (line 103)
- **INT_EN_MASK** (line 130)
- **IWE** (line 96)
- **MMC_AUTOSUSPEND_DELAY** (line 141)
- **MMC_TIMEOUT_MS** (line 142)
- **MMC_TIMEOUT_US** (line 143)
- **MSBS** (line 92)
- **OD** (line 101)
- **OMAP_HSMMC_AC12** (line 64)
- **OMAP_HSMMC_ARG** (line 51)
- **OMAP_HSMMC_BLK** (line 50)
- **OMAP_HSMMC_CAPA** (line 65)
- **OMAP_HSMMC_CMD** (line 52)
- **OMAP_HSMMC_CON** (line 48)
- **OMAP_HSMMC_DATA** (line 57)
- **OMAP_HSMMC_HCTL** (line 59)
- **OMAP_HSMMC_IE** (line 62)
- **OMAP_HSMMC_ISE** (line 63)
- **OMAP_HSMMC_PSTATE** (line 58)
- **OMAP_HSMMC_READ**(base,reg) (line 158)
- **OMAP_HSMMC_RSP10** (line 53)
- **OMAP_HSMMC_RSP32** (line 54)
- **OMAP_HSMMC_RSP54** (line 55)
- **OMAP_HSMMC_RSP76** (line 56)
- **OMAP_HSMMC_SDMASA** (line 49)
- **OMAP_HSMMC_STAT** (line 61)
- **OMAP_HSMMC_SYSCTL** (line 60)
- **OMAP_HSMMC_SYSSTATUS** (line 47)
- **OMAP_HSMMC_WRITE**(base,reg,val) (line 161)
- **OMAP_MMC_MAX_CLOCK** (line 145)
- **OMAP_MMC_MIN_CLOCK** (line 144)
- **SDBP** (line 77)
- **SDVS18** (line 70)
- **SDVS30** (line 71)
- **SDVS33** (line 72)
- **SDVSCLR** (line 74)
- **SDVSDET** (line 75)
- **SDVS_MASK** (line 73)
- **SOFTRESET** (line 107)
- **SRC** (line 105)
- **SRD** (line 106)
- **STAT_CLEAR** (line 102)
- **TC_EN** (line 114)
- **VS18** (line 67)
- **VS30** (line 68)
- **mmc_pdata**(host) (line 153)
