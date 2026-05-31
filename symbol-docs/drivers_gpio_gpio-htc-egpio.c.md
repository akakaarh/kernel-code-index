# drivers/gpio/gpio-htc-egpio.c

Subsystem: drivers/gpio

## Functions (19)

### ack_irqs
- Return type: static void
- Signature: ack_irqs(struct egpio_info * ei)
- Line: 67
- Calls: egpio_writew
- Called by: egpio_handler, egpio_probe

### egpio_ack
- Return type: static void
- Signature: egpio_ack(struct irq_data * data)
- Line: 74

### egpio_bit
- Return type: static int
- Signature: egpio_bit(struct egpio_info * ei,int bit)
- Line: 126
- Called by: egpio_get

### egpio_direction_input
- Return type: static int
- Signature: egpio_direction_input(struct gpio_chip * chip,unsigned offset)
- Line: 160
- Calls: gpiochip_get_data

### egpio_direction_output
- Return type: static int
- Signature: egpio_direction_output(struct gpio_chip * chip,unsigned offset,int value)
- Line: 205
- Calls: egpio_set, gpiochip_get_data

### egpio_get
- Return type: static int
- Signature: egpio_get(struct gpio_chip * chip,unsigned offset)
- Line: 135
- Calls: egpio_bit, egpio_pos, egpio_readw, gpiochip_get_data

### egpio_get_direction
- Return type: static int
- Signature: egpio_get_direction(struct gpio_chip * chip,unsigned offset)
- Line: 217
- Calls: gpiochip_get_data

### egpio_handler
- Return type: static void
- Signature: egpio_handler(struct irq_desc * desc)
- Line: 102
- Calls: ack_irqs, egpio_readw

### egpio_init
- Return type: static int __init
- Signature: egpio_init(void)
- Line: 394

### egpio_mask
- Return type: static void
- Signature: egpio_mask(struct irq_data * data)
- Line: 81

### egpio_pos
- Return type: static int
- Signature: egpio_pos(struct egpio_info * ei,int bit)
- Line: 121
- Called by: egpio_get, egpio_set, egpio_write_cache

### egpio_probe
- Return type: static int __init
- Signature: egpio_probe(struct platform_device * pdev)
- Line: 263
- Calls: ack_irqs, egpio_write_cache

### egpio_readw
- Return type: static u16
- Signature: egpio_readw(struct egpio_info * ei,int reg)
- Line: 58
- Called by: egpio_get, egpio_handler, egpio_write_cache

### egpio_resume
- Return type: static int
- Signature: egpio_resume(struct device * dev)
- Line: 371
- Calls: egpio_write_cache

### egpio_set
- Return type: static int
- Signature: egpio_set(struct gpio_chip * chip,unsigned int offset,int value)
- Line: 173
- Calls: egpio_pos, egpio_writew, gpiochip_get_data
- Called by: egpio_direction_output

### egpio_suspend
- Return type: static int
- Signature: egpio_suspend(struct device * dev)
- Line: 362

### egpio_unmask
- Return type: static void
- Signature: egpio_unmask(struct irq_data * data)
- Line: 88

### egpio_write_cache
- Return type: static void
- Signature: egpio_write_cache(struct egpio_info * ei)
- Line: 229
- Calls: egpio_pos, egpio_readw, egpio_writew
- Called by: egpio_probe, egpio_resume

### egpio_writew
- Return type: static void
- Signature: egpio_writew(u16 value,struct egpio_info * ei,int reg)
- Line: 53
- Called by: ack_irqs, egpio_set, egpio_write_cache

## Structs (2)

### egpio_chip
- Line: 23
- Members:
  - reg_start: int
  - cached_values: int
  - is_out: unsigned long
  - dev: device *
  - chip: gpio_chip
  - lock: spinlock_t
  - base_addr: void __iomem *
  - bus_shift: int
  - reg_shift: int
  - reg_mask: int
  - ack_register: int
  - ack_write: int
  - irqs_enabled: u16
  - irq_start: uint
  - nirqs: int
  - chained_irq: uint
  - nchips: int

### egpio_info
- Line: 31
- Members:
  - reg_start: int
  - cached_values: int
  - is_out: unsigned long
  - dev: device *
  - chip: gpio_chip
  - lock: spinlock_t
  - base_addr: void __iomem *
  - bus_shift: int
  - reg_shift: int
  - reg_mask: int
  - ack_register: int
  - ack_write: int
  - irqs_enabled: u16
  - irq_start: uint
  - nirqs: int
  - chained_irq: uint
  - nchips: int

## Variables (2)

- static **egpio_driver** : platform_driver (line 386)
- static **egpio_muxed_chip** : irq_chip (line 95)
