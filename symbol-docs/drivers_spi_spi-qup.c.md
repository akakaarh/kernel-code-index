# drivers/spi/spi-qup.c

Subsystem: drivers/spi

## Functions (31)

### spi_qup_can_dma
- Return type: static bool
- Signature: spi_qup_can_dma(struct spi_controller * host,struct spi_device * spi,struct spi_transfer * xfer)
- Line: 915

### spi_qup_data_pending
- Return type: static bool
- Signature: spi_qup_data_pending(struct spi_qup * controller)
- Line: 609

### spi_qup_dma_done
- Return type: static void
- Signature: spi_qup_dma_done(void * data)
- Line: 365

### spi_qup_dma_terminate
- Return type: static void
- Signature: spi_qup_dma_terminate(struct spi_controller * host,struct spi_transfer * xfer)
- Line: 440

### spi_qup_do_dma
- Return type: static int
- Signature: spi_qup_do_dma(struct spi_device * spi,struct spi_transfer * xfer,unsigned long timeout)
- Line: 469

### spi_qup_do_pio
- Return type: static int
- Signature: spi_qup_do_pio(struct spi_device * spi,struct spi_transfer * xfer,unsigned long timeout)
- Line: 544

### spi_qup_init_dma
- Return type: static int
- Signature: spi_qup_init_dma(struct spi_controller * host,resource_size_t base)
- Line: 953

### spi_qup_io_config
- Return type: static int
- Signature: spi_qup_io_config(struct spi_device * spi,struct spi_transfer * xfer)
- Line: 722

### spi_qup_io_prep
- Return type: static int
- Signature: spi_qup_io_prep(struct spi_device * spi,struct spi_transfer * xfer)
- Line: 690

### spi_qup_is_dma_xfer
- Return type: static bool
- Signature: spi_qup_is_dma_xfer(int mode)
- Line: 170

### spi_qup_is_flag_set
- Return type: static bool
- Signature: spi_qup_is_flag_set(struct spi_qup * controller,u32 flag)
- Line: 163

### spi_qup_is_valid_state
- Return type: static bool
- Signature: spi_qup_is_valid_state(struct spi_qup * controller)
- Line: 184

### spi_qup_len
- Return type: static unsigned int
- Signature: spi_qup_len(struct spi_qup * controller)
- Line: 179

### spi_qup_pm_resume_runtime
- Return type: static int
- Signature: spi_qup_pm_resume_runtime(struct device * device)
- Line: 1236

### spi_qup_pm_suspend_runtime
- Return type: static int
- Signature: spi_qup_pm_suspend_runtime(struct device * device)
- Line: 1218

### spi_qup_prep_sg
- Return type: static int
- Signature: spi_qup_prep_sg(struct spi_controller * host,struct scatterlist * sgl,unsigned int nents,enum dma_transfer_direction dir,dma_async_tx_callback callback)
- Line: 413

### spi_qup_probe
- Return type: static int
- Signature: spi_qup_probe(struct platform_device * pdev)
- Line: 1025

### spi_qup_qup_irq
- Return type: static irqreturn_t
- Signature: spi_qup_qup_irq(int irq,void * dev_id)
- Line: 622

### spi_qup_read
- Return type: static void
- Signature: spi_qup_read(struct spi_qup * controller,u32 * opflags)
- Line: 286

### spi_qup_read_from_fifo
- Return type: static void
- Signature: spi_qup_read_from_fifo(struct spi_qup * controller,u32 num_words)
- Line: 253

### spi_qup_release_dma
- Return type: static void
- Signature: spi_qup_release_dma(struct spi_controller * host)
- Line: 945

### spi_qup_remove
- Return type: static void
- Signature: spi_qup_remove(struct platform_device * pdev)
- Line: 1320

### spi_qup_resume
- Return type: static int
- Signature: spi_qup_resume(struct device * device)
- Line: 1287

### spi_qup_set_cs
- Return type: static void
- Signature: spi_qup_set_cs(struct spi_device * spi,bool val)
- Line: 1007

### spi_qup_set_state
- Return type: static int
- Signature: spi_qup_set_state(struct spi_qup * controller,u32 state)
- Line: 208

### spi_qup_sgl_get_nents_len
- Return type: static u32
- Signature: spi_qup_sgl_get_nents_len(struct scatterlist * sgl,u32 max,u32 * nents)
- Line: 449

### spi_qup_suspend
- Return type: static int
- Signature: spi_qup_suspend(struct device * device)
- Line: 1262

### spi_qup_transfer_one
- Return type: static int
- Signature: spi_qup_transfer_one(struct spi_controller * host,struct spi_device * spi,struct spi_transfer * xfer)
- Line: 872

### spi_qup_vote_bw
- Return type: static int
- Signature: spi_qup_vote_bw(struct spi_qup * controller,u32 speed_hz)
- Line: 191

### spi_qup_write
- Return type: static void
- Signature: spi_qup_write(struct spi_qup * controller)
- Line: 372

### spi_qup_write_to_fifo
- Return type: static void
- Signature: spi_qup_write_to_fifo(struct spi_qup * controller,u32 num_words)
- Line: 341

## Structs (1)

### spi_qup
- Line: 129
- Members:
  - base: void __iomem *
  - dev: device *
  - cclk: clk *
  - iclk: clk *
  - icc_path: icc_path *
  - irq: int
  - lock: spinlock_t
  - in_fifo_sz: int
  - out_fifo_sz: int
  - in_blk_sz: int
  - out_blk_sz: int
  - xfer: spi_transfer *
  - done: completion
  - error: int
  - w_size: int
  - n_words: int
  - tx_bytes: int
  - rx_bytes: int
  - tx_buf: const u8 *
  - rx_buf: u8 *
  - qup_v1: int
  - mode: int
  - rx_conf: dma_slave_config
  - tx_conf: dma_slave_config
  - bw_speed_hz: u32

