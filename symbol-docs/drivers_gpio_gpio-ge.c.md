# drivers/gpio/gpio-ge.c

Subsystem: drivers/gpio

## Functions (1)

### gef_gpio_probe
- Return type: static int __init
- Signature: gef_gpio_probe(struct platform_device * pdev)
- Line: 53
- Calls: gpio_generic_chip_init

## Variables (2)

- static **gef_gpio_driver** : platform_driver (line 102)
- static **gef_gpio_ids** : const struct of_device_id[] (line 38)

## Macros (9)

- **GEF_GPIO_DIRECT** (line 28)
- **GEF_GPIO_IN** (line 29)
- **GEF_GPIO_INT_STAT** (line 34)
- **GEF_GPIO_MODE** (line 36)
- **GEF_GPIO_OUT** (line 30)
- **GEF_GPIO_OVERRUN** (line 35)
- **GEF_GPIO_POLAR_A** (line 32)
- **GEF_GPIO_POLAR_B** (line 33)
- **GEF_GPIO_TRIG** (line 31)
