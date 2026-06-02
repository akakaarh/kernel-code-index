# drivers/spi/spi-bitbang.c

Subsystem: drivers/spi

## Functions (14)

### bitbang_txrx_16
- Return type: static unsigned int
- Signature: bitbang_txrx_16(struct spi_device * spi,spi_bb_txrx_word_fn txrx_word,unsigned int ns,struct spi_transfer * t,unsigned int flags)
- Line: 82

### bitbang_txrx_32
- Return type: static unsigned int
- Signature: bitbang_txrx_32(struct spi_device * spi,spi_bb_txrx_word_fn txrx_word,unsigned int ns,struct spi_transfer * t,unsigned int flags)
- Line: 113

### bitbang_txrx_8
- Return type: static unsigned int
- Signature: bitbang_txrx_8(struct spi_device * spi,spi_bb_txrx_word_fn txrx_word,unsigned int ns,struct spi_transfer * t,unsigned int flags)
- Line: 51

### spi_bitbang_bufs
- Return type: static int
- Signature: spi_bitbang_bufs(struct spi_device * spi,struct spi_transfer * t)
- Line: 239

### spi_bitbang_cleanup
- Return type: void
- Signature: spi_bitbang_cleanup(struct spi_device * spi)
- Line: 233

### spi_bitbang_init
- Return type: int
- Signature: spi_bitbang_init(struct spi_bitbang * bitbang)
- Line: 348

### spi_bitbang_prepare_hardware
- Return type: static int
- Signature: spi_bitbang_prepare_hardware(struct spi_controller * spi)
- Line: 277

### spi_bitbang_set_cs
- Return type: static void
- Signature: spi_bitbang_set_cs(struct spi_device * spi,bool enable)
- Line: 330

### spi_bitbang_setup
- Return type: int
- Signature: spi_bitbang_setup(struct spi_device * spi)
- Line: 186

### spi_bitbang_setup_transfer
- Return type: int
- Signature: spi_bitbang_setup_transfer(struct spi_device * spi,struct spi_transfer * t)
- Line: 144

### spi_bitbang_start
- Return type: int
- Signature: spi_bitbang_start(struct spi_bitbang * bitbang)
- Line: 429

### spi_bitbang_stop
- Return type: void
- Signature: spi_bitbang_stop(struct spi_bitbang * bitbang)
- Line: 452

### spi_bitbang_transfer_one
- Return type: static int
- Signature: spi_bitbang_transfer_one(struct spi_controller * ctlr,struct spi_device * spi,struct spi_transfer * transfer)
- Line: 290

### spi_bitbang_unprepare_hardware
- Return type: static int
- Signature: spi_bitbang_unprepare_hardware(struct spi_controller * spi)
- Line: 317

## Structs (1)

### spi_bitbang_cs
- Line: 45
- Members:
  - nsecs: unsigned int
  - txrx_word: spi_bb_txrx_word_fn
  - txrx_bufs: spi_bb_txrx_bufs_fn

## Typedefs (1)

- **spi_bb_txrx_bufs_fn** → unsigned int (*)(struct spi_device *,spi_bb_txrx_word_fn,unsigned int,struct spi_transfer *,unsigned int) (line 41)

## Macros (1)

- **SPI_BITBANG_CS_DELAY** (line 19)
