# drivers/gpio/gpio-kempld.c

Subsystem: drivers/gpio

## Functions (18)

### kempld_gpio_bitop
- Return type: static void
- Signature: kempld_gpio_bitop(struct kempld_device_data * pld,u8 reg,unsigned int bit,bool val)
- Line: 49
- Called by: kempld_gpio_direction_input, kempld_gpio_direction_output, kempld_gpio_set

### kempld_gpio_direction_input
- Return type: static int
- Signature: kempld_gpio_direction_input(struct gpio_chip * chip,unsigned offset)
- Line: 153
- Calls: gpiochip_get_data, kempld_gpio_bitop

### kempld_gpio_direction_output
- Return type: static int
- Signature: kempld_gpio_direction_output(struct gpio_chip * chip,unsigned offset,int value)
- Line: 165
- Calls: gpiochip_get_data, kempld_gpio_bitop

### kempld_gpio_get
- Return type: static int
- Signature: kempld_gpio_get(struct gpio_chip * chip,unsigned offset)
- Line: 74
- Calls: gpiochip_get_data, kempld_gpio_get_bit

### kempld_gpio_get_bit
- Return type: static int
- Signature: kempld_gpio_get_bit(struct kempld_device_data * pld,u8 reg,unsigned int bit)
- Line: 62
- Called by: kempld_gpio_get, kempld_gpio_get_direction

### kempld_gpio_get_direction
- Return type: static int
- Signature: kempld_gpio_get_direction(struct gpio_chip * chip,unsigned offset)
- Line: 179
- Calls: gpiochip_get_data, kempld_gpio_get_bit

### kempld_gpio_get_multiple
- Return type: static int
- Signature: kempld_gpio_get_multiple(struct gpio_chip * chip,unsigned long * mask,unsigned long * bits)
- Line: 82
- Calls: gpiochip_get_data

### kempld_gpio_irq_handler
- Return type: static irqreturn_t
- Signature: kempld_gpio_irq_handler(int irq,void * data)
- Line: 291

### kempld_gpio_irq_init
- Return type: static int
- Signature: kempld_gpio_irq_init(struct device * dev,struct kempld_gpio_data * gpio)
- Line: 318
- Called by: kempld_gpio_probe

### kempld_gpio_pincount
- Return type: static int
- Signature: kempld_gpio_pincount(struct kempld_device_data * pld)
- Line: 190
- Called by: kempld_gpio_probe

### kempld_gpio_probe
- Return type: static int
- Signature: kempld_gpio_probe(struct platform_device * pdev)
- Line: 384
- Calls: kempld_gpio_irq_init, kempld_gpio_pincount

### kempld_gpio_set
- Return type: static int
- Signature: kempld_gpio_set(struct gpio_chip * chip,unsigned int offset,int value)
- Line: 109
- Calls: gpiochip_get_data, kempld_gpio_bitop

### kempld_gpio_set_multiple
- Return type: static int
- Signature: kempld_gpio_set_multiple(struct gpio_chip * chip,unsigned long * mask,unsigned long * bits)
- Line: 122
- Calls: gpiochip_get_data

### kempld_irq_bus_lock
- Return type: static void
- Signature: kempld_irq_bus_lock(struct irq_data * data)
- Line: 257
- Calls: gpiochip_get_data

### kempld_irq_bus_sync_unlock
- Return type: static void
- Signature: kempld_irq_bus_sync_unlock(struct irq_data * data)
- Line: 265
- Calls: gpiochip_get_data

### kempld_irq_mask
- Return type: static void
- Signature: kempld_irq_mask(struct irq_data * data)
- Line: 210
- Calls: gpiochip_disable_irq, gpiochip_get_data

### kempld_irq_set_type
- Return type: static int
- Signature: kempld_irq_set_type(struct irq_data * data,unsigned int type)
- Line: 228
- Calls: gpiochip_get_data

### kempld_irq_unmask
- Return type: static void
- Signature: kempld_irq_unmask(struct irq_data * data)
- Line: 219
- Calls: gpiochip_enable_irq, gpiochip_get_data

## Structs (1)

### kempld_gpio_data
- Line: 34
- Members:
  - chip: gpio_chip
  - pld: kempld_device_data *
  - out_lvl_reg: u8
  - irq_lock: mutex
  - ien: u16
  - evt_low_high: u16
  - evt_lvl_edge: u16

## Variables (3)

- static **gpio_irq** : unsigned int (line 30)
- static **kempld_gpio_driver** : platform_driver (line 454)
- static **kempld_irqchip** : const struct irq_chip (line 280)

## Macros (9)

- **KEMPLD_GPIO_DIR** (line 21)
- **KEMPLD_GPIO_EVT_LOW_HIGH** (line 25)
- **KEMPLD_GPIO_EVT_LVL_EDGE** (line 24)
- **KEMPLD_GPIO_IEN** (line 26)
- **KEMPLD_GPIO_LVL** (line 22)
- **KEMPLD_GPIO_MASK**(x) (line 20)
- **KEMPLD_GPIO_MAX_NUM** (line 19)
- **KEMPLD_GPIO_OUT_LVL** (line 27)
- **KEMPLD_GPIO_STS** (line 23)
