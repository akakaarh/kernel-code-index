# drivers/i2c/muxes/i2c-mux-gpio.c

Subsystem: drivers/i2c

## Functions (6)

### i2c_mux_gpio_deselect
- Return type: static int
- Signature: i2c_mux_gpio_deselect(struct i2c_mux_core * muxc,u32 chan)
- Line: 47

### i2c_mux_gpio_probe
- Return type: static int
- Signature: i2c_mux_gpio_probe(struct platform_device * pdev)
- Line: 128

### i2c_mux_gpio_probe_fw
- Return type: static int
- Signature: i2c_mux_gpio_probe_fw(struct gpiomux * mux,struct platform_device * pdev)
- Line: 56

### i2c_mux_gpio_remove
- Return type: static void
- Signature: i2c_mux_gpio_remove(struct platform_device * pdev)
- Line: 234

### i2c_mux_gpio_select
- Return type: static int
- Signature: i2c_mux_gpio_select(struct i2c_mux_core * muxc,u32 chan)
- Line: 35

### i2c_mux_gpio_set
- Return type: static void
- Signature: i2c_mux_gpio_set(const struct gpiomux * mux,unsigned int val)
- Line: 26

## Structs (1)

### gpiomux
- Line: 20
- Members:
  - data: i2c_mux_gpio_platform_data
  - ngpios: int
  - gpios: gpio_desc **

## Variables (2)

- static **i2c_mux_gpio_driver** : platform_driver (line 248)
- static **i2c_mux_gpio_of_match** : const struct of_device_id[] (line 242)