## Variables (3)

- static **spi_qup_dev_pm_ops** : const struct dev_pm_ops (line 1361)
- static **spi_qup_driver** : platform_driver (line 1368)
- static **spi_qup_dt_match** : const struct of_device_id[] (line 1353)

## Macros (79)

- **QUP_CONFIG** (line 23)
- **QUP_CONFIG_CLOCK_AUTO_GATE** (line 46)
- **QUP_CONFIG_N** (line 49)
- **QUP_CONFIG_NO_INPUT** (line 47)
- **QUP_CONFIG_NO_OUTPUT** (line 48)
- **QUP_CONFIG_SPI_MODE** (line 45)
- **QUP_ERROR_FLAGS** (line 28)
- **QUP_ERROR_FLAGS_EN** (line 29)
- **QUP_ERROR_INPUT_OVER_RUN** (line 95)
- **QUP_ERROR_INPUT_UNDER_RUN** (line 93)
- **QUP_ERROR_OUTPUT_OVER_RUN** (line 92)
- **QUP_ERROR_OUTPUT_UNDER_RUN** (line 94)
- **QUP_HW_VERSION** (line 31)
- **QUP_HW_VERSION_2_1_1** (line 59)
- **QUP_INPUT_FIFO** (line 37)
- **QUP_IO_M_INPUT_BLOCK_SIZE**(x) (line 71)
- **QUP_IO_M_INPUT_FIFO_SIZE**(x) (line 72)
- **QUP_IO_M_INPUT_MODE_MASK** (line 66)
- **QUP_IO_M_INPUT_MODE_MASK_SHIFT** (line 64)
- **QUP_IO_M_MODES** (line 25)
- **QUP_IO_M_MODE_BAM** (line 77)
- **QUP_IO_M_MODE_BLOCK** (line 75)
- **QUP_IO_M_MODE_DMOV** (line 76)
- **QUP_IO_M_MODE_FIFO** (line 74)
- **QUP_IO_M_OUTPUT_BLOCK_SIZE**(x) (line 69)
- **QUP_IO_M_OUTPUT_FIFO_SIZE**(x) (line 70)
- **QUP_IO_M_OUTPUT_MODE_MASK** (line 67)
- **QUP_IO_M_OUTPUT_MODE_MASK_SHIFT** (line 65)
- **QUP_IO_M_PACK_EN** (line 62)
- **QUP_IO_M_UNPACK_EN** (line 63)
- **QUP_MX_INPUT_CNT** (line 35)
- **QUP_MX_OUTPUT_CNT** (line 32)
- **QUP_MX_READ_CNT** (line 36)
- **QUP_MX_WRITE_CNT** (line 34)
- **QUP_OPERATIONAL** (line 27)
- **QUP_OPERATIONAL_MASK** (line 30)
- **QUP_OP_IN_BLOCK_READ_REQ** (line 80)
- **QUP_OP_IN_FIFO_FULL** (line 86)
- **QUP_OP_IN_FIFO_NOT_EMPTY** (line 88)
- **QUP_OP_IN_SERVICE_FLAG** (line 84)
- **QUP_OP_MAX_INPUT_DONE_FLAG** (line 82)
- **QUP_OP_MAX_OUTPUT_DONE_FLAG** (line 83)
- **QUP_OP_OUT_BLOCK_WRITE_REQ** (line 81)
- **QUP_OP_OUT_FIFO_FULL** (line 87)
- **QUP_OP_OUT_FIFO_NOT_EMPTY** (line 89)
- **QUP_OP_OUT_SERVICE_FLAG** (line 85)
- **QUP_OUTPUT_FIFO** (line 33)
- **QUP_STATE** (line 24)
- **QUP_STATE_CLEAR** (line 57)
- **QUP_STATE_MASK** (line 56)
- **QUP_STATE_PAUSE** (line 55)
- **QUP_STATE_RESET** (line 53)
- **QUP_STATE_RUN** (line 54)
- **QUP_STATE_VALID** (line 52)
- **QUP_SW_RESET** (line 26)
- **SPI_BUS_WIDTH** (line 127)
- **SPI_CONFIG** (line 39)
- **SPI_CONFIG_HS_MODE** (line 98)
- **SPI_CONFIG_INPUT_FIRST** (line 99)
- **SPI_CONFIG_LOOPBACK** (line 100)
- **SPI_DELAY_RETRY** (line 125)
- **SPI_DELAY_THRESHOLD** (line 124)
- **SPI_ERROR_CLK_OVER_RUN** (line 113)
- **SPI_ERROR_CLK_UNDER_RUN** (line 114)
- **SPI_ERROR_FLAGS** (line 41)
- **SPI_ERROR_FLAGS_EN** (line 42)
- **SPI_HS_MIN_RATE** (line 121)
- **SPI_IO_CONTROL** (line 40)
- **SPI_IO_C_CLK_IDLE_HIGH** (line 104)
- **SPI_IO_C_CS_N_POLARITY_0** (line 106)
- **SPI_IO_C_CS_SELECT**(x) (line 107)
- **SPI_IO_C_CS_SELECT_MASK** (line 108)
- **SPI_IO_C_FORCE_CS** (line 103)
- **SPI_IO_C_MX_CS_MODE** (line 105)
- **SPI_IO_C_NO_TRI_STATE** (line 110)
- **SPI_IO_C_TRISTATE_CS** (line 109)
- **SPI_MAX_RATE** (line 122)
- **SPI_MAX_XFER** (line 118)
- **SPI_NUM_CHIPSELECTS** (line 116)
