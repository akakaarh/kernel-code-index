# drivers/spi/spi-amlogic-spifc-a4.c

Subsystem: drivers/spi

## Functions (40)

### aml_get_dma_safe_input_buf
- Return type: static void *
- Signature: aml_get_dma_safe_input_buf(const struct spi_mem_op * op)
- Line: 479

### aml_set_spi_clk
- Return type: static int
- Signature: aml_set_spi_clk(struct aml_sfc * sfc,struct spi_device * spi)
- Line: 904

### aml_sfc_adjust_op_size
- Return type: static int
- Signature: aml_sfc_adjust_op_size(struct spi_mem * mem,struct spi_mem_op * op)
- Line: 831

### aml_sfc_cal_timeout_cycle
- Return type: static u64
- Signature: aml_sfc_cal_timeout_cycle(struct aml_sfc * sfc,const struct spi_mem_op * op)
- Line: 516

### aml_sfc_check_ecc_pages_valid
- Return type: static void
- Signature: aml_sfc_check_ecc_pages_valid(struct aml_sfc * sfc,bool raw)
- Line: 537

### aml_sfc_check_hwecc_status
- Return type: static int
- Signature: aml_sfc_check_hwecc_status(struct aml_sfc * sfc,__le64 * info_buf)
- Line: 664

### aml_sfc_clk_init
- Return type: static int
- Signature: aml_sfc_clk_init(struct aml_sfc * sfc)
- Line: 1076

### aml_sfc_dma_buffer_is_safe
- Return type: static bool
- Signature: aml_sfc_dma_buffer_is_safe(const void * buffer)
- Line: 468

### aml_sfc_dma_buffer_release
- Return type: static void
- Signature: aml_sfc_dma_buffer_release(struct aml_sfc * sfc,int datalen,int infolen,enum dma_data_direction dir)
- Line: 457

### aml_sfc_dma_buffer_setup
- Return type: static int
- Signature: aml_sfc_dma_buffer_setup(struct aml_sfc * sfc,void * databuf,int datalen,void * infobuf,int infolen,enum dma_data_direction dir)
- Line: 403

### aml_sfc_ecc_cleanup_ctx
- Return type: static void
- Signature: aml_sfc_ecc_cleanup_ctx(struct nand_device * nand)
- Line: 1007

### aml_sfc_ecc_finish_io_req
- Return type: static int
- Signature: aml_sfc_ecc_finish_io_req(struct nand_device * nand,struct nand_page_io_req * req)
- Line: 1041

### aml_sfc_ecc_init_ctx
- Return type: static int
- Signature: aml_sfc_ecc_init_ctx(struct nand_device * nand)
- Line: 947

### aml_sfc_ecc_prepare_io_req
- Return type: static int
- Signature: aml_sfc_ecc_prepare_io_req(struct nand_device * nand,struct nand_page_io_req * req)
- Line: 1016

### aml_sfc_end_transfer
- Return type: static int
- Signature: aml_sfc_end_transfer(struct aml_sfc * sfc,u32 clk2cs_cycle)
- Line: 271

### aml_sfc_exec_op
- Return type: static int
- Signature: aml_sfc_exec_op(struct spi_mem * mem,const struct spi_mem_op * op)
- Line: 792

### aml_sfc_get_dma_safe_output_buf
- Return type: static void *
- Signature: aml_sfc_get_dma_safe_output_buf(const struct spi_mem_op * op)
- Line: 499

### aml_sfc_get_user_byte
- Return type: static void
- Signature: aml_sfc_get_user_byte(struct aml_sfc * sfc,__le64 * info_buf,u8 * oob_buf)
- Line: 649

### aml_sfc_is_snand_hwecc_page_op
- Return type: static bool
- Signature: aml_sfc_is_snand_hwecc_page_op(struct aml_sfc * sfc,const struct spi_mem_op * op)
- Line: 377

### aml_sfc_is_xio_op
- Return type: static bool
- Signature: aml_sfc_is_xio_op(const struct spi_mem_op * op)
- Line: 337

### aml_sfc_layout_ecc
- Return type: static int
- Signature: aml_sfc_layout_ecc(struct mtd_info * mtd,int section,struct mtd_oob_region * oobregion)
- Line: 854

### aml_sfc_ooblayout_free
- Return type: static int
- Signature: aml_sfc_ooblayout_free(struct mtd_info * mtd,int section,struct mtd_oob_region * oobregion)
- Line: 868

### aml_sfc_pre_transfer
- Return type: static int
- Signature: aml_sfc_pre_transfer(struct aml_sfc * sfc,u32 idle_cycle,u32 cs2clk_cycle)
- Line: 260

