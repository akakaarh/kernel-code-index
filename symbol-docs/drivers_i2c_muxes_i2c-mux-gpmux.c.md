# drivers/i2c/muxes/i2c-mux-gpmux.c

Subsystem: drivers/i2c

## Functions (5)

### i2c_mux_deselect
- Return type: static int
- Signature: i2c_mux_deselect(struct i2c_mux_core * muxc,u32 chan)
- Line: 34

### i2c_mux_probe
- Return type: static int
- Signature: i2c_mux_probe(struct platform_device * pdev)
- Line: 69

### i2c_mux_remove
- Return type: static void
- Signature: i2c_mux_remove(struct platform_device * pdev)
- Line: 145

### i2c_mux_select
- Return type: static int
- Signature: i2c_mux_select(struct i2c_mux_core * muxc,u32 chan)
- Line: 23

### mux_parent_adapter
- Return type: static i2c_adapter *
- Signature: mux_parent_adapter(struct device * dev)
- Line: 44

## Structs (1)

### mux
- Line: 17
- Members:
  - control: mux_control *
  - do_not_deselect: bool

## Variables (2)

- static **i2c_mux_driver** : platform_driver (line 153)
- static **i2c_mux_of_match** : const struct of_device_id[] (line 63)
