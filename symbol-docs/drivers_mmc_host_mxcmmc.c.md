# drivers/mmc/host/mxcmmc.c

Subsystem: drivers/mmc

## Functions (40)

### buffer_swap32
- Return type: static void
- Signature: buffer_swap32(u32 * buf,int len)
- Line: 257

### filter
- Return type: static bool
- Signature: filter(struct dma_chan * chan,void * param)
- Line: 944

### is_imx31_mmc
- Return type: static int
- Signature: is_imx31_mmc(struct mxcmci_host * host)
- Line: 175

### is_mpc512x_mmc
- Return type: static int
- Signature: is_mpc512x_mmc(struct mxcmci_host * host)
- Line: 180

### mxcmci_cmd_done
- Return type: static void
- Signature: mxcmci_cmd_done(struct mxcmci_host * host,unsigned int stat)
- Line: 691

### mxcmci_data_done
- Return type: static void
- Signature: mxcmci_data_done(struct mxcmci_host * host,unsigned int stat)
- Line: 649

### mxcmci_datawork
- Return type: static void
- Signature: mxcmci_datawork(struct work_struct * work)
- Line: 629

### mxcmci_detect_irq
- Return type: static irqreturn_t
- Signature: mxcmci_detect_irq(int irq,void * data)
- Line: 884

### mxcmci_dma_callback
- Return type: static void
- Signature: mxcmci_dma_callback(void * data)
- Line: 350

### mxcmci_enable_sdio_irq
- Return type: static void
- Signature: mxcmci_enable_sdio_irq(struct mmc_host * mmc,int enable)
- Line: 908

### mxcmci_finish_data
- Return type: static int
- Signature: mxcmci_finish_data(struct mxcmci_host * host,unsigned int stat)
- Line: 436

### mxcmci_finish_request
- Return type: static void
- Signature: mxcmci_finish_request(struct mxcmci_host * host,struct mmc_request * req)
- Line: 417

### mxcmci_get_ro
- Return type: static int
- Signature: mxcmci_get_ro(struct mmc_host * mmc)
- Line: 894

### mxcmci_init_card
- Return type: static void
- Signature: mxcmci_init_card(struct mmc_host * host,struct mmc_card * card)
- Line: 927

### mxcmci_irq
- Return type: static irqreturn_t
- Signature: mxcmci_irq(int irq,void * devid)
- Line: 710

### mxcmci_poll_status
- Return type: static int
- Signature: mxcmci_poll_status(struct mxcmci_host * host,u32 mask)
- Line: 516

### mxcmci_probe
- Return type: static int
- Signature: mxcmci_probe(struct platform_device * pdev)
- Line: 992

### mxcmci_pull
- Return type: static int
- Signature: mxcmci_pull(struct mxcmci_host * host,u32 * buf,int bytes)
- Line: 536

### mxcmci_push
- Return type: static int
- Signature: mxcmci_push(struct mxcmci_host * host,u32 * buf,int bytes)
- Line: 564

### mxcmci_read_response
- Return type: static void
- Signature: mxcmci_read_response(struct mxcmci_host * host,unsigned int stat)
- Line: 483

### mxcmci_readl
- Return type: static u32
- Signature: mxcmci_readl(struct mxcmci_host * host,int reg)
- Line: 185

### mxcmci_readw
- Return type: static u16
- Signature: mxcmci_readw(struct mxcmci_host * host,int reg)
- Line: 201

### mxcmci_remove
- Return type: static void
- Signature: mxcmci_remove(struct platform_device * pdev)
- Line: 1169

### mxcmci_request
- Return type: static void
- Signature: mxcmci_request(struct mmc_host * mmc,struct mmc_request * req)
- Line: 751

### mxcmci_resume
- Return type: static int
- Signature: mxcmci_resume(struct device * dev)
- Line: 1196

### mxcmci_set_clk_rate
- Return type: static void
- Signature: mxcmci_set_clk_rate(struct mxcmci_host * host,unsigned int clk_ios)
- Line: 786

