# drivers/gpio/gpio-lpc18xx.c

Subsystem: drivers/gpio

## Functions (15)

### lpc18xx_gpio_direction
- Return type: static int
- Signature: lpc18xx_gpio_direction(struct gpio_chip * chip,unsigned offset,bool out)
- Line: 289
- Calls: gpiochip_get_data
- Called by: lpc18xx_gpio_direction_input, lpc18xx_gpio_direction_output

### lpc18xx_gpio_direction_input
- Return type: static int
- Signature: lpc18xx_gpio_direction_input(struct gpio_chip * chip,unsigned offset)
- Line: 311
- Calls: lpc18xx_gpio_direction

### lpc18xx_gpio_direction_output
- Return type: static int
- Signature: lpc18xx_gpio_direction_output(struct gpio_chip * chip,unsigned offset,int value)
- Line: 317
- Calls: lpc18xx_gpio_direction, lpc18xx_gpio_set

### lpc18xx_gpio_get
- Return type: static int
- Signature: lpc18xx_gpio_get(struct gpio_chip * chip,unsigned offset)
- Line: 283
- Calls: gpiochip_get_data

### lpc18xx_gpio_pin_ic_domain_alloc
- Return type: static int
- Signature: lpc18xx_gpio_pin_ic_domain_alloc(struct irq_domain * domain,unsigned int virq,unsigned int nr_irqs,void * data)
- Line: 169

### lpc18xx_gpio_pin_ic_eoi
- Return type: static void
- Signature: lpc18xx_gpio_pin_ic_eoi(struct irq_data * d)
- Line: 120
- Calls: lpc18xx_gpio_pin_ic_set

### lpc18xx_gpio_pin_ic_isel
- Return type: static void
- Signature: lpc18xx_gpio_pin_ic_isel(struct lpc18xx_gpio_pin_ic * ic,u32 pin,bool set)
- Line: 55
- Called by: lpc18xx_gpio_pin_ic_set_type

### lpc18xx_gpio_pin_ic_mask
- Return type: static void
- Signature: lpc18xx_gpio_pin_ic_mask(struct irq_data * d)
- Line: 74
- Calls: gpiochip_disable_irq, lpc18xx_gpio_pin_ic_set

### lpc18xx_gpio_pin_ic_probe
- Return type: static int
- Signature: lpc18xx_gpio_pin_ic_probe(struct lpc18xx_gpio_chip * gc)
- Line: 210
- Called by: lpc18xx_gpio_probe

### lpc18xx_gpio_pin_ic_set
- Return type: static void
- Signature: lpc18xx_gpio_pin_ic_set(struct lpc18xx_gpio_pin_ic * ic,u32 pin,u32 reg)
- Line: 68
- Called by: lpc18xx_gpio_pin_ic_eoi, lpc18xx_gpio_pin_ic_mask, lpc18xx_gpio_pin_ic_set_type, lpc18xx_gpio_pin_ic_unmask

### lpc18xx_gpio_pin_ic_set_type
- Return type: static int
- Signature: lpc18xx_gpio_pin_ic_set_type(struct irq_data * d,unsigned int type)
- Line: 136
- Calls: lpc18xx_gpio_pin_ic_isel, lpc18xx_gpio_pin_ic_set

### lpc18xx_gpio_pin_ic_unmask
- Return type: static void
- Signature: lpc18xx_gpio_pin_ic_unmask(struct irq_data * d)
- Line: 97
- Calls: gpiochip_enable_irq, lpc18xx_gpio_pin_ic_set

### lpc18xx_gpio_probe
- Return type: static int
- Signature: lpc18xx_gpio_probe(struct platform_device * pdev)
- Line: 336
- Calls: lpc18xx_gpio_pin_ic_probe

### lpc18xx_gpio_remove
- Return type: static void
- Signature: lpc18xx_gpio_remove(struct platform_device * pdev)
- Line: 386

### lpc18xx_gpio_set
- Return type: static int
- Signature: lpc18xx_gpio_set(struct gpio_chip * chip,unsigned int offset,int value)
- Line: 273
- Calls: gpiochip_get_data
- Called by: lpc18xx_gpio_direction_output

## Structs (2)

### lpc18xx_gpio_chip
- Line: 48
- Members:
  - base: void __iomem *
  - domain: irq_domain *
  - lock: raw_spinlock
  - gpio: gpio_chip *
  - gpio: gpio_chip
  - base: void __iomem *
  - pin_ic: lpc18xx_gpio_pin_ic *
  - lock: spinlock_t

### lpc18xx_gpio_pin_ic
- Line: 41
- Members:
  - base: void __iomem *
  - domain: irq_domain *
  - lock: raw_spinlock
  - gpio: gpio_chip *
  - gpio: gpio_chip
  - base: void __iomem *
  - pin_ic: lpc18xx_gpio_pin_ic *
  - lock: spinlock_t

## Variables (5)

- static **lpc18xx_chip** : const struct gpio_chip (line 324)
- static **lpc18xx_gpio_driver** : platform_driver (line 400)
- static **lpc18xx_gpio_match** : const struct of_device_id[] (line 394)
- static **lpc18xx_gpio_pin_ic** : const struct irq_chip (line 159)
- static **lpc18xx_gpio_pin_ic_domain_ops** : const struct irq_domain_ops (line 204)

## Macros (14)

- **LPC18XX_GPIO_PIN_IC_CIENF** (line 34)
- **LPC18XX_GPIO_PIN_IC_CIENR** (line 31)
- **LPC18XX_GPIO_PIN_IC_FALL** (line 36)
- **LPC18XX_GPIO_PIN_IC_IENF** (line 32)
- **LPC18XX_GPIO_PIN_IC_IENR** (line 29)
- **LPC18XX_GPIO_PIN_IC_ISEL** (line 28)
- **LPC18XX_GPIO_PIN_IC_IST** (line 37)
- **LPC18XX_GPIO_PIN_IC_RISE** (line 35)
- **LPC18XX_GPIO_PIN_IC_SIENF** (line 33)
- **LPC18XX_GPIO_PIN_IC_SIENR** (line 30)
- **LPC18XX_MAX_PORTS** (line 24)
- **LPC18XX_PINS_PER_PORT** (line 25)
- **LPC18XX_REG_DIR**(n) (line 22)
- **NR_LPC18XX_GPIO_PIN_IC_IRQS** (line 39)
