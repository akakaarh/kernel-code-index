# drivers/gpio/gpio-cros-ec.c

Subsystem: drivers/gpio

## Functions (6)

### cros_ec_gpio_get
- Return type: static int
- Signature: cros_ec_gpio_get(struct gpio_chip * gc,unsigned int gpio)
- Line: 44
- Calls: gpiochip_get_data

### cros_ec_gpio_get_direction
- Return type: static int
- Signature: cros_ec_gpio_get_direction(struct gpio_chip * gc,unsigned int gpio)
- Line: 70
- Calls: gpiochip_get_data

### cros_ec_gpio_init_names
- Return type: static int
- Signature: cros_ec_gpio_init_names(struct cros_ec_device * cros_ec,struct gpio_chip * gc)
- Line: 98
- Called by: cros_ec_gpio_probe

### cros_ec_gpio_ngpios
- Return type: static int
- Signature: cros_ec_gpio_ngpios(struct cros_ec_device * cros_ec)
- Line: 143
- Called by: cros_ec_gpio_probe

### cros_ec_gpio_probe
- Return type: static int
- Signature: cros_ec_gpio_probe(struct platform_device * pdev)
- Line: 159
- Calls: cros_ec_gpio_init_names, cros_ec_gpio_ngpios

### cros_ec_gpio_set
- Return type: static int
- Signature: cros_ec_gpio_set(struct gpio_chip * gc,unsigned int gpio,int val)
- Line: 27
- Calls: gpiochip_get_data

## Variables (3)

- static **cros_ec_gpio_driver** : platform_driver (line 204)
- static **cros_ec_gpio_id** : const struct platform_device_id[] (line 198)
- static **cros_ec_gpio_prefix** : const char[] (line 24)

## Macros (2)

- **CROS_EC_GPIO_INPUT** (line 67)
- **CROS_EC_GPIO_OUTPUT** (line 68)
