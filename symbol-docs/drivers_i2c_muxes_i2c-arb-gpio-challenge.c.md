# drivers/i2c/muxes/i2c-arb-gpio-challenge.c

Subsystem: drivers/i2c

## Functions (4)

### i2c_arbitrator_deselect
- Return type: static int
- Signature: i2c_arbitrator_deselect(struct i2c_mux_core * muxc,u32 chan)
- Line: 85

### i2c_arbitrator_probe
- Return type: static int
- Signature: i2c_arbitrator_probe(struct platform_device * pdev)
- Line: 96

### i2c_arbitrator_remove
- Return type: static void
- Signature: i2c_arbitrator_remove(struct platform_device * pdev)
- Line: 177

### i2c_arbitrator_select
- Return type: static int
- Signature: i2c_arbitrator_select(struct i2c_mux_core * muxc,u32 chan)
- Line: 42

## Structs (1)

### i2c_arbitrator_data
- Line: 28
- Members:
  - our_gpio: gpio_desc *
  - their_gpio: gpio_desc *
  - slew_delay_us: unsigned int
  - wait_retry_us: unsigned int
  - wait_free_us: unsigned int

## Variables (2)

- static **i2c_arbitrator_driver** : platform_driver (line 191)
- static **i2c_arbitrator_of_match** : const struct of_device_id[] (line 185)
