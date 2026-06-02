# drivers/i2c/muxes/i2c-mux-reg.c

Subsystem: drivers/i2c

## Functions (7)

### i2c_mux_reg_deselect
- Return type: static int
- Signature: i2c_mux_reg_deselect(struct i2c_mux_core * muxc,u32 chan)
- Line: 68

### i2c_mux_reg_probe
- Return type: static int
- Signature: i2c_mux_reg_probe(struct platform_device * pdev)
- Line: 156

### i2c_mux_reg_probe_dt
- Return type: static int
- Signature: i2c_mux_reg_probe_dt(struct regmux * mux,struct platform_device * pdev)
- Line: 149

### i2c_mux_reg_probe_dt
- Return type: static int
- Signature: i2c_mux_reg_probe_dt(struct regmux * mux,struct platform_device * pdev)
- Line: 79

### i2c_mux_reg_remove
- Return type: static void
- Signature: i2c_mux_reg_remove(struct platform_device * pdev)
- Line: 234

### i2c_mux_reg_select
- Return type: static int
- Signature: i2c_mux_reg_select(struct i2c_mux_core * muxc,u32 chan)
- Line: 61

### i2c_mux_reg_set
- Return type: static int
- Signature: i2c_mux_reg_set(const struct regmux * mux,unsigned int chan_id)
- Line: 23

## Structs (1)

### regmux
- Line: 19
- Members:
  - data: i2c_mux_reg_platform_data

## Variables (2)

- static **i2c_mux_reg_driver** : platform_driver (line 248)
- static **i2c_mux_reg_of_match** : const struct of_device_id[] (line 242)
