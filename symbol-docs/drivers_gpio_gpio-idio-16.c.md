# drivers/gpio/gpio-idio-16.c

Subsystem: drivers/gpio

## Functions (3)

### devm_idio_16_regmap_register
- Return type: int
- Signature: devm_idio_16_regmap_register(struct device * const dev,const struct idio_16_regmap_config * const config)
- Line: 103
- Calls: devm_gpio_regmap_register
- Called by: idio_16_probe

### idio_16_handle_mask_sync
- Return type: static int
- Signature: idio_16_handle_mask_sync(const int index,const unsigned int mask_buf_def,const unsigned int mask_buf,void * const irq_drv_data)
- Line: 39

### idio_16_reg_mask_xlate
- Return type: static int
- Signature: idio_16_reg_mask_xlate(struct gpio_regmap * const gpio,const unsigned int base,const unsigned int offset,unsigned int * const reg,unsigned int * const mask)
- Line: 69

## Structs (1)

### idio_16_data
- Line: 34
- Members:
  - map: regmap *
  - irq_mask: unsigned int

## Variables (1)

- static **idio_16_names** : const char * [] (line 89)

## Macros (12)

- **DEFAULT_SYMBOL_NAMESPACE** (line 7)
- **IDIO_16_CLEAR_INTERRUPT** (line 24)
- **IDIO_16_DAT_BASE** (line 21)
- **IDIO_16_DEACTIVATE_INPUT_FILTERS** (line 26)
- **IDIO_16_DISABLE_IRQ** (line 27)
- **IDIO_16_ENABLE_IRQ** (line 25)
- **IDIO_16_INTERRUPT_STATUS** (line 28)
- **IDIO_16_IN_BASE** (line 23)
- **IDIO_16_NGPIO** (line 30)
- **IDIO_16_NGPIO_PER_REG** (line 31)
- **IDIO_16_OUT_BASE** (line 22)
- **IDIO_16_REG_STRIDE** (line 32)
