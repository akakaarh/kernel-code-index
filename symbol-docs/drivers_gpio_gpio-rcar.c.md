# drivers/gpio/gpio-rcar.c

Subsystem: drivers/gpio

## Functions (25)

### gpio_rcar_config_general_input_output_mode
- Return type: static void
- Signature: gpio_rcar_config_general_input_output_mode(struct gpio_chip * chip,unsigned int gpio,bool output)
- Line: 237
- Calls: gpio_rcar_modify_bit, gpiochip_get_data
- Called by: gpio_rcar_direction_input, gpio_rcar_direction_output, gpio_rcar_free

### gpio_rcar_config_interrupt_input_mode
- Return type: static void
- Signature: gpio_rcar_config_interrupt_input_mode(struct gpio_rcar_priv * p,unsigned int hwirq,bool active_high_rising_edge,bool level_trigger,bool both)
- Line: 113
- Calls: gpio_rcar_modify_bit, gpio_rcar_write
- Called by: gpio_rcar_irq_set_type, gpio_rcar_resume

### gpio_rcar_direction_input
- Return type: static int
- Signature: gpio_rcar_direction_input(struct gpio_chip * chip,unsigned offset)
- Line: 310
- Calls: gpio_rcar_config_general_input_output_mode
- Called by: gpio_rcar_resume

### gpio_rcar_direction_output
- Return type: static int
- Signature: gpio_rcar_direction_output(struct gpio_chip * chip,unsigned offset,int value)
- Line: 389
- Calls: gpio_rcar_config_general_input_output_mode, gpio_rcar_set
- Called by: gpio_rcar_resume

### gpio_rcar_enable_inputs
- Return type: static void
- Signature: gpio_rcar_enable_inputs(struct gpio_rcar_priv * p)
- Line: 479
- Calls: gpio_rcar_read, gpio_rcar_write, gpiochip_query_valid_mask
- Called by: gpio_rcar_probe, gpio_rcar_resume

### gpio_rcar_free
- Return type: static void
- Signature: gpio_rcar_free(struct gpio_chip * chip,unsigned offset)
- Line: 285
- Calls: gpio_rcar_config_general_input_output_mode, gpiochip_get_data

### gpio_rcar_get
- Return type: static int
- Signature: gpio_rcar_get(struct gpio_chip * chip,unsigned offset)
- Line: 316
- Calls: gpio_rcar_read, gpiochip_get_data

### gpio_rcar_get_direction
- Return type: static int
- Signature: gpio_rcar_get_direction(struct gpio_chip * chip,unsigned int offset)
- Line: 300
- Calls: gpio_rcar_read, gpiochip_get_data

### gpio_rcar_get_multiple
- Return type: static int
- Signature: gpio_rcar_get_multiple(struct gpio_chip * chip,unsigned long * mask,unsigned long * bits)
- Line: 331
- Calls: gpio_rcar_read, gpiochip_get_data

### gpio_rcar_irq_disable
- Return type: static void
- Signature: gpio_rcar_irq_disable(struct irq_data * d)
- Line: 93
- Calls: gpio_rcar_write, gpiochip_disable_irq, gpiochip_get_data

### gpio_rcar_irq_enable
- Return type: static void
- Signature: gpio_rcar_irq_enable(struct irq_data * d)
- Line: 103
- Calls: gpio_rcar_write, gpiochip_enable_irq, gpiochip_get_data

### gpio_rcar_irq_handler
- Return type: static irqreturn_t
- Signature: gpio_rcar_irq_handler(int irq,void * dev_id)
- Line: 219
- Calls: gpio_rcar_read, gpio_rcar_write

### gpio_rcar_irq_set_type
- Return type: static int
- Signature: gpio_rcar_irq_set_type(struct irq_data * d,unsigned int type)
- Line: 148
- Calls: gpio_rcar_config_interrupt_input_mode, gpiochip_get_data

### gpio_rcar_irq_set_wake
- Return type: static int
- Signature: gpio_rcar_irq_set_wake(struct irq_data * d,unsigned int on)
- Line: 185
- Calls: gpiochip_get_data

### gpio_rcar_modify_bit
- Return type: static void
- Signature: gpio_rcar_modify_bit(struct gpio_rcar_priv * p,int offs,int bit,bool value)
- Line: 80
- Calls: gpio_rcar_read, gpio_rcar_write
- Called by: gpio_rcar_config_general_input_output_mode, gpio_rcar_config_interrupt_input_mode, gpio_rcar_set

### gpio_rcar_parse_dt
- Return type: static int
- Signature: gpio_rcar_parse_dt(struct gpio_rcar_priv * p,unsigned int * npins)
- Line: 452
- Called by: gpio_rcar_probe

### gpio_rcar_probe
- Return type: static int
- Signature: gpio_rcar_probe(struct platform_device * pdev)
- Line: 493
- Calls: gpio_rcar_enable_inputs, gpio_rcar_parse_dt, gpiochip_remove

### gpio_rcar_read
- Return type: static u32
- Signature: gpio_rcar_read(struct gpio_rcar_priv * p,int offs)
- Line: 69
- Called by: gpio_rcar_enable_inputs, gpio_rcar_get, gpio_rcar_get_direction, gpio_rcar_get_multiple, gpio_rcar_irq_handler, gpio_rcar_modify_bit, gpio_rcar_set_multiple, gpio_rcar_suspend

