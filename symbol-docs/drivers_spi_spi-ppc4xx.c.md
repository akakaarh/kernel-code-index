# drivers/spi/spi-ppc4xx.c

Subsystem: drivers/spi

## Functions (8)

### spi_ppc4xx_cleanup
- Return type: static void
- Signature: spi_ppc4xx_cleanup(struct spi_device * spi)
- Line: 315

### spi_ppc4xx_enable
- Return type: static void
- Signature: spi_ppc4xx_enable(struct ppc4xx_spi * hw)
- Line: 320

### spi_ppc4xx_int
- Return type: static irqreturn_t
- Signature: spi_ppc4xx_int(int irq,void * dev_id)
- Line: 254

### spi_ppc4xx_of_probe
- Return type: static int
- Signature: spi_ppc4xx_of_probe(struct platform_device * op)
- Line: 335

### spi_ppc4xx_of_remove
- Return type: static void
- Signature: spi_ppc4xx_of_remove(struct platform_device * op)
- Line: 466

### spi_ppc4xx_setup
- Return type: static int
- Signature: spi_ppc4xx_setup(struct spi_device * spi)
- Line: 211

### spi_ppc4xx_setupxfer
- Return type: static int
- Signature: spi_ppc4xx_setupxfer(struct spi_device * spi,struct spi_transfer * t)
- Line: 162

### spi_ppc4xx_txrx
- Return type: static int
- Signature: spi_ppc4xx_txrx(struct spi_device * spi,struct spi_transfer * t)
- Line: 138

## Structs (3)

### ppc4xx_spi
- Line: 110
- Members:
  - mode: u8
  - rxd: u8
  - txd: u8
  - cr: u8
  - sr: u8
  - dummy: u8
  - cdm: u8
  - bitbang: spi_bitbang
  - done: completion
  - mapbase: u64
  - mapsize: u64
  - irqnum: int
  - opb_freq: unsigned int
  - len: int
  - count: int
  - tx: const unsigned char *
  - rx: unsigned char *
  - regs: spi_ppc4xx_regs __iomem *
  - host: spi_controller *
  - dev: device *
  - mode: u8

### spi_ppc4xx_cs
- Line: 134
- Members:
  - mode: u8
  - rxd: u8
  - txd: u8
  - cr: u8
  - sr: u8
  - dummy: u8
  - cdm: u8
  - bitbang: spi_bitbang
  - done: completion
  - mapbase: u64
  - mapsize: u64
  - irqnum: int
  - opb_freq: unsigned int
  - len: int
  - count: int
  - tx: const unsigned char *
  - rx: unsigned char *
  - regs: spi_ppc4xx_regs __iomem *
  - host: spi_controller *
  - dev: device *
  - mode: u8

### spi_ppc4xx_regs
- Line: 91
- Members:
  - mode: u8
  - rxd: u8
  - txd: u8
  - cr: u8
  - sr: u8
  - dummy: u8
  - cdm: u8
  - bitbang: spi_bitbang
  - done: completion
  - mapbase: u64
  - mapsize: u64
  - irqnum: int
  - opb_freq: unsigned int
  - len: int
  - count: int
  - tx: const unsigned char *
  - rx: unsigned char *
  - regs: spi_ppc4xx_regs __iomem *
  - host: spi_controller *
  - dev: device *
  - mode: u8

## Variables (2)

- static **spi_ppc4xx_of_driver** : platform_driver (line 485)
- static **spi_ppc4xx_of_match** : const struct of_device_id[] (line 478)

## Macros (13)

- **DRIVER_NAME** (line 89)
- **SPI_CLK_MODE0** (line 84)
- **SPI_CLK_MODE1** (line 85)
- **SPI_CLK_MODE2** (line 86)
- **SPI_CLK_MODE3** (line 87)
- **SPI_PPC4XX_CR_STR** (line 75)
- **SPI_PPC4XX_MODE_CI** (line 65)
- **SPI_PPC4XX_MODE_IL** (line 71)
- **SPI_PPC4XX_MODE_RD** (line 58)
- **SPI_PPC4XX_MODE_SCP** (line 48)
- **SPI_PPC4XX_MODE_SPE** (line 51)
- **SPI_PPC4XX_SR_BSY** (line 79)
- **SPI_PPC4XX_SR_RBR** (line 81)
