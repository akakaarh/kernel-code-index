# drivers/spi/spi-geni-qcom.c

Subsystem: drivers/spi

## Functions (29)

### geni_byte_per_fifo_word
- Return type: static unsigned int
- Signature: geni_byte_per_fifo_word(struct spi_geni_master * mas)
- Line: 687

### geni_can_dma
- Return type: static bool
- Signature: geni_can_dma(struct spi_controller * ctlr,struct spi_device * slv,struct spi_transfer * xfer)
- Line: 498

### geni_spi_handle_rx
- Return type: static void
- Signature: geni_spi_handle_rx(struct spi_geni_master * mas)
- Line: 739

### geni_spi_handle_tx
- Return type: static bool
- Signature: geni_spi_handle_tx(struct spi_geni_master * mas)
- Line: 701

### geni_spi_isr
- Return type: static irqreturn_t
- Signature: geni_spi_isr(int irq,void * data)
- Line: 904

### geni_spi_set_clock_and_bw
- Return type: static int
- Signature: geni_spi_set_clock_and_bw(struct spi_geni_master * mas,unsigned long clk_hz)
- Line: 305

### get_spi_clk_cfg
- Return type: static int
- Signature: get_spi_clk_cfg(unsigned int speed_hz,struct spi_geni_master * mas,unsigned int * clk_idx,unsigned int * clk_div)
- Line: 117

### get_xfer_len_in_words
- Return type: static u32
- Signature: get_xfer_len_in_words(struct spi_transfer * xfer,struct spi_geni_master * mas)
- Line: 484

### handle_gpi_timeout
- Return type: static void
- Signature: handle_gpi_timeout(struct spi_controller * spi)
- Line: 224

### handle_se_timeout
- Return type: static void
- Signature: handle_se_timeout(struct spi_controller * spi)
- Line: 149

### setup_fifo_params
- Return type: static int
- Signature: setup_fifo_params(struct spi_device * spi_slv,struct spi_controller * spi)
- Line: 344

### setup_gsi_xfer
- Return type: static int
- Signature: setup_gsi_xfer(struct spi_transfer * xfer,struct spi_geni_master * mas,struct spi_device * spi_slv,struct spi_controller * spi)
- Line: 394

### setup_se_xfer
- Return type: static int
- Signature: setup_se_xfer(struct spi_transfer * xfer,struct spi_geni_master * mas,u16 mode,struct spi_controller * spi)
- Line: 783

### spi_geni_grab_gpi_chan
- Return type: static int
- Signature: spi_geni_grab_gpi_chan(struct spi_geni_master * mas)
- Line: 560

### spi_geni_handle_err
- Return type: static void
- Signature: spi_geni_handle_err(struct spi_controller * spi,struct spi_message * msg)
- Line: 232

### spi_geni_init
- Return type: static int
- Signature: spi_geni_init(struct spi_geni_master * mas)
- Line: 594

### spi_geni_is_abort_still_pending
- Return type: static bool
- Signature: spi_geni_is_abort_still_pending(struct spi_geni_master * mas)
- Line: 249

### spi_geni_prepare_message
- Return type: static int
- Signature: spi_geni_prepare_message(struct spi_controller * spi,struct spi_message * spi_msg)
- Line: 520

### spi_geni_probe
- Return type: static int
- Signature: spi_geni_probe(struct platform_device * pdev)
- Line: 1018

### spi_geni_release_dma_chan
- Return type: static void
- Signature: spi_geni_release_dma_chan(void * data)
- Line: 545

### spi_geni_resume
- Return type: static int __maybe_unused
- Signature: spi_geni_resume(struct device * dev)
- Line: 1178

### spi_geni_runtime_resume
- Return type: static int __maybe_unused
- Signature: spi_geni_runtime_resume(struct device * dev)
- Line: 1145

### spi_geni_runtime_suspend
- Return type: static int __maybe_unused
- Signature: spi_geni_runtime_suspend(struct device * dev)
- Line: 1129

### spi_geni_suspend
- Return type: static int __maybe_unused
- Signature: spi_geni_suspend(struct device * dev)
- Line: 1162

### spi_geni_target_abort
- Return type: static int
- Signature: spi_geni_target_abort(struct spi_controller * spi)
- Line: 1007

