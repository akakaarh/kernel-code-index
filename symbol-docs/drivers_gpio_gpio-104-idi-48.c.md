# drivers/gpio/gpio-104-idi-48.c

Subsystem: drivers/gpio

## Functions (2)

### idi_48_probe
- Return type: static int
- Signature: idi_48_probe(struct device * dev,unsigned int id)
- Line: 125
- Calls: devm_gpio_regmap_register

### idi_48_reg_mask_xlate
- Return type: static int
- Signature: idi_48_reg_mask_xlate(struct gpio_regmap * gpio,unsigned int base,unsigned int offset,unsigned int * reg,unsigned int * mask)
- Line: 39

## Variables (14)

- static **base** : unsigned int[] (line 26)
- static **idi48_names** : const char * [] (line 114)
- static **idi48_regmap_config** : const struct regmap_config (line 75)
- static **idi48_regmap_irqs** : const struct regmap_irq[] (line 95)
- static **idi_48_driver** : isa_driver (line 179)
- static **idi_48_precious_ranges** : const struct regmap_range[] (line 60)
- static **idi_48_precious_table** : const struct regmap_access_table (line 71)
- static **idi_48_rd_ranges** : const struct regmap_range[] (line 57)
- static **idi_48_rd_table** : const struct regmap_access_table (line 67)
- static **idi_48_wr_ranges** : const struct regmap_range[] (line 54)
- static **idi_48_wr_table** : const struct regmap_access_table (line 63)
- static **irq** : unsigned int[] (line 31)
- static **num_idi_48** : unsigned int (line 27)
- static **num_irq** : unsigned int (line 32)

## Macros (6)

- **IDI48_IRQ_ENABLE** (line 37)
- **IDI48_IRQ_STATUS** (line 36)
- **IDI48_NGPIO** (line 87)
- **IDI48_REGMAP_IRQ**(_id) (line 89)
- **IDI_48_EXTENT** (line 23)
- **MAX_NUM_IDI_48** (line 24)
