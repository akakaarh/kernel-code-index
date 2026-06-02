# drivers/spi/spi-davinci.c

Subsystem: drivers/spi

## Functions (25)

### clear_io_bits
- Return type: static void
- Signature: clear_io_bits(void __iomem * addr,u32 bits)
- Line: 246

### davinci_spi_bufs
- Return type: static int
- Signature: davinci_spi_bufs(struct spi_device * spi,struct spi_transfer * t)
- Line: 625

### davinci_spi_can_dma
- Return type: static bool
- Signature: davinci_spi_can_dma(struct spi_controller * host,struct spi_device * spi,struct spi_transfer * xfer)
- Line: 504

### davinci_spi_check_error
- Return type: static int
- Signature: davinci_spi_check_error(struct davinci_spi * dspi,int int_status)
- Line: 520

### davinci_spi_chipselect
- Return type: static void
- Signature: davinci_spi_chipselect(struct spi_device * spi,int value)
- Line: 257

### davinci_spi_cleanup
- Return type: static void
- Signature: davinci_spi_cleanup(struct spi_device * spi)
- Line: 495

### davinci_spi_dma_rx_callback
- Return type: static void
- Signature: davinci_spi_dma_rx_callback(void * data)
- Line: 596

### davinci_spi_dma_tx_callback
- Return type: static void
- Signature: davinci_spi_dma_tx_callback(void * data)
- Line: 606

### davinci_spi_get_prescale
- Return type: static int
- Signature: davinci_spi_get_prescale(struct davinci_spi * dspi,u32 max_speed_hz)
- Line: 301

### davinci_spi_irq
- Return type: static irqreturn_t
- Signature: davinci_spi_irq(s32 irq,void * data)
- Line: 794

### davinci_spi_of_setup
- Return type: static int
- Signature: davinci_spi_of_setup(struct spi_device * spi)
- Line: 438

### davinci_spi_probe
- Return type: static int
- Signature: davinci_spi_probe(struct platform_device * pdev)
- Line: 922

### davinci_spi_process_events
- Return type: static int
- Signature: davinci_spi_process_events(struct davinci_spi * dspi)
- Line: 566

### davinci_spi_remove
- Return type: static void
- Signature: davinci_spi_remove(struct platform_device * pdev)
- Line: 1074

### davinci_spi_request_dma
- Return type: static int
- Signature: davinci_spi_request_dma(struct davinci_spi * dspi)
- Line: 809

### davinci_spi_rx_buf_u16
- Return type: static void
- Signature: davinci_spi_rx_buf_u16(u32 data,struct davinci_spi * dspi)
- Line: 203

### davinci_spi_rx_buf_u8
- Return type: static void
- Signature: davinci_spi_rx_buf_u8(u32 data,struct davinci_spi * dspi)
- Line: 194

### davinci_spi_setup
- Return type: static int
- Signature: davinci_spi_setup(struct spi_device * spi)
- Line: 468

### davinci_spi_setup_transfer
- Return type: static int
- Signature: davinci_spi_setup_transfer(struct spi_device * spi,struct spi_transfer * t)
- Line: 324

### davinci_spi_tx_buf_u16
- Return type: static u32
- Signature: davinci_spi_tx_buf_u16(struct davinci_spi * dspi)
- Line: 225

### davinci_spi_tx_buf_u8
- Return type: static u32
- Signature: davinci_spi_tx_buf_u8(struct davinci_spi * dspi)
- Line: 212

### dummy_thread_fn
- Return type: static irqreturn_t
- Signature: dummy_thread_fn(s32 irq,void * data)
- Line: 778

### set_io_bits
- Return type: static void
- Signature: set_io_bits(void __iomem * addr,u32 bits)
- Line: 238

### spi_davinci_get_pdata
- Return type: static int
- Signature: spi_davinci_get_pdata(struct platform_device * pdev,struct davinci_spi * dspi)
- Line: 875

### spi_davinci_get_pdata
- Return type: static int
- Signature: spi_davinci_get_pdata(struct platform_device * pdev,struct davinci_spi * dspi)
- Line: 904

## Structs (4)

