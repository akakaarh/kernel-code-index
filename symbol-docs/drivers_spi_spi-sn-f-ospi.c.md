# drivers/spi/spi-sn-f-ospi.c

Subsystem: drivers/spi

## Functions (23)

### f_ospi_adjust_op_size
- Return type: static int
- Signature: f_ospi_adjust_op_size(struct spi_mem * mem,struct spi_mem_op * op)
- Line: 569

### f_ospi_clear_irq
- Return type: static void
- Signature: f_ospi_clear_irq(struct f_ospi * ospi)
- Line: 125

### f_ospi_config_clk
- Return type: static void
- Signature: f_ospi_config_clk(struct f_ospi * ospi,u32 device_hz)
- Line: 191

### f_ospi_config_dll
- Return type: static void
- Signature: f_ospi_config_dll(struct f_ospi * ospi)
- Line: 232

### f_ospi_config_indir_protocol
- Return type: static void
- Signature: f_ospi_config_indir_protocol(struct f_ospi * ospi,struct spi_mem * mem,const struct spi_mem_op * op)
- Line: 263

### f_ospi_disable_irq_output
- Return type: static void
- Signature: f_ospi_disable_irq_output(struct f_ospi * ospi,u32 irq_bits)
- Line: 149

### f_ospi_disable_irq_status
- Return type: static void
- Signature: f_ospi_disable_irq_status(struct f_ospi * ospi,u32 irq_bits)
- Line: 140

### f_ospi_enable_irq_status
- Return type: static void
- Signature: f_ospi_enable_irq_status(struct f_ospi * ospi,u32 irq_bits)
- Line: 131

### f_ospi_exec_op
- Return type: static int
- Signature: f_ospi_exec_op(struct spi_mem * mem,const struct spi_mem_op * op)
- Line: 504

### f_ospi_get_dummy_cycle
- Return type: static u32
- Signature: f_ospi_get_dummy_cycle(const struct spi_mem_op * op)
- Line: 117

### f_ospi_get_mode
- Return type: static u8
- Signature: f_ospi_get_mode(struct f_ospi * ospi,int width,int data_size)
- Line: 237

### f_ospi_indir_prepare_op
- Return type: static int
- Signature: f_ospi_indir_prepare_op(struct f_ospi * ospi,struct spi_mem * mem,const struct spi_mem_op * op)
- Line: 338

### f_ospi_indir_read
- Return type: static int
- Signature: f_ospi_indir_read(struct f_ospi * ospi,struct spi_mem * mem,const struct spi_mem_op * op)
- Line: 403

### f_ospi_indir_start_xfer
- Return type: static void
- Signature: f_ospi_indir_start_xfer(struct f_ospi * ospi)
- Line: 382

### f_ospi_indir_stop_xfer
- Return type: static void
- Signature: f_ospi_indir_stop_xfer(struct f_ospi * ospi)
- Line: 388

### f_ospi_indir_wait_xfer_complete
- Return type: static int
- Signature: f_ospi_indir_wait_xfer_complete(struct f_ospi * ospi)
- Line: 394

### f_ospi_indir_write
- Return type: static int
- Signature: f_ospi_indir_write(struct f_ospi * ospi,struct spi_mem * mem,const struct spi_mem_op * op)
- Line: 457

### f_ospi_init
- Return type: static int
- Signature: f_ospi_init(struct f_ospi * ospi)
- Line: 586

### f_ospi_prepare_config
- Return type: static int
- Signature: f_ospi_prepare_config(struct f_ospi * ospi)
- Line: 158

### f_ospi_probe
- Return type: static int
- Signature: f_ospi_probe(struct platform_device * pdev)
- Line: 607

### f_ospi_supports_op
- Return type: static bool
- Signature: f_ospi_supports_op(struct spi_mem * mem,const struct spi_mem_op * op)
- Line: 554

### f_ospi_supports_op_width
- Return type: static bool
- Signature: f_ospi_supports_op_width(struct spi_mem * mem,const struct spi_mem_op * op)
- Line: 528

### f_ospi_unprepare_config
- Return type: static int
- Signature: f_ospi_unprepare_config(struct f_ospi * ospi)
- Line: 176

## Structs (1)

### f_ospi
- Line: 110
- Members:
  - base: void __iomem *
  - dev: device *
  - clk: clk *
  - mlock: mutex

## Variables (4)

- static **f_ospi_driver** : platform_driver (line 662)
- static **f_ospi_dt_ids** : const struct of_device_id[] (line 656)
- static **f_ospi_mem_caps** : const struct spi_controller_mem_caps (line 582)
- static **f_ospi_mem_ops** : const struct spi_controller_mem_ops (line 576)

## Macros (77)

