# drivers/spi/spi-fsl-qspi.c

Subsystem: drivers/spi

## Functions (32)

### fsl_qspi_adjust_op_size
- Return type: static int
- Signature: fsl_qspi_adjust_op_size(struct spi_mem * mem,struct spi_mem_op * op)
- Line: 730

### fsl_qspi_check_buswidth
- Return type: static int
- Signature: fsl_qspi_check_buswidth(struct fsl_qspi * q,u8 width)
- Line: 378

### fsl_qspi_cleanup
- Return type: static void
- Signature: fsl_qspi_cleanup(void * data)
- Line: 883

### fsl_qspi_clk_disable_unprep
- Return type: static void
- Signature: fsl_qspi_clk_disable_unprep(struct fsl_qspi * q)
- Line: 514

### fsl_qspi_clk_prep_enable
- Return type: static int
- Signature: fsl_qspi_clk_prep_enable(struct fsl_qspi * q)
- Line: 494

### fsl_qspi_default_setup
- Return type: static int
- Signature: fsl_qspi_default_setup(struct fsl_qspi * q)
- Line: 747

### fsl_qspi_disable
- Return type: static void
- Signature: fsl_qspi_disable(void * data)
- Line: 874

### fsl_qspi_do_op
- Return type: static int
- Signature: fsl_qspi_do_op(struct fsl_qspi * q,const struct spi_mem_op * op)
- Line: 631

### fsl_qspi_endian_xchg
- Return type: static u32
- Signature: fsl_qspi_endian_xchg(struct fsl_qspi * q,u32 a)
- Line: 334

### fsl_qspi_exec_op
- Return type: static int
- Signature: fsl_qspi_exec_op(struct spi_mem * mem,const struct spi_mem_op * op)
- Line: 668

### fsl_qspi_fill_txfifo
- Return type: static void
- Signature: fsl_qspi_fill_txfifo(struct fsl_qspi * q,const struct spi_mem_op * op)
- Line: 585

### fsl_qspi_get_name
- Return type: static const char *
- Signature: fsl_qspi_get_name(struct spi_mem * mem)
- Line: 837

### fsl_qspi_invalidate
- Return type: static void
- Signature: fsl_qspi_invalidate(struct fsl_qspi * q)
- Line: 530

### fsl_qspi_irq_handler
- Return type: static irqreturn_t
- Signature: fsl_qspi_irq_handler(int irq,void * dev_id)
- Line: 362

### fsl_qspi_prepare_lut
- Return type: static void
- Signature: fsl_qspi_prepare_lut(struct fsl_qspi * q,const struct spi_mem_op * op)
- Line: 438

### fsl_qspi_probe
- Return type: static int
- Signature: fsl_qspi_probe(struct platform_device * pdev)
- Line: 894

### fsl_qspi_read_ahb
- Return type: static void
- Signature: fsl_qspi_read_ahb(struct fsl_qspi * q,const struct spi_mem_op * op)
- Line: 578

### fsl_qspi_read_rxfifo
- Return type: static void
- Signature: fsl_qspi_read_rxfifo(struct fsl_qspi * q,const struct spi_mem_op * op)
- Line: 610

### fsl_qspi_readl_poll_tout
- Return type: static int
- Signature: fsl_qspi_readl_poll_tout(struct fsl_qspi * q,void __iomem * base,u32 mask,u32 delay_us,u32 timeout_us)
- Line: 656

### fsl_qspi_resume
- Return type: static int
- Signature: fsl_qspi_resume(struct device * dev)
- Line: 1001

### fsl_qspi_select_mem
- Return type: static void
- Signature: fsl_qspi_select_mem(struct fsl_qspi * q,struct spi_device * spi,const struct spi_mem_op * op)
- Line: 548

### fsl_qspi_supports_op
- Return type: static bool
- Signature: fsl_qspi_supports_op(struct spi_mem * mem,const struct spi_mem_op * op)
- Line: 390

### fsl_qspi_suspend
- Return type: static int
- Signature: fsl_qspi_suspend(struct device * dev)
- Line: 996

### needs_4x_clock
- Return type: static bool
- Signature: needs_4x_clock(struct fsl_qspi * q)
- Line: 300

### needs_amba_base_offset
- Return type: static bool
- Signature: needs_amba_base_offset(struct fsl_qspi * q)
- Line: 315

### needs_clk_disable
- Return type: static bool
- Signature: needs_clk_disable(struct fsl_qspi * q)
- Line: 325

