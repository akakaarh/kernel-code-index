# drivers/mmc/host/wmt-sdmmc.c

Subsystem: drivers/mmc

## Functions (21)

### wmt_complete_data_request
- Return type: static void
- Signature: wmt_complete_data_request(struct wmt_mci_priv * priv)
- Line: 293

### wmt_dma_config
- Return type: static void
- Signature: wmt_dma_config(struct mmc_host * mmc,u32 descaddr,u8 dir)
- Line: 524

### wmt_dma_init
- Return type: static int
- Signature: wmt_dma_init(struct mmc_host * mmc)
- Line: 500

### wmt_dma_init_descriptor
- Return type: static void
- Signature: wmt_dma_init_descriptor(struct wmt_dma_descriptor * desc,u16 req_count,u32 buffer_addr,u32 branch_addr,int end)
- Line: 514

### wmt_dma_start
- Return type: static void
- Signature: wmt_dma_start(struct wmt_mci_priv * priv)
- Line: 550

### wmt_mci_disable_dma
- Return type: static void
- Signature: wmt_mci_disable_dma(struct wmt_mci_priv * priv)
- Line: 287

### wmt_mci_dma_isr
- Return type: static irqreturn_t
- Signature: wmt_mci_dma_isr(int irq_num,void * data)
- Line: 332

### wmt_mci_get_cd
- Return type: static int
- Signature: wmt_mci_get_cd(struct mmc_host * mmc)
- Line: 716

### wmt_mci_get_ro
- Return type: static int
- Signature: wmt_mci_get_ro(struct mmc_host * mmc)
- Line: 709

### wmt_mci_probe
- Return type: static int
- Signature: wmt_mci_probe(struct platform_device * pdev)
- Line: 748

### wmt_mci_read_response
- Return type: static void
- Signature: wmt_mci_read_response(struct mmc_host * mmc)
- Line: 222

### wmt_mci_regular_isr
- Return type: static irqreturn_t
- Signature: wmt_mci_regular_isr(int irq_num,void * data)
- Line: 369

### wmt_mci_remove
- Return type: static void
- Signature: wmt_mci_remove(struct platform_device * pdev)
- Line: 880

### wmt_mci_request
- Return type: static void
- Signature: wmt_mci_request(struct mmc_host * mmc,struct mmc_request * req)
- Line: 558

### wmt_mci_resume
- Return type: static int
- Signature: wmt_mci_resume(struct device * dev)
- Line: 938

### wmt_mci_send_command
- Return type: static int
- Signature: wmt_mci_send_command(struct mmc_host * mmc,u8 command,u8 cmdtype,u32 arg,u8 rsptype)
- Line: 253

