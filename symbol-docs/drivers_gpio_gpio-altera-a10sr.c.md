# drivers/gpio/gpio-altera-a10sr.c

Subsystem: drivers/gpio

## Functions (5)

### altr_a10sr_gpio_direction_input
- Return type: static int
- Signature: altr_a10sr_gpio_direction_input(struct gpio_chip * gc,unsigned int nr)
- Line: 49

### altr_a10sr_gpio_direction_output
- Return type: static int
- Signature: altr_a10sr_gpio_direction_output(struct gpio_chip * gc,unsigned int nr,int value)
- Line: 58
- Calls: altr_a10sr_gpio_set

### altr_a10sr_gpio_get
- Return type: static int
- Signature: altr_a10sr_gpio_get(struct gpio_chip * chip,unsigned int offset)
- Line: 26
- Calls: gpiochip_get_data

### altr_a10sr_gpio_probe
- Return type: static int
- Signature: altr_a10sr_gpio_probe(struct platform_device * pdev)
- Line: 80

### altr_a10sr_gpio_set
- Return type: static int
- Signature: altr_a10sr_gpio_set(struct gpio_chip * chip,unsigned int offset,int value)
- Line: 38
- Calls: gpiochip_get_data
- Called by: altr_a10sr_gpio_direction_output

## Structs (1)

### altr_a10sr_gpio
- Line: 21
- Members:
  - gp: gpio_chip
  - regmap: regmap *

## Variables (3)

- static **altr_a10sr_gc** : const struct gpio_chip (line 68)
- static **altr_a10sr_gpio_driver** : platform_driver (line 104)
- static **altr_a10sr_gpio_of_match** : const struct of_device_id[] (line 98)
