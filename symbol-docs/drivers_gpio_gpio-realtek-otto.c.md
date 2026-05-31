# drivers/gpio/gpio-realtek-otto.c

Subsystem: drivers/gpio

## Functions (19)

### irq_data_to_ctrl
- Return type: static realtek_gpio_ctrl *
- Signature: irq_data_to_ctrl(struct irq_data * data)
- Line: 101
- Called by: realtek_gpio_irq_ack, realtek_gpio_irq_mask, realtek_gpio_irq_set_affinity, realtek_gpio_irq_set_type, realtek_gpio_irq_unmask

### realtek_gpio_bank_read
- Return type: static u32
- Signature: realtek_gpio_bank_read(void __iomem * reg)
- Line: 142

### realtek_gpio_bank_read_swapped
- Return type: static u32
- Signature: realtek_gpio_bank_read_swapped(void __iomem * reg)
- Line: 116

### realtek_gpio_bank_write
- Return type: static void
- Signature: realtek_gpio_bank_write(void __iomem * reg,u32 value)
- Line: 147

### realtek_gpio_bank_write_swapped
- Return type: static void
- Signature: realtek_gpio_bank_write_swapped(void __iomem * reg,u32 value)
- Line: 121

### realtek_gpio_clear_isr
- Return type: static void
- Signature: realtek_gpio_clear_isr(struct realtek_gpio_ctrl * ctrl,u32 mask)
- Line: 157
- Called by: realtek_gpio_irq_ack, realtek_gpio_irq_init

### realtek_gpio_irq_ack
- Return type: static void
- Signature: realtek_gpio_irq_ack(struct irq_data * data)
- Line: 184
- Calls: irq_data_to_ctrl, realtek_gpio_clear_isr

### realtek_gpio_irq_cpu_mask
- Return type: static void __iomem *
- Signature: realtek_gpio_irq_cpu_mask(struct realtek_gpio_ctrl * ctrl,int cpu)
- Line: 268
- Called by: realtek_gpio_irq_init, realtek_gpio_irq_set_affinity

### realtek_gpio_irq_handler
- Return type: static void
- Signature: realtek_gpio_irq_handler(struct irq_desc * desc)
- Line: 251
- Calls: gpiochip_get_data, realtek_gpio_read_isr

### realtek_gpio_irq_init
- Return type: static int
- Signature: realtek_gpio_irq_init(struct gpio_chip * gc)
- Line: 307
- Calls: gpiochip_get_data, realtek_gpio_clear_isr, realtek_gpio_irq_cpu_mask, realtek_gpio_update_line_imr

### realtek_gpio_irq_mask
- Return type: static void
- Signature: realtek_gpio_irq_mask(struct irq_data * data)
- Line: 206
- Calls: gpiochip_disable_irq, irq_data_to_ctrl, realtek_gpio_update_line_imr

### realtek_gpio_irq_set_affinity
- Return type: static int
- Signature: realtek_gpio_irq_set_affinity(struct irq_data * data,const struct cpumask * dest,bool force)
- Line: 273
- Calls: irq_data_to_ctrl, realtek_gpio_irq_cpu_mask

### realtek_gpio_irq_set_type
- Return type: static int
- Signature: realtek_gpio_irq_set_type(struct irq_data * data,unsigned int flow_type)
- Line: 220
- Calls: irq_data_to_ctrl, realtek_gpio_update_line_imr

### realtek_gpio_irq_unmask
- Return type: static void
- Signature: realtek_gpio_irq_unmask(struct irq_data * data)
- Line: 192
- Calls: gpiochip_enable_irq, irq_data_to_ctrl, realtek_gpio_update_line_imr

### realtek_gpio_line_imr_pos
- Return type: static unsigned int
- Signature: realtek_gpio_line_imr_pos(unsigned int line)
- Line: 152

### realtek_gpio_line_imr_pos_swapped
- Return type: static unsigned int
- Signature: realtek_gpio_line_imr_pos_swapped(unsigned int line)
- Line: 126

### realtek_gpio_probe
- Return type: static int
- Signature: realtek_gpio_probe(struct platform_device * pdev)
- Line: 362
- Calls: gpio_generic_chip_init

### realtek_gpio_read_isr
- Return type: static u32
- Signature: realtek_gpio_read_isr(struct realtek_gpio_ctrl * ctrl)
- Line: 162
- Called by: realtek_gpio_irq_handler

### realtek_gpio_update_line_imr
- Return type: static void
- Signature: realtek_gpio_update_line_imr(struct realtek_gpio_ctrl * ctrl,unsigned int line)
- Line: 168
- Called by: realtek_gpio_irq_init, realtek_gpio_irq_mask, realtek_gpio_irq_set_type, realtek_gpio_irq_unmask

## Structs (1)

### realtek_gpio_ctrl
- Line: 67
- Members:
  - chip: gpio_generic_chip
  - base: void __iomem *
  - cpumask_base: void __iomem *
  - cpu_irq_maskable: cpumask
  - lock: raw_spinlock_t
  - intr_mask: u8[]
  - intr_type: u8[]
  - bank_read: u32 (*)(void __iomem * reg)
  - bank_write: void (*)(void __iomem * reg,u32 value)
  - line_imr_pos: unsigned int (*)(unsigned int line)

## Enums (1)

### realtek_gpio_flags
- Line: 81

## Variables (3)

- static **realtek_gpio_driver** : platform_driver (line 458)
- static **realtek_gpio_irq_chip** : const struct irq_chip (line 325)
- static **realtek_gpio_of_match** : const struct of_device_id[] (line 336)

## Macros (13)

- **REALTEK_GPIO_IMR_LINE_MASK** (line 34)
- **REALTEK_GPIO_IRQ_EDGE_BOTH** (line 37)
- **REALTEK_GPIO_IRQ_EDGE_FALLING** (line 35)
- **REALTEK_GPIO_IRQ_EDGE_RISING** (line 36)
- **REALTEK_GPIO_MAX** (line 39)
- **REALTEK_GPIO_PORTS_PER_BANK** (line 40)
- **REALTEK_GPIO_REG_CNR** (line 24)
- **REALTEK_GPIO_REG_DATA** (line 27)
- **REALTEK_GPIO_REG_DIR** (line 26)
- **REALTEK_GPIO_REG_IMR** (line 31)
- **REALTEK_GPIO_REG_IMR_AB** (line 32)
- **REALTEK_GPIO_REG_IMR_CD** (line 33)
- **REALTEK_GPIO_REG_ISR** (line 29)
