# drivers/spi/spi-rb4xx.c

Subsystem: drivers/spi

## Functions (9)

### do_spi_byte
- Return type: static void
- Signature: do_spi_byte(struct rb4xx_spi * rbspi,u32 spi_ioc,u8 byte)
- Line: 57

### do_spi_byte_two
- Return type: static void
- Signature: do_spi_byte_two(struct rb4xx_spi * rbspi,u32 spi_ioc,u8 byte)
- Line: 82

### do_spi_clk
- Return type: static void
- Signature: do_spi_clk(struct rb4xx_spi * rbspi,u32 spi_ioc,int value)
- Line: 45

### do_spi_clk_two
- Return type: static void
- Signature: do_spi_clk_two(struct rb4xx_spi * rbspi,u32 spi_ioc,u8 value)
- Line: 66

### rb4xx_read
- Return type: static u32
- Signature: rb4xx_read(struct rb4xx_spi * rbspi,u32 reg)
- Line: 35

### rb4xx_set_cs
- Return type: static void
- Signature: rb4xx_set_cs(struct spi_device * spi,bool enable)
- Line: 90

### rb4xx_spi_probe
- Return type: static int
- Signature: rb4xx_spi_probe(struct platform_device * pdev)
- Line: 143

### rb4xx_transfer_one
- Return type: static int
- Signature: rb4xx_transfer_one(struct spi_controller * host,struct spi_device * spi,struct spi_transfer * t)
- Line: 104

### rb4xx_write
- Return type: static void
- Signature: rb4xx_write(struct rb4xx_spi * rbspi,u32 reg,u32 value)
- Line: 40

## Structs (1)

### rb4xx_spi
- Line: 30
- Members:
  - base: void __iomem *
  - clk: clk *

## Variables (2)

- static **rb4xx_spi_drv** : platform_driver (line 193)
- static **rb4xx_spi_dt_match** : const struct of_device_id[] (line 187)

## Macros (8)

- **AR71XX_SPI_FS_GPIO** (line 24)
- **AR71XX_SPI_IOC_CLK** (line 27)
- **AR71XX_SPI_IOC_CS**(n) (line 28)
- **AR71XX_SPI_IOC_DO** (line 26)
- **AR71XX_SPI_REG_CTRL** (line 20)
- **AR71XX_SPI_REG_FS** (line 19)
- **AR71XX_SPI_REG_IOC** (line 21)
- **AR71XX_SPI_REG_RDS** (line 22)
