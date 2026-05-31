# drivers/gpio/gpio-mlxbf3.c

Subsystem: drivers/gpio

## Functions (8)

### mlxbf3_gpio_add_pin_ranges
- Return type: static int
- Signature: mlxbf3_gpio_add_pin_ranges(struct gpio_chip * chip)
- Line: 162

### mlxbf3_gpio_irq_ack
- Return type: static void
- Signature: mlxbf3_gpio_irq_ack(struct irq_data * data)
- Line: 148

### mlxbf3_gpio_irq_disable
- Return type: static void
- Signature: mlxbf3_gpio_irq_disable(struct irq_data * irqd)
- Line: 75
- Calls: gpiochip_disable_irq, gpiochip_get_data

### mlxbf3_gpio_irq_enable
- Return type: static void
- Signature: mlxbf3_gpio_irq_enable(struct irq_data * irqd)
- Line: 57
- Calls: gpiochip_enable_irq, gpiochip_get_data

### mlxbf3_gpio_irq_handler
- Return type: static irqreturn_t
- Signature: mlxbf3_gpio_irq_handler(int irq,void * ptr)
- Line: 93

### mlxbf3_gpio_irq_set_type
- Return type: static int
- Signature: mlxbf3_gpio_irq_set_type(struct irq_data * irqd,unsigned int type)
- Line: 110
- Calls: gpiochip_get_data

### mlxbf3_gpio_probe
- Return type: static int
- Signature: mlxbf3_gpio_probe(struct platform_device * pdev)
- Line: 182
- Calls: gpio_generic_chip_init

### mlxbf3_gpio_shutdown
- Return type: static void
- Signature: mlxbf3_gpio_shutdown(struct platform_device * pdev)
- Line: 263

## Structs (1)

### mlxbf3_gpio_context
- Line: 45
- Members:
  - chip: gpio_generic_chip
  - gpio_set_io: void __iomem *
  - gpio_clr_io: void __iomem *
  - gpio_io: void __iomem *
  - gpio_cause_io: void __iomem *

## Variables (3)

- static **gpio_mlxbf3_irqchip** : const struct irq_chip (line 152)
- static **mlxbf3_gpio_acpi_match** : const struct acpi_device_id[] (line 272)
- static **mlxbf3_gpio_driver** : platform_driver (line 278)

## Macros (14)

- **MLXBF3_GPIO_MAX_PINS_BLOCK0** (line 23)
- **MLXBF3_GPIO_MAX_PINS_BLOCK1** (line 24)
- **MLXBF3_GPIO_MAX_PINS_PER_BLOCK** (line 22)
- **MLXBF_GPIO_CAUSE_FALL_EN** (line 36)
- **MLXBF_GPIO_CAUSE_OR_CAUSE_EVTEN0** (line 39)
- **MLXBF_GPIO_CAUSE_OR_CLRCAUSE** (line 41)
- **MLXBF_GPIO_CAUSE_OR_EVTEN0** (line 40)
- **MLXBF_GPIO_CAUSE_RISE_EN** (line 35)
- **MLXBF_GPIO_CLR_ALL_INTS** (line 43)
- **MLXBF_GPIO_FW_DATA_OUT_CLEAR** (line 33)
- **MLXBF_GPIO_FW_DATA_OUT_SET** (line 30)
- **MLXBF_GPIO_FW_OUTPUT_ENABLE_CLEAR** (line 32)
- **MLXBF_GPIO_FW_OUTPUT_ENABLE_SET** (line 29)
- **MLXBF_GPIO_READ_DATA_IN** (line 37)
