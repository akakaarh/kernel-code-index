# drivers/spi/spi-cadence-quadspi.c

Subsystem: drivers/spi

## Functions (46)

### calculate_ticks_for_ns
- Return type: static unsigned int
- Signature: calculate_ticks_for_ns(const unsigned int ref_clk_hz,const unsigned int ns_val)
- Line: 1207

### cqspi_calc_dummy
- Return type: static unsigned int
- Signature: cqspi_calc_dummy(const struct spi_mem_op * op)
- Line: 409

### cqspi_calc_rdreg
- Return type: static unsigned int
- Signature: cqspi_calc_rdreg(const struct spi_mem_op * op)
- Line: 398

### cqspi_chipselect
- Return type: static void
- Signature: cqspi_chipselect(struct cqspi_flash_pdata * f_pdata)
- Line: 1178

### cqspi_command_read
- Return type: static int
- Signature: cqspi_command_read(struct cqspi_flash_pdata * f_pdata,const struct spi_mem_op * op)
- Line: 538

### cqspi_command_write
- Return type: static int
- Signature: cqspi_command_write(struct cqspi_flash_pdata * f_pdata,const struct spi_mem_op * op)
- Line: 621

### cqspi_config_baudrate_div
- Return type: static void
- Signature: cqspi_config_baudrate_div(struct cqspi_st * cqspi)
- Line: 1250

### cqspi_configure
- Return type: static void
- Signature: cqspi_configure(struct cqspi_flash_pdata * f_pdata,unsigned long sclk)
- Line: 1296

### cqspi_controller_detect_fifo_depth
- Return type: static void
- Signature: cqspi_controller_detect_fifo_depth(struct cqspi_st * cqspi)
- Line: 1674

### cqspi_controller_enable
- Return type: static void
- Signature: cqspi_controller_enable(struct cqspi_st * cqspi,bool enable)
- Line: 869

### cqspi_controller_init
- Return type: static void
- Signature: cqspi_controller_init(struct cqspi_st * cqspi)
- Line: 1630

### cqspi_delay
- Return type: static void
- Signature: cqspi_delay(struct cqspi_flash_pdata * f_pdata)
- Line: 1218

### cqspi_device_reset
- Return type: static void
- Signature: cqspi_device_reset(struct cqspi_st * cqspi)
- Line: 850

### cqspi_direct_read_execute
- Return type: static int
- Signature: cqspi_direct_read_execute(struct cqspi_flash_pdata * f_pdata,u_char * buf,loff_t from,size_t len)
- Line: 1363

### cqspi_enable_dtr
- Return type: static int
- Signature: cqspi_enable_dtr(struct cqspi_flash_pdata * f_pdata,const struct spi_mem_op * op,unsigned int shift)
- Line: 503

### cqspi_exec_flash_cmd
- Return type: static int
- Signature: cqspi_exec_flash_cmd(struct cqspi_st * cqspi,unsigned int reg)
- Line: 456

### cqspi_exec_mem_op
- Return type: static int
- Signature: cqspi_exec_mem_op(struct spi_mem * mem,const struct spi_mem_op * op)
- Line: 1476

### cqspi_get_name
- Return type: static const char *
- Signature: cqspi_get_name(struct spi_mem * mem)
- Line: 1725

### cqspi_get_rd_sram_level
- Return type: static u32
- Signature: cqspi_get_rd_sram_level(struct cqspi_st * cqspi)
- Line: 353

### cqspi_get_versal_dma_status
- Return type: static u32
- Signature: cqspi_get_versal_dma_status(struct cqspi_st * cqspi)
- Line: 361

### cqspi_indirect_read_execute
- Return type: static int
- Signature: cqspi_indirect_read_execute(struct cqspi_flash_pdata * f_pdata,u8 * rxbuf,loff_t from_addr,const size_t n_rx)
- Line: 733

### cqspi_indirect_write_execute
- Return type: static int
- Signature: cqspi_indirect_write_execute(struct cqspi_flash_pdata * f_pdata,loff_t to_addr,const u8 * txbuf,const size_t n_tx)
- Line: 1074

