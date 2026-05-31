# drivers/gpio/gpio-tqmx86.c

Subsystem: drivers/gpio

## Functions (19)

### _tqmx86_gpio_set
- Return type: static void
- Signature: _tqmx86_gpio_set(struct tqmx86_gpio_data * gpio,unsigned int offset,int value)
- Line: 88
- Calls: tqmx86_gpio_write
- Called by: tqmx86_gpio_direction_output, tqmx86_gpio_set

### tqmx86_gpio_clrsetbits
- Return type: static void
- Signature: tqmx86_gpio_clrsetbits(struct tqmx86_gpio_data * gpio,u8 clr,u8 set,unsigned int reg)
- Line: 69
- Calls: tqmx86_gpio_read, tqmx86_gpio_write
- Called by: tqmx86_gpio_direction_input, tqmx86_gpio_direction_output, tqmx86_gpio_irq_config

### tqmx86_gpio_direction_input
- Return type: static int
- Signature: tqmx86_gpio_direction_input(struct gpio_chip * chip,unsigned int offset)
- Line: 108
- Calls: gpiochip_get_data, tqmx86_gpio_clrsetbits

### tqmx86_gpio_direction_output
- Return type: static int
- Signature: tqmx86_gpio_direction_output(struct gpio_chip * chip,unsigned int offset,int value)
- Line: 120
- Calls: _tqmx86_gpio_set, gpiochip_get_data, tqmx86_gpio_clrsetbits

### tqmx86_gpio_get
- Return type: static int
- Signature: tqmx86_gpio_get(struct gpio_chip * chip,unsigned int offset)
- Line: 81
- Calls: gpiochip_get_data, tqmx86_gpio_read
- Called by: tqmx86_gpio_irq_config

### tqmx86_gpio_get_direction
- Return type: static int
- Signature: tqmx86_gpio_get_direction(struct gpio_chip * chip,unsigned int offset)
- Line: 134
- Calls: gpiochip_get_data, tqmx86_gpio_read

### tqmx86_gpio_irq_config
- Return type: static void
- Signature: tqmx86_gpio_irq_config(struct tqmx86_gpio_data * gpio,int hwirq)
- Line: 148
- Calls: tqmx86_gpio_clrsetbits, tqmx86_gpio_get
- Called by: tqmx86_gpio_irq_handler, tqmx86_gpio_irq_mask, tqmx86_gpio_irq_set_type, tqmx86_gpio_irq_unmask

### tqmx86_gpio_irq_handler
- Return type: static void
- Signature: tqmx86_gpio_irq_handler(struct irq_desc * desc)
- Line: 225
- Calls: gpiochip_get_data, tqmx86_gpio_irq_config, tqmx86_gpio_read, tqmx86_gpio_write

### tqmx86_gpio_irq_mask
- Return type: static void
- Signature: tqmx86_gpio_irq_mask(struct irq_data * data)
- Line: 169
- Calls: gpiochip_disable_irq, gpiochip_get_data, tqmx86_gpio_irq_config

### tqmx86_gpio_irq_print_chip
- Return type: static void
- Signature: tqmx86_gpio_irq_print_chip(struct irq_data * d,struct seq_file * p)
- Line: 307

### tqmx86_gpio_irq_set_type
- Return type: static int
- Signature: tqmx86_gpio_irq_set_type(struct irq_data * data,unsigned int type)
- Line: 195
- Calls: gpiochip_get_data, tqmx86_gpio_irq_config

### tqmx86_gpio_irq_unmask
- Return type: static void
- Signature: tqmx86_gpio_irq_unmask(struct irq_data * data)
- Line: 182
- Calls: gpiochip_enable_irq, gpiochip_get_data, tqmx86_gpio_irq_config

### tqmx86_gpio_probe
- Return type: static int
- Signature: tqmx86_gpio_probe(struct platform_device * pdev)
- Line: 323
- Calls: tqmx86_gpio_read, tqmx86_gpio_write

### tqmx86_gpio_read
- Return type: static u8
- Signature: tqmx86_gpio_read(struct tqmx86_gpio_data * gd,unsigned int reg)
- Line: 58
- Called by: tqmx86_gpio_clrsetbits, tqmx86_gpio_get, tqmx86_gpio_get_direction, tqmx86_gpio_irq_handler, tqmx86_gpio_probe

### tqmx86_gpio_runtime_resume
- Return type: static int
- Signature: tqmx86_gpio_runtime_resume(struct device * dev)
- Line: 287

### tqmx86_gpio_runtime_suspend
- Return type: static int
- Signature: tqmx86_gpio_runtime_suspend(struct device * dev)
- Line: 282

### tqmx86_gpio_set
- Return type: static int
- Signature: tqmx86_gpio_set(struct gpio_chip * chip,unsigned int offset,int value)
- Line: 96
- Calls: _tqmx86_gpio_set, gpiochip_get_data

### tqmx86_gpio_write
- Return type: static void
- Signature: tqmx86_gpio_write(struct tqmx86_gpio_data * gd,u8 val,unsigned int reg)
- Line: 63
- Called by: _tqmx86_gpio_set, tqmx86_gpio_clrsetbits, tqmx86_gpio_irq_handler, tqmx86_gpio_probe

### tqmx86_init_irq_valid_mask
- Return type: static void
- Signature: tqmx86_init_irq_valid_mask(struct gpio_chip * chip,unsigned long * valid_mask,unsigned int ngpios)
- Line: 296

## Structs (1)

### tqmx86_gpio_data
- Line: 48
- Members:
  - chip: gpio_chip
  - io_base: void __iomem *
  - irq: int
  - spinlock: raw_spinlock_t
  - irq_type: u8[]

## Variables (3)

- static **tqmx86_gpio_dev_pm_ops** : const struct dev_pm_ops (line 292)
- static **tqmx86_gpio_driver** : platform_driver (line 424)
- static **tqmx86_gpio_irq_chip** : const struct irq_chip (line 314)

## Macros (16)

- **TQMX86_DIR_INPUT_MASK** (line 25)
- **TQMX86_GPIIC** (line 29)
- **TQMX86_GPIIC_CONFIG**(i,v) (line 45)
- **TQMX86_GPIIC_MASK**(i) (line 46)
- **TQMX86_GPIIS** (line 30)
- **TQMX86_GPIOD** (line 28)
- **TQMX86_GPIODD** (line 27)
- **TQMX86_INT_TRIG_BOTH** (line 40)
- **TQMX86_INT_TRIG_FALLING** (line 38)
- **TQMX86_INT_TRIG_MASK** (line 41)
- **TQMX86_INT_TRIG_NONE** (line 37)
- **TQMX86_INT_TRIG_RISING** (line 39)
- **TQMX86_INT_UNMASKED** (line 43)
- **TQMX86_NGPI** (line 24)
- **TQMX86_NGPIO** (line 22)
- **TQMX86_NGPO** (line 23)
