# drivers/gpio/gpio-novalake-events.c

Subsystem: drivers/gpio

## Functions (10)

### nvl_acpi_enable_gpe_mode
- Return type: static int
- Signature: nvl_acpi_enable_gpe_mode(struct device * dev)
- Line: 220
- Called by: nvl_gpio_probe

### nvl_gpio_get
- Return type: static int
- Signature: nvl_gpio_get(struct gpio_chip * gc,unsigned int gpio)
- Line: 81
- Calls: gpiochip_get_data, nvl_gpio_get_byte_addr

### nvl_gpio_get_byte_addr
- Return type: static void __iomem *
- Signature: nvl_gpio_get_byte_addr(struct nvl_gpio * priv,unsigned int reg_offset,unsigned long gpio)
- Line: 74
- Called by: nvl_gpio_get, nvl_gpio_irq_ack, nvl_gpio_irq_mask_unmask

### nvl_gpio_irq
- Return type: static irqreturn_t
- Signature: nvl_gpio_irq(int irq,void * data)
- Line: 181

### nvl_gpio_irq_ack
- Return type: static void
- Signature: nvl_gpio_irq_ack(struct irq_data * d)
- Line: 152
- Calls: gpiochip_get_data, nvl_gpio_get_byte_addr

### nvl_gpio_irq_mask
- Return type: static void
- Signature: nvl_gpio_irq_mask(struct irq_data * d)
- Line: 143
- Calls: gpiochip_disable_irq, nvl_gpio_irq_mask_unmask

### nvl_gpio_irq_mask_unmask
- Return type: static void
- Signature: nvl_gpio_irq_mask_unmask(struct gpio_chip * gc,unsigned long hwirq,bool mask)
- Line: 113
- Calls: gpiochip_get_data, nvl_gpio_get_byte_addr
- Called by: nvl_gpio_irq_mask, nvl_gpio_irq_unmask

### nvl_gpio_irq_set_type
- Return type: static int
- Signature: nvl_gpio_irq_set_type(struct irq_data * d,unsigned int type)
- Line: 103

### nvl_gpio_irq_unmask
- Return type: static void
- Signature: nvl_gpio_irq_unmask(struct irq_data * d)
- Line: 134
- Calls: gpiochip_enable_irq, nvl_gpio_irq_mask_unmask

### nvl_gpio_probe
- Return type: static int
- Signature: nvl_gpio_probe(struct platform_device * pdev)
- Line: 241
- Calls: nvl_acpi_enable_gpe_mode

## Structs (1)

### nvl_gpio
- Line: 67
- Members:
  - gc: gpio_chip
  - reg_base: void __iomem *
  - lock: raw_spinlock_t
  - blk_size: size_t

## Variables (5)

- static **nvl_gpe_dsm_guid** : const guid_t (line 212)
- static **nvl_gpio_acpi_match** : const struct acpi_device_id[] (line 306)
- static **nvl_gpio_chip** : const struct gpio_chip (line 98)
- static **nvl_gpio_driver** : platform_driver (line 312)
- static **nvl_gpio_irq_chip** : const struct irq_chip (line 171)

## Macros (7)

- **DSM_ENABLE_GPE_MODE** (line 218)
- **DSM_GPE_MODE_FN_INDEX** (line 217)
- **DSM_GPE_MODE_REV** (line 216)
- **GPE_BLK_REG_SIZE**(block_size) (line 55)
- **GPE_EN_REG_OFFSET**(block_size) (line 58)
- **GPE_REG_PIN_COUNT**(block_size) (line 56)
- **GPE_STS_REG_OFFSET** (line 57)