### cqspi_irq_handler
- Return type: static irqreturn_t
- Signature: cqspi_irq_handler(int this_irq,void * dev)
- Line: 373

### cqspi_is_idle
- Return type: static bool
- Signature: cqspi_is_idle(struct cqspi_st * cqspi)
- Line: 346

### cqspi_mem_process
- Return type: static int
- Signature: cqspi_mem_process(struct spi_mem * mem,const struct spi_mem_op * op)
- Line: 1448

### cqspi_of_get_flash_pdata
- Return type: static int
- Signature: cqspi_of_get_flash_pdata(struct platform_device * pdev,struct cqspi_flash_pdata * f_pdata,struct device_node * np)
- Line: 1557

### cqspi_of_get_pdata
- Return type: static int
- Signature: cqspi_of_get_pdata(struct cqspi_st * cqspi)
- Line: 1594

### cqspi_probe
- Return type: static int
- Signature: cqspi_probe(struct platform_device * pdev)
- Line: 1785

### cqspi_read
- Return type: static ssize_t
- Signature: cqspi_read(struct cqspi_flash_pdata * f_pdata,const struct spi_mem_op * op)
- Line: 1422

### cqspi_read_setup
- Return type: static int
- Signature: cqspi_read_setup(struct cqspi_flash_pdata * f_pdata,const struct spi_mem_op * op)
- Line: 690

### cqspi_readdata_capture
- Return type: static void
- Signature: cqspi_readdata_capture(struct cqspi_st * cqspi,const bool bypass,const unsigned int delay)
- Line: 1273

### cqspi_remove
- Return type: static void
- Signature: cqspi_remove(struct platform_device * pdev)
- Line: 2009

### cqspi_request_mmap_dma
- Return type: static int
- Signature: cqspi_request_mmap_dma(struct cqspi_st * cqspi)
- Line: 1700

### cqspi_resume
- Return type: static int
- Signature: cqspi_resume(struct device * dev)
- Line: 2084

### cqspi_runtime_resume
- Return type: static int
- Signature: cqspi_runtime_resume(struct device * dev)
- Line: 2053

### cqspi_runtime_suspend
- Return type: static int
- Signature: cqspi_runtime_suspend(struct device * dev)
- Line: 2044

### cqspi_rx_dma_callback
- Return type: static void
- Signature: cqspi_rx_dma_callback(void * param)
- Line: 1356

### cqspi_setup_flash
- Return type: static int
- Signature: cqspi_setup_flash(struct cqspi_st * cqspi)
- Line: 1745

### cqspi_setup_opcode_ext
- Return type: static int
- Signature: cqspi_setup_opcode_ext(struct cqspi_flash_pdata * f_pdata,const struct spi_mem_op * op,unsigned int shift)
- Line: 480

### cqspi_supports_mem_op
- Return type: static bool
- Signature: cqspi_supports_mem_op(struct spi_mem * mem,const struct spi_mem_op * op)
- Line: 1520

### cqspi_suspend
- Return type: static int
- Signature: cqspi_suspend(struct device * dev)
- Line: 2072

### cqspi_versal_indirect_read_dma
- Return type: static int
- Signature: cqspi_versal_indirect_read_dma(struct cqspi_flash_pdata * f_pdata,u_char * rxbuf,loff_t from_addr,size_t n_rx)
- Line: 884

### cqspi_wait_for_bit
- Return type: static int
- Signature: cqspi_wait_for_bit(const struct cqspi_driver_platdata * ddata,void __iomem * reg,const u32 mask,bool clr,bool busywait)
- Line: 323

### cqspi_wait_idle
- Return type: static int
- Signature: cqspi_wait_idle(struct cqspi_st * cqspi)
- Line: 423

### cqspi_write
- Return type: static ssize_t
- Signature: cqspi_write(struct cqspi_flash_pdata * f_pdata,const struct spi_mem_op * op)
- Line: 1325