### davinci_spi
- Line: 164
- Members:
  - version: u8
  - num_chipselect: u8
  - intr_line: u8
  - prescaler_limit: u8
  - cshold_bug: bool
  - dma_event_q: dma_event_q
  - wdelay: u8
  - odd_parity: u8
  - parity_enable: u8
  - io_type: u8
  - timer_disable: u8
  - c2tdelay: u8
  - t2cdelay: u8
  - t2edelay: u8
  - c2edelay: u8
  - bitbang: spi_bitbang
  - clk: clk *
  - version: u8
  - pbase: resource_size_t
  - base: void __iomem *
  - irq: u32
  - done: completion
  - tx: const void *
  - rx: void *
  - rcount: int
  - wcount: int
  - dma_rx: dma_chan *
  - dma_tx: dma_chan *
  - pdata: davinci_spi_platform_data
  - get_rx: void (*)(u32 rx_data,struct davinci_spi *)
  - get_tx: u32 (*)(struct davinci_spi *)
  - bytes_per_word: u8 *
  - prescaler_limit: u8
  - version: u8
  - prescaler_limit: u8

### davinci_spi_config
- Line: 151
- Members:
  - version: u8
  - num_chipselect: u8
  - intr_line: u8
  - prescaler_limit: u8
  - cshold_bug: bool
  - dma_event_q: dma_event_q
  - wdelay: u8
  - odd_parity: u8
  - parity_enable: u8
  - io_type: u8
  - timer_disable: u8
  - c2tdelay: u8
  - t2cdelay: u8
  - t2edelay: u8
  - c2edelay: u8
  - bitbang: spi_bitbang
  - clk: clk *
  - version: u8
  - pbase: resource_size_t
  - base: void __iomem *
  - irq: u32
  - done: completion
  - tx: const void *
  - rx: void *
  - rcount: int
  - wcount: int
  - dma_rx: dma_chan *
  - dma_tx: dma_chan *
  - pdata: davinci_spi_platform_data
  - get_rx: void (*)(u32 rx_data,struct davinci_spi *)
  - get_tx: u32 (*)(struct davinci_spi *)
  - bytes_per_word: u8 *
  - prescaler_limit: u8
  - version: u8
  - prescaler_limit: u8

### davinci_spi_of_data
- Line: 829
- Members:
  - version: u8
  - num_chipselect: u8
  - intr_line: u8
  - prescaler_limit: u8
  - cshold_bug: bool
  - dma_event_q: dma_event_q
  - wdelay: u8
  - odd_parity: u8
  - parity_enable: u8
  - io_type: u8
  - timer_disable: u8
  - c2tdelay: u8
  - t2cdelay: u8
  - t2edelay: u8
  - c2edelay: u8
  - bitbang: spi_bitbang
  - clk: clk *
  - version: u8
  - pbase: resource_size_t
  - base: void __iomem *
  - irq: u32
  - done: completion
  - tx: const void *
  - rx: void *
  - rcount: int
  - wcount: int
  - dma_rx: dma_chan *
  - dma_tx: dma_chan *
  - pdata: davinci_spi_platform_data
  - get_rx: void (*)(u32 rx_data,struct davinci_spi *)
  - get_tx: u32 (*)(struct davinci_spi *)
  - bytes_per_word: u8 *
  - prescaler_limit: u8
  - version: u8
  - prescaler_limit: u8

### davinci_spi_platform_data
- Line: 124
- Members:
  - version: u8
  - num_chipselect: u8
  - intr_line: u8
  - prescaler_limit: u8
  - cshold_bug: bool
  - dma_event_q: dma_event_q
  - wdelay: u8
  - odd_parity: u8
  - parity_enable: u8
  - io_type: u8
  - timer_disable: u8
  - c2tdelay: u8
  - t2cdelay: u8
  - t2edelay: u8
  - c2edelay: u8
  - bitbang: spi_bitbang
  - clk: clk *
  - version: u8
  - pbase: resource_size_t
  - base: void __iomem *
  - irq: u32
  - done: completion
  - tx: const void *
  - rx: void *
  - rcount: int
  - wcount: int
  - dma_rx: dma_chan *
  - dma_tx: dma_chan *
  - pdata: davinci_spi_platform_data
  - get_rx: void (*)(u32 rx_data,struct davinci_spi *)
  - get_tx: u32 (*)(struct davinci_spi *)
  - bytes_per_word: u8 *
  - prescaler_limit: u8
  - version: u8
  - prescaler_limit: u8

