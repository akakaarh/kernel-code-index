# drivers/i2c/muxes/i2c-mux-pinctrl.c

Subsystem: drivers/i2c

## Functions (6)

### i2c_mux_pinctrl_deselect
- Return type: static int
- Signature: i2c_mux_pinctrl_deselect(struct i2c_mux_core * muxc,u32 chan)
- Line: 29

### i2c_mux_pinctrl_parent_adapter
- Return type: static i2c_adapter *
- Signature: i2c_mux_pinctrl_parent_adapter(struct device * dev)
- Line: 54

### i2c_mux_pinctrl_probe
- Return type: static int
- Signature: i2c_mux_pinctrl_probe(struct platform_device * pdev)
- Line: 73

### i2c_mux_pinctrl_remove
- Return type: static void
- Signature: i2c_mux_pinctrl_remove(struct platform_device * pdev)
- Line: 169

### i2c_mux_pinctrl_root_adapter
- Return type: static i2c_adapter *
- Signature: i2c_mux_pinctrl_root_adapter(struct pinctrl_state * state)
- Line: 34

### i2c_mux_pinctrl_select
- Return type: static int
- Signature: i2c_mux_pinctrl_select(struct i2c_mux_core * muxc,u32 chan)
- Line: 22

## Structs (1)

### i2c_mux_pinctrl
- Line: 17
- Members:
  - pinctrl: pinctrl *
  - states: pinctrl_state * []

## Variables (2)

- static **i2c_mux_pinctrl_driver** : platform_driver (line 183)
- static **i2c_mux_pinctrl_of_match** : const struct of_device_id[] (line 177)
