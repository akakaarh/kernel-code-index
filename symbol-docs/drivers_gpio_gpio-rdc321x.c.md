# drivers/gpio/gpio-rdc321x.c

Subsystem: drivers/gpio

## Functions (6)

### rdc321x_gpio_probe
- Return type: static int
- Signature: rdc321x_gpio_probe(struct platform_device * pdev)
- Line: 119

### rdc_gpio_config
- Return type: static int
- Signature: rdc_gpio_config(struct gpio_chip * chip,unsigned gpio,int value)
- Line: 80
- Calls: gpiochip_get_data, rdc_gpio_set_value_impl
- Called by: rdc_gpio_direction_input

### rdc_gpio_direction_input
- Return type: static int
- Signature: rdc_gpio_direction_input(struct gpio_chip * chip,unsigned gpio)
- Line: 111
- Calls: rdc_gpio_config

### rdc_gpio_get_value
- Return type: static int
- Signature: rdc_gpio_get_value(struct gpio_chip * chip,unsigned gpio)
- Line: 30
- Calls: gpiochip_get_data

### rdc_gpio_set_value
- Return type: static int
- Signature: rdc_gpio_set_value(struct gpio_chip * chip,unsigned int gpio,int value)
- Line: 67
- Calls: gpiochip_get_data, rdc_gpio_set_value_impl

### rdc_gpio_set_value_impl
- Return type: static void
- Signature: rdc_gpio_set_value_impl(struct gpio_chip * chip,unsigned gpio,int value)
- Line: 48
- Calls: gpiochip_get_data
- Called by: rdc_gpio_config, rdc_gpio_set_value

## Structs (1)

### rdc321x_gpio
- Line: 18
- Members:
  - lock: spinlock_t
  - sb_pdev: pci_dev *
  - data_reg: u32[2]
  - reg1_ctrl_base: int
  - reg1_data_base: int
  - reg2_ctrl_base: int
  - reg2_data_base: int
  - chip: gpio_chip

## Variables (1)

- static **rdc321x_gpio_driver** : platform_driver (line 189)
