# drivers/gpio/gpio-tps68470.c

Subsystem: drivers/gpio

## Functions (7)

### tps68470_enable_i2c_daisy_chain
- Return type: static int
- Signature: tps68470_enable_i2c_daisy_chain(struct gpio_chip * gc)
- Line: 123
- Calls: tps68470_gpio_input
- Called by: tps68470_gpio_probe

### tps68470_gpio_get
- Return type: static int
- Signature: tps68470_gpio_get(struct gpio_chip * gc,unsigned int offset)
- Line: 29
- Calls: gpiochip_get_data

### tps68470_gpio_get_direction
- Return type: static int
- Signature: tps68470_gpio_get_direction(struct gpio_chip * gc,unsigned int offset)
- Line: 50
- Calls: gpiochip_get_data

### tps68470_gpio_input
- Return type: static int
- Signature: tps68470_gpio_input(struct gpio_chip * gc,unsigned int offset)
- Line: 110
- Calls: gpiochip_get_data
- Called by: tps68470_enable_i2c_daisy_chain

### tps68470_gpio_output
- Return type: static int
- Signature: tps68470_gpio_output(struct gpio_chip * gc,unsigned int offset,int value)
- Line: 89
- Calls: gpiochip_get_data, tps68470_gpio_set

### tps68470_gpio_probe
- Return type: static int
- Signature: tps68470_gpio_probe(struct platform_device * pdev)
- Line: 140
- Calls: tps68470_enable_i2c_daisy_chain

### tps68470_gpio_set
- Return type: static int
- Signature: tps68470_gpio_set(struct gpio_chip * gc,unsigned int offset,int value)
- Line: 73
- Calls: gpiochip_get_data
- Called by: tps68470_gpio_output

## Structs (1)

### tps68470_gpio_data
- Line: 24
- Members:
  - tps68470_regmap: regmap *
  - gc: gpio_chip

## Variables (2)

- static **tps68470_gpio_driver** : platform_driver (line 174)
- static **tps68470_names** : const char * [] (line 134)

## Macros (3)

- **TPS68470_N_GPIO** (line 22)
- **TPS68470_N_LOGIC_OUTPUT** (line 20)
- **TPS68470_N_REGULAR_GPIO** (line 21)
