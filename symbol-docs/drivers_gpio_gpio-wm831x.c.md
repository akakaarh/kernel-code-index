# drivers/gpio/gpio-wm831x.c

Subsystem: drivers/gpio

## Functions (11)

### wm831x_gpio_dbg_show
- Return type: static void
- Signature: wm831x_gpio_dbg_show(struct seq_file * s,struct gpio_chip * chip)
- Line: 155
- Calls: gpiochip_dup_line_label, gpiochip_get_data, wm831x_gpio_get

### wm831x_gpio_direction_in
- Return type: static int
- Signature: wm831x_gpio_direction_in(struct gpio_chip * chip,unsigned offset)
- Line: 31
- Calls: gpiochip_get_data

### wm831x_gpio_direction_out
- Return type: static int
- Signature: wm831x_gpio_direction_out(struct gpio_chip * chip,unsigned offset,int value)
- Line: 71
- Calls: gpiochip_get_data, wm831x_gpio_set

### wm831x_gpio_exit
- Return type: static void __exit
- Signature: wm831x_gpio_exit(void)
- Line: 298

### wm831x_gpio_get
- Return type: static int
- Signature: wm831x_gpio_get(struct gpio_chip * chip,unsigned offset)
- Line: 45
- Calls: gpiochip_get_data
- Called by: wm831x_gpio_dbg_show

### wm831x_gpio_init
- Return type: static int __init
- Signature: wm831x_gpio_init(void)
- Line: 292

### wm831x_gpio_probe
- Return type: static int
- Signature: wm831x_gpio_probe(struct platform_device * pdev)
- Line: 262

### wm831x_gpio_set
- Return type: static int
- Signature: wm831x_gpio_set(struct gpio_chip * chip,unsigned int offset,int value)
- Line: 61
- Calls: gpiochip_get_data
- Called by: wm831x_gpio_direction_out

### wm831x_gpio_set_debounce
- Return type: static int
- Signature: wm831x_gpio_set_debounce(struct wm831x * wm831x,unsigned offset,unsigned debounce)
- Line: 101
- Called by: wm831x_set_config

### wm831x_gpio_to_irq
- Return type: static int
- Signature: wm831x_gpio_to_irq(struct gpio_chip * chip,unsigned offset)
- Line: 92
- Calls: gpiochip_get_data

### wm831x_set_config
- Return type: static int
- Signature: wm831x_set_config(struct gpio_chip * chip,unsigned int offset,unsigned long config)
- Line: 130
- Calls: gpiochip_get_data, wm831x_gpio_set_debounce

## Structs (1)

### wm831x_gpio
- Line: 26
- Members:
  - wm831x: wm831x *
  - gpio_chip: gpio_chip

## Variables (2)

- static **template_chip** : const struct gpio_chip (line 249)
- static **wm831x_gpio_driver** : platform_driver (line 287)

## Macros (1)

- **wm831x_gpio_dbg_show** (line 246)
