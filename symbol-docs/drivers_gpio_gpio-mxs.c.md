# drivers/gpio/gpio-mxs.c

Subsystem: drivers/gpio

## Functions (10)

### is_imx23_gpio
- Return type: static int
- Signature: is_imx23_gpio(struct mxs_gpio_port * port)
- Line: 58

### mxs_flip_edge
- Return type: static void
- Signature: mxs_flip_edge(struct mxs_gpio_port * port,u32 gpio)
- Line: 127
- Called by: mxs_gpio_irq_handler

### mxs_gpio_get_direction
- Return type: static int
- Signature: mxs_gpio_get_direction(struct gpio_chip * gc,unsigned int offset)
- Line: 239
- Calls: gpiochip_get_data

### mxs_gpio_init
- Return type: static int __init
- Signature: mxs_gpio_init(void)
- Line: 363

### mxs_gpio_init_gc
- Return type: static int
- Signature: mxs_gpio_init_gc(struct mxs_gpio_port * port,int irq_base)
- Line: 187
- Called by: mxs_gpio_probe

### mxs_gpio_irq_handler
- Return type: static void
- Signature: mxs_gpio_irq_handler(struct irq_desc * desc)
- Line: 145
- Calls: mxs_flip_edge

### mxs_gpio_probe
- Return type: static int
- Signature: mxs_gpio_probe(struct platform_device * pdev)
- Line: 259
- Calls: gpio_generic_chip_init, mxs_gpio_init_gc

### mxs_gpio_set_irq_type
- Return type: static int
- Signature: mxs_gpio_set_irq_type(struct irq_data * d,unsigned int type)
- Line: 65

### mxs_gpio_set_wake_irq
- Return type: static int
- Signature: mxs_gpio_set_wake_irq(struct irq_data * d,unsigned int enable)
- Line: 174

### mxs_gpio_to_irq
- Return type: static int
- Signature: mxs_gpio_to_irq(struct gpio_chip * gc,unsigned int offset)
- Line: 232
- Calls: gpiochip_get_data

## Structs (1)

### mxs_gpio_port
- Line: 47
- Members:
  - base: void __iomem *
  - id: int
  - irq: int
  - domain: irq_domain *
  - chip: gpio_generic_chip
  - dev: device *
  - devid: mxs_gpio_id
  - both_edges: u32

## Enums (1)

### mxs_gpio_id
- Line: 42

## Variables (2)

- static **mxs_gpio_driver** : platform_driver (line 354)
- static **mxs_gpio_dt_ids** : const struct of_device_id[] (line 252)

## Macros (16)

- **GPIO_INT_FALL_EDGE** (line 35)
- **GPIO_INT_HIGH_LEV** (line 38)
- **GPIO_INT_LEV_MASK** (line 39)
- **GPIO_INT_LOW_LEV** (line 36)
- **GPIO_INT_POL_MASK** (line 40)
- **GPIO_INT_RISE_EDGE** (line 37)
- **MXS_CLR** (line 24)
- **MXS_SET** (line 23)
- **PINCTRL_DIN**(p) (line 27)
- **PINCTRL_DOE**(p) (line 28)
- **PINCTRL_DOUT**(p) (line 26)
- **PINCTRL_IRQEN**(p) (line 30)
- **PINCTRL_IRQLEV**(p) (line 31)
- **PINCTRL_IRQPOL**(p) (line 32)
- **PINCTRL_IRQSTAT**(p) (line 33)
- **PINCTRL_PIN2IRQ**(p) (line 29)
