# drivers/spi/spi-qpic-snand.c

Subsystem: drivers/spi

## Functions (37)

### nand_to_qcom_snand
- Return type: static qcom_nand_controller *
- Signature: nand_to_qcom_snand(struct nand_device * nand)
- Line: 161

### qcom_spi_block_erase
- Return type: static int
- Signature: qcom_spi_block_erase(struct qcom_nand_controller * snandc)
- Line: 504

### qcom_spi_check_error
- Return type: static int
- Signature: qcom_spi_check_error(struct qcom_nand_controller * snandc)
- Line: 640

### qcom_spi_check_raw_flash_errors
- Return type: static int
- Signature: qcom_spi_check_raw_flash_errors(struct qcom_nand_controller * snandc,int cw_cnt)
- Line: 559

### qcom_spi_cmd_mapping
- Return type: static int
- Signature: qcom_spi_cmd_mapping(struct qcom_nand_controller * snandc,u32 opcode,u32 * cmd)
- Line: 1253

### qcom_spi_config_cw_read
- Return type: static void
- Signature: qcom_spi_config_cw_read(struct qcom_nand_controller * snandc,bool use_ecc,int cw)
- Line: 479

### qcom_spi_config_cw_write
- Return type: static void
- Signature: qcom_spi_config_cw_write(struct qcom_nand_controller * snandc)
- Line: 1015

### qcom_spi_config_page_write
- Return type: static void
- Signature: qcom_spi_config_page_write(struct qcom_nand_controller * snandc)
- Line: 1007

### qcom_spi_config_single_cw_page_read
- Return type: static void
- Signature: qcom_spi_config_single_cw_page_read(struct qcom_nand_controller * snandc,bool use_ecc,int cw)
- Line: 535

### qcom_spi_ecc_cleanup_ctx_pipelined
- Return type: static void
- Signature: qcom_spi_ecc_cleanup_ctx_pipelined(struct nand_device * nand)
- Line: 401

### qcom_spi_ecc_finish_io_req_pipelined
- Return type: static int
- Signature: qcom_spi_ecc_finish_io_req_pipelined(struct nand_device * nand,struct nand_page_io_req * req)
- Line: 431

### qcom_spi_ecc_init_ctx_pipelined
- Return type: static int
- Signature: qcom_spi_ecc_init_ctx_pipelined(struct nand_device * nand)
- Line: 248

### qcom_spi_ecc_prepare_io_req_pipelined
- Return type: static int
- Signature: qcom_spi_ecc_prepare_io_req_pipelined(struct nand_device * nand,struct nand_page_io_req * req)
- Line: 408

### qcom_spi_exec_op
- Return type: static int
- Signature: qcom_spi_exec_op(struct spi_mem * mem,const struct spi_mem_op * op)
- Line: 1471

### qcom_spi_init
- Return type: static int
- Signature: qcom_spi_init(struct qcom_nand_controller * snandc)
- Line: 169

### qcom_spi_io_op
- Return type: static int
- Signature: qcom_spi_io_op(struct qcom_nand_controller * snandc,const struct spi_mem_op * op)
- Line: 1371

### qcom_spi_is_page_op
- Return type: static bool
- Signature: qcom_spi_is_page_op(const struct spi_mem_op * op)
- Line: 1433

### qcom_spi_ooblayout_ecc
- Return type: static int
- Signature: qcom_spi_ooblayout_ecc(struct mtd_info * mtd,int section,struct mtd_oob_region * oobregion)
- Line: 203

### qcom_spi_ooblayout_free
- Return type: static int
- Signature: qcom_spi_ooblayout_free(struct mtd_info * mtd,int section,struct mtd_oob_region * oobregion)
- Line: 227

### qcom_spi_probe
- Return type: static int
- Signature: qcom_spi_probe(struct platform_device * pdev)
- Line: 1500

### qcom_spi_program_ecc
- Return type: static int
- Signature: qcom_spi_program_ecc(struct qcom_nand_controller * snandc,const struct spi_mem_op * op)
- Line: 1108

### qcom_spi_program_execute
- Return type: static int
- Signature: qcom_spi_program_execute(struct qcom_nand_controller * snandc,const struct spi_mem_op * op)
- Line: 1238

### qcom_spi_program_oob
- Return type: static int
- Signature: qcom_spi_program_oob(struct qcom_nand_controller * snandc,const struct spi_mem_op * op)
- Line: 1185

### qcom_spi_program_raw
- Return type: static int
- Signature: qcom_spi_program_raw(struct qcom_nand_controller * snandc,const struct spi_mem_op * op)
- Line: 1026

### qcom_spi_read_cw_raw
- Return type: static int
- Signature: qcom_spi_read_cw_raw(struct qcom_nand_controller * snandc,u8 * data_buf,u8 * oob_buf,int cw)
- Line: 707

