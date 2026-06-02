# drivers/spi/spi-rockchip-sfc.c

Subsystem: drivers/spi

## Functions (27)

### rockchip_sfc_adjust_op_size
- Return type: static int
- Signature: rockchip_sfc_adjust_op_size(struct spi_mem * mem,struct spi_mem_op * op)
- Line: 573

### rockchip_sfc_adjust_op_work
- Return type: static void
- Signature: rockchip_sfc_adjust_op_work(struct spi_mem_op * op)
- Line: 302

### rockchip_sfc_clk_get_rate
- Return type: static unsigned long
- Signature: rockchip_sfc_clk_get_rate(struct rockchip_sfc * sfc)
- Line: 229

### rockchip_sfc_clk_set_rate
- Return type: static int
- Signature: rockchip_sfc_clk_set_rate(struct rockchip_sfc * sfc,unsigned long speed)
- Line: 221

### rockchip_sfc_exec_mem_op
- Return type: static int
- Signature: rockchip_sfc_exec_mem_op(struct spi_mem * mem,const struct spi_mem_op * op)
- Line: 524

### rockchip_sfc_fifo_transfer_dma
- Return type: static int
- Signature: rockchip_sfc_fifo_transfer_dma(struct rockchip_sfc * sfc,dma_addr_t dma_buf,size_t len)
- Line: 449

### rockchip_sfc_get_max_iosize
- Return type: static u32
- Signature: rockchip_sfc_get_max_iosize(struct rockchip_sfc * sfc)
- Line: 216

### rockchip_sfc_get_version
- Return type: static u16
- Signature: rockchip_sfc_get_version(struct rockchip_sfc * sfc)
- Line: 211

### rockchip_sfc_init
- Return type: static int
- Signature: rockchip_sfc_init(struct rockchip_sfc * sfc)
- Line: 257

### rockchip_sfc_irq_handler
- Return type: static irqreturn_t
- Signature: rockchip_sfc_irq_handler(int irq,void * dev_id)
- Line: 591

### rockchip_sfc_irq_mask
- Return type: static void
- Signature: rockchip_sfc_irq_mask(struct rockchip_sfc * sfc,u32 mask)
- Line: 247

### rockchip_sfc_irq_unmask
- Return type: static void
- Signature: rockchip_sfc_irq_unmask(struct rockchip_sfc * sfc,u32 mask)
- Line: 237

### rockchip_sfc_probe
- Return type: static int
- Signature: rockchip_sfc_probe(struct platform_device * pdev)
- Line: 610

### rockchip_sfc_read_fifo
- Return type: static int
- Signature: rockchip_sfc_read_fifo(struct rockchip_sfc * sfc,u8 * buf,int len)
- Line: 417

### rockchip_sfc_remove
- Return type: static void
- Signature: rockchip_sfc_remove(struct platform_device * pdev)
- Line: 740

### rockchip_sfc_reset
- Return type: static int
- Signature: rockchip_sfc_reset(struct rockchip_sfc * sfc)
- Line: 190

### rockchip_sfc_resume
- Return type: static int
- Signature: rockchip_sfc_resume(struct device * dev)
- Line: 790

### rockchip_sfc_runtime_resume
- Return type: static int
- Signature: rockchip_sfc_runtime_resume(struct device * dev)
- Line: 765

### rockchip_sfc_runtime_suspend
- Return type: static int
- Signature: rockchip_sfc_runtime_suspend(struct device * dev)
- Line: 755

### rockchip_sfc_suspend
- Return type: static int
- Signature: rockchip_sfc_suspend(struct device * dev)
- Line: 783

### rockchip_sfc_wait_rxfifo_ready
- Return type: static int
- Signature: rockchip_sfc_wait_rxfifo_ready(struct rockchip_sfc * sfc,u32 timeout_us)
- Line: 285

### rockchip_sfc_wait_txfifo_ready
- Return type: static int
- Signature: rockchip_sfc_wait_txfifo_ready(struct rockchip_sfc * sfc,u32 timeout_us)
- Line: 268

