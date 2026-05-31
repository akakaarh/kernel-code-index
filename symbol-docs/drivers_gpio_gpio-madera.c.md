# drivers/gpio/gpio-madera.c

Subsystem: drivers/gpio

## Functions (6)

### madera_gpio_direction_in
- Return type: static int
- Signature: madera_gpio_direction_in(struct gpio_chip * chip,unsigned int offset)
- Line: 43
- Calls: gpiochip_get_data

### madera_gpio_direction_out
- Return type: static int
- Signature: madera_gpio_direction_out(struct gpio_chip * chip,unsigned int offset,int value)
- Line: 70
- Calls: gpiochip_get_data

### madera_gpio_get
- Return type: static int
- Signature: madera_gpio_get(struct gpio_chip * chip,unsigned int offset)
- Line: 54
- Calls: gpiochip_get_data

### madera_gpio_get_direction
- Return type: static int
- Signature: madera_gpio_get_direction(struct gpio_chip * chip,unsigned int offset)
- Line: 23
- Calls: gpiochip_get_data

### madera_gpio_probe
- Return type: static int
- Signature: madera_gpio_probe(struct platform_device * pdev)
- Line: 117

### madera_gpio_set
- Return type: static int
- Signature: madera_gpio_set(struct gpio_chip * chip,unsigned int offset,int value)
- Line: 90
- Calls: gpiochip_get_data

## Structs (1)

### madera_gpio
- Line: 17
- Members:
  - madera: madera *
  - gpio_chip: gpio_chip

## Variables (2)

- static **madera_gpio_chip** : const struct gpio_chip (line 103)
- static **madera_gpio_driver** : platform_driver (line 193)