### wmt_mci_set_ios
- Return type: static void
- Signature: wmt_mci_set_ios(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 669

### wmt_mci_start_command
- Return type: static void
- Signature: wmt_mci_start_command(struct wmt_mci_priv * priv)
- Line: 245

### wmt_mci_suspend
- Return type: static int
- Signature: wmt_mci_suspend(struct device * dev)
- Line: 914

### wmt_reset_hardware
- Return type: static void
- Signature: wmt_reset_hardware(struct mmc_host * mmc)
- Line: 461

### wmt_set_sd_power
- Return type: static void
- Signature: wmt_set_sd_power(struct wmt_mci_priv * priv,int enable)
- Line: 210

## Structs (3)

### wmt_dma_descriptor
- Line: 167
- Members:
  - flags: u32
  - data_buffer_addr: u32
  - branch_addr: u32
  - reserved1: u32
  - f_min: unsigned int
  - f_max: unsigned int
  - ocr_avail: u32
  - caps: u32
  - max_seg_size: u32
  - max_segs: u32
  - max_blk_size: u32
  - mmc: mmc_host *
  - sdmmc_base: void __iomem *
  - irq_regular: int
  - irq_dma: int
  - dma_desc_buffer: void *
  - dma_desc_device_addr: dma_addr_t
  - cmdcomp: completion
  - datacomp: completion
  - comp_cmd: completion *
  - comp_dma: completion *
  - req: mmc_request *
  - cmd: mmc_command *
  - clk_sdmmc: clk *
  - dev: device *
  - power_inverted: u8
  - cd_inverted: u8

### wmt_mci_caps
- Line: 174
- Members:
  - flags: u32
  - data_buffer_addr: u32
  - branch_addr: u32
  - reserved1: u32
  - f_min: unsigned int
  - f_max: unsigned int
  - ocr_avail: u32
  - caps: u32
  - max_seg_size: u32
  - max_segs: u32
  - max_blk_size: u32
  - mmc: mmc_host *
  - sdmmc_base: void __iomem *
  - irq_regular: int
  - irq_dma: int
  - dma_desc_buffer: void *
  - dma_desc_device_addr: dma_addr_t
  - cmdcomp: completion
  - datacomp: completion
  - comp_cmd: completion *
  - comp_dma: completion *
  - req: mmc_request *
  - cmd: mmc_command *
  - clk_sdmmc: clk *
  - dev: device *
  - power_inverted: u8
  - cd_inverted: u8

### wmt_mci_priv
- Line: 184
- Members:
  - flags: u32
  - data_buffer_addr: u32
  - branch_addr: u32
  - reserved1: u32
  - f_min: unsigned int
  - f_max: unsigned int
  - ocr_avail: u32
  - caps: u32
  - max_seg_size: u32
  - max_segs: u32
  - max_blk_size: u32
  - mmc: mmc_host *
  - sdmmc_base: void __iomem *
  - irq_regular: int
  - irq_dma: int
  - dma_desc_buffer: void *
  - dma_desc_device_addr: dma_addr_t
  - cmdcomp: completion
  - datacomp: completion
  - comp_cmd: completion *
  - comp_dma: completion *
  - req: mmc_request *
  - cmd: mmc_command *
  - clk_sdmmc: clk *
  - dev: device *
  - power_inverted: u8
  - cd_inverted: u8

## Variables (4)

- static **wm8505_caps** : wmt_mci_caps (line 732)
- static **wmt_mci_driver** : platform_driver (line 967)
- static **wmt_mci_dt_ids** : const struct of_device_id[] (line 743)
- static **wmt_mci_ops** : const struct mmc_host_ops (line 724)

## Macros (95)

- **BLKL_CD_POL_HIGH** (line 74)
- **BLKL_CRCERR_ABORT** (line 73)
- **BLKL_DATA3_CD** (line 76)
- **BLKL_GPI_CD** (line 75)
- **BLKL_INT_ENABLE** (line 77)
- **BM_EIGHTBIT_MODE** (line 66)
- **BM_FOURBIT_MODE** (line 65)
- **BM_SD_OFF** (line 67)
- **BM_SD_POWER** (line 69)
- **BM_SOFT_RESET** (line 70)
- **BM_SPI_CS** (line 68)
- **BM_SPI_MODE** (line 64)
- **CTLR_CMD_START** (line 59)
- **CTLR_CMD_WRITE** (line 60)
- **CTLR_FIFO_RESET** (line 61)
- **DMA_CCR_EVT_DATA_RW** (line 157)
- **DMA_CCR_EVT_DESP_READ** (line 156)
- **DMA_CCR_EVT_EARLY_END** (line 158)
- **DMA_CCR_EVT_NO_STATUS** (line 153)
- **DMA_CCR_EVT_OVERRUN** (line 155)
- **DMA_CCR_EVT_SUCCESS** (line 159)
- **DMA_CCR_EVT_UNDERRUN** (line 154)
- **DMA_CCR_IF_TO_PERIPHERAL** (line 149)
- **DMA_CCR_PERIPHERAL_TO_IF** (line 150)
- **DMA_CCR_RUN** (line 148)
- **DMA_GCR_DMA_EN** (line 134)
- **DMA_GCR_SOFT_RESET** (line 135)
- **DMA_IER_INT_EN** (line 138)
- **DMA_ISR_INT_STS** (line 141)
- **DMA_RBR_END** (line 145)
- **DMA_RBR_FORMAT** (line 144)
- **DRIVER_NAME** (line 32)
- **EXT_EIGHTBIT** (line 119)
- **INT0_BLK_TRAN_DONE_INT_EN** (line 81)
- **INT0_CD_INT_EN** (line 82)
- **INT0_DI_INT_EN** (line 83)
- **INT0_MBLK_TRAN_DONE_INT_EN** (line 80)
- **INT1_CMD_RES_TOUT_INT_EN** (line 87)
- **INT1_CMD_RES_TRAN_DONE_INT_EN** (line 86)
- **INT1_DATA_TOUT_INT_EN** (line 89)
- **INT1_MBLK_AUTO_STOP_INT_EN** (line 88)
- **INT1_RCRC_ERR_INT_EN** (line 91)
- **INT1_RESCRC_ERR_INT_EN** (line 90)
- **INT1_WCRC_ERR_INT_EN** (line 92)
- **PDMA_READ** (line 161)
- **PDMA_WRITE** (line 162)
- **SDDMA_BAR** (line 128)
- **SDDMA_CCR** (line 130)
- **SDDMA_CPR** (line 129)
- **SDDMA_DAR** (line 127)
- **SDDMA_DESPR** (line 125)
- **SDDMA_GCR** (line 122)
- **SDDMA_IER** (line 123)
- **SDDMA_ISR** (line 124)
- **SDDMA_RBR** (line 126)
- **SDMMC_ARG** (line 39)
- **SDMMC_BLKCNT** (line 42)
- **SDMMC_BLKLEN** (line 41)
- **SDMMC_BUSMODE** (line 40)
- **SDMMC_CBCR** (line 44)
- **SDMMC_CLK** (line 52)
- **SDMMC_CMD** (line 37)
- **SDMMC_CTLR** (line 36)
- **SDMMC_DMATIMEOUT** (line 55)
- **SDMMC_EXTCTRL** (line 53)
- **SDMMC_INTMASK0** (line 45)
- **SDMMC_INTMASK1** (line 46)
- **SDMMC_RSP** (line 43)
- **SDMMC_RSPTIMEOUT** (line 51)
- **SDMMC_RSPTYPE** (line 38)
- **SDMMC_SBLKLEN** (line 54)
- **SDMMC_STS0** (line 47)
- **SDMMC_STS1** (line 48)
- **SDMMC_STS2** (line 49)
- **SDMMC_STS3** (line 50)
- **STS0_BLK_DONE** (line 99)
- **STS0_CARD_DETECT** (line 100)
- **STS0_CD_DATA3** (line 96)
- **STS0_CD_GPI** (line 97)
- **STS0_DEVICE_INS** (line 101)
- **STS0_MBLK_DONE** (line 98)
- **STS0_WRITE_PROTECT** (line 95)
- **STS1_AUTOSTOP_DONE** (line 107)
- **STS1_CMDRSP_DONE** (line 105)
- **STS1_DATA_TIMEOUT** (line 108)
- **STS1_RCRC_ERR** (line 110)
- **STS1_RSP_CRC_ERR** (line 109)
- **STS1_RSP_TIMEOUT** (line 106)
- **STS1_SDIO_INT** (line 104)
- **STS1_WCRC_ERR** (line 111)
- **STS2_CMD_RES_BUSY** (line 114)
- **STS2_DATARSP_BUSY** (line 115)
- **STS2_DIS_FORCECLK** (line 116)
- **WMT_SD_POWER_OFF** (line 164)
- **WMT_SD_POWER_ON** (line 165)
