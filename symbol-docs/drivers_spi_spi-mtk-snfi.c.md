# drivers/spi/spi-mtk-snfi.c

Subsystem: drivers/spi

## Functions (32)

### mtk_nfi_reset
- Return type: static int
- Signature: mtk_nfi_reset(struct mtk_snand * snf)
- Line: 378

### mtk_snand_adjust_op_size
- Return type: static int
- Signature: mtk_snand_adjust_op_size(struct spi_mem * mem,struct spi_mem_op * op)
- Line: 1255

### mtk_snand_bm_swap
- Return type: static void
- Signature: mtk_snand_bm_swap(struct mtk_snand * snf,u8 * buf)
- Line: 830

### mtk_snand_ecc_cleanup_ctx
- Return type: static void
- Signature: mtk_snand_ecc_cleanup_ctx(struct nand_device * nand)
- Line: 739

### mtk_snand_ecc_finish_io_req
- Return type: static int
- Signature: mtk_snand_ecc_finish_io_req(struct nand_device * nand,struct nand_page_io_req * req)
- Line: 762

### mtk_snand_ecc_init_ctx
- Return type: static int
- Signature: mtk_snand_ecc_init_ctx(struct nand_device * nand)
- Line: 660

### mtk_snand_ecc_prepare_io_req
- Return type: static int
- Signature: mtk_snand_ecc_prepare_io_req(struct nand_device * nand,struct nand_page_io_req * req)
- Line: 746

### mtk_snand_exec_op
- Return type: static int
- Signature: mtk_snand_exec_op(struct spi_mem * mem,const struct spi_mem_op * op)
- Line: 1282

### mtk_snand_fdm_bm_swap
- Return type: static void
- Signature: mtk_snand_fdm_bm_swap(struct mtk_snand * snf)
- Line: 847

### mtk_snand_irq
- Return type: static irqreturn_t
- Signature: mtk_snand_irq(int irq,void * id)
- Line: 1313

### mtk_snand_is_page_ops
- Return type: static bool
- Signature: mtk_snand_is_page_ops(const struct spi_mem_op * op)
- Line: 1199

### mtk_snand_mac_io
- Return type: static int
- Signature: mtk_snand_mac_io(struct mtk_snand * snf,const struct spi_mem_op * op)
- Line: 460

### mtk_snand_mac_reset
- Return type: static int
- Signature: mtk_snand_mac_reset(struct mtk_snand * snf)
- Line: 413

### mtk_snand_mac_trigger
- Return type: static int
- Signature: mtk_snand_mac_trigger(struct mtk_snand * snf,u32 outlen,u32 inlen)
- Line: 431

### mtk_snand_ooblayout_ecc
- Return type: static int
- Signature: mtk_snand_ooblayout_ecc(struct mtd_info * mtd,int section,struct mtd_oob_region * oobecc)
- Line: 634

### mtk_snand_ooblayout_free
- Return type: static int
- Signature: mtk_snand_ooblayout_free(struct mtd_info * mtd,int section,struct mtd_oob_region * oobfree)
- Line: 641

### mtk_snand_probe
- Return type: static int
- Signature: mtk_snand_probe(struct platform_device * pdev)
- Line: 1338

### mtk_snand_read_fdm
- Return type: static void
- Signature: mtk_snand_read_fdm(struct mtk_snand * snf,u8 * buf)
- Line: 786

### mtk_snand_read_page_cache
- Return type: static int
- Signature: mtk_snand_read_page_cache(struct mtk_snand * snf,const struct spi_mem_op * op)
- Line: 861

### mtk_snand_remove
- Return type: static void
- Signature: mtk_snand_remove(struct platform_device * pdev)
- Line: 1479

### mtk_snand_setup_pagefmt
- Return type: static int
- Signature: mtk_snand_setup_pagefmt(struct mtk_snand * snf,u32 page_size,u32 oob_size)
- Line: 534

### mtk_snand_supports_op
- Return type: static bool
- Signature: mtk_snand_supports_op(struct spi_mem * mem,const struct spi_mem_op * op)
- Line: 1241

