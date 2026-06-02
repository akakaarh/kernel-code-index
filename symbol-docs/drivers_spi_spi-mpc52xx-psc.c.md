# drivers/spi/spi-mpc52xx-psc.c

Subsystem: drivers/spi

## Functions (9)

### mpc52xx_psc_spi_activate_cs
- Return type: static void
- Signature: mpc52xx_psc_spi_activate_cs(struct spi_device * spi)
- Line: 60

### mpc52xx_psc_spi_cleanup
- Return type: static void
- Signature: mpc52xx_psc_spi_cleanup(struct spi_device * spi)
- Line: 237

### mpc52xx_psc_spi_isr
- Return type: static irqreturn_t
- Signature: mpc52xx_psc_spi_isr(int irq,void * dev_id)
- Line: 280

### mpc52xx_psc_spi_of_probe
- Return type: static int
- Signature: mpc52xx_psc_spi_of_probe(struct platform_device * pdev)
- Line: 294

### mpc52xx_psc_spi_port_config
- Return type: static int
- Signature: mpc52xx_psc_spi_port_config(int psc_id,struct mpc52xx_psc_spi * mps)
- Line: 242

### mpc52xx_psc_spi_setup
- Return type: static int
- Signature: mpc52xx_psc_spi_setup(struct spi_device * spi)
- Line: 217

### mpc52xx_psc_spi_transfer_one_message
- Return type: static int
- Signature: mpc52xx_psc_spi_transfer_one_message(struct spi_controller * ctlr,struct spi_message * m)
- Line: 178

### mpc52xx_psc_spi_transfer_rxtx
- Return type: static int
- Signature: mpc52xx_psc_spi_transfer_rxtx(struct spi_device * spi,struct spi_transfer * t)
- Line: 104

### mpc52xx_psc_spi_transfer_setup
- Return type: static int
- Signature: mpc52xx_psc_spi_transfer_setup(struct spi_device * spi,struct spi_transfer * t)
- Line: 47

## Structs (2)

### mpc52xx_psc_spi
- Line: 28
- Members:
  - psc: mpc52xx_psc __iomem *
  - fifo: mpc52xx_psc_fifo __iomem *
  - irq: int
  - bits_per_word: u8
  - done: completion
  - bits_per_word: int
  - speed_hz: int

### mpc52xx_psc_spi_cs
- Line: 39
- Members:
  - psc: mpc52xx_psc __iomem *
  - fifo: mpc52xx_psc_fifo __iomem *
  - irq: int
  - bits_per_word: u8
  - done: completion
  - bits_per_word: int
  - speed_hz: int

## Variables (2)

- static **mpc52xx_psc_spi_of_driver** : platform_driver (line 355)
- static **mpc52xx_psc_spi_of_match** : const struct of_device_id[] (line 347)

## Macros (3)

- **MCLK** (line 26)
- **MPC52xx_PSC_BUFSIZE** (line 100)
- **MPC52xx_PSC_RFALARM** (line 102)
