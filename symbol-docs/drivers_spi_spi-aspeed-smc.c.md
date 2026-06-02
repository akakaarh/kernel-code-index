# drivers/spi/spi-aspeed-smc.c

Subsystem: drivers/spi

## Functions (53)

### aspeed_adjust_window_ast2400
- Return type: static int
- Signature: aspeed_adjust_window_ast2400(struct aspeed_spi * aspi)
- Line: 564

### aspeed_adjust_window_ast2500
- Return type: static int
- Signature: aspeed_adjust_window_ast2500(struct aspeed_spi * aspi)
- Line: 586

### aspeed_adjust_window_ast2600
- Return type: static int
- Signature: aspeed_adjust_window_ast2600(struct aspeed_spi * aspi)
- Line: 629

### aspeed_get_clk_div_ast2400
- Return type: static u32
- Signature: aspeed_get_clk_div_ast2400(struct aspeed_spi_chip * chip,u32 max_hz)
- Line: 1251

### aspeed_get_clk_div_ast2500
- Return type: static u32
- Signature: aspeed_get_clk_div_ast2500(struct aspeed_spi_chip * chip,u32 max_hz)
- Line: 1284

### aspeed_get_clk_div_ast2600
- Return type: static u32
- Signature: aspeed_get_clk_div_ast2600(struct aspeed_spi_chip * chip,u32 max_hz)
- Line: 1330

### aspeed_spi_ast2600_calibrate
- Return type: static int
- Signature: aspeed_spi_ast2600_calibrate(struct aspeed_spi_chip * chip,u32 hdiv,const u8 * golden_buf,u8 * test_buf)
- Line: 1497

### aspeed_spi_ast2600_optimized_timing
- Return type: static u32
- Signature: aspeed_spi_ast2600_optimized_timing(u32 rows,u32 cols,u8 buf[rows][cols])
- Line: 1470

### aspeed_spi_calibrate
- Return type: static int
- Signature: aspeed_spi_calibrate(struct aspeed_spi_chip * chip,u32 hdiv,const u8 * golden_buf,u8 * test_buf)
- Line: 1168

### aspeed_spi_check_calib_data
- Return type: static bool
- Signature: aspeed_spi_check_calib_data(const u8 * test_buf,u32 size)
- Line: 1221

### aspeed_spi_check_reads
- Return type: static bool
- Signature: aspeed_spi_check_reads(struct aspeed_spi_chip * chip,const u8 * golden_buf,u8 * test_buf)
- Line: 1145

### aspeed_spi_chip_adjust_window
- Return type: static int
- Signature: aspeed_spi_chip_adjust_window(struct aspeed_spi_chip * chip,u32 local_offset,u32 size)
- Line: 670

### aspeed_spi_chip_enable
- Return type: static void
- Signature: aspeed_spi_chip_enable(struct aspeed_spi * aspi,unsigned int cs,bool enable)
- Line: 800

### aspeed_spi_chip_set_default_window
- Return type: static int
- Signature: aspeed_spi_chip_set_default_window(struct aspeed_spi * aspi)
- Line: 479

### aspeed_spi_chip_set_type
- Return type: static void
- Signature: aspeed_spi_chip_set_type(struct aspeed_spi * aspi,unsigned int cs,int type)
- Line: 790

### aspeed_spi_cleanup
- Return type: static void
- Signature: aspeed_spi_cleanup(struct spi_device * spi)
- Line: 835

### aspeed_spi_dirmap_create
- Return type: static int
- Signature: aspeed_spi_dirmap_create(struct spi_mem_dirmap_desc * desc)
- Line: 696

### aspeed_spi_dirmap_read
- Return type: static ssize_t
- Signature: aspeed_spi_dirmap_read(struct spi_mem_dirmap_desc * desc,u64 offset,size_t len,void * buf)
- Line: 762

### aspeed_spi_do_calibration
- Return type: static int
- Signature: aspeed_spi_do_calibration(struct aspeed_spi_chip * chip)
- Line: 1370

### aspeed_spi_enable
- Return type: static void
- Signature: aspeed_spi_enable(struct aspeed_spi * aspi,bool enable)
- Line: 845

### aspeed_spi_exec_mem_op
- Return type: static int
- Signature: aspeed_spi_exec_mem_op(struct spi_mem * mem,const struct spi_mem_op * op)
- Line: 376

### aspeed_spi_get_io_mode
- Return type: static u32
- Signature: aspeed_spi_get_io_mode(const struct spi_mem_op * op)
- Line: 116

### aspeed_spi_get_name
- Return type: static const char *
- Signature: aspeed_spi_get_name(struct spi_mem * mem)
- Line: 387