### cqspi_write_setup
- Return type: static int
- Signature: cqspi_write_setup(struct cqspi_flash_pdata * f_pdata,const struct spi_mem_op * op)
- Line: 1017

## Structs (3)

### cqspi_driver_platdata
- Line: 126
- Members:
  - cqspi: cqspi_st *
  - clk_rate: u32
  - read_delay: u32
  - tshsl_ns: u32
  - tsd2d_ns: u32
  - tchsh_ns: u32
  - tslch_ns: u32
  - cs: u8
  - pdev: platform_device *
  - host: spi_controller *
  - clks: clk_bulk_data[]
  - sclk: unsigned int
  - iobase: void __iomem *
  - ahb_base: void __iomem *
  - ahb_size: resource_size_t
  - transfer_complete: completion
  - rx_chan: dma_chan *
  - rx_dma_complete: completion
  - mmap_phys_base: dma_addr_t
  - current_cs: int
  - master_ref_clk_hz: unsigned long
  - is_decoded_cs: bool
  - fifo_depth: u32
  - fifo_width: u32
  - num_chipselect: u32
  - rclk_en: bool
  - trigger_address: u32
  - wr_delay: u32
  - use_direct_mode: bool
  - use_direct_mode_wr: bool
  - f_pdata: cqspi_flash_pdata[]
  - use_dma_read: bool
  - pd_dev_id: u32
  - wr_completion: bool
  - slow_sram: bool
  - apb_ahb_hazard: bool
  - is_jh7110: bool
  - is_rzn1: bool
  - disable_stig_mode: bool
  - refcount: refcount_t
  - inflight_ops: refcount_t
  - ddata: const struct cqspi_driver_platdata *
  - hwcaps_mask: u32
  - quirks: u16
  - indirect_read_dma: int (*)(struct cqspi_flash_pdata * f_pdata,u_char * rxbuf,loff_t from_addr,size_t n_rx)
  - get_dma_status: u32 (*)(struct cqspi_st * cqspi)

### cqspi_flash_pdata
- Line: 68
- Members:
  - cqspi: cqspi_st *
  - clk_rate: u32
  - read_delay: u32
  - tshsl_ns: u32
  - tsd2d_ns: u32
  - tchsh_ns: u32
  - tslch_ns: u32
  - cs: u8
  - pdev: platform_device *
  - host: spi_controller *
  - clks: clk_bulk_data[]
  - sclk: unsigned int
  - iobase: void __iomem *
  - ahb_base: void __iomem *
  - ahb_size: resource_size_t
  - transfer_complete: completion
  - rx_chan: dma_chan *
  - rx_dma_complete: completion
  - mmap_phys_base: dma_addr_t
  - current_cs: int
  - master_ref_clk_hz: unsigned long
  - is_decoded_cs: bool
  - fifo_depth: u32
  - fifo_width: u32
  - num_chipselect: u32
  - rclk_en: bool
  - trigger_address: u32
  - wr_delay: u32
  - use_direct_mode: bool
  - use_direct_mode_wr: bool
  - f_pdata: cqspi_flash_pdata[]
  - use_dma_read: bool
  - pd_dev_id: u32
  - wr_completion: bool
  - slow_sram: bool
  - apb_ahb_hazard: bool
  - is_jh7110: bool
  - is_rzn1: bool
  - disable_stig_mode: bool
  - refcount: refcount_t
  - inflight_ops: refcount_t
  - ddata: const struct cqspi_driver_platdata *
  - hwcaps_mask: u32
  - quirks: u16
  - indirect_read_dma: int (*)(struct cqspi_flash_pdata * f_pdata,u_char * rxbuf,loff_t from_addr,size_t n_rx)
  - get_dma_status: u32 (*)(struct cqspi_st * cqspi)

