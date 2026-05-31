# drivers/gpio/gpio-tn48m.c

Subsystem: drivers/gpio

## Functions (1)

### tn48m_gpio_probe
- Return type: static int
- Signature: tn48m_gpio_probe(struct platform_device * pdev)
- Line: 41
- Calls: devm_gpio_regmap_register

## Structs (1)

### tn48m_gpio_config
- Line: 23
- Members:
  - ngpio: int
  - ngpio_per_reg: int
  - type: tn48m_gpio_type

## Enums (1)

### tn48m_gpio_type
- Line: 18

## Variables (4)

- static **tn48m_gpi_config** : const struct tn48m_gpio_config (line 35)
- static **tn48m_gpio_driver** : platform_driver (line 89)
- static **tn48m_gpio_of_match** : const struct of_device_id[] (line 82)
- static **tn48m_gpo_config** : const struct tn48m_gpio_config (line 29)
