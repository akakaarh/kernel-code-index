# drivers/gpio/gpio-tps65910.c

Subsystem: drivers/gpio

## Functions (8)

### tps65910_gpio_get
- Return type: static int
- Signature: tps65910_gpio_get(struct gpio_chip * gc,unsigned offset)
- Line: 25
- Calls: gpiochip_get_data

### tps65910_gpio_init
- Return type: static int __init
- Signature: tps65910_gpio_init(void)
- Line: 180

### tps65910_gpio_input
- Return type: static int
- Signature: tps65910_gpio_input(struct gpio_chip * gc,unsigned offset)
- Line: 69
- Calls: gpiochip_get_data

### tps65910_gpio_output
- Return type: static int
- Signature: tps65910_gpio_output(struct gpio_chip * gc,unsigned offset,int value)
- Line: 53
- Calls: gpiochip_get_data, tps65910_gpio_set

### tps65910_gpio_probe
- Return type: static int
- Signature: tps65910_gpio_probe(struct platform_device * pdev)
- Line: 109
- Calls: tps65910_parse_dt_for_gpio

### tps65910_gpio_set
- Return type: static int
- Signature: tps65910_gpio_set(struct gpio_chip * gc,unsigned int offset,int value)
- Line: 39
- Calls: gpiochip_get_data
- Called by: tps65910_gpio_output

### tps65910_parse_dt_for_gpio
- Return type: static tps65910_board *
- Signature: tps65910_parse_dt_for_gpio(struct device * dev,struct tps65910 * tps65910,int chip_ngpio)
- Line: 102
- Called by: tps65910_gpio_probe

### tps65910_parse_dt_for_gpio
- Return type: static tps65910_board *
- Signature: tps65910_parse_dt_for_gpio(struct device * dev,struct tps65910 * tps65910,int chip_ngpio)
- Line: 79
- Called by: tps65910_gpio_probe

## Structs (1)

### tps65910_gpio
- Line: 20
- Members:
  - gpio_chip: gpio_chip
  - tps65910: tps65910 *

## Variables (1)

- static **tps65910_gpio_driver** : platform_driver (line 175)