### cqspi_st
- Line: 84
- Members:
  - cqspi: cqspi_st *
  - clk_rate: u32
  - read_delay: u32
  - tshsl_ns: u32
  - tsd2d_ns: u32
  - tchsh_ns: u32
  - tslch_ns: u32
  - cs: u8
  - pdev: platform_device *
  - host: spi_controller *
  - clks: clk_bulk_data[]
  - sclk: unsigned int
  - iobase: void __iomem *
  - ahb_base: void __iomem *
  - ahb_size: resource_size_t
  - transfer_complete: completion
  - rx_chan: dma_chan *
  - rx_dma_complete: completion
  - mmap_phys_base: dma_addr_t
  - current_cs: int
  - master_ref_clk_hz: unsigned long
  - is_decoded_cs: bool
  - fifo_depth: u32
  - fifo_width: u32
  - num_chipselect: u32
  - rclk_en: bool
  - trigger_address: u32
  - wr_delay: u32
  - use_direct_mode: bool
  - use_direct_mode_wr: bool
  - f_pdata: cqspi_flash_pdata[]
  - use_dma_read: bool
  - pd_dev_id: u32
  - wr_completion: bool
  - slow_sram: bool
  - apb_ahb_hazard: bool
  - is_jh7110: bool
  - is_rzn1: bool
  - disable_stig_mode: bool
  - refcount: refcount_t
  - inflight_ops: refcount_t
  - ddata: const struct cqspi_driver_platdata *
  - hwcaps_mask: u32
  - quirks: u16
  - indirect_read_dma: int (*)(struct cqspi_flash_pdata * f_pdata,u_char * rxbuf,loff_t from_addr,size_t n_rx)
  - get_dma_status: u32 (*)(struct cqspi_st * cqspi)

## Enums (1)

### __anonf2aa3e890103
- Line: 59

## Variables (17)

- static **am654_ospi** : const struct cqspi_driver_platdata (line 2111)
- static **cdns_qspi** : const struct cqspi_driver_platdata (line 2103)
- static **cqspi_clks** : const struct clk_bulk_data[] (line 79)
- static **cqspi_dev_pm_ops** : const struct dev_pm_ops (line 2098)
- static **cqspi_dt_ids** : const struct of_device_id[] (line 2162)
- static **cqspi_mem_caps** : const struct spi_controller_mem_caps (line 1740)
- static **cqspi_mem_ops** : const struct spi_controller_mem_ops (line 1734)
- static **cqspi_platform_driver** : platform_driver (line 2212)
- static **intel_lgm_qspi** : const struct cqspi_driver_platdata (line 2116)
- static **jh7110_qspi** : const struct cqspi_driver_platdata (line 2142)
- static **k2g_qspi** : const struct cqspi_driver_platdata (line 2107)
- static **mobileye_eyeq5_ospi** : const struct cqspi_driver_platdata (line 2150)
- static **pensando_cdns_qspi** : const struct cqspi_driver_platdata (line 2146)
- static **renesas_rzn1_qspi** : const struct cqspi_driver_platdata (line 2156)
- static **socfpga_qspi** : const struct cqspi_driver_platdata (line 2120)
- static **versal2_ospi** : const struct cqspi_driver_platdata (line 2134)
- static **versal_ospi** : const struct cqspi_driver_platdata (line 2126)

## Macros (160)

