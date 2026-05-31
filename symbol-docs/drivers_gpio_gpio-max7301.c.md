# drivers/gpio/gpio-max7301.c

Subsystem: drivers/gpio

## Functions (6)

### max7301_exit
- Return type: static void __exit
- Signature: max7301_exit(void)
- Line: 96

### max7301_init
- Return type: static int __init
- Signature: max7301_init(void)
- Line: 87

### max7301_probe
- Return type: static int
- Signature: max7301_probe(struct spi_device * spi)
- Line: 44
- Calls: __max730x_probe

### max7301_remove
- Return type: static void
- Signature: max7301_remove(struct spi_device * spi)
- Line: 67
- Calls: __max730x_remove

### max7301_spi_read
- Return type: static int
- Signature: max7301_spi_read(struct device * dev,unsigned int reg)
- Line: 30

### max7301_spi_write
- Return type: static int
- Signature: max7301_spi_write(struct device * dev,unsigned int reg,unsigned int val)
- Line: 19

## Variables (2)

- static **max7301_driver** : spi_driver (line 78)
- static **max7301_id** : const struct spi_device_id[] (line 72)
