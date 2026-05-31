# drivers/gpio/gpio-mpc5200.c

Subsystem: drivers/gpio

## Functions (14)

### __mpc52xx_simple_gpio_set
- Return type: static void
- Signature: __mpc52xx_simple_gpio_set(struct gpio_chip * gc,unsigned int gpio,int val)
- Line: 221
- Calls: gpiochip_get_data
- Called by: mpc52xx_simple_gpio_dir_out, mpc52xx_simple_gpio_set

### __mpc52xx_wkup_gpio_set
- Return type: static void
- Signature: __mpc52xx_wkup_gpio_set(struct gpio_chip * gc,unsigned int gpio,int val)
- Line: 59
- Calls: gpiochip_get_data
- Called by: mpc52xx_wkup_gpio_dir_out, mpc52xx_wkup_gpio_set

### mpc52xx_gpio_exit
- Return type: static void __exit
- Signature: mpc52xx_gpio_exit(void)
- Line: 367

### mpc52xx_gpio_init
- Return type: static int __init
- Signature: mpc52xx_gpio_init(void)
- Line: 359

### mpc52xx_simple_gpio_dir_in
- Return type: static int
- Signature: mpc52xx_simple_gpio_dir_in(struct gpio_chip * gc,unsigned int gpio)
- Line: 249
- Calls: gpiochip_get_data

### mpc52xx_simple_gpio_dir_out
- Return type: static int
- Signature: mpc52xx_simple_gpio_dir_out(struct gpio_chip * gc,unsigned int gpio,int val)
- Line: 271
- Calls: __mpc52xx_simple_gpio_set, gpiochip_get_data

### mpc52xx_simple_gpio_get
- Return type: static int
- Signature: mpc52xx_simple_gpio_get(struct gpio_chip * gc,unsigned int gpio)
- Line: 209
- Calls: gpiochip_get_data

### mpc52xx_simple_gpio_set
- Return type: static int
- Signature: mpc52xx_simple_gpio_set(struct gpio_chip * gc,unsigned int gpio,int val)
- Line: 234
- Calls: __mpc52xx_simple_gpio_set

### mpc52xx_simple_gpiochip_probe
- Return type: static int
- Signature: mpc52xx_simple_gpiochip_probe(struct platform_device * ofdev)
- Line: 297

### mpc52xx_wkup_gpio_dir_in
- Return type: static int
- Signature: mpc52xx_wkup_gpio_dir_in(struct gpio_chip * gc,unsigned int gpio)
- Line: 88
- Calls: gpiochip_get_data

### mpc52xx_wkup_gpio_dir_out
- Return type: static int
- Signature: mpc52xx_wkup_gpio_dir_out(struct gpio_chip * gc,unsigned int gpio,int val)
- Line: 110
- Calls: __mpc52xx_wkup_gpio_set, gpiochip_get_data

### mpc52xx_wkup_gpio_get
- Return type: static int
- Signature: mpc52xx_wkup_gpio_get(struct gpio_chip * gc,unsigned int gpio)
- Line: 45
- Calls: gpiochip_get_data

### mpc52xx_wkup_gpio_set
- Return type: static int
- Signature: mpc52xx_wkup_gpio_set(struct gpio_chip * gc,unsigned int gpio,int val)
- Line: 73
- Calls: __mpc52xx_wkup_gpio_set

### mpc52xx_wkup_gpiochip_probe
- Return type: static int
- Signature: mpc52xx_wkup_gpiochip_probe(struct platform_device * ofdev)
- Line: 135

## Structs (1)

### mpc52xx_gpiochip
- Line: 21
- Members:
  - gc: gpio_chip
  - regs: void __iomem *
  - shadow_dvo: unsigned int
  - shadow_gpioe: unsigned int
  - shadow_ddr: unsigned int

## Variables (5)

- static **drivers** : platform_driver * const[] (line 354)
- static **mpc52xx_simple_gpiochip_driver** : platform_driver (line 346)
- static **mpc52xx_simple_gpiochip_match** : const struct of_device_id[] (line 341)
- static **mpc52xx_wkup_gpiochip_driver** : platform_driver (line 184)
- static **mpc52xx_wkup_gpiochip_match** : const struct of_device_id[] (line 179)
