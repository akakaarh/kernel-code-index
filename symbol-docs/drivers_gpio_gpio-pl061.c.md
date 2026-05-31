# drivers/gpio/gpio-pl061.c

Subsystem: drivers/gpio

## Functions (15)

### pl061_direction_input
- Return type: static int
- Signature: pl061_direction_input(struct gpio_chip * gc,unsigned offset)
- Line: 69
- Calls: gpiochip_get_data
- Called by: pl061_resume

### pl061_direction_output
- Return type: static int
- Signature: pl061_direction_output(struct gpio_chip * gc,unsigned offset,int value)
- Line: 84
- Calls: gpiochip_get_data
- Called by: pl061_resume

### pl061_get_direction
- Return type: static int
- Signature: pl061_get_direction(struct gpio_chip * gc,unsigned offset)
- Line: 59
- Calls: gpiochip_get_data

### pl061_get_value
- Return type: static int
- Signature: pl061_get_value(struct gpio_chip * gc,unsigned offset)
- Line: 107
- Calls: gpiochip_get_data
- Called by: pl061_suspend

### pl061_irq_ack
- Return type: static void
- Signature: pl061_irq_ack(struct irq_data * d)
- Line: 269
- Calls: gpiochip_get_data

### pl061_irq_handler
- Return type: static void
- Signature: pl061_irq_handler(struct irq_desc * desc)
- Line: 211
- Calls: gpiochip_get_data

### pl061_irq_mask
- Return type: static void
- Signature: pl061_irq_mask(struct irq_data * d)
- Line: 231
- Calls: gpiochip_disable_irq, gpiochip_get_data

### pl061_irq_print_chip
- Return type: static void
- Signature: pl061_irq_print_chip(struct irq_data * data,struct seq_file * p)
- Line: 288

### pl061_irq_set_wake
- Return type: static int
- Signature: pl061_irq_set_wake(struct irq_data * d,unsigned int state)
- Line: 280
- Calls: gpiochip_get_data

### pl061_irq_type
- Return type: static int
- Signature: pl061_irq_type(struct irq_data * d,unsigned trigger)
- Line: 123
- Calls: gpiochip_get_data

### pl061_irq_unmask
- Return type: static void
- Signature: pl061_irq_unmask(struct irq_data * d)
- Line: 246
- Calls: gpiochip_enable_irq, gpiochip_get_data

### pl061_probe
- Return type: static int
- Signature: pl061_probe(struct amba_device * adev,const struct amba_id * id)
- Line: 306

### pl061_resume
- Return type: static int
- Signature: pl061_resume(struct device * dev)
- Line: 387
- Calls: pl061_direction_input, pl061_direction_output

### pl061_set_value
- Return type: static int
- Signature: pl061_set_value(struct gpio_chip * gc,unsigned int offset,int value)
- Line: 114
- Calls: gpiochip_get_data

### pl061_suspend
- Return type: static int
- Signature: pl061_suspend(struct device * dev)
- Line: 366
- Calls: pl061_get_value

## Structs (2)

### pl061
- Line: 49
- Members:
  - gpio_data: u8
  - gpio_dir: u8
  - gpio_is: u8
  - gpio_ibe: u8
  - gpio_iev: u8
  - gpio_ie: u8
  - lock: raw_spinlock_t
  - base: void __iomem *
  - gc: gpio_chip
  - parent_irq: int
  - csave_regs: pl061_context_save_regs

### pl061_context_save_regs
- Line: 40
- Members:
  - gpio_data: u8
  - gpio_dir: u8
  - gpio_is: u8
  - gpio_ibe: u8
  - gpio_iev: u8
  - gpio_ie: u8
  - lock: raw_spinlock_t
  - base: void __iomem *
  - gc: gpio_chip
  - parent_irq: int
  - csave_regs: pl061_context_save_regs

## Variables (3)

- static **pl061_gpio_driver** : amba_driver (line 420)
- static **pl061_ids** : const struct amba_id[] (line 411)
- static **pl061_irq_chip** : const struct irq_chip (line 295)

## Macros (9)

- **GPIODIR** (line 29)
- **GPIOIBE** (line 31)
- **GPIOIC** (line 36)
- **GPIOIE** (line 33)
- **GPIOIEV** (line 32)
- **GPIOIS** (line 30)
- **GPIOMIS** (line 35)
- **GPIORIS** (line 34)
- **PL061_GPIO_NR** (line 38)
