# drivers/spi/spi-ar934x.c

Subsystem: drivers/spi

## Functions (5)

### ar934x_spi_clk_div
- Return type: static int
- Signature: ar934x_spi_clk_div(struct ar934x_spi * sp,unsigned int freq)
- Line: 51

### ar934x_spi_probe
- Return type: static int
- Signature: ar934x_spi_probe(struct platform_device * pdev)
- Line: 165

### ar934x_spi_remove
- Return type: static void
- Signature: ar934x_spi_remove(struct platform_device * pdev)
- Line: 211

### ar934x_spi_setup
- Return type: static int
- Signature: ar934x_spi_setup(struct spi_device * spi)
- Line: 63

### ar934x_spi_transfer_one_message
- Return type: static int
- Signature: ar934x_spi_transfer_one_message(struct spi_controller * ctlr,struct spi_message * m)
- Line: 78

## Structs (1)

### ar934x_spi
- Line: 44
- Members:
  - ctlr: spi_controller *
  - base: void __iomem *
  - clk: clk *
  - clk_freq: unsigned int

## Variables (2)

- static **ar934x_spi_driver** : platform_driver (line 219)
- static **ar934x_spi_match** : const struct of_device_id[] (line 159)

## Macros (14)

- **AR934X_SPI_CLK_MASK** (line 30)
- **AR934X_SPI_DATAIN** (line 42)
- **AR934X_SPI_DATAOUT** (line 32)
- **AR934X_SPI_ENABLE** (line 24)
- **AR934X_SPI_IOC_INITVAL** (line 27)
- **AR934X_SPI_REG_CTRL** (line 29)
- **AR934X_SPI_REG_FS** (line 23)
- **AR934X_SPI_REG_IOC** (line 26)
- **AR934X_SPI_REG_SHIFT_CTRL** (line 34)
- **AR934X_SPI_SHIFT_CS**(n) (line 36)
- **AR934X_SPI_SHIFT_EN** (line 35)
- **AR934X_SPI_SHIFT_TERM** (line 37)
- **AR934X_SPI_SHIFT_VAL**(cs,term,count) (line 38)
- **DRIVER_NAME** (line 21)
