# drivers/spi/spi-clps711x.c

Subsystem: drivers/spi

## Functions (4)

### spi_clps711x_isr
- Return type: static irqreturn_t
- Signature: spi_clps711x_isr(int irq,void * dev_id)
- Line: 69

### spi_clps711x_prepare_message
- Return type: static int
- Signature: spi_clps711x_prepare_message(struct spi_controller * host,struct spi_message * msg)
- Line: 36

### spi_clps711x_probe
- Return type: static int
- Signature: spi_clps711x_probe(struct platform_device * pdev)
- Line: 91

### spi_clps711x_transfer_one
- Return type: static int
- Signature: spi_clps711x_transfer_one(struct spi_controller * host,struct spi_device * spi,struct spi_transfer * xfer)
- Line: 48

## Structs (1)

### spi_clps711x_data
- Line: 25
- Members:
  - syncio: void __iomem *
  - syscon: regmap *
  - spi_clk: clk *
  - tx_buf: u8 *
  - rx_buf: u8 *
  - bpw: unsigned int
  - len: int

## Variables (2)

- static **clps711x_spi_driver** : platform_driver (line 160)
- static **clps711x_spi_dt_ids** : const struct of_device_id[] (line 154)

## Macros (3)

- **DRIVER_NAME** (line 20)
- **SYNCIO_FRMLEN**(x) (line 22)
- **SYNCIO_TXFRMEN** (line 23)
