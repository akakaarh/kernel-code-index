# drivers/gpio/gpio-ts4800.c

Subsystem: drivers/gpio

## Functions (1)

### ts4800_gpio_probe
- Return type: static int
- Signature: ts4800_gpio_probe(struct platform_device * pdev)
- Line: 18
- Calls: gpio_generic_chip_init

## Variables (2)

- static **ts4800_gpio_driver** : platform_driver (line 56)
- static **ts4800_gpio_of_match** : const struct of_device_id[] (line 50)

## Macros (3)

- **DIRECTION_REG_OFFSET** (line 16)
- **INPUT_REG_OFFSET** (line 14)
- **OUTPUT_REG_OFFSET** (line 15)
