# drivers/gpio/gpio-bd9571mwv.c

Subsystem: drivers/gpio

## Functions (6)

### bd9571mwv_gpio_direction_input
- Return type: static int
- Signature: bd9571mwv_gpio_direction_input(struct gpio_chip * chip,unsigned int offset)
- Line: 39
- Calls: gpiochip_get_data

### bd9571mwv_gpio_direction_output
- Return type: static int
- Signature: bd9571mwv_gpio_direction_output(struct gpio_chip * chip,unsigned int offset,int value)
- Line: 49
- Calls: gpiochip_get_data

### bd9571mwv_gpio_get
- Return type: static int
- Signature: bd9571mwv_gpio_get(struct gpio_chip * chip,unsigned int offset)
- Line: 63
- Calls: gpiochip_get_data

### bd9571mwv_gpio_get_direction
- Return type: static int
- Signature: bd9571mwv_gpio_get_direction(struct gpio_chip * chip,unsigned int offset)
- Line: 24
- Calls: gpiochip_get_data

### bd9571mwv_gpio_probe
- Return type: static int
- Signature: bd9571mwv_gpio_probe(struct platform_device * pdev)
- Line: 97

### bd9571mwv_gpio_set
- Return type: static int
- Signature: bd9571mwv_gpio_set(struct gpio_chip * chip,unsigned int offset,int value)
- Line: 75
- Calls: gpiochip_get_data

## Structs (1)

### bd9571mwv_gpio
- Line: 19
- Members:
  - regmap: regmap *
  - chip: gpio_chip

## Variables (3)

- static **bd9571mwv_gpio_driver** : platform_driver (line 119)
- static **bd9571mwv_gpio_id_table** : const struct platform_device_id[] (line 112)
- static **template_chip** : const struct gpio_chip (line 84)
