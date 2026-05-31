# drivers/gpio/gpio-loongson.c

Subsystem: drivers/gpio

## Functions (6)

### loongson_gpio_direction_input
- Return type: static int
- Signature: loongson_gpio_direction_input(struct gpio_chip * chip,unsigned gpio)
- Line: 68
- Calls: loongson_commit_direction, to_loongson_gpio_chip

### loongson_gpio_direction_output
- Return type: static int
- Signature: loongson_gpio_direction_output(struct gpio_chip * chip,unsigned gpio,int level)
- Line: 81
- Calls: loongson_commit_direction, loongson_commit_level, loongson_gpio_set_value, to_loongson_gpio_chip

### loongson_gpio_get_value
- Return type: static int
- Signature: loongson_gpio_get_value(struct gpio_chip * chip,unsigned gpio)
- Line: 40

### loongson_gpio_probe
- Return type: static int
- Signature: loongson_gpio_probe(struct platform_device * pdev)
- Line: 96
- Calls: loongson_gpio_init

### loongson_gpio_set_value
- Return type: static int
- Signature: loongson_gpio_set_value(struct gpio_chip * chip,unsigned int gpio,int value)
- Line: 51
- Called by: loongson_gpio_direction_output

### loongson_gpio_setup
- Return type: static int __init
- Signature: loongson_gpio_setup(void)
- Line: 123

## Variables (1)

- static **loongson_gpio_driver** : platform_driver (line 116)

## Macros (5)

- **LOONGSON_GPIO_IN_OFFSET** (line 36)
- **LOONGSON_N_GPIO** (line 26)
- **LOONGSON_N_GPIO** (line 28)
- **STLS2F_N_GPIO** (line 22)
- **STLS3A_N_GPIO** (line 23)