### mxcmci_set_ios
- Return type: static void
- Signature: mxcmci_set_ios(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 835

### mxcmci_set_power
- Return type: static void
- Signature: mxcmci_set_power(struct mxcmci_host * host,unsigned int vdd)
- Line: 219

### mxcmci_setup_data
- Return type: static int
- Signature: mxcmci_setup_data(struct mxcmci_host * host,struct mmc_data * data)
- Line: 286

### mxcmci_setup_dma
- Return type: static int
- Signature: mxcmci_setup_dma(struct mmc_host * mmc)
- Line: 819

### mxcmci_softreset
- Return type: static void
- Signature: mxcmci_softreset(struct mxcmci_host * host)
- Line: 239

### mxcmci_start_cmd
- Return type: static int
- Signature: mxcmci_start_cmd(struct mxcmci_host * host,struct mmc_command * cmd,unsigned int cmdat)
- Line: 364

### mxcmci_suspend
- Return type: static int
- Signature: mxcmci_suspend(struct device * dev)
- Line: 1186

### mxcmci_swap_buffers
- Return type: static void
- Signature: mxcmci_swap_buffers(struct mmc_data * data)
- Line: 283

### mxcmci_swap_buffers
- Return type: static void
- Signature: mxcmci_swap_buffers(struct mmc_data * data)
- Line: 267

### mxcmci_transfer_data
- Return type: static int
- Signature: mxcmci_transfer_data(struct mxcmci_host * host)
- Line: 591

### mxcmci_use_dma
- Return type: static int
- Signature: mxcmci_use_dma(struct mxcmci_host * host)
- Line: 234

### mxcmci_watchdog
- Return type: static void
- Signature: mxcmci_watchdog(struct timer_list * t)
- Line: 956

### mxcmci_writel
- Return type: static void
- Signature: mxcmci_writel(struct mxcmci_host * host,u32 val,int reg)
- Line: 193

### mxcmci_writew
- Return type: static void
- Signature: mxcmci_writew(struct mxcmci_host * host,u16 val,int reg)
- Line: 209

## Structs (1)

### mxcmci_host
- Line: 119
- Members:
  - mmc: mmc_host *
  - base: void __iomem *
  - phys_base: dma_addr_t
  - detect_irq: int
  - dma: dma_chan *
  - desc: dma_async_tx_descriptor *
  - do_dma: int
  - default_irq_mask: int
  - use_sdio: int
  - power_mode: unsigned int
  - pdata: imxmmc_platform_data *
  - req: mmc_request *
  - cmd: mmc_command *
  - data: mmc_data *
  - datasize: unsigned int
  - dma_dir: unsigned int
  - rev_no: u16
  - cmdat: unsigned int
  - clk_ipg: clk *
  - clk_per: clk *
  - clock: int
  - datawork: work_struct
  - lock: spinlock_t
  - burstlen: int
  - dmareq: int
  - dma_slave_config: dma_slave_config
  - dma_data: imx_dma_data
  - watchdog: timer_list
  - devtype: mxcmci_type

## Enums (1)

### mxcmci_type
- Line: 113

## Variables (3)

- static **mxcmci_driver** : platform_driver (line 1215)
- static **mxcmci_of_match** : const struct of_device_id[] (line 159)
- static **mxcmci_ops** : const struct mmc_host_ops (line 984)

## Macros (64)

- **CMD_DAT_CONT_BUS_WIDTH_4** (line 92)
- **CMD_DAT_CONT_CMD_RESP_LONG_OFF** (line 89)
- **CMD_DAT_CONT_DATA_ENABLE** (line 95)
- **CMD_DAT_CONT_INIT** (line 93)
- **CMD_DAT_CONT_RESPONSE_136BIT** (line 97)
- **CMD_DAT_CONT_RESPONSE_48BIT** (line 98)
- **CMD_DAT_CONT_RESPONSE_48BIT_CRC** (line 96)
- **CMD_DAT_CONT_START_READWAIT** (line 91)
- **CMD_DAT_CONT_STOP_READWAIT** (line 90)
- **CMD_DAT_CONT_WRITE** (line 94)
- **DRIVER_NAME** (line 43)
- **INT_BUF_READ_EN** (line 107)
- **INT_BUF_WRITE_EN** (line 108)
- **INT_CARD_INSERTION_EN** (line 103)
- **INT_CARD_INSERTION_WKP_EN** (line 101)
- **INT_CARD_REMOVAL_EN** (line 104)
- **INT_CARD_REMOVAL_WKP_EN** (line 102)
- **INT_DAT0_EN** (line 106)
- **INT_END_CMD_RES_EN** (line 109)
- **INT_READ_OP_EN** (line 111)
- **INT_SDIO_INT_WKP_EN** (line 100)
- **INT_SDIO_IRQ_EN** (line 105)
- **INT_WRITE_OP_DONE_EN** (line 110)
- **MMC_REG_ARG** (line 57)
- **MMC_REG_BLK_LEN** (line 52)
- **MMC_REG_BUFFER_ACCESS** (line 59)
- **MMC_REG_CLK_RATE** (line 48)
- **MMC_REG_CMD** (line 56)
- **MMC_REG_CMD_DAT_CONT** (line 49)
- **MMC_REG_INT_CNTR** (line 55)
- **MMC_REG_NOB** (line 53)
- **MMC_REG_READ_TO** (line 51)
- **MMC_REG_RES_FIFO** (line 58)
- **MMC_REG_RES_TO** (line 50)
- **MMC_REG_REV_NO** (line 54)
- **MMC_REG_STATUS** (line 47)
- **MMC_REG_STR_STP_CLK** (line 46)
- **MXCMCI_TIMEOUT_MS** (line 44)
- **STATUS_BUF_OVFL** (line 72)
- **STATUS_BUF_READ_RDY** (line 80)
- **STATUS_BUF_UND_RUN** (line 71)
- **STATUS_BUF_WRITE_RDY** (line 81)
- **STATUS_CARD_BUS_CLK_RUN** (line 79)
- **STATUS_CARD_INSERTION** (line 65)
- **STATUS_CARD_REMOVAL** (line 66)
- **STATUS_CRC_READ_ERR** (line 83)
- **STATUS_CRC_WRITE_ERR** (line 84)
- **STATUS_DATA_TRANS_DONE** (line 76)
- **STATUS_END_CMD_RESP** (line 74)
- **STATUS_ERR_MASK** (line 87)
- **STATUS_READ_OP_DONE** (line 77)
- **STATUS_RESP_CRC_ERR** (line 82)
- **STATUS_SDIO_INT_ACTIVE** (line 73)
- **STATUS_TIME_OUT_READ** (line 86)
- **STATUS_TIME_OUT_RESP** (line 85)
- **STATUS_WRITE_OP_DONE** (line 75)
- **STATUS_WR_CRC_ERROR_CODE_MASK** (line 78)
- **STATUS_XBUF_EMPTY** (line 68)
- **STATUS_XBUF_FULL** (line 70)
- **STATUS_YBUF_EMPTY** (line 67)
- **STATUS_YBUF_FULL** (line 69)
- **STR_STP_CLK_RESET** (line 61)
- **STR_STP_CLK_START_CLK** (line 62)
- **STR_STP_CLK_STOP_CLK** (line 63)
