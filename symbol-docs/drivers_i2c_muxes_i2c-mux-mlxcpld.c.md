# drivers/i2c/muxes/i2c-mux-mlxcpld.c

Subsystem: drivers/i2c

## Functions (5)

### mlxcpld_mux_deselect
- Return type: static int
- Signature: mlxcpld_mux_deselect(struct i2c_mux_core * muxc,u32 chan)
- Line: 106

### mlxcpld_mux_probe
- Return type: static int
- Signature: mlxcpld_mux_probe(struct platform_device * pdev)
- Line: 117

### mlxcpld_mux_reg_write
- Return type: static int
- Signature: mlxcpld_mux_reg_write(struct i2c_adapter * adap,struct mlxcpld_mux * mux,u32 val)
- Line: 60

### mlxcpld_mux_remove
- Return type: static void
- Signature: mlxcpld_mux_remove(struct platform_device * pdev)
- Line: 173

### mlxcpld_mux_select_chan
- Return type: static int
- Signature: mlxcpld_mux_select_chan(struct i2c_mux_core * muxc,u32 chan)
- Line: 88

## Structs (1)

### mlxcpld_mux
- Line: 23
- Members:
  - last_val: int
  - client: i2c_client *
  - pdata: mlxcpld_mux_plat_data

## Variables (1)

- static **mlxcpld_mux_driver** : platform_driver (line 180)
