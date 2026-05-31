# drivers/gpio/gpio-mc33880.c

Subsystem: drivers/gpio

## Functions (7)

### __mc33880_set
- Return type: static int
- Signature: __mc33880_set(struct mc33880 * mc,unsigned offset,int value)
- Line: 49
- Calls: mc33880_write_config
- Called by: mc33880_set

### mc33880_exit
- Return type: static void __exit
- Signature: mc33880_exit(void)
- Line: 167

### mc33880_init
- Return type: static int __init
- Signature: mc33880_init(void)
- Line: 158

### mc33880_probe
- Return type: static int
- Signature: mc33880_probe(struct spi_device * spi)
- Line: 74
- Calls: mc33880_write_config

### mc33880_remove
- Return type: static void
- Signature: mc33880_remove(struct spi_device * spi)
- Line: 140
- Calls: gpiochip_remove

### mc33880_set
- Return type: static int
- Signature: mc33880_set(struct gpio_chip * chip,unsigned int offset,int value)
- Line: 60
- Calls: __mc33880_set, gpiochip_get_data

### mc33880_write_config
- Return type: static int
- Signature: mc33880_write_config(struct mc33880 * mc)
- Line: 43
- Called by: __mc33880_set, mc33880_probe

## Structs (1)

### mc33880
- Line: 36
- Members:
  - lock: mutex
  - port_config: u8
  - chip: gpio_chip
  - spi: spi_device *

## Variables (1)

- static **mc33880_driver** : spi_driver (line 150)

## Macros (6)

- **DRIVER_NAME** (line 19)
- **PIN_CONFIG_IN_PULLUP** (line 25)
- **PIN_CONFIG_IN_WO_PULLUP** (line 26)
- **PIN_CONFIG_MASK** (line 24)
- **PIN_CONFIG_OUT** (line 27)
- **PIN_NUMBER** (line 29)
