# drivers/gpio/gpio-xlp.c

Subsystem: drivers/gpio

## Functions (13)

### xlp_gpio_dir_input
- Return type: static int
- Signature: xlp_gpio_dir_input(struct gpio_chip * gc,unsigned gpio)
- Line: 214
- Calls: gpiochip_get_data, xlp_gpio_set_reg

### xlp_gpio_dir_output
- Return type: static int
- Signature: xlp_gpio_dir_output(struct gpio_chip * gc,unsigned gpio,int state)
- Line: 205
- Calls: gpiochip_get_data, xlp_gpio_set_reg

### xlp_gpio_generic_handler
- Return type: static void
- Signature: xlp_gpio_generic_handler(struct irq_desc * desc)
- Line: 182

### xlp_gpio_get
- Return type: static int
- Signature: xlp_gpio_get(struct gpio_chip * gc,unsigned gpio)
- Line: 223
- Calls: gpiochip_get_data, xlp_gpio_get_reg

### xlp_gpio_get_reg
- Return type: static int
- Signature: xlp_gpio_get_reg(void __iomem * addr,unsigned gpio)
- Line: 68
- Called by: xlp_gpio_get

### xlp_gpio_irq_disable
- Return type: static void
- Signature: xlp_gpio_irq_disable(struct irq_data * d)
- Line: 100
- Calls: gpiochip_disable_irq, gpiochip_get_data, xlp_gpio_set_reg

### xlp_gpio_irq_enable
- Return type: static void
- Signature: xlp_gpio_irq_enable(struct irq_data * d)
- Line: 93
- Calls: gpiochip_enable_irq

### xlp_gpio_irq_mask_ack
- Return type: static void
- Signature: xlp_gpio_irq_mask_ack(struct irq_data * d)
- Line: 113
- Calls: gpiochip_get_data, xlp_gpio_set_reg

### xlp_gpio_irq_unmask
- Return type: static void
- Signature: xlp_gpio_irq_unmask(struct irq_data * d)
- Line: 126
- Calls: gpiochip_get_data, xlp_gpio_set_reg

### xlp_gpio_probe
- Return type: static int
- Signature: xlp_gpio_probe(struct platform_device * pdev)
- Line: 239

### xlp_gpio_set
- Return type: static int
- Signature: xlp_gpio_set(struct gpio_chip * gc,unsigned int gpio,int state)
- Line: 230
- Calls: gpiochip_get_data, xlp_gpio_set_reg

### xlp_gpio_set_irq_type
- Return type: static int
- Signature: xlp_gpio_set_irq_type(struct irq_data * d,unsigned int type)
- Line: 138
- Calls: gpiochip_get_data, xlp_gpio_set_reg

### xlp_gpio_set_reg
- Return type: static void
- Signature: xlp_gpio_set_reg(void __iomem * addr,unsigned gpio,int state)
- Line: 77
- Called by: xlp_gpio_dir_input, xlp_gpio_dir_output, xlp_gpio_irq_disable, xlp_gpio_irq_mask_ack, xlp_gpio_irq_unmask, xlp_gpio_set, xlp_gpio_set_irq_type

## Structs (1)

### xlp_gpio_priv
- Line: 56
- Members:
  - chip: gpio_chip
  - gpio_intr_en: void __iomem *
  - gpio_intr_stat: void __iomem *
  - gpio_intr_type: void __iomem *
  - gpio_intr_pol: void __iomem *
  - gpio_out_en: void __iomem *
  - gpio_paddrv: void __iomem *
  - lock: spinlock_t

## Variables (3)

- static **xlp_gpio_acpi_match** : const struct acpi_device_id[] (line 306)
- static **xlp_gpio_driver** : platform_driver (line 314)
- static **xlp_gpio_irq_chip** : irq_chip (line 171)

## Macros (18)

- **GPIO_9XX_BYTESWAP** (line 28)
- **GPIO_9XX_CTRL** (line 29)
- **GPIO_9XX_INT_EN00** (line 36)
- **GPIO_9XX_INT_EN10** (line 37)
- **GPIO_9XX_INT_EN20** (line 38)
- **GPIO_9XX_INT_EN30** (line 39)
- **GPIO_9XX_INT_POL** (line 40)
- **GPIO_9XX_INT_STAT** (line 42)
- **GPIO_9XX_INT_TYPE** (line 41)
- **GPIO_9XX_OUTPUT_EN** (line 30)
- **GPIO_9XX_PADDRV** (line 31)
- **XLP_GPIO_IRQ_BASE** (line 53)
- **XLP_GPIO_IRQ_POL_HIGH** (line 49)
- **XLP_GPIO_IRQ_POL_LOW** (line 50)
- **XLP_GPIO_IRQ_TYPE_EDGE** (line 46)
- **XLP_GPIO_IRQ_TYPE_LVL** (line 45)
- **XLP_GPIO_REGSZ** (line 52)
- **XLP_MAX_NR_GPIO** (line 54)
