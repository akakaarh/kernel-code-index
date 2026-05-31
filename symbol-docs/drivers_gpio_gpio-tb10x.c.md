# drivers/gpio/gpio-tb10x.c

Subsystem: drivers/gpio

## Functions (6)

### tb10x_gpio_irq_cascade
- Return type: static irqreturn_t
- Signature: tb10x_gpio_irq_cascade(int irq,void * data)
- Line: 72
- Calls: tb10x_reg_read

### tb10x_gpio_irq_set_type
- Return type: static int
- Signature: tb10x_gpio_irq_set_type(struct irq_data * data,unsigned int type)
- Line: 60

### tb10x_gpio_probe
- Return type: static int
- Signature: tb10x_gpio_probe(struct platform_device * pdev)
- Line: 86
- Calls: gpio_generic_chip_init

### tb10x_gpio_remove
- Return type: static void
- Signature: tb10x_gpio_remove(struct platform_device * pdev)
- Line: 198

### tb10x_gpio_to_irq
- Return type: static int
- Signature: tb10x_gpio_to_irq(struct gpio_chip * chip,unsigned offset)
- Line: 53
- Calls: gpiochip_get_data

### tb10x_reg_read
- Return type: static u32
- Signature: tb10x_reg_read(struct tb10x_gpio * gpio,unsigned int offs)
- Line: 48
- Called by: tb10x_gpio_irq_cascade

## Structs (1)

### tb10x_gpio
- Line: 41
- Members:
  - base: void __iomem *
  - domain: irq_domain *
  - irq: int
  - chip: gpio_generic_chip

## Variables (2)

- static **tb10x_gpio_driver** : platform_driver (line 216)
- static **tb10x_gpio_dt_ids** : const struct of_device_id[] (line 210)

## Macros (8)

- **OFFSET_TO_REG_CHANGE** (line 30)
- **OFFSET_TO_REG_DATA** (line 28)
- **OFFSET_TO_REG_DDR** (line 27)
- **OFFSET_TO_REG_INT_EN** (line 29)
- **OFFSET_TO_REG_INT_TYPE** (line 32)
- **OFFSET_TO_REG_WRMASK** (line 31)
- **TB10X_GPIO_DIR_IN** (line 25)
- **TB10X_GPIO_DIR_OUT** (line 26)
