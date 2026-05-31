# drivers/gpio/gpio-lp873x.c

Subsystem: drivers/gpio

## Functions (8)

### lp873x_gpio_direction_input
- Return type: static int
- Signature: lp873x_gpio_direction_input(struct gpio_chip * chip,unsigned int offset)
- Line: 31

### lp873x_gpio_direction_output
- Return type: static int
- Signature: lp873x_gpio_direction_output(struct gpio_chip * chip,unsigned int offset,int value)
- Line: 38
- Calls: gpiochip_get_data

### lp873x_gpio_get
- Return type: static int
- Signature: lp873x_gpio_get(struct gpio_chip * chip,unsigned int offset)
- Line: 49
- Calls: gpiochip_get_data

### lp873x_gpio_get_direction
- Return type: static int
- Signature: lp873x_gpio_get_direction(struct gpio_chip * chip,unsigned int offset)
- Line: 24

### lp873x_gpio_probe
- Return type: static int
- Signature: lp873x_gpio_probe(struct platform_device * pdev)
- Line: 134

### lp873x_gpio_request
- Return type: static int
- Signature: lp873x_gpio_request(struct gpio_chip * gc,unsigned int offset)
- Line: 71
- Calls: gpiochip_get_data

### lp873x_gpio_set
- Return type: static int
- Signature: lp873x_gpio_set(struct gpio_chip * chip,unsigned int offset,int value)
- Line: 61
- Calls: gpiochip_get_data

### lp873x_gpio_set_config
- Return type: static int
- Signature: lp873x_gpio_set_config(struct gpio_chip * gc,unsigned offset,unsigned long config)
- Line: 95
- Calls: gpiochip_get_data

## Structs (1)

### lp873x_gpio
- Line: 19
- Members:
  - chip: gpio_chip
  - lp873: lp873x *

## Variables (3)

- static **lp873x_gpio_driver** : platform_driver (line 164)
- static **lp873x_gpio_id_table** : const struct platform_device_id[] (line 158)
- static **template_chip** : const struct gpio_chip (line 119)

## Macros (2)

- **BITS_PER_GPO** (line 16)
- **LP873X_GPO_CTRL_OD** (line 17)
