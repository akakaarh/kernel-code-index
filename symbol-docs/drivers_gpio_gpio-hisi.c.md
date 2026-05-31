# drivers/gpio/gpio-hisi.c

Subsystem: drivers/gpio

## Functions (14)

### hisi_gpio_get_pdata
- Return type: static void
- Signature: hisi_gpio_get_pdata(struct device * dev,struct hisi_gpio * hisi_gpio)
- Line: 237
- Called by: hisi_gpio_probe

### hisi_gpio_init_irq
- Return type: static void
- Signature: hisi_gpio_init_irq(struct hisi_gpio * hisi_gpio)
- Line: 209
- Calls: hisi_gpio_write_reg
- Called by: hisi_gpio_probe

### hisi_gpio_irq_clr_mask
- Return type: static void
- Signature: hisi_gpio_irq_clr_mask(struct irq_data * d)
- Line: 107
- Calls: gpiochip_enable_irq, hisi_gpio_write_reg
- Called by: hisi_gpio_irq_enable

### hisi_gpio_irq_disable
- Return type: static void
- Signature: hisi_gpio_irq_disable(struct irq_data * d)
- Line: 174
- Calls: hisi_gpio_irq_set_mask, hisi_gpio_write_reg

### hisi_gpio_irq_enable
- Return type: static void
- Signature: hisi_gpio_irq_enable(struct irq_data * d)
- Line: 166
- Calls: hisi_gpio_irq_clr_mask, hisi_gpio_write_reg

### hisi_gpio_irq_handler
- Return type: static void
- Signature: hisi_gpio_irq_handler(struct irq_desc * desc)
- Line: 182
- Calls: hisi_gpio_read_reg

### hisi_gpio_irq_set_mask
- Return type: static void
- Signature: hisi_gpio_irq_set_mask(struct irq_data * d)
- Line: 99
- Calls: gpiochip_disable_irq, hisi_gpio_write_reg
- Called by: hisi_gpio_irq_disable

### hisi_gpio_irq_set_type
- Return type: static int
- Signature: hisi_gpio_irq_set_type(struct irq_data * d,u32 type)
- Line: 115
- Calls: hisi_gpio_read_reg, hisi_gpio_write_reg

### hisi_gpio_probe
- Return type: static int
- Signature: hisi_gpio_probe(struct platform_device * pdev)
- Line: 267
- Calls: gpio_generic_chip_init, hisi_gpio_get_pdata, hisi_gpio_init_irq

### hisi_gpio_read_reg
- Return type: static u32
- Signature: hisi_gpio_read_reg(struct gpio_chip * chip,unsigned int off)
- Line: 45
- Called by: hisi_gpio_irq_handler, hisi_gpio_irq_set_type

### hisi_gpio_set_ack
- Return type: static void
- Signature: hisi_gpio_set_ack(struct irq_data * d)
- Line: 92
- Calls: hisi_gpio_write_reg

### hisi_gpio_set_config
- Return type: static int
- Signature: hisi_gpio_set_config(struct gpio_chip * chip,unsigned int offset,unsigned long config)
- Line: 74
- Calls: hisi_gpio_set_debounce

### hisi_gpio_set_debounce
- Return type: static void
- Signature: hisi_gpio_set_debounce(struct gpio_chip * chip,unsigned int off,u32 debounce)
- Line: 65
- Calls: hisi_gpio_write_reg
- Called by: hisi_gpio_set_config

### hisi_gpio_write_reg
- Return type: static void
- Signature: hisi_gpio_write_reg(struct gpio_chip * chip,unsigned int off,u32 val)
- Line: 55
- Called by: hisi_gpio_init_irq, hisi_gpio_irq_clr_mask, hisi_gpio_irq_disable, hisi_gpio_irq_enable, hisi_gpio_irq_set_mask, hisi_gpio_irq_set_type, hisi_gpio_set_ack, hisi_gpio_set_debounce

## Structs (1)

### hisi_gpio
- Line: 37
- Members:
  - chip: gpio_generic_chip
  - dev: device *
  - reg_base: void __iomem *
  - line_num: unsigned int
  - irq: int

## Variables (4)

- static **hisi_gpio_acpi_match** : const struct acpi_device_id[] (line 225)
- static **hisi_gpio_driver** : platform_driver (line 329)
- static **hisi_gpio_dts_match** : const struct of_device_id[] (line 231)
- static **hisi_gpio_irq_chip** : const struct irq_chip (line 197)

## Macros (24)

- **HISI_GPIO_DEBOUNCE_CLR_WX** (line 25)
- **HISI_GPIO_DEBOUNCE_SET_WX** (line 24)
- **HISI_GPIO_DRIVER_NAME** (line 35)
- **HISI_GPIO_EXT_PORT_WX** (line 28)
- **HISI_GPIO_INTCOMB_MASK_WX** (line 29)
- **HISI_GPIO_INTEN_CLR_WX** (line 17)
- **HISI_GPIO_INTEN_SET_WX** (line 16)
- **HISI_GPIO_INTMASK_CLR_WX** (line 19)
- **HISI_GPIO_INTMASK_SET_WX** (line 18)
- **HISI_GPIO_INTSTATUS_WX** (line 26)
- **HISI_GPIO_INTTYPE_EDGE_CLR_WX** (line 21)
- **HISI_GPIO_INTTYPE_EDGE_SET_WX** (line 20)
- **HISI_GPIO_INT_DEDGE_CLR** (line 31)
- **HISI_GPIO_INT_DEDGE_SET** (line 30)
- **HISI_GPIO_INT_DEDGE_ST** (line 32)
- **HISI_GPIO_INT_POLARITY_CLR_WX** (line 23)
- **HISI_GPIO_INT_POLARITY_SET_WX** (line 22)
- **HISI_GPIO_LINE_NUM_MAX** (line 34)
- **HISI_GPIO_PORTA_EOI_WX** (line 27)
- **HISI_GPIO_SWPORT_DDR_CLR_WX** (line 14)
- **HISI_GPIO_SWPORT_DDR_SET_WX** (line 13)
- **HISI_GPIO_SWPORT_DDR_ST_WX** (line 15)
- **HISI_GPIO_SWPORT_DR_CLR_WX** (line 12)
- **HISI_GPIO_SWPORT_DR_SET_WX** (line 11)
