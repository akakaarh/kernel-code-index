# drivers/spi/spi-mux.c

Subsystem: drivers/spi

## Functions (5)

### spi_mux_complete_cb
- Return type: static void
- Signature: spi_mux_complete_cb(void * context)
- Line: 86

### spi_mux_probe
- Return type: static int
- Signature: spi_mux_probe(struct spi_device * spi)
- Line: 126

### spi_mux_select
- Return type: static int
- Signature: spi_mux_select(struct spi_device * spi)
- Line: 49

### spi_mux_setup
- Return type: static int
- Signature: spi_mux_setup(struct spi_device * spi)
- Line: 74

### spi_mux_transfer_one_message
- Return type: static int
- Signature: spi_mux_transfer_one_message(struct spi_controller * ctlr,struct spi_message * m)
- Line: 99

## Structs (1)

### spi_mux_priv
- Line: 38
- Members:
  - spi: spi_device *
  - current_cs: unsigned int
  - child_msg_complete: void (*)(void * context)
  - child_msg_context: void *
  - child_msg_dev: spi_device *
  - mux: mux_control *

## Variables (3)

- static **spi_mux_driver** : spi_driver (line 191)
- static **spi_mux_id** : const struct spi_device_id[] (line 179)
- static **spi_mux_of_match** : const struct of_device_id[] (line 185)

## Macros (1)

- **SPI_MUX_NO_CS** (line 12)
