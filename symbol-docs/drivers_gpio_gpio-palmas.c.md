# drivers/gpio/gpio-palmas.c

Subsystem: drivers/gpio

## Functions (8)

### palmas_gpio_exit
- Return type: static void __exit
- Signature: palmas_gpio_exit(void)
- Line: 201

### palmas_gpio_get
- Return type: static int
- Signature: palmas_gpio_get(struct gpio_chip * gc,unsigned offset)
- Line: 26
- Calls: gpiochip_get_data

### palmas_gpio_init
- Return type: static int __init
- Signature: palmas_gpio_init(void)
- Line: 195

### palmas_gpio_input
- Return type: static int
- Signature: palmas_gpio_input(struct gpio_chip * gc,unsigned offset)
- Line: 101
- Calls: gpiochip_get_data

### palmas_gpio_output
- Return type: static int
- Signature: palmas_gpio_output(struct gpio_chip * gc,unsigned offset,int value)
- Line: 76
- Calls: gpiochip_get_data, palmas_gpio_set

### palmas_gpio_probe
- Return type: static int
- Signature: palmas_gpio_probe(struct platform_device * pdev)
- Line: 144

### palmas_gpio_set
- Return type: static int
- Signature: palmas_gpio_set(struct gpio_chip * gc,unsigned int offset,int value)
- Line: 57
- Calls: gpiochip_get_data
- Called by: palmas_gpio_output

### palmas_gpio_to_irq
- Return type: static int
- Signature: palmas_gpio_to_irq(struct gpio_chip * gc,unsigned offset)
- Line: 119
- Calls: gpiochip_get_data

## Structs (2)

### palmas_device_data
- Line: 22
- Members:
  - gpio_chip: gpio_chip
  - palmas: palmas *
  - ngpio: int

### palmas_gpio
- Line: 17
- Members:
  - gpio_chip: gpio_chip
  - palmas: palmas *
  - ngpio: int

## Variables (4)

- static **of_palmas_gpio_match** : const struct of_device_id[] (line 135)
- static **palmas_dev_data** : const struct palmas_device_data (line 127)
- static **palmas_gpio_driver** : platform_driver (line 189)
- static **tps80036_dev_data** : const struct palmas_device_data (line 131)
