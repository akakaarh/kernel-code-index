# drivers/spi/spi-zynqmp-gqspi.c

Subsystem: drivers/spi

## Functions (28)

### zynqmp_gqspi_read
- Return type: static u32
- Signature: zynqmp_gqspi_read(struct zynqmp_qspi * xqspi,u32 offset)
- Line: 219

### zynqmp_gqspi_selecttarget
- Return type: static void
- Signature: zynqmp_gqspi_selecttarget(struct zynqmp_qspi * instanceptr,u8 targetcs,u8 targetbus)
- Line: 242

### zynqmp_gqspi_write
- Return type: static void
- Signature: zynqmp_gqspi_write(struct zynqmp_qspi * xqspi,u32 offset,u32 val)
- Line: 230

### zynqmp_process_dma_irq
- Return type: static void
- Signature: zynqmp_process_dma_irq(struct zynqmp_qspi * xqspi)
- Line: 754

### zynqmp_qspi_chipselect
- Return type: static void
- Signature: zynqmp_qspi_chipselect(struct spi_device * qspi,bool is_high)
- Line: 459

### zynqmp_qspi_config_op
- Return type: static int
- Signature: zynqmp_qspi_config_op(struct zynqmp_qspi * xqspi,const struct spi_mem_op * op)
- Line: 554

### zynqmp_qspi_copy_read_data
- Return type: static void
- Signature: zynqmp_qspi_copy_read_data(struct zynqmp_qspi * xqspi,ulong data,u8 size)
- Line: 446

### zynqmp_qspi_disable_dma
- Return type: static void
- Signature: zynqmp_qspi_disable_dma(struct zynqmp_qspi * xqspi)
- Line: 724

### zynqmp_qspi_enable_dma
- Return type: static void
- Signature: zynqmp_qspi_enable_dma(struct zynqmp_qspi * xqspi)
- Line: 737

### zynqmp_qspi_exec_op
- Return type: static int
- Signature: zynqmp_qspi_exec_op(struct spi_mem * mem,const struct spi_mem_op * op)
- Line: 1044

### zynqmp_qspi_fillgenfifo
- Return type: static void
- Signature: zynqmp_qspi_fillgenfifo(struct zynqmp_qspi * xqspi,u8 nbits,u32 genfifoentry)
- Line: 671

### zynqmp_qspi_filltxfifo
- Return type: static void
- Signature: zynqmp_qspi_filltxfifo(struct zynqmp_qspi * xqspi,int size)
- Line: 616

### zynqmp_qspi_init_hw
- Return type: static void
- Signature: zynqmp_qspi_init_hw(struct zynqmp_qspi * xqspi)
- Line: 353

### zynqmp_qspi_irq
- Return type: static irqreturn_t
- Signature: zynqmp_qspi_irq(int irq,void * dev_id)
- Line: 806

### zynqmp_qspi_probe
- Return type: static int
- Signature: zynqmp_qspi_probe(struct platform_device * pdev)
- Line: 1220

### zynqmp_qspi_read_op
- Return type: static int
- Signature: zynqmp_qspi_read_op(struct zynqmp_qspi * xqspi,u8 rx_nbits,u32 genfifoentry)
- Line: 917

### zynqmp_qspi_readrxfifo
- Return type: static void
- Signature: zynqmp_qspi_readrxfifo(struct zynqmp_qspi * xqspi,u32 size)
- Line: 643

### zynqmp_qspi_remove
- Return type: static void
- Signature: zynqmp_qspi_remove(struct platform_device * pdev)
- Line: 1359

### zynqmp_qspi_resume
- Return type: static int __maybe_unused
- Signature: zynqmp_qspi_resume(struct device * dev)
- Line: 962

### zynqmp_qspi_selectspimode
- Return type: static u32
- Signature: zynqmp_qspi_selectspimode(struct zynqmp_qspi * xqspi,u8 spimode)
- Line: 511

### zynqmp_qspi_set_tapdelay
- Return type: static void
- Signature: zynqmp_qspi_set_tapdelay(struct zynqmp_qspi * xqspi,u32 baudrateval)
- Line: 288

