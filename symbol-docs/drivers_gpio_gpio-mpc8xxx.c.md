# drivers/gpio/gpio-mpc8xxx.c

Subsystem: drivers/gpio

## Functions (17)

### mpc5121_gpio_dir_out
- Return type: static int
- Signature: mpc5121_gpio_dir_out(struct gpio_chip * gc,unsigned int gpio,int val)
- Line: 79
- Calls: gpiochip_get_data

### mpc5125_gpio_dir_out
- Return type: static int
- Signature: mpc5125_gpio_dir_out(struct gpio_chip * gc,unsigned int gpio,int val)
- Line: 90
- Calls: gpiochip_get_data

### mpc512x_irq_set_type
- Return type: static int
- Signature: mpc512x_irq_set_type(struct irq_data * d,unsigned int flow_type)
- Line: 208

### mpc8572_gpio_get
- Return type: static int
- Signature: mpc8572_gpio_get(struct gpio_chip * gc,unsigned int gpio)
- Line: 64
- Calls: gpiochip_get_data, mpc_pin2mask

### mpc8xxx_gpio_irq_cascade
- Return type: static irqreturn_t
- Signature: mpc8xxx_gpio_irq_cascade(int irq,void * data)
- Line: 111

### mpc8xxx_gpio_irq_map
- Return type: static int
- Signature: mpc8xxx_gpio_irq_map(struct irq_domain * h,unsigned int irq,irq_hw_number_t hwirq)
- Line: 271

### mpc8xxx_gpio_to_irq
- Return type: static int
- Signature: mpc8xxx_gpio_to_irq(struct gpio_chip * gc,unsigned offset)
- Line: 101
- Calls: gpiochip_get_data

### mpc8xxx_init
- Return type: static int __init
- Signature: mpc8xxx_init(void)
- Line: 506

### mpc8xxx_irq_ack
- Return type: static void
- Signature: mpc8xxx_irq_ack(struct irq_data * d)
- Line: 166
- Calls: mpc_pin2mask

### mpc8xxx_irq_mask
- Return type: static void
- Signature: mpc8xxx_irq_mask(struct irq_data * d)
- Line: 147
- Calls: gpiochip_disable_irq, mpc_pin2mask

### mpc8xxx_irq_set_type
- Return type: static int
- Signature: mpc8xxx_irq_set_type(struct irq_data * d,unsigned int flow_type)
- Line: 174
- Calls: mpc_pin2mask

### mpc8xxx_irq_unmask
- Return type: static void
- Signature: mpc8xxx_irq_unmask(struct irq_data * d)
- Line: 127
- Calls: gpiochip_enable_irq, mpc_pin2mask

### mpc8xxx_probe
- Return type: static int
- Signature: mpc8xxx_probe(struct platform_device * pdev)
- Line: 323
- Calls: gpio_generic_chip_init

### mpc8xxx_remove
- Return type: static void
- Signature: mpc8xxx_remove(struct platform_device * pdev)
- Line: 454

### mpc8xxx_resume
- Return type: static int
- Signature: mpc8xxx_resume(struct device * dev)
- Line: 474

### mpc8xxx_suspend
- Return type: static int
- Signature: mpc8xxx_suspend(struct device * dev)
- Line: 464

### mpc_pin2mask
- Return type: static u32
- Signature: mpc_pin2mask(unsigned int offset)
- Line: 54
- Called by: mpc8572_gpio_get, mpc8xxx_irq_ack, mpc8xxx_irq_mask, mpc8xxx_irq_set_type, mpc8xxx_irq_unmask

## Structs (2)

### mpc8xxx_gpio_chip
- Line: 37
- Members:
  - chip: gpio_generic_chip
  - regs: void __iomem *
  - lock: raw_spinlock_t
  - direction_output: int (*)(struct gpio_chip * chip,unsigned offset,int value)
  - irq: irq_domain *
  - irqn: int
  - gpio_dir_out: int (*)(struct gpio_chip *,unsigned int,int)
  - gpio_get: int (*)(struct gpio_chip *,unsigned int)
  - irq_set_type: int (*)(struct irq_data *,unsigned int)

### mpc8xxx_gpio_devtype
- Line: 285
- Members:
  - chip: gpio_generic_chip
  - regs: void __iomem *
  - lock: raw_spinlock_t
  - direction_output: int (*)(struct gpio_chip * chip,unsigned offset,int value)
  - irq: irq_domain *
  - irqn: int
  - gpio_dir_out: int (*)(struct gpio_chip *,unsigned int,int)
  - gpio_get: int (*)(struct gpio_chip *,unsigned int)
  - irq_set_type: int (*)(struct irq_data *,unsigned int)

## Variables (9)

- static **gpio_acpi_ids** : const struct acpi_device_id[] (line 488)
- static **mpc5125_gpio_devtype** : const struct mpc8xxx_gpio_devtype (line 296)
- static **mpc512x_gpio_devtype** : const struct mpc8xxx_gpio_devtype (line 291)
- static **mpc8572_gpio_devtype** : const struct mpc8xxx_gpio_devtype (line 301)
- static **mpc8xxx_gpio_devtype_default** : const struct mpc8xxx_gpio_devtype (line 305)
- static **mpc8xxx_gpio_ids** : const struct of_device_id[] (line 309)
- static **mpc8xxx_gpio_irq_ops** : const struct irq_domain_ops (line 280)
- static **mpc8xxx_irq_chip** : irq_chip (line 260)
- static **mpc8xxx_plat_driver** : platform_driver (line 495)

## Macros (9)

- **GPIO_DAT** (line 30)
- **GPIO_DIR** (line 28)
- **GPIO_IBE** (line 35)
- **GPIO_ICR** (line 33)
- **GPIO_ICR2** (line 34)
- **GPIO_IER** (line 31)
- **GPIO_IMR** (line 32)
- **GPIO_ODR** (line 29)
- **MPC8XXX_GPIO_PINS** (line 26)
