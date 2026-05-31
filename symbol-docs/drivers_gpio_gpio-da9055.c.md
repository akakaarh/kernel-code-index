# drivers/gpio/gpio-da9055.c

Subsystem: drivers/gpio

## Functions (8)

### da9055_gpio_direction_input
- Return type: static int
- Signature: da9055_gpio_direction_input(struct gpio_chip * gc,unsigned offset)
- Line: 70
- Calls: gpiochip_get_data

### da9055_gpio_direction_output
- Return type: static int
- Signature: da9055_gpio_direction_output(struct gpio_chip * gc,unsigned offset,int value)
- Line: 85
- Calls: da9055_gpio_set, gpiochip_get_data

### da9055_gpio_exit
- Return type: static void __exit
- Signature: da9055_gpio_exit(void)
- Line: 160

### da9055_gpio_get
- Return type: static int
- Signature: da9055_gpio_get(struct gpio_chip * gc,unsigned offset)
- Line: 33
- Calls: gpiochip_get_data

### da9055_gpio_init
- Return type: static int __init
- Signature: da9055_gpio_init(void)
- Line: 154

### da9055_gpio_probe
- Return type: static int
- Signature: da9055_gpio_probe(struct platform_device * pdev)
- Line: 128

### da9055_gpio_set
- Return type: static int
- Signature: da9055_gpio_set(struct gpio_chip * gc,unsigned int offset,int value)
- Line: 62
- Calls: gpiochip_get_data
- Called by: da9055_gpio_direction_output

### da9055_gpio_to_irq
- Return type: static int
- Signature: da9055_gpio_to_irq(struct gpio_chip * gc,u32 offset)
- Line: 106
- Calls: gpiochip_get_data

## Structs (1)

### da9055_gpio
- Line: 28
- Members:
  - da9055: da9055 *
  - gp: gpio_chip

## Variables (2)

- static **da9055_gpio_driver** : platform_driver (line 147)
- static **reference_gp** : const struct gpio_chip (line 115)

## Macros (9)

- **DA9055_ACT_LOW** (line 19)
- **DA9055_GPI** (line 20)
- **DA9055_INPUT** (line 24)
- **DA9055_IRQ_GPI0** (line 26)
- **DA9055_OUTPUT** (line 25)
- **DA9055_PORT_MASK** (line 21)
- **DA9055_PORT_SHIFT**(offset) (line 22)
- **DA9055_PUSH_PULL** (line 18)
- **DA9055_VDD_IO** (line 17)
