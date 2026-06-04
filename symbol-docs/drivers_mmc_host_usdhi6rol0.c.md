# drivers/mmc/host/usdhi6rol0.c

Subsystem: drivers/mmc

## Functions (56)

### usdhi6_blk_bounce
- Return type: static void
- Signature: usdhi6_blk_bounce(struct usdhi6_host * host,struct scatterlist * sg)
- Line: 314

### usdhi6_blk_read
- Return type: static int
- Signature: usdhi6_blk_read(struct usdhi6_host * host)
- Line: 1262

### usdhi6_blk_write
- Return type: static int
- Signature: usdhi6_blk_write(struct usdhi6_host * host)
- Line: 1302

### usdhi6_card_busy
- Return type: static int
- Signature: usdhi6_card_busy(struct mmc_host * mmc)
- Line: 1189

### usdhi6_cd
- Return type: static irqreturn_t
- Signature: usdhi6_cd(int irq,void * dev_id)
- Line: 1650

### usdhi6_clk_set
- Return type: static void
- Signature: usdhi6_clk_set(struct usdhi6_host * host,struct mmc_ios * ios)
- Line: 727

### usdhi6_cmd_flags
- Return type: static int
- Signature: usdhi6_cmd_flags(struct usdhi6_host * host)
- Line: 932

### usdhi6_dma_check_error
- Return type: static void
- Signature: usdhi6_dma_check_error(struct usdhi6_host * host)
- Line: 639

### usdhi6_dma_complete
- Return type: static void
- Signature: usdhi6_dma_complete(void * arg)
- Line: 550

### usdhi6_dma_kick
- Return type: static void
- Signature: usdhi6_dma_kick(struct usdhi6_host * host)
- Line: 665

### usdhi6_dma_kill
- Return type: static void
- Signature: usdhi6_dma_kill(struct usdhi6_host * host)
- Line: 626

### usdhi6_dma_release
- Return type: static void
- Signature: usdhi6_dma_release(struct usdhi6_host * host)
- Line: 517

### usdhi6_dma_request
- Return type: static void
- Signature: usdhi6_dma_request(struct usdhi6_host * host,phys_addr_t start)
- Line: 673

### usdhi6_dma_setup
- Return type: static int
- Signature: usdhi6_dma_setup(struct usdhi6_host * host,struct dma_chan * chan,enum dma_transfer_direction dir)
- Line: 566

### usdhi6_dma_start
- Return type: static int
- Signature: usdhi6_dma_start(struct usdhi6_host * host)
- Line: 615

### usdhi6_dma_stop_unmap
- Return type: static void
- Signature: usdhi6_dma_stop_unmap(struct usdhi6_host * host)
- Line: 532

### usdhi6_enable_sdio_irq
- Return type: static void
- Signature: usdhi6_enable_sdio_irq(struct mmc_host * mmc,int enable)
- Line: 1141

### usdhi6_end_cmd
- Return type: static bool
- Signature: usdhi6_end_cmd(struct usdhi6_host * host)
- Line: 1367

### usdhi6_error_code
- Return type: static int
- Signature: usdhi6_error_code(struct usdhi6_host * host)
- Line: 272

### usdhi6_get_cd
- Return type: static int
- Signature: usdhi6_get_cd(struct mmc_host * mmc)
- Line: 1109

### usdhi6_get_ro
- Return type: static int
- Signature: usdhi6_get_ro(struct mmc_host * mmc)
- Line: 1125

### usdhi6_irq_enable
- Return type: static void
- Signature: usdhi6_irq_enable(struct usdhi6_host * host,u32 info1,u32 info2)
- Line: 239

### usdhi6_mask_all
- Return type: static void
- Signature: usdhi6_mask_all(struct usdhi6_host * host)
- Line: 267

### usdhi6_mread_block
- Return type: static bool
- Signature: usdhi6_mread_block(struct usdhi6_host * host)
- Line: 1426

### usdhi6_mwrite_block
- Return type: static bool
- Signature: usdhi6_mwrite_block(struct usdhi6_host * host)
- Line: 1453

### usdhi6_only_cd
- Return type: static void
- Signature: usdhi6_only_cd(struct usdhi6_host * host)
- Line: 261

