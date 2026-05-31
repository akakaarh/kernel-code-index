# drivers/gpio/gpio-tps65219.c

Subsystem: drivers/gpio

## Functions (9)

### tps65214_gpio_change_direction
- Return type: static int
- Signature: tps65214_gpio_change_direction(struct gpio_chip * gc,unsigned int offset,unsigned int direction)
- Line: 142
- Calls: gpiochip_get_data

### tps65214_gpio_get_direction
- Return type: static int
- Signature: tps65214_gpio_get_direction(struct gpio_chip * gc,unsigned int offset)
- Line: 37
- Calls: gpiochip_get_data

### tps65219_gpio_change_direction
- Return type: static int
- Signature: tps65219_gpio_change_direction(struct gpio_chip * gc,unsigned int offset,unsigned int direction)
- Line: 110
- Calls: gpiochip_get_data

### tps65219_gpio_direction_input
- Return type: static int
- Signature: tps65219_gpio_direction_input(struct gpio_chip * gc,unsigned int offset)
- Line: 169
- Calls: gpiochip_get_data, tps65219_gpio_get_direction

### tps65219_gpio_direction_output
- Return type: static int
- Signature: tps65219_gpio_direction_output(struct gpio_chip * gc,unsigned int offset,int value)
- Line: 185
- Calls: gpiochip_get_data, tps65219_gpio_get_direction, tps65219_gpio_set

### tps65219_gpio_get
- Return type: static int
- Signature: tps65219_gpio_get(struct gpio_chip * gc,unsigned int offset)
- Line: 67
- Calls: gpiochip_get_data, tps65219_gpio_get_direction

### tps65219_gpio_get_direction
- Return type: static int
- Signature: tps65219_gpio_get_direction(struct gpio_chip * gc,unsigned int offset)
- Line: 52
- Calls: gpiochip_get_data
- Called by: tps65219_gpio_direction_input, tps65219_gpio_direction_output, tps65219_gpio_get

### tps65219_gpio_probe
- Return type: static int
- Signature: tps65219_gpio_probe(struct platform_device * pdev)
- Line: 225

### tps65219_gpio_set
- Return type: static int
- Signature: tps65219_gpio_set(struct gpio_chip * gc,unsigned int offset,int value)
- Line: 96
- Calls: gpiochip_get_data
- Called by: tps65219_gpio_direction_output

## Structs (1)

### tps65219_gpio
- Line: 31
- Members:
  - change_dir: int (*)(struct gpio_chip * gc,unsigned int offset,unsigned int dir)
  - gpio_chip: gpio_chip
  - tps: tps65219 *

## Variables (4)

- static **tps65214_template_chip** : const struct gpio_chip (line 199)
- static **tps65219_gpio_driver** : platform_driver (line 258)
- static **tps65219_template_chip** : const struct gpio_chip (line 212)
- static **tps6521x_gpio_id_table** : const struct platform_device_id[] (line 251)

## Macros (4)

- **TPS65214_GPIO0_DIR_MASK** (line 16)
- **TPS65219_GPIO0_DIR_MASK** (line 15)
- **TPS6521X_GPIO0_IDX** (line 18)
- **TPS6521X_GPIO0_OFFSET** (line 17)
