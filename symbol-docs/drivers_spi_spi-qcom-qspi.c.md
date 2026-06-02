# drivers/spi/spi-qcom-qspi.c

Subsystem: drivers/spi

## Functions (23)

### pio_read
- Return type: static irqreturn_t
- Signature: pio_read(struct qcom_qspi * ctrl)
- Line: 524

### pio_write
- Return type: static irqreturn_t
- Signature: pio_write(struct qcom_qspi * ctrl)
- Line: 567

### qcom_qspi_adjust_op_size
- Return type: static int
- Signature: qcom_qspi_adjust_op_size(struct spi_mem * mem,struct spi_mem_op * op)
- Line: 669

### qcom_qspi_alloc_desc
- Return type: static int
- Signature: qcom_qspi_alloc_desc(struct qcom_qspi * ctrl,dma_addr_t dma_ptr,uint32_t n_bytes)
- Line: 304

### qcom_qspi_alloc_dma
- Return type: static int
- Signature: qcom_qspi_alloc_dma(struct qcom_qspi * ctrl)
- Line: 514

### qcom_qspi_can_dma
- Return type: static bool
- Signature: qcom_qspi_can_dma(struct spi_controller * ctlr,struct spi_device * slv,struct spi_transfer * xfer)
- Line: 408

### qcom_qspi_dma_xfer
- Return type: static void
- Signature: qcom_qspi_dma_xfer(struct qcom_qspi * ctrl)
- Line: 396

### qcom_qspi_handle_err
- Return type: static void
- Signature: qcom_qspi_handle_err(struct spi_controller * host,struct spi_message * msg)
- Line: 250

### qcom_qspi_irq
- Return type: static irqreturn_t
- Signature: qcom_qspi_irq(int irq,void * dev_id)
- Line: 611

### qcom_qspi_pio_xfer
- Return type: static void
- Signature: qcom_qspi_pio_xfer(struct qcom_qspi * ctrl)
- Line: 230

### qcom_qspi_pio_xfer_cfg
- Return type: static void
- Signature: qcom_qspi_pio_xfer_cfg(struct qcom_qspi * ctrl)
- Line: 199

### qcom_qspi_pio_xfer_ctrl
- Return type: static void
- Signature: qcom_qspi_pio_xfer_ctrl(struct qcom_qspi * ctrl)
- Line: 220

### qcom_qspi_prepare_message
- Return type: static int
- Signature: qcom_qspi_prepare_message(struct spi_controller * host,struct spi_message * message)
- Line: 484

### qcom_qspi_probe
- Return type: static int
- Signature: qcom_qspi_probe(struct platform_device * pdev)
- Line: 693

### qcom_qspi_remove
- Return type: static void
- Signature: qcom_qspi_remove(struct platform_device * pdev)
- Line: 805

### qcom_qspi_resume
- Return type: static int __maybe_unused
- Signature: qcom_qspi_resume(struct device * dev)
- Line: 875

### qcom_qspi_runtime_resume
- Return type: static int __maybe_unused
- Signature: qcom_qspi_runtime_resume(struct device * dev)
- Line: 837

### qcom_qspi_runtime_suspend
- Return type: static int __maybe_unused
- Signature: qcom_qspi_runtime_suspend(struct device * dev)
- Line: 815

### qcom_qspi_set_speed
- Return type: static int
- Signature: qcom_qspi_set_speed(struct qcom_qspi * ctrl,unsigned long speed_hz)
- Line: 272

### qcom_qspi_setup_dma_desc
- Return type: static int
- Signature: qcom_qspi_setup_dma_desc(struct qcom_qspi * ctrl,struct spi_transfer * xfer)
- Line: 338

### qcom_qspi_suspend
- Return type: static int __maybe_unused
- Signature: qcom_qspi_suspend(struct device * dev)
- Line: 859

### qcom_qspi_transfer_one
- Return type: static int
- Signature: qcom_qspi_transfer_one(struct spi_controller * host,struct spi_device * slv,struct spi_transfer * xfer)
- Line: 414

### qspi_buswidth_to_iomode
- Return type: static u32
- Signature: qspi_buswidth_to_iomode(struct qcom_qspi * ctrl,unsigned int buswidth)
- Line: 182

## Structs (3)

