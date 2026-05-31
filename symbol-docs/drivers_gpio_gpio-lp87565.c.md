# drivers/gpio/gpio-lp87565.c

Subsystem: drivers/gpio

## Functions (8)

### lp87565_gpio_direction_input
- Return type: static int
- Signature: lp87565_gpio_direction_input(struct gpio_chip * chip,unsigned int offset)
- Line: 58
- Calls: gpiochip_get_data

### lp87565_gpio_direction_output
- Return type: static int
- Signature: lp87565_gpio_direction_output(struct gpio_chip * chip,unsigned int offset,int value)
- Line: 68
- Calls: gpiochip_get_data, lp87565_gpio_set

### lp87565_gpio_get
- Return type: static int
- Signature: lp87565_gpio_get(struct gpio_chip * chip,unsigned int offset)
- Line: 21
- Calls: gpiochip_get_data

### lp87565_gpio_get_direction
- Return type: static int
- Signature: lp87565_gpio_get_direction(struct gpio_chip * chip,unsigned int offset)
- Line: 42
- Calls: gpiochip_get_data

### lp87565_gpio_probe
- Return type: static int
- Signature: lp87565_gpio_probe(struct platform_device * pdev)
- Line: 149

### lp87565_gpio_request
- Return type: static int
- Signature: lp87565_gpio_request(struct gpio_chip * gc,unsigned int offset)
- Line: 83
- Calls: gpiochip_get_data

### lp87565_gpio_set
- Return type: static int
- Signature: lp87565_gpio_set(struct gpio_chip * chip,unsigned int offset,int value)
- Line: 33
- Calls: gpiochip_get_data
- Called by: lp87565_gpio_direction_output

### lp87565_gpio_set_config
- Return type: static int
- Signature: lp87565_gpio_set_config(struct gpio_chip * gc,unsigned int offset,unsigned long config)
- Line: 111
- Calls: gpiochip_get_data

## Structs (1)

### lp87565_gpio
- Line: 16
- Members:
  - chip: gpio_chip
  - map: regmap *

## Variables (3)

- static **lp87565_gpio_driver** : platform_driver (line 179)
- static **lp87565_gpio_id_table** : const struct platform_device_id[] (line 173)
- static **template_chip** : const struct gpio_chip (line 134)
