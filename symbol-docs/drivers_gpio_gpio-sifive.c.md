# drivers/gpio/gpio-sifive.c

Subsystem: drivers/gpio

## Functions (8)

### sifive_gpio_child_to_parent_hwirq
- Return type: static int
- Signature: sifive_gpio_child_to_parent_hwirq(struct gpio_chip * gc,unsigned int child,unsigned int child_type,unsigned int * parent,unsigned int * parent_type)
- Line: 156
- Calls: gpiochip_get_data

### sifive_gpio_irq_disable
- Return type: static void
- Signature: sifive_gpio_irq_disable(struct irq_data * d)
- Line: 101
- Calls: gpiochip_disable_irq, gpiochip_get_data, sifive_gpio_set_ie

### sifive_gpio_irq_enable
- Return type: static void
- Signature: sifive_gpio_irq_enable(struct irq_data * d)
- Line: 74
- Calls: gpiochip_enable_irq, gpiochip_get_data, sifive_gpio_set_ie

### sifive_gpio_irq_eoi
- Return type: static void
- Signature: sifive_gpio_irq_eoi(struct irq_data * d)
- Line: 114
- Calls: gpiochip_get_data

### sifive_gpio_irq_set_affinity
- Return type: static int
- Signature: sifive_gpio_irq_set_affinity(struct irq_data * data,const struct cpumask * dest,bool force)
- Line: 132

### sifive_gpio_irq_set_type
- Return type: static int
- Signature: sifive_gpio_irq_set_type(struct irq_data * d,unsigned int trigger)
- Line: 60
- Calls: gpiochip_get_data, sifive_gpio_set_ie

### sifive_gpio_probe
- Return type: static int
- Signature: sifive_gpio_probe(struct platform_device * pdev)
- Line: 178
- Calls: gpio_generic_chip_init

### sifive_gpio_set_ie
- Return type: static void
- Signature: sifive_gpio_set_ie(struct sifive_gpio * chip,unsigned int offset)
- Line: 43
- Called by: sifive_gpio_irq_disable, sifive_gpio_irq_enable, sifive_gpio_irq_set_type

## Structs (1)

### sifive_gpio
- Line: 34
- Members:
  - base: void __iomem *
  - gen_gc: gpio_generic_chip
  - regs: regmap *
  - irq_state: unsigned long
  - trigger: unsigned int[]
  - irq_number: unsigned int[]

## Variables (4)

- static **sifive_gpio_driver** : platform_driver (line 264)
- static **sifive_gpio_irqchip** : const struct irq_chip (line 142)
- static **sifive_gpio_match** : const struct of_device_id[] (line 258)
- static **sifive_gpio_regmap_config** : const struct regmap_config (line 171)

## Macros (14)

- **SIFIVE_GPIO_FALL_IE** (line 24)
- **SIFIVE_GPIO_FALL_IP** (line 25)
- **SIFIVE_GPIO_HIGH_IE** (line 26)
- **SIFIVE_GPIO_HIGH_IP** (line 27)
- **SIFIVE_GPIO_INPUT_EN** (line 19)
- **SIFIVE_GPIO_INPUT_VAL** (line 18)
- **SIFIVE_GPIO_LOW_IE** (line 28)
- **SIFIVE_GPIO_LOW_IP** (line 29)
- **SIFIVE_GPIO_MAX** (line 32)
- **SIFIVE_GPIO_OUTPUT_EN** (line 20)
- **SIFIVE_GPIO_OUTPUT_VAL** (line 21)
- **SIFIVE_GPIO_OUTPUT_XOR** (line 30)
- **SIFIVE_GPIO_RISE_IE** (line 22)
- **SIFIVE_GPIO_RISE_IP** (line 23)
