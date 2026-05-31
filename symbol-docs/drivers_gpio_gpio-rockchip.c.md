# drivers/gpio/gpio-rockchip.c

Subsystem: drivers/gpio

## Functions (31)

### gpio_readl_v2
- Return type: static u32
- Signature: gpio_readl_v2(void __iomem * reg)
- Line: 77
- Called by: rockchip_gpio_readl

### gpio_writel_v2
- Return type: static void
- Signature: gpio_writel_v2(u32 val,void __iomem * reg)
- Line: 71
- Called by: rockchip_gpio_writel

### rockchip_get_bank_data
- Return type: static int
- Signature: rockchip_get_bank_data(struct rockchip_pin_bank * bank)
- Line: 641
- Called by: rockchip_gpio_probe

### rockchip_gpio_direction_input
- Return type: static int
- Signature: rockchip_gpio_direction_input(struct gpio_chip * gc,unsigned int offset)
- Line: 259
- Calls: rockchip_gpio_set_direction
- Called by: rockchip_gpio_probe

### rockchip_gpio_direction_output
- Return type: static int
- Signature: rockchip_gpio_direction_output(struct gpio_chip * gc,unsigned int offset,int value)
- Line: 265
- Calls: rockchip_gpio_set, rockchip_gpio_set_direction
- Called by: rockchip_gpio_probe

### rockchip_gpio_exit
- Return type: static void __exit
- Signature: rockchip_gpio_exit(void)
- Line: 820

### rockchip_gpio_find_bank
- Return type: static rockchip_pin_bank *
- Signature: rockchip_gpio_find_bank(struct pinctrl_dev * pctldev,int id)
- Line: 692
- Called by: rockchip_gpio_probe

### rockchip_gpio_get
- Return type: static int
- Signature: rockchip_gpio_get(struct gpio_chip * gc,unsigned int offset)
- Line: 186
- Calls: gpiochip_get_data

### rockchip_gpio_get_direction
- Return type: static int
- Signature: rockchip_gpio_get_direction(struct gpio_chip * chip,unsigned int offset)
- Line: 146
- Calls: gpiochip_get_data, rockchip_gpio_readl_bit

### rockchip_gpio_init
- Return type: static int __init
- Signature: rockchip_gpio_init(void)
- Line: 814

### rockchip_gpio_probe
- Return type: static int
- Signature: rockchip_gpio_probe(struct platform_device * pdev)
- Line: 710
- Calls: rockchip_get_bank_data, rockchip_gpio_direction_input, rockchip_gpio_direction_output, rockchip_gpio_find_bank, rockchip_gpiolib_register

### rockchip_gpio_readl
- Return type: static u32
- Signature: rockchip_gpio_readl(struct rockchip_pin_bank * bank,unsigned int offset)
- Line: 93
- Calls: gpio_readl_v2
- Called by: rockchip_irq_set_type

### rockchip_gpio_readl_bit
- Return type: static u32
- Signature: rockchip_gpio_readl_bit(struct rockchip_pin_bank * bank,u32 bit,unsigned int offset)
- Line: 129
- Called by: rockchip_gpio_get_direction

### rockchip_gpio_remove
- Return type: static void
- Signature: rockchip_gpio_remove(struct platform_device * pdev)
- Line: 791
- Calls: gpiochip_remove

### rockchip_gpio_set
- Return type: static int
- Signature: rockchip_gpio_set(struct gpio_chip * gc,unsigned int offset,int value)
- Line: 173
- Calls: gpiochip_get_data, rockchip_gpio_writel_bit
- Called by: rockchip_gpio_direction_output

### rockchip_gpio_set_config
- Return type: static int
- Signature: rockchip_gpio_set_config(struct gpio_chip * gc,unsigned int offset,unsigned long config)
- Line: 278
- Calls: gpiochip_generic_config, rockchip_gpio_set_debounce

