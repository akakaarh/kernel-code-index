# drivers/gpio/gpio-loongson-64bit.c

Subsystem: drivers/gpio

## Functions (18)

### loongson_commit_direction
- Return type: static void
- Signature: loongson_commit_direction(struct loongson_gpio_chip * lgpio,unsigned int pin,int input)
- Line: 57
- Called by: loongson_gpio_direction_input, loongson_gpio_direction_output

### loongson_commit_level
- Return type: static void
- Signature: loongson_commit_level(struct loongson_gpio_chip * lgpio,unsigned int pin,int high)
- Line: 65
- Called by: loongson_gpio_direction_output, loongson_gpio_set

### loongson_gpio_direction_input
- Return type: static int
- Signature: loongson_gpio_direction_input(struct gpio_chip * chip,unsigned int pin)
- Line: 72
- Calls: loongson_commit_direction, to_loongson_gpio_chip

### loongson_gpio_direction_output
- Return type: static int
- Signature: loongson_gpio_direction_output(struct gpio_chip * chip,unsigned int pin,int value)
- Line: 84
- Calls: loongson_commit_direction, loongson_commit_level, loongson_gpio_set_value, to_loongson_gpio_chip

### loongson_gpio_get
- Return type: static int
- Signature: loongson_gpio_get(struct gpio_chip * chip,unsigned int pin)
- Line: 97
- Calls: to_loongson_gpio_chip

### loongson_gpio_get_direction
- Return type: static int
- Signature: loongson_gpio_get_direction(struct gpio_chip * chip,unsigned int pin)
- Line: 109
- Calls: to_loongson_gpio_chip

### loongson_gpio_init
- Return type: static int
- Signature: loongson_gpio_init(struct platform_device * pdev,struct loongson_gpio_chip * lgpio,void __iomem * reg_base)
- Line: 287
- Calls: gpio_generic_chip_init, loongson_gpio_init_irqchip
- Called by: loongson_gpio_probe

### loongson_gpio_init_irqchip
- Return type: static int
- Signature: loongson_gpio_init_irqchip(struct platform_device * pdev,struct loongson_gpio_chip * lgpio)
- Line: 250
- Called by: loongson_gpio_init

### loongson_gpio_irq_ack
- Return type: static void
- Signature: loongson_gpio_irq_ack(struct irq_data * data)
- Line: 151
- Calls: to_loongson_gpio_chip

### loongson_gpio_irq_mask
- Return type: static void
- Signature: loongson_gpio_irq_mask(struct irq_data * data)
- Line: 160
- Calls: to_loongson_gpio_chip

### loongson_gpio_irq_set_type
- Return type: static int
- Signature: loongson_gpio_irq_set_type(struct irq_data * data,unsigned int type)
- Line: 178
- Calls: to_loongson_gpio_chip

### loongson_gpio_irq_unmask
- Return type: static void
- Signature: loongson_gpio_irq_unmask(struct irq_data * data)
- Line: 169
- Calls: to_loongson_gpio_chip

### loongson_gpio_ls2k0300_irq_handler
- Return type: static void
- Signature: loongson_gpio_ls2k0300_irq_handler(struct irq_desc * desc)
- Line: 218

### loongson_gpio_probe
- Return type: static int
- Signature: loongson_gpio_probe(struct platform_device * pdev)
- Line: 332
- Calls: loongson_gpio_init

### loongson_gpio_set
- Return type: static int
- Signature: loongson_gpio_set(struct gpio_chip * chip,unsigned int pin,int value)
- Line: 121
- Calls: loongson_commit_level, to_loongson_gpio_chip

### loongson_gpio_setup
- Return type: static int __init
- Signature: loongson_gpio_setup(void)
- Line: 572

### loongson_gpio_to_irq
- Return type: static int
- Signature: loongson_gpio_to_irq(struct gpio_chip * chip,unsigned int offset)
- Line: 133
- Calls: to_loongson_gpio_chip

### to_loongson_gpio_chip
- Return type: static loongson_gpio_chip *
- Signature: to_loongson_gpio_chip(struct gpio_chip * chip)
- Line: 51
- Called by: loongson_gpio_direction_input, loongson_gpio_direction_output, loongson_gpio_get, loongson_gpio_get_direction, loongson_gpio_irq_ack, loongson_gpio_irq_mask, loongson_gpio_irq_set_type, loongson_gpio_irq_unmask, loongson_gpio_set, loongson_gpio_to_irq

## Structs (2)

### loongson_gpio_chip
- Line: 44
- Members:
  - label: const char *
  - mode: loongson_gpio_mode
  - conf_offset: unsigned int
  - out_offset: unsigned int
  - in_offset: unsigned int
  - inten_offset: unsigned int
  - intpol_offset: unsigned int
  - intedge_offset: unsigned int
  - intclr_offset: unsigned int
  - intsts_offset: unsigned int
  - intdual_offset: unsigned int
  - intr_num: unsigned int
  - irq_handler: irq_flow_handler_t
  - girqchip: const struct irq_chip *
  - chip: gpio_generic_chip
  - lock: spinlock_t
  - reg_base: void __iomem *
  - chip_data: const struct loongson_gpio_chip_data *

### loongson_gpio_chip_data
- Line: 27
- Members:
  - label: const char *
  - mode: loongson_gpio_mode
  - conf_offset: unsigned int
  - out_offset: unsigned int
  - in_offset: unsigned int
  - inten_offset: unsigned int
  - intpol_offset: unsigned int
  - intedge_offset: unsigned int
  - intclr_offset: unsigned int
  - intsts_offset: unsigned int
  - intdual_offset: unsigned int
  - intr_num: unsigned int
  - irq_handler: irq_flow_handler_t
  - girqchip: const struct irq_chip *
  - chip: gpio_generic_chip
  - lock: spinlock_t
  - reg_base: void __iomem *
  - chip_data: const struct loongson_gpio_chip_data *

## Enums (1)

### loongson_gpio_mode
- Line: 22

## Variables (16)

- static **loongson_gpio_acpi_match** : const struct acpi_device_id[] (line 526)
- static **loongson_gpio_driver** : platform_driver (line 563)
- static **loongson_gpio_ls2k0300_data** : const struct loongson_gpio_chip_data (line 365)
- static **loongson_gpio_ls2k0300_irqchip** : const struct irq_chip (line 241)
- static **loongson_gpio_ls2k0500_data0** : const struct loongson_gpio_chip_data (line 382)
- static **loongson_gpio_ls2k0500_data1** : const struct loongson_gpio_chip_data (line 391)
- static **loongson_gpio_ls2k2000_data0** : const struct loongson_gpio_chip_data (line 400)
- static **loongson_gpio_ls2k2000_data1** : const struct loongson_gpio_chip_data (line 409)
- static **loongson_gpio_ls2k2000_data2** : const struct loongson_gpio_chip_data (line 418)
- static **loongson_gpio_ls2k_data** : const struct loongson_gpio_chip_data (line 356)
- static **loongson_gpio_ls3a5000_data** : const struct loongson_gpio_chip_data (line 426)
- static **loongson_gpio_ls3a6000_data** : const struct loongson_gpio_chip_data (line 464)
- static **loongson_gpio_ls7a2000_data0** : const struct loongson_gpio_chip_data (line 445)
- static **loongson_gpio_ls7a2000_data1** : const struct loongson_gpio_chip_data (line 455)
- static **loongson_gpio_ls7a_data** : const struct loongson_gpio_chip_data (line 435)
- static **loongson_gpio_of_match** : const struct of_device_id[] (line 473)
