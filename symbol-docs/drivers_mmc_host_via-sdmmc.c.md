# drivers/mmc/host/via-sdmmc.c

Subsystem: drivers/mmc

## Functions (30)

### via_init_mmc_host
- Return type: static void
- Signature: via_init_mmc_host(struct via_crdr_mmc_host * host)
- Line: 1027

### via_init_sdc_pm
- Return type: static void
- Signature: via_init_sdc_pm(struct via_crdr_mmc_host * host)
- Line: 1221

### via_print_pcictrl
- Return type: static void
- Signature: via_print_pcictrl(struct via_crdr_mmc_host * host)
- Line: 352

### via_print_sdchc
- Return type: static void
- Signature: via_print_sdchc(struct via_crdr_mmc_host * host)
- Line: 333

### via_pwron_sleep
- Return type: static void
- Signature: via_pwron_sleep(struct via_crdr_mmc_host * sdhost)
- Line: 442

### via_reset_pcictrl
- Return type: static void
- Signature: via_reset_pcictrl(struct via_crdr_mmc_host * host)
- Line: 804

### via_restore_pcictrlreg
- Return type: static void
- Signature: via_restore_pcictrlreg(struct via_crdr_mmc_host * host)
- Line: 385

### via_restore_sdcreg
- Return type: static void
- Signature: via_restore_sdcreg(struct via_crdr_mmc_host * host)
- Line: 422

### via_save_pcictrlreg
- Return type: static void
- Signature: via_save_pcictrlreg(struct via_crdr_mmc_host * host)
- Line: 366

### via_save_sdcreg
- Return type: static void
- Signature: via_save_sdcreg(struct via_crdr_mmc_host * host)
- Line: 402

### via_sd_probe
- Return type: static int
- Signature: via_sd_probe(struct pci_dev * pcidev,const struct pci_device_id * id)
- Line: 1078

### via_sd_remove
- Return type: static void
- Signature: via_sd_remove(struct pci_dev * pcidev)
- Line: 1171

### via_sd_resume
- Return type: static int
- Signature: via_sd_resume(struct device * dev)
- Line: 1272

### via_sd_suspend
- Return type: static int
- Signature: via_sd_suspend(struct device * dev)
- Line: 1255

### via_sdc_card_detect
- Return type: static void
- Signature: via_sdc_card_detect(struct work_struct * work)
- Line: 985

### via_sdc_cmd_isr
- Return type: static void
- Signature: via_sdc_cmd_isr(struct via_crdr_mmc_host * host,u16 intmask)
- Line: 835

### via_sdc_data_isr
- Return type: static void
- Signature: via_sdc_data_isr(struct via_crdr_mmc_host * host,u16 intmask)
- Line: 857

### via_sdc_finish_bh_work
- Return type: static void
- Signature: via_sdc_finish_bh_work(struct work_struct * t)
- Line: 966

### via_sdc_finish_command
- Return type: static void
- Signature: via_sdc_finish_command(struct via_crdr_mmc_host * host)
- Line: 650

### via_sdc_finish_data
- Return type: static void
- Signature: via_sdc_finish_data(struct via_crdr_mmc_host * host)
- Line: 626

### via_sdc_get_response
- Return type: static void
- Signature: via_sdc_get_response(struct via_crdr_mmc_host * host,struct mmc_command * cmd)
- Line: 510

### via_sdc_get_ro
- Return type: static int
- Signature: via_sdc_get_ro(struct mmc_host * mmc)
- Line: 781

### via_sdc_isr
- Return type: static irqreturn_t
- Signature: via_sdc_isr(int irq,void * dev_id)
- Line: 872

### via_sdc_preparedata
- Return type: static void
- Signature: via_sdc_preparedata(struct via_crdr_mmc_host * host,struct mmc_data * data)
- Line: 478

### via_sdc_request
- Return type: static void
- Signature: via_sdc_request(struct mmc_host * mmc,struct mmc_request * mrq)
- Line: 662

### via_sdc_send_command
- Return type: static void
- Signature: via_sdc_send_command(struct via_crdr_mmc_host * host,struct mmc_command * cmd)
- Line: 552

