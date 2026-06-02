# drivers/spi/spi-mxic.c

Subsystem: drivers/spi

## Functions (26)

### mxic_spi_clk_disable
- Return type: static void
- Signature: mxic_spi_clk_disable(struct mxic_spi * mxic)
- Line: 211

### mxic_spi_clk_enable
- Return type: static int
- Signature: mxic_spi_clk_enable(struct mxic_spi * mxic)
- Line: 191

### mxic_spi_clk_setup
- Return type: static int
- Signature: mxic_spi_clk_setup(struct mxic_spi * mxic,unsigned long freq)
- Line: 231

### mxic_spi_data_xfer
- Return type: static int
- Signature: mxic_spi_data_xfer(struct mxic_spi * mxic,const void * txbuf,void * rxbuf,unsigned int len)
- Line: 348

### mxic_spi_hw_init
- Return type: static void
- Signature: mxic_spi_hw_init(struct mxic_spi * mxic)
- Line: 285

### mxic_spi_mem_dirmap_create
- Return type: static int
- Signature: mxic_spi_mem_dirmap_create(struct spi_mem_dirmap_desc * desc)
- Line: 502

### mxic_spi_mem_dirmap_read
- Return type: static ssize_t
- Signature: mxic_spi_mem_dirmap_read(struct spi_mem_dirmap_desc * desc,u64 offs,size_t len,void * buf)
- Line: 396

### mxic_spi_mem_dirmap_write
- Return type: static ssize_t
- Signature: mxic_spi_mem_dirmap_write(struct spi_mem_dirmap_desc * desc,u64 offs,size_t len,const void * buf)
- Line: 440

### mxic_spi_mem_ecc_cleanup_ctx
- Return type: static void
- Signature: mxic_spi_mem_ecc_cleanup_ctx(struct nand_device * nand)
- Line: 661

### mxic_spi_mem_ecc_finish_io_req
- Return type: static int
- Signature: mxic_spi_mem_ecc_finish_io_req(struct nand_device * nand,struct nand_page_io_req * req)
- Line: 679

### mxic_spi_mem_ecc_init_ctx
- Return type: static int
- Signature: mxic_spi_mem_ecc_init_ctx(struct nand_device * nand)
- Line: 651

### mxic_spi_mem_ecc_prepare_io_req
- Return type: static int
- Signature: mxic_spi_mem_ecc_prepare_io_req(struct nand_device * nand,struct nand_page_io_req * req)
- Line: 671

### mxic_spi_mem_ecc_probe
- Return type: static int
- Signature: mxic_spi_mem_ecc_probe(struct platform_device * pdev,struct mxic_spi * mxic)
- Line: 702

### mxic_spi_mem_ecc_remove
- Return type: static void
- Signature: mxic_spi_mem_ecc_remove(struct mxic_spi * mxic)
- Line: 694

### mxic_spi_mem_exec_op
- Return type: static int
- Signature: mxic_spi_mem_exec_op(struct spi_mem * mem,const struct spi_mem_op * op)
- Line: 518

### mxic_spi_mem_prep_op_cfg
- Return type: static u32
- Signature: mxic_spi_mem_prep_op_cfg(const struct spi_mem_op * op,unsigned int data_len)
- Line: 319

### mxic_spi_mem_supports_op
- Return type: static bool
- Signature: mxic_spi_mem_supports_op(struct spi_mem * mem,const struct spi_mem_op * op)
- Line: 485

### mxic_spi_prep_hc_cfg
- Return type: static u32
- Signature: mxic_spi_prep_hc_cfg(struct spi_device * spi,u32 flags,bool swap16)
- Line: 297

### mxic_spi_probe
- Return type: static int
- Signature: mxic_spi_probe(struct platform_device * pdev)
- Line: 755

### mxic_spi_remove
- Return type: static void
- Signature: mxic_spi_remove(struct platform_device * pdev)
- Line: 830

### mxic_spi_runtime_resume
- Return type: static int __maybe_unused
- Signature: mxic_spi_runtime_resume(struct device * dev)
- Line: 735

### mxic_spi_runtime_suspend
- Return type: static int __maybe_unused
- Signature: mxic_spi_runtime_suspend(struct device * dev)
- Line: 724

### mxic_spi_set_cs
- Return type: static void
- Signature: mxic_spi_set_cs(struct spi_device * spi,bool lvl)
- Line: 588

### mxic_spi_set_freq
- Return type: static int
- Signature: mxic_spi_set_freq(struct mxic_spi * mxic,unsigned long freq)
- Line: 264

