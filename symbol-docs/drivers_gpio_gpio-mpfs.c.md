# drivers/gpio/gpio-mpfs.c

Subsystem: drivers/gpio

## Functions (10)

### mpfs_gpio_direction_input
- Return type: static int
- Signature: mpfs_gpio_direction_input(struct gpio_chip * gc,unsigned int gpio_index)
- Line: 59
- Calls: gpiochip_get_data
- Called by: mpfs_gpio_irq_unmask

### mpfs_gpio_direction_output
- Return type: static int
- Signature: mpfs_gpio_direction_output(struct gpio_chip * gc,unsigned int gpio_index,int value)
- Line: 69
- Calls: gpiochip_get_data

### mpfs_gpio_get
- Return type: static int
- Signature: mpfs_gpio_get(struct gpio_chip * gc,unsigned int gpio_index)
- Line: 94
- Calls: gpiochip_get_data, mpfs_gpio_get_direction
- Called by: mpfs_gpio_set

### mpfs_gpio_get_direction
- Return type: static int
- Signature: mpfs_gpio_get_direction(struct gpio_chip * gc,unsigned int gpio_index)
- Line: 81
- Calls: gpiochip_get_data
- Called by: mpfs_gpio_get

### mpfs_gpio_irq_handler
- Return type: static void
- Signature: mpfs_gpio_irq_handler(struct irq_desc * desc)
- Line: 182

### mpfs_gpio_irq_mask
- Return type: static void
- Signature: mpfs_gpio_irq_mask(struct irq_data * data)
- Line: 162
- Calls: gpiochip_disable_irq, gpiochip_get_data

### mpfs_gpio_irq_set_type
- Return type: static int
- Signature: mpfs_gpio_irq_set_type(struct irq_data * data,unsigned int type)
- Line: 119
- Calls: gpiochip_get_data

### mpfs_gpio_irq_unmask
- Return type: static void
- Signature: mpfs_gpio_irq_unmask(struct irq_data * data)
- Line: 150
- Calls: gpiochip_enable_irq, gpiochip_get_data, mpfs_gpio_direction_input

### mpfs_gpio_probe
- Return type: static int
- Signature: mpfs_gpio_probe(struct platform_device * pdev)
- Line: 202

### mpfs_gpio_set
- Return type: static int
- Signature: mpfs_gpio_set(struct gpio_chip * gc,unsigned int gpio_index,int value)
- Line: 104
- Calls: gpiochip_get_data, mpfs_gpio_get

## Structs (2)

### mpfs_gpio_chip
- Line: 46
- Members:
  - inp: u8
  - outp: u8
  - regs: regmap *
  - offsets: const struct mpfs_gpio_reg_offsets *
  - gc: gpio_chip

### mpfs_gpio_reg_offsets
- Line: 41
- Members:
  - inp: u8
  - outp: u8
  - regs: regmap *
  - offsets: const struct mpfs_gpio_reg_offsets *
  - gc: gpio_chip

## Variables (6)

- static **coregpio_reg_offsets** : const struct mpfs_gpio_reg_offsets (line 284)
- static **mpfs_gpio_driver** : platform_driver (line 300)
- static **mpfs_gpio_irqchip** : const struct irq_chip (line 173)
- static **mpfs_gpio_of_ids** : const struct of_device_id[] (line 289)
- static **mpfs_gpio_regmap_config** : const struct regmap_config (line 52)
- static **mpfs_reg_offsets** : const struct mpfs_gpio_reg_offsets (line 279)

## Macros (18)

- **COREGPIO_INP_REG** (line 37)
- **COREGPIO_OUTP_REG** (line 39)
- **MPFS_GPIO_CTRL**(i) (line 20)
- **MPFS_GPIO_DIR_MASK** (line 26)
- **MPFS_GPIO_EN_IN** (line 24)
- **MPFS_GPIO_EN_INT** (line 22)
- **MPFS_GPIO_EN_OUT** (line 25)
- **MPFS_GPIO_EN_OUT_BUF** (line 23)
- **MPFS_GPIO_TYPE_INT_EDGE_BOTH** (line 28)
- **MPFS_GPIO_TYPE_INT_EDGE_NEG** (line 29)
- **MPFS_GPIO_TYPE_INT_EDGE_POS** (line 30)
- **MPFS_GPIO_TYPE_INT_LEVEL_HIGH** (line 32)
- **MPFS_GPIO_TYPE_INT_LEVEL_LOW** (line 31)
- **MPFS_GPIO_TYPE_INT_MASK** (line 33)
- **MPFS_INP_REG** (line 36)
- **MPFS_IRQ_REG** (line 34)
- **MPFS_MAX_NUM_GPIO** (line 21)
- **MPFS_OUTP_REG** (line 38)
