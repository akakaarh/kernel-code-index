# drivers/spi/spi-nxp-fspi.c

Subsystem: drivers/spi

## Functions (29)

### erratum_err050568
- Return type: static void
- Signature: erratum_err050568(struct nxp_fspi * f)
- Line: 1096

### fspi_readl
- Return type: static u32
- Signature: fspi_readl(struct nxp_fspi * f,void __iomem * addr)
- Line: 433

### fspi_readl_poll_tout
- Return type: static int
- Signature: fspi_readl_poll_tout(struct nxp_fspi * f,void __iomem * base,u32 mask,u32 delay_us,u32 timeout_us,bool c)
- Line: 523

### fspi_writel
- Return type: static void
- Signature: fspi_writel(struct nxp_fspi * f,u32 val,void __iomem * addr)
- Line: 425

### needs_ip_only
- Return type: static int
- Signature: needs_ip_only(struct nxp_fspi * f)
- Line: 413

### nxp_fspi_adjust_op_size
- Return type: static int
- Signature: nxp_fspi_adjust_op_size(struct spi_mem * mem,struct spi_mem_op * op)
- Line: 1073

### nxp_fspi_check_buswidth
- Return type: static int
- Signature: nxp_fspi_check_buswidth(struct nxp_fspi * f,u8 width)
- Line: 456

### nxp_fspi_cleanup
- Return type: static void
- Signature: nxp_fspi_cleanup(void * data)
- Line: 1268

### nxp_fspi_clk_disable_unprep
- Return type: static void
- Signature: nxp_fspi_clk_disable_unprep(struct nxp_fspi * f)
- Line: 654

### nxp_fspi_clk_prep_enable
- Return type: static int
- Signature: nxp_fspi_clk_prep_enable(struct nxp_fspi * f)
- Line: 634

### nxp_fspi_default_setup
- Return type: static int
- Signature: nxp_fspi_default_setup(struct nxp_fspi * f)
- Line: 1135

### nxp_fspi_dll_calibration
- Return type: static void
- Signature: nxp_fspi_dll_calibration(struct nxp_fspi * f)
- Line: 702

### nxp_fspi_dll_override
- Return type: static void
- Signature: nxp_fspi_dll_override(struct nxp_fspi * f)
- Line: 742

### nxp_fspi_do_op
- Return type: static int
- Signature: nxp_fspi_do_op(struct nxp_fspi * f,const struct spi_mem_op * op)
- Line: 986

### nxp_fspi_exec_op
- Return type: static int
- Signature: nxp_fspi_exec_op(struct spi_mem * mem,const struct spi_mem_op * op)
- Line: 1027

### nxp_fspi_fill_txfifo
- Return type: static void
- Signature: nxp_fspi_fill_txfifo(struct nxp_fspi * f,const struct spi_mem_op * op)
- Line: 890

### nxp_fspi_get_name
- Return type: static const char *
- Signature: nxp_fspi_get_name(struct spi_mem * mem)
- Line: 1228

### nxp_fspi_invalid
- Return type: static void
- Signature: nxp_fspi_invalid(struct nxp_fspi * f)
- Line: 545

### nxp_fspi_irq_handler
- Return type: static irqreturn_t
- Signature: nxp_fspi_irq_handler(int irq,void * dev_id)
- Line: 441

### nxp_fspi_prepare_lut
- Return type: static void
- Signature: nxp_fspi_prepare_lut(struct nxp_fspi * f,const struct spi_mem_op * op)
- Line: 559

### nxp_fspi_probe
- Return type: static int
- Signature: nxp_fspi_probe(struct platform_device * pdev)
- Line: 1286

### nxp_fspi_read_ahb
- Return type: static int
- Signature: nxp_fspi_read_ahb(struct nxp_fspi * f,const struct spi_mem_op * op)
- Line: 860

### nxp_fspi_read_rxfifo
- Return type: static void
- Signature: nxp_fspi_read_rxfifo(struct nxp_fspi * f,const struct spi_mem_op * op)
- Line: 935

### nxp_fspi_runtime_resume
- Return type: static int
- Signature: nxp_fspi_runtime_resume(struct device * dev)
- Line: 1403

