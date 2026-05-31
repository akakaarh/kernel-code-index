# drivers/gpio/gpio-pcie-idio-24.c

Subsystem: drivers/gpio

## Functions (4)

### idio_24_handle_mask_sync
- Return type: static int
- Signature: idio_24_handle_mask_sync(const int index,const unsigned int mask_buf_def,const unsigned int mask_buf,void * const irq_drv_data)
- Line: 158

### idio_24_probe
- Return type: static int
- Signature: idio_24_probe(struct pci_dev * pdev,const struct pci_device_id * id)
- Line: 292
- Calls: devm_gpio_regmap_register

### idio_24_reg_mask_xlate
- Return type: static int
- Signature: idio_24_reg_mask_xlate(struct gpio_regmap * const gpio,const unsigned int base,const unsigned int offset,unsigned int * const reg,unsigned int * const mask)
- Line: 228
- Calls: gpio_regmap_get_drvdata

### idio_24_set_type_config
- Return type: static int
- Signature: idio_24_set_type_config(unsigned int ** const buf,const unsigned int type,const struct regmap_irq * const irq_data,const int idx,void * const irq_drv_data)
- Line: 178

## Structs (1)

### idio_24_gpio
- Line: 152
- Members:
  - map: regmap *
  - lock: raw_spinlock_t
  - irq_type: u8

## Variables (12)

- static **idio_24_driver** : pci_driver (line 391)
- static **idio_24_names** : const char * [] (line 282)
- static **idio_24_pci_dev_id** : const struct pci_device_id[] (line 384)
- static **idio_24_rd_ranges** : const struct regmap_range[] (line 91)
- static **idio_24_rd_table** : const struct regmap_access_table (line 101)
- static **idio_24_regmap_config** : const struct regmap_config (line 110)
- static **idio_24_regmap_irqs** : const struct regmap_irq[] (line 132)
- static **idio_24_volatile_ranges** : const struct regmap_range[] (line 94)
- static **idio_24_volatile_table** : const struct regmap_access_table (line 105)
- static **idio_24_wr_ranges** : const struct regmap_range[] (line 87)
- static **idio_24_wr_table** : const struct regmap_access_table (line 97)
- static **pex8311_intcsr_regmap_config** : const struct regmap_config (line 78)

## Macros (21)

- **CONTROL_REG_OUT_MODE** (line 72)
- **COS_ENABLE_BOTH** (line 76)
- **COS_ENABLE_FALLING** (line 75)
- **COS_ENABLE_RISING** (line 74)
- **IDIO_24_CONTROL_REG** (line 68)
- **IDIO_24_COS_ENABLE** (line 69)
- **IDIO_24_COS_STATUS_BASE** (line 67)
- **IDIO_24_ENABLE_IRQ** (line 61)
- **IDIO_24_IIN_IRQ**(_id) (line 129)
- **IDIO_24_IN_BASE** (line 65)
- **IDIO_24_NGPIO** (line 281)
- **IDIO_24_NGPIO_PER_REG** (line 122)
- **IDIO_24_OUT_BASE** (line 63)
- **IDIO_24_REGMAP_IRQ**(_id) (line 123)
- **IDIO_24_SOFT_RESET** (line 70)
- **IDIO_24_TTLCMOS_IN_REG** (line 66)
- **IDIO_24_TTLCMOS_OUT_REG** (line 64)
- **IDIO_24_TTL_IRQ**(_id) (line 130)
- **INTCSR_INTERNAL_PCI_WIRE** (line 59)
- **INTCSR_LOCAL_INPUT** (line 60)
- **PLX_PEX8311_PCI_LCS_INTCSR** (line 58)
