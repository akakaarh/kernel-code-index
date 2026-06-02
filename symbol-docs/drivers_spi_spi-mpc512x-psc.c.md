# drivers/spi/spi-mpc512x-psc.c

Subsystem: drivers/spi

## Functions (12)

### mpc512x_psc_spi_activate_cs
- Return type: static void
- Signature: mpc512x_psc_spi_activate_cs(struct spi_device * spi)
- Line: 85

### mpc512x_psc_spi_cleanup
- Return type: static void
- Signature: mpc512x_psc_spi_cleanup(struct spi_device * spi)
- Line: 378

### mpc512x_psc_spi_deactivate_cs
- Return type: static void
- Signature: mpc512x_psc_spi_deactivate_cs(struct spi_device * spi)
- Line: 130

### mpc512x_psc_spi_isr
- Return type: static irqreturn_t
- Signature: mpc512x_psc_spi_isr(int irq,void * dev_id)
- Line: 442

### mpc512x_psc_spi_msg_xfer
- Return type: static int
- Signature: mpc512x_psc_spi_msg_xfer(struct spi_controller * host,struct spi_message * m)
- Line: 283

### mpc512x_psc_spi_of_probe
- Return type: static int
- Signature: mpc512x_psc_spi_of_probe(struct platform_device * pdev)
- Line: 458

### mpc512x_psc_spi_port_config
- Return type: static int
- Signature: mpc512x_psc_spi_port_config(struct spi_controller * host,struct mpc512x_psc_spi * mps)
- Line: 383

### mpc512x_psc_spi_prep_xfer_hw
- Return type: static int
- Signature: mpc512x_psc_spi_prep_xfer_hw(struct spi_controller * host)
- Line: 327

### mpc512x_psc_spi_setup
- Return type: static int
- Signature: mpc512x_psc_spi_setup(struct spi_device * spi)
- Line: 357

### mpc512x_psc_spi_transfer_rxtx
- Return type: static int
- Signature: mpc512x_psc_spi_transfer_rxtx(struct spi_device * spi,struct spi_transfer * t)
- Line: 143

### mpc512x_psc_spi_transfer_setup
- Return type: static int
- Signature: mpc512x_psc_spi_transfer_setup(struct spi_device * spi,struct spi_transfer * t)
- Line: 72

### mpc512x_psc_spi_unprep_xfer_hw
- Return type: static int
- Signature: mpc512x_psc_spi_unprep_xfer_hw(struct spi_controller * host)
- Line: 343

## Structs (2)

### mpc512x_psc_spi
- Line: 51
- Members:
  - type: int
  - psc: void __iomem *
  - fifo: mpc512x_psc_fifo __iomem *
  - irq: int
  - bits_per_word: u8
  - mclk_rate: u32
  - txisrdone: completion
  - bits_per_word: int
  - speed_hz: int

### mpc512x_psc_spi_cs
- Line: 64
- Members:
  - type: int
  - psc: void __iomem *
  - fifo: mpc512x_psc_fifo __iomem *
  - irq: int
  - bits_per_word: u8
  - mclk_rate: u32
  - txisrdone: completion
  - bits_per_word: int
  - speed_hz: int

## Enums (1)

### __anond0b9ea250103
- Line: 26

## Variables (2)

- static **mpc512x_psc_spi_of_driver** : platform_driver (line 525)
- static **mpc512x_psc_spi_of_match** : const struct of_device_id[] (line 517)

## Macros (3)

- **EOFBYTE** (line 141)
- **MPC512x_PSC_FIFO_SZ**(sz) (line 139)
- **psc_addr**(mps,regname) (line 35)
