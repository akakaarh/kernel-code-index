# drivers/gpio/gpio-regmap.c

Subsystem: drivers/gpio

## Functions (14)

### devm_gpio_regmap_register
- Return type: gpio_regmap *
- Signature: devm_gpio_regmap_register(struct device * dev,const struct gpio_regmap_config * config)
- Line: 399
- Calls: gpio_regmap_register
- Called by: devm_i8255_regmap_register, devm_idio_16_regmap_register, ds4520_gpio_probe, fxl6408_probe, idi_48_probe, idio_24_probe, max7360_gpio_probe, qixis_cpld_gpio_probe, sl28cpld_gpio_probe, tn48m_gpio_probe, ws16c48_probe

### devm_gpio_regmap_unregister
- Return type: static void
- Signature: devm_gpio_regmap_unregister(void * res)
- Line: 383
- Calls: gpio_regmap_unregister

### gpio_regmap_addr
- Return type: static unsigned int
- Signature: gpio_regmap_addr(unsigned int addr)
- Line: 48
- Called by: gpio_regmap_get, gpio_regmap_get_direction, gpio_regmap_set, gpio_regmap_set_direction, gpio_regmap_set_with_clear

### gpio_regmap_direction_input
- Return type: static int
- Signature: gpio_regmap_direction_input(struct gpio_chip * chip,unsigned int offset)
- Line: 213
- Calls: gpio_regmap_set_direction

### gpio_regmap_direction_output
- Return type: static int
- Signature: gpio_regmap_direction_output(struct gpio_chip * chip,unsigned int offset,int value)
- Line: 219
- Calls: gpio_regmap_set, gpio_regmap_set_direction

### gpio_regmap_get
- Return type: static int
- Signature: gpio_regmap_get(struct gpio_chip * chip,unsigned int offset)
- Line: 69
- Calls: gpio_regmap_addr, gpiochip_get_data

### gpio_regmap_get_direction
- Return type: static int
- Signature: gpio_regmap_get_direction(struct gpio_chip * chip,unsigned int offset)
- Line: 141
- Calls: gpio_regmap_addr, gpiochip_get_data

### gpio_regmap_get_drvdata
- Return type: void *
- Signature: gpio_regmap_get_drvdata(struct gpio_regmap * gpio)
- Line: 227
- Called by: idio_24_reg_mask_xlate

### gpio_regmap_register
- Return type: gpio_regmap *
- Signature: gpio_regmap_register(const struct gpio_regmap_config * config)
- Line: 239
- Calls: gpiochip_get_ngpios, gpiochip_irqchip_add_domain, gpiochip_remove
- Called by: devm_gpio_regmap_register

### gpio_regmap_set
- Return type: static int
- Signature: gpio_regmap_set(struct gpio_chip * chip,unsigned int offset,int val)
- Line: 96
- Calls: gpio_regmap_addr, gpiochip_get_data
- Called by: gpio_regmap_direction_output

### gpio_regmap_set_direction
- Return type: static int
- Signature: gpio_regmap_set_direction(struct gpio_chip * chip,unsigned int offset,bool output)
- Line: 184
- Calls: gpio_regmap_addr, gpiochip_get_data
- Called by: gpio_regmap_direction_input, gpio_regmap_direction_output

### gpio_regmap_set_with_clear
- Return type: static int
- Signature: gpio_regmap_set_with_clear(struct gpio_chip * chip,unsigned int offset,int val)
- Line: 122
- Calls: gpio_regmap_addr, gpiochip_get_data

### gpio_regmap_simple_xlate
- Return type: static int
- Signature: gpio_regmap_simple_xlate(struct gpio_regmap * gpio,unsigned int base,unsigned int offset,unsigned int * reg,unsigned int * mask)
- Line: 56

### gpio_regmap_unregister
- Return type: void
- Signature: gpio_regmap_unregister(struct gpio_regmap * gpio)
- Line: 370
- Calls: gpiochip_remove
- Called by: devm_gpio_regmap_unregister

## Structs (1)

### gpio_regmap
- Line: 22
- Members:
  - parent: device *
  - regmap: regmap *
  - gpio_chip: gpio_chip
  - reg_stride: int
  - ngpio_per_reg: int
  - reg_dat_base: unsigned int
  - reg_set_base: unsigned int
  - reg_clr_base: unsigned int
  - reg_dir_in_base: unsigned int
  - reg_dir_out_base: unsigned int
  - fixed_direction_output: unsigned long *
  - regmap_irq_line: int
  - irq_chip_data: regmap_irq_chip_data *
  - reg_mask_xlate: int (*)(struct gpio_regmap * gpio,unsigned int base,unsigned int offset,unsigned int * reg,unsigned int * mask)
  - driver_data: void *
