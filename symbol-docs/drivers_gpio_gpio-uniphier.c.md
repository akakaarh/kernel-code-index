# drivers/gpio/gpio-uniphier.c

Subsystem: drivers/gpio

## Functions (27)

### uniphier_gpio_bank_to_reg
- Return type: static unsigned int
- Signature: uniphier_gpio_bank_to_reg(unsigned int bank)
- Line: 36
- Called by: uniphier_gpio_bank_write, uniphier_gpio_offset_read, uniphier_gpio_resume, uniphier_gpio_suspend

### uniphier_gpio_bank_write
- Return type: static void
- Signature: uniphier_gpio_bank_write(struct gpio_chip * chip,unsigned int bank,unsigned int reg,u32 mask,u32 val)
- Line: 73
- Calls: gpiochip_get_data, uniphier_gpio_bank_to_reg, uniphier_gpio_reg_update
- Called by: uniphier_gpio_offset_write, uniphier_gpio_set_multiple

### uniphier_gpio_direction_input
- Return type: static int
- Signature: uniphier_gpio_direction_input(struct gpio_chip * chip,unsigned int offset)
- Line: 119
- Calls: uniphier_gpio_offset_write

### uniphier_gpio_direction_output
- Return type: static int
- Signature: uniphier_gpio_direction_output(struct gpio_chip * chip,unsigned int offset,int val)
- Line: 127
- Calls: uniphier_gpio_offset_write

### uniphier_gpio_get
- Return type: static int
- Signature: uniphier_gpio_get(struct gpio_chip * chip,unsigned int offset)
- Line: 136
- Calls: uniphier_gpio_offset_read

### uniphier_gpio_get_bank_and_mask
- Return type: static void
- Signature: uniphier_gpio_get_bank_and_mask(unsigned int offset,unsigned int * bank,u32 * mask)
- Line: 52
- Called by: uniphier_gpio_offset_read, uniphier_gpio_offset_write

### uniphier_gpio_get_direction
- Return type: static int
- Signature: uniphier_gpio_get_direction(struct gpio_chip * chip,unsigned int offset)
- Line: 110
- Calls: uniphier_gpio_offset_read

### uniphier_gpio_get_nbanks
- Return type: static unsigned int
- Signature: uniphier_gpio_get_nbanks(unsigned int ngpio)
- Line: 338
- Called by: uniphier_gpio_probe, uniphier_gpio_resume, uniphier_gpio_suspend

### uniphier_gpio_hw_init
- Return type: static void
- Signature: uniphier_gpio_hw_init(struct uniphier_gpio_priv * priv)
- Line: 326
- Called by: uniphier_gpio_probe, uniphier_gpio_resume

### uniphier_gpio_irq_domain_activate
- Return type: static int
- Signature: uniphier_gpio_irq_domain_activate(struct irq_domain * domain,struct irq_data * data,bool early)
- Line: 298
- Calls: gpiochip_lock_as_irq

### uniphier_gpio_irq_domain_alloc
- Return type: static int
- Signature: uniphier_gpio_irq_domain_alloc(struct irq_domain * domain,unsigned int virq,unsigned int nr_irqs,void * arg)
- Line: 262
- Calls: uniphier_gpio_irq_domain_translate, uniphier_gpio_irq_get_parent_hwirq

### uniphier_gpio_irq_domain_deactivate
- Return type: static void
- Signature: uniphier_gpio_irq_domain_deactivate(struct irq_domain * domain,struct irq_data * data)
- Line: 308
- Calls: gpiochip_unlock_as_irq

### uniphier_gpio_irq_domain_translate
- Return type: static int
- Signature: uniphier_gpio_irq_domain_translate(struct irq_domain * domain,struct irq_fwspec * fwspec,unsigned long * out_hwirq,unsigned int * out_type)
- Line: 248
- Called by: uniphier_gpio_irq_domain_alloc

### uniphier_gpio_irq_get_parent_hwirq
- Return type: static int
- Signature: uniphier_gpio_irq_get_parent_hwirq(struct uniphier_gpio_priv * priv,unsigned int hwirq)
- Line: 222
- Called by: uniphier_gpio_irq_domain_alloc

### uniphier_gpio_irq_mask
- Return type: static void
- Signature: uniphier_gpio_irq_mask(struct irq_data * data)
- Line: 184
- Calls: uniphier_gpio_reg_update

