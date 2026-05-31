# drivers/gpio/gpio-by-pinctrl.c

Subsystem: drivers/gpio

## Functions (5)

### pin_control_gpio_direction_output
- Return type: static int
- Signature: pin_control_gpio_direction_output(struct gpio_chip * chip,unsigned int offset,int val)
- Line: 31

### pin_control_gpio_get
- Return type: static int
- Signature: pin_control_gpio_get(struct gpio_chip * chip,unsigned int offset)
- Line: 37

### pin_control_gpio_get_direction
- Return type: static int
- Signature: pin_control_gpio_get_direction(struct gpio_chip * gc,unsigned int offset)
- Line: 16

### pin_control_gpio_probe
- Return type: static int
- Signature: pin_control_gpio_probe(struct platform_device * pdev)
- Line: 59

### pin_control_gpio_set
- Return type: static int
- Signature: pin_control_gpio_set(struct gpio_chip * chip,unsigned int offset,int val)
- Line: 50

## Variables (2)

- static **pin_control_gpio_driver** : platform_driver (line 90)
- static **pin_control_gpio_match** : const struct of_device_id[] (line 84)
