# drivers/gpio/gpio-amdpt.c

Subsystem: drivers/gpio

## Functions (3)

### pt_gpio_free
- Return type: static void
- Signature: pt_gpio_free(struct gpio_chip * gc,unsigned offset)
- Line: 54
- Calls: gpiochip_get_data

### pt_gpio_probe
- Return type: static int
- Signature: pt_gpio_probe(struct platform_device * pdev)
- Line: 69
- Calls: gpio_generic_chip_init

### pt_gpio_request
- Return type: static int
- Signature: pt_gpio_request(struct gpio_chip * gc,unsigned offset)
- Line: 32
- Calls: gpiochip_get_data

## Structs (1)

### pt_gpio_chip
- Line: 27
- Members:
  - chip: gpio_generic_chip
  - reg_base: void __iomem *

## Variables (2)

- static **pt_gpio_acpi_match** : const struct acpi_device_id[] (line 127)
- static **pt_gpio_driver** : platform_driver (line 135)

## Macros (7)

- **PT_CLOCKRATE_REG** (line 24)
- **PT_DIRECTION_REG** (line 21)
- **PT_INPUTDATA_REG** (line 22)
- **PT_OUTPUTDATA_REG** (line 23)
- **PT_SYNC_REG** (line 25)
- **PT_TOTAL_GPIO** (line 17)
- **PT_TOTAL_GPIO_EX** (line 18)