### usdhi6_probe
- Return type: static int
- Signature: usdhi6_probe(struct platform_device * pdev)
- Line: 1744

### usdhi6_read
- Return type: static u32
- Signature: usdhi6_read(struct usdhi6_host * host,u32 reg)
- Line: 223

### usdhi6_read16
- Return type: static u16
- Signature: usdhi6_read16(struct usdhi6_host * host,u32 reg)
- Line: 231

### usdhi6_read_block
- Return type: static bool
- Signature: usdhi6_read_block(struct usdhi6_host * host)
- Line: 1407

### usdhi6_remove
- Return type: static void
- Signature: usdhi6_remove(struct platform_device * pdev)
- Line: 1878

### usdhi6_request
- Return type: static void
- Signature: usdhi6_request(struct mmc_host * mmc,struct mmc_request * mrq)
- Line: 1091

### usdhi6_request_done
- Return type: static void
- Signature: usdhi6_request_done(struct usdhi6_host * host)
- Line: 901

### usdhi6_reset
- Return type: static int
- Signature: usdhi6_reset(struct usdhi6_host * host)
- Line: 804

### usdhi6_resp_cmd12
- Return type: static void
- Signature: usdhi6_resp_cmd12(struct usdhi6_host * host)
- Line: 1210

### usdhi6_resp_read
- Return type: static void
- Signature: usdhi6_resp_read(struct usdhi6_host * host)
- Line: 1216

### usdhi6_rq_start
- Return type: static int
- Signature: usdhi6_rq_start(struct usdhi6_host * host)
- Line: 985

### usdhi6_sd
- Return type: static irqreturn_t
- Signature: usdhi6_sd(int irq,void * dev_id)
- Line: 1581

### usdhi6_sd_bh
- Return type: static irqreturn_t
- Signature: usdhi6_sd_bh(int irq,void * dev_id)
- Line: 1468

### usdhi6_sdio
- Return type: static irqreturn_t
- Signature: usdhi6_sdio(int irq,void * dev_id)
- Line: 1633

