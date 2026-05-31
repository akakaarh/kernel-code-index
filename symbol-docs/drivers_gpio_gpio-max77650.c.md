# drivers/gpio/gpio-max77650.c

Subsystem: drivers/gpio

## Functions (8)

### max77650_gpio_direction_input
- Return type: static int
- Signature: max77650_gpio_direction_input(struct gpio_chip * gc,unsigned int offset)
- Line: 40
- Calls: gpiochip_get_data

### max77650_gpio_direction_output
- Return type: static int
- Signature: max77650_gpio_direction_output(struct gpio_chip * gc,unsigned int offset,int value)
- Line: 51
- Calls: gpiochip_get_data

### max77650_gpio_get_direction
- Return type: static int
- Signature: max77650_gpio_get_direction(struct gpio_chip * gc,unsigned int offset)
- Line: 91
- Calls: gpiochip_get_data

### max77650_gpio_get_value
- Return type: static int
- Signature: max77650_gpio_get_value(struct gpio_chip * gc,unsigned int offset)
- Line: 77
- Calls: gpiochip_get_data

### max77650_gpio_probe
- Return type: static int
- Signature: max77650_gpio_probe(struct platform_device * pdev)
- Line: 138

### max77650_gpio_set_config
- Return type: static int
- Signature: max77650_gpio_set_config(struct gpio_chip * gc,unsigned int offset,unsigned long cfg)
- Line: 105
- Calls: gpiochip_get_data

### max77650_gpio_set_value
- Return type: static int
- Signature: max77650_gpio_set_value(struct gpio_chip * gc,unsigned int offset,int value)
- Line: 65
- Calls: gpiochip_get_data

### max77650_gpio_to_irq
- Return type: static int
- Signature: max77650_gpio_to_irq(struct gpio_chip * gc,unsigned int offset)
- Line: 131
- Calls: gpiochip_get_data

## Structs (1)

### max77650_gpio_chip
- Line: 34
- Members:
  - map: regmap *
  - gc: gpio_chip
  - irq: int

## Variables (1)

- static **max77650_gpio_driver** : platform_driver (line 178)

## Macros (14)

- **MAX77650_GPIO_DEBOUNCE** (line 27)
- **MAX77650_GPIO_DEBOUNCE_MASK** (line 19)
- **MAX77650_GPIO_DIR_BITS**(_reg) (line 29)
- **MAX77650_GPIO_DIR_IN** (line 22)
- **MAX77650_GPIO_DIR_MASK** (line 15)
- **MAX77650_GPIO_DIR_OUT** (line 21)
- **MAX77650_GPIO_DRV_MASK** (line 17)
- **MAX77650_GPIO_DRV_OPEN_DRAIN** (line 25)
- **MAX77650_GPIO_DRV_PUSH_PULL** (line 26)
- **MAX77650_GPIO_INVAL_BITS**(_reg) (line 31)
- **MAX77650_GPIO_INVAL_MASK** (line 16)
- **MAX77650_GPIO_OUTVAL_MASK** (line 18)
- **MAX77650_GPIO_OUT_HIGH** (line 24)
- **MAX77650_GPIO_OUT_LOW** (line 23)
