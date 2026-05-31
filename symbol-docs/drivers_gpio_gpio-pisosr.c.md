# drivers/gpio/gpio-pisosr.c

Subsystem: drivers/gpio

## Functions (6)

### pisosr_gpio_direction_input
- Return type: static int
- Signature: pisosr_gpio_direction_input(struct gpio_chip * chip,unsigned offset)
- Line: 63

### pisosr_gpio_get
- Return type: static int
- Signature: pisosr_gpio_get(struct gpio_chip * chip,unsigned offset)
- Line: 70
- Calls: gpiochip_get_data, pisosr_gpio_refresh

### pisosr_gpio_get_direction
- Return type: static int
- Signature: pisosr_gpio_get_direction(struct gpio_chip * chip,unsigned offset)
- Line: 56

### pisosr_gpio_get_multiple
- Return type: static int
- Signature: pisosr_gpio_get_multiple(struct gpio_chip * chip,unsigned long * mask,unsigned long * bits)
- Line: 80
- Calls: gpiochip_get_data, pisosr_gpio_refresh

### pisosr_gpio_probe
- Return type: static int
- Signature: pisosr_gpio_probe(struct spi_device * spi)
- Line: 111
- Calls: devm_gpiod_get_optional

### pisosr_gpio_refresh
- Return type: static int
- Signature: pisosr_gpio_refresh(struct pisosr_gpio * gpio)
- Line: 36
- Calls: gpiod_set_value_cansleep
- Called by: pisosr_gpio_get, pisosr_gpio_get_multiple

## Structs (1)

### pisosr_gpio
- Line: 27
- Members:
  - chip: gpio_chip
  - spi: spi_device *
  - buffer: u8 *
  - buffer_size: size_t
  - load_gpio: gpio_desc *
  - lock: mutex

## Variables (4)

- static **pisosr_gpio_driver** : spi_driver (line 162)
- static **pisosr_gpio_id_table** : const struct spi_device_id[] (line 150)
- static **pisosr_gpio_of_match_table** : const struct of_device_id[] (line 156)
- static **template_chip** : const struct gpio_chip (line 99)

## Macros (1)

- **DEFAULT_NGPIO** (line 16)
