# drivers/gpio/gpio-adp5520.c

Subsystem: drivers/gpio

## Functions (5)

### adp5520_gpio_direction_input
- Return type: static int
- Signature: adp5520_gpio_direction_input(struct gpio_chip * chip,unsigned off)
- Line: 57
- Calls: gpiochip_get_data

### adp5520_gpio_direction_output
- Return type: static int
- Signature: adp5520_gpio_direction_output(struct gpio_chip * chip,unsigned off,int val)
- Line: 68
- Calls: gpiochip_get_data

### adp5520_gpio_get_value
- Return type: static int
- Signature: adp5520_gpio_get_value(struct gpio_chip * chip,unsigned off)
- Line: 23
- Calls: gpiochip_get_data

### adp5520_gpio_probe
- Return type: static int
- Signature: adp5520_gpio_probe(struct platform_device * pdev)
- Line: 90

### adp5520_gpio_set_value
- Return type: static int
- Signature: adp5520_gpio_set_value(struct gpio_chip * chip,unsigned int off,int val)
- Line: 43
- Calls: gpiochip_get_data

## Structs (1)

### adp5520_gpio
- Line: 16
- Members:
  - master: device *
  - gpio_chip: gpio_chip
  - lut: unsigned char[]
  - output: unsigned long

## Variables (1)

- static **adp5520_gpio_driver** : platform_driver (line 157)
