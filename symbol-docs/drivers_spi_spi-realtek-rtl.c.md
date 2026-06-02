# drivers/spi/spi-realtek-rtl.c

Subsystem: drivers/spi

## Functions (10)

### init_hw
- Return type: static void
- Signature: init_hw(struct rtspi * rtspi)
- Line: 133

### rcv1
- Return type: static void
- Signature: rcv1(struct rtspi * rtspi,u8 * buf)
- Line: 86

### rcv4
- Return type: static void
- Signature: rcv4(struct rtspi * rtspi,u32 * buf)
- Line: 79

### realtek_rtl_spi_probe
- Return type: static int
- Signature: realtek_rtl_spi_probe(struct platform_device * pdev)
- Line: 150

### rt_set_cs
- Return type: static void
- Signature: rt_set_cs(struct spi_device * spi,bool active)
- Line: 33

### send1
- Return type: static void
- Signature: send1(struct rtspi * rtspi,const u8 * buf)
- Line: 72

### send4
- Return type: static void
- Signature: send4(struct rtspi * rtspi,const u32 * buf)
- Line: 65

### set_size
- Return type: static void
- Signature: set_size(struct rtspi * rtspi,int size)
- Line: 47

### transfer_one
- Return type: static int
- Signature: transfer_one(struct spi_controller * ctrl,struct spi_device * spi,struct spi_transfer * xfer)
- Line: 93

### wait_ready
- Return type: static void
- Signature: wait_ready(struct rtspi * rtspi)
- Line: 60

## Structs (1)

### rtspi
- Line: 8
- Members:
  - base: void __iomem *

## Variables (2)

- static **realtek_rtl_spi_driver** : platform_driver (line 196)
- static **realtek_rtl_spi_of_ids** : const struct of_device_id[] (line 186)

## Macros (13)

- **REG**(x) (line 30)
- **RTL_SPI_SFCR** (line 13)
- **RTL_SPI_SFCR_RBO** (line 14)
- **RTL_SPI_SFCR_WBO** (line 15)
- **RTL_SPI_SFCSR** (line 18)
- **RTL_SPI_SFCSR_CS** (line 22)
- **RTL_SPI_SFCSR_CSB0** (line 19)
- **RTL_SPI_SFCSR_CSB1** (line 20)
- **RTL_SPI_SFCSR_LEN1** (line 24)
- **RTL_SPI_SFCSR_LEN4** (line 25)
- **RTL_SPI_SFCSR_LEN_MASK** (line 23)
- **RTL_SPI_SFCSR_RDY** (line 21)
- **RTL_SPI_SFDR** (line 28)
