# drivers/gpio/gpio-idt3243x.c

Subsystem: drivers/gpio

## Functions (7)

### idt_gpio_ack
- Return type: static void
- Signature: idt_gpio_ack(struct irq_data * d)
- Line: 74
- Calls: gpiochip_get_data

### idt_gpio_dispatch
- Return type: static void
- Signature: idt_gpio_dispatch(struct irq_desc * desc)
- Line: 28
- Calls: gpiochip_get_data

### idt_gpio_irq_init_hw
- Return type: static int
- Signature: idt_gpio_irq_init_hw(struct gpio_chip * gc)
- Line: 108
- Calls: gpiochip_get_data

### idt_gpio_irq_set_type
- Return type: static int
- Signature: idt_gpio_irq_set_type(struct irq_data * d,unsigned int flow_type)
- Line: 49
- Calls: gpiochip_get_data

### idt_gpio_mask
- Return type: static void
- Signature: idt_gpio_mask(struct irq_data * d)
- Line: 82
- Calls: gpiochip_disable_irq, gpiochip_get_data

### idt_gpio_probe
- Return type: static int
- Signature: idt_gpio_probe(struct platform_device * pdev)
- Line: 129
- Calls: gpio_generic_chip_init

### idt_gpio_unmask
- Return type: static void
- Signature: idt_gpio_unmask(struct irq_data * d)
- Line: 95
- Calls: gpiochip_enable_irq, gpiochip_get_data

## Structs (1)

### idt_gpio_ctrl
- Line: 21
- Members:
  - chip: gpio_generic_chip
  - pic: void __iomem *
  - gpio: void __iomem *
  - mask_cache: u32

## Variables (3)

- static **idt_gpio_driver** : platform_driver (line 201)
- static **idt_gpio_irqchip** : const struct irq_chip (line 119)
- static **idt_gpio_of_match** : const struct of_device_id[] (line 195)

## Macros (6)

- **IDT_GPIO_DATA** (line 17)
- **IDT_GPIO_DIR** (line 16)
- **IDT_GPIO_ILEVEL** (line 18)
- **IDT_GPIO_ISTAT** (line 19)
- **IDT_PIC_IRQ_MASK** (line 14)
- **IDT_PIC_IRQ_PEND** (line 13)
