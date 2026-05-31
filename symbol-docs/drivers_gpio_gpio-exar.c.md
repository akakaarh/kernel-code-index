# drivers/gpio/gpio-exar.c

Subsystem: drivers/gpio

## Functions (10)

### exar_devm_ida_free
- Return type: static void
- Signature: exar_devm_ida_free(void * data)
- Line: 137

### exar_direction_input
- Return type: static int
- Signature: exar_direction_input(struct gpio_chip * chip,unsigned int offset)
- Line: 126
- Calls: exar_offset_to_bit, exar_offset_to_sel_addr, gpiochip_get_data

### exar_direction_output
- Return type: static int
- Signature: exar_direction_output(struct gpio_chip * chip,unsigned int offset,int value)
- Line: 111
- Calls: exar_offset_to_bit, exar_offset_to_sel_addr, exar_set_value, gpiochip_get_data

### exar_get_direction
- Return type: static int
- Signature: exar_get_direction(struct gpio_chip * chip,unsigned int offset)
- Line: 75
- Calls: exar_offset_to_bit, exar_offset_to_sel_addr, gpiochip_get_data

### exar_get_value
- Return type: static int
- Signature: exar_get_value(struct gpio_chip * chip,unsigned int offset)
- Line: 87
- Calls: exar_offset_to_bit, exar_offset_to_lvl_addr, gpiochip_get_data

### exar_offset_to_bit
- Return type: static unsigned int
- Signature: exar_offset_to_bit(struct exar_gpio_chip * exar_gpio,unsigned int offset)
- Line: 68
- Called by: exar_direction_input, exar_direction_output, exar_get_direction, exar_get_value, exar_set_value

### exar_offset_to_lvl_addr
- Return type: static unsigned int
- Signature: exar_offset_to_lvl_addr(struct exar_gpio_chip * exar_gpio,unsigned int offset)
- Line: 58
- Called by: exar_get_value, exar_set_value

### exar_offset_to_sel_addr
- Return type: static unsigned int
- Signature: exar_offset_to_sel_addr(struct exar_gpio_chip * exar_gpio,unsigned int offset)
- Line: 48
- Called by: exar_direction_input, exar_direction_output, exar_get_direction

### exar_set_value
- Return type: static int
- Signature: exar_set_value(struct gpio_chip * chip,unsigned int offset,int value)
- Line: 96
- Calls: exar_offset_to_bit, exar_offset_to_lvl_addr, gpiochip_get_data
- Called by: exar_direction_output

### gpio_exar_probe
- Return type: static int
- Signature: gpio_exar_probe(struct platform_device * pdev)
- Line: 151

## Structs (1)

### exar_gpio_chip
- Line: 34
- Members:
  - gpio_chip: gpio_chip
  - regmap: regmap *
  - index: int
  - name: char[20]
  - first_pin: unsigned int
  - cascaded_offset: unsigned int

## Variables (2)

- static **exar_regmap_config** : const struct regmap_config (line 144)
- static **gpio_exar_driver** : platform_driver (line 227)

## Macros (6)

- **DRIVER_NAME** (line 30)
- **EXAR_OFFSET_MPIOLVL_HI** (line 21)
- **EXAR_OFFSET_MPIOLVL_LO** (line 19)
- **EXAR_OFFSET_MPIOSEL_HI** (line 22)
- **EXAR_OFFSET_MPIOSEL_LO** (line 20)
- **EXAR_UART_CHANNEL_SIZE** (line 28)
