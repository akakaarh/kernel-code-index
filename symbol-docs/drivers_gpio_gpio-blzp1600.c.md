# drivers/gpio/gpio-blzp1600.c

Subsystem: drivers/gpio

## Functions (15)

### blzp1600_gpio_irq_ack
- Return type: static void
- Signature: blzp1600_gpio_irq_ack(struct irq_data * d)
- Line: 92
- Calls: blzp1600_gpio_write, get_blzp1600_gpio_from_irq_data

### blzp1600_gpio_irq_disable
- Return type: static void
- Signature: blzp1600_gpio_irq_disable(struct irq_data * d)
- Line: 110
- Calls: blzp1600_gpio_rmw, get_blzp1600_gpio_from_irq_data, gpiochip_disable_irq

### blzp1600_gpio_irq_enable
- Return type: static void
- Signature: blzp1600_gpio_irq_enable(struct irq_data * d)
- Line: 99
- Calls: blzp1600_gpio_rmw, get_blzp1600_gpio_from_irq_data, gpiochip_enable_irq

### blzp1600_gpio_irq_mask
- Return type: static void
- Signature: blzp1600_gpio_irq_mask(struct irq_data * d)
- Line: 76
- Calls: blzp1600_gpio_rmw, get_blzp1600_gpio_from_irq_data

### blzp1600_gpio_irq_set_type
- Return type: static int
- Signature: blzp1600_gpio_irq_set_type(struct irq_data * d,u32 type)
- Line: 119
- Calls: blzp1600_gpio_read, blzp1600_gpio_write, get_blzp1600_gpio_from_irq_data

### blzp1600_gpio_irq_unmask
- Return type: static void
- Signature: blzp1600_gpio_irq_unmask(struct irq_data * d)
- Line: 84
- Calls: blzp1600_gpio_rmw, get_blzp1600_gpio_from_irq_data

### blzp1600_gpio_irqhandler
- Return type: static void
- Signature: blzp1600_gpio_irqhandler(struct irq_desc * desc)
- Line: 181
- Calls: blzp1600_gpio_read, get_blzp1600_gpio_from_irq_desc

### blzp1600_gpio_probe
- Return type: static int
- Signature: blzp1600_gpio_probe(struct platform_device * pdev)
- Line: 218
- Calls: gpio_generic_chip_init

### blzp1600_gpio_read
- Return type: static u32
- Signature: blzp1600_gpio_read(struct blzp1600_gpio * chip,unsigned int offset)
- Line: 54
- Called by: blzp1600_gpio_irq_set_type, blzp1600_gpio_irqhandler

### blzp1600_gpio_rmw
- Return type: static void
- Signature: blzp1600_gpio_rmw(void __iomem * reg,u32 mask,bool set)
- Line: 64
- Called by: blzp1600_gpio_irq_disable, blzp1600_gpio_irq_enable, blzp1600_gpio_irq_mask, blzp1600_gpio_irq_unmask, blzp1600_gpio_set_debounce

### blzp1600_gpio_set_config
- Return type: static int
- Signature: blzp1600_gpio_set_config(struct gpio_chip * gc,unsigned int offset,unsigned long config)
- Line: 207
- Calls: blzp1600_gpio_set_debounce

### blzp1600_gpio_set_debounce
- Return type: static int
- Signature: blzp1600_gpio_set_debounce(struct gpio_chip * gc,unsigned int offset,unsigned int debounce)
- Line: 196
- Calls: blzp1600_gpio_rmw, gpiochip_get_data
- Called by: blzp1600_gpio_set_config

### blzp1600_gpio_write
- Return type: static void
- Signature: blzp1600_gpio_write(struct blzp1600_gpio * chip,unsigned int offset,u32 val)
- Line: 59
- Called by: blzp1600_gpio_irq_ack, blzp1600_gpio_irq_set_type

### get_blzp1600_gpio_from_irq_data
- Return type: static blzp1600_gpio *
- Signature: get_blzp1600_gpio_from_irq_data(struct irq_data * d)
- Line: 44
- Calls: gpiochip_get_data
- Called by: blzp1600_gpio_irq_ack, blzp1600_gpio_irq_disable, blzp1600_gpio_irq_enable, blzp1600_gpio_irq_mask, blzp1600_gpio_irq_set_type, blzp1600_gpio_irq_unmask

### get_blzp1600_gpio_from_irq_desc
- Return type: static blzp1600_gpio *
- Signature: get_blzp1600_gpio_from_irq_desc(struct irq_desc * d)
- Line: 49
- Calls: gpiochip_get_data
- Called by: blzp1600_gpio_irqhandler

## Structs (1)

### blzp1600_gpio
- Line: 38
- Members:
  - base: void __iomem *
  - gen_gc: gpio_generic_chip
  - irq: int

## Variables (3)

- static **blzp1600_gpio_driver** : platform_driver (line 278)
- static **blzp1600_gpio_irqchip** : const struct irq_chip (line 169)
- static **blzp1600_gpio_of_match** : const struct of_device_id[] (line 272)

## Macros (17)

- **DRIVER_NAME** (line 36)
- **GPIO_CLR_REG** (line 22)
- **GPIO_CTRL_REG** (line 20)
- **GPIO_DB_REG** (line 33)
- **GPIO_DFG_REG** (line 34)
- **GPIO_DIR_REG** (line 19)
- **GPIO_IBE_REG** (line 27)
- **GPIO_IC_REG** (line 32)
- **GPIO_IDATA_REG** (line 24)
- **GPIO_IEN_REG** (line 25)
- **GPIO_IEV_REG** (line 28)
- **GPIO_IM_REG** (line 30)
- **GPIO_IS_REG** (line 26)
- **GPIO_MIS_REG** (line 31)
- **GPIO_ODATA_REG** (line 23)
- **GPIO_RIS_REG** (line 29)
- **GPIO_SET_REG** (line 21)