- **OSPI_ACC_MODE** (line 80)
- **OSPI_ACC_MODE_BOOT_DISABLE** (line 81)
- **OSPI_ADDR** (line 65)
- **OSPI_ALT_INDIR** (line 66)
- **OSPI_CLK_CTL** (line 49)
- **OSPI_CLK_CTL_BOOT_INT_CLK_EN** (line 50)
- **OSPI_CLK_CTL_DIV** (line 54)
- **OSPI_CLK_CTL_DIV_1** (line 55)
- **OSPI_CLK_CTL_DIV_2** (line 56)
- **OSPI_CLK_CTL_DIV_4** (line 57)
- **OSPI_CLK_CTL_DIV_8** (line 58)
- **OSPI_CLK_CTL_INT_CLK_EN** (line 59)
- **OSPI_CLK_CTL_PHA** (line 51)
- **OSPI_CLK_CTL_PHA_180** (line 52)
- **OSPI_CLK_CTL_PHA_90** (line 53)
- **OSPI_CMD_IDX_INDIR** (line 64)
- **OSPI_CS_CTL1** (line 61)
- **OSPI_CS_CTL2** (line 62)
- **OSPI_DAT** (line 68)
- **OSPI_DAT_SIZE_EN** (line 72)
- **OSPI_DAT_SIZE_INDIR** (line 71)
- **OSPI_DAT_SIZE_MASK** (line 73)
- **OSPI_DAT_SIZE_MAX** (line 74)
- **OSPI_DAT_SWP_INDIR** (line 69)
- **OSPI_DMY_INDIR** (line 67)
- **OSPI_DUMMY_CYCLE_MAX** (line 107)
- **OSPI_IRQ** (line 93)
- **OSPI_IRQ_ALL** (line 98)
- **OSPI_IRQ_CS_DEASSERT** (line 94)
- **OSPI_IRQ_CS_TRANS_COMP** (line 97)
- **OSPI_IRQ_READ_BUF_READY** (line 96)
- **OSPI_IRQ_SIG_EN** (line 103)
- **OSPI_IRQ_STAT_EN** (line 102)
- **OSPI_IRQ_WRITE_BUF_READY** (line 95)
- **OSPI_NUM_CS** (line 106)
- **OSPI_PROT_ADDR_SIZE_MASK** (line 46)
- **OSPI_PROT_ALT_SIZE_MASK** (line 45)
- **OSPI_PROT_BIT_POS_ADDR** (line 36)
- **OSPI_PROT_BIT_POS_ALT** (line 35)
- **OSPI_PROT_BIT_POS_CODE** (line 37)
- **OSPI_PROT_BIT_POS_DATA** (line 34)
- **OSPI_PROT_CODE_SIZE_MASK** (line 47)
- **OSPI_PROT_CTL_INDIR** (line 19)
- **OSPI_PROT_DATA_EN** (line 44)
- **OSPI_PROT_DATA_RATE_ADDR** (line 30)
- **OSPI_PROT_DATA_RATE_ALT** (line 29)
- **OSPI_PROT_DATA_RATE_CODE** (line 31)
- **OSPI_PROT_DATA_RATE_DATA** (line 28)
- **OSPI_PROT_DATA_UNIT_1B** (line 40)
- **OSPI_PROT_DATA_UNIT_2B** (line 41)
- **OSPI_PROT_DATA_UNIT_4B** (line 42)
- **OSPI_PROT_DATA_UNIT_MASK** (line 39)
- **OSPI_PROT_DDR** (line 33)
- **OSPI_PROT_MODE_ADDR_MASK** (line 22)
- **OSPI_PROT_MODE_ALT_MASK** (line 21)
- **OSPI_PROT_MODE_CODE_MASK** (line 23)
- **OSPI_PROT_MODE_DATA_MASK** (line 20)
- **OSPI_PROT_MODE_DUAL** (line 25)
- **OSPI_PROT_MODE_OCTAL** (line 27)
- **OSPI_PROT_MODE_QUAD** (line 26)
- **OSPI_PROT_MODE_SINGLE** (line 24)
- **OSPI_PROT_SAMP_EDGE** (line 38)
- **OSPI_PROT_SDR** (line 32)
- **OSPI_PROT_TRANS_DIR_WRITE** (line 43)
- **OSPI_SSEL** (line 63)
- **OSPI_STAT** (line 87)
- **OSPI_STAT_IS_AXI_READING** (line 89)
- **OSPI_STAT_IS_AXI_WRITING** (line 88)
- **OSPI_STAT_IS_SPI_IDLE** (line 91)
- **OSPI_STAT_IS_SPI_INT_CLK_STOP** (line 90)
- **OSPI_SWRST** (line 83)
- **OSPI_SWRST_INDIR_READ_FIFO** (line 85)
- **OSPI_SWRST_INDIR_WRITE_FIFO** (line 84)
- **OSPI_TRANS_CTL** (line 76)
- **OSPI_TRANS_CTL_START_REQ** (line 78)
- **OSPI_TRANS_CTL_STOP_REQ** (line 77)
- **OSPI_WAIT_MAX_MSEC** (line 108)
