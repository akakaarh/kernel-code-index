# drivers/gpio/gpio-macsmc.c

Subsystem: drivers/gpio

## Functions (8)

### macsmc_gpio_find_first_gpio_index
- Return type: static int
- Signature: macsmc_gpio_find_first_gpio_index(struct macsmc_gpio * smcgp)
- Line: 96
- Calls: macsmc_gpio_key
- Called by: macsmc_gpio_probe

### macsmc_gpio_get
- Return type: static int
- Signature: macsmc_gpio_get(struct gpio_chip * gc,unsigned int offset)
- Line: 163
- Calls: gpiochip_get_data, macsmc_gpio_get_direction, macsmc_gpio_key

### macsmc_gpio_get_direction
- Return type: static int
- Signature: macsmc_gpio_get_direction(struct gpio_chip * gc,unsigned int offset)
- Line: 143
- Calls: gpiochip_get_data, macsmc_gpio_key
- Called by: macsmc_gpio_get

### macsmc_gpio_init_valid_mask
- Return type: static int
- Signature: macsmc_gpio_init_valid_mask(struct gpio_chip * gc,unsigned long * valid_mask,unsigned int ngpios)
- Line: 201
- Calls: gpiochip_get_data, macsmc_gpio_nr

### macsmc_gpio_key
- Return type: static int
- Signature: macsmc_gpio_key(unsigned int offset)
- Line: 91
- Called by: macsmc_gpio_find_first_gpio_index, macsmc_gpio_get, macsmc_gpio_get_direction, macsmc_gpio_probe, macsmc_gpio_set

### macsmc_gpio_nr
- Return type: static int
- Signature: macsmc_gpio_nr(smc_key key)
- Line: 80
- Called by: macsmc_gpio_init_valid_mask

### macsmc_gpio_probe
- Return type: static int
- Signature: macsmc_gpio_probe(struct platform_device * pdev)
- Line: 235
- Calls: macsmc_gpio_find_first_gpio_index, macsmc_gpio_key

### macsmc_gpio_set
- Return type: static int
- Signature: macsmc_gpio_set(struct gpio_chip * gc,unsigned int offset,int value)
- Line: 186
- Calls: gpiochip_get_data, macsmc_gpio_key

## Structs (1)

### macsmc_gpio
- Line: 72
- Members:
  - dev: device *
  - smc: apple_smc *
  - gc: gpio_chip
  - first_index: int

## Variables (2)

- static **macsmc_gpio_driver** : platform_driver (line 282)
- static **macsmc_gpio_of_table** : const struct of_device_id[] (line 276)

## Macros (25)

- **CMD_ACTION** (line 29)
- **CMD_CONFIG** (line 36)
- **CMD_INPUT** (line 31)
- **CMD_IRQ_ACK** (line 34)
- **CMD_IRQ_ENABLE** (line 33)
- **CMD_IRQ_MODE** (line 35)
- **CMD_OUTPUT** (line 30)
- **CMD_PINMODE** (line 32)
- **CONFIG_IRQMODE** (line 53)
- **CONFIG_MASK** (line 49)
- **CONFIG_OUTMODE** (line 52)
- **CONFIG_OUTVAL** (line 56)
- **CONFIG_PULLDOWN** (line 54)
- **CONFIG_PULLUP** (line 55)
- **CONFIG_VAL** (line 50)
- **IRQ_MODE_BOTH** (line 47)
- **IRQ_MODE_FALLING** (line 46)
- **IRQ_MODE_HIGH** (line 43)
- **IRQ_MODE_LOW** (line 44)
- **IRQ_MODE_RISING** (line 45)
- **MAX_GPIO** (line 17)
- **MODE_INPUT** (line 38)
- **MODE_OUTPUT** (line 39)
- **MODE_VALUE_0** (line 40)
- **MODE_VALUE_1** (line 41)
