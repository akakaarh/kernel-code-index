# drivers/gpio/gpio-sl28cpld.c

Subsystem: drivers/gpio

## Functions (2)

### sl28cpld_gpio_irq_init
- Return type: static int
- Signature: sl28cpld_gpio_irq_init(struct platform_device * pdev,unsigned int base,struct gpio_regmap_config * config)
- Line: 48
- Called by: sl28cpld_gpio_probe

### sl28cpld_gpio_probe
- Return type: static int
- Signature: sl28cpld_gpio_probe(struct platform_device * pdev)
- Line: 88
- Calls: devm_gpio_regmap_register, sl28cpld_gpio_irq_init

## Enums (1)

### sl28cpld_gpio_type
- Line: 31

## Variables (3)

- static **sl28cpld_gpio_driver** : platform_driver (line 149)
- static **sl28cpld_gpio_irqs** : const struct regmap_irq[] (line 37)
- static **sl28cpld_gpio_of_match** : const struct of_device_id[] (line 141)

## Macros (7)

- **GPIO_REG_DIR** (line 19)
- **GPIO_REG_IE** (line 22)
- **GPIO_REG_IN** (line 21)
- **GPIO_REG_IP** (line 23)
- **GPIO_REG_OUT** (line 20)
- **GPI_REG_IN** (line 26)
- **GPO_REG_OUT** (line 29)
