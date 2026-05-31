# drivers/gpio/gpio-max77620.c

Subsystem: drivers/gpio

## Functions (15)

### max77620_gpio_bus_lock
- Return type: static void
- Signature: max77620_gpio_bus_lock(struct irq_data * data)
- Line: 98
- Calls: gpiochip_get_data

### max77620_gpio_bus_sync_unlock
- Return type: static void
- Signature: max77620_gpio_bus_sync_unlock(struct irq_data * data)
- Line: 106
- Calls: gpiochip_get_data

### max77620_gpio_dir_input
- Return type: static int
- Signature: max77620_gpio_dir_input(struct gpio_chip * gc,unsigned int offset)
- Line: 153
- Calls: gpiochip_get_data

### max77620_gpio_dir_output
- Return type: static int
- Signature: max77620_gpio_dir_output(struct gpio_chip * gc,unsigned int offset,int value)
- Line: 185
- Calls: gpiochip_get_data

### max77620_gpio_get
- Return type: static int
- Signature: max77620_gpio_get(struct gpio_chip * gc,unsigned int offset)
- Line: 167
- Calls: gpiochip_get_data

### max77620_gpio_get_dir
- Return type: static int
- Signature: max77620_gpio_get_dir(struct gpio_chip * gc,unsigned int offset)
- Line: 135
- Calls: gpiochip_get_data

### max77620_gpio_irq_init_hw
- Return type: static int
- Signature: max77620_gpio_irq_init_hw(struct gpio_chip * gc)
- Line: 281
- Calls: gpiochip_get_data

### max77620_gpio_irq_mask
- Return type: static void
- Signature: max77620_gpio_irq_mask(struct irq_data * data)
- Line: 51
- Calls: gpiochip_disable_irq, gpiochip_get_data

### max77620_gpio_irq_unmask
- Return type: static void
- Signature: max77620_gpio_irq_unmask(struct irq_data * data)
- Line: 60
- Calls: gpiochip_enable_irq, gpiochip_get_data

### max77620_gpio_irqhandler
- Return type: static irqreturn_t
- Signature: max77620_gpio_irqhandler(int irq,void * data)
- Line: 26

### max77620_gpio_probe
- Return type: static int
- Signature: max77620_gpio_probe(struct platform_device * pdev)
- Line: 305

### max77620_gpio_set
- Return type: static int
- Signature: max77620_gpio_set(struct gpio_chip * gc,unsigned int offset,int value)
- Line: 244
- Calls: gpiochip_get_data

### max77620_gpio_set_config
- Return type: static int
- Signature: max77620_gpio_set_config(struct gpio_chip * gc,unsigned int offset,unsigned long config)
- Line: 257
- Calls: gpiochip_get_data, max77620_gpio_set_debounce

### max77620_gpio_set_debounce
- Return type: static int
- Signature: max77620_gpio_set_debounce(struct max77620_gpio * mgpio,unsigned int offset,unsigned int debounce)
- Line: 211
- Called by: max77620_gpio_set_config

### max77620_gpio_set_irq_type
- Return type: static int
- Signature: max77620_gpio_set_irq_type(struct irq_data * data,unsigned int type)
- Line: 69
- Calls: gpiochip_get_data

## Structs (1)

### max77620_gpio
- Line: 17
- Members:
  - gpio_chip: gpio_chip
  - rmap: regmap *
  - dev: device *
  - buslock: mutex
  - irq_type: unsigned int[]
  - irq_enabled: bool[]

## Variables (3)

- static **max77620_gpio_devtype** : const struct platform_device_id[] (line 367)
- static **max77620_gpio_driver** : platform_driver (line 374)
- static **max77620_gpio_irqchip** : const struct irq_chip (line 124)

## Macros (1)

- **GPIO_REG_ADDR**(offset) (line 15)