### mtk_snand_write_fdm
- Return type: static void
- Signature: mtk_snand_write_fdm(struct mtk_snand * snf,const u8 * buf)
- Line: 803

### mtk_snand_write_page_cache
- Return type: static int
- Signature: mtk_snand_write_page_cache(struct mtk_snand * snf,const struct spi_mem_op * op)
- Line: 1054

### mtk_unregister_ecc_engine
- Return type: static void
- Signature: mtk_unregister_ecc_engine(void * data)
- Line: 1306

### nand_to_mtk_snand
- Return type: static mtk_snand *
- Signature: nand_to_mtk_snand(struct nand_device * nand)
- Line: 321

### nfi_read32
- Return type: static u32
- Signature: nfi_read32(struct mtk_snand * snf,u32 reg)
- Line: 341

### nfi_read_data
- Return type: static void
- Signature: nfi_read_data(struct mtk_snand * snf,u32 reg,u8 * data,u32 len)
- Line: 366

### nfi_rmw32
- Return type: static void
- Signature: nfi_rmw32(struct mtk_snand * snf,u32 reg,u32 clr,u32 set)
- Line: 356

### nfi_write16
- Return type: static void
- Signature: nfi_write16(struct mtk_snand * snf,u32 reg,u16 val)
- Line: 351

### nfi_write32
- Return type: static void
- Signature: nfi_write32(struct mtk_snand * snf,u32 reg,u32 val)
- Line: 346

### snand_prepare_bouncebuf
- Return type: static int
- Signature: snand_prepare_bouncebuf(struct mtk_snand * snf,size_t size)
- Line: 328

## Structs (3)

### mtk_snand
- Line: 301
- Members:
  - sector_size: u16
  - max_sectors: u16
  - fdm_size: u16
  - fdm_ecc_size: u16
  - fifo_size: u16
  - bbm_swap: bool
  - empty_page_check: bool
  - mastersta_mask: u32
  - nandfsm_mask: u32
  - spare_sizes: const u8 *
  - num_spare_size: u32
  - page_size: size_t
  - oob_size: size_t
  - nsectors: u8
  - spare_size: u8
  - ctlr: spi_controller *
  - dev: device *
  - nfi_clk: clk *
  - pad_clk: clk *
  - nfi_hclk: clk *
  - nfi_base: void __iomem *
  - irq: int
  - op_done: completion
  - caps: const struct mtk_snand_caps *
  - ecc_cfg: mtk_ecc_config *
  - ecc: mtk_ecc *
  - nfi_cfg: mtk_snand_conf
  - ecc_stats: mtk_ecc_stats
  - ecc_eng: nand_ecc_engine
  - autofmt: bool
  - buf: u8 *
  - buf_len: size_t

### mtk_snand_caps
- Line: 236
- Members:
  - sector_size: u16
  - max_sectors: u16
  - fdm_size: u16
  - fdm_ecc_size: u16
  - fifo_size: u16
  - bbm_swap: bool
  - empty_page_check: bool
  - mastersta_mask: u32
  - nandfsm_mask: u32
  - spare_sizes: const u8 *
  - num_spare_size: u32
  - page_size: size_t
  - oob_size: size_t
  - nsectors: u8
  - spare_size: u8
  - ctlr: spi_controller *
  - dev: device *
  - nfi_clk: clk *
  - pad_clk: clk *
  - nfi_hclk: clk *
  - nfi_base: void __iomem *
  - irq: int
  - op_done: completion
  - caps: const struct mtk_snand_caps *
  - ecc_cfg: mtk_ecc_config *
  - ecc: mtk_ecc *
  - nfi_cfg: mtk_snand_conf
  - ecc_stats: mtk_ecc_stats
  - ecc_eng: nand_ecc_engine
  - autofmt: bool
  - buf: u8 *
  - buf_len: size_t

