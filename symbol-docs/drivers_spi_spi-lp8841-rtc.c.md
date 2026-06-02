# drivers/spi/spi-lp8841-rtc.c

Subsystem: drivers/spi

## Functions (8)

### bitbang_txrx_be_cpha0_lsb
- Return type: static u32
- Signature: bitbang_txrx_be_cpha0_lsb(struct spi_lp8841_rtc * data,unsigned usecs,unsigned cpol,unsigned flags,u32 word,u8 bits)
- Line: 66

### getmiso
- Return type: static int
- Signature: getmiso(struct spi_lp8841_rtc * data)
- Line: 60

### setmosi
- Return type: static void
- Signature: setmosi(struct spi_lp8841_rtc * data,int is_on)
- Line: 50

### setsck
- Return type: static void
- Signature: setsck(struct spi_lp8841_rtc * data,int is_on)
- Line: 40

### spi_lp8841_rtc_probe
- Return type: static int
- Signature: spi_lp8841_rtc_probe(struct platform_device * pdev)
- Line: 182

### spi_lp8841_rtc_set_cs
- Return type: static void
- Signature: spi_lp8841_rtc_set_cs(struct spi_device * spi,bool enable)
- Line: 137

### spi_lp8841_rtc_setup
- Return type: static int
- Signature: spi_lp8841_rtc_setup(struct spi_device * spi)
- Line: 152

### spi_lp8841_rtc_transfer_one
- Return type: static int
- Signature: spi_lp8841_rtc_transfer_one(struct spi_controller * host,struct spi_device * spi,struct spi_transfer * t)
- Line: 98

## Structs (1)

### spi_lp8841_rtc
- Line: 34
- Members:
  - iomem: void *
  - state: unsigned long

## Variables (2)

- static **spi_lp8841_rtc_driver** : platform_driver (line 232)
- static **spi_lp8841_rtc_dt_ids** : const struct of_device_id[] (line 173)

## Macros (6)

- **DRIVER_NAME** (line 20)
- **SPI_LP8841_RTC_CE** (line 22)
- **SPI_LP8841_RTC_CLK** (line 23)
- **SPI_LP8841_RTC_MISO** (line 26)
- **SPI_LP8841_RTC_MOSI** (line 25)
- **SPI_LP8841_RTC_nWE** (line 24)
