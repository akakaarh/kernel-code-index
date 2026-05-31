# drivers/gpio/gpio-tangier.c

Subsystem: drivers/gpio

## Functions (21)

### devm_tng_gpio_probe
- Return type: int
- Signature: devm_tng_gpio_probe(struct device * dev,struct tng_gpio * gpio)
- Line: 415
- Called by: ehl_gpio_probe, mrfld_gpio_probe

### gpio_reg
- Return type: static void __iomem *
- Signature: gpio_reg(struct gpio_chip * chip,unsigned int offset,unsigned int reg)
- Line: 63
- Calls: gpiochip_get_data
- Called by: tng_gpio_resume, tng_gpio_suspend, tng_irq_handler, tng_irq_init_hw, tng_irq_set_type, tng_irq_set_wake

### gpio_reg_and_bit
- Return type: static void __iomem *
- Signature: gpio_reg_and_bit(struct gpio_chip * chip,unsigned int offset,unsigned int reg,u8 * bit)
- Line: 72
- Calls: gpiochip_get_data
- Called by: tng_gpio_direction_input, tng_gpio_direction_output, tng_gpio_get, tng_gpio_get_direction, tng_gpio_set, tng_gpio_set_debounce, tng_irq_ack, tng_irq_unmask_mask

### tng_gpio_add_pin_ranges
- Return type: static int
- Signature: tng_gpio_add_pin_ranges(struct gpio_chip * chip)
- Line: 392
- Calls: gpiochip_get_data

### tng_gpio_direction_input
- Return type: static int
- Signature: tng_gpio_direction_input(struct gpio_chip * chip,unsigned int offset)
- Line: 108
- Calls: gpio_reg_and_bit, gpiochip_get_data

### tng_gpio_direction_output
- Return type: static int
- Signature: tng_gpio_direction_output(struct gpio_chip * chip,unsigned int offset,int value)
- Line: 126
- Calls: gpio_reg_and_bit, gpiochip_get_data, tng_gpio_set

### tng_gpio_get
- Return type: static int
- Signature: tng_gpio_get(struct gpio_chip * chip,unsigned int offset)
- Line: 83
- Calls: gpio_reg_and_bit

### tng_gpio_get_direction
- Return type: static int
- Signature: tng_gpio_get_direction(struct gpio_chip * chip,unsigned int offset)
- Line: 145
- Calls: gpio_reg_and_bit

### tng_gpio_resume
- Return type: static int
- Signature: tng_gpio_resume(struct device * dev)
- Line: 489
- Calls: gpio_reg

### tng_gpio_set
- Return type: static int
- Signature: tng_gpio_set(struct gpio_chip * chip,unsigned int offset,int value)
- Line: 93
- Calls: gpio_reg_and_bit, gpiochip_get_data
- Called by: tng_gpio_direction_output

### tng_gpio_set_config
- Return type: static int
- Signature: tng_gpio_set_config(struct gpio_chip * chip,unsigned int offset,unsigned long config)
- Line: 180
- Calls: gpiochip_generic_config, tng_gpio_set_debounce

### tng_gpio_set_debounce
- Return type: static int
- Signature: tng_gpio_set_debounce(struct gpio_chip * chip,unsigned int offset,unsigned int debounce)
- Line: 158
- Calls: gpio_reg_and_bit, gpiochip_get_data
- Called by: tng_gpio_set_config

### tng_gpio_suspend
- Return type: static int
- Signature: tng_gpio_suspend(struct device * dev)
- Line: 466
- Calls: gpio_reg

### tng_irq_ack
- Return type: static void
- Signature: tng_irq_ack(struct irq_data * d)
- Line: 198
- Calls: gpio_reg_and_bit, gpiochip_get_data

### tng_irq_handler
- Return type: static void
- Signature: tng_irq_handler(struct irq_desc * desc)
- Line: 345
- Calls: gpio_reg, gpiochip_get_data

### tng_irq_init_hw
- Return type: static int
- Signature: tng_irq_init_hw(struct gpio_chip * chip)
- Line: 373
- Calls: gpio_reg, gpiochip_get_data

### tng_irq_mask
- Return type: static void
- Signature: tng_irq_mask(struct irq_data * d)
- Line: 231
- Calls: gpiochip_disable_irq, gpiochip_get_data, tng_irq_unmask_mask

### tng_irq_set_type
- Return type: static int
- Signature: tng_irq_set_type(struct irq_data * d,unsigned int type)
- Line: 251
- Calls: gpio_reg, gpiochip_get_data

### tng_irq_set_wake
- Return type: static int
- Signature: tng_irq_set_wake(struct irq_data * d,unsigned int on)
- Line: 307
- Calls: gpio_reg, gpiochip_get_data

### tng_irq_unmask
- Return type: static void
- Signature: tng_irq_unmask(struct irq_data * d)
- Line: 241
- Calls: gpiochip_enable_irq, gpiochip_get_data, tng_irq_unmask_mask

### tng_irq_unmask_mask
- Return type: static void
- Signature: tng_irq_unmask_mask(struct tng_gpio * priv,u32 gpio,bool unmask)
- Line: 213
- Calls: gpio_reg_and_bit
- Called by: tng_irq_mask, tng_irq_unmask

## Structs (1)

### tng_gpio_context
- Line: 54
- Members:
  - level: u32
  - gpdr: u32
  - grer: u32
  - gfer: u32
  - gimr: u32
  - gwmr: u32

## Variables (1)

- static **tng_irqchip** : const struct irq_chip (line 334)

## Macros (12)

- **GCCR** (line 32)
- **GFBR** (line 39)
- **GFER** (line 38)
- **GIMR** (line 40)
- **GISR** (line 41)
- **GITR** (line 42)
- **GLPR** (line 43)
- **GPCR** (line 36)
- **GPDR** (line 34)
- **GPLR** (line 33)
- **GPSR** (line 35)
- **GRER** (line 37)