### needs_fill_txfifo
- Return type: static bool
- Signature: needs_fill_txfifo(struct fsl_qspi * q)
- Line: 305

### needs_swap_endian
- Return type: static bool
- Signature: needs_swap_endian(struct fsl_qspi * q)
- Line: 295

### needs_tdh_setting
- Return type: static bool
- Signature: needs_tdh_setting(struct fsl_qspi * q)
- Line: 320

### needs_wakeup_wait_mode
- Return type: static bool
- Signature: needs_wakeup_wait_mode(struct fsl_qspi * q)
- Line: 310

### qspi_readl
- Return type: static u32
- Signature: qspi_readl(struct fsl_qspi * q,void __iomem * addr)
- Line: 354

### qspi_writel
- Return type: static void
- Signature: qspi_writel(struct fsl_qspi * q,u32 val,void __iomem * addr)
- Line: 346

## Structs (2)

### fsl_qspi
- Line: 281
- Members:
  - rxfifo: unsigned int
  - txfifo: unsigned int
  - invalid_mstrid: int
  - ahb_buf_size: unsigned int
  - sfa_size: unsigned int
  - quirks: unsigned int
  - little_endian: bool
  - iobase: void __iomem *
  - ahb_addr: void __iomem *
  - devtype_data: const struct fsl_qspi_devtype_data *
  - lock: mutex
  - c: completion
  - resets: reset_control *
  - clk: clk *
  - clk_en: clk *
  - pm_qos_req: pm_qos_request
  - dev: device *
  - selected: int
  - memmap_phy: u32

### fsl_qspi_devtype_data
- Line: 205
- Members:
  - rxfifo: unsigned int
  - txfifo: unsigned int
  - invalid_mstrid: int
  - ahb_buf_size: unsigned int
  - sfa_size: unsigned int
  - quirks: unsigned int
  - little_endian: bool
  - iobase: void __iomem *
  - ahb_addr: void __iomem *
  - devtype_data: const struct fsl_qspi_devtype_data *
  - lock: mutex
  - c: completion
  - resets: reset_control *
  - clk: clk *
  - clk_en: clk *
  - pm_qos_req: pm_qos_request
  - dev: device *
  - selected: int
  - memmap_phy: u32

## Variables (12)

- static **fsl_qspi_driver** : platform_driver (line 1027)
- static **fsl_qspi_dt_ids** : const struct of_device_id[] (line 1010)
- static **fsl_qspi_mem_caps** : const struct spi_controller_mem_caps (line 870)
- static **fsl_qspi_mem_ops** : const struct spi_controller_mem_ops (line 863)
- static **fsl_qspi_pm_ops** : const struct dev_pm_ops (line 1022)
- static **imx6sx_data** : const struct fsl_qspi_devtype_data (line 224)
- static **imx6ul_data** : const struct fsl_qspi_devtype_data (line 243)
- static **imx7d_data** : const struct fsl_qspi_devtype_data (line 233)
- static **ls1021a_data** : const struct fsl_qspi_devtype_data (line 253)
- static **ls2080a_data** : const struct fsl_qspi_devtype_data (line 262)
- static **spacemit_k1_data** : const struct fsl_qspi_devtype_data (line 271)
- static **vybrid_data** : const struct fsl_qspi_devtype_data (line 215)

## Macros (88)

