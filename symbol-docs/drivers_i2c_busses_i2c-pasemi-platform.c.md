# drivers/i2c/busses/i2c-pasemi-platform.c

Subsystem: drivers/i2c

## Functions (3)

### pasemi_platform_i2c_calc_clk_div
- Return type: static int
- Signature: pasemi_platform_i2c_calc_clk_div(struct pasemi_platform_i2c_data * data,u32 frequency)
- Line: 24

### pasemi_platform_i2c_probe
- Return type: static int
- Signature: pasemi_platform_i2c_probe(struct platform_device * pdev)
- Line: 45

### pasemi_platform_i2c_remove
- Return type: static void
- Signature: pasemi_platform_i2c_remove(struct platform_device * pdev)
- Line: 92

## Structs (1)

### pasemi_platform_i2c_data
- Line: 18
- Members:
  - smbus: pasemi_smbus
  - clk_ref: clk *

## Variables (2)

- static **pasemi_platform_i2c_driver** : platform_driver (line 101)
- static **pasemi_platform_i2c_of_match** : const struct of_device_id[] (line 94)
