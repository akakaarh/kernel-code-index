# drivers/gpio/gpio-line-mux.c

Subsystem: drivers/gpio

## Functions (3)

### gpio_lmux_gpio_get
- Return type: static int
- Signature: gpio_lmux_gpio_get(struct gpio_chip * gc,unsigned int offset)
- Line: 27
- Calls: gpiochip_get_data, gpiod_get_raw_value_cansleep

### gpio_lmux_gpio_get_direction
- Return type: static int
- Signature: gpio_lmux_gpio_get_direction(struct gpio_chip * gc,unsigned int offset)
- Line: 42

### gpio_lmux_probe
- Return type: static int
- Signature: gpio_lmux_probe(struct platform_device * pdev)
- Line: 48
- Calls: devm_gpiod_get

## Structs (1)

### gpio_lmux
- Line: 18
- Members:
  - gc: gpio_chip
  - mux: mux_control *
  - muxed_gpio: gpio_desc *
  - num_gpio_mux_states: u32

## Variables (2)

- static **gpio_lmux_driver** : platform_driver (line 105)
- static **gpio_lmux_of_match** : const struct of_device_id[] (line 99)

## Macros (1)

- **MUX_SELECT_DELAY_US** (line 16)
