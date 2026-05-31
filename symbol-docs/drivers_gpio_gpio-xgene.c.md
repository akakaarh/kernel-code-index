# drivers/gpio/gpio-xgene.c

Subsystem: drivers/gpio

## Functions (9)

### __xgene_gpio_set
- Return type: static void
- Signature: __xgene_gpio_set(struct gpio_chip * gc,unsigned int offset,int val)
- Line: 48
- Calls: gpiochip_get_data
- Called by: xgene_gpio_dir_out, xgene_gpio_set

### xgene_gpio_dir_in
- Return type: static int
- Signature: xgene_gpio_dir_in(struct gpio_chip * gc,unsigned int offset)
- Line: 91
- Calls: gpiochip_get_data

### xgene_gpio_dir_out
- Return type: static int
- Signature: xgene_gpio_dir_out(struct gpio_chip * gc,unsigned int offset,int val)
- Line: 111
- Calls: __xgene_gpio_set, gpiochip_get_data

### xgene_gpio_get
- Return type: static int
- Signature: xgene_gpio_get(struct gpio_chip * gc,unsigned int offset)
- Line: 37
- Calls: gpiochip_get_data

### xgene_gpio_get_direction
- Return type: static int
- Signature: xgene_gpio_get_direction(struct gpio_chip * gc,unsigned int offset)
- Line: 77
- Calls: gpiochip_get_data

### xgene_gpio_probe
- Return type: static int
- Signature: xgene_gpio_probe(struct platform_device * pdev)
- Line: 161

### xgene_gpio_resume
- Return type: static int
- Signature: xgene_gpio_resume(struct device * dev)
- Line: 146

### xgene_gpio_set
- Return type: static int
- Signature: xgene_gpio_set(struct gpio_chip * gc,unsigned int offset,int val)
- Line: 65
- Calls: __xgene_gpio_set, gpiochip_get_data

### xgene_gpio_suspend
- Return type: static int
- Signature: xgene_gpio_suspend(struct device * dev)
- Line: 133

## Structs (1)

### xgene_gpio
- Line: 30
- Members:
  - chip: gpio_chip
  - base: void __iomem *
  - lock: spinlock_t
  - set_dr_val: u32[]

## Variables (3)

- static **xgene_gpio_acpi_match** : const struct acpi_device_id[] (line 196)
- static **xgene_gpio_driver** : platform_driver (line 202)
- static **xgene_gpio_of_match** : const struct of_device_id[] (line 190)

## Macros (8)

- **GPIO_BANK_OFFSET**(x) (line 28)
- **GPIO_BANK_STRIDE** (line 21)
- **GPIO_BIT_OFFSET**(x) (line 27)
- **GPIO_DATA_OFFSET** (line 20)
- **GPIO_SET_DR_OFFSET** (line 19)
- **XGENE_GPIOS_PER_BANK** (line 23)
- **XGENE_MAX_GPIOS** (line 25)
- **XGENE_MAX_GPIO_BANKS** (line 24)
