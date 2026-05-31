# drivers/gpio/gpio-logicvc.c

Subsystem: drivers/gpio

## Functions (5)

### logicvc_gpio_direction_output
- Return type: static int
- Signature: logicvc_gpio_direction_output(struct gpio_chip * chip,unsigned offset,int value)
- Line: 75
- Calls: logicvc_gpio_set

### logicvc_gpio_get
- Return type: static int
- Signature: logicvc_gpio_get(struct gpio_chip * chip,unsigned offset)
- Line: 49
- Calls: gpiochip_get_data, logicvc_gpio_offset

### logicvc_gpio_offset
- Return type: static void
- Signature: logicvc_gpio_offset(struct logicvc_gpio * logicvc,unsigned offset,unsigned int * reg,unsigned int * bit)
- Line: 29
- Called by: logicvc_gpio_get, logicvc_gpio_set

### logicvc_gpio_probe
- Return type: static int
- Signature: logicvc_gpio_probe(struct platform_device * pdev)
- Line: 89

### logicvc_gpio_set
- Return type: static int
- Signature: logicvc_gpio_set(struct gpio_chip * chip,unsigned int offset,int value)
- Line: 64
- Calls: gpiochip_get_data, logicvc_gpio_offset
- Called by: logicvc_gpio_direction_output

## Structs (1)

### logicvc_gpio
- Line: 24
- Members:
  - chip: gpio_chip
  - regmap: regmap *

## Variables (3)

- static **logicivc_gpio_of_table** : const struct of_device_id[] (line 143)
- static **logicvc_gpio_driver** : platform_driver (line 152)
- static **logicvc_gpio_regmap_config** : regmap_config (line 82)

## Macros (6)

- **LOGICVC_CTRL_GPIO_BITS** (line 18)
- **LOGICVC_CTRL_GPIO_SHIFT** (line 17)
- **LOGICVC_CTRL_REG** (line 16)
- **LOGICVC_POWER_CTRL_GPIO_BITS** (line 22)
- **LOGICVC_POWER_CTRL_GPIO_SHIFT** (line 21)
- **LOGICVC_POWER_CTRL_REG** (line 20)
