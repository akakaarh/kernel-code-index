# drivers/gpio/gpio-pca9570.c

Subsystem: drivers/gpio

## Functions (6)

### pca9570_get
- Return type: static int
- Signature: pca9570_get(struct gpio_chip * chip,unsigned offset)
- Line: 83
- Calls: gpiochip_get_data, pca9570_read

### pca9570_get_direction
- Return type: static int
- Signature: pca9570_get_direction(struct gpio_chip * chip,unsigned offset)
- Line: 76

### pca9570_probe
- Return type: static int
- Signature: pca9570_probe(struct i2c_client * client)
- Line: 119
- Calls: pca9570_read

### pca9570_read
- Return type: static int
- Signature: pca9570_read(struct pca9570 * gpio,u8 * value)
- Line: 49
- Called by: pca9570_get, pca9570_probe

### pca9570_set
- Return type: static int
- Signature: pca9570_set(struct gpio_chip * chip,unsigned int offset,int value)
- Line: 96
- Calls: gpiochip_get_data, pca9570_write

### pca9570_write
- Return type: static int
- Signature: pca9570_write(struct pca9570 * gpio,u8 value)
- Line: 66
- Called by: pca9570_set

## Structs (2)

### pca9570
- Line: 42
- Members:
  - ngpio: u16
  - command: u32
  - chip: gpio_chip
  - chip_data: const struct pca9570_chip_data *
  - lock: mutex
  - out: u8

### pca9570_chip_data
- Line: 30
- Members:
  - ngpio: u16
  - command: u32
  - chip: gpio_chip
  - chip_data: const struct pca9570_chip_data *
  - lock: mutex
  - out: u8

## Variables (6)

- static **pca9570_driver** : i2c_driver (line 181)
- static **pca9570_gpio** : const struct pca9570_chip_data (line 152)
- static **pca9570_id_table** : const struct i2c_device_id[] (line 165)
- static **pca9570_of_match_table** : const struct of_device_id[] (line 173)
- static **pca9571_gpio** : const struct pca9570_chip_data (line 156)
- static **slg7xl45106_gpio** : const struct pca9570_chip_data (line 160)

## Macros (1)

- **SLG7XL45106_GPO_REG** (line 23)
