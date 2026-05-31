# drivers/gpio/gpio-creg-snps.c

Subsystem: drivers/gpio

## Functions (5)

### creg_gpio_dir_out
- Return type: static int
- Signature: creg_gpio_dir_out(struct gpio_chip * gc,unsigned int offset,int val)
- Line: 54
- Calls: creg_gpio_set

### creg_gpio_probe
- Return type: static int
- Signature: creg_gpio_probe(struct platform_device * pdev)
- Line: 135
- Calls: creg_gpio_validate

### creg_gpio_set
- Return type: static int
- Signature: creg_gpio_set(struct gpio_chip * gc,unsigned int offset,int val)
- Line: 30
- Calls: gpiochip_get_data
- Called by: creg_gpio_dir_out

### creg_gpio_validate
- Return type: static int
- Signature: creg_gpio_validate(struct device * dev,struct creg_gpio * hcg,u32 ngpios)
- Line: 81
- Calls: creg_gpio_validate_pg
- Called by: creg_gpio_probe

### creg_gpio_validate_pg
- Return type: static int
- Signature: creg_gpio_validate_pg(struct device * dev,struct creg_gpio * hcg,int i)
- Line: 59
- Called by: creg_gpio_validate

## Structs (2)

### creg_gpio
- Line: 23
- Members:
  - ngpio: u8
  - shift: u8[]
  - on: u8[]
  - off: u8[]
  - bit_per_gpio: u8[]
  - gc: gpio_chip
  - regs: void __iomem *
  - lock: spinlock_t
  - layout: const struct creg_layout *

### creg_layout
- Line: 15
- Members:
  - ngpio: u8
  - shift: u8[]
  - on: u8[]
  - off: u8[]
  - bit_per_gpio: u8[]
  - gc: gpio_chip
  - regs: void __iomem *
  - lock: spinlock_t
  - layout: const struct creg_layout *

## Variables (4)

- static **axs10x_flsh_cs_ctl** : const struct creg_layout (line 117)
- static **creg_gpio_ids** : const struct of_device_id[] (line 125)
- static **creg_gpio_snps_driver** : platform_driver (line 180)
- static **hsdk_cs_ctl** : const struct creg_layout (line 109)

## Macros (1)

- **MAX_GPIO** (line 13)