### mxic_spi_set_input_delay_dqs
- Return type: static void
- Signature: mxic_spi_set_input_delay_dqs(struct mxic_spi * mxic,u8 idly_code)
- Line: 217

### mxic_spi_transfer_one
- Return type: static int
- Signature: mxic_spi_transfer_one(struct spi_controller * host,struct spi_device * spi,struct spi_transfer * t)
- Line: 605

## Structs (3)

### __anon029dadd30108
- Line: 178
- Members:
  - dev: device *
  - ps_clk: clk *
  - send_clk: clk *
  - send_dly_clk: clk *
  - regs: void __iomem *
  - cur_speed_hz: u32
  - map: void __iomem *
  - dma: dma_addr_t
  - size: size_t
  - linear: mxic_spi::__anon029dadd30108
  - use_pipelined_conf: bool
  - pipelined_engine: nand_ecc_engine *
  - ctx: void *
  - ecc: mxic_spi::__anon029dadd30208

### __anon029dadd30208
- Line: 184
- Members:
  - dev: device *
  - ps_clk: clk *
  - send_clk: clk *
  - send_dly_clk: clk *
  - regs: void __iomem *
  - cur_speed_hz: u32
  - map: void __iomem *
  - dma: dma_addr_t
  - size: size_t
  - linear: mxic_spi::__anon029dadd30108
  - use_pipelined_conf: bool
  - pipelined_engine: nand_ecc_engine *
  - ctx: void *
  - ecc: mxic_spi::__anon029dadd30208

### mxic_spi
- Line: 171
- Members:
  - dev: device *
  - ps_clk: clk *
  - send_clk: clk *
  - send_dly_clk: clk *
  - regs: void __iomem *
  - cur_speed_hz: u32
  - map: void __iomem *
  - dma: dma_addr_t
  - size: size_t
  - linear: mxic_spi::__anon029dadd30108
  - use_pipelined_conf: bool
  - pipelined_engine: nand_ecc_engine *
  - ctx: void *
  - ecc: mxic_spi::__anon029dadd30208

## Variables (6)

- static **mxic_spi_dev_pm_ops** : const struct dev_pm_ops (line 750)
- static **mxic_spi_driver** : platform_driver (line 847)
- static **mxic_spi_mem_caps** : const struct spi_controller_mem_caps (line 581)
- static **mxic_spi_mem_ecc_engine_pipelined_ops** : const struct nand_ecc_engine_ops (line 687)
- static **mxic_spi_mem_ops** : const struct spi_controller_mem_ops (line 573)
- static **mxic_spi_of_ids** : const struct of_device_id[] (line 841)

## Macros (124)

