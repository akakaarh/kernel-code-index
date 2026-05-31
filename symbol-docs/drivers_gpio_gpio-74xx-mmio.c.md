# drivers/gpio/gpio-74xx-mmio.c

Subsystem: drivers/gpio

## Functions (4)

### mmio_74xx_dir_in
- Return type: static int
- Signature: mmio_74xx_dir_in(struct gpio_chip * gc,unsigned int gpio)
- Line: 89
- Calls: gpiochip_get_data

### mmio_74xx_dir_out
- Return type: static int
- Signature: mmio_74xx_dir_out(struct gpio_chip * gc,unsigned int gpio,int val)
- Line: 99
- Calls: gpiochip_get_data

### mmio_74xx_get_direction
- Return type: static int
- Signature: mmio_74xx_get_direction(struct gpio_chip * gc,unsigned offset)
- Line: 79
- Calls: gpiochip_get_data

### mmio_74xx_gpio_probe
- Return type: static int
- Signature: mmio_74xx_gpio_probe(struct platform_device * pdev)
- Line: 109
- Calls: gpio_generic_chip_init

## Structs (1)

### mmio_74xx_gpio_priv
- Line: 21
- Members:
  - gen_gc: gpio_generic_chip
  - flags: unsigned int

## Variables (2)

- static **mmio_74xx_gpio_driver** : platform_driver (line 143)
- static **mmio_74xx_gpio_ids** : const struct of_device_id[] (line 26)

## Macros (3)

- **MMIO_74XX_BIT_CNT**(x) (line 19)
- **MMIO_74XX_DIR_IN** (line 17)
- **MMIO_74XX_DIR_OUT** (line 18)