### aml_sfc_probe
- Return type: static int
- Signature: aml_sfc_probe(struct platform_device * pdev)
- Line: 1093

### aml_sfc_put_dma_safe_input_buf
- Return type: static void
- Signature: aml_sfc_put_dma_safe_input_buf(const struct spi_mem_op * op,void * buf)
- Line: 487

### aml_sfc_put_dma_safe_output_buf
- Return type: static void
- Signature: aml_sfc_put_dma_safe_output_buf(const struct spi_mem_op * op,const void * buf)
- Line: 507

### aml_sfc_raw_io_op
- Return type: static int
- Signature: aml_sfc_raw_io_op(struct aml_sfc * sfc,const struct spi_mem_op * op)
- Line: 557

### aml_sfc_read_page_hwecc
- Return type: static int
- Signature: aml_sfc_read_page_hwecc(struct aml_sfc * sfc,const struct spi_mem_op * op)
- Line: 690

### aml_sfc_send_addr
- Return type: static int
- Signature: aml_sfc_send_addr(struct aml_sfc * sfc,const struct spi_mem_op * op)
- Line: 317

### aml_sfc_send_cmd
- Return type: static int
- Signature: aml_sfc_send_cmd(struct aml_sfc * sfc,const struct spi_mem_op * op)
- Line: 298

### aml_sfc_send_cmd_addr_dummy
- Return type: static int
- Signature: aml_sfc_send_cmd_addr_dummy(struct aml_sfc * sfc,const struct spi_mem_op * op)
- Line: 351

### aml_sfc_set_bus_width
- Return type: static int
- Signature: aml_sfc_set_bus_width(struct aml_sfc * sfc,u8 buswidth,u32 mask)
- Line: 282

### aml_sfc_set_user_byte
- Return type: static void
- Signature: aml_sfc_set_user_byte(struct aml_sfc * sfc,__le64 * info_buf,u8 * oob_buf,bool auto_oob)
- Line: 632

### aml_sfc_setup
- Return type: static int
- Signature: aml_sfc_setup(struct spi_device * spi)
- Line: 928

### aml_sfc_to_ecc_ctx
- Return type: static void *
- Signature: aml_sfc_to_ecc_ctx(struct aml_sfc * sfc)
- Line: 225

### aml_sfc_unregister_ecc_engine
- Return type: static void
- Signature: aml_sfc_unregister_ecc_engine(void * data)
- Line: 1069

### aml_sfc_wait_cmd_finish
- Return type: static int
- Signature: aml_sfc_wait_cmd_finish(struct aml_sfc * sfc,u64 timeout_ms)
- Line: 230

### aml_sfc_write_page_hwecc
- Return type: static int
- Signature: aml_sfc_write_page_hwecc(struct aml_sfc * sfc,const struct spi_mem_op * op)
- Line: 743

### aml_spi_settings
- Return type: static int
- Signature: aml_spi_settings(struct aml_sfc * sfc,struct spi_device * spi)
- Line: 887

### nand_to_aml_sfc
- Return type: static aml_sfc *
- Signature: nand_to_aml_sfc(struct nand_device * nand)
- Line: 218

## Structs (4)

### aml_ecc_stats
- Line: 174
- Members:
  - stepsize: u32
  - nsteps: u32
  - strength: u32
  - oobsize: u32
  - bch: u32
  - corrected: u32
  - bitflips: u32
  - failed: u32
  - ecc_caps: aml_sfc_ecc_cfg *
  - num_ecc_caps: u32
  - dev: device *
  - gate_clk: clk *
  - core_clk: clk *
  - ctrl: spi_controller *
  - regmap_base: regmap *
  - caps: const struct aml_sfc_caps *
  - ecc_eng: nand_ecc_engine
  - ecc_stats: aml_ecc_stats
  - daddr: dma_addr_t
  - iaddr: dma_addr_t
  - info_bytes: u32
  - bus_rate: u32
  - flags: u32
  - rx_adj: u32
  - cs_sel: u32
  - data_buf: u8 *
  - info_buf: __le64 *
  - priv: u8 *

