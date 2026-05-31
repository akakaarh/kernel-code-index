# drivers/gpio/gpio-max7360.c

Subsystem: drivers/gpio

## Functions (6)

### max7360_get_available_gpos
- Return type: static int
- Signature: max7360_get_available_gpos(struct device * dev,unsigned int * available_gpios)
- Line: 34
- Called by: max7360_gpo_init_valid_mask, max7360_set_gpos_count

### max7360_gpio_probe
- Return type: static int
- Signature: max7360_gpio_probe(struct platform_device * pdev)
- Line: 144
- Calls: devm_gpio_regmap_register, max7360_set_gpos_count

### max7360_gpio_reg_mask_xlate
- Return type: static int
- Signature: max7360_gpio_reg_mask_xlate(struct gpio_regmap * gpio,unsigned int base,unsigned int offset,unsigned int * reg,unsigned int * mask)
- Line: 96

### max7360_gpo_init_valid_mask
- Return type: static int
- Signature: max7360_gpo_init_valid_mask(struct gpio_chip * gc,unsigned long * valid_mask,unsigned int ngpios)
- Line: 50
- Calls: max7360_get_available_gpos

### max7360_handle_mask_sync
- Return type: static int
- Signature: max7360_handle_mask_sync(const int index,const unsigned int mask_buf_def,const unsigned int mask_buf,void * const irq_drv_data)
- Line: 126

### max7360_set_gpos_count
- Return type: static int
- Signature: max7360_set_gpos_count(struct device * dev,struct regmap * regmap)
- Line: 66
- Calls: max7360_get_available_gpos
- Called by: max7360_gpio_probe

## Structs (1)

### max7360_gpio_plat_data
- Line: 27
- Members:
  - function: unsigned int

## Variables (5)

- static **max7360_gpio_col_plat** : max7360_gpio_plat_data (line 32)
- static **max7360_gpio_driver** : platform_driver (line 245)
- static **max7360_gpio_of_match** : const struct of_device_id[] (line 233)
- static **max7360_gpio_port_plat** : max7360_gpio_plat_data (line 31)
- static **max7360_regmap_irqs** : const struct regmap_irq[] (line 115)

## Macros (2)

- **MAX7360_GPIO_COL** (line 25)
- **MAX7360_GPIO_PORT** (line 24)
