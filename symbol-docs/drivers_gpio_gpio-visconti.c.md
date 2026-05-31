# drivers/gpio/gpio-visconti.c

Subsystem: drivers/gpio

## Functions (7)

### visconti_gpio_child_to_parent_hwirq
- Return type: static int
- Signature: visconti_gpio_child_to_parent_hwirq(struct gpio_chip * gc,unsigned int child,unsigned int child_type,unsigned int * parent,unsigned int * parent_type)
- Line: 93

### visconti_gpio_irq_print_chip
- Return type: static void
- Signature: visconti_gpio_irq_print_chip(struct irq_data * d,struct seq_file * p)
- Line: 141
- Calls: gpiochip_get_data

### visconti_gpio_irq_set_type
- Return type: static int
- Signature: visconti_gpio_irq_set_type(struct irq_data * d,unsigned int type)
- Line: 40
- Calls: gpiochip_get_data

### visconti_gpio_mask_irq
- Return type: static void
- Signature: visconti_gpio_mask_irq(struct irq_data * d)
- Line: 125
- Calls: gpiochip_disable_irq

### visconti_gpio_populate_parent_fwspec
- Return type: static int
- Signature: visconti_gpio_populate_parent_fwspec(struct gpio_chip * chip,union gpio_irq_fwspec * gfwspec,unsigned int parent_hwirq,unsigned int parent_type)
- Line: 109

### visconti_gpio_probe
- Return type: static int
- Signature: visconti_gpio_probe(struct platform_device * pdev)
- Line: 160
- Calls: gpio_generic_chip_init

### visconti_gpio_unmask_irq
- Return type: static void
- Signature: visconti_gpio_unmask_irq(struct irq_data * d)
- Line: 133
- Calls: gpiochip_enable_irq

## Structs (1)

### visconti_gpio
- Line: 33
- Members:
  - base: void __iomem *
  - lock: spinlock_t
  - chip: gpio_generic_chip
  - dev: device *

## Variables (3)

- static **visconti_gpio_driver** : platform_driver (line 227)
- static **visconti_gpio_irq_chip** : const struct irq_chip (line 149)
- static **visconti_gpio_of_match** : const struct of_device_id[] (line 221)

## Macros (7)

- **BASE_HW_IRQ** (line 31)
- **GPIO_DIR** (line 24)
- **GPIO_IDATA** (line 25)
- **GPIO_INTMODE** (line 29)
- **GPIO_OCLR** (line 28)
- **GPIO_ODATA** (line 26)
- **GPIO_OSET** (line 27)
