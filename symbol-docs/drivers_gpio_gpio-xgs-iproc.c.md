# drivers/gpio/gpio-xgs-iproc.c

Subsystem: drivers/gpio

## Functions (9)

### iproc_gpio_irq_ack
- Return type: static void
- Signature: iproc_gpio_irq_ack(struct irq_data * d)
- Line: 45
- Calls: to_iproc_gpio

### iproc_gpio_irq_handler
- Return type: static irqreturn_t
- Signature: iproc_gpio_irq_handler(int irq,void * data)
- Line: 167
- Calls: to_iproc_gpio

### iproc_gpio_irq_mask
- Return type: static void
- Signature: iproc_gpio_irq_mask(struct irq_data * d)
- Line: 91
- Calls: gpiochip_disable_irq, to_iproc_gpio

### iproc_gpio_irq_print_chip
- Return type: static void
- Signature: iproc_gpio_irq_print_chip(struct irq_data * d,struct seq_file * p)
- Line: 197
- Calls: to_iproc_gpio

### iproc_gpio_irq_set_type
- Return type: static int
- Signature: iproc_gpio_irq_set_type(struct irq_data * d,u32 type)
- Line: 118
- Calls: to_iproc_gpio

### iproc_gpio_irq_unmask
- Return type: static void
- Signature: iproc_gpio_irq_unmask(struct irq_data * d)
- Line: 64
- Calls: gpiochip_enable_irq, to_iproc_gpio

### iproc_gpio_probe
- Return type: static int
- Signature: iproc_gpio_probe(struct platform_device * pdev)
- Line: 215
- Calls: gpio_generic_chip_init

### iproc_gpio_remove
- Return type: static void
- Signature: iproc_gpio_remove(struct platform_device * pdev)
- Line: 298

### to_iproc_gpio
- Return type: static iproc_gpio_chip *
- Signature: to_iproc_gpio(struct gpio_chip * gc)
- Line: 40
- Called by: iproc_gpio_irq_ack, iproc_gpio_irq_handler, iproc_gpio_irq_mask, iproc_gpio_irq_print_chip, iproc_gpio_irq_set_type, iproc_gpio_irq_unmask

## Structs (1)

### iproc_gpio_chip
- Line: 31
- Members:
  - gen_gc: gpio_generic_chip
  - lock: spinlock_t
  - dev: device *
  - base: void __iomem *
  - intr: void __iomem *

## Variables (3)

- static **bcm_iproc_gpio_driver** : platform_driver (line 317)
- static **bcm_iproc_gpio_of_match** : const struct of_device_id[] (line 311)
- static **iproc_gpio_irq_chip** : const struct irq_chip (line 205)

## Macros (11)

- **IPROC_CCA_INT_F_GPIOINT** (line 18)
- **IPROC_CCA_INT_MASK** (line 20)
- **IPROC_CCA_INT_STS** (line 19)
- **IPROC_GPIO_CCA_DIN** (line 22)
- **IPROC_GPIO_CCA_DOUT** (line 23)
- **IPROC_GPIO_CCA_INT_EDGE** (line 29)
- **IPROC_GPIO_CCA_INT_EVENT** (line 27)
- **IPROC_GPIO_CCA_INT_EVENT_MASK** (line 28)
- **IPROC_GPIO_CCA_INT_LEVEL** (line 25)
- **IPROC_GPIO_CCA_INT_LEVEL_MASK** (line 26)
- **IPROC_GPIO_CCA_OUT_EN** (line 24)
