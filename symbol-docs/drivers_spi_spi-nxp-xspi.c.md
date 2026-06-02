# drivers/spi/spi-nxp-xspi.c

Subsystem: drivers/spi

## Functions (26)

### needs_ip_only
- Return type: static int
- Signature: needs_ip_only(struct nxp_xspi * xspi)
- Line: 347

### nxp_xspi_adjust_op_size
- Return type: static int
- Signature: nxp_xspi_adjust_op_size(struct spi_mem * mem,struct spi_mem_op * op)
- Line: 1032

### nxp_xspi_ahb_read
- Return type: static int
- Signature: nxp_xspi_ahb_read(struct nxp_xspi * xspi,const struct spi_mem_op * op)
- Line: 771

### nxp_xspi_check_buswidth
- Return type: static int
- Signature: nxp_xspi_check_buswidth(struct nxp_xspi * xspi,u8 width)
- Line: 368

### nxp_xspi_cleanup
- Return type: static void
- Signature: nxp_xspi_cleanup(void * data)
- Line: 1190

### nxp_xspi_config_ahb_buffer
- Return type: static void
- Signature: nxp_xspi_config_ahb_buffer(struct nxp_xspi * xspi)
- Line: 1053

### nxp_xspi_default_setup
- Return type: static int
- Signature: nxp_xspi_default_setup(struct nxp_xspi * xspi)
- Line: 1084

### nxp_xspi_disable_ddr
- Return type: static void
- Signature: nxp_xspi_disable_ddr(struct nxp_xspi * xspi)
- Line: 485

### nxp_xspi_dll_auto
- Return type: static void
- Signature: nxp_xspi_dll_auto(struct nxp_xspi * xspi,unsigned long rate)
- Line: 643

### nxp_xspi_dll_bypass
- Return type: static void
- Signature: nxp_xspi_dll_bypass(struct nxp_xspi * xspi)
- Line: 613

### nxp_xspi_do_op
- Return type: static int
- Signature: nxp_xspi_do_op(struct nxp_xspi * xspi,const struct spi_mem_op * op)
- Line: 904

### nxp_xspi_enable_ddr
- Return type: static void
- Signature: nxp_xspi_enable_ddr(struct nxp_xspi * xspi)
- Line: 516

### nxp_xspi_exec_op
- Return type: static int
- Signature: nxp_xspi_exec_op(struct spi_mem * mem,const struct spi_mem_op * op)
- Line: 988

### nxp_xspi_fill_txfifo
- Return type: static int
- Signature: nxp_xspi_fill_txfifo(struct nxp_xspi * xspi,const struct spi_mem_op * op)
- Line: 802

### nxp_xspi_get_name
- Return type: static const char *
- Signature: nxp_xspi_get_name(struct spi_mem * mem)
- Line: 1155

### nxp_xspi_irq_handler
- Return type: static irqreturn_t
- Signature: nxp_xspi_irq_handler(int irq,void * dev_id)
- Line: 352

### nxp_xspi_prepare_lut
- Return type: static void
- Signature: nxp_xspi_prepare_lut(struct nxp_xspi * xspi,const struct spi_mem_op * op)
- Line: 415

### nxp_xspi_probe
- Return type: static int
- Signature: nxp_xspi_probe(struct platform_device * pdev)
- Line: 1212

### nxp_xspi_read_rxfifo
- Return type: static int
- Signature: nxp_xspi_read_rxfifo(struct nxp_xspi * xspi,const struct spi_mem_op * op)
- Line: 835

### nxp_xspi_resume
- Return type: static int
- Signature: nxp_xspi_resume(struct device * dev)
- Line: 1342

### nxp_xspi_runtime_resume
- Return type: static int
- Signature: nxp_xspi_runtime_resume(struct device * dev)
- Line: 1312

### nxp_xspi_runtime_suspend
- Return type: static int
- Signature: nxp_xspi_runtime_suspend(struct device * dev)
- Line: 1298

### nxp_xspi_select_mem
- Return type: static void
- Signature: nxp_xspi_select_mem(struct nxp_xspi * xspi,struct spi_device * spi,const struct spi_mem_op * op)
- Line: 686

### nxp_xspi_supports_op
- Return type: static bool
- Signature: nxp_xspi_supports_op(struct spi_mem * mem,const struct spi_mem_op * op)
- Line: 373

### nxp_xspi_suspend
- Return type: static int
- Signature: nxp_xspi_suspend(struct device * dev)
- Line: 1329

