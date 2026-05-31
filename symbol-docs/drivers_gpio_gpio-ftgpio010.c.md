# drivers/gpio/gpio-ftgpio010.c

Subsystem: drivers/gpio

## Functions (7)

### ftgpio_gpio_ack_irq
- Return type: static void
- Signature: ftgpio_gpio_ack_irq(struct irq_data * d)
- Line: 56
- Calls: gpiochip_get_data
- Called by: ftgpio_gpio_set_irq_type

### ftgpio_gpio_irq_handler
- Return type: static void
- Signature: ftgpio_gpio_irq_handler(struct irq_desc * desc)
- Line: 141
- Calls: gpiochip_get_data

### ftgpio_gpio_mask_irq
- Return type: static void
- Signature: ftgpio_gpio_mask_irq(struct irq_data * d)
- Line: 64
- Calls: gpiochip_disable_irq, gpiochip_get_data

### ftgpio_gpio_probe
- Return type: static int
- Signature: ftgpio_gpio_probe(struct platform_device * pdev)
- Line: 236
- Calls: gpio_generic_chip_init

### ftgpio_gpio_set_config
- Return type: static int
- Signature: ftgpio_gpio_set_config(struct gpio_chip * gc,unsigned int offset,unsigned long config)
- Line: 159
- Calls: gpiochip_get_data

### ftgpio_gpio_set_irq_type
- Return type: static int
- Signature: ftgpio_gpio_set_irq_type(struct irq_data * d,unsigned int type)
- Line: 88
- Calls: ftgpio_gpio_ack_irq, gpiochip_get_data

### ftgpio_gpio_unmask_irq
- Return type: static void
- Signature: ftgpio_gpio_unmask_irq(struct irq_data * d)
- Line: 76
- Calls: gpiochip_enable_irq, gpiochip_get_data

## Structs (1)

### ftgpio_gpio
- Line: 49
- Members:
  - dev: device *
  - chip: gpio_generic_chip
  - base: void __iomem *
  - clk: clk *

## Variables (3)

- static **ftgpio_gpio_driver** : platform_driver (line 327)
- static **ftgpio_gpio_of_match** : const struct of_device_id[] (line 314)
- static **ftgpio_irq_chip** : const struct irq_chip (line 226)

## Macros (18)

- **GPIO_BYPASS_IN** (line 26)
- **GPIO_DATA_CLR** (line 28)
- **GPIO_DATA_IN** (line 24)
- **GPIO_DATA_OUT** (line 23)
- **GPIO_DATA_SET** (line 27)
- **GPIO_DEBOUNCE_EN** (line 39)
- **GPIO_DEBOUNCE_PRESCALE** (line 40)
- **GPIO_DIR** (line 25)
- **GPIO_INT_BOTH_EDGE** (line 37)
- **GPIO_INT_CLR** (line 35)
- **GPIO_INT_EN** (line 31)
- **GPIO_INT_LEVEL** (line 38)
- **GPIO_INT_MASK** (line 34)
- **GPIO_INT_STAT_MASKED** (line 33)
- **GPIO_INT_STAT_RAW** (line 32)
- **GPIO_INT_TYPE** (line 36)
- **GPIO_PULL_EN** (line 29)
- **GPIO_PULL_TYPE** (line 30)