### qcom_spi_read_last_cw
- Return type: static int
- Signature: qcom_spi_read_last_cw(struct qcom_nand_controller * snandc,const struct spi_mem_op * op)
- Line: 575

### qcom_spi_read_page
- Return type: static int
- Signature: qcom_spi_read_page(struct qcom_nand_controller * snandc,const struct spi_mem_op * op)
- Line: 989

### qcom_spi_read_page_ecc
- Return type: static int
- Signature: qcom_spi_read_page_ecc(struct qcom_nand_controller * snandc,const struct spi_mem_op * op)
- Line: 825

### qcom_spi_read_page_oob
- Return type: static int
- Signature: qcom_spi_read_page_oob(struct qcom_nand_controller * snandc,const struct spi_mem_op * op)
- Line: 914

### qcom_spi_read_page_raw
- Return type: static int
- Signature: qcom_spi_read_page_raw(struct qcom_nand_controller * snandc,const struct spi_mem_op * op)
- Line: 797

### qcom_spi_remove
- Return type: static void
- Signature: qcom_spi_remove(struct platform_device * pdev)
- Line: 1607

### qcom_spi_send_cmdaddr
- Return type: static int
- Signature: qcom_spi_send_cmdaddr(struct qcom_nand_controller * snandc,const struct spi_mem_op * op)
- Line: 1317

### qcom_spi_set_read_loc
- Return type: static void
- Signature: qcom_spi_set_read_loc(struct qcom_nand_controller * snandc,int cw,int reg,int cw_offset,int read_size,int is_last_read_loc)
- Line: 459

### qcom_spi_set_read_loc_first
- Return type: static void
- Signature: qcom_spi_set_read_loc_first(struct qcom_nand_controller * snandc,int reg,int cw_offset,int read_size,int is_last_read_loc)
- Line: 119

### qcom_spi_set_read_loc_last
- Return type: static void
- Signature: qcom_spi_set_read_loc_last(struct qcom_nand_controller * snandc,int reg,int cw_offset,int read_size,int is_last_read_loc)
- Line: 140

### qcom_spi_supports_op
- Return type: static bool
- Signature: qcom_spi_supports_op(struct spi_mem * mem,const struct spi_mem_op * op)
- Line: 1455

### qcom_spi_write_page
- Return type: static int
- Signature: qcom_spi_write_page(struct qcom_nand_controller * snandc,const struct spi_mem_op * op)
- Line: 1301

## Structs (4)

### qcom_ecc_stats
- Line: 74
- Members:
  - snandc_flash: __le32
  - snandc_buffer: __le32
  - snandc_erased_cw: __le32
  - corrected: u32
  - bitflips: u32
  - failed: u32
  - ecc_bytes_hw: int
  - spare_bytes: int
  - bbm_size: int
  - ecc_mode: int
  - bytes: int
  - steps: int
  - step_size: int
  - strength: int
  - cw_size: int
  - cw_data: int
  - cfg0: u32
  - cfg1: u32
  - cfg0_raw: u32
  - cfg1_raw: u32
  - ecc_buf_cfg: u32
  - ecc_bch_cfg: u32
  - bch_enabled: bool
  - snandc: qcom_nand_controller *
  - ctlr: spi_controller *
  - mtd: mtd_info *
  - iomacro_clk: clk *
  - ecc: qpic_ecc *
  - ecc_stats: qcom_ecc_stats
  - ecc_eng: nand_ecc_engine
  - data_buf: u8 *
  - oob_buf: u8 *
  - addr1: __le32
  - addr2: __le32
  - cmd: __le32
  - num_cw: u32
  - oob_rw: bool
  - page_rw: bool
  - raw_rw: bool

### qpic_ecc
- Line: 80
- Members:
  - snandc_flash: __le32
  - snandc_buffer: __le32
  - snandc_erased_cw: __le32
  - corrected: u32
  - bitflips: u32
  - failed: u32
  - ecc_bytes_hw: int
  - spare_bytes: int
  - bbm_size: int
  - ecc_mode: int
  - bytes: int
  - steps: int
  - step_size: int
  - strength: int
  - cw_size: int
  - cw_data: int
  - cfg0: u32
  - cfg1: u32
  - cfg0_raw: u32
  - cfg1_raw: u32
  - ecc_buf_cfg: u32
  - ecc_bch_cfg: u32
  - bch_enabled: bool
  - snandc: qcom_nand_controller *
  - ctlr: spi_controller *
  - mtd: mtd_info *
  - iomacro_clk: clk *
  - ecc: qpic_ecc *
  - ecc_stats: qcom_ecc_stats
  - ecc_eng: nand_ecc_engine
  - data_buf: u8 *
  - oob_buf: u8 *
  - addr1: __le32
  - addr2: __le32
  - cmd: __le32
  - num_cw: u32
  - oob_rw: bool
  - page_rw: bool
  - raw_rw: bool