## Enums (1)

### __anone1c016800103
- Line: 105

## Variables (6)

- static **da830_spi_data** : const struct davinci_spi_of_data (line 839)
- static **davinci_spi_default_cfg** : davinci_spi_config (line 192)
- static **davinci_spi_driver** : platform_driver (line 1095)
- static **davinci_spi_of_match** : const struct of_device_id[] (line 849)
- static **dm6441_spi_data** : const struct davinci_spi_of_data (line 834)
- static **keystone_spi_data** : const struct davinci_spi_of_data (line 844)

## Macros (59)

- **CS_DEFAULT** (line 23)
- **DMA_MIN_BYTES** (line 103)
- **SPIBUF** (line 95)
- **SPIBUF_RXEMPTY_MASK** (line 60)
- **SPIBUF_TXFULL_MASK** (line 59)
- **SPIDAT1** (line 94)
- **SPIDAT1_CSHOLD_MASK** (line 48)
- **SPIDAT1_WDEL** (line 49)
- **SPIDEF** (line 97)
- **SPIDELAY** (line 96)
- **SPIDELAY_C2EDELAY_MASK** (line 70)
- **SPIDELAY_C2EDELAY_SHIFT** (line 69)
- **SPIDELAY_C2TDELAY_MASK** (line 64)
- **SPIDELAY_C2TDELAY_SHIFT** (line 63)
- **SPIDELAY_T2CDELAY_MASK** (line 66)
- **SPIDELAY_T2CDELAY_SHIFT** (line 65)
- **SPIDELAY_T2EDELAY_MASK** (line 68)
- **SPIDELAY_T2EDELAY_SHIFT** (line 67)
- **SPIFLG** (line 92)
- **SPIFLG_BITERR_MASK** (line 77)
- **SPIFLG_BUF_INIT_ACTIVE_MASK** (line 79)
- **SPIFLG_DESYNC_MASK** (line 76)
- **SPIFLG_DLEN_ERR_MASK** (line 73)
- **SPIFLG_ERROR_MASK** (line 80)
- **SPIFLG_OVRRUN_MASK** (line 78)
- **SPIFLG_PARERR_MASK** (line 75)
- **SPIFLG_TIMEOUT_MASK** (line 74)
- **SPIFMT0** (line 98)
- **SPIFMT_DISTIMER_MASK** (line 27)
- **SPIFMT_ODD_PARITY_MASK** (line 31)
- **SPIFMT_PARITYENA_MASK** (line 30)
- **SPIFMT_PHASE_MASK** (line 25)
- **SPIFMT_POLARITY_MASK** (line 26)
- **SPIFMT_PRESCALE_SHIFT** (line 34)
- **SPIFMT_SHIFTDIR_MASK** (line 28)
- **SPIFMT_WAITENA_MASK** (line 29)
- **SPIFMT_WDELAY_MASK** (line 32)
- **SPIFMT_WDELAY_SHIFT** (line 33)
- **SPIGCR0** (line 88)
- **SPIGCR1** (line 89)
- **SPIGCR1_CLKMOD_MASK** (line 52)
- **SPIGCR1_LOOPBACK_MASK** (line 55)
- **SPIGCR1_MASTER_MASK** (line 53)
- **SPIGCR1_POWERDOWN_MASK** (line 54)
- **SPIGCR1_SPIENA_MASK** (line 56)
- **SPIINT** (line 90)
- **SPIINT_DMA_REQ_EN** (line 85)
- **SPIINT_MASKALL** (line 42)
- **SPIINT_MASKINT** (line 43)
- **SPILVL** (line 91)
- **SPIPC0** (line 93)
- **SPIPC0_CLKFUN_MASK** (line 39)
- **SPIPC0_DIFUN_MASK** (line 37)
- **SPIPC0_DOFUN_MASK** (line 38)
- **SPIPC0_SPIENA_MASK** (line 40)
- **SPI_INTLVL_0** (line 45)
- **SPI_INTLVL_1** (line 44)
- **SPI_IO_TYPE_DMA** (line 101)
- **SPI_IO_TYPE_POLL** (line 100)