### nxp_fspi_runtime_suspend
- Return type: static int
- Signature: nxp_fspi_runtime_suspend(struct device * dev)
- Line: 1394

### nxp_fspi_select_mem
- Return type: static void
- Signature: nxp_fspi_select_mem(struct nxp_fspi * f,struct spi_device * spi,const struct spi_mem_op * op)
- Line: 786

### nxp_fspi_select_rx_sample_clk_source
- Return type: static void
- Signature: nxp_fspi_select_rx_sample_clk_source(struct nxp_fspi * f,bool op_is_dtr)
- Line: 677

### nxp_fspi_supports_op
- Return type: static bool
- Signature: nxp_fspi_supports_op(struct spi_mem * mem,const struct spi_mem_op * op)
- Line: 469

### nxp_fspi_suspend
- Return type: static int
- Signature: nxp_fspi_suspend(struct device * dev)
- Line: 1423

## Structs (2)

### nxp_fspi
- Line: 390
- Members:
  - rxfifo: unsigned int
  - txfifo: unsigned int
  - ahb_buf_size: unsigned int
  - quirks: unsigned int
  - lut_num: unsigned int
  - little_endian: bool
  - iobase: void __iomem *
  - ahb_addr: void __iomem *
  - memmap_phy: u32
  - memmap_phy_size: u32
  - memmap_start: u32
  - memmap_len: u32
  - clk: clk *
  - clk_en: clk *
  - dev: device *
  - c: completion
  - devtype_data: nxp_fspi_devtype_data *
  - lock: mutex
  - pm_qos_req: pm_qos_request
  - selected: int
  - flags: int
  - pre_op_rate: unsigned long
  - max_rate: unsigned long

### nxp_fspi_devtype_data
- Line: 336
- Members:
  - rxfifo: unsigned int
  - txfifo: unsigned int
  - ahb_buf_size: unsigned int
  - quirks: unsigned int
  - lut_num: unsigned int
  - little_endian: bool
  - iobase: void __iomem *
  - ahb_addr: void __iomem *
  - memmap_phy: u32
  - memmap_phy_size: u32
  - memmap_start: u32
  - memmap_len: u32
  - clk: clk *
  - clk_en: clk *
  - dev: device *
  - c: completion
  - devtype_data: nxp_fspi_devtype_data *
  - lock: mutex
  - pm_qos_req: pm_qos_request
  - selected: int
  - flags: int
  - pre_op_rate: unsigned long
  - max_rate: unsigned long

## Variables (12)

- static **imx8dxl_data** : nxp_fspi_devtype_data (line 372)
- static **imx8mm_data** : nxp_fspi_devtype_data (line 354)
- static **imx8qxp_data** : nxp_fspi_devtype_data (line 363)
- static **imx8ulp_data** : nxp_fspi_devtype_data (line 381)
- static **lx2160a_data** : nxp_fspi_devtype_data (line 345)
- static **nxp_fspi_acpi_ids** : const struct acpi_device_id[] (line 1456)
- static **nxp_fspi_driver** : platform_driver (line 1463)
- static **nxp_fspi_dt_ids** : const struct of_device_id[] (line 1444)
- static **nxp_fspi_mem_caps** : const struct spi_controller_mem_caps (line 1257)
- static **nxp_fspi_mem_caps_disable_dtr** : const struct spi_controller_mem_caps (line 1263)
- static **nxp_fspi_mem_ops** : const struct spi_controller_mem_ops (line 1250)
- static **nxp_fspi_pm_ops** : const struct dev_pm_ops (line 1439)

## Macros (209)

