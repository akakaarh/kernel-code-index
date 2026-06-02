# drivers/spi/spi-mtk-nor.c

Subsystem: drivers/spi

## Functions (33)

### mtk_max_msg_size
- Return type: static size_t
- Signature: mtk_max_msg_size(struct spi_device * spi)
- Line: 776

### mtk_nor_adj_prg_size
- Return type: static void
- Signature: mtk_nor_adj_prg_size(struct spi_mem_op * op)
- Line: 257

### mtk_nor_adjust_op_size
- Return type: static int
- Signature: mtk_nor_adjust_op_size(struct spi_mem * mem,struct spi_mem_op * op)
- Line: 276

### mtk_nor_cmd_exec
- Return type: static int
- Signature: mtk_nor_cmd_exec(struct mtk_nor * sp,u32 cmd,ulong clk)
- Line: 140

### mtk_nor_disable_clk
- Return type: static void
- Signature: mtk_nor_disable_clk(struct mtk_nor * sp)
- Line: 704

### mtk_nor_dma_exec
- Return type: static int
- Signature: mtk_nor_dma_exec(struct mtk_nor * sp,u32 from,unsigned int length,dma_addr_t dma_addr)
- Line: 366

### mtk_nor_enable_clk
- Return type: static int
- Signature: mtk_nor_enable_clk(struct mtk_nor * sp)
- Line: 712

### mtk_nor_exec_op
- Return type: static int
- Signature: mtk_nor_exec_op(struct spi_mem * mem,const struct spi_mem_op * op)
- Line: 599

### mtk_nor_init
- Return type: static void
- Signature: mtk_nor_init(struct mtk_nor * sp)
- Line: 744

### mtk_nor_irq_handler
- Return type: static irqreturn_t
- Signature: mtk_nor_irq_handler(int irq,void * data)
- Line: 755

### mtk_nor_match_prg
- Return type: static bool
- Signature: mtk_nor_match_prg(const struct spi_mem_op * op)
- Line: 208

### mtk_nor_match_read
- Return type: static bool
- Signature: mtk_nor_match_read(const struct spi_mem_op * op)
- Line: 185

### mtk_nor_pp_buffered
- Return type: static int
- Signature: mtk_nor_pp_buffered(struct mtk_nor * sp,const struct spi_mem_op * op)
- Line: 485

### mtk_nor_pp_unbuffered
- Return type: static int
- Signature: mtk_nor_pp_unbuffered(struct mtk_nor * sp,const struct spi_mem_op * op)
- Line: 504

### mtk_nor_probe
- Return type: static int
- Signature: mtk_nor_probe(struct platform_device * pdev)
- Line: 810

### mtk_nor_read_bounce
- Return type: static int
- Signature: mtk_nor_read_bounce(struct mtk_nor * sp,const struct spi_mem_op * op)
- Line: 410

### mtk_nor_read_dma
- Return type: static int
- Signature: mtk_nor_read_dma(struct mtk_nor * sp,const struct spi_mem_op * op)
- Line: 428

### mtk_nor_read_pio
- Return type: static int
- Signature: mtk_nor_read_pio(struct mtk_nor * sp,const struct spi_mem_op * op)
- Line: 449

### mtk_nor_remove
- Return type: static void
- Signature: mtk_nor_remove(struct platform_device * pdev)
- Line: 936

### mtk_nor_reset
- Return type: static void
- Signature: mtk_nor_reset(struct mtk_nor * sp)
- Line: 154

### mtk_nor_resume
- Return type: static int __maybe_unused
- Signature: mtk_nor_resume(struct device * dev)
- Line: 973

### mtk_nor_rmw
- Return type: static void
- Signature: mtk_nor_rmw(struct mtk_nor * sp,u32 reg,u32 set,u32 clr)
- Line: 131

### mtk_nor_runtime_resume
- Return type: static int __maybe_unused
- Signature: mtk_nor_runtime_resume(struct device * dev)
- Line: 960

### mtk_nor_runtime_suspend
- Return type: static int __maybe_unused
- Signature: mtk_nor_runtime_suspend(struct device * dev)
- Line: 950

### mtk_nor_set_addr
- Return type: static void
- Signature: mtk_nor_set_addr(struct mtk_nor * sp,const struct spi_mem_op * op)
- Line: 163

### mtk_nor_setup
- Return type: static int
- Signature: mtk_nor_setup(struct spi_device * spi)
- Line: 640

### mtk_nor_setup_bus
- Return type: static void
- Signature: mtk_nor_setup_bus(struct mtk_nor * sp,const struct spi_mem_op * op)
- Line: 340

### mtk_nor_setup_write_buffer
- Return type: static int
- Signature: mtk_nor_setup_write_buffer(struct mtk_nor * sp,bool on)
- Line: 460

### mtk_nor_spi_mem_prg
- Return type: static int
- Signature: mtk_nor_spi_mem_prg(struct mtk_nor * sp,const struct spi_mem_op * op)
- Line: 517

### mtk_nor_supports_op
- Return type: static bool
- Signature: mtk_nor_supports_op(struct spi_mem * mem,const struct spi_mem_op * op)
- Line: 311

### mtk_nor_suspend
- Return type: static int __maybe_unused
- Signature: mtk_nor_suspend(struct device * dev)
- Line: 968

### mtk_nor_transfer_one_message
- Return type: static int
- Signature: mtk_nor_transfer_one_message(struct spi_controller * host,struct spi_message * m)
- Line: 654

### need_bounce
- Return type: static bool
- Signature: need_bounce(struct mtk_nor * sp,const struct spi_mem_op * op)
- Line: 180

