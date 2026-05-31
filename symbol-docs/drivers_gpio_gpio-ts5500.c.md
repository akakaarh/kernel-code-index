# drivers/gpio/gpio-ts5500.c

Subsystem: drivers/gpio

## Functions (11)

### ts5500_clear_mask
- Return type: static void
- Signature: ts5500_clear_mask(u8 mask,u8 addr)
- Line: 191
- Called by: ts5500_dio_probe, ts5500_disable_irq, ts5500_gpio_input, ts5500_gpio_output, ts5500_gpio_set

### ts5500_dio_probe
- Return type: static int
- Signature: ts5500_dio_probe(struct platform_device * pdev)
- Line: 316
- Calls: ts5500_clear_mask, ts5500_enable_irq

### ts5500_dio_remove
- Return type: static void
- Signature: ts5500_dio_remove(struct platform_device * pdev)
- Line: 417
- Calls: ts5500_disable_irq

### ts5500_disable_irq
- Return type: static void
- Signature: ts5500_disable_irq(struct ts5500_priv * priv)
- Line: 299
- Calls: ts5500_clear_mask
- Called by: ts5500_dio_remove

### ts5500_enable_irq
- Return type: static int
- Signature: ts5500_enable_irq(struct ts5500_priv * priv)
- Line: 280
- Calls: ts5500_set_mask
- Called by: ts5500_dio_probe

### ts5500_gpio_get
- Return type: static int
- Signature: ts5500_gpio_get(struct gpio_chip * chip,unsigned offset)
- Line: 217
- Calls: gpiochip_get_data

### ts5500_gpio_input
- Return type: static int
- Signature: ts5500_gpio_input(struct gpio_chip * chip,unsigned offset)
- Line: 198
- Calls: gpiochip_get_data, ts5500_clear_mask

### ts5500_gpio_output
- Return type: static int
- Signature: ts5500_gpio_output(struct gpio_chip * chip,unsigned offset,int val)
- Line: 225
- Calls: gpiochip_get_data, ts5500_clear_mask, ts5500_set_mask

### ts5500_gpio_set
- Return type: static int
- Signature: ts5500_gpio_set(struct gpio_chip * chip,unsigned offset,int val)
- Line: 247
- Calls: gpiochip_get_data, ts5500_clear_mask, ts5500_set_mask

### ts5500_gpio_to_irq
- Return type: static int
- Signature: ts5500_gpio_to_irq(struct gpio_chip * chip,unsigned offset)
- Line: 263
- Calls: gpiochip_get_data

### ts5500_set_mask
- Return type: static void
- Signature: ts5500_set_mask(u8 mask,u8 addr)
- Line: 184
- Called by: ts5500_enable_irq, ts5500_gpio_output, ts5500_gpio_set

## Structs (2)

### ts5500_dio
- Line: 50
- Members:
  - pinout: const struct ts5500_dio *
  - gpio_chip: gpio_chip
  - lock: spinlock_t
  - strap: bool
  - hwirq: u8
  - value_addr: const u8
  - value_mask: const u8
  - control_addr: const u8
  - control_mask: const u8
  - no_input: const bool
  - no_output: const bool
  - irq: const u8

### ts5500_priv
- Line: 32
- Members:
  - pinout: const struct ts5500_dio *
  - gpio_chip: gpio_chip
  - lock: spinlock_t
  - strap: bool
  - hwirq: u8
  - value_addr: const u8
  - value_mask: const u8
  - control_addr: const u8
  - control_mask: const u8
  - no_input: const bool
  - no_output: const bool
  - irq: const u8

## Enums (1)

### ts5500_blocks
- Line: 30

## Variables (6)

- static **hex7d_reserved** : bool (line 44)
- static **ts5500_dio1** : const struct ts5500_dio[] (line 122)
- static **ts5500_dio2** : const struct ts5500_dio[] (line 150)
- static **ts5500_dio_driver** : platform_driver (line 433)
- static **ts5500_dio_ids** : const struct platform_device_id[] (line 424)
- static **ts5500_lcd** : const struct ts5500_dio[] (line 176)

## Macros (5)

- **TS5500_DIO_GROUP**(vaddr,vbitfrom,caddr,cbit) (line 95)
- **TS5500_DIO_IN**(addr,bit) (line 68)
- **TS5500_DIO_IN_IRQ**(addr,bit,_irq) (line 75)
- **TS5500_DIO_IN_OUT**(vaddr,vbit,caddr,cbit) (line 60)
- **TS5500_DIO_OUT**(addr,bit) (line 83)