### rockchip_gpio_set_debounce
- Return type: static int
- Signature: rockchip_gpio_set_debounce(struct gpio_chip * gc,unsigned int offset,unsigned int debounce)
- Line: 198
- Calls: gpiochip_get_data, rockchip_gpio_writel_bit
- Called by: rockchip_gpio_set_config

### rockchip_gpio_set_direction
- Return type: static int
- Signature: rockchip_gpio_set_direction(struct gpio_chip * chip,unsigned int offset,bool input)
- Line: 159
- Calls: gpiochip_get_data, rockchip_gpio_writel_bit
- Called by: rockchip_gpio_direction_input, rockchip_gpio_direction_output

### rockchip_gpio_to_irq
- Return type: static int
- Signature: rockchip_gpio_to_irq(struct gpio_chip * gc,unsigned int offset)
- Line: 307
- Calls: gpiochip_get_data

### rockchip_gpio_writel
- Return type: static void
- Signature: rockchip_gpio_writel(struct rockchip_pin_bank * bank,u32 value,unsigned int offset)
- Line: 82
- Calls: gpio_writel_v2
- Called by: rockchip_interrupts_register, rockchip_irq_set_type

### rockchip_gpio_writel_bit
- Return type: static void
- Signature: rockchip_gpio_writel_bit(struct rockchip_pin_bank * bank,u32 bit,u32 value,unsigned int offset)
- Line: 107
- Called by: rockchip_gpio_set, rockchip_gpio_set_debounce, rockchip_gpio_set_direction, rockchip_irq_set_type

### rockchip_gpiolib_register
- Return type: static int
- Signature: rockchip_gpiolib_register(struct rockchip_pin_bank * bank)
- Line: 577
- Calls: gpiochip_remove, rockchip_interrupts_register
- Called by: rockchip_gpio_probe

### rockchip_interrupts_register
- Return type: static int
- Signature: rockchip_interrupts_register(struct rockchip_pin_bank * bank)
- Line: 513
- Calls: rockchip_gpio_writel
- Called by: rockchip_gpiolib_register

### rockchip_irq_demux
- Return type: static void
- Signature: rockchip_irq_demux(struct irq_desc * desc)
- Line: 333

### rockchip_irq_disable
- Return type: static void
- Signature: rockchip_irq_disable(struct irq_data * d)
- Line: 508

### rockchip_irq_enable
- Return type: static void
- Signature: rockchip_irq_enable(struct irq_data * d)
- Line: 503

### rockchip_irq_relres
- Return type: static void
- Signature: rockchip_irq_relres(struct irq_data * d)
- Line: 478
- Calls: gpiochip_relres_irq

### rockchip_irq_reqres
- Return type: static int
- Signature: rockchip_irq_reqres(struct irq_data * d)
- Line: 470
- Calls: gpiochip_reqres_irq

### rockchip_irq_resume
- Return type: static void
- Signature: rockchip_irq_resume(struct irq_data * d)
- Line: 495

### rockchip_irq_set_type
- Return type: static int
- Signature: rockchip_irq_set_type(struct irq_data * d,unsigned int type)
- Line: 385
- Calls: rockchip_gpio_readl, rockchip_gpio_writel, rockchip_gpio_writel_bit

### rockchip_irq_suspend
- Return type: static void
- Signature: rockchip_irq_suspend(struct irq_data * d)
- Line: 486

## Variables (5)

- static **gpio_regs_v1** : const struct rockchip_gpio_regs (line 39)
- static **gpio_regs_v2** : const struct rockchip_gpio_regs (line 53)
- static **rockchip_gpio_driver** : platform_driver (line 805)
- static **rockchip_gpio_match** : const struct of_device_id[] (line 799)
- static **rockchip_gpiolib_chip** : const struct gpio_chip (line 320)

## Macros (4)

- **GPIO_TYPE_V1** (line 34)
- **GPIO_TYPE_V2** (line 35)
- **GPIO_TYPE_V2_1** (line 36)
- **GPIO_TYPE_V2_2** (line 37)
