# drivers/gpio/gpio-moxtet.c

Subsystem: drivers/gpio

## Functions (6)

### moxtet_gpio_direction_input
- Return type: static int
- Signature: moxtet_gpio_direction_input(struct gpio_chip * gc,unsigned int offset)
- Line: 88
- Calls: gpiochip_get_data

### moxtet_gpio_direction_output
- Return type: static int
- Signature: moxtet_gpio_direction_output(struct gpio_chip * gc,unsigned int offset,int val)
- Line: 101
- Calls: gpiochip_get_data, moxtet_gpio_set_value

### moxtet_gpio_get_direction
- Return type: static int
- Signature: moxtet_gpio_get_direction(struct gpio_chip * gc,unsigned int offset)
- Line: 75
- Calls: gpiochip_get_data

### moxtet_gpio_get_value
- Return type: static int
- Signature: moxtet_gpio_get_value(struct gpio_chip * gc,unsigned int offset)
- Line: 34
- Calls: gpiochip_get_data

### moxtet_gpio_probe
- Return type: static int
- Signature: moxtet_gpio_probe(struct device * dev)
- Line: 114

### moxtet_gpio_set_value
- Return type: static int
- Signature: moxtet_gpio_set_value(struct gpio_chip * gc,unsigned int offset,int val)
- Line: 55
- Calls: gpiochip_get_data
- Called by: moxtet_gpio_direction_output

## Structs (2)

### moxtet_gpio_chip
- Line: 28
- Members:
  - in_mask: u16
  - out_mask: u16
  - dev: device *
  - gpio_chip: gpio_chip
  - desc: const struct moxtet_gpio_desc *

### moxtet_gpio_desc
- Line: 16
- Members:
  - in_mask: u16
  - out_mask: u16
  - dev: device *
  - gpio_chip: gpio_chip
  - desc: const struct moxtet_gpio_desc *

## Enums (1)

### moxtet_gpio_module_table
- Line: 160

## Variables (3)

- static **descs** : const struct moxtet_gpio_desc[] (line 21)
- static **moxtet_gpio_driver** : moxtet_driver (line 165)
- static **moxtet_gpio_dt_ids** : const struct of_device_id[] (line 154)

## Macros (2)

- **MOXTET_GPIO_INPUTS** (line 14)
- **MOXTET_GPIO_NGPIOS** (line 13)
