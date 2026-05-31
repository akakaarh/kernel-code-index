# drivers/gpio/gpio-mb86s7x.c

Subsystem: drivers/gpio

## Functions (9)

### mb86s70_gpio_direction_input
- Return type: static int
- Signature: mb86s70_gpio_direction_input(struct gpio_chip * gc,unsigned gpio)
- Line: 73
- Calls: gpiochip_get_data

### mb86s70_gpio_direction_output
- Return type: static int
- Signature: mb86s70_gpio_direction_output(struct gpio_chip * gc,unsigned gpio,int value)
- Line: 90
- Calls: gpiochip_get_data

### mb86s70_gpio_free
- Return type: static void
- Signature: mb86s70_gpio_free(struct gpio_chip * gc,unsigned gpio)
- Line: 58
- Calls: gpiochip_get_data

### mb86s70_gpio_get
- Return type: static int
- Signature: mb86s70_gpio_get(struct gpio_chip * gc,unsigned gpio)
- Line: 115
- Calls: gpiochip_get_data

### mb86s70_gpio_probe
- Return type: static int
- Signature: mb86s70_gpio_probe(struct platform_device * pdev)
- Line: 156
- Calls: acpi_gpiochip_request_interrupts

### mb86s70_gpio_remove
- Return type: static void
- Signature: mb86s70_gpio_remove(struct platform_device * pdev)
- Line: 201
- Calls: acpi_gpiochip_free_interrupts, gpiochip_remove

### mb86s70_gpio_request
- Return type: static int
- Signature: mb86s70_gpio_request(struct gpio_chip * gc,unsigned gpio)
- Line: 41
- Calls: gpiochip_get_data

### mb86s70_gpio_set
- Return type: static int
- Signature: mb86s70_gpio_set(struct gpio_chip * gc,unsigned int gpio,int value)
- Line: 122
- Calls: gpiochip_get_data

### mb86s70_gpio_to_irq
- Return type: static int
- Signature: mb86s70_gpio_to_irq(struct gpio_chip * gc,unsigned int offset)
- Line: 142

## Structs (1)

### mb86s70_gpio_chip
- Line: 35
- Members:
  - gc: gpio_chip
  - base: void __iomem *
  - lock: spinlock_t

## Variables (3)

- static **mb86s70_gpio_acpi_ids** : const struct acpi_device_id[] (line 216)
- static **mb86s70_gpio_driver** : platform_driver (line 223)
- static **mb86s70_gpio_dt_ids** : const struct of_device_id[] (line 209)

## Macros (4)

- **DDR**(x) (line 30)
- **OFFSET**(x) (line 33)
- **PDR**(x) (line 29)
- **PFR**(x) (line 31)