- **CQSPI_AUTOSUSPEND_TIMEOUT** (line 140)
- **CQSPI_BUSYWAIT_TIMEOUT_US** (line 137)
- **CQSPI_DISABLE_DAC_MODE** (line 40)
- **CQSPI_DISABLE_RUNTIME_PM** (line 49)
- **CQSPI_DISABLE_STIG_MODE** (line 48)
- **CQSPI_DMA_SET_MASK** (line 46)
- **CQSPI_DMA_UNALIGN** (line 319)
- **CQSPI_DUMMY_BYTES_MAX** (line 143)
- **CQSPI_DUMMY_CLKS_MAX** (line 144)
- **CQSPI_DUMMY_CLKS_PER_BYTE** (line 142)
- **CQSPI_HAS_WR_PROTECT** (line 51)
- **CQSPI_IRQ_MASK_RD** (line 307)
- **CQSPI_IRQ_MASK_RD_SLOW_SRAM** (line 311)
- **CQSPI_IRQ_MASK_WR** (line 314)
- **CQSPI_IRQ_STATUS_MASK** (line 318)
- **CQSPI_MAX_CHIPSELECT** (line 34)
- **CQSPI_NAME** (line 33)
- **CQSPI_NEEDS_APB_AHB_HAZARD_WAR** (line 44)
- **CQSPI_NEEDS_WR_DELAY** (line 39)
- **CQSPI_NO_INDIRECT_MODE** (line 50)
- **CQSPI_NO_SUPPORT_WR_COMPLETION** (line 42)
- **CQSPI_OP_WIDTH**(part) (line 57)
- **CQSPI_RD_NO_IRQ** (line 45)
- **CQSPI_READ_TIMEOUT_MS** (line 136)
- **CQSPI_REG_CMDADDRESS** (line 266)
- **CQSPI_REG_CMDCTRL** (line 239)
- **CQSPI_REG_CMDCTRL_ADDR_EN_LSB** (line 246)
- **CQSPI_REG_CMDCTRL_ADD_BYTES_LSB** (line 245)
- **CQSPI_REG_CMDCTRL_ADD_BYTES_MASK** (line 251)
- **CQSPI_REG_CMDCTRL_DUMMY_LSB** (line 242)
- **CQSPI_REG_CMDCTRL_DUMMY_MASK** (line 253)
- **CQSPI_REG_CMDCTRL_EXECUTE_MASK** (line 240)
- **CQSPI_REG_CMDCTRL_INPROGRESS_MASK** (line 241)
- **CQSPI_REG_CMDCTRL_OPCODE_LSB** (line 249)
- **CQSPI_REG_CMDCTRL_RD_BYTES_LSB** (line 247)
- **CQSPI_REG_CMDCTRL_RD_BYTES_MASK** (line 252)
- **CQSPI_REG_CMDCTRL_RD_EN_LSB** (line 248)
- **CQSPI_REG_CMDCTRL_WR_BYTES_LSB** (line 243)
- **CQSPI_REG_CMDCTRL_WR_BYTES_MASK** (line 250)
- **CQSPI_REG_CMDCTRL_WR_EN_LSB** (line 244)
- **CQSPI_REG_CMDREADDATALOWER** (line 267)
- **CQSPI_REG_CMDREADDATAUPPER** (line 268)
- **CQSPI_REG_CMDWRITEDATALOWER** (line 269)
- **CQSPI_REG_CMDWRITEDATAUPPER** (line 270)
- **CQSPI_REG_CONFIG** (line 149)
- **CQSPI_REG_CONFIG_BAUD_LSB** (line 155)
- **CQSPI_REG_CONFIG_BAUD_MASK** (line 160)
- **CQSPI_REG_CONFIG_CHIPSELECT_LSB** (line 153)
- **CQSPI_REG_CONFIG_CHIPSELECT_MASK** (line 159)
- **CQSPI_REG_CONFIG_DECODE_MASK** (line 152)
- **CQSPI_REG_CONFIG_DMA_MASK** (line 154)
- **CQSPI_REG_CONFIG_DTR_PROTO** (line 156)
- **CQSPI_REG_CONFIG_DUAL_OPCODE** (line 157)
- **CQSPI_REG_CONFIG_ENABLE_MASK** (line 150)
- **CQSPI_REG_CONFIG_ENB_DIR_ACC_CTRL** (line 151)
- **CQSPI_REG_CONFIG_IDLE_LSB** (line 158)
- **CQSPI_REG_CONFIG_RESET_CFG_FLD_MASK** (line 162)
- **CQSPI_REG_CONFIG_RESET_PIN_FLD_MASK** (line 161)
- **CQSPI_REG_DELAY** (line 181)
- **CQSPI_REG_DELAY_TCHSH_LSB** (line 183)
- **CQSPI_REG_DELAY_TCHSH_MASK** (line 187)
- **CQSPI_REG_DELAY_TSD2D_LSB** (line 184)
- **CQSPI_REG_DELAY_TSD2D_MASK** (line 188)
- **CQSPI_REG_DELAY_TSHSL_LSB** (line 185)
- **CQSPI_REG_DELAY_TSHSL_MASK** (line 189)
- **CQSPI_REG_DELAY_TSLCH_LSB** (line 182)
- **CQSPI_REG_DELAY_TSLCH_MASK** (line 186)
- **CQSPI_REG_DMA** (line 207)
- **CQSPI_REG_DMA_BURST_LSB** (line 209)
- **CQSPI_REG_DMA_BURST_MASK** (line 211)
- **CQSPI_REG_DMA_SINGLE_LSB** (line 208)
- **CQSPI_REG_DMA_SINGLE_MASK** (line 210)
- **CQSPI_REG_INDIRECTRD** (line 230)
- **CQSPI_REG_INDIRECTRDBYTES** (line 237)
- **CQSPI_REG_INDIRECTRDSTARTADDR** (line 236)
- **CQSPI_REG_INDIRECTRDWATERMARK** (line 235)
- **CQSPI_REG_INDIRECTRD_CANCEL_MASK** (line 232)
- **CQSPI_REG_INDIRECTRD_DONE_MASK** (line 233)
- **CQSPI_REG_INDIRECTRD_START_MASK** (line 231)
- **CQSPI_REG_INDIRECTTRIGGER** (line 205)
- **CQSPI_REG_INDIRECTWR** (line 255)
- **CQSPI_REG_INDIRECTWRBYTES** (line 262)
- **CQSPI_REG_INDIRECTWRSTARTADDR** (line 261)
- **CQSPI_REG_INDIRECTWRWATERMARK** (line 260)
- **CQSPI_REG_INDIRECTWR_CANCEL_MASK** (line 257)
- **CQSPI_REG_INDIRECTWR_DONE_MASK** (line 258)
- **CQSPI_REG_INDIRECTWR_START_MASK** (line 256)
- **CQSPI_REG_INDTRIG_ADDRRANGE** (line 264)
- **CQSPI_REG_IRQMASK** (line 226)
- **CQSPI_REG_IRQSTATUS** (line 225)
- **CQSPI_REG_IRQ_ILLEGAL_AHB_ERR** (line 303)
- **CQSPI_REG_IRQ_IND_COMP** (line 300)
- **CQSPI_REG_IRQ_IND_RD_REJECT** (line 301)
- **CQSPI_REG_IRQ_IND_SRAM_FULL** (line 305)
- **CQSPI_REG_IRQ_MODE_ERR** (line 298)
- **CQSPI_REG_IRQ_UNDERFLOW** (line 299)
- **CQSPI_REG_IRQ_WATERMARK** (line 304)
- **CQSPI_REG_IRQ_WR_PROTECTED_ERR** (line 302)
- **CQSPI_REG_MODE_BIT** (line 214)
- **CQSPI_REG_OP_EXT_LOWER** (line 275)
- **CQSPI_REG_OP_EXT_READ_LSB** (line 276)
- **CQSPI_REG_OP_EXT_STIG_LSB** (line 278)
- **CQSPI_REG_OP_EXT_WRITE_LSB** (line 277)
- **CQSPI_REG_POLLING_STATUS** (line 272)
- **CQSPI_REG_POLLING_STATUS_DUMMY_LSB** (line 273)
- **CQSPI_REG_RD_INSTR** (line 164)
- **CQSPI_REG_RD_INSTR_DUMMY_LSB** (line 170)
- **CQSPI_REG_RD_INSTR_DUMMY_MASK** (line 174)
- **CQSPI_REG_RD_INSTR_MODE_EN_LSB** (line 169)
- **CQSPI_REG_RD_INSTR_OPCODE_LSB** (line 165)
- **CQSPI_REG_RD_INSTR_TYPE_ADDR_LSB** (line 167)
- **CQSPI_REG_RD_INSTR_TYPE_ADDR_MASK** (line 172)
- **CQSPI_REG_RD_INSTR_TYPE_DATA_LSB** (line 168)
- **CQSPI_REG_RD_INSTR_TYPE_DATA_MASK** (line 173)
- **CQSPI_REG_RD_INSTR_TYPE_INSTR_LSB** (line 166)
- **CQSPI_REG_RD_INSTR_TYPE_INSTR_MASK** (line 171)
- **CQSPI_REG_READCAPTURE** (line 191)
- **CQSPI_REG_READCAPTURE_BYPASS_LSB** (line 192)
- **CQSPI_REG_READCAPTURE_DELAY_LSB** (line 193)
- **CQSPI_REG_READCAPTURE_DELAY_MASK** (line 194)
- **CQSPI_REG_REMAP** (line 213)
- **CQSPI_REG_SDRAMLEVEL** (line 216)
- **CQSPI_REG_SDRAMLEVEL_RD_LSB** (line 217)
- **CQSPI_REG_SDRAMLEVEL_RD_MASK** (line 219)
- **CQSPI_REG_SDRAMLEVEL_WR_LSB** (line 218)
- **CQSPI_REG_SDRAMLEVEL_WR_MASK** (line 220)
- **CQSPI_REG_SIZE** (line 196)
- **CQSPI_REG_SIZE_ADDRESS_LSB** (line 197)
- **CQSPI_REG_SIZE_ADDRESS_MASK** (line 200)
- **CQSPI_REG_SIZE_BLOCK_LSB** (line 199)
- **CQSPI_REG_SIZE_BLOCK_MASK** (line 202)
- **CQSPI_REG_SIZE_PAGE_LSB** (line 198)
- **CQSPI_REG_SIZE_PAGE_MASK** (line 201)
- **CQSPI_REG_SRAMPARTITION** (line 204)
- **CQSPI_REG_VERSAL_ADDRRANGE_WIDTH_VAL** (line 295)
- **CQSPI_REG_VERSAL_DMA_DST_ADDR** (line 282)
- **CQSPI_REG_VERSAL_DMA_DST_ADDR_MSB** (line 292)
- **CQSPI_REG_VERSAL_DMA_DST_CTRL** (line 285)
- **CQSPI_REG_VERSAL_DMA_DST_CTRL_VAL** (line 294)
- **CQSPI_REG_VERSAL_DMA_DST_DONE_MASK** (line 290)
- **CQSPI_REG_VERSAL_DMA_DST_I_DIS** (line 289)
- **CQSPI_REG_VERSAL_DMA_DST_I_EN** (line 288)
- **CQSPI_REG_VERSAL_DMA_DST_I_STS** (line 287)
- **CQSPI_REG_VERSAL_DMA_DST_SIZE** (line 283)
- **CQSPI_REG_VERSAL_DMA_SRC_ADDR** (line 280)
- **CQSPI_REG_VERSAL_DMA_VAL** (line 321)
- **CQSPI_REG_WR_COMPLETION_CTRL** (line 222)
- **CQSPI_REG_WR_DISABLE_AUTO_POLL** (line 223)
- **CQSPI_REG_WR_INSTR** (line 176)
- **CQSPI_REG_WR_INSTR_OPCODE_LSB** (line 177)
- **CQSPI_REG_WR_INSTR_TYPE_ADDR_LSB** (line 178)
- **CQSPI_REG_WR_INSTR_TYPE_DATA_LSB** (line 179)
- **CQSPI_REG_WR_PROT_CTRL** (line 228)
- **CQSPI_SLOW_SRAM** (line 43)
- **CQSPI_STIG_DATA_LEN_MAX** (line 146)
- **CQSPI_SUPPORTS_OCTAL** (line 54)
- **CQSPI_SUPPORTS_QUAD** (line 55)
- **CQSPI_SUPPORT_DEVICE_RESET** (line 47)
- **CQSPI_SUPPORT_EXTERNAL_DMA** (line 41)
- **CQSPI_TIMEOUT_MS** (line 135)
