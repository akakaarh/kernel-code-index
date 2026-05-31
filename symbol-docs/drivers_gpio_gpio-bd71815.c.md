# drivers/gpio/gpio-bd71815.c

Subsystem: drivers/gpio

## Functions (6)

### bd71815_gpio_set_config
- Return type: static int
- Signature: bd71815_gpio_set_config(struct gpio_chip * chip,unsigned int offset,unsigned long config)
- Line: 54
- Calls: gpiochip_get_data

### bd71815_init_valid_mask
- Return type: static int
- Signature: bd71815_init_valid_mask(struct gpio_chip * gc,unsigned long * valid_mask,unsigned int ngpios)
- Line: 111

### bd71815gpo_direction_get
- Return type: static int
- Signature: bd71815gpo_direction_get(struct gpio_chip * gc,unsigned int offset)
- Line: 77

### bd71815gpo_get
- Return type: static int
- Signature: bd71815gpo_get(struct gpio_chip * chip,unsigned int offset)
- Line: 28
- Calls: gpiochip_get_data

### bd71815gpo_set
- Return type: static int
- Signature: bd71815gpo_set(struct gpio_chip * chip,unsigned int offset,int value)
- Line: 40
- Calls: gpiochip_get_data

### gpo_bd71815_probe
- Return type: static int
- Signature: gpo_bd71815_probe(struct platform_device * pdev)
- Line: 127

## Structs (1)

### bd71815_gpio
- Line: 20
- Members:
  - chip: gpio_chip
  - dev: device *
  - regmap: regmap *

## Variables (2)

- static **bd71815gpo_chip** : const struct gpio_chip (line 83)
- static **gpo_bd71815_driver** : platform_driver (line 170)

## Macros (2)

- **BD71815_ONE_GPIO** (line 94)
- **BD71815_TWO_GPIOS** (line 93)
