# drivers/gpio/gpio-cadence.c

Subsystem: drivers/gpio

## Functions (8)

### cdns_gpio_free
- Return type: static void
- Signature: cdns_gpio_free(struct gpio_chip * chip,unsigned int offset)
- Line: 66
- Calls: gpiochip_get_data

### cdns_gpio_irq_handler
- Return type: static void
- Signature: cdns_gpio_irq_handler(struct irq_desc * desc)
- Line: 142
- Calls: gpiochip_get_data

### cdns_gpio_irq_mask
- Return type: static void
- Signature: cdns_gpio_irq_mask(struct irq_data * d)
- Line: 77
- Calls: gpiochip_disable_irq, gpiochip_get_data

### cdns_gpio_irq_set_type
- Return type: static int
- Signature: cdns_gpio_irq_set_type(struct irq_data * d,unsigned int type)
- Line: 95
- Calls: gpiochip_get_data

### cdns_gpio_irq_unmask
- Return type: static void
- Signature: cdns_gpio_irq_unmask(struct irq_data * d)
- Line: 86
- Calls: gpiochip_enable_irq, gpiochip_get_data

### cdns_gpio_probe
- Return type: static int
- Signature: cdns_gpio_probe(struct platform_device * pdev)
- Line: 183
- Calls: gpio_generic_chip_init

### cdns_gpio_remove
- Return type: static void
- Signature: cdns_gpio_remove(struct platform_device * pdev)
- Line: 308

### cdns_gpio_request
- Return type: static int
- Signature: cdns_gpio_request(struct gpio_chip * chip,unsigned int offset)
- Line: 54
- Calls: gpiochip_get_data

## Structs (2)

### cdns_gpio_chip
- Line: 39
- Members:
  - skip_init: bool
  - gen_gc: gpio_generic_chip
  - regs: void __iomem *
  - bypass_orig: u32
  - quirks: const struct cdns_gpio_quirks *

### cdns_gpio_quirks
- Line: 35
- Members:
  - skip_init: bool
  - gen_gc: gpio_generic_chip
  - regs: void __iomem *
  - bypass_orig: u32
  - quirks: const struct cdns_gpio_quirks *

## Variables (5)

- static **ax3000_gpio_quirks** : const struct cdns_gpio_quirks (line 50)
- static **cdns_default_quirks** : const struct cdns_gpio_quirks (line 46)
- static **cdns_gpio_driver** : platform_driver (line 315)
- static **cdns_gpio_irqchip** : const struct irq_chip (line 161)
- static **cdns_of_ids** : const struct of_device_id[] (line 170)

## Macros (12)

- **CDNS_GPIO_BYPASS_MODE** (line 22)
- **CDNS_GPIO_DIRECTION_MODE** (line 23)
- **CDNS_GPIO_INPUT_VALUE** (line 26)
- **CDNS_GPIO_IRQ_ANY_EDGE** (line 33)
- **CDNS_GPIO_IRQ_DIS** (line 29)
- **CDNS_GPIO_IRQ_EN** (line 28)
- **CDNS_GPIO_IRQ_MASK** (line 27)
- **CDNS_GPIO_IRQ_STATUS** (line 30)
- **CDNS_GPIO_IRQ_TYPE** (line 31)
- **CDNS_GPIO_IRQ_VALUE** (line 32)
- **CDNS_GPIO_OUTPUT_EN** (line 24)
- **CDNS_GPIO_OUTPUT_VALUE** (line 25)
