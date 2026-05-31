# drivers/gpio/gpio-wcd934x.c

Subsystem: drivers/gpio

## Functions (6)

### wcd_gpio_direction_input
- Return type: static int
- Signature: wcd_gpio_direction_input(struct gpio_chip * chip,unsigned int pin)
- Line: 37
- Calls: gpiochip_get_data

### wcd_gpio_direction_output
- Return type: static int
- Signature: wcd_gpio_direction_output(struct gpio_chip * chip,unsigned int pin,int val)
- Line: 45
- Calls: gpiochip_get_data

### wcd_gpio_get
- Return type: static int
- Signature: wcd_gpio_get(struct gpio_chip * chip,unsigned int pin)
- Line: 61
- Calls: gpiochip_get_data

### wcd_gpio_get_direction
- Return type: static int
- Signature: wcd_gpio_get_direction(struct gpio_chip * chip,unsigned int pin)
- Line: 21
- Calls: gpiochip_get_data

### wcd_gpio_probe
- Return type: static int
- Signature: wcd_gpio_probe(struct platform_device * pdev)
- Line: 80

### wcd_gpio_set
- Return type: static int
- Signature: wcd_gpio_set(struct gpio_chip * chip,unsigned int pin,int val)
- Line: 71
- Calls: gpiochip_get_data

## Structs (1)

### wcd_gpio_data
- Line: 16
- Members:
  - map: regmap *
  - chip: gpio_chip

## Variables (2)

- static **wcd_gpio_driver** : platform_driver (line 118)
- static **wcd_gpio_of_match** : const struct of_device_id[] (line 111)

## Macros (4)

- **WCD934X_NPINS** (line 14)
- **WCD_PIN_MASK**(p) (line 11)
- **WCD_REG_DIR_CTL_OFFSET** (line 12)
- **WCD_REG_VAL_CTL_OFFSET** (line 13)
