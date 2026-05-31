# drivers/gpio/gpio-davinci.c

Subsystem: drivers/gpio

## Functions (25)

### __davinci_direction
- Return type: static int
- Signature: __davinci_direction(struct gpio_chip * chip,unsigned offset,bool out,int value)
- Line: 77
- Calls: __gpio_mask, gpiochip_get_data
- Called by: davinci_direction_in, davinci_direction_out

### __gpio_mask
- Return type: static u32
- Signature: __gpio_mask(unsigned gpio)
- Line: 67
- Called by: __davinci_direction, davinci_get_direction, davinci_gpio_get, davinci_gpio_irq_map, davinci_gpio_set, gpio_irq_type_unbanked

### davinci_direction_in
- Return type: static int
- Signature: davinci_direction_in(struct gpio_chip * chip,unsigned offset)
- Line: 102
- Calls: __davinci_direction

### davinci_direction_out
- Return type: static int
- Signature: davinci_direction_out(struct gpio_chip * chip,unsigned offset,int value)
- Line: 108
- Calls: __davinci_direction

### davinci_get_direction
- Return type: static int
- Signature: davinci_get_direction(struct gpio_chip * chip,unsigned int offset)
- Line: 113
- Calls: __gpio_mask, gpiochip_get_data

### davinci_gpio_drv_reg
- Return type: static int __init
- Signature: davinci_gpio_drv_reg(void)
- Line: 689

### davinci_gpio_exit
- Return type: static void __exit
- Signature: davinci_gpio_exit(void)
- Line: 695

### davinci_gpio_get
- Return type: static int
- Signature: davinci_gpio_get(struct gpio_chip * chip,unsigned offset)
- Line: 136
- Calls: __gpio_mask, gpiochip_get_data

### davinci_gpio_get_irq_chip
- Return type: static irq_chip *
- Signature: davinci_gpio_get_irq_chip(unsigned int irq)
- Line: 435

### davinci_gpio_irq_map
- Return type: static int
- Signature: davinci_gpio_irq_map(struct irq_domain * d,unsigned int irq,irq_hw_number_t hw)
- Line: 415
- Calls: __gpio_mask

### davinci_gpio_irq_setup
- Return type: static int
- Signature: davinci_gpio_irq_setup(struct platform_device * pdev)
- Line: 462
- Called by: davinci_gpio_probe

### davinci_gpio_probe
- Return type: static int
- Signature: davinci_gpio_probe(struct platform_device * pdev)
- Line: 165
- Calls: davinci_gpio_irq_setup

### davinci_gpio_restore_context
- Return type: static void
- Signature: davinci_gpio_restore_context(struct davinci_gpio_controller * chips,u32 nbank)
- Line: 618
- Called by: davinci_gpio_resume

### davinci_gpio_resume
- Return type: static int
- Signature: davinci_gpio_resume(struct device * dev)
- Line: 655
- Calls: davinci_gpio_restore_context

### davinci_gpio_save_context
- Return type: static void
- Signature: davinci_gpio_save_context(struct davinci_gpio_controller * chips,u32 nbank)
- Line: 594
- Called by: davinci_gpio_suspend

### davinci_gpio_set
- Return type: static int
- Signature: davinci_gpio_set(struct gpio_chip * chip,unsigned offset,int value)
- Line: 151
- Calls: __gpio_mask, gpiochip_get_data

### davinci_gpio_suspend
- Return type: static int
- Signature: davinci_gpio_suspend(struct device * dev)
- Line: 645
- Calls: davinci_gpio_save_context

### gpio_irq_handler
- Return type: static void
- Signature: gpio_irq_handler(struct irq_desc * desc)
- Line: 315

### gpio_irq_mask
- Return type: static void
- Signature: gpio_irq_mask(struct irq_data * d)
- Line: 265
- Calls: gpiochip_disable_irq

