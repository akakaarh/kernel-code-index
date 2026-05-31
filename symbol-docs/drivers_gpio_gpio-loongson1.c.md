# drivers/gpio/gpio-loongson1.c

Subsystem: drivers/gpio

## Functions (3)

### ls1x_gpio_free
- Return type: static void
- Signature: ls1x_gpio_free(struct gpio_chip * gc,unsigned int offset)
- Line: 37
- Calls: gpiochip_get_data

### ls1x_gpio_probe
- Return type: static int
- Signature: ls1x_gpio_probe(struct platform_device * pdev)
- Line: 47
- Calls: gpio_generic_chip_init

### ls1x_gpio_request
- Return type: static int
- Signature: ls1x_gpio_request(struct gpio_chip * gc,unsigned int offset)
- Line: 25
- Calls: gpiochip_get_data

## Structs (1)

### ls1x_gpio_chip
- Line: 20
- Members:
  - chip: gpio_generic_chip
  - reg_base: void __iomem *

## Variables (2)

- static **ls1x_gpio_driver** : platform_driver (line 104)
- static **ls1x_gpio_dt_ids** : const struct of_device_id[] (line 98)

## Macros (4)

- **GPIO_CFG** (line 15)
- **GPIO_DATA** (line 17)
- **GPIO_DIR** (line 16)
- **GPIO_OUTPUT** (line 18)
