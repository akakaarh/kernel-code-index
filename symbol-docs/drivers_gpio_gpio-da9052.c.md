# drivers/gpio/gpio-da9052.c

Subsystem: drivers/gpio

## Functions (7)

### da9052_gpio_direction_input
- Return type: static int
- Signature: da9052_gpio_direction_input(struct gpio_chip * gc,unsigned offset)
- Line: 108
- Calls: da9052_gpio_port_odd, gpiochip_get_data

### da9052_gpio_direction_output
- Return type: static int
- Signature: da9052_gpio_direction_output(struct gpio_chip * gc,unsigned offset,int value)
- Line: 133
- Calls: da9052_gpio_port_odd, gpiochip_get_data

### da9052_gpio_get
- Return type: static int
- Signature: da9052_gpio_get(struct gpio_chip * gc,unsigned offset)
- Line: 53
- Calls: da9052_gpio_port_odd, gpiochip_get_data

### da9052_gpio_port_odd
- Return type: static unsigned char
- Signature: da9052_gpio_port_odd(unsigned offset)
- Line: 48
- Called by: da9052_gpio_direction_input, da9052_gpio_direction_output, da9052_gpio_get, da9052_gpio_set

### da9052_gpio_probe
- Return type: static int
- Signature: da9052_gpio_probe(struct platform_device * pdev)
- Line: 184

### da9052_gpio_set
- Return type: static int
- Signature: da9052_gpio_set(struct gpio_chip * gc,unsigned int offset,int value)
- Line: 92
- Calls: da9052_gpio_port_odd, gpiochip_get_data

### da9052_gpio_to_irq
- Return type: static int
- Signature: da9052_gpio_to_irq(struct gpio_chip * gc,u32 offset)
- Line: 159
- Calls: gpiochip_get_data

## Structs (1)

### da9052_gpio
- Line: 43
- Members:
  - da9052: da9052 *
  - gp: gpio_chip

## Variables (2)

- static **da9052_gpio_driver** : platform_driver (line 203)
- static **reference_gp** : const struct gpio_chip (line 171)

## Macros (17)

- **DA9052_ACTIVE_HIGH** (line 32)
- **DA9052_ACTIVE_LOW** (line 31)
- **DA9052_DEBOUNCING_OFF** (line 26)
- **DA9052_DEBOUNCING_ON** (line 27)
- **DA9052_GPIO_EVEN_SHIFT** (line 41)
- **DA9052_GPIO_MASK_LOWER_NIBBLE** (line 37)
- **DA9052_GPIO_MASK_UPPER_NIBBLE** (line 36)
- **DA9052_GPIO_MAX_PORTS_PER_REGISTER** (line 34)
- **DA9052_GPIO_NIBBLE_SHIFT** (line 38)
- **DA9052_GPIO_ODD_SHIFT** (line 40)
- **DA9052_GPIO_SHIFT_COUNT**(no) (line 35)
- **DA9052_INPUT** (line 20)
- **DA9052_IRQ_GPI0** (line 39)
- **DA9052_OUTPUT_LOWLEVEL** (line 29)
- **DA9052_OUTPUT_OPENDRAIN** (line 21)
- **DA9052_OUTPUT_PUSHPULL** (line 22)
- **DA9052_SUPPLY_VDD_IO1** (line 24)