### mtk_snand_conf
- Line: 294
- Members:
  - sector_size: u16
  - max_sectors: u16
  - fdm_size: u16
  - fdm_ecc_size: u16
  - fifo_size: u16
  - bbm_swap: bool
  - empty_page_check: bool
  - mastersta_mask: u32
  - nandfsm_mask: u32
  - spare_sizes: const u8 *
  - num_spare_size: u32
  - page_size: size_t
  - oob_size: size_t
  - nsectors: u8
  - spare_size: u8
  - ctlr: spi_controller *
  - dev: device *
  - nfi_clk: clk *
  - pad_clk: clk *
  - nfi_hclk: clk *
  - nfi_base: void __iomem *
  - irq: int
  - op_done: completion
  - caps: const struct mtk_snand_caps *
  - ecc_cfg: mtk_ecc_config *
  - ecc: mtk_ecc *
  - nfi_cfg: mtk_snand_conf
  - ecc_stats: mtk_ecc_stats
  - ecc_eng: nand_ecc_engine
  - autofmt: bool
  - buf: u8 *
  - buf_len: size_t

## Variables (11)

- static **mt7622_snand_caps** : const struct mtk_snand_caps (line 252)
- static **mt7622_spare_sizes** : const u8[] (line 229)
- static **mt7629_snand_caps** : const struct mtk_snand_caps (line 266)
- static **mt7986_snand_caps** : const struct mtk_snand_caps (line 280)
- static **mt7986_spare_sizes** : const u8[] (line 231)
- static **mtk_snand_driver** : platform_driver (line 1489)
- static **mtk_snand_ids** : const struct of_device_id[] (line 1329)
- static **mtk_snand_mem_caps** : const struct spi_controller_mem_caps (line 1302)
- static **mtk_snand_mem_ops** : const struct spi_controller_mem_ops (line 1296)
- static **mtk_snand_ooblayout** : const struct mtd_ooblayout_ops (line 655)
- static **mtk_snfi_ecc_engine_ops** : const struct nand_ecc_engine_ops (line 779)

## Macros (114)

