# drivers/gpio/gpio-amd-fch.c

Subsystem: drivers/gpio

## Functions (8)

### amd_fch_gpio_addr
- Return type: static void __iomem *
- Signature: amd_fch_gpio_addr(struct amd_fch_gpio_priv * priv,unsigned int gpio)
- Line: 42
- Called by: amd_fch_gpio_direction_input, amd_fch_gpio_direction_output, amd_fch_gpio_get, amd_fch_gpio_get_direction, amd_fch_gpio_set

### amd_fch_gpio_direction_input
- Return type: static int
- Signature: amd_fch_gpio_direction_input(struct gpio_chip * gc,unsigned int offset)
- Line: 48
- Calls: amd_fch_gpio_addr, gpiochip_get_data

### amd_fch_gpio_direction_output
- Return type: static int
- Signature: amd_fch_gpio_direction_output(struct gpio_chip * gc,unsigned int gpio,int value)
- Line: 62
- Calls: amd_fch_gpio_addr, gpiochip_get_data

### amd_fch_gpio_get
- Return type: static int
- Signature: amd_fch_gpio_get(struct gpio_chip * gc,unsigned int offset)
- Line: 120
- Calls: amd_fch_gpio_addr, gpiochip_get_data

### amd_fch_gpio_get_direction
- Return type: static int
- Signature: amd_fch_gpio_get_direction(struct gpio_chip * gc,unsigned int gpio)
- Line: 85
- Calls: amd_fch_gpio_addr, gpiochip_get_data

### amd_fch_gpio_probe
- Return type: static int
- Signature: amd_fch_gpio_probe(struct platform_device * pdev)
- Line: 141

### amd_fch_gpio_request
- Return type: static int
- Signature: amd_fch_gpio_request(struct gpio_chip * chip,unsigned int gpio_pin)
- Line: 135

### amd_fch_gpio_set
- Return type: static int
- Signature: amd_fch_gpio_set(struct gpio_chip * gc,unsigned int gpio,int value)
- Line: 99
- Calls: amd_fch_gpio_addr, gpiochip_get_data

## Structs (1)

### amd_fch_gpio_priv
- Line: 35
- Members:
  - gc: gpio_chip
  - base: void __iomem *
  - pdata: amd_fch_gpio_pdata *
  - lock: spinlock_t

## Variables (2)

- static **amd_fch_gpio_driver** : platform_driver (line 182)
- static **amd_fch_gpio_iores** : const struct resource (line 29)

## Macros (6)

- **AMD_FCH_GPIO_BANK0_BASE** (line 22)
- **AMD_FCH_GPIO_FLAG_DIRECTION** (line 25)
- **AMD_FCH_GPIO_FLAG_READ** (line 27)
- **AMD_FCH_GPIO_FLAG_WRITE** (line 26)
- **AMD_FCH_GPIO_SIZE** (line 23)
- **AMD_FCH_MMIO_BASE** (line 21)
