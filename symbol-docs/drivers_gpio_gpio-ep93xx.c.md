# drivers/gpio/gpio-ep93xx.c

Subsystem: drivers/gpio

## Functions (17)

### ep93xx_ab_irq_handler
- Return type: static irqreturn_t
- Signature: ep93xx_ab_irq_handler(int irq,void * dev_id)
- Line: 103
- Calls: ep93xx_gpio_ab_irq_handler

### ep93xx_gpio_ab_irq_handler
- Return type: static u32
- Signature: ep93xx_gpio_ab_irq_handler(struct gpio_chip * gc)
- Line: 90
- Calls: to_ep93xx_gpio_irq_chip
- Called by: ep93xx_ab_irq_handler

### ep93xx_gpio_f_irq_handler
- Return type: static void
- Signature: ep93xx_gpio_f_irq_handler(struct irq_desc * desc)
- Line: 108

### ep93xx_gpio_init
- Return type: static int __init
- Signature: ep93xx_gpio_init(void)
- Line: 390

### ep93xx_gpio_int_debounce
- Return type: static void
- Signature: ep93xx_gpio_int_debounce(struct gpio_chip * gc,unsigned int offset,bool enable)
- Line: 76
- Calls: to_ep93xx_gpio_irq_chip
- Called by: ep93xx_gpio_set_config

### ep93xx_gpio_irq_ack
- Return type: static void
- Signature: ep93xx_gpio_irq_ack(struct irq_data * d)
- Line: 127
- Calls: ep93xx_gpio_update_int_params, to_ep93xx_gpio_irq_chip

### ep93xx_gpio_irq_mask
- Return type: static void
- Signature: ep93xx_gpio_irq_mask(struct irq_data * d)
- Line: 158
- Calls: ep93xx_gpio_update_int_params, gpiochip_disable_irq, to_ep93xx_gpio_irq_chip

### ep93xx_gpio_irq_mask_ack
- Return type: static void
- Signature: ep93xx_gpio_irq_mask_ack(struct irq_data * d)
- Line: 141
- Calls: ep93xx_gpio_update_int_params, gpiochip_disable_irq, to_ep93xx_gpio_irq_chip

### ep93xx_gpio_irq_type
- Return type: static int
- Signature: ep93xx_gpio_irq_type(struct irq_data * d,unsigned int type)
- Line: 185
- Calls: ep93xx_gpio_update_int_params, to_ep93xx_gpio_irq_chip

### ep93xx_gpio_irq_unmask
- Return type: static void
- Signature: ep93xx_gpio_irq_unmask(struct irq_data * d)
- Line: 169
- Calls: ep93xx_gpio_update_int_params, gpiochip_enable_irq, to_ep93xx_gpio_irq_chip

### ep93xx_gpio_probe
- Return type: static int
- Signature: ep93xx_gpio_probe(struct platform_device * pdev)
- Line: 332
- Calls: ep93xx_setup_irqs, gpio_generic_chip_init

### ep93xx_gpio_set_config
- Return type: static int
- Signature: ep93xx_gpio_set_config(struct gpio_chip * gc,unsigned offset,unsigned long config)
- Line: 238
- Calls: ep93xx_gpio_int_debounce

### ep93xx_gpio_update_int_params
- Return type: static void
- Signature: ep93xx_gpio_update_int_params(struct ep93xx_gpio_irq_chip * eic)
- Line: 62
- Called by: ep93xx_gpio_irq_ack, ep93xx_gpio_irq_mask, ep93xx_gpio_irq_mask_ack, ep93xx_gpio_irq_type, ep93xx_gpio_irq_unmask

### ep93xx_irq_print_chip
- Return type: static void
- Signature: ep93xx_irq_print_chip(struct irq_data * data,struct seq_file * p)
- Line: 252

### ep93xx_setup_irqs
- Return type: static int
- Signature: ep93xx_setup_irqs(struct platform_device * pdev,struct ep93xx_gpio_chip * egc)
- Line: 271
- Called by: ep93xx_gpio_probe

### to_ep93xx_gpio_chip
- Return type: static ep93xx_gpio_chip *
- Signature: to_ep93xx_gpio_chip(struct gpio_chip * gc)
- Line: 39
- Called by: to_ep93xx_gpio_irq_chip

### to_ep93xx_gpio_irq_chip
- Return type: static ep93xx_gpio_irq_chip *
- Signature: to_ep93xx_gpio_irq_chip(struct gpio_chip * gc)
- Line: 44
- Calls: to_ep93xx_gpio_chip
- Called by: ep93xx_gpio_ab_irq_handler, ep93xx_gpio_int_debounce, ep93xx_gpio_irq_ack, ep93xx_gpio_irq_mask, ep93xx_gpio_irq_mask_ack, ep93xx_gpio_irq_type, ep93xx_gpio_irq_unmask

## Structs (2)

### ep93xx_gpio_chip
- Line: 33
- Members:
  - base: void __iomem *
  - int_unmasked: u8
  - int_enabled: u8
  - int_type1: u8
  - int_type2: u8
  - int_debounce: u8
  - base: void __iomem *
  - chip: gpio_generic_chip
  - eic: ep93xx_gpio_irq_chip *

### ep93xx_gpio_irq_chip
- Line: 24
- Members:
  - base: void __iomem *
  - int_unmasked: u8
  - int_enabled: u8
  - int_type1: u8
  - int_type2: u8
  - int_debounce: u8
  - base: void __iomem *
  - chip: gpio_generic_chip
  - eic: ep93xx_gpio_irq_chip *

## Variables (3)

- static **ep93xx_gpio_driver** : platform_driver (line 382)
- static **ep93xx_gpio_match** : const struct of_device_id[] (line 377)
- static **gpio_eic_irq_chip** : const struct irq_chip (line 259)

## Macros (7)

- **EP93XX_INT_DEBOUNCE_OFFSET** (line 60)
- **EP93XX_INT_EN_OFFSET** (line 57)
- **EP93XX_INT_EOI_OFFSET** (line 56)
- **EP93XX_INT_RAW_STATUS_OFFSET** (line 59)
- **EP93XX_INT_STATUS_OFFSET** (line 58)
- **EP93XX_INT_TYPE1_OFFSET** (line 54)
- **EP93XX_INT_TYPE2_OFFSET** (line 55)
