# drivers/spi/spi-slave-system-control.c

Subsystem: drivers/spi

## Functions (4)

### spi_slave_system_control_complete
- Return type: static void
- Signature: spi_slave_system_control_complete(void * arg)
- Line: 49

### spi_slave_system_control_probe
- Return type: static int
- Signature: spi_slave_system_control_probe(struct spi_device * spi)
- Line: 113

### spi_slave_system_control_remove
- Return type: static void
- Signature: spi_slave_system_control_remove(struct spi_device * spi)
- Line: 135

### spi_slave_system_control_submit
- Return type: static int
- Signature: spi_slave_system_control_submit(struct spi_slave_system_control_priv * priv)
- Line: 97

## Structs (1)

### spi_slave_system_control_priv
- Line: 38
- Members:
  - spi: spi_device *
  - finished: completion
  - xfer: spi_transfer
  - msg: spi_message
  - cmd: __be16

## Variables (1)

- static **spi_slave_system_control_driver** : spi_driver (line 143)

## Macros (4)

- **CMD_HALT** (line 35)
- **CMD_POWEROFF** (line 34)
- **CMD_REBOOT** (line 33)
- **CMD_SUSPEND** (line 36)