### spi_geni_transfer_one
- Return type: static int
- Signature: spi_geni_transfer_one(struct spi_controller * spi,struct spi_device * slv,struct spi_transfer * xfer)
- Line: 880

### spi_gsi_callback_result
- Return type: static void
- Signature: spi_gsi_callback_result(void * cb,const struct dmaengine_result * result)
- Line: 373

### spi_setup_word_len
- Return type: static void
- Signature: spi_setup_word_len(struct spi_geni_master * mas,u16 mode,unsigned int bits_per_word)
- Line: 283

### spi_slv_setup
- Return type: static void
- Signature: spi_slv_setup(struct spi_geni_master * mas)
- Line: 107

## Structs (1)

### spi_geni_master
- Line: 78
- Members:
  - se: geni_se
  - dev: device *
  - tx_fifo_depth: u32
  - fifo_width_bits: u32
  - tx_wm: u32
  - last_mode: u32
  - last_cs: u8
  - cur_speed_hz: unsigned long
  - cur_sclk_hz: unsigned long
  - cur_bits_per_word: unsigned int
  - tx_rem_bytes: unsigned int
  - rx_rem_bytes: unsigned int
  - cur_xfer: const struct spi_transfer *
  - cs_done: completion
  - cancel_done: completion
  - abort_done: completion
  - tx_reset_done: completion
  - rx_reset_done: completion
  - oversampling: unsigned int
  - lock: spinlock_t
  - irq: int
  - cs_flag: bool
  - abort_failed: bool
  - tx: dma_chan *
  - rx: dma_chan *
  - cur_xfer_mode: int

## Variables (3)

- static **spi_geni_driver** : platform_driver (line 1206)
- static **spi_geni_dt_match** : const struct of_device_id[] (line 1200)
- static **spi_geni_pm_ops** : const struct dev_pm_ops (line 1194)

## Macros (42)

- **CPHA** (line 22)
- **CPOL** (line 30)
- **CS_DEMUX_OUTPUT_INV_MSK** (line 33)
- **CS_DEMUX_OUTPUT_SEL** (line 36)
- **CS_TOGGLE** (line 39)
- **FRAGMENTATION** (line 69)
- **GSI_CPHA** (line 75)
- **GSI_CPOL** (line 76)
- **GSI_CS_TOGGLE** (line 74)
- **GSI_LOOPBACK_EN** (line 73)
- **LOOPBACK_ENABLE** (line 25)
- **LOOPBACK_MSK** (line 27)
- **MIN_WORD_LEN** (line 43)
- **NORMAL_MODE** (line 26)
- **POST_CMD_DELAY** (line 71)
- **SE_SPI_CPHA** (line 21)
- **SE_SPI_CPOL** (line 29)
- **SE_SPI_DELAY_COUNTERS** (line 51)
- **SE_SPI_DEMUX_OUTPUT_INV** (line 32)
- **SE_SPI_DEMUX_SEL** (line 35)
- **SE_SPI_LOOPBACK** (line 24)
- **SE_SPI_PRE_POST_CMD_DLY** (line 49)
- **SE_SPI_RX_TRANS_LEN** (line 46)
- **SE_SPI_SLAVE_EN** (line 56)
- **SE_SPI_TRANS_CFG** (line 38)
- **SE_SPI_TX_TRANS_LEN** (line 45)
- **SE_SPI_WORD_LEN** (line 41)
- **SPI_CS_ASSERT** (line 63)
- **SPI_CS_CLK_DELAY_MSK** (line 53)
- **SPI_CS_CLK_DELAY_SHFT** (line 54)
- **SPI_CS_DEASSERT** (line 64)
- **SPI_INTER_WORDS_DELAY_MSK** (line 52)
- **SPI_PRE_CMD_DELAY** (line 67)
- **SPI_RX_ONLY** (line 61)
- **SPI_SCK_ONLY** (line 65)
- **SPI_SLAVE_EN** (line 57)
- **SPI_TX_ONLY** (line 60)
- **SPI_TX_RX** (line 62)
- **TIMESTAMP_AFTER** (line 70)
- **TIMESTAMP_BEFORE** (line 68)
- **TRANS_LEN_MSK** (line 47)
- **WORD_LEN_MSK** (line 42)