### usdhi6_set_ios
- Return type: static void
- Signature: usdhi6_set_ios(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 818

### usdhi6_set_pinstates
- Return type: static int
- Signature: usdhi6_set_pinstates(struct usdhi6_host * host,int voltage)
- Line: 1158

### usdhi6_set_power
- Return type: static void
- Signature: usdhi6_set_power(struct usdhi6_host * host,struct mmc_ios * ios)
- Line: 794

### usdhi6_sg_advance
- Return type: static void
- Signature: usdhi6_sg_advance(struct usdhi6_host * host)
- Line: 435

### usdhi6_sg_map
- Return type: static void *
- Signature: usdhi6_sg_map(struct usdhi6_host * host)
- Line: 355

### usdhi6_sg_prep
- Return type: static void
- Signature: usdhi6_sg_prep(struct usdhi6_host * host)
- Line: 342

### usdhi6_sg_unmap
- Return type: static void
- Signature: usdhi6_sg_unmap(struct usdhi6_host * host,bool force)
- Line: 395

### usdhi6_sig_volt_switch
- Return type: static int
- Signature: usdhi6_sig_volt_switch(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 1174

### usdhi6_stop_cmd
- Return type: static int
- Signature: usdhi6_stop_cmd(struct usdhi6_host * host)
- Line: 1345

### usdhi6_timeout_set
- Return type: static void
- Signature: usdhi6_timeout_set(struct usdhi6_host * host)
- Line: 872

### usdhi6_timeout_work
- Return type: static void
- Signature: usdhi6_timeout_work(struct work_struct * work)
- Line: 1681

### usdhi6_wait_for_brwe
- Return type: static void
- Signature: usdhi6_wait_for_brwe(struct usdhi6_host * host,bool read)
- Line: 254

### usdhi6_wait_for_resp
- Return type: static void
- Signature: usdhi6_wait_for_resp(struct usdhi6_host * host)
- Line: 247

### usdhi6_write
- Return type: static void
- Signature: usdhi6_write(struct usdhi6_host * host,u32 reg,u32 data)
- Line: 209

### usdhi6_write16
- Return type: static void
- Signature: usdhi6_write16(struct usdhi6_host * host,u32 reg,u16 data)
- Line: 216

### usdhi6_write_block
- Return type: static bool
- Signature: usdhi6_write_block(struct usdhi6_host * host)
- Line: 1439

## Structs (2)

### usdhi6_host
- Line: 158
- Members:
  - page: page *
  - mapped: void *
  - mmc: mmc_host *
  - mrq: mmc_request *
  - base: void __iomem *
  - clk: clk *
  - pg: usdhi6_page
  - blk_page: void *
  - offset: size_t
  - head_len: size_t
  - head_pg: usdhi6_page
  - bounce_sg: scatterlist
  - bounce_buf: u8[512]
  - sg: scatterlist *
  - page_idx: int
  - wait: usdhi6_wait_for
  - status_mask: u32
  - status2_mask: u32
  - sdio_mask: u32
  - io_error: u32
  - irq_status: u32
  - imclk: unsigned long
  - rate: unsigned long
  - app_cmd: bool
  - timeout_work: delayed_work
  - timeout: unsigned long
  - chan_rx: dma_chan *
  - chan_tx: dma_chan *
  - dma_active: bool
  - pinctrl: pinctrl *
  - pins_uhs: pinctrl_state *

### usdhi6_page
- Line: 153
- Members:
  - page: page *
  - mapped: void *
  - mmc: mmc_host *
  - mrq: mmc_request *
  - base: void __iomem *
  - clk: clk *
  - pg: usdhi6_page
  - blk_page: void *
  - offset: size_t
  - head_len: size_t
  - head_pg: usdhi6_page
  - bounce_sg: scatterlist
  - bounce_buf: u8[512]
  - sg: scatterlist *
  - page_idx: int
  - wait: usdhi6_wait_for
  - status_mask: u32
  - status2_mask: u32
  - sdio_mask: u32
  - io_error: u32
  - irq_status: u32
  - imclk: unsigned long
  - rate: unsigned long
  - app_cmd: bool
  - timeout_work: delayed_work
  - timeout: unsigned long
  - chan_rx: dma_chan *
  - chan_tx: dma_chan *
  - dma_active: bool
  - pinctrl: pinctrl *
  - pins_uhs: pinctrl_state *

## Enums (1)

### usdhi6_wait_for
- Line: 141

## Variables (3)

- static **usdhi6_driver** : platform_driver (line 1890)
- static **usdhi6_of_match** : const struct of_device_id[] (line 1738)
- static **usdhi6_ops** : const struct mmc_host_ops (line 1198)

## Macros (84)

- **USDHI6_CC_EXT_MODE** (line 52)
- **USDHI6_CC_EXT_MODE_SDRW** (line 70)
- **USDHI6_HOST_MODE** (line 55)
- **USDHI6_MIN_DMA** (line 137)
- **USDHI6_REQ_TIMEOUT_MS** (line 139)
- **USDHI6_SDIF_MODE** (line 56)
- **USDHI6_SDIO_INFO1** (line 50)
- **USDHI6_SDIO_INFO1_EXPUB52** (line 118)
- **USDHI6_SDIO_INFO1_EXWT** (line 119)
- **USDHI6_SDIO_INFO1_IOIRQ** (line 117)
- **USDHI6_SDIO_INFO1_IRQ** (line 134)
- **USDHI6_SDIO_INFO1_MASK** (line 51)
- **USDHI6_SDIO_MODE** (line 49)
- **USDHI6_SD_ARG** (line 32)
- **USDHI6_SD_BUF0** (line 48)
- **USDHI6_SD_CLK_CTRL** (line 43)
- **USDHI6_SD_CLK_CTRL_DIV_MASK** (line 132)
- **USDHI6_SD_CLK_CTRL_SCLKEN** (line 112)
- **USDHI6_SD_CMD** (line 30)
- **USDHI6_SD_CMD_APP** (line 58)
- **USDHI6_SD_CMD_CMD12_AUTO_OFF** (line 68)
- **USDHI6_SD_CMD_DATA** (line 65)
- **USDHI6_SD_CMD_MODE_RSP_AUTO** (line 59)
- **USDHI6_SD_CMD_MODE_RSP_NONE** (line 60)
- **USDHI6_SD_CMD_MODE_RSP_R1** (line 61)
- **USDHI6_SD_CMD_MODE_RSP_R1B** (line 62)
- **USDHI6_SD_CMD_MODE_RSP_R2** (line 63)
- **USDHI6_SD_CMD_MODE_RSP_R3** (line 64)
- **USDHI6_SD_CMD_MULTI** (line 67)
- **USDHI6_SD_CMD_READ** (line 66)
- **USDHI6_SD_ERR_STS1** (line 46)
- **USDHI6_SD_ERR_STS1_CRC_NO_ERROR** (line 121)
- **USDHI6_SD_ERR_STS2** (line 47)
- **USDHI6_SD_INFO1** (line 39)
- **USDHI6_SD_INFO1_ACCESS_END** (line 73)
- **USDHI6_SD_INFO1_CARD** (line 97)
- **USDHI6_SD_INFO1_CARD_CD** (line 98)
- **USDHI6_SD_INFO1_CARD_EJECT** (line 96)
- **USDHI6_SD_INFO1_CARD_IN** (line 75)
- **USDHI6_SD_INFO1_CARD_INSERT** (line 95)
- **USDHI6_SD_INFO1_CARD_OUT** (line 74)
- **USDHI6_SD_INFO1_CD** (line 76)
- **USDHI6_SD_INFO1_D3_CARD_IN** (line 79)
- **USDHI6_SD_INFO1_D3_CARD_OUT** (line 78)
- **USDHI6_SD_INFO1_IRQ** (line 106)
- **USDHI6_SD_INFO1_MASK** (line 41)
- **USDHI6_SD_INFO1_RSP_END** (line 72)
- **USDHI6_SD_INFO1_WP** (line 77)
- **USDHI6_SD_INFO2** (line 40)
- **USDHI6_SD_INFO2_BRE** (line 89)
- **USDHI6_SD_INFO2_BWE** (line 90)
- **USDHI6_SD_INFO2_CBSY** (line 92)
- **USDHI6_SD_INFO2_CMD_ERR** (line 81)
- **USDHI6_SD_INFO2_CRC_ERR** (line 82)
- **USDHI6_SD_INFO2_END_ERR** (line 83)
- **USDHI6_SD_INFO2_ERR** (line 100)
- **USDHI6_SD_INFO2_ILA** (line 93)
- **USDHI6_SD_INFO2_IRA_ERR** (line 86)
- **USDHI6_SD_INFO2_IRQ** (line 109)
- **USDHI6_SD_INFO2_IWA_ERR** (line 85)
- **USDHI6_SD_INFO2_MASK** (line 42)
- **USDHI6_SD_INFO2_RSP_TOUT** (line 87)
- **USDHI6_SD_INFO2_SCLKDIVEN** (line 91)
- **USDHI6_SD_INFO2_SDDAT0** (line 88)
- **USDHI6_SD_INFO2_TOUT** (line 84)
- **USDHI6_SD_OPTION** (line 45)
- **USDHI6_SD_OPTION_TIMEOUT_MASK** (line 127)
- **USDHI6_SD_OPTION_TIMEOUT_SHIFT** (line 126)
- **USDHI6_SD_OPTION_WIDTH_1** (line 128)
- **USDHI6_SD_PORT_SEL** (line 31)
- **USDHI6_SD_PORT_SEL_PORTS_SHIFT** (line 130)
- **USDHI6_SD_RSP10** (line 35)
- **USDHI6_SD_RSP32** (line 36)
- **USDHI6_SD_RSP54** (line 37)
- **USDHI6_SD_RSP76** (line 38)
- **USDHI6_SD_SECCNT** (line 34)
- **USDHI6_SD_SIZE** (line 44)
- **USDHI6_SD_STOP** (line 33)
- **USDHI6_SD_STOP_SEC** (line 115)
- **USDHI6_SD_STOP_STP** (line 114)
- **USDHI6_SOFT_RST** (line 53)
- **USDHI6_SOFT_RST_RESERVED** (line 123)
- **USDHI6_SOFT_RST_RESET** (line 124)
- **USDHI6_VERSION** (line 54)