### zynqmp_qspi_setup_op
- Return type: static int
- Signature: zynqmp_qspi_setup_op(struct spi_device * qspi)
- Line: 596

### zynqmp_qspi_setuprxdma
- Return type: static int
- Signature: zynqmp_qspi_setuprxdma(struct zynqmp_qspi * xqspi)
- Line: 849

### zynqmp_qspi_suspend
- Return type: static int __maybe_unused
- Signature: zynqmp_qspi_suspend(struct device * dev)
- Line: 938

### zynqmp_qspi_timeout
- Return type: static unsigned long
- Signature: zynqmp_qspi_timeout(struct zynqmp_qspi * xqspi,u8 bits,unsigned long bytes)
- Line: 1021

### zynqmp_qspi_write_op
- Return type: static void
- Signature: zynqmp_qspi_write_op(struct zynqmp_qspi * xqspi,u8 tx_nbits,u32 genfifoentry)
- Line: 898

### zynqmp_runtime_resume
- Return type: static int __maybe_unused
- Signature: zynqmp_runtime_resume(struct device * dev)
- Line: 1000

### zynqmp_runtime_suspend
- Return type: static int __maybe_unused
- Signature: zynqmp_runtime_suspend(struct device * dev)
- Line: 982

## Structs (2)

### qspi_platform_data
- Line: 163
- Members:
  - quirks: u32
  - ctlr: spi_controller *
  - regs: void __iomem *
  - refclk: clk *
  - pclk: clk *
  - irq: int
  - dev: device *
  - txbuf: const void *
  - rxbuf: void *
  - bytes_to_transfer: int
  - bytes_to_receive: int
  - genfifocs: u32
  - genfifobus: u32
  - dma_rx_bytes: u32
  - dma_addr: dma_addr_t
  - genfifoentry: u32
  - mode: mode_type
  - data_completion: completion
  - op_lock: mutex
  - speed_hz: u32
  - has_tapdelay: bool

### zynqmp_qspi
- Line: 190
- Members:
  - quirks: u32
  - ctlr: spi_controller *
  - regs: void __iomem *
  - refclk: clk *
  - pclk: clk *
  - irq: int
  - dev: device *
  - txbuf: const void *
  - rxbuf: void *
  - bytes_to_transfer: int
  - bytes_to_receive: int
  - genfifocs: u32
  - genfifobus: u32
  - dma_rx_bytes: u32
  - dma_addr: dma_addr_t
  - genfifoentry: u32
  - mode: mode_type
  - data_completion: completion
  - op_lock: mutex
  - speed_hz: u32
  - has_tapdelay: bool

## Enums (1)

### mode_type
- Line: 157

## Variables (6)

- static **versal_qspi_def** : const struct qspi_platform_data (line 1194)
- static **zynqmp_qspi_dev_pm_ops** : const struct dev_pm_ops (line 1188)
- static **zynqmp_qspi_driver** : platform_driver (line 1379)
- static **zynqmp_qspi_mem_caps** : const struct spi_controller_mem_caps (line 1208)
- static **zynqmp_qspi_mem_ops** : const struct spi_controller_mem_ops (line 1204)
- static **zynqmp_qspi_of_match** : const struct of_device_id[] (line 1198)

## Macros (121)