### uniphier_gpio_irq_set_type
- Return type: static int
- Signature: uniphier_gpio_irq_set_type(struct irq_data * data,unsigned int type)
- Line: 204
- Calls: uniphier_gpio_reg_update

### uniphier_gpio_irq_unmask
- Return type: static void
- Signature: uniphier_gpio_irq_unmask(struct irq_data * data)
- Line: 194
- Calls: uniphier_gpio_reg_update

### uniphier_gpio_offset_read
- Return type: static int
- Signature: uniphier_gpio_offset_read(struct gpio_chip * chip,unsigned int offset,unsigned int reg)
- Line: 97
- Calls: gpiochip_get_data, uniphier_gpio_bank_to_reg, uniphier_gpio_get_bank_and_mask
- Called by: uniphier_gpio_get, uniphier_gpio_get_direction

### uniphier_gpio_offset_write
- Return type: static void
- Signature: uniphier_gpio_offset_write(struct gpio_chip * chip,unsigned int offset,unsigned int reg,int val)
- Line: 85
- Calls: uniphier_gpio_bank_write, uniphier_gpio_get_bank_and_mask
- Called by: uniphier_gpio_direction_input, uniphier_gpio_direction_output, uniphier_gpio_set

### uniphier_gpio_probe
- Return type: static int
- Signature: uniphier_gpio_probe(struct platform_device * pdev)
- Line: 343
- Calls: uniphier_gpio_get_nbanks, uniphier_gpio_hw_init

### uniphier_gpio_reg_update
- Return type: static void
- Signature: uniphier_gpio_reg_update(struct uniphier_gpio_priv * priv,unsigned int reg,u32 mask,u32 val)
- Line: 59
- Called by: uniphier_gpio_bank_write, uniphier_gpio_irq_mask, uniphier_gpio_irq_set_type, uniphier_gpio_irq_unmask

### uniphier_gpio_remove
- Return type: static void
- Signature: uniphier_gpio_remove(struct platform_device * pdev)
- Line: 422

### uniphier_gpio_resume
- Return type: static int
- Signature: uniphier_gpio_resume(struct device * dev)
- Line: 451
- Calls: uniphier_gpio_bank_to_reg, uniphier_gpio_get_nbanks, uniphier_gpio_hw_init

### uniphier_gpio_set
- Return type: static int
- Signature: uniphier_gpio_set(struct gpio_chip * chip,unsigned int offset,int val)
- Line: 141
- Calls: uniphier_gpio_offset_write

### uniphier_gpio_set_multiple
- Return type: static int
- Signature: uniphier_gpio_set_multiple(struct gpio_chip * chip,unsigned long * mask,unsigned long * bits)
- Line: 149
- Calls: uniphier_gpio_bank_write

### uniphier_gpio_suspend
- Return type: static int
- Signature: uniphier_gpio_suspend(struct device * dev)
- Line: 429
- Calls: uniphier_gpio_bank_to_reg, uniphier_gpio_get_nbanks

### uniphier_gpio_to_irq
- Return type: static int
- Signature: uniphier_gpio_to_irq(struct gpio_chip * chip,unsigned int offset)
- Line: 165

## Structs (1)

### uniphier_gpio_priv
- Line: 27
- Members:
  - chip: gpio_chip
  - irq_chip: irq_chip
  - domain: irq_domain *
  - regs: void __iomem *
  - lock: spinlock_t
  - saved_vals: u32[]

## Variables (4)

- static **uniphier_gpio_driver** : platform_driver (line 485)
- static **uniphier_gpio_irq_domain_ops** : const struct irq_domain_ops (line 318)
- static **uniphier_gpio_match** : const struct of_device_id[] (line 479)
- static **uniphier_gpio_pm_ops** : const struct dev_pm_ops (line 475)

## Macros (7)

- **UNIPHIER_GPIO_IRQ_EN** (line 22)
- **UNIPHIER_GPIO_IRQ_FLT_CYC** (line 25)
- **UNIPHIER_GPIO_IRQ_FLT_EN** (line 24)
- **UNIPHIER_GPIO_IRQ_MAX_NUM** (line 18)
- **UNIPHIER_GPIO_IRQ_MODE** (line 23)
- **UNIPHIER_GPIO_PORT_DATA** (line 20)
- **UNIPHIER_GPIO_PORT_DIR** (line 21)
