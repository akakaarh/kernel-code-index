# drivers/gpio/gpio-tps65218.c

Subsystem: drivers/gpio

## Functions (6)

### tps65218_gpio_get
- Return type: static int
- Signature: tps65218_gpio_get(struct gpio_chip * gc,unsigned offset)
- Line: 23
- Calls: gpiochip_get_data

### tps65218_gpio_output
- Return type: static int
- Signature: tps65218_gpio_output(struct gpio_chip * gc,unsigned offset,int value)
- Line: 54
- Calls: tps65218_gpio_set

### tps65218_gpio_probe
- Return type: static int
- Signature: tps65218_gpio_probe(struct platform_device * pdev)
- Line: 179

### tps65218_gpio_request
- Return type: static int
- Signature: tps65218_gpio_request(struct gpio_chip * gc,unsigned offset)
- Line: 61
- Calls: gpiochip_get_data, gpiochip_line_is_open_drain, gpiochip_line_is_open_source

### tps65218_gpio_set
- Return type: static int
- Signature: tps65218_gpio_set(struct gpio_chip * gc,unsigned int offset,int value)
- Line: 37
- Calls: gpiochip_get_data
- Called by: tps65218_gpio_output

### tps65218_gpio_set_config
- Return type: static int
- Signature: tps65218_gpio_set_config(struct gpio_chip * gc,unsigned offset,unsigned long config)
- Line: 132
- Calls: gpiochip_get_data

## Structs (1)

### tps65218_gpio
- Line: 18
- Members:
  - tps65218: tps65218 *
  - gpio_chip: gpio_chip

## Variables (4)

- static **template_chip** : const struct gpio_chip (line 166)
- static **tps65218_dt_match** : const struct of_device_id[] (line 197)
- static **tps65218_gpio_driver** : platform_driver (line 209)
- static **tps65218_gpio_id_table** : const struct platform_device_id[] (line 203)