- **BUS_SEC_CNTR**(val) (line 147)
- **CNFG_AUTO_FMT_EN** (line 91)
- **CNFG_DMA_BURST_EN** (line 93)
- **CNFG_DMA_MODE** (line 95)
- **CNFG_HW_ECC_EN** (line 92)
- **CNFG_OP_MODE_CUST** (line 89)
- **CNFG_OP_MODE_PROGRAM** (line 90)
- **CNFG_OP_MODE_S** (line 88)
- **CNFG_READ_MODE** (line 94)
- **CON_BRD** (line 112)
- **CON_BWR** (line 111)
- **CON_FIFO_FLUSH** (line 114)
- **CON_NFI_RST** (line 113)
- **CON_SEC_NUM_S** (line 110)
- **CS_DESELECT_CYC_S** (line 203)
- **CUS_PG_DONE** (line 216)
- **CUS_READ_DONE** (line 217)
- **DATARD_CUSTOM_EN** (line 202)
- **DATA_READ_CMD_S** (line 179)
- **DATA_READ_DUMMY_S** (line 177)
- **DATA_READ_LATCH_LAT** (line 199)
- **DATA_READ_LATCH_LAT_S** (line 200)
- **DATA_READ_MAX_DUMMY** (line 178)
- **DATA_READ_MODE** (line 193)
- **DATA_READ_MODE_DUAL** (line 197)
- **DATA_READ_MODE_QUAD** (line 198)
- **DATA_READ_MODE_S** (line 192)
- **DATA_READ_MODE_X1** (line 194)
- **DATA_READ_MODE_X2** (line 195)
- **DATA_READ_MODE_X4** (line 196)
- **FIFO_RD_LTC_S** (line 190)
- **FIFO_RD_REMAIN_S** (line 137)
- **FIFO_WR_REMAIN_S** (line 136)
- **MAC_XIO_SEL** (line 167)
- **MAS_ADDR** (line 158)
- **MAS_RD** (line 159)
- **MAS_RDDLY** (line 161)
- **MAS_WR** (line 160)
- **NFI_ADDRCNTR** (line 139)
- **NFI_BYTELEN** (line 146)
- **NFI_CMD** (line 122)
- **NFI_CMD_DUMMY_READ** (line 123)
- **NFI_CMD_DUMMY_WRITE** (line 124)
- **NFI_CNFG** (line 87)
- **NFI_CON** (line 109)
- **NFI_DEBUG_CON1** (line 154)
- **NFI_FDM0L** (line 149)
- **NFI_FDM0M** (line 150)
- **NFI_FDML**(n) (line 151)
- **NFI_FDMM**(n) (line 152)
- **NFI_FDM_ECC_NUM_S** (line 99)
- **NFI_FDM_NUM_S** (line 100)
- **NFI_FIFOSTA** (line 135)
- **NFI_FSM** (line 132)
- **NFI_INTR_EN** (line 116)
- **NFI_INTR_STA** (line 117)
- **NFI_IRQ_CUS_PG** (line 120)
- **NFI_IRQ_CUS_READ** (line 119)
- **NFI_IRQ_INTR_EN** (line 118)
- **NFI_MASTERSTA** (line 157)
- **NFI_MASTERSTA_MASK_7622** (line 162)
- **NFI_MASTERSTA_MASK_7986** (line 163)
- **NFI_NAND_FSM_7622** (line 130)
- **NFI_NAND_FSM_7986** (line 131)
- **NFI_PAGEFMT** (line 97)
- **NFI_PAGE_SIZE_2K_4K** (line 105)
- **NFI_PAGE_SIZE_4K_8K** (line 106)
- **NFI_PAGE_SIZE_512_2K** (line 104)
- **NFI_PAGE_SIZE_8K_16K** (line 107)
- **NFI_PAGE_SIZE_S** (line 103)
- **NFI_SEC_CNTR**(val) (line 142)
- **NFI_SEC_SEL_512** (line 102)
- **NFI_SPARE_SIZE_LS_S** (line 98)
- **NFI_SPARE_SIZE_S** (line 101)
- **NFI_STA** (line 129)
- **NFI_STRADDR** (line 144)
- **NFI_STRDATA** (line 126)
- **PG_LOAD_CMD_S** (line 184)
- **PG_LOAD_CUSTOM_EN** (line 201)
- **PG_LOAD_X4_EN** (line 191)
- **PROGRAM_LOAD_BYTE_NUM_S** (line 206)
- **READ_DATA_BYTE_NUM_S** (line 207)
- **READ_EMPTY** (line 133)
- **SEC_CNTR** (line 140)
- **SEC_CNTR_S** (line 141)
- **SFCK_SAM_DLY** (line 211)
- **SFCK_SAM_DLY_RANGE** (line 213)
- **SFCK_SAM_DLY_S** (line 210)
- **SFCK_SAM_DLY_TOTAL** (line 212)
- **SF_MAC_EN** (line 168)
- **SF_TRIG** (line 169)
- **SNFI_POLL_INTERVAL** (line 227)
- **SNF_CFG** (line 221)
- **SNF_DLY_CTL3** (line 209)
- **SNF_GPRAM** (line 224)
- **SNF_GPRAM_SIZE** (line 225)
- **SNF_MAC_CTL** (line 166)
- **SNF_MAC_INL** (line 174)
- **SNF_MAC_OUTL** (line 173)
- **SNF_MISC_CTL** (line 188)
- **SNF_MISC_CTL2** (line 205)
- **SNF_PG_CTL1** (line 183)
- **SNF_PG_CTL2** (line 186)
- **SNF_RD_CTL2** (line 176)
- **SNF_RD_CTL3** (line 181)
- **SNF_STA_CTL1** (line 215)
- **SPI_MODE** (line 222)
- **SPI_STATE** (line 219)
- **SPI_STATE_S** (line 218)
- **STR_DATA** (line 127)
- **SW_RST** (line 189)
- **WBUF_EN** (line 155)
- **WIP** (line 171)
- **WIP_READY** (line 170)
