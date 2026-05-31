# drivers/gpio/gpio-zevio.c

Subsystem: drivers/gpio

## Functions (8)

### zevio_gpio_direction_input
- Return type: static int
- Signature: zevio_gpio_direction_input(struct gpio_chip * chip,unsigned pin)
- Line: 112
- Calls: gpiochip_get_data, zevio_gpio_port_get, zevio_gpio_port_set

### zevio_gpio_direction_output
- Return type: static int
- Signature: zevio_gpio_direction_output(struct gpio_chip * chip,unsigned pin,int value)
- Line: 128
- Calls: gpiochip_get_data, zevio_gpio_port_get, zevio_gpio_port_set

### zevio_gpio_get
- Return type: static int
- Signature: zevio_gpio_get(struct gpio_chip * chip,unsigned pin)
- Line: 78
- Calls: gpiochip_get_data, zevio_gpio_port_get

### zevio_gpio_port_get
- Return type: static u32
- Signature: zevio_gpio_port_get(struct zevio_gpio * c,unsigned pin,unsigned port_offset)
- Line: 63
- Called by: zevio_gpio_direction_input, zevio_gpio_direction_output, zevio_gpio_get, zevio_gpio_set

### zevio_gpio_port_set
- Return type: static void
- Signature: zevio_gpio_port_set(struct zevio_gpio * c,unsigned pin,unsigned port_offset,u32 val)
- Line: 70
- Called by: zevio_gpio_direction_input, zevio_gpio_direction_output, zevio_gpio_probe, zevio_gpio_set

### zevio_gpio_probe
- Return type: static int
- Signature: zevio_gpio_probe(struct platform_device * pdev)
- Line: 173
- Calls: zevio_gpio_port_set

### zevio_gpio_set
- Return type: static int
- Signature: zevio_gpio_set(struct gpio_chip * chip,unsigned int pin,int value)
- Line: 94
- Calls: gpiochip_get_data, zevio_gpio_port_get, zevio_gpio_port_set

### zevio_gpio_to_irq
- Return type: static int
- Signature: zevio_gpio_to_irq(struct gpio_chip * chip,unsigned pin)
- Line: 151

## Structs (1)

### zevio_gpio
- Line: 57
- Members:
  - chip: gpio_chip
  - lock: spinlock_t
  - regs: void __iomem *

## Variables (3)

- static **zevio_gpio_chip** : const struct gpio_chip (line 161)
- static **zevio_gpio_driver** : platform_driver (line 218)
- static **zevio_gpio_of_match** : const struct of_device_id[] (line 213)

## Macros (10)

- **ZEVIO_GPIO_BIT**(gpio) (line 55)
- **ZEVIO_GPIO_DIRECTION** (line 49)
- **ZEVIO_GPIO_INPUT** (line 51)
- **ZEVIO_GPIO_INT_MASK** (line 48)
- **ZEVIO_GPIO_INT_MASKED_STATUS** (line 45)
- **ZEVIO_GPIO_INT_STATUS** (line 46)
- **ZEVIO_GPIO_INT_STICKY** (line 52)
- **ZEVIO_GPIO_INT_UNMASK** (line 47)
- **ZEVIO_GPIO_OUTPUT** (line 50)
- **ZEVIO_GPIO_SECTION_SIZE** (line 42)