### aspeed_spi_probe
- Return type: static int
- Signature: aspeed_spi_probe(struct platform_device * pdev)
- Line: 957

### aspeed_spi_read_from_ahb
- Return type: static int
- Signature: aspeed_spi_read_from_ahb(void * buf,void __iomem * src,size_t len)
- Line: 163

### aspeed_spi_read_reg
- Return type: static int
- Signature: aspeed_spi_read_reg(struct aspeed_spi_chip * chip,const struct spi_mem_op * op)
- Line: 217

### aspeed_spi_read_user
- Return type: static ssize_t
- Signature: aspeed_spi_read_user(struct aspeed_spi_chip * chip,const struct spi_mem_op * op,u64 offset,size_t len,void * buf)
- Line: 239

### aspeed_spi_remove
- Return type: static void
- Signature: aspeed_spi_remove(struct platform_device * pdev)
- Line: 1031

### aspeed_spi_segment_ast2600_end
- Return type: static phys_addr_t
- Signature: aspeed_spi_segment_ast2600_end(struct aspeed_spi * aspi,u32 reg)
- Line: 1081

### aspeed_spi_segment_ast2600_reg
- Return type: static u32
- Signature: aspeed_spi_segment_ast2600_reg(struct aspeed_spi * aspi,phys_addr_t start,phys_addr_t end)
- Line: 1093

### aspeed_spi_segment_ast2600_start
- Return type: static phys_addr_t
- Signature: aspeed_spi_segment_ast2600_start(struct aspeed_spi * aspi,u32 reg)
- Line: 1073

### aspeed_spi_segment_ast2700_end
- Return type: static phys_addr_t
- Signature: aspeed_spi_segment_ast2700_end(struct aspeed_spi * aspi,u32 reg)
- Line: 1118

### aspeed_spi_segment_ast2700_reg
- Return type: static u32
- Signature: aspeed_spi_segment_ast2700_reg(struct aspeed_spi * aspi,phys_addr_t start,phys_addr_t end)
- Line: 1129

### aspeed_spi_segment_ast2700_start
- Return type: static phys_addr_t
- Signature: aspeed_spi_segment_ast2700_start(struct aspeed_spi * aspi,u32 reg)
- Line: 1107

### aspeed_spi_segment_end
- Return type: static phys_addr_t
- Signature: aspeed_spi_segment_end(struct aspeed_spi * aspi,u32 reg)
- Line: 1055

### aspeed_spi_segment_reg
- Return type: static u32
- Signature: aspeed_spi_segment_reg(struct aspeed_spi * aspi,phys_addr_t start,phys_addr_t end)
- Line: 1060

### aspeed_spi_segment_start
- Return type: static phys_addr_t
- Signature: aspeed_spi_segment_start(struct aspeed_spi * aspi,u32 reg)
- Line: 1050

### aspeed_spi_send_cmd_addr
- Return type: static int
- Signature: aspeed_spi_send_cmd_addr(struct aspeed_spi_chip * chip,u8 addr_nbytes,u64 offset,u32 opcode)
- Line: 191

### aspeed_spi_set_io_mode
- Return type: static void
- Signature: aspeed_spi_set_io_mode(struct aspeed_spi_chip * chip,u32 io_mode)
- Line: 130

### aspeed_spi_set_window
- Return type: static int
- Signature: aspeed_spi_set_window(struct aspeed_spi * aspi)
- Line: 396

### aspeed_spi_setup
- Return type: static int
- Signature: aspeed_spi_setup(struct spi_device * spi)
- Line: 812

### aspeed_spi_start_user
- Return type: static void
- Signature: aspeed_spi_start_user(struct aspeed_spi_chip * chip)
- Line: 141

### aspeed_spi_stop_user
- Return type: static void
- Signature: aspeed_spi_stop_user(struct aspeed_spi_chip * chip)
- Line: 152

### aspeed_spi_supports_mem_op
- Return type: static bool
- Signature: aspeed_spi_supports_mem_op(struct spi_mem * mem,const struct spi_mem_op * op)
- Line: 287

### aspeed_spi_trim_window_size
- Return type: static int
- Signature: aspeed_spi_trim_window_size(struct aspeed_spi * aspi)
- Line: 519

### aspeed_spi_user_prepare_msg
- Return type: static int
- Signature: aspeed_spi_user_prepare_msg(struct spi_controller * ctlr,struct spi_message * msg)
- Line: 853

### aspeed_spi_user_transfer
- Return type: static int
- Signature: aspeed_spi_user_transfer(struct spi_controller * ctlr,struct spi_device * spi,struct spi_transfer * xfer)
- Line: 915

