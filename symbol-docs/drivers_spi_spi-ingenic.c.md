# drivers/spi/spi-ingenic.c

Subsystem: drivers/spi

## Functions (14)

### spi_ingenic_can_dma
- Return type: static bool
- Signature: spi_ingenic_can_dma(struct spi_controller * ctlr,struct spi_device * spi,struct spi_transfer * xfer)
- Line: 329

### spi_ingenic_dma_tx
- Return type: static int
- Signature: spi_ingenic_dma_tx(struct spi_controller * ctlr,struct spi_transfer * xfer,unsigned int bits)
- Line: 175

### spi_ingenic_finalize_transfer
- Return type: static void
- Signature: spi_ingenic_finalize_transfer(void * controller)
- Line: 116

### spi_ingenic_prepare_dma
- Return type: static dma_async_tx_descriptor *
- Signature: spi_ingenic_prepare_dma(struct spi_controller * ctlr,struct dma_chan * chan,struct sg_table * sg,enum dma_transfer_direction dir,unsigned int bits)
- Line: 122

### spi_ingenic_prepare_hardware
- Return type: static int
- Signature: spi_ingenic_prepare_hardware(struct spi_controller * ctlr)
- Line: 301

### spi_ingenic_prepare_message
- Return type: static int
- Signature: spi_ingenic_prepare_message(struct spi_controller * ctlr,struct spi_message * message)
- Line: 261

### spi_ingenic_prepare_transfer
- Return type: static void
- Signature: spi_ingenic_prepare_transfer(struct ingenic_spi * priv,struct spi_device * spi,struct spi_transfer * xfer)
- Line: 100

### spi_ingenic_probe
- Return type: static int
- Signature: spi_ingenic_probe(struct platform_device * pdev)
- Line: 383

### spi_ingenic_release_dma
- Return type: static void
- Signature: spi_ingenic_release_dma(void * data)
- Line: 366

### spi_ingenic_request_dma
- Return type: static int
- Signature: spi_ingenic_request_dma(struct spi_controller * ctlr,struct device * dev)
- Line: 346

### spi_ingenic_set_cs
- Return type: static void
- Signature: spi_ingenic_set_cs(struct spi_device * spi,bool disable)
- Line: 82

### spi_ingenic_transfer_one
- Return type: static void
- Signature: spi_ingenic_transfer_one(struct spi_controller * ctlr,struct spi_device * spi,struct spi_transfer * xfer)
- Line: 240

### spi_ingenic_unprepare_hardware
- Return type: static int
- Signature: spi_ingenic_unprepare_hardware(struct spi_controller * ctlr)
- Line: 318

### spi_ingenic_wait
- Return type: static int
- Signature: spi_ingenic_wait(struct ingenic_spi * priv,unsigned long mask,bool condition)
- Line: 71

## Structs (2)

### ingenic_spi
- Line: 62
- Members:
  - bits_per_word_mask: u32
  - flen_field: reg_field
  - has_trendian: bool
  - max_speed_hz: unsigned int
  - max_native_cs: unsigned int
  - soc_info: const struct jz_soc_info *
  - clk: clk *
  - mem_res: resource *
  - map: regmap *
  - flen_field: regmap_field *

### jz_soc_info
- Line: 53
- Members:
  - bits_per_word_mask: u32
  - flen_field: reg_field
  - has_trendian: bool
  - max_speed_hz: unsigned int
  - max_native_cs: unsigned int
  - soc_info: const struct jz_soc_info *
  - clk: clk *
  - mem_res: resource *
  - map: regmap *
  - flen_field: regmap_field *

## Variables (7)

- static **jz4750_soc_info** : const struct jz_soc_info (line 462)
- static **jz4780_soc_info** : const struct jz_soc_info (line 471)
- static **spi_ingenic_driver** : platform_driver (line 508)
- static **spi_ingenic_of_match** : const struct of_device_id[] (line 498)
- static **spi_ingenic_regmap_config** : const struct regmap_config (line 376)
- static **x1000_soc_info** : const struct jz_soc_info (line 480)
- static **x2000_soc_info** : const struct jz_soc_info (line 489)

## Macros (28)

- **REG_SSICR0** (line 22)
- **REG_SSICR0_EACLRUN** (line 31)
- **REG_SSICR0_FSEL** (line 32)
- **REG_SSICR0_LOOP** (line 30)
- **REG_SSICR0_RENDIAN_LSB** (line 28)
- **REG_SSICR0_RFLUSH** (line 34)
- **REG_SSICR0_SSIE** (line 29)
- **REG_SSICR0_TENDIAN_LSB** (line 27)
- **REG_SSICR0_TFLUSH** (line 33)
- **REG_SSICR1** (line 23)
- **REG_SSICR1_FRMHL** (line 37)
- **REG_SSICR1_FRMHL_MASK** (line 36)
- **REG_SSICR1_LFST** (line 38)
- **REG_SSICR1_PHA** (line 40)
- **REG_SSICR1_POL** (line 41)
- **REG_SSICR1_UNFIN** (line 39)
- **REG_SSIDR** (line 21)
- **REG_SSIGR** (line 25)
- **REG_SSISR** (line 24)
- **REG_SSISR_BUSY** (line 44)
- **REG_SSISR_END** (line 43)
- **REG_SSISR_OVER** (line 49)
- **REG_SSISR_RFE** (line 46)
- **REG_SSISR_RFHF** (line 47)
- **REG_SSISR_TFF** (line 45)
- **REG_SSISR_UNDR** (line 48)
- **SPI_INGENIC_FIFO_SIZE** (line 51)
- **SPI_INGENIC_TX**(x) (line 199)
