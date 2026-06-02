# drivers/i2c/muxes/i2c-mux-mule.c

Subsystem: drivers/i2c

## Functions (4)

### mule_i2c_mux_deselect
- Return type: static int
- Signature: mule_i2c_mux_deselect(struct i2c_mux_core * muxc,u32 dev)
- Line: 30

### mule_i2c_mux_probe
- Return type: static int
- Signature: mule_i2c_mux_probe(struct platform_device * pdev)
- Line: 44

### mule_i2c_mux_remove
- Return type: static void
- Signature: mule_i2c_mux_remove(void * data)
- Line: 35

### mule_i2c_mux_select
- Return type: static int
- Signature: mule_i2c_mux_select(struct i2c_mux_core * muxc,u32 dev)
- Line: 23

## Structs (1)

### mule_i2c_reg_mux
- Line: 19
- Members:
  - regmap: regmap *

## Variables (2)

- static **mule_i2c_mux_driver** : platform_driver (line 135)
- static **mule_i2c_mux_of_match** : const struct of_device_id[] (line 129)

## Macros (2)

- **MULE_I2C_MUX_CONFIG_REG** (line 16)
- **MULE_I2C_MUX_DEFAULT_DEV** (line 17)