- **LUT_ADDR** (line 136)
- **LUT_ADDR_DDR** (line 144)
- **LUT_CMD** (line 135)
- **LUT_DATA_LEARN** (line 150)
- **LUT_DEF**(idx,ins,pad,opr) (line 169)
- **LUT_DUMMY** (line 137)
- **LUT_FSL_READ** (line 141)
- **LUT_FSL_READ_DDR** (line 148)
- **LUT_FSL_WRITE** (line 142)
- **LUT_FSL_WRITE_DDR** (line 149)
- **LUT_JMP_ON_CS** (line 143)
- **LUT_MODE** (line 138)
- **LUT_MODE2** (line 139)
- **LUT_MODE2_DDR** (line 146)
- **LUT_MODE4** (line 140)
- **LUT_MODE4_DDR** (line 147)
- **LUT_MODE_DDR** (line 145)
- **LUT_PAD**(x) (line 159)
- **LUT_STOP** (line 134)
- **QUADSPI_BFGENCR** (line 81)
- **QUADSPI_BFGENCR_SEQID**(x) (line 82)
- **QUADSPI_BUF0CR** (line 71)
- **QUADSPI_BUF0IND** (line 84)
- **QUADSPI_BUF1CR** (line 72)
- **QUADSPI_BUF1IND** (line 85)
- **QUADSPI_BUF2CR** (line 73)
- **QUADSPI_BUF2IND** (line 86)
- **QUADSPI_BUF3CR** (line 76)
- **QUADSPI_BUF3CR_ADATSZ**(x) (line 78)
- **QUADSPI_BUF3CR_ADATSZ_MASK** (line 79)
- **QUADSPI_BUF3CR_ALLMST_MASK** (line 77)
- **QUADSPI_BUFXCR_INVALID_MSTRID** (line 74)
- **QUADSPI_FLSHCR** (line 66)
- **QUADSPI_FLSHCR_TCSH_MASK** (line 68)
- **QUADSPI_FLSHCR_TCSS_MASK** (line 67)
- **QUADSPI_FLSHCR_TDH_MASK** (line 69)
- **QUADSPI_FR** (line 105)
- **QUADSPI_FR_TFF_MASK** (line 106)
- **QUADSPI_IPCR** (line 63)
- **QUADSPI_IPCR_SEQID**(x) (line 64)
- **QUADSPI_LCKCR** (line 124)
- **QUADSPI_LCKER_LOCK** (line 125)
- **QUADSPI_LCKER_UNLOCK** (line 126)
- **QUADSPI_LUTKEY** (line 121)
- **QUADSPI_LUTKEY_VALUE** (line 122)
- **QUADSPI_LUT_BASE** (line 128)
- **QUADSPI_LUT_OFFSET** (line 129)
- **QUADSPI_LUT_REG**(idx) (line 130)
- **QUADSPI_MCR** (line 53)
- **QUADSPI_MCR_CLR_RXF_MASK** (line 57)
- **QUADSPI_MCR_CLR_TXF_MASK** (line 56)
- **QUADSPI_MCR_DDR_EN_MASK** (line 58)
- **QUADSPI_MCR_END_CFG_MASK** (line 59)
- **QUADSPI_MCR_MDIS_MASK** (line 55)
- **QUADSPI_MCR_RESERVED_MASK** (line 54)
- **QUADSPI_MCR_SWRSTHD_MASK** (line 60)
- **QUADSPI_MCR_SWRSTSD_MASK** (line 61)
- **QUADSPI_QUIRK_4X_INT_CLK** (line 176)
- **QUADSPI_QUIRK_BASE_INTERNAL** (line 192)
- **QUADSPI_QUIRK_SKIP_CLK_DISABLE** (line 203)
- **QUADSPI_QUIRK_SWAP_ENDIAN** (line 173)
- **QUADSPI_QUIRK_TKT245618** (line 186)
- **QUADSPI_QUIRK_TKT253890** (line 183)
- **QUADSPI_QUIRK_USE_TDH_SETTING** (line 198)
- **QUADSPI_RBCT** (line 95)
- **QUADSPI_RBCT_RXBRD_USEIPS** (line 97)
- **QUADSPI_RBCT_WMRK_MASK** (line 96)
- **QUADSPI_RBDR**(x) (line 119)
- **QUADSPI_RSER** (line 108)
- **QUADSPI_RSER_TFIE** (line 109)
- **QUADSPI_SFA1AD** (line 115)
- **QUADSPI_SFA2AD** (line 116)
- **QUADSPI_SFAR** (line 87)
- **QUADSPI_SFB1AD** (line 117)
- **QUADSPI_SFB2AD** (line 118)
- **QUADSPI_SMPR** (line 89)
- **QUADSPI_SMPR_DDRSMP_MASK** (line 90)
- **QUADSPI_SMPR_FSDLY_MASK** (line 91)
- **QUADSPI_SMPR_FSPHS_MASK** (line 92)
- **QUADSPI_SMPR_HSENA_MASK** (line 93)
- **QUADSPI_SPTRCLR** (line 111)
- **QUADSPI_SPTRCLR_BFPTRC** (line 113)
- **QUADSPI_SPTRCLR_IPPTRC** (line 112)
- **QUADSPI_SR** (line 101)
- **QUADSPI_SR_AHB_ACC_MASK** (line 103)
- **QUADSPI_SR_IP_ACC_MASK** (line 102)
- **QUADSPI_TBDR** (line 99)
- **SEQID_LUT** (line 50)
