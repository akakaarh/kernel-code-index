# drivers/gpio/gpio-cs5535.c

Subsystem: drivers/gpio

## Functions (14)

### __cs5535_gpio_clear
- Return type: static void
- Signature: __cs5535_gpio_clear(struct cs5535_gpio_chip * chip,unsigned offset,unsigned int reg)
- Line: 101
- Calls: errata_outl
- Called by: chip_direction_input, chip_direction_output, chip_gpio_request, cs5535_gpio_clear

### __cs5535_gpio_set
- Return type: static void
- Signature: __cs5535_gpio_set(struct cs5535_gpio_chip * chip,unsigned offset,unsigned int reg)
- Line: 79
- Calls: errata_outl
- Called by: chip_direction_input, chip_direction_output, cs5535_gpio_set

### chip_direction_input
- Return type: static int
- Signature: chip_direction_input(struct gpio_chip * c,unsigned offset)
- Line: 241
- Calls: __cs5535_gpio_clear, __cs5535_gpio_set, gpiochip_get_data

### chip_direction_output
- Return type: static int
- Signature: chip_direction_output(struct gpio_chip * c,unsigned offset,int val)
- Line: 254
- Calls: __cs5535_gpio_clear, __cs5535_gpio_set, gpiochip_get_data

### chip_gpio_get
- Return type: static int
- Signature: chip_gpio_get(struct gpio_chip * chip,unsigned offset)
- Line: 226
- Calls: cs5535_gpio_isset

### chip_gpio_request
- Return type: static int
- Signature: chip_gpio_request(struct gpio_chip * c,unsigned offset)
- Line: 199
- Calls: __cs5535_gpio_clear, gpiochip_get_data

### chip_gpio_set
- Return type: static int
- Signature: chip_gpio_set(struct gpio_chip * chip,unsigned int offset,int val)
- Line: 231
- Calls: cs5535_gpio_clear, cs5535_gpio_set

### cs5535_gpio_clear
- Return type: void
- Signature: cs5535_gpio_clear(unsigned offset,unsigned int reg)
- Line: 112
- Calls: __cs5535_gpio_clear
- Called by: chip_gpio_set

### cs5535_gpio_isset
- Return type: int
- Signature: cs5535_gpio_isset(unsigned offset,unsigned int reg)
- Line: 123
- Called by: chip_gpio_get

### cs5535_gpio_probe
- Return type: static int
- Signature: cs5535_gpio_probe(struct platform_device * pdev)
- Line: 284

### cs5535_gpio_set
- Return type: void
- Signature: cs5535_gpio_set(unsigned offset,unsigned int reg)
- Line: 90
- Calls: __cs5535_gpio_set
- Called by: chip_gpio_set

### cs5535_gpio_set_irq
- Return type: int
- Signature: cs5535_gpio_set_irq(unsigned group,unsigned irq)
- Line: 144

### cs5535_gpio_setup_event
- Return type: void
- Signature: cs5535_gpio_setup_event(unsigned offset,int pair,int pme)
- Line: 161

### errata_outl
- Return type: static void
- Signature: errata_outl(struct cs5535_gpio_chip * chip,u32 val,unsigned int reg)
- Line: 56
- Called by: __cs5535_gpio_clear, __cs5535_gpio_set

## Structs (1)

### cs5535_gpio_chip
- Line: 42
- Members:
  - chip: gpio_chip
  - base: resource_size_t
  - pdev: platform_device *
  - lock: spinlock_t

## Variables (4)

- **cs5535_gpio_chip** : cs5535_gpio_chip (line 48)
- static **cs5535_gpio_driver** : platform_driver (line 348)
- static **cs5535_gpio_names** : const char * const[] (line 273)
- static **mask** : ulong (line 38)

## Macros (2)

- **DRV_NAME** (line 17)
- **GPIO_DEFAULT_MASK** (line 36)
