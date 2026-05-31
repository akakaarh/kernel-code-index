# drivers/gpio/gpio-en7523.c

Subsystem: drivers/gpio

## Functions (5)

### airoha_dir_in
- Return type: static int
- Signature: airoha_dir_in(struct gpio_chip * gc,unsigned int gpio)
- Line: 62
- Calls: airoha_dir_set

### airoha_dir_out
- Return type: static int
- Signature: airoha_dir_out(struct gpio_chip * gc,unsigned int gpio,int val)
- Line: 56
- Calls: airoha_dir_set

### airoha_dir_set
- Return type: static int
- Signature: airoha_dir_set(struct gpio_chip * gc,unsigned int gpio,int val,int out)
- Line: 30
- Calls: gpiochip_get_data
- Called by: airoha_dir_in, airoha_dir_out

### airoha_get_dir
- Return type: static int
- Signature: airoha_get_dir(struct gpio_chip * gc,unsigned int gpio)
- Line: 67
- Calls: gpiochip_get_data

### airoha_gpio_probe
- Return type: static int
- Signature: airoha_gpio_probe(struct platform_device * pdev)
- Line: 76
- Calls: gpio_generic_chip_init

## Structs (1)

### airoha_gpio_ctrl
- Line: 23
- Members:
  - gen_gc: gpio_generic_chip
  - data: void __iomem *
  - dir: void __iomem * [2]
  - output: void __iomem *

## Variables (2)

- static **airoha_gpio_driver** : platform_driver (line 126)
- static **airoha_gpio_of_match** : const struct of_device_id[] (line 120)

## Macros (1)

- **AIROHA_GPIO_MAX** (line 13)
