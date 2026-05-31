# drivers/gpio/gpio-amd8111.c

Subsystem: drivers/gpio

## Functions (8)

### amd_gpio_dirin
- Return type: static int
- Signature: amd_gpio_dirin(struct gpio_chip * chip,unsigned offset)
- Line: 143
- Calls: gpiochip_get_data

### amd_gpio_dirout
- Return type: static int
- Signature: amd_gpio_dirout(struct gpio_chip * chip,unsigned offset,int value)
- Line: 126
- Calls: gpiochip_get_data

### amd_gpio_exit
- Return type: static void __exit
- Signature: amd_gpio_exit(void)
- Line: 240
- Calls: gpiochip_remove

### amd_gpio_free
- Return type: static void
- Signature: amd_gpio_free(struct gpio_chip * chip,unsigned offset)
- Line: 88
- Calls: gpiochip_get_data

### amd_gpio_get
- Return type: static int
- Signature: amd_gpio_get(struct gpio_chip * chip,unsigned offset)
- Line: 114
- Calls: gpiochip_get_data

### amd_gpio_init
- Return type: static int __init
- Signature: amd_gpio_init(void)
- Line: 175

### amd_gpio_request
- Return type: static int
- Signature: amd_gpio_request(struct gpio_chip * chip,unsigned offset)
- Line: 76
- Calls: gpiochip_get_data

### amd_gpio_set
- Return type: static int
- Signature: amd_gpio_set(struct gpio_chip * chip,unsigned int offset,int value)
- Line: 97
- Calls: gpiochip_get_data

## Structs (1)

### amd_gpio
- Line: 67
- Members:
  - chip: gpio_chip
  - pmbase: u32
  - pm: void __iomem *
  - pdev: pci_dev *
  - lock: spinlock_t
  - orig: u8[32]

## Variables (2)

- static **gp** : amd_gpio (line 160)
- static **pci_tbl** : const struct pci_device_id[] (line 61)

## Macros (17)

- **AMD_GPIO_DEBOUNCE** (line 39)
- **AMD_GPIO_LTCH_STS** (line 37)
- **AMD_GPIO_MODE_ALTFN** (line 44)
- **AMD_GPIO_MODE_IN** (line 41)
- **AMD_GPIO_MODE_MASK** (line 40)
- **AMD_GPIO_MODE_OUT** (line 42)
- **AMD_GPIO_RTIN** (line 38)
- **AMD_GPIO_X_IN_ACTIVEHI** (line 46)
- **AMD_GPIO_X_IN_LATCH** (line 47)
- **AMD_GPIO_X_MASK** (line 45)
- **AMD_GPIO_X_OUT_CLK0** (line 50)
- **AMD_GPIO_X_OUT_CLK1** (line 51)
- **AMD_GPIO_X_OUT_HI** (line 49)
- **AMD_GPIO_X_OUT_LOW** (line 48)
- **AMD_REG_GPIO**(i) (line 35)
- **PMBASE_OFFSET** (line 32)
- **PMBASE_SIZE** (line 33)