### qcom_qspi
- Line: 167
- Members:
  - data_address: u32
  - next_descriptor: u32
  - direction: u32:1
  - multi_io_mode: u32:3
  - reserved1: u32:4
  - fragment: u32:1
  - reserved2: u32:7
  - length: u32:16
  - tx_buf: const void *
  - rx_buf: void *
  - rem_bytes: unsigned int
  - buswidth: unsigned int
  - dir: qspi_dir
  - is_last: bool
  - base: void __iomem *
  - dev: device *
  - clks: clk_bulk_data *
  - xfer: qspi_xfer
  - dma_cmd_pool: dma_pool *
  - dma_cmd_desc: dma_addr_t[]
  - virt_cmd_desc: void * []
  - n_cmd_desc: unsigned int
  - icc_path_cpu_to_qspi: icc_path *
  - last_speed: unsigned long
  - lock: spinlock_t

### qspi_cmd_desc
- Line: 131
- Members:
  - data_address: u32
  - next_descriptor: u32
  - direction: u32:1
  - multi_io_mode: u32:3
  - reserved1: u32:4
  - fragment: u32:1
  - reserved2: u32:7
  - length: u32:16
  - tx_buf: const void *
  - rx_buf: void *
  - rem_bytes: unsigned int
  - buswidth: unsigned int
  - dir: qspi_dir
  - is_last: bool
  - base: void __iomem *
  - dev: device *
  - clks: clk_bulk_data *
  - xfer: qspi_xfer
  - dma_cmd_pool: dma_pool *
  - dma_cmd_desc: dma_addr_t[]
  - virt_cmd_desc: void * []
  - n_cmd_desc: unsigned int
  - icc_path_cpu_to_qspi: icc_path *
  - last_speed: unsigned long
  - lock: spinlock_t

### qspi_xfer
- Line: 142
- Members:
  - data_address: u32
  - next_descriptor: u32
  - direction: u32:1
  - multi_io_mode: u32:3
  - reserved1: u32:4
  - fragment: u32:1
  - reserved2: u32:7
  - length: u32:16
  - tx_buf: const void *
  - rx_buf: void *
  - rem_bytes: unsigned int
  - buswidth: unsigned int
  - dir: qspi_dir
  - is_last: bool
  - base: void __iomem *
  - dev: device *
  - clks: clk_bulk_data *
  - xfer: qspi_xfer
  - dma_cmd_pool: dma_pool *
  - dma_cmd_desc: dma_addr_t[]
  - virt_cmd_desc: void * []
  - n_cmd_desc: unsigned int
  - icc_path_cpu_to_qspi: icc_path *
  - last_speed: unsigned long
  - lock: spinlock_t

## Enums (2)

### qspi_clocks
- Line: 153

### qspi_dir
- Line: 126

## Unions (1)

### __anon37825b3c010a
- Line: 143
- Members:
  - data_address: u32
  - next_descriptor: u32
  - direction: u32:1
  - multi_io_mode: u32:3
  - reserved1: u32:4
  - fragment: u32:1
  - reserved2: u32:7
  - length: u32:16
  - tx_buf: const void *
  - rx_buf: void *
  - rem_bytes: unsigned int
  - buswidth: unsigned int
  - dir: qspi_dir
  - is_last: bool
  - base: void __iomem *
  - dev: device *
  - clks: clk_bulk_data *
  - xfer: qspi_xfer
  - dma_cmd_pool: dma_pool *
  - dma_cmd_desc: dma_addr_t[]
  - virt_cmd_desc: void * []
  - n_cmd_desc: unsigned int
  - icc_path_cpu_to_qspi: icc_path *
  - last_speed: unsigned long
  - lock: spinlock_t

## Variables (4)

- static **qcom_qspi_dev_pm_ops** : const struct dev_pm_ops (line 891)
- static **qcom_qspi_driver** : platform_driver (line 903)
- static **qcom_qspi_dt_match** : const struct of_device_id[] (line 897)
- static **qcom_qspi_mem_ops** : const struct spi_controller_mem_ops (line 689)

## Macros (91)

