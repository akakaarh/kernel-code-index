# drivers/spi/spi-oc-tiny.c

Subsystem: drivers/spi

## Functions (12)

### tiny_spi_baud
- Return type: static unsigned int
- Signature: tiny_spi_baud(struct spi_device * spi,unsigned int hz)
- Line: 59

### tiny_spi_irq
- Return type: static irqreturn_t
- Signature: tiny_spi_irq(int irq,void * dev)
- Line: 158

### tiny_spi_of_probe
- Return type: static int
- Signature: tiny_spi_of_probe(struct platform_device * pdev)
- Line: 187

### tiny_spi_of_probe
- Return type: static int
- Signature: tiny_spi_of_probe(struct platform_device * pdev)
- Line: 202

### tiny_spi_probe
- Return type: static int
- Signature: tiny_spi_probe(struct platform_device * pdev)
- Line: 208

### tiny_spi_remove
- Return type: static void
- Signature: tiny_spi_remove(struct platform_device * pdev)
- Line: 271

### tiny_spi_setup
- Return type: static int
- Signature: tiny_spi_setup(struct spi_device * spi)
- Line: 81

### tiny_spi_setup_transfer
- Return type: static int
- Signature: tiny_spi_setup_transfer(struct spi_device * spi,struct spi_transfer * t)
- Line: 66

### tiny_spi_to_hw
- Return type: static tiny_spi *
- Signature: tiny_spi_to_hw(struct spi_device * sdev)
- Line: 54

### tiny_spi_txrx_bufs
- Return type: static int
- Signature: tiny_spi_txrx_bufs(struct spi_device * spi,struct spi_transfer * t)
- Line: 107

### tiny_spi_wait_txe
- Return type: static void
- Signature: tiny_spi_wait_txe(struct tiny_spi * hw)
- Line: 100

### tiny_spi_wait_txr
- Return type: static void
- Signature: tiny_spi_wait_txr(struct tiny_spi * hw)
- Line: 93

## Structs (1)

### tiny_spi
- Line: 36
- Members:
  - bitbang: spi_bitbang
  - done: completion
  - base: void __iomem *
  - irq: int
  - freq: unsigned int
  - baudwidth: unsigned int
  - baud: unsigned int
  - speed_hz: unsigned int
  - mode: unsigned int
  - len: unsigned int
  - rxc: unsigned int
  - txc: unsigned int
  - txp: const u8 *
  - rxp: u8 *

## Variables (2)

- static **tiny_spi_driver** : platform_driver (line 288)
- static **tiny_spi_match** : const struct of_device_id[] (line 281)

## Macros (8)

- **DRV_NAME** (line 25)
- **TINY_SPI_BAUD** (line 31)
- **TINY_SPI_CONTROL** (line 30)
- **TINY_SPI_RXDATA** (line 27)
- **TINY_SPI_STATUS** (line 29)
- **TINY_SPI_STATUS_TXE** (line 33)
- **TINY_SPI_STATUS_TXR** (line 34)
- **TINY_SPI_TXDATA** (line 28)
