# drivers/gpio/gpio-spear-spics.c

Subsystem: drivers/gpio

## Functions (6)

### spics_direction_output
- Return type: static int
- Signature: spics_direction_output(struct gpio_chip * chip,unsigned offset,int value)
- Line: 76
- Calls: spics_set_value

### spics_free
- Return type: static void
- Signature: spics_free(struct gpio_chip * chip,unsigned offset)
- Line: 97
- Calls: gpiochip_get_data

### spics_gpio_init
- Return type: static int __init
- Signature: spics_gpio_init(void)
- Line: 169

### spics_gpio_probe
- Return type: static int
- Signature: spics_gpio_probe(struct platform_device * pdev)
- Line: 109

### spics_request
- Return type: static int
- Signature: spics_request(struct gpio_chip * chip,unsigned offset)
- Line: 82
- Calls: gpiochip_get_data

### spics_set_value
- Return type: static int
- Signature: spics_set_value(struct gpio_chip * chip,unsigned int offset,int value)
- Line: 54
- Calls: gpiochip_get_data
- Called by: spics_direction_output

## Structs (1)

### spear_spics
- Line: 42
- Members:
  - base: void __iomem *
  - perip_cfg: u32
  - sw_enable_bit: u32
  - cs_value_bit: u32
  - cs_enable_mask: u32
  - cs_enable_shift: u32
  - use_count: unsigned long
  - last_off: int
  - chip: gpio_chip

## Variables (2)

- static **spics_gpio_driver** : platform_driver (line 161)
- static **spics_gpio_of_match** : const struct of_device_id[] (line 156)

## Macros (1)

- **NUM_OF_GPIO** (line 18)
