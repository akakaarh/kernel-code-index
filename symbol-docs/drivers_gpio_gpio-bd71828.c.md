# drivers/gpio/gpio-bd71828.c

Subsystem: drivers/gpio

## Functions (5)

### bd71828_get_direction
- Return type: static int
- Signature: bd71828_get_direction(struct gpio_chip * chip,unsigned int offset)
- Line: 79

### bd71828_gpio_get
- Return type: static int
- Signature: bd71828_gpio_get(struct gpio_chip * chip,unsigned int offset)
- Line: 36
- Calls: gpiochip_get_data

### bd71828_gpio_set
- Return type: static int
- Signature: bd71828_gpio_set(struct gpio_chip * chip,unsigned int offset,int value)
- Line: 19
- Calls: gpiochip_get_data

### bd71828_gpio_set_config
- Return type: static int
- Signature: bd71828_gpio_set_config(struct gpio_chip * chip,unsigned int offset,unsigned long config)
- Line: 54
- Calls: gpiochip_get_data

### bd71828_probe
- Return type: static int
- Signature: bd71828_probe(struct platform_device * pdev)
- Line: 95

## Structs (1)

### bd71828_gpio
- Line: 13
- Members:
  - regmap: regmap *
  - dev: device *
  - gpio: gpio_chip

## Variables (1)

- static **bd71828_gpio** : platform_driver (line 128)

## Macros (2)

- **GPIO_OUT_REG**(off) (line 10)
- **HALL_GPIO_OFFSET** (line 11)
