# drivers/gpio/gpio-ath79.c

Subsystem: drivers/gpio

## Functions (11)

### ath79_gpio_irq_disable
- Return type: static void
- Signature: ath79_gpio_irq_disable(struct irq_data * data)
- Line: 103
- Calls: ath79_gpio_update_bits, irq_data_to_ath79_gpio

### ath79_gpio_irq_enable
- Return type: static void
- Signature: ath79_gpio_irq_enable(struct irq_data * data)
- Line: 93
- Calls: ath79_gpio_update_bits, irq_data_to_ath79_gpio

### ath79_gpio_irq_handler
- Return type: static void
- Signature: ath79_gpio_irq_handler(struct irq_desc * desc)
- Line: 179
- Calls: ath79_gpio_read, ath79_gpio_update_bits

### ath79_gpio_irq_mask
- Return type: static void
- Signature: ath79_gpio_irq_mask(struct irq_data * data)
- Line: 82
- Calls: ath79_gpio_update_bits, gpiochip_disable_irq, irq_data_to_ath79_gpio

### ath79_gpio_irq_set_type
- Return type: static int
- Signature: ath79_gpio_irq_set_type(struct irq_data * data,unsigned int flow_type)
- Line: 113
- Calls: ath79_gpio_read, ath79_gpio_update_bits, irq_data_to_ath79_gpio

### ath79_gpio_irq_unmask
- Return type: static void
- Signature: ath79_gpio_irq_unmask(struct irq_data * data)
- Line: 70
- Calls: ath79_gpio_update_bits, gpiochip_enable_irq, irq_data_to_ath79_gpio

### ath79_gpio_probe
- Return type: static int
- Signature: ath79_gpio_probe(struct platform_device * pdev)
- Line: 217
- Calls: gpio_generic_chip_init

### ath79_gpio_read
- Return type: static u32
- Signature: ath79_gpio_read(struct ath79_gpio_ctrl * ctrl,unsigned reg)
- Line: 45
- Called by: ath79_gpio_irq_handler, ath79_gpio_irq_set_type, ath79_gpio_update_bits

### ath79_gpio_update_bits
- Return type: static bool
- Signature: ath79_gpio_update_bits(struct ath79_gpio_ctrl * ctrl,unsigned reg,u32 mask,u32 bits)
- Line: 56
- Calls: ath79_gpio_read, ath79_gpio_write
- Called by: ath79_gpio_irq_disable, ath79_gpio_irq_enable, ath79_gpio_irq_handler, ath79_gpio_irq_mask, ath79_gpio_irq_set_type, ath79_gpio_irq_unmask

### ath79_gpio_write
- Return type: static void
- Signature: ath79_gpio_write(struct ath79_gpio_ctrl * ctrl,unsigned reg,u32 val)
- Line: 50
- Called by: ath79_gpio_update_bits

### irq_data_to_ath79_gpio
- Return type: static ath79_gpio_ctrl *
- Signature: irq_data_to_ath79_gpio(struct irq_data * data)
- Line: 37
- Called by: ath79_gpio_irq_disable, ath79_gpio_irq_enable, ath79_gpio_irq_mask, ath79_gpio_irq_set_type, ath79_gpio_irq_unmask

## Structs (1)

### ath79_gpio_ctrl
- Line: 31
- Members:
  - chip: gpio_generic_chip
  - base: void __iomem *
  - both_edges: unsigned long

## Variables (3)

- static **ath79_gpio_driver** : platform_driver (line 282)
- static **ath79_gpio_irqchip** : const struct irq_chip (line 168)
- static **ath79_gpio_of_match** : const struct of_device_id[] (line 210)

## Macros (9)

- **AR71XX_GPIO_REG_CLEAR** (line 23)
- **AR71XX_GPIO_REG_IN** (line 21)
- **AR71XX_GPIO_REG_INT_ENABLE** (line 25)
- **AR71XX_GPIO_REG_INT_MASK** (line 29)
- **AR71XX_GPIO_REG_INT_PENDING** (line 28)
- **AR71XX_GPIO_REG_INT_POLARITY** (line 27)
- **AR71XX_GPIO_REG_INT_TYPE** (line 26)
- **AR71XX_GPIO_REG_OE** (line 20)
- **AR71XX_GPIO_REG_SET** (line 22)
