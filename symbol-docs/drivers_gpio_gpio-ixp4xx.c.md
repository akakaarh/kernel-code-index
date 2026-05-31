# drivers/gpio/gpio-ixp4xx.c

Subsystem: drivers/gpio

## Functions (6)

### ixp4xx_gpio_child_to_parent_hwirq
- Return type: static int
- Signature: ixp4xx_gpio_child_to_parent_hwirq(struct gpio_chip * gc,unsigned int child,unsigned int child_type,unsigned int * parent,unsigned int * parent_type)
- Line: 180

### ixp4xx_gpio_irq_ack
- Return type: static void
- Signature: ixp4xx_gpio_irq_ack(struct irq_data * d)
- Line: 70
- Calls: gpiochip_get_data
- Called by: ixp4xx_gpio_irq_unmask

### ixp4xx_gpio_irq_set_type
- Return type: static int
- Signature: ixp4xx_gpio_irq_set_type(struct irq_data * d,unsigned int type)
- Line: 99
- Calls: gpiochip_get_data

### ixp4xx_gpio_irq_unmask
- Return type: static void
- Signature: ixp4xx_gpio_irq_unmask(struct irq_data * d)
- Line: 86
- Calls: gpiochip_enable_irq, gpiochip_get_data, ixp4xx_gpio_irq_ack

### ixp4xx_gpio_mask_irq
- Return type: static void
- Signature: ixp4xx_gpio_mask_irq(struct irq_data * d)
- Line: 78
- Calls: gpiochip_disable_irq

### ixp4xx_gpio_probe
- Return type: static int
- Signature: ixp4xx_gpio_probe(struct platform_device * pdev)
- Line: 205
- Calls: gpio_generic_chip_init

## Structs (1)

### ixp4xx_gpio
- Line: 63
- Members:
  - chip: gpio_generic_chip
  - dev: device *
  - base: void __iomem *
  - irq_edge: unsigned long long

## Variables (3)

- static **ixp4xx_gpio_driver** : platform_driver (line 351)
- static **ixp4xx_gpio_irqchip** : const struct irq_chip (line 170)
- static **ixp4xx_gpio_of_match** : const struct of_device_id[] (line 343)

## Macros (23)

- **IXP4XX_GPCLK_CLK0DC_SHIFT** (line 46)
- **IXP4XX_GPCLK_CLK0TC_SHIFT** (line 47)
- **IXP4XX_GPCLK_CLK0_MASK** (line 48)
- **IXP4XX_GPCLK_CLK1DC_SHIFT** (line 50)
- **IXP4XX_GPCLK_CLK1TC_SHIFT** (line 51)
- **IXP4XX_GPCLK_CLK1_MASK** (line 52)
- **IXP4XX_GPCLK_MUX14** (line 49)
- **IXP4XX_GPCLK_MUX15** (line 53)
- **IXP4XX_GPIO_STYLE_ACTIVE_HIGH** (line 35)
- **IXP4XX_GPIO_STYLE_ACTIVE_LOW** (line 36)
- **IXP4XX_GPIO_STYLE_FALLING_EDGE** (line 38)
- **IXP4XX_GPIO_STYLE_MASK** (line 40)
- **IXP4XX_GPIO_STYLE_RISING_EDGE** (line 37)
- **IXP4XX_GPIO_STYLE_SIZE** (line 41)
- **IXP4XX_GPIO_STYLE_TRANSITIONAL** (line 39)
- **IXP4XX_REG_GPCLK** (line 26)
- **IXP4XX_REG_GPDBSEL** (line 27)
- **IXP4XX_REG_GPIN** (line 22)
- **IXP4XX_REG_GPIS** (line 23)
- **IXP4XX_REG_GPIT1** (line 24)
- **IXP4XX_REG_GPIT2** (line 25)
- **IXP4XX_REG_GPOE** (line 21)
- **IXP4XX_REG_GPOUT** (line 20)
