# drivers/gpio/gpio-adp5585.c

Subsystem: drivers/gpio

## Functions (23)

### adp5585_gpio_bank
- Return type: static int
- Signature: adp5585_gpio_bank(unsigned int off)
- Line: 69

### adp5585_gpio_bit
- Return type: static int
- Signature: adp5585_gpio_bit(unsigned int off)
- Line: 74

### adp5585_gpio_direction_input
- Return type: static int
- Signature: adp5585_gpio_direction_input(struct gpio_chip * chip,unsigned int off)
- Line: 100
- Calls: gpiochip_get_data

### adp5585_gpio_direction_output
- Return type: static int
- Signature: adp5585_gpio_direction_output(struct gpio_chip * chip,unsigned int off,int val)
- Line: 109
- Calls: gpiochip_get_data

### adp5585_gpio_free
- Return type: static void
- Signature: adp5585_gpio_free(struct gpio_chip * chip,unsigned int off)
- Line: 260

### adp5585_gpio_get_direction
- Return type: static int
- Signature: adp5585_gpio_get_direction(struct gpio_chip * chip,unsigned int off)
- Line: 89
- Calls: gpiochip_get_data

### adp5585_gpio_get_value
- Return type: static int
- Signature: adp5585_gpio_get_value(struct gpio_chip * chip,unsigned int off)
- Line: 126
- Calls: gpiochip_get_data

### adp5585_gpio_key_event
- Return type: static int
- Signature: adp5585_gpio_key_event(struct notifier_block * nb,unsigned long key,void * data)
- Line: 268

### adp5585_gpio_probe
- Return type: static int
- Signature: adp5585_gpio_probe(struct platform_device * pdev)
- Line: 403

### adp5585_gpio_request
- Return type: static int
- Signature: adp5585_gpio_request(struct gpio_chip * chip,unsigned int off)
- Line: 241
- Calls: gpiochip_get_data

### adp5585_gpio_set_bias
- Return type: static int
- Signature: adp5585_gpio_set_bias(struct adp5585_gpio_dev * adp5585_gpio,unsigned int off,unsigned int bias)
- Line: 164
- Called by: adp5585_gpio_set_config

### adp5585_gpio_set_config
- Return type: static int
- Signature: adp5585_gpio_set_config(struct gpio_chip * chip,unsigned int off,unsigned long config)
- Line: 207
- Calls: adp5585_gpio_set_bias, adp5585_gpio_set_debounce, adp5585_gpio_set_drive, gpiochip_get_data

### adp5585_gpio_set_debounce
- Return type: static int
- Signature: adp5585_gpio_set_debounce(struct adp5585_gpio_dev * adp5585_gpio,unsigned int off,unsigned int debounce)
- Line: 196
- Called by: adp5585_gpio_set_config

### adp5585_gpio_set_drive
- Return type: static int
- Signature: adp5585_gpio_set_drive(struct adp5585_gpio_dev * adp5585_gpio,unsigned int off,enum pin_config_param drive)
- Line: 185
- Called by: adp5585_gpio_set_config

### adp5585_gpio_set_value
- Return type: static int
- Signature: adp5585_gpio_set_value(struct gpio_chip * chip,unsigned int off,int val)
- Line: 153
- Calls: gpiochip_get_data

### adp5585_gpio_unreg_notifier
- Return type: static void
- Signature: adp5585_gpio_unreg_notifier(void * data)
- Line: 393

### adp5585_irq_bus_lock
- Return type: static void
- Signature: adp5585_irq_bus_lock(struct irq_data * d)
- Line: 311
- Calls: gpiochip_get_data

### adp5585_irq_bus_sync_unlock
- Return type: static void
- Signature: adp5585_irq_bus_sync_unlock(struct irq_data * d)
- Line: 319
- Calls: gpiochip_get_data

### adp5585_irq_mask
- Return type: static void
- Signature: adp5585_irq_mask(struct irq_data * d)
- Line: 346
- Calls: gpiochip_disable_irq, gpiochip_get_data

### adp5585_irq_set_type
- Return type: static int
- Signature: adp5585_irq_set_type(struct irq_data * d,unsigned int type)
- Line: 366
- Calls: gpiochip_get_data

### adp5585_irq_unmask
- Return type: static void
- Signature: adp5585_irq_unmask(struct irq_data * d)
- Line: 356
- Calls: gpiochip_enable_irq, gpiochip_get_data

### adp5589_gpio_bank
- Return type: static int
- Signature: adp5589_gpio_bank(unsigned int off)
- Line: 79

### adp5589_gpio_bit
- Return type: static int
- Signature: adp5589_gpio_bit(unsigned int off)
- Line: 84

## Structs (2)

### adp5585_gpio_chip
- Line: 41
- Members:
  - bank: int (*)(unsigned int off)
  - bit: int (*)(unsigned int off)
  - debounce_dis_a: unsigned int
  - rpull_cfg_a: unsigned int
  - gpo_data_a: unsigned int
  - gpo_out_a: unsigned int
  - gpio_dir_a: unsigned int
  - gpi_stat_a: unsigned int
  - gpi_int_lvl_a: unsigned int
  - gpi_ev_a: unsigned int
  - gpi_ev_min: unsigned int
  - gpi_ev_max: unsigned int
  - has_bias_hole: bool
  - gpio_chip: gpio_chip
  - nb: notifier_block
  - info: const struct adp5585_gpio_chip *
  - regmap: regmap *
  - irq_mask: unsigned long
  - irq_en: unsigned long
  - irq_active_high: unsigned long
  - bus_lock: mutex

### adp5585_gpio_dev
- Line: 57
- Members:
  - bank: int (*)(unsigned int off)
  - bit: int (*)(unsigned int off)
  - debounce_dis_a: unsigned int
  - rpull_cfg_a: unsigned int
  - gpo_data_a: unsigned int
  - gpo_out_a: unsigned int
  - gpio_dir_a: unsigned int
  - gpi_stat_a: unsigned int
  - gpi_int_lvl_a: unsigned int
  - gpi_ev_a: unsigned int
  - gpi_ev_min: unsigned int
  - gpi_ev_max: unsigned int
  - has_bias_hole: bool
  - gpio_chip: gpio_chip
  - nb: notifier_block
  - info: const struct adp5585_gpio_chip *
  - regmap: regmap *
  - irq_mask: unsigned long
  - irq_en: unsigned long
  - irq_active_high: unsigned long
  - bus_lock: mutex

## Variables (5)

- static **adp5585_gpio_chip_info** : const struct adp5585_gpio_chip (line 478)
- static **adp5585_gpio_driver** : platform_driver (line 516)
- static **adp5585_gpio_id_table** : const struct platform_device_id[] (line 509)
- static **adp5585_irq_chip** : const struct irq_chip (line 382)
- static **adp5589_gpio_chip_info** : const struct adp5585_gpio_chip (line 494)

## Macros (4)

- **ADP5585_BANK**(n) (line 30)
- **ADP5585_BIT**(n) (line 31)
- **ADP5589_BANK**(n) (line 38)
- **ADP5589_BIT**(n) (line 39)
