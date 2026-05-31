# drivers/gpio/gpio-nomadik.c

Subsystem: drivers/gpio

## Functions (26)

### __nmk_gpio_irq_modify
- Return type: static void
- Signature: __nmk_gpio_irq_modify(struct nmk_gpio_chip * nmk_chip,int offset,enum nmk_gpio_irq_type which,bool enable)
- Line: 93
- Called by: __nmk_gpio_set_wake, nmk_gpio_irq_maskunmask, nmk_gpio_irq_set_type

### __nmk_gpio_make_output
- Return type: void
- Signature: __nmk_gpio_make_output(struct nmk_gpio_chip * nmk_chip,unsigned int offset,int val)
- Line: 69
- Calls: __nmk_gpio_set_output
- Called by: nmk_gpio_make_output

### __nmk_gpio_set_output
- Return type: static void
- Signature: __nmk_gpio_set_output(struct nmk_gpio_chip * nmk_chip,unsigned int offset,int val)
- Line: 60
- Called by: __nmk_gpio_make_output, nmk_gpio_set_output

### __nmk_gpio_set_slpm
- Return type: void
- Signature: __nmk_gpio_set_slpm(struct nmk_gpio_chip * nmk_chip,unsigned int offset,enum nmk_gpio_slpm mode)
- Line: 43
- Called by: __nmk_gpio_set_wake

### __nmk_gpio_set_wake
- Return type: static void
- Signature: __nmk_gpio_set_wake(struct nmk_gpio_chip * nmk_chip,int offset,bool on)
- Line: 134
- Calls: __nmk_gpio_irq_modify, __nmk_gpio_set_slpm
- Called by: nmk_gpio_irq_maskunmask, nmk_gpio_irq_set_wake

### nmk_gpio_dbg_show
- Return type: static void
- Signature: nmk_gpio_dbg_show(struct seq_file * s,struct gpio_chip * chip)
- Line: 484
- Calls: nmk_gpio_dbg_show_one

### nmk_gpio_dbg_show_one
- Return type: void
- Signature: nmk_gpio_dbg_show_one(struct seq_file * s,struct pinctrl_dev * pctldev,struct gpio_chip * chip,unsigned int offset)
- Line: 399
- Calls: desc_to_gpio, gpio_device_get_desc, gpiochip_dup_line_label, gpiochip_get_data, nmk_gpio_get_input, nmk_gpio_get_mode
- Called by: nmk_gpio_dbg_show

### nmk_gpio_get_dir
- Return type: static int
- Signature: nmk_gpio_get_dir(struct gpio_chip * chip,unsigned int offset)
- Line: 307
- Calls: gpiochip_get_data

### nmk_gpio_get_input
- Return type: static int
- Signature: nmk_gpio_get_input(struct gpio_chip * chip,unsigned int offset)
- Line: 337
- Calls: gpiochip_get_data
- Called by: nmk_gpio_dbg_show_one

### nmk_gpio_get_mode
- Return type: static int
- Signature: nmk_gpio_get_mode(struct nmk_gpio_chip * nmk_chip,int offset)
- Line: 381
- Called by: nmk_gpio_dbg_show_one

### nmk_gpio_init
- Return type: static int __init
- Signature: nmk_gpio_init(void)
- Line: 733

### nmk_gpio_irq_ack
- Return type: static void
- Signature: nmk_gpio_irq_ack(struct irq_data * d)
- Line: 78
- Calls: gpiochip_get_data

### nmk_gpio_irq_handler
- Return type: static irqreturn_t
- Signature: nmk_gpio_irq_handler(int irq,void * dev_id)
- Line: 281

### nmk_gpio_irq_mask
- Return type: static void
- Signature: nmk_gpio_irq_mask(struct irq_data * d)
- Line: 173
- Calls: gpiochip_disable_irq, gpiochip_get_data, nmk_gpio_irq_maskunmask
- Called by: nmk_gpio_irq_shutdown

### nmk_gpio_irq_maskunmask
- Return type: static void
- Signature: nmk_gpio_irq_maskunmask(struct nmk_gpio_chip * nmk_chip,struct irq_data * d,bool enable)
- Line: 154
- Calls: __nmk_gpio_irq_modify, __nmk_gpio_set_wake
- Called by: nmk_gpio_irq_mask, nmk_gpio_irq_unmask

### nmk_gpio_irq_print_chip
- Return type: static void
- Signature: nmk_gpio_irq_print_chip(struct irq_data * d,struct seq_file * p)
- Line: 618
- Calls: gpiochip_get_data

### nmk_gpio_irq_set_type
- Return type: static int
- Signature: nmk_gpio_irq_set_type(struct irq_data * d,unsigned int type)
- Line: 220
- Calls: __nmk_gpio_irq_modify, gpiochip_get_data

### nmk_gpio_irq_set_wake
- Return type: static int
- Signature: nmk_gpio_irq_set_wake(struct irq_data * d,unsigned int on)
- Line: 191
- Calls: __nmk_gpio_set_wake, gpiochip_get_data

### nmk_gpio_irq_shutdown
- Return type: static void
- Signature: nmk_gpio_irq_shutdown(struct irq_data * d)
- Line: 272
- Calls: gpiochip_get_data, nmk_gpio_irq_mask

### nmk_gpio_irq_startup
- Return type: static unsigned int
- Signature: nmk_gpio_irq_startup(struct irq_data * d)
- Line: 262
- Calls: gpiochip_get_data, nmk_gpio_irq_unmask

### nmk_gpio_irq_unmask
- Return type: static void
- Signature: nmk_gpio_irq_unmask(struct irq_data * d)
- Line: 182
- Calls: gpiochip_enable_irq, gpiochip_get_data, nmk_gpio_irq_maskunmask
- Called by: nmk_gpio_irq_startup

### nmk_gpio_make_input
- Return type: static int
- Signature: nmk_gpio_make_input(struct gpio_chip * chip,unsigned int offset)
- Line: 324
- Calls: gpiochip_get_data

### nmk_gpio_make_output
- Return type: static int
- Signature: nmk_gpio_make_output(struct gpio_chip * chip,unsigned int offset,int val)
- Line: 365
- Calls: __nmk_gpio_make_output, gpiochip_get_data

### nmk_gpio_populate_chip
- Return type: nmk_gpio_chip *
- Signature: nmk_gpio_populate_chip(struct fwnode_handle * fwnode,struct platform_device * pdev)
- Line: 506
- Called by: nmk_gpio_probe

### nmk_gpio_probe
- Return type: static int
- Signature: nmk_gpio_probe(struct platform_device * pdev)
- Line: 640
- Calls: nmk_gpio_populate_chip

### nmk_gpio_set_output
- Return type: static int
- Signature: nmk_gpio_set_output(struct gpio_chip * chip,unsigned int offset,int val)
- Line: 351
- Calls: __nmk_gpio_set_output, gpiochip_get_data

## Enums (1)

### nmk_gpio_irq_type
- Line: 88

## Variables (3)

- static **nmk_gpio_driver** : platform_driver (line 724)
- static **nmk_gpio_match** : const struct of_device_id[] (line 718)
- static **nmk_irq_chip** : const struct irq_chip (line 627)

## Macros (1)

- **nmk_gpio_dbg_show** (line 496)