- **AXI_SLV_ADDR** (line 110)
- **DATA_STROB** (line 153)
- **DATA_STROB_DELAY_2CYC** (line 156)
- **DATA_STROB_EDO_EN** (line 154)
- **DATA_STROB_INV_POL** (line 155)
- **DMAC_CFG_ALLFLUSH_EN** (line 115)
- **DMAC_CFG_BURST_LEN**(x) (line 118)
- **DMAC_CFG_BURST_SZ**(x) (line 119)
- **DMAC_CFG_DIR_READ** (line 120)
- **DMAC_CFG_LASTFLUSH_EN** (line 116)
- **DMAC_CFG_PERIPH_EN** (line 114)
- **DMAC_CFG_QE**(x) (line 117)
- **DMAC_CFG_START** (line 121)
- **DMAC_RD_CFG** (line 112)
- **DMAC_RD_CNT** (line 123)
- **DMAC_WR_CFG** (line 113)
- **DMAC_WR_CNT** (line 124)
- **DMAM_CFG** (line 128)
- **DMAM_CFG_CONT** (line 130)
- **DMAM_CFG_DIR_READ** (line 132)
- **DMAM_CFG_EN** (line 133)
- **DMAM_CFG_SDMA_GAP**(x) (line 131)
- **DMAM_CFG_START** (line 129)
- **DMAM_CNT** (line 135)
- **DMAS_CTRL** (line 149)
- **DMAS_CTRL_DIR_READ** (line 151)
- **DMAS_CTRL_EN** (line 150)
- **GPIO** (line 161)
- **GPIO_HOLDB**(x) (line 164)
- **GPIO_PT**(x) (line 162)
- **GPIO_RESET**(x) (line 163)
- **GPIO_WPB**(x) (line 165)
- **HC_CFG** (line 22)
- **HC_CFG_BIG_ENDIAN** (line 35)
- **HC_CFG_CLK_PH_EN** (line 33)
- **HC_CFG_CLK_POL_INV** (line 34)
- **HC_CFG_DATA_PASS** (line 36)
- **HC_CFG_DUAL_SLAVE** (line 24)
- **HC_CFG_IDLE_SIO_LVL**(x) (line 37)
- **HC_CFG_IF_CFG**(x) (line 23)
- **HC_CFG_INDIVIDUAL** (line 25)
- **HC_CFG_MAN_CS_ASSERT** (line 41)
- **HC_CFG_MAN_CS_EN** (line 40)
- **HC_CFG_MAN_START** (line 39)
- **HC_CFG_MAN_START_EN** (line 38)
- **HC_CFG_NIO**(x) (line 26)
- **HC_CFG_SLV_ACT**(x) (line 32)
- **HC_CFG_TYPE**(s,t) (line 27)
- **HC_CFG_TYPE_RAW_NAND** (line 31)
- **HC_CFG_TYPE_SPI_NAND** (line 29)
- **HC_CFG_TYPE_SPI_NOR** (line 28)
- **HC_CFG_TYPE_SPI_RAM** (line 30)
- **HC_EN** (line 61)
- **HC_EN_BIT** (line 62)
- **HC_VER** (line 167)
- **HW_TEST**(x) (line 169)
- **IDLY_CODE**(x) (line 158)
- **IDLY_CODE_VAL**(x,v) (line 159)
- **INT_CRC_ERR** (line 51)
- **INT_DMA_FINISH** (line 55)
- **INT_ECC_ERR** (line 50)
- **INT_LNR_SUSP** (line 49)
- **INT_LRD_DIS** (line 53)
- **INT_LWR_DIS** (line 52)
- **INT_RDY_PIN** (line 47)
- **INT_RDY_SR** (line 48)
- **INT_RX_NOT_EMPTY** (line 57)
- **INT_RX_NOT_FULL** (line 56)
- **INT_SDMA_INT** (line 54)
- **INT_SIG_EN** (line 45)
- **INT_STS** (line 43)
- **INT_STS_ALL** (line 46)
- **INT_STS_EN** (line 44)
- **INT_TX_EMPTY** (line 59)
- **INT_TX_NOT_FULL** (line 58)
- **LMODE_CMD0**(x) (line 103)
- **LMODE_CMD1**(x) (line 102)
- **LMODE_EN** (line 100)
- **LMODE_SLV_ACT**(x) (line 101)
- **LNR_TIMER_TH** (line 137)
- **LRD_ADDR** (line 105)
- **LRD_CFG** (line 68)
- **LRD_CTRL** (line 97)
- **LRD_RANGE** (line 107)
- **LWR_ADDR** (line 106)
- **LWR_CFG** (line 69)
- **LWR_CTRL** (line 99)
- **LWR_RANGE** (line 108)
- **LWR_SUSP_CTRL** (line 146)
- **LWR_SUSP_CTRL_EN** (line 147)
- **OCTA_CRC** (line 90)
- **OCTA_CRC_CHUNK**(s,x) (line 92)
- **OCTA_CRC_IN_EN**(s) (line 91)
- **OCTA_CRC_OUT_EN**(s) (line 93)
- **ONFI_DIN_CNT**(s) (line 95)
- **OP_ADDR_BUSW**(x) (line 82)
- **OP_ADDR_BYTES**(x) (line 73)
- **OP_ADDR_DDR** (line 81)
- **OP_BUSW_1** (line 85)
- **OP_BUSW_2** (line 86)
- **OP_BUSW_4** (line 87)
- **OP_BUSW_8** (line 88)
- **OP_CMD_BUSW**(x) (line 84)
- **OP_CMD_BYTES**(x) (line 74)
- **OP_CMD_DDR** (line 83)
- **OP_DATA_BUSW**(x) (line 80)
- **OP_DATA_DDR** (line 79)
- **OP_DQS_EN** (line 76)
- **OP_DUMMY_CYC**(x) (line 72)
- **OP_ENHC_EN** (line 77)
- **OP_OCTA_CRC_EN** (line 75)
- **OP_PREAMBLE_EN** (line 78)
- **OP_READ** (line 71)
- **RDM_CFG0** (line 139)
- **RDM_CFG0_POLY**(x) (line 140)
- **RDM_CFG1** (line 142)
- **RDM_CFG1_RDM_EN** (line 143)
- **RDM_CFG1_SEED**(x) (line 144)
- **RWW_CFG** (line 70)
- **RWW_CTRL** (line 98)
- **RXD** (line 65)
- **SDMA_ADDR** (line 126)
- **SS_CTRL**(s) (line 67)
- **TXD**(x) (line 64)
