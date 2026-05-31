# drivers/gpio/gpio-wcove.c

Subsystem: drivers/gpio

## Functions (18)

### to_ireg
- Return type: static int
- Signature: to_ireg(int gpio,enum ctrl_register type,unsigned int * mask)
- Line: 113
- Called by: wcove_gpio_dbg_show, wcove_gpio_irq_handler, wcove_update_irq_mask

### to_reg
- Return type: static int
- Signature: to_reg(int gpio,enum ctrl_register type)
- Line: 103
- Called by: crystalcove_gpio_dbg_show, crystalcove_gpio_dir_in, crystalcove_gpio_dir_out, crystalcove_gpio_get, crystalcove_gpio_set, crystalcove_update_irq_ctrl, wcove_gpio_dbg_show, wcove_gpio_dir_in, wcove_gpio_dir_out, wcove_gpio_get, wcove_gpio_get_direction, wcove_gpio_set, wcove_gpio_set_config, wcove_update_irq_ctrl, xra1403_direction_input, xra1403_direction_output, xra1403_get, xra1403_get_direction, xra1403_set

### wcove_bus_lock
- Return type: static void
- Signature: wcove_bus_lock(struct irq_data * data)
- Line: 268
- Calls: gpiochip_get_data

### wcove_bus_sync_unlock
- Return type: static void
- Signature: wcove_bus_sync_unlock(struct irq_data * data)
- Line: 276
- Calls: gpiochip_get_data, wcove_update_irq_ctrl, wcove_update_irq_mask

### wcove_gpio_dbg_show
- Return type: static void
- Signature: wcove_gpio_dbg_show(struct seq_file * s,struct gpio_chip * chip)
- Line: 371
- Calls: gpiochip_get_data, to_ireg, to_reg

### wcove_gpio_dir_in
- Return type: static int
- Signature: wcove_gpio_dir_in(struct gpio_chip * chip,unsigned int gpio)
- Line: 145
- Calls: gpiochip_get_data, to_reg

### wcove_gpio_dir_out
- Return type: static int
- Signature: wcove_gpio_dir_out(struct gpio_chip * chip,unsigned int gpio,int value)
- Line: 156
- Calls: gpiochip_get_data, to_reg

### wcove_gpio_get
- Return type: static int
- Signature: wcove_gpio_get(struct gpio_chip * chip,unsigned int gpio)
- Line: 187
- Calls: gpiochip_get_data, to_reg

### wcove_gpio_get_direction
- Return type: static int
- Signature: wcove_gpio_get_direction(struct gpio_chip * chip,unsigned int gpio)
- Line: 168
- Calls: gpiochip_get_data, to_reg

### wcove_gpio_irq_handler
- Return type: static irqreturn_t
- Signature: wcove_gpio_irq_handler(int irq,void * data)
- Line: 332
- Calls: to_ireg

### wcove_gpio_probe
- Return type: static int
- Signature: wcove_gpio_probe(struct platform_device * pdev)
- Line: 403

### wcove_gpio_set
- Return type: static int
- Signature: wcove_gpio_set(struct gpio_chip * chip,unsigned int gpio,int value)
- Line: 203
- Calls: gpiochip_get_data, to_reg

### wcove_gpio_set_config
- Return type: static int
- Signature: wcove_gpio_set_config(struct gpio_chip * chip,unsigned int gpio,unsigned long config)
- Line: 214
- Calls: gpiochip_get_data, to_reg

### wcove_irq_mask
- Return type: static void
- Signature: wcove_irq_mask(struct irq_data * data)
- Line: 306
- Calls: gpiochip_disable_irq, gpiochip_get_data

### wcove_irq_type
- Return type: static int
- Signature: wcove_irq_type(struct irq_data * data,unsigned int type)
- Line: 237
- Calls: gpiochip_get_data

### wcove_irq_unmask
- Return type: static void
- Signature: wcove_irq_unmask(struct irq_data * data)
- Line: 291
- Calls: gpiochip_enable_irq, gpiochip_get_data

### wcove_update_irq_ctrl
- Return type: static void
- Signature: wcove_update_irq_ctrl(struct wcove_gpio * wg,irq_hw_number_t gpio)
- Line: 138
- Calls: to_reg
- Called by: wcove_bus_sync_unlock

### wcove_update_irq_mask
- Return type: static void
- Signature: wcove_update_irq_mask(struct wcove_gpio * wg,irq_hw_number_t gpio)
- Line: 128
- Calls: to_ireg
- Called by: wcove_bus_sync_unlock

## Structs (1)

### wcove_gpio
- Line: 92
- Members:
  - buslock: mutex
  - chip: gpio_chip
  - dev: device *
  - regmap: regmap *
  - regmap_irq_chip: regmap_irq_chip_data *
  - update: int
  - intcnt: int
  - set_irq_mask: bool

## Enums (1)

### ctrl_register
- Line: 74

## Variables (2)

- static **wcove_gpio_driver** : platform_driver (line 499)
- static **wcove_irqchip** : const struct irq_chip (line 321)

## Macros (31)

- **BANK0_NR_PINS** (line 27)
- **BANK1_NR_PINS** (line 28)
- **BANK2_NR_PINS** (line 29)
- **CTLI_INTCNT_BE** (line 55)
- **CTLI_INTCNT_DIS** (line 52)
- **CTLI_INTCNT_NE** (line 53)
- **CTLI_INTCNT_PE** (line 54)
- **CTLO_DIR_IN** (line 57)
- **CTLO_DIR_OUT** (line 58)
- **CTLO_DRV_CMOS** (line 62)
- **CTLO_DRV_MASK** (line 60)
- **CTLO_DRV_OD** (line 61)
- **CTLO_DRV_REN** (line 64)
- **CTLO_INPUT_SET** (line 71)
- **CTLO_OUTPUT_SET** (line 72)
- **CTLO_RVAL_2KDOWN** (line 66)
- **CTLO_RVAL_2KUP** (line 67)
- **CTLO_RVAL_50KDOWN** (line 68)
- **CTLO_RVAL_50KUP** (line 69)
- **GPIO_IN_CTRL_BASE** (line 35)
- **GPIO_IRQ0_MASK** (line 47)
- **GPIO_IRQ1_MASK** (line 48)
- **GPIO_OUT_CTRL_BASE** (line 33)
- **GROUP0_NR_IRQS** (line 43)
- **GROUP1_NR_IRQS** (line 44)
- **IRQ_MASK_BASE** (line 45)
- **IRQ_STATUS_BASE** (line 46)
- **UPDATE_IRQ_MASK** (line 50)
- **UPDATE_IRQ_TYPE** (line 49)
- **WCOVE_GPIO_NUM** (line 30)
- **WCOVE_VGPIO_NUM** (line 31)