### gpio_rcar_remove
- Return type: static void
- Signature: gpio_rcar_remove(struct platform_device * pdev)
- Line: 586
- Calls: gpiochip_remove

### gpio_rcar_request
- Return type: static int
- Signature: gpio_rcar_request(struct gpio_chip * chip,unsigned offset)
- Line: 267
- Calls: gpiochip_get_data

### gpio_rcar_resume
- Return type: static int
- Signature: gpio_rcar_resume(struct device * dev)
- Line: 614
- Calls: gpio_rcar_config_interrupt_input_mode, gpio_rcar_direction_input, gpio_rcar_direction_output, gpio_rcar_enable_inputs, gpio_rcar_write, gpiochip_line_is_valid

### gpio_rcar_set
- Return type: static int
- Signature: gpio_rcar_set(struct gpio_chip * chip,unsigned int offset,int value)
- Line: 359
- Calls: gpio_rcar_modify_bit, gpiochip_get_data
- Called by: gpio_rcar_direction_output

### gpio_rcar_set_multiple
- Return type: static int
- Signature: gpio_rcar_set_multiple(struct gpio_chip * chip,unsigned long * mask,unsigned long * bits)
- Line: 371
- Calls: gpio_rcar_read, gpio_rcar_write, gpiochip_get_data

### gpio_rcar_suspend
- Return type: static int
- Signature: gpio_rcar_suspend(struct device * dev)
- Line: 595
- Calls: gpio_rcar_read

### gpio_rcar_write
- Return type: static void
- Signature: gpio_rcar_write(struct gpio_rcar_priv * p,int offs,u32 value)
- Line: 74
- Called by: gpio_rcar_config_interrupt_input_mode, gpio_rcar_enable_inputs, gpio_rcar_irq_disable, gpio_rcar_irq_enable, gpio_rcar_irq_handler, gpio_rcar_modify_bit, gpio_rcar_resume, gpio_rcar_set_multiple

## Structs (3)

### gpio_rcar_bank_info
- Line: 24
- Members:
  - iointsel: u32
  - inoutsel: u32
  - outdt: u32
  - posneg: u32
  - edglevel: u32
  - bothedge: u32
  - intmsk: u32
  - has_outdtsel: bool
  - has_both_edge_trigger: bool
  - has_always_in: bool
  - has_inen: bool
  - base: void __iomem *
  - lock: raw_spinlock_t
  - dev: device *
  - gpio_chip: gpio_chip
  - irq_parent: unsigned int
  - wakeup_path: atomic_t
  - info: gpio_rcar_info
  - bank_info: gpio_rcar_bank_info

### gpio_rcar_info
- Line: 34
- Members:
  - iointsel: u32
  - inoutsel: u32
  - outdt: u32
  - posneg: u32
  - edglevel: u32
  - bothedge: u32
  - intmsk: u32
  - has_outdtsel: bool
  - has_both_edge_trigger: bool
  - has_always_in: bool
  - has_inen: bool
  - base: void __iomem *
  - lock: raw_spinlock_t
  - dev: device *
  - gpio_chip: gpio_chip
  - irq_parent: unsigned int
  - wakeup_path: atomic_t
  - info: gpio_rcar_info
  - bank_info: gpio_rcar_bank_info

### gpio_rcar_priv
- Line: 41
- Members:
  - iointsel: u32
  - inoutsel: u32
  - outdt: u32
  - posneg: u32
  - edglevel: u32
  - bothedge: u32
  - intmsk: u32
  - has_outdtsel: bool
  - has_both_edge_trigger: bool
  - has_always_in: bool
  - has_inen: bool
  - base: void __iomem *
  - lock: raw_spinlock_t
  - dev: device *
  - gpio_chip: gpio_chip
  - irq_parent: unsigned int
  - wakeup_path: atomic_t
  - info: gpio_rcar_info
  - bank_info: gpio_rcar_bank_info

## Variables (7)

- static **gpio_rcar_device_driver** : platform_driver (line 657)
- static **gpio_rcar_info_gen1** : const struct gpio_rcar_info (line 398)
- static **gpio_rcar_info_gen2** : const struct gpio_rcar_info (line 405)
- static **gpio_rcar_info_gen3** : const struct gpio_rcar_info (line 412)
- static **gpio_rcar_info_gen4** : const struct gpio_rcar_info (line 419)
- static **gpio_rcar_irq_chip** : const struct irq_chip (line 208)
- static **gpio_rcar_of_table** : const struct of_device_id[] (line 426)

## Macros (15)

- **BOTHEDGE** (line 64)
- **EDGLEVEL** (line 61)
- **FILONOFF** (line 62)
- **INDT** (line 55)
- **INEN** (line 65)
- **INOUTSEL** (line 53)
- **INTCLR** (line 57)
- **INTDT** (line 56)
- **INTMSK** (line 58)
- **IOINTSEL** (line 52)
- **MSKCLR** (line 59)
- **OUTDT** (line 54)
- **OUTDTSEL** (line 63)
- **POSNEG** (line 60)
- **RCAR_MAX_GPIO_PER_BANK** (line 67)