### aspeed_spi_user_transfer_tx
- Return type: static void
- Signature: aspeed_spi_user_transfer_tx(struct aspeed_spi * aspi,struct spi_device * spi,const u8 * tx_buf,u8 * rx_buf,void * dst,u32 len)
- Line: 891

### aspeed_spi_user_unprepare_msg
- Return type: static int
- Signature: aspeed_spi_user_unprepare_msg(struct spi_controller * ctlr,struct spi_message * msg)
- Line: 876

### aspeed_spi_write_reg
- Return type: static int
- Signature: aspeed_spi_write_reg(struct aspeed_spi_chip * chip,const struct spi_mem_op * op)
- Line: 228

### aspeed_spi_write_to_ahb
- Return type: static int
- Signature: aspeed_spi_write_to_ahb(void __iomem * dst,const void * buf,size_t len)
- Line: 177

### aspeed_spi_write_user
- Return type: static ssize_t
- Signature: aspeed_spi_write_user(struct aspeed_spi_chip * chip,const struct spi_mem_op * op)
- Line: 267

### do_aspeed_spi_exec_mem_op
- Return type: static int
- Signature: do_aspeed_spi_exec_mem_op(struct spi_mem * mem,const struct spi_mem_op * op)
- Line: 313

## Structs (3)

### aspeed_spi
- Line: 100
- Members:
  - aspi: aspeed_spi *
  - cs: u32
  - ctl: void __iomem *
  - ahb_base: void __iomem *
  - ahb_window_size: u32
  - ctl_val: u32[]
  - clk_freq: u32
  - force_user_mode: bool
  - ctl0: u32
  - max_cs: u32
  - hastype: bool
  - mode_bits: u32
  - we0: u32
  - timing: u32
  - hclk_mask: u32
  - hdiv_max: u32
  - min_window_size: u32
  - full_duplex: bool
  - segment_start: phys_addr_t (*)(struct aspeed_spi * aspi,u32 reg)
  - segment_end: phys_addr_t (*)(struct aspeed_spi * aspi,u32 reg)
  - segment_reg: u32 (*)(struct aspeed_spi * aspi,phys_addr_t start,phys_addr_t end)
  - adjust_window: int (*)(struct aspeed_spi * aspi)
  - get_clk_div: u32 (*)(struct aspeed_spi_chip * chip,u32 hz)
  - calibrate: int (*)(struct aspeed_spi_chip * chip,u32 hdiv,const u8 * golden_buf,u8 * test_buf)
  - data: const struct aspeed_spi_data *
  - regs: void __iomem *
  - ahb_base_phy: phys_addr_t
  - ahb_window_size: u32
  - num_cs: u32
  - dev: device *
  - clk: clk *
  - clk_freq: u32
  - cs_change: u8
  - chips: aspeed_spi_chip[]

### aspeed_spi_chip
- Line: 65
- Members:
  - aspi: aspeed_spi *
  - cs: u32
  - ctl: void __iomem *
  - ahb_base: void __iomem *
  - ahb_window_size: u32
  - ctl_val: u32[]
  - clk_freq: u32
  - force_user_mode: bool
  - ctl0: u32
  - max_cs: u32
  - hastype: bool
  - mode_bits: u32
  - we0: u32
  - timing: u32
  - hclk_mask: u32
  - hdiv_max: u32
  - min_window_size: u32
  - full_duplex: bool
  - segment_start: phys_addr_t (*)(struct aspeed_spi * aspi,u32 reg)
  - segment_end: phys_addr_t (*)(struct aspeed_spi * aspi,u32 reg)
  - segment_reg: u32 (*)(struct aspeed_spi * aspi,phys_addr_t start,phys_addr_t end)
  - adjust_window: int (*)(struct aspeed_spi * aspi)
  - get_clk_div: u32 (*)(struct aspeed_spi_chip * chip,u32 hz)
  - calibrate: int (*)(struct aspeed_spi_chip * chip,u32 hdiv,const u8 * golden_buf,u8 * test_buf)
  - data: const struct aspeed_spi_data *
  - regs: void __iomem *
  - ahb_base_phy: phys_addr_t
  - ahb_window_size: u32
  - num_cs: u32
  - dev: device *
  - clk: clk *
  - clk_freq: u32
  - cs_change: u8
  - chips: aspeed_spi_chip[]

