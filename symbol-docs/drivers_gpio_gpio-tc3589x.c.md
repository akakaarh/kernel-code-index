# drivers/gpio/gpio-tc3589x.c

Subsystem: drivers/gpio

## Functions (14)

### tc3589x_gpio_direction_input
- Return type: static int
- Signature: tc3589x_gpio_direction_input(struct gpio_chip * chip,unsigned int offset)
- Line: 79
- Calls: gpiochip_get_data

### tc3589x_gpio_direction_output
- Return type: static int
- Signature: tc3589x_gpio_direction_output(struct gpio_chip * chip,unsigned int offset,int val)
- Line: 63
- Calls: gpiochip_get_data, tc3589x_gpio_set

### tc3589x_gpio_get
- Return type: static int
- Signature: tc3589x_gpio_get(struct gpio_chip * chip,unsigned int offset)
- Line: 37
- Calls: gpiochip_get_data

### tc3589x_gpio_get_direction
- Return type: static int
- Signature: tc3589x_gpio_get_direction(struct gpio_chip * chip,unsigned int offset)
- Line: 90
- Calls: gpiochip_get_data

### tc3589x_gpio_init
- Return type: static int __init
- Signature: tc3589x_gpio_init(void)
- Line: 374

### tc3589x_gpio_irq
- Return type: static irqreturn_t
- Signature: tc3589x_gpio_irq(int irq,void * dev)
- Line: 263

### tc3589x_gpio_irq_lock
- Return type: static void
- Signature: tc3589x_gpio_irq_lock(struct irq_data * d)
- Line: 188
- Calls: gpiochip_get_data

### tc3589x_gpio_irq_mask
- Return type: static void
- Signature: tc3589x_gpio_irq_mask(struct irq_data * d)
- Line: 226
- Calls: gpiochip_disable_irq, gpiochip_get_data

### tc3589x_gpio_irq_set_type
- Return type: static int
- Signature: tc3589x_gpio_irq_set_type(struct irq_data * d,unsigned int type)
- Line: 160
- Calls: gpiochip_get_data

### tc3589x_gpio_irq_sync_unlock
- Return type: static void
- Signature: tc3589x_gpio_irq_sync_unlock(struct irq_data * d)
- Line: 196
- Calls: gpiochip_get_data

### tc3589x_gpio_irq_unmask
- Return type: static void
- Signature: tc3589x_gpio_irq_unmask(struct irq_data * d)
- Line: 239
- Calls: gpiochip_enable_irq, gpiochip_get_data

### tc3589x_gpio_probe
- Return type: static int
- Signature: tc3589x_gpio_probe(struct platform_device * pdev)
- Line: 297

### tc3589x_gpio_set
- Return type: static int
- Signature: tc3589x_gpio_set(struct gpio_chip * chip,unsigned int offset,int val)
- Line: 52
- Calls: gpiochip_get_data
- Called by: tc3589x_gpio_direction_output

### tc3589x_gpio_set_config
- Return type: static int
- Signature: tc3589x_gpio_set_config(struct gpio_chip * chip,unsigned int offset,unsigned long config)
- Line: 109
- Calls: gpiochip_get_data

## Structs (1)

### tc3589x_gpio
- Line: 27
- Members:
  - chip: gpio_chip
  - tc3589x: tc3589x *
  - dev: device *
  - irq_lock: mutex
  - regs: u8[][]
  - oldregs: u8[][]

## Enums (1)

### __anon8f7d34900103
- Line: 22

## Variables (3)

- static **tc3589x_gpio_driver** : platform_driver (line 369)
- static **tc3589x_gpio_irq_chip** : const struct irq_chip (line 252)
- static **template_chip** : const struct gpio_chip (line 148)

## Macros (2)

- **CACHE_NR_BANKS** (line 25)
- **CACHE_NR_REGS** (line 24)
