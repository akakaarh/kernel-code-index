# drivers/gpio/gpio-pci-idio-16.c

Subsystem: drivers/gpio

## Functions (1)

### idio_16_probe
- Return type: static int
- Signature: idio_16_probe(struct pci_dev * pdev,const struct pci_device_id * id)
- Line: 69
- Calls: devm_idio_16_regmap_register

## Variables (10)

- static **idio_16_driver** : pci_driver (line 105)
- static **idio_16_pci_dev_id** : const struct pci_device_id[] (line 100)
- static **idio_16_precious_ranges** : const struct regmap_range[] (line 24)
- static **idio_16_precious_table** : const struct regmap_access_table (line 35)
- static **idio_16_rd_ranges** : const struct regmap_range[] (line 21)
- static **idio_16_rd_table** : const struct regmap_access_table (line 31)
- static **idio_16_regmap_config** : const struct regmap_config (line 39)
- static **idio_16_regmap_irqs** : const struct regmap_irq[] (line 60)
- static **idio_16_wr_ranges** : const struct regmap_range[] (line 18)
- static **idio_16_wr_table** : const struct regmap_access_table (line 27)

## Macros (1)

- **IDIO_16_REGMAP_IRQ**(_id) (line 54)
