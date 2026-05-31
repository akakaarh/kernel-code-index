# drivers/gpio/gpio-rda.c

Subsystem: drivers/gpio

## Functions (8)

### rda_gpio_irq_ack
- Return type: static void
- Signature: rda_gpio_irq_ack(struct irq_data * data)
- Line: 80
- Calls: rda_gpio_update

### rda_gpio_irq_handler
- Return type: static void
- Signature: rda_gpio_irq_handler(struct irq_desc * desc)
- Line: 180
- Calls: gpiochip_get_data

### rda_gpio_irq_mask
- Return type: static void
- Signature: rda_gpio_irq_mask(struct irq_data * data)
- Line: 65
- Calls: gpiochip_disable_irq, gpiochip_get_data

### rda_gpio_irq_set_type
- Return type: static int
- Signature: rda_gpio_irq_set_type(struct irq_data * data,unsigned int flow_type)
- Line: 162
- Calls: rda_gpio_set_irq

### rda_gpio_irq_unmask
- Return type: static void
- Signature: rda_gpio_irq_unmask(struct irq_data * data)
- Line: 152
- Calls: gpiochip_enable_irq, rda_gpio_set_irq

### rda_gpio_probe
- Return type: static int
- Signature: rda_gpio_probe(struct platform_device * pdev)
- Line: 210
- Calls: gpio_generic_chip_init

### rda_gpio_set_irq
- Return type: static int
- Signature: rda_gpio_set_irq(struct gpio_chip * chip,u32 offset,unsigned int flow_type)
- Line: 88
- Calls: gpiochip_get_data
- Called by: rda_gpio_irq_set_type, rda_gpio_irq_unmask

### rda_gpio_update
- Return type: static void
- Signature: rda_gpio_update(struct gpio_chip * chip,unsigned int offset,u16 reg,int val)
- Line: 45
- Calls: gpiochip_get_data
- Called by: rda_gpio_irq_ack

## Structs (1)

### rda_gpio
- Line: 38
- Members:
  - chip: gpio_generic_chip
  - base: void __iomem *
  - lock: spinlock_t
  - irq: int

## Variables (3)

- static **rda_gpio_driver** : platform_driver (line 288)
- static **rda_gpio_irq_chip** : const struct irq_chip (line 200)
- static **rda_gpio_of_match** : const struct of_device_id[] (line 282)

## Macros (16)

- **RDA_GPIO_BANK_NR** (line 36)
- **RDA_GPIO_CLR** (line 22)
- **RDA_GPIO_DEBOUCE_SHIFT** (line 30)
- **RDA_GPIO_INT_CLR** (line 25)
- **RDA_GPIO_INT_CTRL_CLR** (line 24)
- **RDA_GPIO_INT_CTRL_SET** (line 23)
- **RDA_GPIO_INT_STATUS** (line 26)
- **RDA_GPIO_IRQ_FALL_SHIFT** (line 29)
- **RDA_GPIO_IRQ_MASK** (line 33)
- **RDA_GPIO_IRQ_RISE_SHIFT** (line 28)
- **RDA_GPIO_LEVEL_SHIFT** (line 31)
- **RDA_GPIO_OEN_SET_IN** (line 19)
- **RDA_GPIO_OEN_SET_OUT** (line 18)
- **RDA_GPIO_OEN_VAL** (line 17)
- **RDA_GPIO_SET** (line 21)
- **RDA_GPIO_VAL** (line 20)
