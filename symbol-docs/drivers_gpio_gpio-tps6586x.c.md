# drivers/gpio/gpio-tps6586x.c

Subsystem: drivers/gpio

## Functions (6)

### tps6586x_gpio_get
- Return type: static int
- Signature: tps6586x_gpio_get(struct gpio_chip * gc,unsigned offset)
- Line: 30
- Calls: gpiochip_get_data

### tps6586x_gpio_init
- Return type: static int __init
- Signature: tps6586x_gpio_init(void)
- Line: 119

### tps6586x_gpio_output
- Return type: static int
- Signature: tps6586x_gpio_output(struct gpio_chip * gc,unsigned offset,int value)
- Line: 52
- Calls: gpiochip_get_data, tps6586x_gpio_set

### tps6586x_gpio_probe
- Return type: static int
- Signature: tps6586x_gpio_probe(struct platform_device * pdev)
- Line: 78

### tps6586x_gpio_set
- Return type: static int
- Signature: tps6586x_gpio_set(struct gpio_chip * gc,unsigned int offset,int value)
- Line: 43
- Calls: gpiochip_get_data
- Called by: tps6586x_gpio_output

### tps6586x_gpio_to_irq
- Return type: static int
- Signature: tps6586x_gpio_to_irq(struct gpio_chip * gc,unsigned offset)
- Line: 70
- Calls: gpiochip_get_data

## Structs (1)

### tps6586x_gpio
- Line: 25
- Members:
  - gpio_chip: gpio_chip
  - parent: device *

## Variables (1)

- static **tps6586x_gpio_driver** : platform_driver (line 114)

## Macros (2)

- **TPS6586X_GPIOSET1** (line 22)
- **TPS6586X_GPIOSET2** (line 23)
