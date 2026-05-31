# drivers/gpio/gpio-fxl6408.c

Subsystem: drivers/gpio

## Functions (3)

### fxl6408_identify
- Return type: static int
- Signature: fxl6408_identify(struct device * dev,struct regmap * regmap)
- Line: 91
- Called by: fxl6408_probe

### fxl6408_probe
- Return type: static int
- Signature: fxl6408_probe(struct i2c_client * client)
- Line: 104
- Calls: devm_gpio_regmap_register, fxl6408_identify

### fxl6408_resume
- Return type: static int
- Signature: fxl6408_resume(struct device * dev)
- Line: 136

## Variables (10)

- static **fxl6408_driver** : i2c_driver (line 158)
- static **fxl6408_dt_ids** : const struct of_device_id[] (line 146)
- static **fxl6408_id** : const struct i2c_device_id[] (line 152)
- static **rd_range** : const struct regmap_range[] (line 46)
- static **rd_table** : const struct regmap_access_table (line 63)
- static **regmap** : const struct regmap_config (line 78)
- static **volatile_range** : const struct regmap_range[] (line 58)
- static **volatile_table** : const struct regmap_access_table (line 73)
- static **wr_range** : const struct regmap_range[] (line 52)
- static **wr_table** : const struct regmap_access_table (line 68)

## Macros (9)

- **FXL6408_MF_FAIRCHILD** (line 18)
- **FXL6408_MF_SHIFT** (line 19)
- **FXL6408_NGPIO** (line 44)
- **FXL6408_REG_DEVICE_ID** (line 17)
- **FXL6408_REG_INPUT_STATUS** (line 34)
- **FXL6408_REG_INT_STS** (line 42)
- **FXL6408_REG_IO_DIR** (line 22)
- **FXL6408_REG_OUTPUT** (line 28)
- **FXL6408_REG_OUTPUT_HIGH_Z** (line 31)
