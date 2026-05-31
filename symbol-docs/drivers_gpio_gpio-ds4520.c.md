# drivers/gpio/gpio-ds4520.c

Subsystem: drivers/gpio

## Functions (1)

### ds4520_gpio_probe
- Return type: static int
- Signature: ds4520_gpio_probe(struct i2c_client * client)
- Line: 23
- Calls: devm_gpio_regmap_register

## Variables (4)

- static **ds4520_gpio_driver** : i2c_driver (line 62)
- static **ds4520_gpio_id_table** : const struct i2c_device_id[] (line 56)
- static **ds4520_gpio_of_match_table** : const struct of_device_id[] (line 50)
- static **ds4520_regmap_config** : const struct regmap_config (line 18)

## Macros (3)

- **DS4520_IO_CONTROL0** (line 15)
- **DS4520_IO_STATUS0** (line 16)
- **DS4520_PULLUP0** (line 14)