### gpio_irq_type
- Return type: static int
- Signature: gpio_irq_type(struct irq_data * d,unsigned trigger)
- Line: 298

### gpio_irq_type_unbanked
- Return type: static int
- Signature: gpio_irq_type_unbanked(struct irq_data * data,unsigned trigger)
- Line: 386
- Calls: __gpio_mask

### gpio_irq_unmask
- Return type: static void
- Signature: gpio_irq_unmask(struct irq_data * d)
- Line: 278
- Calls: gpiochip_enable_irq

### gpio_to_irq_banked
- Return type: static int
- Signature: gpio_to_irq_banked(struct gpio_chip * chip,unsigned offset)
- Line: 362
- Calls: gpiochip_get_data

### gpio_to_irq_unbanked
- Return type: static int
- Signature: gpio_to_irq_unbanked(struct gpio_chip * chip,unsigned offset)
- Line: 372
- Calls: gpiochip_get_data

### keystone_gpio_get_irq_chip
- Return type: static irq_chip *
- Signature: keystone_gpio_get_irq_chip(unsigned int irq)
- Line: 444

## Structs (3)

### davinci_gpio_controller
- Line: 55
- Members:
  - dir: u32
  - out_data: u32
  - set_data: u32
  - clr_data: u32
  - in_data: u32
  - set_rising: u32
  - clr_rising: u32
  - set_falling: u32
  - clr_falling: u32
  - intstat: u32
  - regs: void __iomem *
  - chip: davinci_gpio_controller *
  - bank_num: int
  - chip: gpio_chip
  - irq_domain: irq_domain *
  - lock: spinlock_t
  - regs: void __iomem * []
  - gpio_unbanked: int
  - irqs: int[]
  - context: davinci_gpio_regs[]
  - binten_context: u32

### davinci_gpio_irq_data
- Line: 49
- Members:
  - dir: u32
  - out_data: u32
  - set_data: u32
  - clr_data: u32
  - in_data: u32
  - set_rising: u32
  - clr_rising: u32
  - set_falling: u32
  - clr_falling: u32
  - intstat: u32
  - regs: void __iomem *
  - chip: davinci_gpio_controller *
  - bank_num: int
  - chip: gpio_chip
  - irq_domain: irq_domain *
  - lock: spinlock_t
  - regs: void __iomem * []
  - gpio_unbanked: int
  - irqs: int[]
  - context: davinci_gpio_regs[]
  - binten_context: u32

### davinci_gpio_regs
- Line: 29
- Members:
  - dir: u32
  - out_data: u32
  - set_data: u32
  - clr_data: u32
  - in_data: u32
  - set_rising: u32
  - clr_rising: u32
  - set_falling: u32
  - clr_falling: u32
  - intstat: u32
  - regs: void __iomem *
  - chip: davinci_gpio_controller *
  - bank_num: int
  - chip: gpio_chip
  - irq_domain: irq_domain *
  - lock: spinlock_t
  - regs: void __iomem * []
  - gpio_unbanked: int
  - irqs: int[]
  - context: davinci_gpio_regs[]
  - binten_context: u32

## Typedefs (1)

- **gpio_get_irq_chip_cb_t** → irq_chip * (*)(unsigned int irq) (line 42)

## Variables (7)

- static **davinci_gpio_driver** : platform_driver (line 676)
- static **davinci_gpio_ids** : const struct of_device_id[] (line 668)
- static **davinci_gpio_ids** : const struct of_device_id[] (line 452)
- static **davinci_gpio_irq_ops** : const struct irq_domain_ops (line 430)
- static **gpio_base** : void __iomem * (line 46)
- static **gpio_irqchip** : const struct irq_chip (line 306)
- static **offset_array** : unsigned int[5] (line 47)

## Macros (3)

- **BINTEN** (line 44)
- **MAX_INT_PER_BANK** (line 27)
- **MAX_REGS_BANKS** (line 26)
