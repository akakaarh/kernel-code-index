# drivers/gpio/gpio-cgbc.c

Subsystem: drivers/gpio

## Functions (9)

### __cgbc_gpio_set
- Return type: static int
- Signature: __cgbc_gpio_set(struct gpio_chip * chip,unsigned int offset,int value)
- Line: 54
- Calls: cgbc_gpio_cmd, gpiochip_get_data
- Called by: cgbc_gpio_direction_output, cgbc_gpio_set

### cgbc_gpio_cmd
- Return type: static int
- Signature: cgbc_gpio_cmd(struct cgbc_device_data * cgbc,u8 cmd0,u8 cmd1,u8 cmd2,u8 * value)
- Line: 28
- Called by: __cgbc_gpio_set, cgbc_gpio_direction_set, cgbc_gpio_get, cgbc_gpio_get_direction

### cgbc_gpio_direction_input
- Return type: static int
- Signature: cgbc_gpio_direction_input(struct gpio_chip * chip,unsigned int offset)
- Line: 106
- Calls: cgbc_gpio_direction_set, gpiochip_get_data

### cgbc_gpio_direction_output
- Return type: static int
- Signature: cgbc_gpio_direction_output(struct gpio_chip * chip,unsigned int offset,int value)
- Line: 115
- Calls: __cgbc_gpio_set, cgbc_gpio_direction_set, gpiochip_get_data

### cgbc_gpio_direction_set
- Return type: static int
- Signature: cgbc_gpio_direction_set(struct gpio_chip * chip,unsigned int offset,int direction)
- Line: 83
- Calls: cgbc_gpio_cmd, gpiochip_get_data
- Called by: cgbc_gpio_direction_input, cgbc_gpio_direction_output

### cgbc_gpio_get
- Return type: static int
- Signature: cgbc_gpio_get(struct gpio_chip * chip,unsigned int offset)
- Line: 36
- Calls: cgbc_gpio_cmd, gpiochip_get_data

### cgbc_gpio_get_direction
- Return type: static int
- Signature: cgbc_gpio_get_direction(struct gpio_chip * chip,unsigned int offset)
- Line: 130
- Calls: cgbc_gpio_cmd, gpiochip_get_data

### cgbc_gpio_probe
- Return type: static int
- Signature: cgbc_gpio_probe(struct platform_device * pdev)
- Line: 149

### cgbc_gpio_set
- Return type: static int
- Signature: cgbc_gpio_set(struct gpio_chip * chip,unsigned int offset,int value)
- Line: 74
- Calls: __cgbc_gpio_set, gpiochip_get_data

## Structs (1)

### cgbc_gpio_data
- Line: 22
- Members:
  - chip: gpio_chip
  - cgbc: cgbc_device_data *
  - lock: mutex

## Variables (1)

- static **cgbc_gpio_driver** : platform_driver (line 188)

## Macros (5)

- **CGBC_GPIO_CMD_DIR_GET** (line 19)
- **CGBC_GPIO_CMD_DIR_SET** (line 20)
- **CGBC_GPIO_CMD_GET** (line 17)
- **CGBC_GPIO_CMD_SET** (line 18)
- **CGBC_GPIO_NGPIO** (line 15)