### nxp_xspi_sw_reset
- Return type: static void
- Signature: nxp_xspi_sw_reset(struct nxp_xspi * xspi)
- Line: 547

## Structs (2)

### nxp_xspi
- Line: 325
- Members:
  - rxfifo: unsigned int
  - txfifo: unsigned int
  - ahb_buf_size: unsigned int
  - quirks: unsigned int
  - iobase: void __iomem *
  - ahb_addr: void __iomem *
  - memmap_phy: u32
  - memmap_phy_size: u32
  - memmap_start: u32
  - memmap_len: u32
  - clk: clk *
  - dev: device *
  - c: completion
  - devtype_data: const struct nxp_xspi_devtype_data *
  - lock: mutex
  - selected: int
  - flags: int
  - pre_op_rate: unsigned long
  - support_max_rate: unsigned long

### nxp_xspi_devtype_data
- Line: 312
- Members:
  - rxfifo: unsigned int
  - txfifo: unsigned int
  - ahb_buf_size: unsigned int
  - quirks: unsigned int
  - iobase: void __iomem *
  - ahb_addr: void __iomem *
  - memmap_phy: u32
  - memmap_phy_size: u32
  - memmap_start: u32
  - memmap_len: u32
  - clk: clk *
  - dev: device *
  - c: completion
  - devtype_data: const struct nxp_xspi_devtype_data *
  - lock: mutex
  - selected: int
  - flags: int
  - pre_op_rate: unsigned long
  - support_max_rate: unsigned long

## Variables (6)

- static **imx94_data** : nxp_xspi_devtype_data (line 319)
- static **nxp_xspi_driver** : platform_driver (line 1372)
- static **nxp_xspi_dt_ids** : const struct of_device_id[] (line 1366)
- static **nxp_xspi_mem_caps** : const struct spi_controller_mem_caps (line 1184)
- static **nxp_xspi_mem_ops** : const struct spi_controller_mem_ops (line 1177)
- static **nxp_xspi_pm_ops** : const struct dev_pm_ops (line 1361)

## Macros (185)

