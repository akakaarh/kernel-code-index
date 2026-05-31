# drivers/gpio/gpio-zynqmp-modepin.c

Subsystem: drivers/gpio

## Functions (5)

### modepin_gpio_dir_in
- Return type: static int
- Signature: modepin_gpio_dir_in(struct gpio_chip * chip,unsigned int pin)
- Line: 91

### modepin_gpio_dir_out
- Return type: static int
- Signature: modepin_gpio_dir_out(struct gpio_chip * chip,unsigned int pin,int state)
- Line: 104
- Calls: modepin_gpio_set_value

### modepin_gpio_get_value
- Return type: static int
- Signature: modepin_gpio_get_value(struct gpio_chip * chip,unsigned int pin)
- Line: 31

### modepin_gpio_probe
- Return type: static int
- Signature: modepin_gpio_probe(struct platform_device * pdev)
- Line: 116

### modepin_gpio_set_value
- Return type: static int
- Signature: modepin_gpio_set_value(struct gpio_chip * chip,unsigned int pin,int state)
- Line: 60
- Called by: modepin_gpio_dir_out

## Variables (2)

- static **modepin_platform_driver** : platform_driver (line 153)
- static **modepin_platform_id** : const struct of_device_id[] (line 147)

## Macros (1)

- **MODE_PINS** (line 19)
