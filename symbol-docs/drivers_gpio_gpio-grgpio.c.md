# drivers/gpio/gpio-grgpio.c

Subsystem: drivers/gpio

## Functions (10)

### grgpio_irq_domain_remove
- Return type: static void
- Signature: grgpio_irq_domain_remove(void * data)
- Line: 311

### grgpio_irq_handler
- Return type: static irqreturn_t
- Signature: grgpio_irq_handler(int irq,void * dev)
- Line: 191

### grgpio_irq_map
- Return type: static int
- Signature: grgpio_irq_map(struct irq_domain * d,unsigned int irq,irq_hw_number_t hwirq)
- Line: 224

### grgpio_irq_mask
- Return type: static void
- Signature: grgpio_irq_mask(struct irq_data * d)
- Line: 159
- Calls: gpiochip_disable_irq, grgpio_set_imask

### grgpio_irq_set_type
- Return type: static int
- Signature: grgpio_irq_set_type(struct irq_data * d,unsigned int type)
- Line: 118

### grgpio_irq_unmap
- Return type: static void
- Signature: grgpio_irq_unmap(struct irq_domain * d,unsigned int irq)
- Line: 271
- Calls: grgpio_set_imask

### grgpio_irq_unmask
- Return type: static void
- Signature: grgpio_irq_unmask(struct irq_data * d)
- Line: 170
- Calls: gpiochip_enable_irq, grgpio_set_imask

### grgpio_probe
- Return type: static int
- Signature: grgpio_probe(struct platform_device * ofdev)
- Line: 325
- Calls: gpio_generic_chip_init

### grgpio_set_imask
- Return type: static void
- Signature: grgpio_set_imask(struct grgpio_priv * priv,unsigned int offset,int val)
- Line: 92
- Called by: grgpio_irq_mask, grgpio_irq_unmap, grgpio_irq_unmask

### grgpio_to_irq
- Return type: static int
- Signature: grgpio_to_irq(struct gpio_chip * gc,unsigned offset)
- Line: 103
- Calls: gpiochip_get_data

## Structs (3)

### grgpio_lirq
- Line: 57
- Members:
  - refcnt: atomic_t
  - uirq: u8
  - index: s8
  - irq: u8
  - chip: gpio_generic_chip
  - regs: void __iomem *
  - dev: device *
  - imask: u32
  - domain: irq_domain *
  - uirqs: grgpio_uirq[]
  - lirqs: grgpio_lirq[]

### grgpio_priv
- Line: 62
- Members:
  - refcnt: atomic_t
  - uirq: u8
  - index: s8
  - irq: u8
  - chip: gpio_generic_chip
  - regs: void __iomem *
  - dev: device *
  - imask: u32
  - domain: irq_domain *
  - uirqs: grgpio_uirq[]
  - lirqs: grgpio_lirq[]

### grgpio_uirq
- Line: 48
- Members:
  - refcnt: atomic_t
  - uirq: u8
  - index: s8
  - irq: u8
  - chip: gpio_generic_chip
  - regs: void __iomem *
  - dev: device *
  - imask: u32
  - domain: irq_domain *
  - uirqs: grgpio_uirq[]
  - lirqs: grgpio_lirq[]

## Variables (4)

- static **grgpio_driver** : platform_driver (line 452)
- static **grgpio_irq_chip** : const struct irq_chip (line 182)
- static **grgpio_irq_domain_ops** : const struct irq_domain_ops (line 318)
- static **grgpio_match** : const struct of_device_id[] (line 444)

## Macros (9)

- **GRGPIO_BYPASS** (line 44)
- **GRGPIO_DATA** (line 38)
- **GRGPIO_DIR** (line 40)
- **GRGPIO_IEDGE** (line 43)
- **GRGPIO_IMAP_BASE** (line 45)
- **GRGPIO_IMASK** (line 41)
- **GRGPIO_IPOL** (line 42)
- **GRGPIO_MAX_NGPIO** (line 36)
- **GRGPIO_OUTPUT** (line 39)
