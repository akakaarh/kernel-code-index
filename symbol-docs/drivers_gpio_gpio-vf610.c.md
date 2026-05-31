# drivers/gpio/gpio-vf610.c

Subsystem: drivers/gpio

## Functions (10)

### vf610_gpio_disable_clk
- Return type: static void
- Signature: vf610_gpio_disable_clk(void * data)
- Line: 211

### vf610_gpio_irq_ack
- Return type: static void
- Signature: vf610_gpio_irq_ack(struct irq_data * d)
- Line: 118
- Calls: gpiochip_get_data, vf610_gpio_writel

### vf610_gpio_irq_handler
- Return type: static void
- Signature: vf610_gpio_irq_handler(struct irq_desc * desc)
- Line: 97
- Calls: gpiochip_get_data, vf610_gpio_readl, vf610_gpio_writel

### vf610_gpio_irq_mask
- Return type: static void
- Signature: vf610_gpio_irq_mask(struct irq_data * d)
- Line: 163
- Calls: gpiochip_disable_irq, gpiochip_get_data, vf610_gpio_writel

### vf610_gpio_irq_set_type
- Return type: static int
- Signature: vf610_gpio_irq_set_type(struct irq_data * d,u32 type)
- Line: 127
- Calls: gpiochip_get_data

### vf610_gpio_irq_set_wake
- Return type: static int
- Signature: vf610_gpio_irq_set_wake(struct irq_data * d,u32 enable)
- Line: 186
- Calls: gpiochip_get_data

### vf610_gpio_irq_unmask
- Return type: static void
- Signature: vf610_gpio_irq_unmask(struct irq_data * d)
- Line: 174
- Calls: gpiochip_enable_irq, gpiochip_get_data, vf610_gpio_writel

### vf610_gpio_probe
- Return type: static int
- Signature: vf610_gpio_probe(struct platform_device * pdev)
- Line: 216
- Calls: gpio_generic_chip_init, vf610_gpio_writel

### vf610_gpio_readl
- Return type: static u32
- Signature: vf610_gpio_readl(void __iomem * reg)
- Line: 92
- Called by: vf610_gpio_irq_handler

### vf610_gpio_writel
- Return type: static void
- Signature: vf610_gpio_writel(u32 val,void __iomem * reg)
- Line: 87
- Called by: vf610_gpio_irq_ack, vf610_gpio_irq_handler, vf610_gpio_irq_mask, vf610_gpio_irq_unmask, vf610_gpio_probe

## Structs (2)

### fsl_gpio_soc_data
- Line: 25
- Members:
  - have_paddr: bool
  - have_dual_base: bool
  - chip: gpio_generic_chip
  - base: void __iomem *
  - gpio_base: void __iomem *
  - sdata: const struct fsl_gpio_soc_data *
  - irqc: u8[]
  - clk_port: clk *
  - clk_gpio: clk *
  - irq: int

### vf610_gpio_port
- Line: 31
- Members:
  - have_paddr: bool
  - have_dual_base: bool
  - chip: gpio_generic_chip
  - base: void __iomem *
  - gpio_base: void __iomem *
  - sdata: const struct fsl_gpio_soc_data *
  - irqc: u8[]
  - clk_port: clk *
  - clk_gpio: clk *
  - irq: int

## Variables (6)

- static **imx8ulp_data** : const struct fsl_gpio_soc_data (line 76)
- static **imx_data** : const struct fsl_gpio_soc_data (line 71)
- static **vf610_data** : const struct fsl_gpio_soc_data (line 67)
- static **vf610_gpio_driver** : platform_driver (line 347)
- static **vf610_gpio_dt_ids** : const struct of_device_id[] (line 80)
- static **vf610_irqchip** : const struct irq_chip (line 199)

## Macros (21)

- **GPIO_PCOR** (line 44)
- **GPIO_PDDR** (line 47)
- **GPIO_PDIR** (line 46)
- **GPIO_PDOR** (line 42)
- **GPIO_PSOR** (line 43)
- **GPIO_PTOR** (line 45)
- **IMX8ULP_BASE_OFF** (line 65)
- **IMX8ULP_GPIO_BASE_OFF** (line 64)
- **PORT_DFCR** (line 54)
- **PORT_DFER** (line 53)
- **PORT_DFWR** (line 55)
- **PORT_INT_EITHER_EDGE** (line 61)
- **PORT_INT_FALLING_EDGE** (line 60)
- **PORT_INT_LOGIC_ONE** (line 62)
- **PORT_INT_LOGIC_ZERO** (line 58)
- **PORT_INT_OFF** (line 57)
- **PORT_INT_RISING_EDGE** (line 59)
- **PORT_ISFR** (line 52)
- **PORT_PCR**(n) (line 49)
- **PORT_PCR_IRQC_OFFSET** (line 50)
- **VF610_GPIO_PER_PORT** (line 23)
