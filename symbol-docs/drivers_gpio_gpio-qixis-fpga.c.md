# drivers/gpio/gpio-qixis-fpga.c

Subsystem: drivers/gpio

## Functions (1)

### qixis_cpld_gpio_probe
- Return type: static int
- Signature: qixis_cpld_gpio_probe(struct platform_device * pdev)
- Line: 34
- Calls: devm_gpio_regmap_register

## Structs (1)

### qixis_cpld_gpio_config
- Line: 17
- Members:
  - output_lines: u64

## Variables (5)

- static **ls1046aqds_stat_pres2_cfg** : const struct qixis_cpld_gpio_config (line 25)
- static **lx2160ardb_sfp_cfg** : const struct qixis_cpld_gpio_config (line 21)
- static **qixis_cpld_gpio_driver** : platform_driver (line 100)
- static **qixis_cpld_gpio_of_match** : const struct of_device_id[] (line 86)
- static **regmap_config_8r_8v** : const struct regmap_config (line 29)