### aspeed_spi_data
- Line: 76
- Members:
  - aspi: aspeed_spi *
  - cs: u32
  - ctl: void __iomem *
  - ahb_base: void __iomem *
  - ahb_window_size: u32
  - ctl_val: u32[]
  - clk_freq: u32
  - force_user_mode: bool
  - ctl0: u32
  - max_cs: u32
  - hastype: bool
  - mode_bits: u32
  - we0: u32
  - timing: u32
  - hclk_mask: u32
  - hdiv_max: u32
  - min_window_size: u32
  - full_duplex: bool
  - segment_start: phys_addr_t (*)(struct aspeed_spi * aspi,u32 reg)
  - segment_end: phys_addr_t (*)(struct aspeed_spi * aspi,u32 reg)
  - segment_reg: u32 (*)(struct aspeed_spi * aspi,phys_addr_t start,phys_addr_t end)
  - adjust_window: int (*)(struct aspeed_spi * aspi)
  - get_clk_div: u32 (*)(struct aspeed_spi_chip * chip,u32 hz)
  - calibrate: int (*)(struct aspeed_spi_chip * chip,u32 hdiv,const u8 * golden_buf,u8 * test_buf)
  - data: const struct aspeed_spi_data *
  - regs: void __iomem *
  - ahb_base_phy: phys_addr_t
  - ahb_window_size: u32
  - num_cs: u32
  - dev: device *
  - clk: clk *
  - clk_freq: u32
  - cs_change: u8
  - chips: aspeed_spi_chip[]

## Enums (1)

### aspeed_spi_ctl_reg_value
- Line: 56

## Variables (16)

- static **aspeed_spi_driver** : platform_driver (line 1720)
- static **aspeed_spi_hclk_divs** : const u32[] (line 1239)
- static **aspeed_spi_matches** : const struct of_device_id[] (line 1707)
- static **aspeed_spi_mem_ops** : const struct spi_controller_mem_ops (line 782)
- static **ast2400_fmc_data** : const struct aspeed_spi_data (line 1565)
- static **ast2400_spi_data** : const struct aspeed_spi_data (line 1583)
- static **ast2400_spi_data** : const struct aspeed_spi_data (line 311)
- static **ast2500_fmc_data** : const struct aspeed_spi_data (line 1597)
- static **ast2500_spi_data** : const struct aspeed_spi_data (line 1615)
- static **ast2500_spi_data** : const struct aspeed_spi_data (line 475)
- static **ast2600_fmc_data** : const struct aspeed_spi_data (line 1633)
- static **ast2600_fmc_data** : const struct aspeed_spi_data (line 477)
- static **ast2600_spi_data** : const struct aspeed_spi_data (line 1652)
- static **ast2600_spi_data** : const struct aspeed_spi_data (line 476)
- static **ast2700_fmc_data** : const struct aspeed_spi_data (line 1671)
- static **ast2700_spi_data** : const struct aspeed_spi_data (line 1689)

## Macros (34)

- **ASPEED_SPI_HCLK_DIV**(i) (line 1247)
- **ASPEED_SPI_MAX_NUM_CS** (line 98)
- **AST2600_SEG_ADDR_MASK** (line 1071)
- **AST2700_SEG_ADDR_MASK** (line 1105)
- **CALIBRATE_BUF_SIZE** (line 1143)
- **CE0_CTRL_REG** (line 28)
- **CE0_SEGMENT_ADDR_REG** (line 49)
- **CE0_TIMING_COMPENSATION_REG** (line 54)
- **CE_CTRL_REG** (line 25)
- **CONFIG_REG** (line 21)
- **CONFIG_TYPE_SPI** (line 22)
- **CTRL_CE_STOP_ACTIVE** (line 39)
- **CTRL_COMMAND_SHIFT** (line 33)
- **CTRL_FREQ_SEL_MASK** (line 38)
- **CTRL_FREQ_SEL_SHIFT** (line 37)
- **CTRL_IO_ADDRESS_4B** (line 34)
- **CTRL_IO_CMD_MASK** (line 46)
- **CTRL_IO_DUAL_DATA** (line 31)
- **CTRL_IO_DUMMY_SET**(dummy) (line 35)
- **CTRL_IO_MODE_CMD_MASK** (line 40)
- **CTRL_IO_MODE_MASK** (line 29)
- **CTRL_IO_MODE_NORMAL** (line 41)
- **CTRL_IO_MODE_READ** (line 42)
- **CTRL_IO_MODE_USER** (line 44)
- **CTRL_IO_MODE_WRITE** (line 43)
- **CTRL_IO_QUAD_DATA** (line 32)
- **CTRL_IO_SINGLE_DATA** (line 30)
- **DEVICE_NAME** (line 18)
- **FREAD_TPASS**(i) (line 1163)
- **FULL_DUPLEX_RX_DATA** (line 51)
- **TIMING_DELAY_DI** (line 1457)
- **TIMING_DELAY_HCYCLE_MAX** (line 1458)
- **TIMING_DELAY_INPUT_MAX** (line 1459)
- **TIMING_REG_AST2600**(chip) (line 1460)
