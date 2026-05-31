# drivers/gpio/gpio-sa1100.c

Subsystem: drivers/gpio

## Functions (18)

### sa1100_direction_input
- Return type: static int
- Signature: sa1100_direction_input(struct gpio_chip * chip,unsigned offset)
- Line: 66

### sa1100_direction_output
- Return type: static int
- Signature: sa1100_direction_output(struct gpio_chip * chip,unsigned offset,int value)
- Line: 78
- Calls: sa1100_gpio_set

### sa1100_get_direction
- Return type: static int
- Signature: sa1100_get_direction(struct gpio_chip * chip,unsigned offset)
- Line: 56

### sa1100_gpio_ack
- Return type: static void
- Signature: sa1100_gpio_ack(struct irq_data * d)
- Line: 157

### sa1100_gpio_get
- Return type: static int
- Signature: sa1100_gpio_get(struct gpio_chip * chip,unsigned offset)
- Line: 40

### sa1100_gpio_handler
- Return type: static void
- Signature: sa1100_gpio_handler(struct irq_desc * desc)
- Line: 233

### sa1100_gpio_init_devicefs
- Return type: static int __init
- Signature: sa1100_gpio_init_devicefs(void)
- Line: 292

### sa1100_gpio_irqdomain_map
- Return type: static int
- Signature: sa1100_gpio_irqdomain_map(struct irq_domain * d,unsigned int irq,irq_hw_number_t hwirq)
- Line: 209

### sa1100_gpio_mask
- Return type: static void
- Signature: sa1100_gpio_mask(struct irq_data * d)
- Line: 164
- Calls: sa1100_update_edge_regs

### sa1100_gpio_resume
- Return type: static void
- Signature: sa1100_gpio_resume(void * data)
- Line: 278
- Calls: sa1100_update_edge_regs

### sa1100_gpio_set
- Return type: static int
- Signature: sa1100_gpio_set(struct gpio_chip * chip,unsigned int offset,int value)
- Line: 46
- Called by: sa1100_direction_output

### sa1100_gpio_suspend
- Return type: static int
- Signature: sa1100_gpio_suspend(void * data)
- Line: 259

### sa1100_gpio_type
- Return type: static int
- Signature: sa1100_gpio_type(struct irq_data * d,unsigned int type)
- Line: 129
- Calls: sa1100_update_edge_regs

### sa1100_gpio_unmask
- Return type: static void
- Signature: sa1100_gpio_unmask(struct irq_data * d)
- Line: 174
- Calls: sa1100_update_edge_regs

### sa1100_gpio_wake
- Return type: static int
- Signature: sa1100_gpio_wake(struct irq_data * d,unsigned int on)
- Line: 184

### sa1100_init_gpio
- Return type: void __init
- Signature: sa1100_init_gpio(void)
- Line: 317

### sa1100_to_irq
- Return type: static int
- Signature: sa1100_to_irq(struct gpio_chip * chip,unsigned offset)
- Line: 91

### sa1100_update_edge_regs
- Return type: static void
- Signature: sa1100_update_edge_regs(struct sa1100_gpio_chip * sgc)
- Line: 117
- Called by: sa1100_gpio_mask, sa1100_gpio_resume, sa1100_gpio_type, sa1100_gpio_unmask

## Structs (1)

### sa1100_gpio_chip
- Line: 17
- Members:
  - chip: gpio_chip
  - membase: void __iomem *
  - irqbase: int
  - irqmask: u32
  - irqrising: u32
  - irqfalling: u32
  - irqwake: u32

## Enums (1)

### __anon98334e3e0103
- Line: 29

## Variables (7)

- static **sa1100_gpio_chip** : sa1100_gpio_chip (line 96)
- static **sa1100_gpio_irq_chip** : irq_chip (line 200)
- static **sa1100_gpio_irqdomain** : irq_domain * (line 226)
- static **sa1100_gpio_irqdomain_ops** : const struct irq_domain_ops (line 221)
- static **sa1100_gpio_irqs** : const int[]__initconst (line 300)
- static **sa1100_gpio_syscore** : syscore (line 288)
- static **sa1100_gpio_syscore_ops** : const struct syscore_ops (line 283)

## Macros (1)

- **sa1100_gpio_chip**(x) (line 27)
