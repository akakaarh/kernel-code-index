# drivers/gpio/gpio-sprd.c

Subsystem: drivers/gpio

## Functions (15)

### sprd_gpio_bank_base
- Return type: static void __iomem *
- Signature: sprd_gpio_bank_base(struct sprd_gpio * sprd_gpio,unsigned int bank)
- Line: 42
- Called by: sprd_gpio_irq_handler, sprd_gpio_read, sprd_gpio_update

### sprd_gpio_direction_input
- Return type: static int
- Signature: sprd_gpio_direction_input(struct gpio_chip * chip,unsigned int offset)
- Line: 89
- Calls: sprd_gpio_update

### sprd_gpio_direction_output
- Return type: static int
- Signature: sprd_gpio_direction_output(struct gpio_chip * chip,unsigned int offset,int value)
- Line: 97
- Calls: sprd_gpio_update

### sprd_gpio_free
- Return type: static void
- Signature: sprd_gpio_free(struct gpio_chip * chip,unsigned int offset)
- Line: 84
- Calls: sprd_gpio_update

### sprd_gpio_get
- Return type: static int
- Signature: sprd_gpio_get(struct gpio_chip * chip,unsigned int offset)
- Line: 106
- Calls: sprd_gpio_read

### sprd_gpio_irq_ack
- Return type: static void
- Signature: sprd_gpio_irq_ack(struct irq_data * data)
- Line: 128
- Calls: sprd_gpio_update

### sprd_gpio_irq_handler
- Return type: static void
- Signature: sprd_gpio_irq_handler(struct irq_desc * desc)
- Line: 191
- Calls: gpiochip_get_data, sprd_gpio_bank_base

### sprd_gpio_irq_mask
- Return type: static void
- Signature: sprd_gpio_irq_mask(struct irq_data * data)
- Line: 119
- Calls: gpiochip_disable_irq, sprd_gpio_update

### sprd_gpio_irq_set_type
- Return type: static int
- Signature: sprd_gpio_irq_set_type(struct irq_data * data,unsigned int flow_type)
- Line: 145
- Calls: sprd_gpio_update

### sprd_gpio_irq_unmask
- Return type: static void
- Signature: sprd_gpio_irq_unmask(struct irq_data * data)
- Line: 136
- Calls: gpiochip_enable_irq, sprd_gpio_update

### sprd_gpio_probe
- Return type: static int
- Signature: sprd_gpio_probe(struct platform_device * pdev)
- Line: 222

### sprd_gpio_read
- Return type: static int
- Signature: sprd_gpio_read(struct gpio_chip * chip,unsigned int offset,u16 reg)
- Line: 69
- Calls: gpiochip_get_data, sprd_gpio_bank_base
- Called by: sprd_gpio_get

### sprd_gpio_request
- Return type: static int
- Signature: sprd_gpio_request(struct gpio_chip * chip,unsigned int offset)
- Line: 78
- Calls: sprd_gpio_update

### sprd_gpio_set
- Return type: static int
- Signature: sprd_gpio_set(struct gpio_chip * chip,unsigned int offset,int value)
- Line: 111
- Calls: sprd_gpio_update

### sprd_gpio_update
- Return type: static void
- Signature: sprd_gpio_update(struct gpio_chip * chip,unsigned int offset,u16 reg,int val)
- Line: 48
- Calls: gpiochip_get_data, sprd_gpio_bank_base
- Called by: sprd_gpio_direction_input, sprd_gpio_direction_output, sprd_gpio_free, sprd_gpio_irq_ack, sprd_gpio_irq_mask, sprd_gpio_irq_set_type, sprd_gpio_irq_unmask, sprd_gpio_request, sprd_gpio_set

## Structs (1)

### sprd_gpio
- Line: 35
- Members:
  - chip: gpio_chip
  - base: void __iomem *
  - lock: raw_spinlock_t
  - irq: int

## Variables (3)

- static **sprd_gpio_driver** : platform_driver (line 270)
- static **sprd_gpio_irqchip** : const struct irq_chip (line 212)
- static **sprd_gpio_of_match** : const struct of_device_id[] (line 264)

## Macros (16)

- **SPRD_GPIO_BANK_MASK** (line 32)
- **SPRD_GPIO_BANK_NR** (line 29)
- **SPRD_GPIO_BANK_SIZE** (line 31)
- **SPRD_GPIO_BIT**(x) (line 33)
- **SPRD_GPIO_DATA** (line 16)
- **SPRD_GPIO_DIR** (line 18)
- **SPRD_GPIO_DMSK** (line 17)
- **SPRD_GPIO_IBE** (line 20)
- **SPRD_GPIO_IC** (line 25)
- **SPRD_GPIO_IE** (line 22)
- **SPRD_GPIO_IEV** (line 21)
- **SPRD_GPIO_INEN** (line 26)
- **SPRD_GPIO_IS** (line 19)
- **SPRD_GPIO_MIS** (line 24)
- **SPRD_GPIO_NR** (line 30)
- **SPRD_GPIO_RIS** (line 23)
