# drivers/gpio/gpio-reg.c

Subsystem: drivers/gpio

## Functions (9)

### gpio_reg_direction_input
- Return type: static int
- Signature: gpio_reg_direction_input(struct gpio_chip * gc,unsigned offset)
- Line: 53

### gpio_reg_direction_output
- Return type: static int
- Signature: gpio_reg_direction_output(struct gpio_chip * gc,unsigned offset,int value)
- Line: 41

### gpio_reg_get
- Return type: static int
- Signature: gpio_reg_get(struct gpio_chip * gc,unsigned offset)
- Line: 79

### gpio_reg_get_direction
- Return type: static int
- Signature: gpio_reg_get_direction(struct gpio_chip * gc,unsigned offset)
- Line: 33

### gpio_reg_init
- Return type: gpio_chip *
- Signature: gpio_reg_init(struct device * dev,void __iomem * reg,int base,int num,const char * label,u32 direction,u32 def_out,const char * const * names,struct irq_domain * irqdom,const int * irqs)
- Line: 143

### gpio_reg_resume
- Return type: int
- Signature: gpio_reg_resume(struct gpio_chip * gc)
- Line: 185

### gpio_reg_set
- Return type: static int
- Signature: gpio_reg_set(struct gpio_chip * gc,unsigned int offset,int value)
- Line: 60

### gpio_reg_set_multiple
- Return type: static int
- Signature: gpio_reg_set_multiple(struct gpio_chip * gc,unsigned long * mask,unsigned long * bits)
- Line: 97

### gpio_reg_to_irq
- Return type: static int
- Signature: gpio_reg_to_irq(struct gpio_chip * gc,unsigned offset)
- Line: 111

## Structs (1)

### gpio_reg
- Line: 21
- Members:
  - gc: gpio_chip
  - lock: spinlock_t
  - direction: u32
  - out: u32
  - reg: void __iomem *
  - irqdomain: irq_domain *
  - irqs: const int *

## Macros (1)

- **to_gpio_reg**(x) (line 31)
