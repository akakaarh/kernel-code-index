# drivers/gpio/gpio-sodaville.c

Subsystem: drivers/gpio

## Functions (5)

### sdv_gpio_probe
- Return type: static int
- Signature: sdv_gpio_probe(struct pci_dev * pdev,const struct pci_device_id * pci_id)
- Line: 181
- Calls: gpio_generic_chip_init, sdv_register_irqsupport

### sdv_gpio_pub_irq_handler
- Return type: static irqreturn_t
- Signature: sdv_gpio_pub_irq_handler(int irq,void * data)
- Line: 77

### sdv_gpio_pub_set_type
- Return type: static int
- Signature: sdv_gpio_pub_set_type(struct irq_data * d,unsigned int type)
- Line: 46

### sdv_register_irqsupport
- Return type: static int
- Signature: sdv_register_irqsupport(struct sdv_gpio_chip_data * sd,struct pci_dev * pdev)
- Line: 126
- Called by: sdv_gpio_probe

### sdv_xlate
- Return type: static int
- Signature: sdv_xlate(struct irq_domain * h,struct device_node * node,const u32 * intspec,u32 intsize,irq_hw_number_t * out_hwirq,u32 * out_type)
- Line: 93

## Structs (1)

### sdv_gpio_chip_data
- Line: 38
- Members:
  - irq_base: int
  - gpio_pub_base: void __iomem *
  - id: irq_domain *
  - gc: irq_chip_generic *
  - gen_gc: gpio_generic_chip

## Variables (3)

- static **irq_domain_sdv_ops** : const struct irq_domain_ops (line 122)
- static **sdv_gpio_driver** : pci_driver (line 245)
- static **sdv_gpio_pci_ids** : const struct pci_device_id[] (line 240)

## Macros (12)

- **DRV_NAME** (line 22)
- **GPINR** (line 29)
- **GPIO_BAR** (line 25)
- **GPIO_INT** (line 33)
- **GPIT1R0** (line 32)
- **GPIT1R1** (line 34)
- **GPMUXCTL** (line 36)
- **GPOER** (line 28)
- **GPOUTR** (line 27)
- **GPSTR** (line 31)
- **PCI_DEVICE_ID_SDV_GPIO** (line 24)
- **SDV_NUM_PUB_GPIOS** (line 23)
