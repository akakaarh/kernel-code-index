# drivers/gpio/gpio-tps65086.c

Subsystem: drivers/gpio

## Functions (6)

### tps65086_gpio_direction_input
- Return type: static int
- Signature: tps65086_gpio_direction_input(struct gpio_chip * chip,unsigned offset)
- Line: 27

### tps65086_gpio_direction_output
- Return type: static int
- Signature: tps65086_gpio_direction_output(struct gpio_chip * chip,unsigned offset,int value)
- Line: 34
- Calls: gpiochip_get_data

### tps65086_gpio_get
- Return type: static int
- Signature: tps65086_gpio_get(struct gpio_chip * chip,unsigned offset)
- Line: 44
- Calls: gpiochip_get_data

### tps65086_gpio_get_direction
- Return type: static int
- Signature: tps65086_gpio_get_direction(struct gpio_chip * chip,unsigned offset)
- Line: 20

### tps65086_gpio_probe
- Return type: static int
- Signature: tps65086_gpio_probe(struct platform_device * pdev)
- Line: 78

### tps65086_gpio_set
- Return type: static int
- Signature: tps65086_gpio_set(struct gpio_chip * chip,unsigned int offset,int value)
- Line: 56
- Calls: gpiochip_get_data

## Structs (1)

### tps65086_gpio
- Line: 15
- Members:
  - chip: gpio_chip
  - tps: tps65086 *

## Variables (3)

- static **template_chip** : const struct gpio_chip (line 65)
- static **tps65086_gpio_driver** : platform_driver (line 99)
- static **tps65086_gpio_id_table** : const struct platform_device_id[] (line 93)
