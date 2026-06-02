# drivers/spi/spi-jcore.c

Subsystem: drivers/spi

## Functions (6)

### jcore_spi_baudrate
- Return type: static void
- Signature: jcore_spi_baudrate(struct jcore_spi * hw,int speed)
- Line: 83

### jcore_spi_chipsel
- Return type: static void
- Signature: jcore_spi_chipsel(struct spi_device * spi,bool value)
- Line: 68

### jcore_spi_probe
- Return type: static int
- Signature: jcore_spi_probe(struct platform_device * pdev)
- Line: 141

### jcore_spi_program
- Return type: static void
- Signature: jcore_spi_program(struct jcore_spi * hw)
- Line: 57

### jcore_spi_txrx
- Return type: static int
- Signature: jcore_spi_txrx(struct spi_controller * host,struct spi_device * spi,struct spi_transfer * t)
- Line: 97

### jcore_spi_wait
- Return type: static int
- Signature: jcore_spi_wait(void __iomem * ctrl_reg)
- Line: 44

## Structs (1)

### jcore_spi
- Line: 35
- Members:
  - host: spi_controller *
  - base: void __iomem *
  - cs_reg: unsigned int
  - speed_reg: unsigned int
  - speed_hz: unsigned int
  - clock_freq: unsigned int

## Variables (2)

- static **jcore_spi_driver** : platform_driver (line 222)
- static **jcore_spi_of_match** : const struct of_device_id[] (line 216)

## Macros (8)

- **CTRL_REG** (line 25)
- **DATA_REG** (line 26)
- **DRV_NAME** (line 23)
- **JCORE_SPI_CTRL_CS_BITS** (line 31)
- **JCORE_SPI_CTRL_LOOP** (line 30)
- **JCORE_SPI_CTRL_XMIT** (line 28)
- **JCORE_SPI_STAT_BUSY** (line 29)
- **JCORE_SPI_WAIT_RDY_MAX_LOOP** (line 33)
