# drivers/spi/spi-atcspi200.c

Subsystem: drivers/spi

## Functions (18)

### atcspi_adjust_op_size
- Return type: static int
- Signature: atcspi_adjust_op_size(struct spi_mem * mem,struct spi_mem_op * op)
- Line: 256

### atcspi_configure_dma
- Return type: static int
- Signature: atcspi_configure_dma(struct atcspi_dev * spi)
- Line: 501

### atcspi_dma_callback
- Return type: static void
- Signature: atcspi_dma_callback(void * arg)
- Line: 298

### atcspi_dma_config
- Return type: static int
- Signature: atcspi_dma_config(struct atcspi_dev * spi,bool is_rx)
- Line: 270

### atcspi_dma_trans
- Return type: static int
- Signature: atcspi_dma_trans(struct atcspi_dev * spi,const struct spi_mem_op * op)
- Line: 305

### atcspi_enable_clk
- Return type: static int
- Signature: atcspi_enable_clk(struct atcspi_dev * spi)
- Line: 516

### atcspi_exec_mem_op
- Return type: static int
- Signature: atcspi_exec_mem_op(struct spi_mem * mem,const struct spi_mem_op * op)
- Line: 364

### atcspi_init_controller
- Return type: static void
- Signature: atcspi_init_controller(struct platform_device * pdev,struct atcspi_dev * spi,struct spi_controller * host,struct resource * mem_res)
- Line: 530

### atcspi_init_resources
- Return type: static int
- Signature: atcspi_init_resources(struct platform_device * pdev,struct atcspi_dev * spi,struct resource ** mem_res)
- Line: 471

### atcspi_prepare_trans
- Return type: static void
- Signature: atcspi_prepare_trans(struct atcspi_dev * spi,const struct spi_mem_op * op)
- Line: 246

### atcspi_probe
- Return type: static int
- Signature: atcspi_probe(struct platform_device * pdev)
- Line: 546

### atcspi_resume
- Return type: static int
- Signature: atcspi_resume(struct device * dev)
- Line: 614

### atcspi_set_trans_ctl
- Return type: static void
- Signature: atcspi_set_trans_ctl(struct atcspi_dev * spi,const struct spi_mem_op * op)
- Line: 186

### atcspi_set_trans_fmt
- Return type: static void
- Signature: atcspi_set_trans_fmt(struct atcspi_dev * spi,const struct spi_mem_op * op)
- Line: 224

### atcspi_setup
- Return type: static int
- Signature: atcspi_setup(struct atcspi_dev * spi)
- Line: 405

### atcspi_suspend
- Return type: static int
- Signature: atcspi_suspend(struct device * dev)
- Line: 602

### atcspi_wait_fifo_ready
- Return type: static int
- Signature: atcspi_wait_fifo_ready(struct atcspi_dev * spi,enum spi_mem_data_dir dir)
- Line: 125

### atcspi_xfer_data_poll
- Return type: static int
- Signature: atcspi_xfer_data_poll(struct atcspi_dev * spi,const struct spi_mem_op * op)
- Line: 145

## Structs (1)

### atcspi_dev
- Line: 109
- Members:
  - host: spi_controller *
  - mutex_lock: mutex
  - dma_completion: completion
  - dev: device *
  - regmap: regmap *
  - clk: clk *
  - dma_addr: dma_addr_t
  - clk_rate: unsigned int
  - sclk_rate: unsigned int
  - txfifo_size: unsigned int
  - rxfifo_size: unsigned int
  - data_merge: bool
  - use_dma: bool

## Variables (3)

- static **atcspi_driver** : platform_driver (line 650)
- static **atcspi_mem_ops** : const struct spi_controller_mem_ops (line 400)
- static **atcspi_of_match** : const struct of_device_id[] (line 642)

## Macros (50)

- **ATCSPI_ACTIVE** (line 68)
- **ATCSPI_ADDR** (line 29)
- **ATCSPI_BITS_PER_UINT** (line 87)
- **ATCSPI_CMD** (line 28)
- **ATCSPI_CONFIG** (line 34)
- **ATCSPI_CTRL** (line 31)
- **ATCSPI_DATA** (line 30)
- **ATCSPI_DATA_MERGE_EN** (line 88)
- **ATCSPI_DMA_SUPPORT** (line 89)
- **ATCSPI_DMA_THRESHOLD** (line 86)
- **ATCSPI_MAX_CS_NUM** (line 85)
- **ATCSPI_MAX_SPEED_HZ** (line 82)
- **ATCSPI_MAX_TRANS_LEN** (line 81)
- **ATCSPI_RDY_TIMEOUT_US** (line 83)
- **ATCSPI_RX_EMPTY** (line 69)
- **ATCSPI_STATUS** (line 32)
- **ATCSPI_TIMING** (line 33)
- **ATCSPI_TRANS_CTRL** (line 27)
- **ATCSPI_TRANS_FMT** (line 26)
- **ATCSPI_TX_FULL** (line 70)
- **ATCSPI_XFER_TIMEOUT**(n) (line 84)
- **CTRL_RX_DMA_EN** (line 64)
- **CTRL_RX_FIFO_RST** (line 62)
- **CTRL_SPI_RST** (line 61)
- **CTRL_TX_DMA_EN** (line 65)
- **CTRL_TX_FIFO_RST** (line 63)
- **RXFIFO_SIZE**(x) (line 77)
- **TIMING_SCLK_DIV_MASK** (line 73)
- **TIMING_SCLK_DIV_MAX** (line 74)
- **TRANS_ADDR_EN** (line 57)
- **TRANS_ADDR_FMT** (line 56)
- **TRANS_CMD_EN** (line 58)
- **TRANS_DUAL_QUAD**(x) (line 55)
- **TRANS_DUMMY_CNT**(x) (line 53)
- **TRANS_FIELD_DECNZ**(m,x) (line 51)
- **TRANS_FMT_ADDR_LEN**(x) (line 43)
- **TRANS_FMT_ADDR_LEN_MASK** (line 41)
- **TRANS_FMT_CPHA** (line 37)
- **TRANS_FMT_CPOL** (line 38)
- **TRANS_FMT_DATA_LEN**(x) (line 42)
- **TRANS_FMT_DATA_LEN_MASK** (line 40)
- **TRANS_FMT_DATA_MERGE_EN** (line 39)
- **TRANS_MODE_DMY_READ** (line 50)
- **TRANS_MODE_MASK** (line 46)
- **TRANS_MODE_NONE_DATA** (line 49)
- **TRANS_MODE_R_ONLY** (line 48)
- **TRANS_MODE_W_ONLY** (line 47)
- **TRANS_RD_TRANS_CNT**(x) (line 52)
- **TRANS_WR_TRANS_CNT**(x) (line 54)
- **TXFIFO_SIZE**(x) (line 78)
