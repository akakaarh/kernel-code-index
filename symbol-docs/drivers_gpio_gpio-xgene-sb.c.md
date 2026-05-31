# drivers/gpio/gpio-xgene-sb.c

Subsystem: drivers/gpio

## Functions (11)

### xgene_gpio_sb_domain_activate
- Return type: static int
- Signature: xgene_gpio_sb_domain_activate(struct irq_domain * d,struct irq_data * irq_data,bool reserve)
- Line: 152
- Calls: gpiochip_lock_as_irq, xgene_gpio_set_bit

### xgene_gpio_sb_domain_alloc
- Return type: static int
- Signature: xgene_gpio_sb_domain_alloc(struct irq_domain * domain,unsigned int virq,unsigned int nr_irqs,void * data)
- Line: 199

### xgene_gpio_sb_domain_deactivate
- Return type: static void
- Signature: xgene_gpio_sb_domain_deactivate(struct irq_domain * d,struct irq_data * irq_data)
- Line: 173
- Calls: gpiochip_unlock_as_irq, xgene_gpio_set_bit

### xgene_gpio_sb_domain_translate
- Return type: static int
- Signature: xgene_gpio_sb_domain_translate(struct irq_domain * d,struct irq_fwspec * fwspec,unsigned long * hwirq,unsigned int * type)
- Line: 184

### xgene_gpio_sb_irq_mask
- Return type: static void
- Signature: xgene_gpio_sb_irq_mask(struct irq_data * d)
- Line: 108
- Calls: gpiochip_disable_irq

### xgene_gpio_sb_irq_set_type
- Return type: static int
- Signature: xgene_gpio_sb_irq_set_type(struct irq_data * d,unsigned int type)
- Line: 77
- Calls: xgene_gpio_set_bit

### xgene_gpio_sb_irq_unmask
- Return type: static void
- Signature: xgene_gpio_sb_irq_unmask(struct irq_data * d)
- Line: 117
- Calls: gpiochip_enable_irq

### xgene_gpio_sb_probe
- Return type: static int
- Signature: xgene_gpio_sb_probe(struct platform_device * pdev)
- Line: 240
- Calls: acpi_gpiochip_request_interrupts, gpio_generic_chip_init

### xgene_gpio_sb_remove
- Return type: static void
- Signature: xgene_gpio_sb_remove(struct platform_device * pdev)
- Line: 327
- Calls: acpi_gpiochip_free_interrupts

### xgene_gpio_sb_to_irq
- Return type: static int
- Signature: xgene_gpio_sb_to_irq(struct gpio_chip * gc,u32 gpio)
- Line: 136
- Calls: gpiochip_get_data

### xgene_gpio_set_bit
- Return type: static void
- Signature: xgene_gpio_set_bit(struct gpio_chip * gc,void __iomem * reg,u32 gpio,int val)
- Line: 63
- Called by: xgene_gpio_sb_domain_activate, xgene_gpio_sb_domain_deactivate, xgene_gpio_sb_irq_set_type

## Structs (1)

### xgene_gpio_sb
- Line: 51
- Members:
  - chip: gpio_generic_chip
  - regs: void __iomem *
  - irq_domain: irq_domain *
  - irq_start: u16
  - nirq: u16
  - parent_irq_base: u16

## Variables (5)

- static **xgene_gpio_sb_acpi_match** : const struct acpi_device_id[] (line 342)
- static **xgene_gpio_sb_domain_ops** : const struct irq_domain_ops (line 232)
- static **xgene_gpio_sb_driver** : platform_driver (line 348)
- static **xgene_gpio_sb_irq_chip** : const struct irq_chip (line 126)
- static **xgene_gpio_sb_of_match** : const struct of_device_id[] (line 336)

## Macros (13)

- **GPIO_INT_LEVEL_H** (line 39)
- **GPIO_INT_LEVEL_L** (line 40)
- **GPIO_MASK**(x) (line 31)
- **GPIO_TO_HWIRQ**(priv,gpio) (line 61)
- **HWIRQ_TO_GPIO**(priv,hwirq) (line 60)
- **MPA_GPIO_INT_LVL** (line 33)
- **MPA_GPIO_IN_ADDR** (line 36)
- **MPA_GPIO_OE_ADDR** (line 34)
- **MPA_GPIO_OUT_ADDR** (line 35)
- **MPA_GPIO_SEL_LO** (line 37)
- **XGENE_DFLT_IRQ_START_PIN** (line 30)
- **XGENE_DFLT_MAX_NGPIO** (line 28)
- **XGENE_DFLT_MAX_NIRQ** (line 29)
