# drivers/gpio/gpio-sama5d2-piobu.c

Subsystem: drivers/gpio

## Functions (9)

### sama5d2_piobu_direction_input
- Return type: static int
- Signature: sama5d2_piobu_direction_input(struct gpio_chip * chip,unsigned int pin)
- Line: 129
- Calls: sama5d2_piobu_write_value

### sama5d2_piobu_direction_output
- Return type: static int
- Signature: sama5d2_piobu_direction_output(struct gpio_chip * chip,unsigned int pin,int value)
- Line: 138
- Calls: sama5d2_piobu_write_value

### sama5d2_piobu_get
- Return type: static int
- Signature: sama5d2_piobu_get(struct gpio_chip * chip,unsigned int pin)
- Line: 153
- Calls: sama5d2_piobu_get_direction, sama5d2_piobu_read_value

### sama5d2_piobu_get_direction
- Return type: static int
- Signature: sama5d2_piobu_get_direction(struct gpio_chip * chip,unsigned int pin)
- Line: 114
- Calls: sama5d2_piobu_read_value
- Called by: sama5d2_piobu_get

### sama5d2_piobu_probe
- Return type: static int
- Signature: sama5d2_piobu_probe(struct platform_device * pdev)
- Line: 183
- Calls: sama5d2_piobu_setup_pin

### sama5d2_piobu_read_value
- Return type: static int
- Signature: sama5d2_piobu_read_value(struct gpio_chip * chip,unsigned int pin,unsigned int mask)
- Line: 95
- Called by: sama5d2_piobu_get, sama5d2_piobu_get_direction

### sama5d2_piobu_set
- Return type: static int
- Signature: sama5d2_piobu_set(struct gpio_chip * chip,unsigned int pin,int value)
- Line: 172
- Calls: sama5d2_piobu_write_value

### sama5d2_piobu_setup_pin
- Return type: static int
- Signature: sama5d2_piobu_setup_pin(struct gpio_chip * chip,unsigned int pin)
- Line: 58
- Called by: sama5d2_piobu_probe

### sama5d2_piobu_write_value
- Return type: static int
- Signature: sama5d2_piobu_write_value(struct gpio_chip * chip,unsigned int pin,unsigned int mask,unsigned int value)
- Line: 79
- Called by: sama5d2_piobu_direction_input, sama5d2_piobu_direction_output, sama5d2_piobu_set

## Structs (1)

### sama5d2_piobu
- Line: 47
- Members:
  - chip: gpio_chip
  - regmap: regmap *

## Variables (2)

- static **sama5d2_piobu_driver** : platform_driver (line 235)
- static **sama5d2_piobu_ids** : const struct of_device_id[] (line 229)

## Macros (14)

- **PIOBU_BASE** (line 32)
- **PIOBU_BMPR** (line 28)
- **PIOBU_DET_OFFSET** (line 34)
- **PIOBU_DIRECTION** (line 37)
- **PIOBU_HIGH** (line 44)
- **PIOBU_IN** (line 39)
- **PIOBU_LOW** (line 45)
- **PIOBU_NMPR** (line 29)
- **PIOBU_NUM** (line 20)
- **PIOBU_OUT** (line 38)
- **PIOBU_PDS** (line 42)
- **PIOBU_REG_SIZE** (line 21)
- **PIOBU_SOD** (line 41)
- **PIOBU_WKPR** (line 30)
