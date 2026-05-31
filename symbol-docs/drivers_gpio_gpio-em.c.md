# drivers/gpio/gpio-em.c

Subsystem: drivers/gpio

## Functions (21)

### __em_gio_set
- Return type: static void
- Signature: __em_gio_set(struct gpio_chip * chip,unsigned int reg,unsigned shift,int value)
- Line: 199
- Calls: em_gio_write, gpio_to_priv
- Called by: em_gio_set

### em_gio_direction_input
- Return type: static int
- Signature: em_gio_direction_input(struct gpio_chip * chip,unsigned offset)
- Line: 188
- Calls: em_gio_write, gpio_to_priv
- Called by: em_gio_free

### em_gio_direction_output
- Return type: static int
- Signature: em_gio_direction_output(struct gpio_chip * chip,unsigned offset,int value)
- Line: 218
- Calls: em_gio_set, em_gio_write, gpio_to_priv

### em_gio_exit
- Return type: static void __exit
- Signature: em_gio_exit(void)
- Line: 379

### em_gio_free
- Return type: static void
- Signature: em_gio_free(struct gpio_chip * chip,unsigned offset)
- Line: 232
- Calls: em_gio_direction_input

### em_gio_get
- Return type: static int
- Signature: em_gio_get(struct gpio_chip * chip,unsigned offset)
- Line: 194
- Calls: em_gio_read, gpio_to_priv

### em_gio_init
- Return type: static int __init
- Signature: em_gio_init(void)
- Line: 373

### em_gio_irq_disable
- Return type: static void
- Signature: em_gio_irq_disable(struct irq_data * d)
- Line: 75
- Calls: em_gio_write

### em_gio_irq_domain_map
- Return type: static int
- Signature: em_gio_irq_domain_map(struct irq_domain * h,unsigned int irq,irq_hw_number_t hwirq)
- Line: 242

### em_gio_irq_domain_remove
- Return type: static void
- Signature: em_gio_irq_domain_remove(void * data)
- Line: 259

### em_gio_irq_enable
- Return type: static void
- Signature: em_gio_irq_enable(struct irq_data * d)
- Line: 82
- Calls: em_gio_write

### em_gio_irq_handler
- Return type: static irqreturn_t
- Signature: em_gio_irq_handler(int irq,void * dev_id)
- Line: 167
- Calls: em_gio_read, em_gio_write

### em_gio_irq_relres
- Return type: static void
- Signature: em_gio_irq_relres(struct irq_data * d)
- Line: 104
- Calls: gpiochip_unlock_as_irq

### em_gio_irq_reqres
- Return type: static int
- Signature: em_gio_irq_reqres(struct irq_data * d)
- Line: 89
- Calls: gpiochip_lock_as_irq

### em_gio_irq_set_type
- Return type: static int
- Signature: em_gio_irq_set_type(struct irq_data * d,unsigned int type)
- Line: 122
- Calls: em_gio_read, em_gio_write

### em_gio_probe
- Return type: static int
- Signature: em_gio_probe(struct platform_device * pdev)
- Line: 266

### em_gio_read
- Return type: static unsigned long
- Signature: em_gio_read(struct em_gio_priv * p,int offs)
- Line: 58
- Called by: em_gio_get, em_gio_irq_handler, em_gio_irq_set_type

### em_gio_set
- Return type: static int
- Signature: em_gio_set(struct gpio_chip * chip,unsigned int offset,int value)
- Line: 207
- Calls: __em_gio_set
- Called by: em_gio_direction_output

### em_gio_to_irq
- Return type: static int
- Signature: em_gio_to_irq(struct gpio_chip * chip,unsigned offset)
- Line: 227
- Calls: gpio_to_priv

### em_gio_write
- Return type: static void
- Signature: em_gio_write(struct em_gio_priv * p,int offs,unsigned long value)
- Line: 66
- Called by: __em_gio_set, em_gio_direction_input, em_gio_direction_output, em_gio_irq_disable, em_gio_irq_enable, em_gio_irq_handler, em_gio_irq_set_type

### gpio_to_priv
- Return type: static em_gio_priv *
- Signature: gpio_to_priv(struct gpio_chip * chip)
- Line: 183
- Calls: gpiochip_get_data
- Called by: __em_gio_set, em_gio_direction_input, em_gio_direction_output, em_gio_get, em_gio_to_irq

## Structs (1)

### em_gio_priv
- Line: 23
- Members:
  - base0: void __iomem *
  - base1: void __iomem *
  - sense_lock: spinlock_t
  - pdev: platform_device *
  - gpio_chip: gpio_chip
  - irq_chip: irq_chip
  - irq_domain: irq_domain *

## Variables (4)

- static **em_gio_device_driver** : platform_driver (line 365)
- static **em_gio_dt_ids** : const struct of_device_id[] (line 359)
- static **em_gio_irq_domain_ops** : const struct irq_domain_ops (line 254)
- static **em_gio_sense_table** : unsigned char[] (line 114)

## Macros (23)

- **GIO_ASYNC**(x) (line 112)
- **GIO_E0** (line 34)
- **GIO_E1** (line 33)
- **GIO_EM** (line 35)
- **GIO_I** (line 38)
- **GIO_IDS** (line 41)
- **GIO_IDT**(n) (line 56)
- **GIO_IDT0** (line 47)
- **GIO_IDT1** (line 48)
- **GIO_IDT2** (line 49)
- **GIO_IDT3** (line 50)
- **GIO_IEN** (line 40)
- **GIO_IIA** (line 39)
- **GIO_IIM** (line 42)
- **GIO_IIR** (line 45)
- **GIO_IRBH** (line 54)
- **GIO_IRBL** (line 53)
- **GIO_MST** (line 44)
- **GIO_OH** (line 37)
- **GIO_OL** (line 36)
- **GIO_RAW** (line 43)
- **GIO_RAWBH** (line 52)
- **GIO_RAWBL** (line 51)