- **AHB_MASTER_CFG** (line 45)
- **BIG_ENDIAN_MODE** (line 29)
- **CHIP_SELECT_NUM** (line 32)
- **CONTINUOUS_MODE** (line 100)
- **CURRENT_DMA_DESC_ADDR** (line 115)
- **CURRENT_MEM_ADDR** (line 116)
- **CUR_MEM_ADDR** (line 118)
- **DDR_1BIT** (line 85)
- **DDR_2BIT** (line 86)
- **DDR_4BIT** (line 87)
- **DMA_CHAIN_DONE** (line 67)
- **DMA_DESC_DUAL_SPI** (line 89)
- **DMA_DESC_QUAD_SPI** (line 90)
- **DMA_DESC_SINGLE_SPI** (line 88)
- **DMA_ENABLE** (line 28)
- **FB_CLK_EN** (line 25)
- **FIFO_EMPTY** (line 103)
- **FIFO_RDY** (line 109)
- **FULL_CYCLE_MODE** (line 24)
- **HINNERSHARED** (line 55)
- **HMEMTYPE_READ_TRANS_MSK** (line 52)
- **HMEMTYPE_READ_TRANS_SHFT** (line 53)
- **HMEM_TYPE_LAST_TRANS_MSK** (line 48)
- **HMEM_TYPE_LAST_TRANS_SHFT** (line 49)
- **HMEM_TYPE_START_MID_TRANS_MSK** (line 46)
- **HMEM_TYPE_START_MID_TRANS_SHFT** (line 47)
- **HRESP_FROM_NOC_ERR** (line 62)
- **HSHARED** (line 54)
- **HW_VERSION** (line 119)
- **LPA_BASE_MSK** (line 34)
- **LPA_BASE_SHFT** (line 35)
- **MSTR_CONFIG** (line 23)
- **MSTR_INT_EN** (line 57)
- **MSTR_INT_STATUS** (line 58)
- **MULTI_IO_MODE_MSK** (line 79)
- **MULTI_IO_MODE_SHFT** (line 80)
- **NEXT_DMA_DESC_ADDR** (line 114)
- **PIN_HOLDN** (line 26)
- **PIN_WPN** (line 27)
- **PIO_DATAOUT_1B** (line 96)
- **PIO_DATAOUT_4B** (line 97)
- **PIO_XFER_CFG** (line 77)
- **PIO_XFER_CTRL** (line 74)
- **PIO_XFER_STATUS** (line 92)
- **QSPI_ALIGN_REQ** (line 124)
- **QSPI_ALL_IRQS** (line 70)
- **QSPI_BYTES_PER_WORD** (line 21)
- **QSPI_ERR_IRQS** (line 68)
- **QSPI_MAX_BYTES_FIFO** (line 406)
- **QSPI_MAX_SG** (line 165)
- **QSPI_NUM_CS** (line 20)
- **RDY_16BYTE** (line 108)
- **RDY_32BYTE** (line 107)
- **RDY_64BYTE** (line 106)
- **RD_FIFO** (line 120)
- **RD_FIFO_CFG** (line 99)
- **RD_FIFO_RESET** (line 111)
- **RD_FIFO_STATUS** (line 102)
- **REQUEST_COUNT_MSK** (line 75)
- **RESET_FIFO** (line 112)
- **RESP_FIFO_NOT_EMPTY** (line 60)
- **RESP_FIFO_RDY** (line 61)
- **RESP_FIFO_UNDERRUN** (line 59)
- **SAMPLING_CLK_CFG** (line 121)
- **SAMPLING_CLK_STATUS** (line 122)
- **SBL_EN** (line 33)
- **SDR_1BIT** (line 82)
- **SDR_2BIT** (line 83)
- **SDR_4BIT** (line 84)
- **SPI_MODE_MSK** (line 30)
- **SPI_MODE_SHFT** (line 31)
- **TRANSACTION_DONE** (line 66)
- **TRANSFER_DIRECTION** (line 78)
- **TRANSFER_FRAGMENT** (line 81)
- **TX_CLK_DELAY_MSK** (line 38)
- **TX_CLK_DELAY_SHFT** (line 39)
- **TX_CS_N_DELAY_MSK** (line 40)
- **TX_CS_N_DELAY_SHFT** (line 41)
- **TX_DATA_DELAY_MSK** (line 36)
- **TX_DATA_DELAY_SHFT** (line 37)
- **TX_DATA_OE_DELAY_MSK** (line 42)
- **TX_DATA_OE_DELAY_SHFT** (line 43)
- **USE_HMEMTYPE_LAST_ON_DESC_OR_CHAIN_MSK** (line 50)
- **USE_HMEMTYPE_LAST_ON_DESC_OR_CHAIN_SHFT** (line 51)
- **WR_CNTS_MSK** (line 104)
- **WR_CNTS_SHFT** (line 105)
- **WR_FIFO_BYTES_MSK** (line 93)
- **WR_FIFO_BYTES_SHFT** (line 94)
- **WR_FIFO_EMPTY** (line 63)
- **WR_FIFO_FULL** (line 64)
- **WR_FIFO_OVERRUN** (line 65)
