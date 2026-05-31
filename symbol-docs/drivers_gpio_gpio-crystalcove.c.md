# drivers/gpio/gpio-crystalcove.c

Subsystem: drivers/gpio

## Functions (15)

### crystalcove_bus_lock
- Return type: static void
- Signature: crystalcove_bus_lock(struct irq_data * data)
- Line: 215
- Calls: gpiochip_get_data

### crystalcove_bus_sync_unlock
- Return type: static void
- Signature: crystalcove_bus_sync_unlock(struct irq_data * data)
- Line: 222
- Calls: crystalcove_update_irq_ctrl, crystalcove_update_irq_mask, gpiochip_get_data

### crystalcove_gpio_dbg_show
- Return type: static void
- Signature: crystalcove_gpio_dbg_show(struct seq_file * s,struct gpio_chip * chip)
- Line: 302
- Calls: gpiochip_get_data, to_reg

### crystalcove_gpio_dir_in
- Return type: static int
- Signature: crystalcove_gpio_dir_in(struct gpio_chip * chip,unsigned int gpio)
- Line: 133
- Calls: gpiochip_get_data, to_reg

### crystalcove_gpio_dir_out
- Return type: static int
- Signature: crystalcove_gpio_dir_out(struct gpio_chip * chip,unsigned int gpio,int value)
- Line: 144
- Calls: gpiochip_get_data, to_reg

### crystalcove_gpio_get
- Return type: static int
- Signature: crystalcove_gpio_get(struct gpio_chip * chip,unsigned int gpio)
- Line: 155
- Calls: gpiochip_get_data, to_reg

### crystalcove_gpio_irq_handler
- Return type: static irqreturn_t
- Signature: crystalcove_gpio_irq_handler(int irq,void * data)
- Line: 277

### crystalcove_gpio_probe
- Return type: static int
- Signature: crystalcove_gpio_probe(struct platform_device * pdev)
- Line: 331

### crystalcove_gpio_set
- Return type: static int
- Signature: crystalcove_gpio_set(struct gpio_chip * chip,unsigned int gpio,int value)
- Line: 171
- Calls: gpiochip_get_data, to_reg

### crystalcove_irq_mask
- Return type: static void
- Signature: crystalcove_irq_mask(struct irq_data * data)
- Line: 251
- Calls: gpiochip_disable_irq, gpiochip_get_data

### crystalcove_irq_type
- Return type: static int
- Signature: crystalcove_irq_type(struct irq_data * data,unsigned int type)
- Line: 185
- Calls: gpiochip_get_data

### crystalcove_irq_unmask
- Return type: static void
- Signature: crystalcove_irq_unmask(struct irq_data * data)
- Line: 236
- Calls: gpiochip_enable_irq, gpiochip_get_data

### crystalcove_update_irq_ctrl
- Return type: static void
- Signature: crystalcove_update_irq_ctrl(struct crystalcove_gpio * cg,int gpio)
- Line: 126
- Calls: to_reg
- Called by: crystalcove_bus_sync_unlock

### crystalcove_update_irq_mask
- Return type: static void
- Signature: crystalcove_update_irq_mask(struct crystalcove_gpio * cg,int gpio)
- Line: 115
- Called by: crystalcove_bus_sync_unlock

### to_reg
- Return type: static int
- Signature: to_reg(int gpio,enum ctrl_register reg_type)
- Line: 83
- Called by: crystalcove_gpio_dbg_show, crystalcove_gpio_dir_in, crystalcove_gpio_dir_out, crystalcove_gpio_get, crystalcove_gpio_set, crystalcove_update_irq_ctrl, wcove_gpio_dbg_show, wcove_gpio_dir_in, wcove_gpio_dir_out, wcove_gpio_get, wcove_gpio_get_direction, wcove_gpio_set, wcove_gpio_set_config, wcove_update_irq_ctrl, xra1403_direction_input, xra1403_direction_output, xra1403_get, xra1403_get_direction, xra1403_set

## Structs (1)

### crystalcove_gpio
- Line: 74
- Members:
  - buslock: mutex
  - chip: gpio_chip
  - regmap: regmap *
  - update: int
  - intcnt_value: int
  - set_irq_mask: bool

## Enums (1)

### ctrl_register
- Line: 60

## Variables (2)

- static **crystalcove_gpio_driver** : platform_driver (line 388)
- static **crystalcove_irqchip** : const struct irq_chip (line 266)

## Macros (30)

- **CRYSTALCOVE_GPIO_NUM** (line 21)
- **CRYSTALCOVE_VGPIO_NUM** (line 22)
- **CTLI_INTCNT_BE** (line 42)
- **CTLI_INTCNT_DIS** (line 39)
- **CTLI_INTCNT_NE** (line 40)
- **CTLI_INTCNT_PE** (line 41)
- **CTLO_DIR_IN** (line 44)
- **CTLO_DIR_OUT** (line 45)
- **CTLO_DRV_CMOS** (line 47)
- **CTLO_DRV_OD** (line 48)
- **CTLO_DRV_REN** (line 50)
- **CTLO_INPUT_SET** (line 57)
- **CTLO_OUTPUT_SET** (line 58)
- **CTLO_RVAL_2KDW** (line 52)
- **CTLO_RVAL_2KUP** (line 53)
- **CTLO_RVAL_50KDW** (line 54)
- **CTLO_RVAL_50KUP** (line 55)
- **GPIO0IRQ** (line 27)
- **GPIO0P0CTLI** (line 34)
- **GPIO0P0CTLO** (line 33)
- **GPIO1IRQ** (line 28)
- **GPIO1P0CTLI** (line 36)
- **GPIO1P0CTLO** (line 35)
- **GPIOPANELCTL** (line 37)
- **MGPIO0IRQS0** (line 29)
- **MGPIO0IRQSX** (line 31)
- **MGPIO1IRQS0** (line 30)
- **MGPIO1IRQSX** (line 32)
- **UPDATE_IRQ_MASK** (line 25)
- **UPDATE_IRQ_TYPE** (line 24)
