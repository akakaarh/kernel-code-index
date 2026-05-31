# drivers/gpio/gpio-bd72720.c

Subsystem: drivers/gpio

## Functions (8)

### bd72720_gpio_set_config
- Return type: static int
- Signature: bd72720_gpio_set_config(struct gpio_chip * chip,unsigned int offset,unsigned long config)
- Line: 131
- Calls: gpiochip_get_data

### bd72720_valid_mask
- Return type: static int
- Signature: bd72720_valid_mask(struct gpio_chip * gc,unsigned long * valid_mask,unsigned int ngpios)
- Line: 175
- Calls: gpiochip_get_data

### bd72720gpi_get
- Return type: static int
- Signature: bd72720gpi_get(struct bd72720_gpio * bdgpio,unsigned int reg_offset)
- Line: 72
- Called by: bd72720gpio_get

### bd72720gpio_get
- Return type: static int
- Signature: bd72720gpio_get(struct gpio_chip * chip,unsigned int offset)
- Line: 100
- Calls: bd72720gpi_get, bd72720gpo_get, gpiochip_get_data

### bd72720gpo_direction_get
- Return type: static int
- Signature: bd72720gpo_direction_get(struct gpio_chip * chip,unsigned int offset)
- Line: 164
- Calls: gpiochip_get_data

### bd72720gpo_get
- Return type: static int
- Signature: bd72720gpo_get(struct bd72720_gpio * bdgpio,unsigned int offset)
- Line: 85
- Called by: bd72720gpio_get

### bd72720gpo_set
- Return type: static int
- Signature: bd72720gpo_set(struct gpio_chip * chip,unsigned int offset,int value)
- Line: 110
- Calls: gpiochip_get_data

### gpo_bd72720_probe
- Return type: static int
- Signature: gpo_bd72720_probe(struct platform_device * pdev)
- Line: 238

## Structs (1)

### bd72720_gpio
- Line: 63
- Members:
  - chip: gpio_chip
  - dev: device *
  - regmap: regmap *
  - gpio_is_input: int

## Enums (2)

### __anon77d16f100103
- Line: 53

### bd72720_gpio_state
- Line: 47

## Variables (3)

- static **bd72720_gpio_id** : const struct platform_device_id[] (line 265)
- static **bd72720gpo_chip** : const struct gpio_chip (line 225)
- static **gpo_bd72720_driver** : platform_driver (line 271)

## Macros (3)

- **BD72720_GPIO_CMOS** (line 17)
- **BD72720_GPIO_OPEN_DRAIN** (line 16)
- **BD72720_INT_GPIO1_IN_SRC** (line 18)
