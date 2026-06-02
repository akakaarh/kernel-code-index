# drivers/spi/spi-sh-sci.c

Subsystem: drivers/spi

## Functions (11)

### getmiso
- Return type: static u32
- Signature: getmiso(struct spi_device * dev)
- Line: 67

### setbits
- Return type: static void
- Signature: setbits(struct sh_sci_spi * sp,int bits,int on)
- Line: 39

### setmosi
- Return type: static void
- Signature: setmosi(struct spi_device * dev,int on)
- Line: 62

### setsck
- Return type: static void
- Signature: setsck(struct spi_device * dev,int on)
- Line: 57

### sh_sci_spi_chipselect
- Return type: static void
- Signature: sh_sci_spi_chipselect(struct spi_device * dev,int value)
- Line: 106

### sh_sci_spi_probe
- Return type: static int
- Signature: sh_sci_spi_probe(struct platform_device * dev)
- Line: 114

### sh_sci_spi_remove
- Return type: static void
- Signature: sh_sci_spi_remove(struct platform_device * dev)
- Line: 174

### sh_sci_spi_txrx_mode0
- Return type: static u32
- Signature: sh_sci_spi_txrx_mode0(struct spi_device * spi,unsigned nsecs,u32 word,u8 bits,unsigned flags)
- Line: 78

### sh_sci_spi_txrx_mode1
- Return type: static u32
- Signature: sh_sci_spi_txrx_mode1(struct spi_device * spi,unsigned nsecs,u32 word,u8 bits,unsigned flags)
- Line: 85

### sh_sci_spi_txrx_mode2
- Return type: static u32
- Signature: sh_sci_spi_txrx_mode2(struct spi_device * spi,unsigned nsecs,u32 word,u8 bits,unsigned flags)
- Line: 92

### sh_sci_spi_txrx_mode3
- Return type: static u32
- Signature: sh_sci_spi_txrx_mode3(struct spi_device * spi,unsigned nsecs,u32 word,u8 bits,unsigned flags)
- Line: 99

## Structs (1)

### sh_sci_spi
- Line: 24
- Members:
  - bitbang: spi_bitbang
  - membase: void __iomem *
  - val: unsigned char
  - info: sh_spi_info *
  - dev: platform_device *

## Variables (1)

- static **sh_sci_spi_drv** : platform_driver (line 184)

## Macros (6)

- **PIN_INIT** (line 37)
- **PIN_RXD** (line 36)
- **PIN_SCK** (line 34)
- **PIN_TXD** (line 35)
- **SCSPTR**(sp) (line 33)
- **spidelay**(x) (line 74)
