# drivers/gpio/gpio-timberdale.c

Subsystem: drivers/gpio

## Functions (11)

### timbgpio_gpio_direction_input
- Return type: static int
- Signature: timbgpio_gpio_direction_input(struct gpio_chip * gpio,unsigned nr)
- Line: 63
- Calls: timbgpio_update_bit

### timbgpio_gpio_direction_output
- Return type: static int
- Signature: timbgpio_gpio_direction_output(struct gpio_chip * gpio,unsigned nr,int val)
- Line: 77
- Calls: timbgpio_update_bit

### timbgpio_gpio_get
- Return type: static int
- Signature: timbgpio_gpio_get(struct gpio_chip * gpio,unsigned nr)
- Line: 68
- Calls: gpiochip_get_data

### timbgpio_gpio_set
- Return type: static int
- Signature: timbgpio_gpio_set(struct gpio_chip * gpio,unsigned int nr,int val)
- Line: 83
- Calls: timbgpio_update_bit

### timbgpio_irq
- Return type: static void
- Signature: timbgpio_irq(struct irq_desc * desc)
- Line: 190
- Calls: timbgpio_to_irq

### timbgpio_irq_disable
- Return type: static void
- Signature: timbgpio_irq_disable(struct irq_data * d)
- Line: 101
- Calls: gpiochip_disable_irq

### timbgpio_irq_enable
- Return type: static void
- Signature: timbgpio_irq_enable(struct irq_data * d)
- Line: 116
- Calls: gpiochip_enable_irq

### timbgpio_irq_type
- Return type: static int
- Signature: timbgpio_irq_type(struct irq_data * d,unsigned trigger)
- Line: 131

### timbgpio_probe
- Return type: static int
- Signature: timbgpio_probe(struct platform_device * pdev)
- Line: 222

### timbgpio_to_irq
- Return type: static int
- Signature: timbgpio_to_irq(struct gpio_chip * gpio,unsigned offset)
- Line: 88
- Calls: gpiochip_get_data
- Called by: timbgpio_irq

### timbgpio_update_bit
- Return type: static int
- Signature: timbgpio_update_bit(struct gpio_chip * gpio,unsigned index,unsigned offset,bool enabled)
- Line: 42
- Calls: gpiochip_get_data
- Called by: timbgpio_gpio_direction_input, timbgpio_gpio_direction_output, timbgpio_gpio_set

## Structs (1)

### timbgpio
- Line: 34
- Members:
  - membase: void __iomem *
  - lock: spinlock_t
  - gpio: gpio_chip
  - irq_base: int
  - last_ier: unsigned long

## Variables (2)

- static **timbgpio_irqchip** : const struct irq_chip (line 213)
- static **timbgpio_platform_driver** : platform_driver (line 285)

## Macros (11)

- **DRIVER_NAME** (line 21)
- **TGPIODIR** (line 24)
- **TGPIOVAL** (line 23)
- **TGPIO_BFLR** (line 32)
- **TGPIO_FLR** (line 29)
- **TGPIO_ICR** (line 28)
- **TGPIO_IER** (line 25)
- **TGPIO_IPR** (line 27)
- **TGPIO_ISR** (line 26)
- **TGPIO_LVR** (line 30)
- **TGPIO_VER** (line 31)