### aml_sfc
- Line: 185
- Members:
  - stepsize: u32
  - nsteps: u32
  - strength: u32
  - oobsize: u32
  - bch: u32
  - corrected: u32
  - bitflips: u32
  - failed: u32
  - ecc_caps: aml_sfc_ecc_cfg *
  - num_ecc_caps: u32
  - dev: device *
  - gate_clk: clk *
  - core_clk: clk *
  - ctrl: spi_controller *
  - regmap_base: regmap *
  - caps: const struct aml_sfc_caps *
  - ecc_eng: nand_ecc_engine
  - ecc_stats: aml_ecc_stats
  - daddr: dma_addr_t
  - iaddr: dma_addr_t
  - info_bytes: u32
  - bus_rate: u32
  - flags: u32
  - rx_adj: u32
  - cs_sel: u32
  - data_buf: u8 *
  - info_buf: __le64 *
  - priv: u8 *

### aml_sfc_caps
- Line: 180
- Members:
  - stepsize: u32
  - nsteps: u32
  - strength: u32
  - oobsize: u32
  - bch: u32
  - corrected: u32
  - bitflips: u32
  - failed: u32
  - ecc_caps: aml_sfc_ecc_cfg *
  - num_ecc_caps: u32
  - dev: device *
  - gate_clk: clk *
  - core_clk: clk *
  - ctrl: spi_controller *
  - regmap_base: regmap *
  - caps: const struct aml_sfc_caps *
  - ecc_eng: nand_ecc_engine
  - ecc_stats: aml_ecc_stats
  - daddr: dma_addr_t
  - iaddr: dma_addr_t
  - info_bytes: u32
  - bus_rate: u32
  - flags: u32
  - rx_adj: u32
  - cs_sel: u32
  - data_buf: u8 *
  - info_buf: __le64 *
  - priv: u8 *

### aml_sfc_ecc_cfg
- Line: 166
- Members:
  - stepsize: u32
  - nsteps: u32
  - strength: u32
  - oobsize: u32
  - bch: u32
  - corrected: u32
  - bitflips: u32
  - failed: u32
  - ecc_caps: aml_sfc_ecc_cfg *
  - num_ecc_caps: u32
  - dev: device *
  - gate_clk: clk *
  - core_clk: clk *
  - ctrl: spi_controller *
  - regmap_base: regmap *
  - caps: const struct aml_sfc_caps *
  - ecc_eng: nand_ecc_engine
  - ecc_stats: aml_ecc_stats
  - daddr: dma_addr_t
  - iaddr: dma_addr_t
  - info_bytes: u32
  - bus_rate: u32
  - flags: u32
  - rx_adj: u32
  - cs_sel: u32
  - data_buf: u8 *
  - info_buf: __le64 *
  - priv: u8 *

## Variables (8)

- static **aml_a113l2_ecc_caps** : aml_sfc_ecc_cfg[] (line 208)
- static **aml_a113l2_sfc_caps** : const struct aml_sfc_caps (line 213)
- static **aml_sfc_driver** : platform_driver (line 1190)
- static **aml_sfc_ecc_engine_ops** : const struct nand_ecc_engine_ops (line 1062)
- static **aml_sfc_mem_caps** : const struct spi_controller_mem_caps (line 1058)
- static **aml_sfc_mem_ops** : const struct spi_controller_mem_ops (line 849)
- static **aml_sfc_of_match** : const struct of_device_id[] (line 1181)
- static **aml_sfc_ooblayout_ops** : const struct mtd_ooblayout_ops (line 882)

## Macros (116)

