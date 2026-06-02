# drivers/spi/spi-ti-qspi.c

Subsystem: drivers/spi

## Functions (24)

### qspi_is_busy
- Return type: static u32
- Signature: qspi_is_busy(struct ti_qspi * qspi)
- Line: 207

### qspi_read_msg
- Return type: static int
- Signature: qspi_read_msg(struct ti_qspi * qspi,struct spi_transfer * t,int count)
- Line: 309

### qspi_transfer_msg
- Return type: static int
- Signature: qspi_transfer_msg(struct ti_qspi * qspi,struct spi_transfer * t,int count)
- Line: 408

### qspi_write_msg
- Return type: static int
- Signature: qspi_write_msg(struct ti_qspi * qspi,struct spi_transfer * t,int count)
- Line: 240

### ti_qspi_adjust_op_size
- Return type: static int
- Signature: ti_qspi_adjust_op_size(struct spi_mem * mem,struct spi_mem_op * op)
- Line: 575

### ti_qspi_disable_memory_map
- Return type: static void
- Signature: ti_qspi_disable_memory_map(struct spi_device * spi)
- Line: 539

### ti_qspi_dma_bounce_buffer
- Return type: static int
- Signature: ti_qspi_dma_bounce_buffer(struct ti_qspi * qspi,loff_t offs,void * to,size_t readsize)
- Line: 478

### ti_qspi_dma_callback
- Return type: static void
- Signature: ti_qspi_dma_callback(void * param)
- Line: 432

### ti_qspi_dma_cleanup
- Return type: static void
- Signature: ti_qspi_dma_cleanup(struct ti_qspi * qspi)
- Line: 740

### ti_qspi_dma_xfer
- Return type: static int
- Signature: ti_qspi_dma_xfer(struct ti_qspi * qspi,dma_addr_t dma_dst,dma_addr_t dma_src,size_t len)
- Line: 439

### ti_qspi_dma_xfer_sg
- Return type: static int
- Signature: ti_qspi_dma_xfer_sg(struct ti_qspi * qspi,struct sg_table rx_sg,loff_t from)
- Line: 505

### ti_qspi_enable_memory_map
- Return type: static void
- Signature: ti_qspi_enable_memory_map(struct spi_device * spi)
- Line: 525

### ti_qspi_exec_mem_op
- Return type: static int
- Signature: ti_qspi_exec_mem_op(struct spi_mem * mem,const struct spi_mem_op * op)
- Line: 604

### ti_qspi_poll_wc
- Return type: static int
- Signature: ti_qspi_poll_wc(struct ti_qspi * qspi)
- Line: 222

### ti_qspi_probe
- Return type: static int
- Signature: ti_qspi_probe(struct platform_device * pdev)
- Line: 758

### ti_qspi_read
- Return type: static unsigned long
- Signature: ti_qspi_read(struct ti_qspi * qspi,unsigned long reg)
- Line: 126

### ti_qspi_remove
- Return type: static void
- Signature: ti_qspi_remove(struct platform_device * pdev)
- Line: 904

### ti_qspi_restore_ctx
- Return type: static void
- Signature: ti_qspi_restore_ctx(struct ti_qspi * qspi)
- Line: 200

### ti_qspi_runtime_resume
- Return type: static int
- Signature: ti_qspi_runtime_resume(struct device * dev)
- Line: 730

### ti_qspi_setup
- Return type: static int
- Signature: ti_qspi_setup(struct spi_device * spi)
- Line: 138

### ti_qspi_setup_clk
- Return type: static void
- Signature: ti_qspi_setup_clk(struct ti_qspi * qspi,u32 speed_hz)
- Line: 170

### ti_qspi_setup_mmap_read
- Return type: static void
- Signature: ti_qspi_setup_mmap_read(struct spi_device * spi,u8 opcode,u8 data_nbits,u8 addr_width,u8 dummy_bytes)
- Line: 551

### ti_qspi_start_transfer_one
- Return type: static int
- Signature: ti_qspi_start_transfer_one(struct spi_controller * host,struct spi_message * m)
- Line: 663

### ti_qspi_write
- Return type: static void
- Signature: ti_qspi_write(struct ti_qspi * qspi,unsigned long val,unsigned long reg)
- Line: 132

## Structs (2)

