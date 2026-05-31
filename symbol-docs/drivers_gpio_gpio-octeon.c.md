# drivers/gpio/gpio-octeon.c

Subsystem: drivers/gpio

## Functions (6)

### bit_cfg_reg
- Return type: static unsigned int
- Signature: bit_cfg_reg(unsigned int offset)
- Line: 25
- Called by: octeon_gpio_dir_in, octeon_gpio_dir_out, thunderx_gpio_dir_in, thunderx_gpio_dir_out, thunderx_gpio_get_direction, thunderx_gpio_irq_set_type, thunderx_gpio_is_gpio_nowarn, thunderx_gpio_probe, thunderx_gpio_set_config

### octeon_gpio_dir_in
- Return type: static int
- Signature: octeon_gpio_dir_in(struct gpio_chip * chip,unsigned offset)
- Line: 42
- Calls: bit_cfg_reg, gpiochip_get_data

### octeon_gpio_dir_out
- Return type: static int
- Signature: octeon_gpio_dir_out(struct gpio_chip * chip,unsigned offset,int value)
- Line: 61
- Calls: bit_cfg_reg, gpiochip_get_data, octeon_gpio_set

### octeon_gpio_get
- Return type: static int
- Signature: octeon_gpio_get(struct gpio_chip * chip,unsigned offset)
- Line: 76
- Calls: gpiochip_get_data

### octeon_gpio_probe
- Return type: static int
- Signature: octeon_gpio_probe(struct platform_device * pdev)
- Line: 84

### octeon_gpio_set
- Return type: static int
- Signature: octeon_gpio_set(struct gpio_chip * chip,unsigned int offset,int value)
- Line: 50
- Calls: gpiochip_get_data
- Called by: octeon_gpio_dir_out

## Structs (1)

### octeon_gpio
- Line: 37
- Members:
  - chip: gpio_chip
  - register_base: u64

## Variables (2)

- static **octeon_gpio_driver** : platform_driver (line 128)
- static **octeon_gpio_match** : const struct of_device_id[] (line 120)

## Macros (3)

- **RX_DAT** (line 18)
- **TX_CLEAR** (line 20)
- **TX_SET** (line 19)