### via_sdc_set_ios
- Return type: static void
- Signature: via_sdc_set_ios(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 720

### via_sdc_set_power
- Return type: static void
- Signature: via_sdc_set_power(struct via_crdr_mmc_host * host,unsigned short power,unsigned int on)
- Line: 694

### via_sdc_timeout
- Return type: static void
- Signature: via_sdc_timeout(struct timer_list * t)
- Line: 935

### via_set_ddma
- Return type: static void
- Signature: via_set_ddma(struct via_crdr_mmc_host * host,dma_addr_t dmaaddr,u32 count,int dir,int enirq)
- Line: 450

## Structs (3)

### pcictrlreg
- Line: 282
- Members:
  - sdcontrol_reg: u32
  - sdcmdarg_reg: u32
  - sdbusmode_reg: u32
  - sdblklen_reg: u32
  - sdresp_reg: u32[4]
  - sdcurblkcnt_reg: u32
  - sdintmask_reg: u32
  - sdstatus_reg: u32
  - sdrsptmo_reg: u32
  - sdclksel_reg: u32
  - sdextctrl_reg: u32
  - reserve: u8[2]
  - pciclkgat_reg: u8
  - pcinfcclk_reg: u8
  - pcimscclk_reg: u8
  - pcisdclk_reg: u8
  - pcicaclk_reg: u8
  - pcidmaclk_reg: u8
  - pciintctrl_reg: u8
  - pciintstatus_reg: u8
  - pcitmoctrl_reg: u8
  - Resv: u8
  - mmc: mmc_host *
  - mrq: mmc_request *
  - cmd: mmc_command *
  - data: mmc_data *
  - mmiobase: void __iomem *
  - sdhc_mmiobase: void __iomem *
  - ddma_mmiobase: void __iomem *
  - pcictrl_mmiobase: void __iomem *
  - pm_pcictrl_reg: pcictrlreg
  - pm_sdhc_reg: sdhcreg
  - carddet_work: work_struct
  - finish_bh_work: work_struct
  - timer: timer_list
  - lock: spinlock_t
  - power: u8
  - reject: int
  - quirks: unsigned int

### sdhcreg
- Line: 268
- Members:
  - sdcontrol_reg: u32
  - sdcmdarg_reg: u32
  - sdbusmode_reg: u32
  - sdblklen_reg: u32
  - sdresp_reg: u32[4]
  - sdcurblkcnt_reg: u32
  - sdintmask_reg: u32
  - sdstatus_reg: u32
  - sdrsptmo_reg: u32
  - sdclksel_reg: u32
  - sdextctrl_reg: u32
  - reserve: u8[2]
  - pciclkgat_reg: u8
  - pcinfcclk_reg: u8
  - pcimscclk_reg: u8
  - pcisdclk_reg: u8
  - pcicaclk_reg: u8
  - pcidmaclk_reg: u8
  - pciintctrl_reg: u8
  - pciintstatus_reg: u8
  - pcitmoctrl_reg: u8
  - Resv: u8
  - mmc: mmc_host *
  - mrq: mmc_request *
  - cmd: mmc_command *
  - data: mmc_data *
  - mmiobase: void __iomem *
  - sdhc_mmiobase: void __iomem *
  - ddma_mmiobase: void __iomem *
  - pcictrl_mmiobase: void __iomem *
  - pm_pcictrl_reg: pcictrlreg
  - pm_sdhc_reg: sdhcreg
  - carddet_work: work_struct
  - finish_bh_work: work_struct
  - timer: timer_list
  - lock: spinlock_t
  - power: u8
  - reject: int
  - quirks: unsigned int

### via_crdr_mmc_host
- Line: 296
- Members:
  - sdcontrol_reg: u32
  - sdcmdarg_reg: u32
  - sdbusmode_reg: u32
  - sdblklen_reg: u32
  - sdresp_reg: u32[4]
  - sdcurblkcnt_reg: u32
  - sdintmask_reg: u32
  - sdstatus_reg: u32
  - sdrsptmo_reg: u32
  - sdclksel_reg: u32
  - sdextctrl_reg: u32
  - reserve: u8[2]
  - pciclkgat_reg: u8
  - pcinfcclk_reg: u8
  - pcimscclk_reg: u8
  - pcisdclk_reg: u8
  - pcicaclk_reg: u8
  - pcidmaclk_reg: u8
  - pciintctrl_reg: u8
  - pciintstatus_reg: u8
  - pcitmoctrl_reg: u8
  - Resv: u8
  - mmc: mmc_host *
  - mrq: mmc_request *
  - cmd: mmc_command *
  - data: mmc_data *
  - mmiobase: void __iomem *
  - sdhc_mmiobase: void __iomem *
  - ddma_mmiobase: void __iomem *
  - pcictrl_mmiobase: void __iomem *
  - pm_pcictrl_reg: pcictrlreg
  - pm_sdhc_reg: sdhcreg
  - carddet_work: work_struct
  - finish_bh_work: work_struct
  - timer: timer_list
  - lock: spinlock_t
  - power: u8
  - reject: int
  - quirks: unsigned int

## Enums (1)

### PCI_HOST_CLK_CONTROL
- Line: 258

## Variables (3)

- static **via_ids** : const struct pci_device_id[] (line 325)
- static **via_sd_driver** : pci_driver (line 1300)
- static **via_sdc_ops** : const struct mmc_host_ops (line 798)

## Macros (112)

- **DRV_NAME** (line 17)
- **PCI_DEVICE_ID_VIA_9530** (line 19)
- **VIA_CMD_TIMEOUT_MS** (line 323)
- **VIA_CRDR_DDMA_OFF** (line 22)
- **VIA_CRDR_DMABASEADD** (line 189)
- **VIA_CRDR_DMACOUNTER** (line 190)
- **VIA_CRDR_DMACTRL** (line 192)
- **VIA_CRDR_DMACTRL_DIR** (line 198)
- **VIA_CRDR_DMACTRL_ENIRQ** (line 199)
- **VIA_CRDR_DMACTRL_SFTRST** (line 200)
- **VIA_CRDR_DMASTART** (line 204)
- **VIA_CRDR_DMASTS** (line 202)
- **VIA_CRDR_MAX_BLOCK_COUNT** (line 70)
- **VIA_CRDR_MAX_BLOCK_LENGTH** (line 71)
- **VIA_CRDR_MAX_CLOCK** (line 26)
- **VIA_CRDR_MIN_CLOCK** (line 25)
- **VIA_CRDR_PCICLKGATT** (line 212)
- **VIA_CRDR_PCICLKGATT_3V3** (line 226)
- **VIA_CRDR_PCICLKGATT_PAD_PWRON** (line 234)
- **VIA_CRDR_PCICLKGATT_SFTRST** (line 218)
- **VIA_CRDR_PCICTRL_OFF** (line 23)
- **VIA_CRDR_PCIDMACLK** (line 238)
- **VIA_CRDR_PCIDMACLK_SDC** (line 239)
- **VIA_CRDR_PCIINTCTRL** (line 241)
- **VIA_CRDR_PCIINTCTRL_SDCIRQEN** (line 242)
- **VIA_CRDR_PCIINTSTATUS** (line 244)
- **VIA_CRDR_PCIINTSTATUS_SDC** (line 245)
- **VIA_CRDR_PCISDCCLK** (line 236)
- **VIA_CRDR_PCITMOCTRL** (line 247)
- **VIA_CRDR_PCITMOCTRL_1024MS** (line 254)
- **VIA_CRDR_PCITMOCTRL_1024US** (line 251)
- **VIA_CRDR_PCITMOCTRL_256MS** (line 252)
- **VIA_CRDR_PCITMOCTRL_256US** (line 250)
- **VIA_CRDR_PCITMOCTRL_32US** (line 249)
- **VIA_CRDR_PCITMOCTRL_512MS** (line 253)
- **VIA_CRDR_PCITMOCTRL_NO** (line 248)
- **VIA_CRDR_PCI_DBG_MODE** (line 33)
- **VIA_CRDR_PCI_WORK_MODE** (line 32)
- **VIA_CRDR_QUIRK_300MS_PWRDELAY** (line 321)
- **VIA_CRDR_SDACTIVE_INTMASK** (line 104)
- **VIA_CRDR_SDBLKLEN** (line 60)
- **VIA_CRDR_SDBLKLEN_GPIDET** (line 68)
- **VIA_CRDR_SDBLKLEN_INTEN** (line 69)
- **VIA_CRDR_SDBUSMODE** (line 56)
- **VIA_CRDR_SDCARG** (line 54)
- **VIA_CRDR_SDCLKSEL** (line 172)
- **VIA_CRDR_SDCTRL** (line 39)
- **VIA_CRDR_SDCTRL_MULTI_RD** (line 45)
- **VIA_CRDR_SDCTRL_MULTI_WR** (line 44)
- **VIA_CRDR_SDCTRL_RSP_NONE** (line 48)
- **VIA_CRDR_SDCTRL_RSP_R1** (line 49)
- **VIA_CRDR_SDCTRL_RSP_R1B** (line 52)
- **VIA_CRDR_SDCTRL_RSP_R2** (line 50)
- **VIA_CRDR_SDCTRL_RSP_R3** (line 51)
- **VIA_CRDR_SDCTRL_SINGLE_RD** (line 43)
- **VIA_CRDR_SDCTRL_SINGLE_WR** (line 42)
- **VIA_CRDR_SDCTRL_START** (line 40)
- **VIA_CRDR_SDCTRL_STOP** (line 46)
- **VIA_CRDR_SDCTRL_WRITE** (line 41)
- **VIA_CRDR_SDCURBLKCNT** (line 78)
- **VIA_CRDR_SDC_OFF** (line 21)
- **VIA_CRDR_SDEXTCTRL** (line 174)
- **VIA_CRDR_SDEXTCTRL_HISPD** (line 182)
- **VIA_CRDR_SDINTMASK** (line 80)
- **VIA_CRDR_SDINTMASK_ASCRDIE** (line 98)
- **VIA_CRDR_SDINTMASK_BDDIE** (line 94)
- **VIA_CRDR_SDINTMASK_CIRIE** (line 95)
- **VIA_CRDR_SDINTMASK_CRDIE** (line 96)
- **VIA_CRDR_SDINTMASK_CRTOIE** (line 97)
- **VIA_CRDR_SDINTMASK_DTIE** (line 99)
- **VIA_CRDR_SDINTMASK_MBDIE** (line 93)
- **VIA_CRDR_SDINTMASK_RCIE** (line 101)
- **VIA_CRDR_SDINTMASK_SCIE** (line 100)
- **VIA_CRDR_SDINTMASK_WCIE** (line 102)
- **VIA_CRDR_SDMODE_4BIT** (line 57)
- **VIA_CRDR_SDMODE_CLK_ON** (line 58)
- **VIA_CRDR_SDRESP0** (line 73)
- **VIA_CRDR_SDRESP1** (line 74)
- **VIA_CRDR_SDRESP2** (line 75)
- **VIA_CRDR_SDRESP3** (line 76)
- **VIA_CRDR_SDRSPTMO** (line 170)
- **VIA_CRDR_SDSTATUS** (line 110)
- **VIA_CRDR_SDSTATUS2** (line 164)
- **VIA_CRDR_SDSTS_ASCRDIE** (line 140)
- **VIA_CRDR_SDSTS_BDD** (line 134)
- **VIA_CRDR_SDSTS_CD** (line 135)
- **VIA_CRDR_SDSTS_CECC** (line 129)
- **VIA_CRDR_SDSTS_CFE** (line 168)
- **VIA_CRDR_SDSTS_CIR** (line 136)
- **VIA_CRDR_SDSTS_CMD_MASK** (line 158)
- **VIA_CRDR_SDSTS_CRD** (line 138)
- **VIA_CRDR_SDSTS_CRTO** (line 139)
- **VIA_CRDR_SDSTS_DATA_MASK** (line 160)
- **VIA_CRDR_SDSTS_DT** (line 141)
- **VIA_CRDR_SDSTS_IGN_MASK** (line 146)
- **VIA_CRDR_SDSTS_INT_MASK** (line 148)
- **VIA_CRDR_SDSTS_IO** (line 137)
- **VIA_CRDR_SDSTS_MBD** (line 133)
- **VIA_CRDR_SDSTS_RC** (line 143)
- **VIA_CRDR_SDSTS_SC** (line 142)
- **VIA_CRDR_SDSTS_SLOTD** (line 131)
- **VIA_CRDR_SDSTS_SLOTG** (line 132)
- **VIA_CRDR_SDSTS_W1C_MASK** (line 153)
- **VIA_CRDR_SDSTS_WC** (line 144)
- **VIA_CRDR_SDSTS_WP** (line 130)
- **VIS_CRDR_SDEXTCTRL_AUTOSTOP_SD** (line 175)
- **VIS_CRDR_SDEXTCTRL_AUTOSTOP_SPI** (line 181)
- **VIS_CRDR_SDEXTCTRL_BAD_CMDA** (line 179)
- **VIS_CRDR_SDEXTCTRL_BAD_DATA** (line 180)
- **VIS_CRDR_SDEXTCTRL_MMC_8BIT** (line 177)
- **VIS_CRDR_SDEXTCTRL_RELD_BLK** (line 178)
- **VIS_CRDR_SDEXTCTRL_SHIFT_9** (line 176)
