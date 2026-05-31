# drivers/gpio/gpio-rc5t583.c

Subsystem: drivers/gpio

## Functions (8)

### rc5t583_gpio_dir_input
- Return type: static int
- Signature: rc5t583_gpio_dir_input(struct gpio_chip * gc,unsigned int offset)
- Line: 54
- Calls: gpiochip_get_data

### rc5t583_gpio_dir_output
- Return type: static int
- Signature: rc5t583_gpio_dir_output(struct gpio_chip * gc,unsigned offset,int value)
- Line: 68
- Calls: gpiochip_get_data, rc5t583_gpio_set

### rc5t583_gpio_free
- Return type: static void
- Signature: rc5t583_gpio_free(struct gpio_chip * gc,unsigned offset)
- Line: 97
- Calls: gpiochip_get_data

### rc5t583_gpio_get
- Return type: static int
- Signature: rc5t583_gpio_get(struct gpio_chip * gc,unsigned int offset)
- Line: 24
- Calls: gpiochip_get_data

### rc5t583_gpio_init
- Return type: static int __init
- Signature: rc5t583_gpio_init(void)
- Line: 144

### rc5t583_gpio_probe
- Return type: static int
- Signature: rc5t583_gpio_probe(struct platform_device * pdev)
- Line: 105

### rc5t583_gpio_set
- Return type: static int
- Signature: rc5t583_gpio_set(struct gpio_chip * gc,unsigned int offset,int val)
- Line: 38
- Calls: gpiochip_get_data
- Called by: rc5t583_gpio_dir_output

### rc5t583_gpio_to_irq
- Return type: static int
- Signature: rc5t583_gpio_to_irq(struct gpio_chip * gc,unsigned offset)
- Line: 87
- Calls: gpiochip_get_data

## Structs (1)

### rc5t583_gpio
- Line: 19
- Members:
  - gpio_chip: gpio_chip
  - rc5t583: rc5t583 *

## Variables (1)

- static **rc5t583_gpio_driver** : platform_driver (line 137)