### ti_qspi
- Line: 37
- Members:
  - clkctrl: u32
  - transfer_complete: completion
  - list_lock: mutex
  - host: spi_controller *
  - base: void __iomem *
  - mmap_base: void __iomem *
  - mmap_size: size_t
  - ctrl_base: regmap *
  - ctrl_reg: unsigned int
  - fclk: clk *
  - dev: device *
  - ctx_reg: ti_qspi_regs
  - mmap_phys_base: dma_addr_t
  - rx_bb_dma_addr: dma_addr_t
  - rx_bb_addr: void *
  - rx_chan: dma_chan *
  - cmd: u32
  - dc: u32
  - mmap_enabled: bool
  - current_cs: int

### ti_qspi_regs
- Line: 33
- Members:
  - clkctrl: u32
  - transfer_complete: completion
  - list_lock: mutex
  - host: spi_controller *
  - base: void __iomem *
  - mmap_base: void __iomem *
  - mmap_size: size_t
  - ctrl_base: regmap *
  - ctrl_reg: unsigned int
  - fclk: clk *
  - dev: device *
  - ctx_reg: ti_qspi_regs
  - mmap_phys_base: dma_addr_t
  - rx_bb_dma_addr: dma_addr_t
  - rx_bb_addr: void *
  - rx_chan: dma_chan *
  - cmd: u32
  - dc: u32
  - mmap_enabled: bool
  - current_cs: int

## Variables (5)

- static **ti_qspi_driver** : platform_driver (line 924)
- static **ti_qspi_match** : const struct of_device_id[] (line 751)
- static **ti_qspi_mem_caps** : const struct spi_controller_mem_caps (line 659)
- static **ti_qspi_mem_ops** : const struct spi_controller_mem_ops (line 654)
- static **ti_qspi_pm_ops** : const struct dev_pm_ops (line 920)

## Macros (44)

- **BUSY** (line 100)
- **MEM_CS_EN**(n) (line 113)
- **MEM_CS_MASK** (line 114)
- **MM_SWITCH** (line 116)
- **QSPI_3_PIN** (line 88)
- **QSPI_AUTOSUSPEND_TIMEOUT** (line 111)
- **QSPI_CKPHA**(n) (line 105)
- **QSPI_CKPOL**(n) (line 107)
- **QSPI_CLK_DIV_MAX** (line 83)
- **QSPI_CLK_EN** (line 82)
- **QSPI_COMPLETION_TIMEOUT** (line 79)
- **QSPI_CSPOL**(n) (line 106)
- **QSPI_DD**(m,n) (line 104)
- **QSPI_DMA_BUFFER_SIZE** (line 124)
- **QSPI_EN_CS**(n) (line 86)
- **QSPI_FLEN**(n) (line 94)
- **QSPI_FRAME** (line 109)
- **QSPI_INVAL** (line 93)
- **QSPI_PID** (line 66)
- **QSPI_RD_DUAL** (line 91)
- **QSPI_RD_QUAD** (line 92)
- **QSPI_RD_SNGL** (line 89)
- **QSPI_SETUP_ADDR_SHIFT** (line 121)
- **QSPI_SETUP_DUMMY_SHIFT** (line 122)
- **QSPI_SETUP_RD_DUAL** (line 119)
- **QSPI_SETUP_RD_NORMAL** (line 118)
- **QSPI_SETUP_RD_QUAD** (line 120)
- **QSPI_SPI_CLOCK_CNTRL_REG** (line 68)
- **QSPI_SPI_CMD_REG** (line 70)
- **QSPI_SPI_DATA_REG** (line 72)
- **QSPI_SPI_DATA_REG_1** (line 75)
- **QSPI_SPI_DATA_REG_2** (line 76)
- **QSPI_SPI_DATA_REG_3** (line 77)
- **QSPI_SPI_DC_REG** (line 69)
- **QSPI_SPI_SETUP_REG**(n) (line 73)
- **QSPI_SPI_STATUS_REG** (line 71)
- **QSPI_SPI_SWITCH_REG** (line 74)
- **QSPI_SYSCONFIG** (line 67)
- **QSPI_WLEN**(n) (line 87)
- **QSPI_WLEN_MASK** (line 97)
- **QSPI_WLEN_MAX_BITS** (line 95)
- **QSPI_WLEN_MAX_BYTES** (line 96)
- **QSPI_WR_SNGL** (line 90)
- **WC** (line 101)
