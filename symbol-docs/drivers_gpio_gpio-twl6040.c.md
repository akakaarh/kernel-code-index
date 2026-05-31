# drivers/gpio/gpio-twl6040.c

Subsystem: drivers/gpio

## Functions (5)

### gpo_twl6040_probe
- Return type: static int
- Signature: gpo_twl6040_probe(struct platform_device * pdev)
- Line: 78

### twl6040gpo_direction_out
- Return type: static int
- Signature: twl6040gpo_direction_out(struct gpio_chip * chip,unsigned int offset,int value)
- Line: 59
- Calls: twl6040gpo_set

### twl6040gpo_get
- Return type: static int
- Signature: twl6040gpo_get(struct gpio_chip * chip,unsigned offset)
- Line: 23
- Calls: gpiochip_get_data

### twl6040gpo_get_direction
- Return type: static int
- Signature: twl6040gpo_get_direction(struct gpio_chip * chip,unsigned offset)
- Line: 35

### twl6040gpo_set
- Return type: static int
- Signature: twl6040gpo_set(struct gpio_chip * chip,unsigned int offset,int value)
- Line: 40
- Calls: gpiochip_get_data
- Called by: twl6040gpo_direction_out

## Variables (2)

- static **gpo_twl6040_driver** : platform_driver (line 107)
- static **twl6040gpo_chip** : gpio_chip (line 66)
