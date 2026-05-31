# drivers/gpio/gpio-wm8350.c

Subsystem: drivers/gpio

## Functions (8)

### wm8350_gpio_direction_in
- Return type: static int
- Signature: wm8350_gpio_direction_in(struct gpio_chip * chip,unsigned offset)
- Line: 26
- Calls: gpiochip_get_data

### wm8350_gpio_direction_out
- Return type: static int
- Signature: wm8350_gpio_direction_out(struct gpio_chip * chip,unsigned offset,int value)
- Line: 63
- Calls: gpiochip_get_data, wm8350_gpio_set

### wm8350_gpio_exit
- Return type: static void __exit
- Signature: wm8350_gpio_exit(void)
- Line: 135

### wm8350_gpio_get
- Return type: static int
- Signature: wm8350_gpio_get(struct gpio_chip * chip,unsigned offset)
- Line: 35
- Calls: gpiochip_get_data

### wm8350_gpio_init
- Return type: static int __init
- Signature: wm8350_gpio_init(void)
- Line: 129

### wm8350_gpio_probe
- Return type: static int
- Signature: wm8350_gpio_probe(struct platform_device * pdev)
- Line: 101

### wm8350_gpio_set
- Return type: static int
- Signature: wm8350_gpio_set(struct gpio_chip * chip,unsigned int offset,int value)
- Line: 51
- Calls: gpiochip_get_data
- Called by: wm8350_gpio_direction_out

### wm8350_gpio_to_irq
- Return type: static int
- Signature: wm8350_gpio_to_irq(struct gpio_chip * chip,unsigned offset)
- Line: 79
- Calls: gpiochip_get_data

## Structs (1)

### wm8350_gpio_data
- Line: 21
- Members:
  - wm8350: wm8350 *
  - gpio_chip: gpio_chip

## Variables (2)

- static **template_chip** : const struct gpio_chip (line 90)
- static **wm8350_gpio_driver** : platform_driver (line 124)
