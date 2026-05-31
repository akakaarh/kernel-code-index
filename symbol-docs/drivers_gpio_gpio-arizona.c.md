# drivers/gpio/gpio-arizona.c

Subsystem: drivers/gpio

## Functions (5)

### arizona_gpio_direction_in
- Return type: static int
- Signature: arizona_gpio_direction_in(struct gpio_chip * chip,unsigned offset)
- Line: 26
- Calls: gpiochip_get_data, gpiochip_line_is_persistent

### arizona_gpio_direction_out
- Return type: static int
- Signature: arizona_gpio_direction_out(struct gpio_chip * chip,unsigned offset,int value)
- Line: 93
- Calls: gpiochip_get_data, gpiochip_line_is_persistent

### arizona_gpio_get
- Return type: static int
- Signature: arizona_gpio_get(struct gpio_chip * chip,unsigned offset)
- Line: 48
- Calls: gpiochip_get_data

### arizona_gpio_probe
- Return type: static int
- Signature: arizona_gpio_probe(struct platform_device * pdev)
- Line: 145

### arizona_gpio_set
- Return type: static int
- Signature: arizona_gpio_set(struct gpio_chip * chip,unsigned int offset,int value)
- Line: 122
- Calls: gpiochip_get_data

## Structs (1)

### arizona_gpio
- Line: 21
- Members:
  - arizona: arizona *
  - gpio_chip: gpio_chip

## Variables (2)

- static **arizona_gpio_driver** : platform_driver (line 201)
- static **template_chip** : const struct gpio_chip (line 135)