- **INSTR_SHIFT** (line 297)
- **JMP_TO_SEQ** (line 275)
- **LUT_ADDR_DDR** (line 265)
- **LUT_ADDR_SDR** (line 257)
- **LUT_CADDR_DDR** (line 274)
- **LUT_CADDR_SDR** (line 273)
- **LUT_CMD_DDR** (line 272)
- **LUT_CMD_SDR** (line 256)
- **LUT_DATA_LEARN** (line 271)
- **LUT_DEF**(idx,ins,pad,opr) (line 301)
- **LUT_DUMMY** (line 258)
- **LUT_JMP_ON_CS** (line 264)
- **LUT_MODE2_DDR** (line 267)
- **LUT_MODE2_SDR** (line 260)
- **LUT_MODE4_DDR** (line 268)
- **LUT_MODE4_SDR** (line 261)
- **LUT_MODE8_DDR** (line 266)
- **LUT_MODE8_SDR** (line 259)
- **LUT_PAD**(x) (line 286)
- **LUT_READ_DDR** (line 269)
- **LUT_READ_SDR** (line 262)
- **LUT_STOP** (line 255)
- **LUT_WRITE_DDR** (line 270)
- **LUT_WRITE_SDR** (line 263)
- **NXP_XSPI_MAX_CHIPSELECT** (line 306)
- **NXP_XSPI_MIN_IOMAP** (line 305)
- **OPRND_SHIFT** (line 298)
- **PAD_SHIFT** (line 296)
- **POLL_TOUT_US** (line 307)
- **XSPI_64BIT_LE** (line 277)
- **XSPI_BFGENCR** (line 98)
- **XSPI_BFGENCR_ALIGN_MASK** (line 100)
- **XSPI_BFGENCR_PPWF_CLR** (line 101)
- **XSPI_BFGENCR_SEQID_MASK** (line 104)
- **XSPI_BFGENCR_SEQID_WR_EN** (line 103)
- **XSPI_BFGENCR_SEQID_WR_MASK** (line 99)
- **XSPI_BFGENCR_WR_FLUSH_EN** (line 102)
- **XSPI_BUF0CR** (line 90)
- **XSPI_BUF0IND** (line 106)
- **XSPI_BUF1CR** (line 91)
- **XSPI_BUF1IND** (line 107)
- **XSPI_BUF2CR** (line 92)
- **XSPI_BUF2IND** (line 108)
- **XSPI_BUF3CR** (line 93)
- **XSPI_BUF3CR_ADATSZ_MASK** (line 95)
- **XSPI_BUF3CR_ALLMST** (line 94)
- **XSPI_BUF3CR_MSTRID_MASK** (line 96)
- **XSPI_DLLCRA** (line 110)
- **XSPI_DLLCRA_DLLEN** (line 111)
- **XSPI_DLLCRA_DLLRES_MASK** (line 114)
- **XSPI_DLLCRA_DLL_CDL8** (line 119)
- **XSPI_DLLCRA_DLL_REFCNTR_MASK** (line 113)
- **XSPI_DLLCRA_FREQEN** (line 112)
- **XSPI_DLLCRA_SLAVE_AUTO_UPDT** (line 120)
- **XSPI_DLLCRA_SLV_DLL_BYPASS** (line 122)
- **XSPI_DLLCRA_SLV_DLY_COARSE_MASK** (line 117)
- **XSPI_DLLCRA_SLV_DLY_FINE_MASK** (line 118)
- **XSPI_DLLCRA_SLV_DLY_MASK** (line 116)
- **XSPI_DLLCRA_SLV_EN** (line 121)
- **XSPI_DLLCRA_SLV_FINE_MASK** (line 115)
- **XSPI_DLLCRA_SLV_UPD** (line 123)
- **XSPI_DLLSR** (line 146)
- **XSPI_DLLSR_DLLA_FINE_UNDERFLOW** (line 150)
- **XSPI_DLLSR_DLLA_LOCK** (line 147)
- **XSPI_DLLSR_DLLA_RANGE_ERR** (line 149)
- **XSPI_DLLSR_SLVA_LOCK** (line 148)
- **XSPI_DTR_PROTO** (line 339)
- **XSPI_ERRSTAT** (line 241)
- **XSPI_FLSHCR** (line 85)
- **XSPI_FLSHCR_TCSH_MASK** (line 87)
- **XSPI_FLSHCR_TCSS_MASK** (line 88)
- **XSPI_FLSHCR_TDH_MASK** (line 86)
- **XSPI_FR** (line 177)
- **XSPI_FRAD0_WORD2** (line 223)
- **XSPI_FRAD0_WORD2_MD0ACP_MASK** (line 224)
- **XSPI_FRAD0_WORD3** (line 226)
- **XSPI_FRAD0_WORD3_VLD** (line 227)
- **XSPI_FR_AAEF** (line 186)
- **XSPI_FR_ABOF** (line 189)
- **XSPI_FR_AIBSEF** (line 188)
- **XSPI_FR_AITEF** (line 187)
- **XSPI_FR_CRCAEF** (line 190)
- **XSPI_FR_DLLABRT** (line 179)
- **XSPI_FR_DLLUNLCK** (line 182)
- **XSPI_FR_DLPFF** (line 178)
- **XSPI_FR_ILLINE** (line 183)
- **XSPI_FR_IPEDERR** (line 193)
- **XSPI_FR_IPIEF** (line 192)
- **XSPI_FR_PERFOVF** (line 194)
- **XSPI_FR_PPWF** (line 191)
- **XSPI_FR_RBDF** (line 185)
- **XSPI_FR_RBOF** (line 184)
- **XSPI_FR_RDADDR** (line 195)
- **XSPI_FR_TBFF** (line 180)
- **XSPI_FR_TBUF** (line 181)
- **XSPI_FR_TFF** (line 196)
- **XSPI_INT_EN** (line 242)
- **XSPI_IPCR** (line 83)
- **XSPI_LCKCR** (line 210)
- **XSPI_LOKCR_LOCK** (line 211)
- **XSPI_LOKCR_UNLOCK** (line 212)
- **XSPI_LUT** (line 214)
- **XSPI_LUTKEY** (line 207)
- **XSPI_LUT_KEY_VAL** (line 208)
- **XSPI_LUT_OFFSET** (line 215)
- **XSPI_LUT_REG**(idx) (line 216)
- **XSPI_MCR** (line 64)
- **XSPI_MCREXT** (line 219)
- **XSPI_MCREXT_RST_MASK** (line 220)
- **XSPI_MCR_CKN_FA_EN** (line 65)
- **XSPI_MCR_CLR_RXF** (line 73)
- **XSPI_MCR_CLR_TXF** (line 72)
- **XSPI_MCR_DDR_EN** (line 76)
- **XSPI_MCR_DLPEN** (line 71)
- **XSPI_MCR_DOZE** (line 69)
- **XSPI_MCR_DQS_EN** (line 77)
- **XSPI_MCR_DQS_FA_SEL_MASK** (line 66)
- **XSPI_MCR_DQS_LAT_EN** (line 78)
- **XSPI_MCR_DQS_OUT_EN** (line 79)
- **XSPI_MCR_IPS_TG_RST** (line 74)
- **XSPI_MCR_ISD2FA** (line 68)
- **XSPI_MCR_ISD3FA** (line 67)
- **XSPI_MCR_MDIS** (line 70)
- **XSPI_MCR_SWRSTHD** (line 80)
- **XSPI_MCR_SWRSTSD** (line 81)
- **XSPI_MCR_VAR_LAT_EN** (line 75)
- **XSPI_MGC** (line 234)
- **XSPI_MGC_GVLD** (line 235)
- **XSPI_MGC_GVLDFRAD** (line 237)
- **XSPI_MGC_GVLDMDAD** (line 236)
- **XSPI_MTO** (line 239)
- **XSPI_QUIRK_USE_IP_ONLY** (line 310)
- **XSPI_RBCT** (line 143)
- **XSPI_RBCT_WMRK_MASK** (line 144)
- **XSPI_RBDR0** (line 205)
- **XSPI_RBSR** (line 141)
- **XSPI_RPM_TIMEOUT_MS** (line 56)
- **XSPI_RSER** (line 198)
- **XSPI_RSER_TFIE** (line 199)
- **XSPI_SEQID_LUT** (line 62)
- **XSPI_SFA1AD** (line 201)
- **XSPI_SFA2AD** (line 203)
- **XSPI_SFACR** (line 127)
- **XSPI_SFACR_BYTE_SWAP** (line 132)
- **XSPI_SFACR_CAS_INTRLVD** (line 130)
- **XSPI_SFACR_CAS_MASK** (line 134)
- **XSPI_SFACR_FORCE_A10** (line 128)
- **XSPI_SFACR_RX_BP_EN** (line 131)
- **XSPI_SFACR_WA** (line 133)
- **XSPI_SFACR_WA_4B_EN** (line 129)
- **XSPI_SFAR** (line 125)
- **XSPI_SFP_TG_IPCR** (line 244)
- **XSPI_SFP_TG_IPCR_ARB_LOCK** (line 247)
- **XSPI_SFP_TG_IPCR_ARB_UNLOCK** (line 246)
- **XSPI_SFP_TG_IPCR_IDATSZ_MASK** (line 248)
- **XSPI_SFP_TG_IPCR_SEQID_MASK** (line 245)
- **XSPI_SFP_TG_SFAR** (line 250)
- **XSPI_SMPR** (line 136)
- **XSPI_SMPR_DLLFSMPFA_MASK** (line 137)
- **XSPI_SMPR_FSDLY** (line 138)
- **XSPI_SMPR_FSPHS** (line 139)
- **XSPI_SR** (line 159)
- **XSPI_SR_AHBTRN** (line 171)
- **XSPI_SR_AHB_ACC** (line 173)
- **XSPI_SR_AHBnFUL** (line 169)
- **XSPI_SR_AHBnNE** (line 170)
- **XSPI_SR_ARB_LCK** (line 168)
- **XSPI_SR_ARB_STATE_MASK** (line 165)
- **XSPI_SR_AWRACC** (line 172)
- **XSPI_SR_BUSY** (line 175)
- **XSPI_SR_IP_ACC** (line 174)
- **XSPI_SR_RXDMA** (line 164)
- **XSPI_SR_RXFULL** (line 166)
- **XSPI_SR_RXWE** (line 167)
- **XSPI_SR_TXDMA** (line 161)
- **XSPI_SR_TXFULL** (line 160)
- **XSPI_SR_TXNE** (line 163)
- **XSPI_SR_TXWA** (line 162)
- **XSPI_TBCT** (line 156)
- **XSPI_TBCT_WMRK_MASK** (line 157)
- **XSPI_TBDR** (line 154)
- **XSPI_TBSR** (line 152)
- **XSPI_TG0MDAD** (line 229)
- **XSPI_TG0MDAD_VLD** (line 230)
- **XSPI_TG1MDAD** (line 232)