### rockchip_sfc_write_fifo
- Return type: static int
- Signature: rockchip_sfc_write_fifo(struct rockchip_sfc * sfc,const u8 * buf,int len)
- Line: 386

### rockchip_sfc_xfer_data_dma
- Return type: static int
- Signature: rockchip_sfc_xfer_data_dma(struct rockchip_sfc * sfc,const struct spi_mem_op * op,u32 len)
- Line: 469

### rockchip_sfc_xfer_data_poll
- Return type: static int
- Signature: rockchip_sfc_xfer_data_poll(struct rockchip_sfc * sfc,const struct spi_mem_op * op,u32 len)
- Line: 458

### rockchip_sfc_xfer_done
- Return type: static int
- Signature: rockchip_sfc_xfer_done(struct rockchip_sfc * sfc,u32 timeout_us)
- Line: 496

### rockchip_sfc_xfer_setup
- Return type: static int
- Signature: rockchip_sfc_xfer_setup(struct rockchip_sfc * sfc,struct spi_mem * mem,const struct spi_mem_op * op,u32 len)
- Line: 317

## Structs (1)

### rockchip_sfc
- Line: 174
- Members:
  - dev: device *
  - regbase: void __iomem *
  - hclk: clk *
  - clk: clk *
  - speed: u32[]
  - buffer: void *
  - dma_buffer: dma_addr_t
  - cp: completion
  - use_dma: bool
  - max_iosize: u32
  - version: u16
  - host: spi_controller *

## Variables (5)

- static **rockchip_sfc_driver** : platform_driver (line 827)
- static **rockchip_sfc_dt_ids** : const struct of_device_id[] (line 821)
- static **rockchip_sfc_mem_caps** : const struct spi_controller_mem_caps (line 587)
- static **rockchip_sfc_mem_ops** : const struct spi_controller_mem_ops (line 582)
- static **rockchip_sfc_pm_ops** : const struct dev_pm_ops (line 815)

## Macros (99)

