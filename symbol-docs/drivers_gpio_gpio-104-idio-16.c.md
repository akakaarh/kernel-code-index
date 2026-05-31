# drivers/gpio/gpio-104-idio-16.c

Subsystem: drivers/gpio

## Functions (1)

### idio_16_probe
- Return type: static int
- Signature: idio_16_probe(struct device * dev,unsigned int id)
- Line: 87
- Calls: devm_idio_16_regmap_register

## Variables (13)

- static **base** : unsigned int[] (line 26)
- static **idio_16_driver** : isa_driver (line 118)
- static **idio_16_precious_ranges** : const struct regmap_range[] (line 42)
- static **idio_16_precious_table** : const struct regmap_access_table (line 53)
- static **idio_16_rd_ranges** : const struct regmap_range[] (line 39)
- static **idio_16_rd_table** : const struct regmap_access_table (line 49)
- static **idio_16_regmap_config** : const struct regmap_config (line 57)
- static **idio_16_regmap_irqs** : const struct regmap_irq[] (line 78)
- static **idio_16_wr_ranges** : const struct regmap_range[] (line 36)
- static **idio_16_wr_table** : const struct regmap_access_table (line 45)
- static **irq** : unsigned int[] (line 31)
- static **num_idio_16** : unsigned int (line 27)
- static **num_irq** : unsigned int (line 32)

## Macros (3)

- **IDIO_16_EXTENT** (line 23)
- **IDIO_16_REGMAP_IRQ**(_id) (line 72)
- **MAX_NUM_IDIO_16** (line 24)
