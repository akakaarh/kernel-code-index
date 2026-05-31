# drivers/gpio/gpio-wm8994.c

Subsystem: drivers/gpio

## Functions (12)

### wm8994_gpio_dbg_show
- Return type: static void
- Signature: wm8994_gpio_dbg_show(struct seq_file * s,struct gpio_chip * chip)
- Line: 190
- Calls: gpiochip_dup_line_label, gpiochip_get_data, wm8994_gpio_fn

### wm8994_gpio_direction_in
- Return type: static int
- Signature: wm8994_gpio_direction_in(struct gpio_chip * chip,unsigned offset)
- Line: 54
- Calls: gpiochip_get_data

### wm8994_gpio_direction_out
- Return type: static int
- Signature: wm8994_gpio_direction_out(struct gpio_chip * chip,unsigned offset,int value)
- Line: 79
- Calls: gpiochip_get_data

### wm8994_gpio_exit
- Return type: static void __exit
- Signature: wm8994_gpio_exit(void)
- Line: 298

### wm8994_gpio_fn
- Return type: static const char *
- Signature: wm8994_gpio_fn(u16 fn)
- Line: 136
- Called by: wm8994_gpio_dbg_show

### wm8994_gpio_get
- Return type: static int
- Signature: wm8994_gpio_get(struct gpio_chip * chip,unsigned offset)
- Line: 63
- Calls: gpiochip_get_data

### wm8994_gpio_init
- Return type: static int __init
- Signature: wm8994_gpio_init(void)
- Line: 292

### wm8994_gpio_probe
- Return type: static int
- Signature: wm8994_gpio_probe(struct platform_device * pdev)
- Line: 264

### wm8994_gpio_request
- Return type: static int
- Signature: wm8994_gpio_request(struct gpio_chip * chip,unsigned offset)
- Line: 31
- Calls: gpiochip_get_data

### wm8994_gpio_set
- Return type: static int
- Signature: wm8994_gpio_set(struct gpio_chip * chip,unsigned int offset,int value)
- Line: 92
- Calls: gpiochip_get_data

### wm8994_gpio_set_config
- Return type: static int
- Signature: wm8994_gpio_set_config(struct gpio_chip * chip,unsigned int offset,unsigned long config)
- Line: 105
- Calls: gpiochip_get_data

### wm8994_gpio_to_irq
- Return type: static int
- Signature: wm8994_gpio_to_irq(struct gpio_chip * chip,unsigned offset)
- Line: 126
- Calls: gpiochip_get_data

## Structs (1)

### wm8994_gpio
- Line: 26
- Members:
  - wm8994: wm8994 *
  - gpio_chip: gpio_chip

## Variables (2)

- static **template_chip** : const struct gpio_chip (line 250)
- static **wm8994_gpio_driver** : platform_driver (line 287)

## Macros (1)

- **wm8994_gpio_dbg_show** (line 247)
