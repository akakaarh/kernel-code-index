# drivers/gpio/gpio-gw-pld.c

Subsystem: drivers/gpio

## Functions (5)

### gw_pld_get8
- Return type: static int
- Signature: gw_pld_get8(struct gpio_chip * gc,unsigned offset)
- Line: 43
- Calls: gpiochip_get_data

### gw_pld_input8
- Return type: static int
- Signature: gw_pld_input8(struct gpio_chip * gc,unsigned offset)
- Line: 35
- Calls: gpiochip_get_data

### gw_pld_output8
- Return type: static int
- Signature: gw_pld_output8(struct gpio_chip * gc,unsigned offset,int value)
- Line: 53
- Calls: gpiochip_get_data
- Called by: gw_pld_set8

### gw_pld_probe
- Return type: static int
- Signature: gw_pld_probe(struct i2c_client * client)
- Line: 70

### gw_pld_set8
- Return type: static int
- Signature: gw_pld_set8(struct gpio_chip * gc,unsigned int offset,int value)
- Line: 65
- Calls: gw_pld_output8

## Structs (1)

### gw_pld
- Line: 24
- Members:
  - chip: gpio_chip
  - client: i2c_client *
  - out: u8

## Variables (3)

- static **gw_pld_driver** : i2c_driver (line 123)
- static **gw_pld_dt_ids** : const struct of_device_id[] (line 117)
- static **gw_pld_id** : const struct i2c_device_id[] (line 111)