## Structs (2)

### mtk_nor
- Line: 113
- Members:
  - dma_bits: u8
  - extra_dummy_bit: u8
  - ctlr: spi_controller *
  - dev: device *
  - base: void __iomem *
  - buffer: u8 *
  - buffer_dma: dma_addr_t
  - spi_clk: clk *
  - ctlr_clk: clk *
  - axi_clk: clk *
  - axi_s_clk: clk *
  - spi_freq: unsigned int
  - wbuf_en: bool
  - has_irq: bool
  - high_dma: bool
  - op_done: completion
  - caps: const struct mtk_nor_caps *

### mtk_nor_caps
- Line: 102
- Members:
  - dma_bits: u8
  - extra_dummy_bit: u8
  - ctlr: spi_controller *
  - dev: device *
  - base: void __iomem *
  - buffer: u8 *
  - buffer_dma: dma_addr_t
  - spi_clk: clk *
  - ctlr_clk: clk *
  - axi_clk: clk *
  - axi_s_clk: clk *
  - spi_freq: unsigned int
  - wbuf_en: bool
  - has_irq: bool
  - high_dma: bool
  - op_done: completion
  - caps: const struct mtk_nor_caps *

## Variables (7)

- static **mtk_nor_caps_mt8173** : const struct mtk_nor_caps (line 787)
- static **mtk_nor_caps_mt8186** : const struct mtk_nor_caps (line 792)
- static **mtk_nor_caps_mt8192** : const struct mtk_nor_caps (line 797)
- static **mtk_nor_driver** : platform_driver (line 994)
- static **mtk_nor_match** : const struct of_device_id[] (line 802)
- static **mtk_nor_mem_ops** : const struct spi_controller_mem_ops (line 781)
- static **mtk_nor_pm_ops** : const struct dev_pm_ops (line 988)

## Macros (56)

- **CLK_TO_US**(sp,clkcnt) (line 100)
- **DRIVER_NAME** (line 23)
- **MTK_NOR_4B_ADDR** (line 71)
- **MTK_NOR_BOUNCE_BUF_SIZE** (line 95)
- **MTK_NOR_BUS_MODE_MASK** (line 76)
- **MTK_NOR_CMD_MASK** (line 29)
- **MTK_NOR_CMD_PROGRAM** (line 27)
- **MTK_NOR_CMD_READ** (line 28)
- **MTK_NOR_CMD_WRITE** (line 26)
- **MTK_NOR_DISABLE_SR_POLL** (line 65)
- **MTK_NOR_DISABLE_WREN** (line 64)
- **MTK_NOR_DMA_ALIGN** (line 92)
- **MTK_NOR_DMA_ALIGN_MASK** (line 93)
- **MTK_NOR_DMA_START** (line 79)
- **MTK_NOR_DUAL_ADDR** (line 74)
- **MTK_NOR_DUAL_READ** (line 75)
- **MTK_NOR_ENABLE_SF_CMD** (line 68)
- **MTK_NOR_FAST_READ** (line 50)
- **MTK_NOR_IRQ_DMA** (line 60)
- **MTK_NOR_IRQ_MASK** (line 61)
- **MTK_NOR_PP_SIZE** (line 98)
- **MTK_NOR_PRG_CNT_MAX** (line 32)
- **MTK_NOR_PRG_MAX_SIZE** (line 90)
- **MTK_NOR_QUAD_ADDR** (line 72)
- **MTK_NOR_QUAD_READ** (line 73)
- **MTK_NOR_REG_BUSCFG** (line 70)
- **MTK_NOR_REG_CFG1** (line 49)
- **MTK_NOR_REG_CFG2** (line 52)
- **MTK_NOR_REG_CFG3** (line 63)
- **MTK_NOR_REG_CG_DIS** (line 84)
- **MTK_NOR_REG_CMD** (line 25)
- **MTK_NOR_REG_DMA_CTL** (line 78)
- **MTK_NOR_REG_DMA_DADR** (line 82)
- **MTK_NOR_REG_DMA_DADR_HB** (line 87)
- **MTK_NOR_REG_DMA_END_DADR** (line 83)
- **MTK_NOR_REG_DMA_END_DADR_HB** (line 88)
- **MTK_NOR_REG_DMA_FADR** (line 81)
- **MTK_NOR_REG_IRQ_EN** (line 59)
- **MTK_NOR_REG_IRQ_STAT** (line 58)
- **MTK_NOR_REG_PP_DATA** (line 56)
- **MTK_NOR_REG_PRGDATA**(n) (line 42)
- **MTK_NOR_REG_PRGDATA0** (line 41)
- **MTK_NOR_REG_PRGDATA_MAX** (line 43)
- **MTK_NOR_REG_PRG_CNT** (line 31)
- **MTK_NOR_REG_RADR**(n) (line 36)
- **MTK_NOR_REG_RADR0** (line 35)
- **MTK_NOR_REG_RADR3** (line 37)
- **MTK_NOR_REG_RDATA** (line 33)
- **MTK_NOR_REG_SHIFT**(n) (line 46)
- **MTK_NOR_REG_SHIFT0** (line 45)
- **MTK_NOR_REG_SHIFT_MAX** (line 47)
- **MTK_NOR_REG_WDATA** (line 39)
- **MTK_NOR_REG_WP** (line 67)
- **MTK_NOR_SFC_SW_RST** (line 85)
- **MTK_NOR_WR_BUF_EN** (line 54)
- **MTK_NOR_WR_CUSTOM_OP_EN** (line 53)