- **ADDR_LANE** (line 99)
- **ALE** (line 51)
- **AML_ECC_DATA**(sz,s,b) (line 206)
- **CHIP_SELECT_MASK** (line 45)
- **CLE** (line 50)
- **CMD_ADDR**(cs_sel,addr) (line 73)
- **CMD_COMMAND**(cs_sel,cmd) (line 72)
- **CMD_DATA_ADDRH**(addr) (line 79)
- **CMD_DATA_ADDRL**(addr) (line 78)
- **CMD_DUMMY**(cs_sel,cyc) (line 74)
- **CMD_IDLE**(cs_sel,cyc) (line 75)
- **CMD_INFO_ADDRH**(addr) (line 81)
- **CMD_INFO_ADDRL**(addr) (line 80)
- **CMD_LANE** (line 106)
- **CMD_MEM2NAND**(bch,pages) (line 76)
- **CMD_NAND2MEM**(bch,pages) (line 77)
- **CMD_SEED**(seed) (line 82)
- **CPHA** (line 101)
- **CPOL** (line 100)
- **CS_0** (line 47)
- **CS_1** (line 48)
- **CS_HOLD_CYCLE** (line 88)
- **CS_NONE** (line 46)
- **CS_SETUP_CYCLE** (line 87)
- **DATA_LANE** (line 107)
- **DEFAULT_BUS_CYCLE** (line 89)
- **DEFAULT_PULLUP_CYCLE** (line 86)
- **DMA_ADDR_ALIGN** (line 94)
- **DRD** (line 53)
- **DUMMY** (line 54)
- **DWR** (line 52)
- **ECC_BCH8_1K** (line 120)
- **ECC_BCH8_512** (line 119)
- **ECC_BCH8_DEFAULT_STEP** (line 125)
- **ECC_BCH8_INFO_BYTES** (line 123)
- **ECC_BCH8_PARITY_BYTES** (line 121)
- **ECC_BCH8_STRENGTH** (line 124)
- **ECC_BCH8_USER_BYTES** (line 122)
- **ECC_BCH_MAX_SECT_SIZE** (line 129)
- **ECC_COMPLETE** (line 114)
- **ECC_DEFAULT_BCH_MODE** (line 126)
- **ECC_ERR_CNT**(x) (line 116)
- **ECC_PATTERN** (line 128)
- **ECC_PER_INFO_BYTE** (line 127)
- **ECC_UNCORRECTABLE** (line 115)
- **ECC_ZERO_CNT**(x) (line 117)
- **ENABLE_RANDOM** (line 70)
- **EN_HOLD** (line 102)
- **EN_WP** (line 103)
- **EXT_CYCLE_MASK** (line 57)
- **GET_CMD_SIZE**(x) (line 84)
- **IDLE** (line 55)
- **IDLE_CYCLE_MASK** (line 56)
- **LANE_MAX** (line 108)
- **OP_ADH** (line 63)
- **OP_ADL** (line 62)
- **OP_AIH** (line 65)
- **OP_AIL** (line 64)
- **OP_ASH** (line 67)
- **OP_ASL** (line 66)
- **OP_M2N** (line 59)
- **OP_N2M** (line 60)
- **OP_SEED** (line 68)
- **OP_STS** (line 61)
- **RAW_EXT_SIZE** (line 98)
- **RAW_MAX_RW_SIZE_MASK** (line 111)
- **RAW_SIZE** (line 91)
- **RAW_SIZE_BW** (line 92)
- **RXADJ** (line 105)
- **SEED_MASK** (line 69)
- **SFC_ADR** (line 33)
- **SFC_AUTO_OOB** (line 136)
- **SFC_BUF** (line 30)
- **SFC_BUF_SIZE** (line 142)
- **SFC_BUS_DEFAULT_CLK** (line 147)
- **SFC_CADR** (line 36)
- **SFC_CFG** (line 27)
- **SFC_CMD** (line 26)
- **SFC_DADR** (line 28)
- **SFC_DATABUF_SIZE** (line 140)
- **SFC_DATA_ONLY** (line 133)
- **SFC_DATA_OOB** (line 135)
- **SFC_DATA_RANDOM** (line 132)
- **SFC_DC** (line 32)
- **SFC_DH** (line 35)
- **SFC_DL** (line 34)
- **SFC_HWECC** (line 131)
- **SFC_IADR** (line 29)
- **SFC_INFO** (line 31)
- **SFC_INFOBUF_SIZE** (line 141)
- **SFC_MAX_CS_NUM** (line 148)
- **SFC_MAX_FREQUENCY** (line 145)
- **SFC_MIN_FREQUENCY** (line 146)
- **SFC_OOB_ONLY** (line 134)
- **SFC_RAW_RW** (line 137)
- **SFC_RX_DAT** (line 39)
- **SFC_RX_IDX** (line 38)
- **SFC_SADR** (line 37)
- **SFC_SPI_CFG** (line 40)
- **SFC_XFER_MDOE_MASK** (line 138)
- **SPIFLASH_RD** (line 158)
- **SPIFLASH_RD_DUAL** (line 156)
- **SPIFLASH_RD_DUALIO** (line 155)
- **SPIFLASH_RD_FAST** (line 157)
- **SPIFLASH_RD_OCTAL** (line 152)
- **SPIFLASH_RD_OCTALIO** (line 151)
- **SPIFLASH_RD_QUAD** (line 154)
- **SPIFLASH_RD_QUADIO** (line 153)
- **SPIFLASH_UP** (line 164)
- **SPIFLASH_UP_QUAD** (line 163)
- **SPIFLASH_WR** (line 162)
- **SPIFLASH_WR_OCTAL** (line 160)
- **SPIFLASH_WR_OCTALIO** (line 159)
- **SPIFLASH_WR_QUAD** (line 161)
- **SPI_MODE_EN** (line 97)
- **TXADJ** (line 104)
