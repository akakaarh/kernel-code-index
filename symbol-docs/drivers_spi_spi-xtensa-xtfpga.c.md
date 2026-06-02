# drivers/spi/spi-xtensa-xtfpga.c

Subsystem: drivers/spi

## Functions (7)

### xtfpga_spi_chipselect
- Return type: static void
- Signature: xtfpga_spi_chipselect(struct spi_device * spi,int is_on)
- Line: 72

### xtfpga_spi_probe
- Return type: static int
- Signature: xtfpga_spi_probe(struct platform_device * pdev)
- Line: 80

### xtfpga_spi_read32
- Return type: static unsigned int
- Signature: xtfpga_spi_read32(const struct xtfpga_spi * spi,unsigned addr)
- Line: 37

### xtfpga_spi_remove
- Return type: static void
- Signature: xtfpga_spi_remove(struct platform_device * pdev)
- Line: 119

### xtfpga_spi_txrx_word
- Return type: static u32
- Signature: xtfpga_spi_txrx_word(struct spi_device * spi,unsigned nsecs,u32 v,u8 bits,unsigned flags)
- Line: 53

### xtfpga_spi_wait_busy
- Return type: static void
- Signature: xtfpga_spi_wait_busy(struct xtfpga_spi * xspi)
- Line: 43

### xtfpga_spi_write32
- Return type: static void
- Signature: xtfpga_spi_write32(const struct xtfpga_spi * spi,unsigned addr,u32 val)
- Line: 31

## Structs (1)

### xtfpga_spi
- Line: 24
- Members:
  - bitbang: spi_bitbang
  - regs: void __iomem *
  - data: u32
  - data_sz: unsigned

## Variables (2)

- static **xtfpga_spi_driver** : platform_driver (line 138)
- static **xtfpga_spi_of_match** : const struct of_device_id[] (line 131)

## Macros (5)

- **BUSY_WAIT_US** (line 22)
- **XTFPGA_SPI_BUSY** (line 19)
- **XTFPGA_SPI_DATA** (line 20)
- **XTFPGA_SPI_NAME** (line 16)
- **XTFPGA_SPI_START** (line 18)
