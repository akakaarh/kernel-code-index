# drivers/spi/spi-lm70llp.c

Subsystem: drivers/spi

## Functions (13)

### assertCS
- Return type: static void
- Signature: assertCS(struct spi_lm70llp * pp)
- Line: 104

### clkHigh
- Return type: static void
- Signature: clkHigh(struct spi_lm70llp * pp)
- Line: 112

### clkLow
- Return type: static void
- Signature: clkLow(struct spi_lm70llp * pp)
- Line: 119

### deassertCS
- Return type: static void
- Signature: deassertCS(struct spi_lm70llp * pp)
- Line: 96

### getmiso
- Return type: static int
- Signature: getmiso(struct spi_device * s)
- Line: 158

### lm70_chipselect
- Return type: static void
- Signature: lm70_chipselect(struct spi_device * spi,int value)
- Line: 169

### lm70_txrx
- Return type: static u32
- Signature: lm70_txrx(struct spi_device * spi,unsigned nsecs,u32 word,u8 bits,unsigned flags)
- Line: 182

### setmosi
- Return type: static void
- Signature: setmosi(struct spi_device * s,int is_on)
- Line: 143

### setsck
- Return type: static void
- Signature: setsck(struct spi_device * s,int is_on)
- Line: 133

### spi_lm70llp_attach
- Return type: static void
- Signature: spi_lm70llp_attach(struct parport * p)
- Line: 188

### spi_lm70llp_detach
- Return type: static void
- Signature: spi_lm70llp_detach(struct parport * p)
- Line: 296

### spidelay
- Return type: static void
- Signature: spidelay(unsigned d)
- Line: 128

### spidev_to_pp
- Return type: static spi_lm70llp *
- Signature: spidev_to_pp(struct spi_device * spi)
- Line: 84

## Structs (1)

### spi_lm70llp
- Line: 70
- Members:
  - bitbang: spi_bitbang
  - port: parport *
  - pd: pardevice *
  - spidev_lm70: spi_device *
  - info: spi_board_info

## Variables (2)

- static **lm70llp** : spi_lm70llp * (line 80)
- static **spi_lm70llp_drv** : parport_driver (line 317)

## Macros (6)

- **DRVNAME** (line 61)
- **SCLK** (line 66)
- **SIO** (line 64)
- **lm70_INIT** (line 63)
- **nCS** (line 65)
- **pr_fmt**(fmt) (line 8)
