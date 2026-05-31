# drivers/gpio/gpio-tpic2810.c

Subsystem: drivers/gpio

## Functions (6)

### tpic2810_direction_output
- Return type: static int
- Signature: tpic2810_direction_output(struct gpio_chip * chip,unsigned offset,int value)
- Line: 37
- Calls: tpic2810_set

### tpic2810_get_direction
- Return type: static int
- Signature: tpic2810_get_direction(struct gpio_chip * chip,unsigned offset)
- Line: 30

### tpic2810_probe
- Return type: static int
- Signature: tpic2810_probe(struct i2c_client * client)
- Line: 96

### tpic2810_set
- Return type: static int
- Signature: tpic2810_set(struct gpio_chip * chip,unsigned int offset,int value)
- Line: 63
- Calls: tpic2810_set_mask_bits
- Called by: tpic2810_direction_output

### tpic2810_set_mask_bits
- Return type: static void
- Signature: tpic2810_set_mask_bits(struct gpio_chip * chip,u8 mask,u8 bits)
- Line: 44
- Calls: gpiochip_get_data
- Called by: tpic2810_set, tpic2810_set_multiple

### tpic2810_set_multiple
- Return type: static int
- Signature: tpic2810_set_multiple(struct gpio_chip * chip,unsigned long * mask,unsigned long * bits)
- Line: 70
- Calls: tpic2810_set_mask_bits

## Structs (1)

### tpic2810
- Line: 21
- Members:
  - chip: gpio_chip
  - client: i2c_client *
  - buffer: u8
  - lock: mutex

## Variables (4)

- static **template_chip** : const struct gpio_chip (line 78)
- static **tpic2810_driver** : i2c_driver (line 120)
- static **tpic2810_id_table** : const struct i2c_device_id[] (line 114)
- static **tpic2810_of_match_table** : const struct of_device_id[] (line 90)

## Macros (1)

- **TPIC2810_WS_COMMAND** (line 12)