- **ROCKCHIP_AUTOSUSPEND_DELAY** (line 172)
- **SFC_ABIT** (line 70)
- **SFC_ADDR** (line 151)
- **SFC_AX** (line 67)
- **SFC_CMD** (line 136)
- **SFC_CMD_ADDR_0BITS** (line 143)
- **SFC_CMD_ADDR_24BITS** (line 144)
- **SFC_CMD_ADDR_32BITS** (line 145)
- **SFC_CMD_ADDR_SHIFT** (line 142)
- **SFC_CMD_ADDR_XBITS** (line 146)
- **SFC_CMD_CS_SHIFT** (line 148)
- **SFC_CMD_DIR_RD** (line 140)
- **SFC_CMD_DIR_SHIFT** (line 139)
- **SFC_CMD_DIR_WR** (line 141)
- **SFC_CMD_DUMMY_SHIFT** (line 138)
- **SFC_CMD_IDX_SHIFT** (line 137)
- **SFC_CMD_TRAN_BYTES_SHIFT** (line 147)
- **SFC_CS1_REG_OFFSET** (line 156)
- **SFC_CTRL** (line 27)
- **SFC_CTRL_ADDR_BITS_SHIFT** (line 30)
- **SFC_CTRL_CMD_BITS_SHIFT** (line 29)
- **SFC_CTRL_DATA_BITS_SHIFT** (line 31)
- **SFC_CTRL_PHASE_SEL_NEGETIVE** (line 28)
- **SFC_DATA** (line 154)
- **SFC_DLL_CTRL0** (line 118)
- **SFC_DLL_CTRL0_DLL_MAX_VER4** (line 120)
- **SFC_DLL_CTRL0_DLL_MAX_VER5** (line 121)
- **SFC_DLL_CTRL0_SCLK_SMP_DLL** (line 119)
- **SFC_DMA_ADDR** (line 128)
- **SFC_DMA_TRANS_THRETHOLD** (line 165)
- **SFC_DMA_TRIGGER** (line 124)
- **SFC_DMA_TRIGGER_START** (line 125)
- **SFC_FSR** (line 84)
- **SFC_FSR_RXLV_MASK** (line 91)
- **SFC_FSR_RXLV_SHIFT** (line 92)
- **SFC_FSR_RX_IS_EMPTY** (line 87)
- **SFC_FSR_RX_IS_FULL** (line 88)
- **SFC_FSR_TXLV_MASK** (line 89)
- **SFC_FSR_TXLV_SHIFT** (line 90)
- **SFC_FSR_TX_IS_EMPTY** (line 86)
- **SFC_FSR_TX_IS_FULL** (line 85)
- **SFC_FTLR** (line 56)
- **SFC_FTLR_RX_MASK** (line 60)
- **SFC_FTLR_RX_SHIFT** (line 59)
- **SFC_FTLR_TX_MASK** (line 58)
- **SFC_FTLR_TX_SHIFT** (line 57)
- **SFC_ICLR** (line 45)
- **SFC_ICLR_BUS_ERR** (line 51)
- **SFC_ICLR_DMA** (line 53)
- **SFC_ICLR_NSPI_ERR** (line 52)
- **SFC_ICLR_RX_FULL** (line 46)
- **SFC_ICLR_RX_UFLOW** (line 47)
- **SFC_ICLR_TRAN_FINISH** (line 50)
- **SFC_ICLR_TX_EMPTY** (line 49)
- **SFC_ICLR_TX_OFLOW** (line 48)
- **SFC_IMR** (line 34)
- **SFC_IMR_BUS_ERR** (line 40)
- **SFC_IMR_DMA** (line 42)
- **SFC_IMR_NSPI_ERR** (line 41)
- **SFC_IMR_RX_FULL** (line 35)
- **SFC_IMR_RX_UFLOW** (line 36)
- **SFC_IMR_TRAN_FINISH** (line 39)
- **SFC_IMR_TX_EMPTY** (line 38)
- **SFC_IMR_TX_OFLOW** (line 37)
- **SFC_ISR** (line 73)
- **SFC_ISR_BUS_ERR_SHIFT** (line 79)
- **SFC_ISR_DMA_SHIFT** (line 81)
- **SFC_ISR_NSPI_ERR_SHIFT** (line 80)
- **SFC_ISR_RX_FULL_SHIFT** (line 74)
- **SFC_ISR_RX_UFLOW_SHIFT** (line 75)
- **SFC_ISR_TX_EMPTY_SHIFT** (line 77)
- **SFC_ISR_TX_FINISH_SHIFT** (line 78)
- **SFC_ISR_TX_OFLOW_SHIFT** (line 76)
- **SFC_LEN_CTRL** (line 131)
- **SFC_LEN_CTRL_TRB_SEL** (line 132)
- **SFC_LEN_EXT** (line 133)
- **SFC_MAX_CHIPSELECT_NUM** (line 158)
- **SFC_MAX_IOSIZE_VER3** (line 160)
- **SFC_MAX_IOSIZE_VER4** (line 162)
- **SFC_MAX_SPEED** (line 170)
- **SFC_RCVR** (line 63)
- **SFC_RCVR_RESET** (line 64)
- **SFC_RISR** (line 100)
- **SFC_RISR_BUS_ERR** (line 106)
- **SFC_RISR_DMA** (line 108)
- **SFC_RISR_NSPI_ERR** (line 107)
- **SFC_RISR_RX_FULL** (line 101)
- **SFC_RISR_RX_UNDERFLOW** (line 102)
- **SFC_RISR_TRAN_FINISH** (line 105)
- **SFC_RISR_TX_EMPTY** (line 104)
- **SFC_RISR_TX_OVERFLOW** (line 103)
- **SFC_SR** (line 95)
- **SFC_SR_IS_BUSY** (line 97)
- **SFC_SR_IS_IDLE** (line 96)
- **SFC_VER** (line 111)
- **SFC_VER_3** (line 112)
- **SFC_VER_4** (line 113)
- **SFC_VER_5** (line 114)
- **SFC_VER_8** (line 115)