- **GQSPI_BAUD_DIV_MAX** (line 129)
- **GQSPI_BAUD_DIV_SHIFT** (line 130)
- **GQSPI_CFG_BAUD_RATE_DIV_MASK** (line 64)
- **GQSPI_CFG_BAUD_RATE_DIV_SHIFT** (line 112)
- **GQSPI_CFG_CLK_PHA_MASK** (line 65)
- **GQSPI_CFG_CLK_POL_MASK** (line 66)
- **GQSPI_CFG_ENDIAN_MASK** (line 61)
- **GQSPI_CFG_EN_POLL_TO_MASK** (line 62)
- **GQSPI_CFG_GEN_FIFO_START_MODE_MASK** (line 60)
- **GQSPI_CFG_MODE_EN_DMA_MASK** (line 106)
- **GQSPI_CFG_MODE_EN_MASK** (line 59)
- **GQSPI_CFG_START_GEN_FIFO_MASK** (line 67)
- **GQSPI_CFG_WP_HOLD_MASK** (line 63)
- **GQSPI_CONFIG_OFST** (line 26)
- **GQSPI_DATA_DLY_ADJ_OFST** (line 51)
- **GQSPI_DATA_DLY_ADJ_SHIFT** (line 142)
- **GQSPI_DATA_DLY_ADJ_VALUE** (line 141)
- **GQSPI_DEFAULT_NUM_CS** (line 135)
- **GQSPI_DMA_UNALIGN** (line 134)
- **GQSPI_EN_MASK** (line 55)
- **GQSPI_EN_OFST** (line 31)
- **GQSPI_FIFO_CTRL_OFST** (line 41)
- **GQSPI_FIFO_CTRL_RST_GEN_FIFO_MASK** (line 87)
- **GQSPI_FIFO_CTRL_RST_RX_FIFO_MASK** (line 85)
- **GQSPI_FIFO_CTRL_RST_TX_FIFO_MASK** (line 86)
- **GQSPI_FREQ_100MHZ** (line 153)
- **GQSPI_FREQ_150MHZ** (line 154)
- **GQSPI_FREQ_37_5MHZ** (line 151)
- **GQSPI_FREQ_40MHZ** (line 152)
- **GQSPI_GENFIFO_BUS_BOTH** (line 79)
- **GQSPI_GENFIFO_BUS_LOWER** (line 77)
- **GQSPI_GENFIFO_BUS_MASK** (line 80)
- **GQSPI_GENFIFO_BUS_UPPER** (line 78)
- **GQSPI_GENFIFO_CS_HOLD** (line 114)
- **GQSPI_GENFIFO_CS_LOWER** (line 75)
- **GQSPI_GENFIFO_CS_SETUP** (line 113)
- **GQSPI_GENFIFO_CS_UPPER** (line 76)
- **GQSPI_GENFIFO_DATA_XFER** (line 69)
- **GQSPI_GENFIFO_EXP** (line 70)
- **GQSPI_GENFIFO_IMM_DATA_MASK** (line 68)
- **GQSPI_GENFIFO_MODE_DUALSPI** (line 72)
- **GQSPI_GENFIFO_MODE_MASK** (line 74)
- **GQSPI_GENFIFO_MODE_QUADSPI** (line 73)
- **GQSPI_GENFIFO_MODE_SPI** (line 71)
- **GQSPI_GENFIFO_POLL** (line 84)
- **GQSPI_GENFIFO_RX** (line 82)
- **GQSPI_GENFIFO_STRIPE** (line 83)
- **GQSPI_GENFIFO_TX** (line 81)
- **GQSPI_GEN_FIFO_OFST** (line 38)
- **GQSPI_GEN_FIFO_THRESHOLD_RESET_VAL** (line 121)
- **GQSPI_GF_THRESHOLD_OFST** (line 40)
- **GQSPI_IDR_ALL_MASK** (line 58)
- **GQSPI_IDR_OFST** (line 28)
- **GQSPI_IER_GENFIFOEMPTY_MASK** (line 102)
- **GQSPI_IER_OFST** (line 29)
- **GQSPI_IER_POLL_TIME_EXPIRE_MASK** (line 100)
- **GQSPI_IER_RXEMPTY_MASK** (line 99)
- **GQSPI_IER_RXNEMPTY_MASK** (line 101)
- **GQSPI_IER_TXEMPTY_MASK** (line 103)
- **GQSPI_IER_TXNOT_FULL_MASK** (line 98)
- **GQSPI_IMASK_OFST** (line 30)
- **GQSPI_IRQ_MASK** (line 110)
- **GQSPI_ISR_GENFIFOEMPTY_MASK** (line 92)
- **GQSPI_ISR_GENFIFOFULL_MASK** (line 89)
- **GQSPI_ISR_GENFIFONOT_FULL_MASK** (line 90)
- **GQSPI_ISR_IDR_MASK** (line 107)
- **GQSPI_ISR_OFST** (line 27)
- **GQSPI_ISR_POLL_TIME_EXPIRE_MASK** (line 97)
- **GQSPI_ISR_RXEMPTY_MASK** (line 88)
- **GQSPI_ISR_RXFULL_MASK** (line 93)
- **GQSPI_ISR_RXNEMPTY_MASK** (line 94)
- **GQSPI_ISR_TXEMPTY_MASK** (line 91)
- **GQSPI_ISR_TXFULL_MASK** (line 95)
- **GQSPI_ISR_TXNOT_FULL_MASK** (line 96)
- **GQSPI_ISR_WR_TO_CLR_MASK** (line 57)
- **GQSPI_LPBK_DLY_ADJ_DLY_1** (line 143)
- **GQSPI_LPBK_DLY_ADJ_DLY_1_SHIFT** (line 144)
- **GQSPI_LPBK_DLY_ADJ_OFST** (line 37)
- **GQSPI_LPBK_DLY_ADJ_USE_LPBK_MASK** (line 56)
- **GQSPI_MAX_NUM_CS** (line 137)
- **GQSPI_QSPIDMA_DST_ADDR_MSB_OFST** (line 50)
- **GQSPI_QSPIDMA_DST_ADDR_OFST** (line 49)
- **GQSPI_QSPIDMA_DST_CTRL_OFST** (line 42)
- **GQSPI_QSPIDMA_DST_CTRL_RESET_VAL** (line 122)
- **GQSPI_QSPIDMA_DST_INTR_ALL_MASK** (line 104)
- **GQSPI_QSPIDMA_DST_I_DIS_OFST** (line 47)
- **GQSPI_QSPIDMA_DST_I_EN_DONE_MASK** (line 108)
- **GQSPI_QSPIDMA_DST_I_EN_OFST** (line 46)
- **GQSPI_QSPIDMA_DST_I_MASK_OFST** (line 48)
- **GQSPI_QSPIDMA_DST_I_STS_DONE_MASK** (line 109)
- **GQSPI_QSPIDMA_DST_I_STS_OFST** (line 45)
- **GQSPI_QSPIDMA_DST_SIZE_OFST** (line 43)
- **GQSPI_QSPIDMA_DST_STS_OFST** (line 44)
- **GQSPI_QSPIDMA_DST_STS_WTC** (line 105)
- **GQSPI_RXD_OFST** (line 33)
- **GQSPI_RX_FIFO_FILL** (line 117)
- **GQSPI_RX_FIFO_THRESHOLD** (line 116)
- **GQSPI_RX_THRESHOLD_OFST** (line 35)
- **GQSPI_SELECT_FLASH_BUS_BOTH** (line 128)
- **GQSPI_SELECT_FLASH_BUS_LOWER** (line 126)
- **GQSPI_SELECT_FLASH_BUS_UPPER** (line 127)
- **GQSPI_SELECT_FLASH_CS_BOTH** (line 125)
- **GQSPI_SELECT_FLASH_CS_LOWER** (line 123)
- **GQSPI_SELECT_FLASH_CS_UPPER** (line 124)
- **GQSPI_SELECT_MODE_DUALSPI** (line 132)
- **GQSPI_SELECT_MODE_QUADSPI** (line 133)
- **GQSPI_SELECT_MODE_SPI** (line 131)
- **GQSPI_SEL_MASK** (line 54)
- **GQSPI_SEL_OFST** (line 39)
- **GQSPI_TXD_DEPTH** (line 115)
- **GQSPI_TXD_OFST** (line 32)
- **GQSPI_TX_FIFO_FILL** (line 119)
- **GQSPI_TX_FIFO_THRESHOLD_RESET_VAL** (line 118)
- **GQSPI_TX_THRESHOLD_OFST** (line 34)
- **GQSPI_USE_DATA_DLY** (line 139)
- **GQSPI_USE_DATA_DLY_SHIFT** (line 140)
- **IOU_TAPDLY_BYPASS_OFST** (line 36)
- **QSPI_QUIRK_HAS_TAPDELAY** (line 149)
- **SPI_AUTOSUSPEND_TIMEOUT** (line 156)
- **TAP_DLY_BYPASS_LQSPI_RX_SHIFT** (line 146)
- **TAP_DLY_BYPASS_LQSPI_RX_VALUE** (line 145)