### qpic_spi_nand
- Line: 100
- Members:
  - snandc_flash: __le32
  - snandc_buffer: __le32
  - snandc_erased_cw: __le32
  - corrected: u32
  - bitflips: u32
  - failed: u32
  - ecc_bytes_hw: int
  - spare_bytes: int
  - bbm_size: int
  - ecc_mode: int
  - bytes: int
  - steps: int
  - step_size: int
  - strength: int
  - cw_size: int
  - cw_data: int
  - cfg0: u32
  - cfg1: u32
  - cfg0_raw: u32
  - cfg1_raw: u32
  - ecc_buf_cfg: u32
  - ecc_bch_cfg: u32
  - bch_enabled: bool
  - snandc: qcom_nand_controller *
  - ctlr: spi_controller *
  - mtd: mtd_info *
  - iomacro_clk: clk *
  - ecc: qpic_ecc *
  - ecc_stats: qcom_ecc_stats
  - ecc_eng: nand_ecc_engine
  - data_buf: u8 *
  - oob_buf: u8 *
  - addr1: __le32
  - addr2: __le32
  - cmd: __le32
  - num_cw: u32
  - oob_rw: bool
  - page_rw: bool
  - raw_rw: bool

### snandc_read_status
- Line: 62
- Members:
  - snandc_flash: __le32
  - snandc_buffer: __le32
  - snandc_erased_cw: __le32
  - corrected: u32
  - bitflips: u32
  - failed: u32
  - ecc_bytes_hw: int
  - spare_bytes: int
  - bbm_size: int
  - ecc_mode: int
  - bytes: int
  - steps: int
  - step_size: int
  - strength: int
  - cw_size: int
  - cw_data: int
  - cfg0: u32
  - cfg1: u32
  - cfg0_raw: u32
  - cfg1_raw: u32
  - ecc_buf_cfg: u32
  - ecc_bch_cfg: u32
  - bch_enabled: bool
  - snandc: qcom_nand_controller *
  - ctlr: spi_controller *
  - mtd: mtd_info *
  - iomacro_clk: clk *
  - ecc: qpic_ecc *
  - ecc_stats: qcom_ecc_stats
  - ecc_eng: nand_ecc_engine
  - data_buf: u8 *
  - oob_buf: u8 *
  - addr1: __le32
  - addr2: __le32
  - cmd: __le32
  - num_cw: u32
  - oob_rw: bool
  - page_rw: bool
  - raw_rw: bool

## Variables (7)

- static **ipq9574_snandc_props** : const struct qcom_nandc_props (line 1620)
- static **qcom_snandc_of_match** : const struct of_device_id[] (line 1626)
- static **qcom_spi_driver** : platform_driver (line 1635)
- static **qcom_spi_ecc_engine_ops_pipelined** : const struct nand_ecc_engine_ops (line 451)
- static **qcom_spi_mem_caps** : const struct spi_controller_mem_caps (line 1496)
- static **qcom_spi_mem_ops** : const struct spi_controller_mem_ops (line 1491)
- static **qcom_spi_ooblayout** : const struct mtd_ooblayout_ops (line 243)

## Macros (31)

- **ACC_FEATURE** (line 57)
- **BAD_BLOCK_MARKER_SIZE** (line 58)
- **CLK_CNTR_INIT_VAL_VEC** (line 33)
- **CLK_CNTR_INIT_VAL_VEC_MASK** (line 34)
- **FEA_STATUS_DEV_ADDR** (line 35)
- **FEA_STATUS_DEV_ADDR_MASK** (line 36)
- **LOAD_CLK_CNTR_INIT_EN** (line 32)
- **NAND_BUSY_CHECK_WAIT_CNT** (line 28)
- **NAND_FLASH_FEATURES** (line 29)
- **NAND_FLASH_SPI_CFG** (line 26)
- **NAND_NUM_ADDR_CYCLES** (line 27)
- **OOB_BUF_SIZE** (line 59)
- **QPIC_QSPI_NUM_CS** (line 40)
- **QPIC_SET_FEATURE** (line 45)
- **SPINAND_ERASE** (line 52)
- **SPINAND_GET_FEATURE** (line 49)
- **SPINAND_PROGRAM_EXECUTE** (line 54)
- **SPINAND_PROGRAM_LOAD** (line 55)
- **SPINAND_READ** (line 51)
- **SPINAND_READID** (line 48)
- **SPINAND_RESET** (line 47)
- **SPINAND_SET_FEATURE** (line 50)
- **SPINAND_WRITE_EN** (line 53)
- **SPI_CFG** (line 37)
- **SPI_HOLD** (line 44)
- **SPI_NUM_ADDR** (line 38)
- **SPI_TRANSFER_MODE_x1** (line 41)
- **SPI_TRANSFER_MODE_x4** (line 42)
- **SPI_WAIT_CNT** (line 39)
- **SPI_WP** (line 43)
- **ecceng_to_qspi**(eng) (line 60)
