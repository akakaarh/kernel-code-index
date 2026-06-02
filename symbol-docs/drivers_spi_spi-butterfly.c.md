# drivers/spi/spi-butterfly.c

Subsystem: drivers/spi

## Functions (8)

### butterfly_attach
- Return type: static void
- Signature: butterfly_attach(struct parport * p)
- Line: 176

### butterfly_chipselect
- Return type: static void
- Signature: butterfly_chipselect(struct spi_device * spi,int value)
- Line: 111

### butterfly_detach
- Return type: static void
- Signature: butterfly_detach(struct parport * p)
- Line: 288

### butterfly_txrx_word_mode0
- Return type: static u32
- Signature: butterfly_txrx_word_mode0(struct spi_device * spi,unsigned nsecs,u32 word,u8 bits,unsigned flags)
- Line: 137

### getmiso
- Return type: static int
- Signature: getmiso(struct spi_device * spi)
- Line: 98

### setmosi
- Return type: static void
- Signature: setmosi(struct spi_device * spi,int is_on)
- Line: 83

### setsck
- Return type: static void
- Signature: setsck(struct spi_device * spi,int is_on)
- Line: 67

### spidev_to_pp
- Return type: static butterfly *
- Signature: spidev_to_pp(struct spi_device * spi)
- Line: 44

## Structs (1)

### butterfly
- Line: 49
- Members:
  - bitbang: spi_bitbang
  - port: parport *
  - pd: pardevice *
  - lastbyte: u8
  - dataflash: spi_device *
  - butterfly: spi_device *
  - info: spi_board_info[2]

## Variables (4)

- static **butterfly** : butterfly * (line 174)
- static **butterfly_driver** : parport_driver (line 314)
- static **flash** : flash_platform_data (line 167)
- static **partitions** : mtd_partition[] (line 146)

## Macros (7)

- **butterfly_nreset** (line 31)
- **spi_cs_bit** (line 42)
- **spi_miso_bit** (line 39)
- **spi_mosi_bit** (line 34)
- **spi_sck_bit** (line 33)
- **spidelay**(X) (line 131)
- **vcc_bits** (line 36)
