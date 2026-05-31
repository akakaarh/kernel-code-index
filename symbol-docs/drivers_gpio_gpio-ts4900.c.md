# drivers/gpio/gpio-ts4900.c

Subsystem: drivers/gpio

## Functions (6)

### ts4900_gpio_direction_input
- Return type: static int
- Signature: ts4900_gpio_direction_input(struct gpio_chip * chip,unsigned int offset)
- Line: 45
- Calls: gpiochip_get_data

### ts4900_gpio_direction_output
- Return type: static int
- Signature: ts4900_gpio_direction_output(struct gpio_chip * chip,unsigned int offset,int value)
- Line: 57
- Calls: gpiochip_get_data

### ts4900_gpio_get
- Return type: static int
- Signature: ts4900_gpio_get(struct gpio_chip * chip,unsigned int offset)
- Line: 88
- Calls: gpiochip_get_data

### ts4900_gpio_get_direction
- Return type: static int
- Signature: ts4900_gpio_get_direction(struct gpio_chip * chip,unsigned int offset)
- Line: 31
- Calls: gpiochip_get_data

### ts4900_gpio_probe
- Return type: static int
- Signature: ts4900_gpio_probe(struct i2c_client * client)
- Line: 139

### ts4900_gpio_set
- Return type: static int
- Signature: ts4900_gpio_set(struct gpio_chip * chip,unsigned int offset,int value)
- Line: 98
- Calls: gpiochip_get_data

## Structs (1)

### ts4900_gpio_priv
- Line: 25
- Members:
  - regmap: regmap *
  - gpio_chip: gpio_chip
  - input_bit: unsigned int

## Variables (5)

- static **template_chip** : const struct gpio_chip (line 115)
- static **ts4900_gpio_driver** : i2c_driver (line 183)
- static **ts4900_gpio_id_table** : const struct i2c_device_id[] (line 177)
- static **ts4900_gpio_of_match_table** : const struct of_device_id[] (line 127)
- static **ts4900_regmap_config** : const struct regmap_config (line 110)

## Macros (5)

- **DEFAULT_PIN_NUMBER** (line 15)
- **TS4900_GPIO_IN** (line 22)
- **TS4900_GPIO_OE** (line 20)
- **TS4900_GPIO_OUT** (line 21)
- **TS7970_GPIO_IN** (line 23)