- **DCFG_RCWSR1** (line 328)
- **FSPI_AHBCR** (line 100)
- **FSPI_AHBCR_BUFF_EN** (line 103)
- **FSPI_AHBCR_CACH_EN** (line 104)
- **FSPI_AHBCR_CLRRXBUF** (line 106)
- **FSPI_AHBCR_CLRTXBUF** (line 105)
- **FSPI_AHBCR_PAR_EN** (line 107)
- **FSPI_AHBCR_PREF_EN** (line 102)
- **FSPI_AHBCR_RDADDROPT** (line 101)
- **FSPI_AHBRXBUF0CR7_PREF** (line 150)
- **FSPI_AHBRX_BUF0CR0** (line 142)
- **FSPI_AHBRX_BUF0CR1** (line 152)
- **FSPI_AHBRX_BUF1CR0** (line 143)
- **FSPI_AHBRX_BUF1CR1** (line 153)
- **FSPI_AHBRX_BUF2CR0** (line 144)
- **FSPI_AHBRX_BUF2CR1** (line 154)
- **FSPI_AHBRX_BUF3CR0** (line 145)
- **FSPI_AHBRX_BUF3CR1** (line 155)
- **FSPI_AHBRX_BUF4CR0** (line 146)
- **FSPI_AHBRX_BUF4CR1** (line 156)
- **FSPI_AHBRX_BUF5CR0** (line 147)
- **FSPI_AHBRX_BUF5CR1** (line 157)
- **FSPI_AHBRX_BUF6CR0** (line 148)
- **FSPI_AHBRX_BUF6CR1** (line 158)
- **FSPI_AHBRX_BUF7CR0** (line 149)
- **FSPI_AHBRX_BUF7CR1** (line 159)
- **FSPI_AHBSPNST** (line 247)
- **FSPI_AHBSPNST_ACTIVE** (line 250)
- **FSPI_AHBSPNST_BUFID**(x) (line 249)
- **FSPI_AHBSPNST_DATLFT**(x) (line 248)
- **FSPI_BUFXCR_INVALID_MSTRID** (line 141)
- **FSPI_DLLACR** (line 212)
- **FSPI_DLLACR_DLLEN** (line 216)
- **FSPI_DLLACR_DLLRESET** (line 215)
- **FSPI_DLLACR_OVRDEN** (line 213)
- **FSPI_DLLACR_SLVDLY**(x) (line 214)
- **FSPI_DLLBCR** (line 218)
- **FSPI_DLLBCR_DLLEN** (line 222)
- **FSPI_DLLBCR_DLLRESET** (line 221)
- **FSPI_DLLBCR_OVRDEN** (line 219)
- **FSPI_DLLBCR_SLVDLY**(x) (line 220)
- **FSPI_DLPR** (line 200)
- **FSPI_DTR_MODE** (line 405)
- **FSPI_FLSHA1CR0** (line 161)
- **FSPI_FLSHA1CR1** (line 168)
- **FSPI_FLSHA1CR2** (line 178)
- **FSPI_FLSHA2CR0** (line 162)
- **FSPI_FLSHA2CR1** (line 169)
- **FSPI_FLSHA2CR2** (line 179)
- **FSPI_FLSHB1CR0** (line 163)
- **FSPI_FLSHB1CR1** (line 170)
- **FSPI_FLSHB1CR2** (line 180)
- **FSPI_FLSHB2CR0** (line 164)
- **FSPI_FLSHB2CR1** (line 171)
- **FSPI_FLSHB2CR2** (line 181)
- **FSPI_FLSHXCR0_SZ**(x) (line 166)
- **FSPI_FLSHXCR0_SZ_KB** (line 165)
- **FSPI_FLSHXCR1_CAS**(x) (line 173)
- **FSPI_FLSHXCR1_CSINTR**(x) (line 172)
- **FSPI_FLSHXCR1_TCSH**(x) (line 175)
- **FSPI_FLSHXCR1_TCSS**(x) (line 176)
- **FSPI_FLSHXCR1_WA** (line 174)
- **FSPI_FLSHXCR2_ARDSEQI_SHIFT** (line 187)
- **FSPI_FLSHXCR2_ARDSEQN_SHIFT** (line 186)
- **FSPI_FLSHXCR2_AWRSEQI_SHIFT** (line 185)
- **FSPI_FLSHXCR2_AWRSEQN_SHIFT** (line 184)
- **FSPI_FLSHXCR2_AWRWAIT** (line 183)
- **FSPI_FLSHXCR2_CLRINSP** (line 182)
- **FSPI_INTEN** (line 109)
- **FSPI_INTEN_AHBCMDERR** (line 115)
- **FSPI_INTEN_AHBCMDGE** (line 117)
- **FSPI_INTEN_DATALRNFL** (line 112)
- **FSPI_INTEN_IPCMDDONE** (line 119)
- **FSPI_INTEN_IPCMDERR** (line 116)
- **FSPI_INTEN_IPCMDGE** (line 118)
- **FSPI_INTEN_IPRXWA** (line 114)
- **FSPI_INTEN_IPTXWE** (line 113)
- **FSPI_INTEN_SCLKSBRD** (line 111)
- **FSPI_INTEN_SCLKSBWR** (line 110)
- **FSPI_INTR** (line 121)
- **FSPI_INTR_AHBCMDERR** (line 127)
- **FSPI_INTR_AHBCMDGE** (line 129)
- **FSPI_INTR_DATALRNFL** (line 124)
- **FSPI_INTR_IPCMDDONE** (line 131)
- **FSPI_INTR_IPCMDERR** (line 128)
- **FSPI_INTR_IPCMDGE** (line 130)
- **FSPI_INTR_IPRXWA** (line 126)
- **FSPI_INTR_IPTXWE** (line 125)
- **FSPI_INTR_SCLKSBRD** (line 123)
- **FSPI_INTR_SCLKSBWR** (line 122)
- **FSPI_IPCMD** (line 197)
- **FSPI_IPCMD_TRG** (line 198)
- **FSPI_IPCR0** (line 189)
- **FSPI_IPCR1** (line 191)
- **FSPI_IPCR1_IDATSZ**(x) (line 195)
- **FSPI_IPCR1_IPAREN** (line 192)
- **FSPI_IPCR1_SEQID_SHIFT** (line 194)
- **FSPI_IPCR1_SEQNUM_SHIFT** (line 193)
- **FSPI_IPRXFCR** (line 202)
- **FSPI_IPRXFCR_CLR** (line 203)
- **FSPI_IPRXFCR_DMA_EN** (line 204)
- **FSPI_IPRXFCR_WMRK**(x) (line 205)
- **FSPI_IPRXFSTS** (line 252)
- **FSPI_IPRXFSTS_FILL**(x) (line 254)
- **FSPI_IPRXFSTS_RDCNTR**(x) (line 253)
- **FSPI_IPTXFCR** (line 207)
- **FSPI_IPTXFCR_CLR** (line 208)
- **FSPI_IPTXFCR_DMA_EN** (line 209)
- **FSPI_IPTXFCR_WMRK**(x) (line 210)
- **FSPI_IPTXFSTS** (line 256)
- **FSPI_IPTXFSTS_FILL**(x) (line 258)
- **FSPI_IPTXFSTS_WRCNTR**(x) (line 257)
- **FSPI_LCKCR** (line 136)
- **FSPI_LCKER_LOCK** (line 138)
- **FSPI_LCKER_UNLOCK** (line 139)
- **FSPI_LUTKEY** (line 133)
- **FSPI_LUTKEY_VALUE** (line 134)
- **FSPI_LUT_BASE** (line 263)
- **FSPI_MCR0** (line 66)
- **FSPI_MCR0_AHB_TIMEOUT**(x) (line 67)
- **FSPI_MCR0_ARDF_EN** (line 76)
- **FSPI_MCR0_ATDF_EN** (line 75)
- **FSPI_MCR0_DOZE_EN** (line 72)
- **FSPI_MCR0_END_CFG**(x) (line 78)
- **FSPI_MCR0_HSEN** (line 73)
- **FSPI_MCR0_IP_TIMEOUT**(x) (line 68)
- **FSPI_MCR0_LEARN_EN** (line 69)
- **FSPI_MCR0_MDIS** (line 79)
- **FSPI_MCR0_OCTCOMB_EN** (line 71)
- **FSPI_MCR0_RXCLKSRC**(x) (line 77)
- **FSPI_MCR0_SCRFRUN_EN** (line 70)
- **FSPI_MCR0_SERCLKDIV** (line 74)
- **FSPI_MCR0_SWRST** (line 80)
- **FSPI_MCR1** (line 82)
- **FSPI_MCR1_AHB_TIMEOUT**(x) (line 84)
- **FSPI_MCR1_SEQ_TIMEOUT**(x) (line 83)
- **FSPI_MCR2** (line 86)
- **FSPI_MCR2_ABRCADDR** (line 96)
- **FSPI_MCR2_ABRDATSZ** (line 90)
- **FSPI_MCR2_ABRDUMMY** (line 94)
- **FSPI_MCR2_ABRLEARN** (line 91)
- **FSPI_MCR2_ABRRADDR** (line 97)
- **FSPI_MCR2_ABRWRITE** (line 93)
- **FSPI_MCR2_ABR_CMD** (line 98)
- **FSPI_MCR2_ABR_MODE** (line 95)
- **FSPI_MCR2_ABR_READ** (line 92)
- **FSPI_MCR2_CLRLRPHS** (line 89)
- **FSPI_MCR2_IDLE_WAIT**(x) (line 87)
- **FSPI_MCR2_SAMEDEVICEEN** (line 88)
- **FSPI_NEED_INIT** (line 404)
- **FSPI_QUIRK_DISABLE_DTR** (line 334)
- **FSPI_QUIRK_USE_IP_ONLY** (line 332)
- **FSPI_RFDR** (line 260)
- **FSPI_RPM_TIMEOUT** (line 63)
- **FSPI_STS0** (line 224)
- **FSPI_STS0_ARB_IDLE** (line 228)
- **FSPI_STS0_CMD_SRC**(x) (line 227)
- **FSPI_STS0_DLPHA**(x) (line 226)
- **FSPI_STS0_DLPHB**(x) (line 225)
- **FSPI_STS0_SEQ_IDLE** (line 229)
- **FSPI_STS1** (line 231)
- **FSPI_STS1_AHB_ERRCD**(x) (line 234)
- **FSPI_STS1_AHB_ERRID**(x) (line 235)
- **FSPI_STS1_IP_ERRCD**(x) (line 232)
- **FSPI_STS1_IP_ERRID**(x) (line 233)
- **FSPI_STS2** (line 237)
- **FSPI_STS2_AB_LOCK** (line 242)
- **FSPI_STS2_AREFLOCK** (line 240)
- **FSPI_STS2_ASLVLOCK** (line 241)
- **FSPI_STS2_BREFLOCK** (line 238)
- **FSPI_STS2_BSLVLOCK** (line 239)
- **FSPI_TFDR** (line 261)
- **INSTR_SHIFT** (line 316)
- **LUT_ADDR** (line 270)
- **LUT_ADDR_DDR** (line 284)
- **LUT_CADDR_DDR** (line 285)
- **LUT_CADDR_SDR** (line 271)
- **LUT_CMD** (line 269)
- **LUT_CMD_DDR** (line 283)
- **LUT_DATSZ_DDR** (line 293)
- **LUT_DATSZ_SDR** (line 279)
- **LUT_DEF**(idx,ins,pad,opr) (line 320)
- **LUT_DUMMY** (line 280)
- **LUT_DUMMY_DDR** (line 294)
- **LUT_DUMMY_RWDS_DDR** (line 295)
- **LUT_DUMMY_RWDS_SDR** (line 281)
- **LUT_JMP_ON_CS** (line 282)
- **LUT_LEARN_DDR** (line 292)
- **LUT_LEARN_SDR** (line 278)
- **LUT_MODE** (line 272)
- **LUT_MODE2** (line 273)
- **LUT_MODE2_DDR** (line 287)
- **LUT_MODE4** (line 274)
- **LUT_MODE4_DDR** (line 288)
- **LUT_MODE8** (line 275)
- **LUT_MODE8_DDR** (line 289)
- **LUT_MODE_DDR** (line 286)
- **LUT_NXP_READ** (line 277)
- **LUT_NXP_WRITE** (line 276)
- **LUT_PAD**(x) (line 305)
- **LUT_READ_DDR** (line 291)
- **LUT_STOP** (line 268)
- **LUT_WRITE_DDR** (line 290)
- **NXP_FSPI_MAX_CHIPSELECT** (line 325)
- **NXP_FSPI_MIN_IOMAP** (line 326)
- **OPRND_SHIFT** (line 317)
- **PAD_SHIFT** (line 315)
- **POLL_TOUT** (line 324)
- **SYS_PLL_RAT** (line 329)
