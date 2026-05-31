# drivers/gpio/gpio-gpio-mm.c

Subsystem: drivers/gpio

## Functions (1)

### gpiomm_probe
- Return type: static int
- Signature: gpiomm_probe(struct device * dev,unsigned int id)
- Line: 62
- Calls: devm_i8255_regmap_register

## Variables (7)

- static **base** : unsigned int[] (line 26)
- static **gpiomm_driver** : isa_driver (line 90)
- static **gpiomm_names** : const char * [] (line 51)
- static **gpiomm_regmap_config** : const struct regmap_config (line 40)
- static **gpiomm_volatile_ranges** : const struct regmap_range[] (line 33)
- static **gpiomm_volatile_table** : const struct regmap_access_table (line 36)
- static **num_gpiomm** : unsigned int (line 27)

## Macros (4)

- **GPIOMM_EXTENT** (line 23)
- **GPIOMM_NGPIO** (line 50)
- **GPIOMM_NUM_PPI** (line 31)
- **MAX_NUM_GPIOMM** (line 24)
