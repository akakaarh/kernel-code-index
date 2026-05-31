# drivers/gpio/gpio-mt7621.c

Subsystem: drivers/gpio

## Functions (10)

### mediatek_gpio_bank_probe
- Return type: static int
- Signature: mediatek_gpio_bank_probe(struct device * dev,int bank)
- Line: 220
- Calls: gpio_generic_chip_init, mtk_gpio_w32
- Called by: mediatek_gpio_probe

### mediatek_gpio_irq_handler
- Return type: static irqreturn_t
- Signature: mediatek_gpio_irq_handler(int irq,void * data)
- Line: 87
- Calls: mtk_gpio_r32, mtk_gpio_w32, to_mediatek_gpio

### mediatek_gpio_irq_mask
- Return type: static void
- Signature: mediatek_gpio_irq_mask(struct irq_data * d)
- Line: 129
- Calls: gpiochip_disable_irq, mtk_gpio_r32, mtk_gpio_w32, to_mediatek_gpio

### mediatek_gpio_irq_type
- Return type: static int
- Signature: mediatek_gpio_irq_type(struct irq_data * d,unsigned int type)
- Line: 151
- Calls: to_mediatek_gpio

### mediatek_gpio_irq_unmask
- Return type: static void
- Signature: mediatek_gpio_irq_unmask(struct irq_data * d)
- Line: 107
- Calls: gpiochip_enable_irq, mtk_gpio_r32, mtk_gpio_w32, to_mediatek_gpio

### mediatek_gpio_probe
- Return type: static int
- Signature: mediatek_gpio_probe(struct platform_device * pdev)
- Line: 306
- Calls: mediatek_gpio_bank_probe

### mediatek_gpio_xlate
- Return type: static int
- Signature: mediatek_gpio_xlate(struct gpio_chip * chip,const struct of_phandle_args * spec,u32 * flags)
- Line: 194
- Calls: to_mediatek_gpio

### mtk_gpio_r32
- Return type: static u32
- Signature: mtk_gpio_r32(struct mtk_gc * rg,u32 offset)
- Line: 77
- Calls: gpiochip_get_data
- Called by: mediatek_gpio_irq_handler, mediatek_gpio_irq_mask, mediatek_gpio_irq_unmask

### mtk_gpio_w32
- Return type: static void
- Signature: mtk_gpio_w32(struct mtk_gc * rg,u32 offset,u32 val)
- Line: 67
- Calls: gpiochip_get_data
- Called by: mediatek_gpio_bank_probe, mediatek_gpio_irq_handler, mediatek_gpio_irq_mask, mediatek_gpio_irq_unmask

### to_mediatek_gpio
- Return type: static mtk_gc *
- Signature: to_mediatek_gpio(struct gpio_chip * chip)
- Line: 59
- Called by: mediatek_gpio_irq_handler, mediatek_gpio_irq_mask, mediatek_gpio_irq_type, mediatek_gpio_irq_unmask, mediatek_gpio_xlate

## Structs (2)

### mtk
- Line: 51
- Members:
  - irq_chip: irq_chip
  - chip: gpio_generic_chip
  - bank: int
  - rising: u32
  - falling: u32
  - hlevel: u32
  - llevel: u32
  - dev: device *
  - base: void __iomem *
  - gpio_irq: int
  - gc_map: mtk_gc[]

### mtk_gc
- Line: 31
- Members:
  - irq_chip: irq_chip
  - chip: gpio_generic_chip
  - bank: int
  - rising: u32
  - falling: u32
  - hlevel: u32
  - llevel: u32
  - dev: device *
  - base: void __iomem *
  - gpio_irq: int
  - gc_map: mtk_gc[]

## Variables (3)

- static **mediatek_gpio_driver** : platform_driver (line 343)
- static **mediatek_gpio_match** : const struct of_device_id[] (line 337)
- static **mt7621_irq_chip** : const struct irq_chip (line 209)

## Macros (14)

- **GPIO_BANK_STRIDE** (line 18)
- **GPIO_REG_CTRL** (line 19)
- **GPIO_REG_DATA** (line 21)
- **GPIO_REG_DCLR** (line 23)
- **GPIO_REG_DSET** (line 22)
- **GPIO_REG_EDGE** (line 29)
- **GPIO_REG_FEDGE** (line 25)
- **GPIO_REG_HLVL** (line 26)
- **GPIO_REG_LLVL** (line 27)
- **GPIO_REG_POL** (line 20)
- **GPIO_REG_REDGE** (line 24)
- **GPIO_REG_STAT** (line 28)
- **MTK_BANK_CNT** (line 15)
- **MTK_BANK_WIDTH** (line 16)
