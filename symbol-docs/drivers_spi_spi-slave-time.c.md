# drivers/spi/spi-slave-time.c

Subsystem: drivers/spi

## Functions (4)

### spi_slave_time_complete
- Return type: static void
- Signature: spi_slave_time_complete(void * arg)
- Line: 43

### spi_slave_time_probe
- Return type: static int
- Signature: spi_slave_time_probe(struct spi_device * spi)
- Line: 87

### spi_slave_time_remove
- Return type: static void
- Signature: spi_slave_time_remove(struct spi_device * spi)
- Line: 109

### spi_slave_time_submit
- Return type: static int
- Signature: spi_slave_time_submit(struct spi_slave_time_priv * priv)
- Line: 63

## Structs (1)

### spi_slave_time_priv
- Line: 33
- Members:
  - spi: spi_device *
  - finished: completion
  - xfer: spi_transfer
  - msg: spi_message
  - buf: __be32[2]

## Variables (1)

- static **spi_slave_time_driver** : spi_driver (line 117)
