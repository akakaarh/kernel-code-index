# drivers/gpio/gpio-altera.c

Subsystem: drivers/gpio

## Functions (13)

### altera_gpio_direction_input
- Return type: static int
- Signature: altera_gpio_direction_input(struct gpio_chip * gc,unsigned offset)
- Line: 134
- Calls: gpiochip_get_data

### altera_gpio_direction_output
- Return type: static int
- Signature: altera_gpio_direction_output(struct gpio_chip * gc,unsigned offset,int value)
- Line: 150
- Calls: gpiochip_get_data

### altera_gpio_exit
- Return type: static void __exit
- Signature: altera_gpio_exit(void)
- Line: 332

### altera_gpio_get
- Return type: static int
- Signature: altera_gpio_get(struct gpio_chip * gc,unsigned offset)
- Line: 109
- Calls: gpiochip_get_data

### altera_gpio_init
- Return type: static int __init
- Signature: altera_gpio_init(void)
- Line: 326

### altera_gpio_irq_edge_handler
- Return type: static void
- Signature: altera_gpio_irq_edge_handler(struct irq_desc * desc)
- Line: 175
- Calls: gpiochip_get_data

### altera_gpio_irq_leveL_high_handler
- Return type: static void
- Signature: altera_gpio_irq_leveL_high_handler(struct irq_desc * desc)
- Line: 199
- Calls: gpiochip_get_data

### altera_gpio_irq_mask
- Return type: static void
- Signature: altera_gpio_irq_mask(struct irq_data * d)
- Line: 60
- Calls: gpiochip_disable_irq, gpiochip_get_data

### altera_gpio_irq_set_type
- Return type: static int
- Signature: altera_gpio_irq_set_type(struct irq_data * d,unsigned int type)
- Line: 81
- Calls: gpiochip_get_data

### altera_gpio_irq_startup
- Return type: static unsigned int
- Signature: altera_gpio_irq_startup(struct irq_data * d)
- Line: 102
- Calls: altera_gpio_irq_unmask

### altera_gpio_irq_unmask
- Return type: static void
- Signature: altera_gpio_irq_unmask(struct irq_data * d)
- Line: 43
- Calls: gpiochip_enable_irq, gpiochip_get_data
- Called by: altera_gpio_irq_startup

### altera_gpio_probe
- Return type: static int
- Signature: altera_gpio_probe(struct platform_device * pdev)
- Line: 232

### altera_gpio_set
- Return type: static int
- Signature: altera_gpio_set(struct gpio_chip * gc,unsigned int offset,int value)
- Line: 116
- Calls: gpiochip_get_data

## Structs (1)

### altera_gpio_chip
- Line: 36
- Members:
  - gc: gpio_chip
  - regs: void __iomem *
  - gpio_lock: raw_spinlock_t
  - interrupt_trigger: int

## Variables (3)

- static **altera_gpio_driver** : platform_driver (line 318)
- static **altera_gpio_irq_chip** : const struct irq_chip (line 221)
- static **altera_gpio_of_match** : const struct of_device_id[] (line 312)

## Macros (5)

- **ALTERA_GPIO_DATA** (line 22)
- **ALTERA_GPIO_DIR** (line 23)
- **ALTERA_GPIO_EDGE_CAP** (line 25)
- **ALTERA_GPIO_IRQ_MASK** (line 24)
- **ALTERA_GPIO_MAX_NGPIO** (line 21)
