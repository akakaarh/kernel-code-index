# drivers/gpio/gpio-hlwd.c

Subsystem: drivers/gpio

## Functions (9)

### hlwd_gpio_irq_ack
- Return type: static void
- Signature: hlwd_gpio_irq_ack(struct irq_data * data)
- Line: 107
- Calls: gpiochip_get_data
- Called by: hlwd_gpio_irq_enable

### hlwd_gpio_irq_enable
- Return type: static void
- Signature: hlwd_gpio_irq_enable(struct irq_data * data)
- Line: 144
- Calls: hlwd_gpio_irq_ack, hlwd_gpio_irq_unmask

### hlwd_gpio_irq_mask
- Return type: static void
- Signature: hlwd_gpio_irq_mask(struct irq_data * data)
- Line: 115
- Calls: gpiochip_disable_irq, gpiochip_get_data

### hlwd_gpio_irq_print_chip
- Return type: static void
- Signature: hlwd_gpio_irq_print_chip(struct irq_data * data,struct seq_file * p)
- Line: 204
- Calls: gpiochip_get_data

### hlwd_gpio_irq_set_type
- Return type: static int
- Signature: hlwd_gpio_irq_set_type(struct irq_data * data,unsigned int flow_type)
- Line: 171
- Calls: gpiochip_get_data, hlwd_gpio_irq_setup_emulation

### hlwd_gpio_irq_setup_emulation
- Return type: static void
- Signature: hlwd_gpio_irq_setup_emulation(struct hlwd_gpio * hlwd,int hwirq,unsigned int flow_type)
- Line: 150
- Called by: hlwd_gpio_irq_set_type

### hlwd_gpio_irq_unmask
- Return type: static void
- Signature: hlwd_gpio_irq_unmask(struct irq_data * data)
- Line: 129
- Calls: gpiochip_enable_irq, gpiochip_get_data
- Called by: hlwd_gpio_irq_enable

### hlwd_gpio_irqhandler
- Return type: static void
- Signature: hlwd_gpio_irqhandler(struct irq_desc * desc)
- Line: 60
- Calls: gpiochip_get_data

### hlwd_gpio_probe
- Return type: static int
- Signature: hlwd_gpio_probe(struct platform_device * pdev)
- Line: 222
- Calls: gpio_generic_chip_init

## Structs (1)

### hlwd_gpio
- Line: 51
- Members:
  - gpioc: gpio_generic_chip
  - dev: device *
  - regs: void __iomem *
  - irq: int
  - edge_emulation: u32
  - falling_edge: u32
  - rising_edge: u32

## Variables (3)

- static **hlwd_gpio_driver** : platform_driver (line 311)
- static **hlwd_gpio_irq_chip** : const struct irq_chip (line 212)
- static **hlwd_gpio_match** : const struct of_device_id[] (line 305)

## Macros (16)

- **HW_GPIOB_DIR** (line 35)
- **HW_GPIOB_IN** (line 36)
- **HW_GPIOB_INMIR** (line 40)
- **HW_GPIOB_INTFLAG** (line 38)
- **HW_GPIOB_INTLVL** (line 37)
- **HW_GPIOB_INTMASK** (line 39)
- **HW_GPIOB_OUT** (line 34)
- **HW_GPIO_DIR** (line 43)
- **HW_GPIO_ENABLE** (line 41)
- **HW_GPIO_IN** (line 44)
- **HW_GPIO_INMIR** (line 48)
- **HW_GPIO_INTFLAG** (line 46)
- **HW_GPIO_INTLVL** (line 45)
- **HW_GPIO_INTMASK** (line 47)
- **HW_GPIO_OUT** (line 42)
- **HW_GPIO_OWNER** (line 49)
