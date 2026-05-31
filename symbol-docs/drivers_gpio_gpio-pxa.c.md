# drivers/gpio/gpio-pxa.c

Subsystem: drivers/gpio

## Functions (32)

### __gpio_is_inverted
- Return type: static int
- Signature: __gpio_is_inverted(int gpio)
- Line: 181
- Called by: __gpio_is_occupied, pxa_gpio_direction_input, pxa_gpio_direction_output, pxa_gpio_irq_type

### __gpio_is_occupied
- Return type: static int
- Signature: __gpio_is_occupied(struct pxa_gpio_chip * pchip,unsigned gpio)
- Line: 194
- Calls: __gpio_is_inverted, gpio_bank_base
- Called by: pxa_gpio_irq_type

### chip_to_pxachip
- Return type: static pxa_gpio_chip *
- Signature: chip_to_pxachip(struct gpio_chip * c)
- Line: 152
- Calls: gpiochip_get_data
- Called by: gpio_to_pxabank, pxa_gpio_to_irq

### gpio_bank_base
- Return type: static void __iomem *
- Signature: gpio_bank_base(struct gpio_chip * c,int gpio)
- Line: 159
- Calls: gpiochip_get_data
- Called by: __gpio_is_occupied, pxa_ack_muxed_gpio, pxa_gpio_direction_input, pxa_gpio_direction_output, pxa_gpio_get, pxa_gpio_set, pxa_mask_muxed_gpio

### gpio_is_mmp_type
- Return type: static int
- Signature: gpio_is_mmp_type(int type)
- Line: 173
- Called by: pxa_gpio_probe

### gpio_to_pxabank
- Return type: static pxa_gpio_bank *
- Signature: gpio_to_pxabank(struct gpio_chip * c,unsigned gpio)
- Line: 167
- Calls: chip_to_pxachip
- Called by: pxa_gpio_irq_type, pxa_mask_muxed_gpio, pxa_unmask_muxed_gpio

### pxa_ack_muxed_gpio
- Return type: static void
- Signature: pxa_ack_muxed_gpio(struct irq_data * d)
- Line: 479
- Calls: gpio_bank_base

### pxa_gpio_demux_handler
- Return type: static irqreturn_t
- Signature: pxa_gpio_demux_handler(int in_irq,void * d)
- Line: 437

### pxa_gpio_direct_handler
- Return type: static irqreturn_t
- Signature: pxa_gpio_direct_handler(int in_irq,void * d)
- Line: 464

### pxa_gpio_direction_input
- Return type: static int
- Signature: pxa_gpio_direction_input(struct gpio_chip * chip,unsigned offset)
- Line: 255
- Calls: __gpio_is_inverted, gpio_bank_base, pxa_gpio_has_pinctrl

### pxa_gpio_direction_output
- Return type: static int
- Signature: pxa_gpio_direction_output(struct gpio_chip * chip,unsigned offset,int value)
- Line: 281
- Calls: __gpio_is_inverted, gpio_bank_base, pxa_gpio_has_pinctrl

### pxa_gpio_dt_init
- Return type: static int __init
- Signature: pxa_gpio_dt_init(void)
- Line: 740

### pxa_gpio_get
- Return type: static int
- Signature: pxa_gpio_get(struct gpio_chip * chip,unsigned offset)
- Line: 310
- Calls: gpio_bank_base

### pxa_gpio_has_pinctrl
- Return type: static bool
- Signature: pxa_gpio_has_pinctrl(void)
- Line: 235
- Called by: pxa_gpio_direction_input, pxa_gpio_direction_output

### pxa_gpio_irq_type
- Return type: static int
- Signature: pxa_gpio_irq_type(struct irq_data * d,unsigned int type)
- Line: 392
- Calls: __gpio_is_inverted, __gpio_is_occupied, gpio_to_pxabank, update_edge_detect

### pxa_gpio_legacy_init
- Return type: static int __init
- Signature: pxa_gpio_legacy_init(void)
- Line: 731

### pxa_gpio_nums
- Return type: static int
- Signature: pxa_gpio_nums(struct platform_device * pdev)
- Line: 534
- Called by: pxa_gpio_probe

### pxa_gpio_of_xlate
- Return type: static int
- Signature: pxa_gpio_of_xlate(struct gpio_chip * gc,const struct of_phandle_args * gpiospec,u32 * flags)
- Line: 329

### pxa_gpio_probe
- Return type: static int
- Signature: pxa_gpio_probe(struct platform_device * pdev)
- Line: 610
- Calls: gpio_is_mmp_type, pxa_gpio_nums, pxa_gpio_probe_dt, pxa_init_gpio_chip

### pxa_gpio_probe_dt
- Return type: static int
- Signature: pxa_gpio_probe_dt(struct platform_device * pdev,struct pxa_gpio_chip * pchip)
- Line: 587
- Called by: pxa_gpio_probe

### pxa_gpio_resume
- Return type: static void
- Signature: pxa_gpio_resume(void * data)
- Line: 771

### pxa_gpio_set
- Return type: static int
- Signature: pxa_gpio_set(struct gpio_chip * chip,unsigned int offset,int value)
- Line: 318
- Calls: gpio_bank_base

### pxa_gpio_set_wake
- Return type: static int
- Signature: pxa_gpio_set_wake(struct irq_data * d,unsigned int on)
- Line: 504

### pxa_gpio_suspend
- Return type: static int
- Signature: pxa_gpio_suspend(void * data)
- Line: 750

### pxa_gpio_sysinit
- Return type: static int __init
- Signature: pxa_gpio_sysinit(void)
- Line: 804

### pxa_gpio_to_irq
- Return type: static int
- Signature: pxa_gpio_to_irq(struct gpio_chip * chip,unsigned offset)
- Line: 248
- Calls: chip_to_pxachip

### pxa_init_gpio_chip
- Return type: static int
- Signature: pxa_init_gpio_chip(struct pxa_gpio_chip * pchip,int ngpio,void __iomem * regbase)
- Line: 343
- Called by: pxa_gpio_probe

### pxa_irq_domain_map
- Return type: static int
- Signature: pxa_irq_domain_map(struct irq_domain * d,unsigned int irq,irq_hw_number_t hw)
- Line: 559

### pxa_irq_to_gpio
- Return type: int
- Signature: pxa_irq_to_gpio(int irq)
- Line: 223

### pxa_mask_muxed_gpio
- Return type: static void
- Signature: pxa_mask_muxed_gpio(struct irq_data * d)
- Line: 488
- Calls: gpio_bank_base, gpio_to_pxabank

### pxa_unmask_muxed_gpio
- Return type: static void
- Signature: pxa_unmask_muxed_gpio(struct irq_data * d)
- Line: 515
- Calls: gpio_to_pxabank, update_edge_detect

### update_edge_detect
- Return type: static void
- Signature: update_edge_detect(struct pxa_gpio_bank * c)
- Line: 380
- Called by: pxa_gpio_irq_type, pxa_unmask_muxed_gpio

## Structs (3)

### pxa_gpio_bank
- Line: 64
- Members:
  - regbase: void __iomem *
  - irq_mask: unsigned long
  - irq_edge_rise: unsigned long
  - irq_edge_fall: unsigned long
  - saved_gplr: unsigned long
  - saved_gpdr: unsigned long
  - saved_grer: unsigned long
  - saved_gfer: unsigned long
  - dev: device *
  - chip: gpio_chip
  - banks: pxa_gpio_bank *
  - irqdomain: irq_domain *
  - irq0: int
  - irq1: int
  - set_wake: int (*)(unsigned int gpio,unsigned int on)
  - type: pxa_gpio_type
  - gpio_nums: int

### pxa_gpio_chip
- Line: 78
- Members:
  - regbase: void __iomem *
  - irq_mask: unsigned long
  - irq_edge_rise: unsigned long
  - irq_edge_fall: unsigned long
  - saved_gplr: unsigned long
  - saved_gpdr: unsigned long
  - saved_grer: unsigned long
  - saved_gfer: unsigned long
  - dev: device *
  - chip: gpio_chip
  - banks: pxa_gpio_bank *
  - irqdomain: irq_domain *
  - irq0: int
  - irq1: int
  - set_wake: int (*)(unsigned int gpio,unsigned int on)
  - type: pxa_gpio_type
  - gpio_nums: int

### pxa_gpio_id
- Line: 100
- Members:
  - regbase: void __iomem *
  - irq_mask: unsigned long
  - irq_edge_rise: unsigned long
  - irq_edge_fall: unsigned long
  - saved_gplr: unsigned long
  - saved_gpdr: unsigned long
  - saved_grer: unsigned long
  - saved_gfer: unsigned long
  - dev: device *
  - chip: gpio_chip
  - banks: pxa_gpio_bank *
  - irqdomain: irq_domain *
  - irq0: int
  - irq1: int
  - set_wake: int (*)(unsigned int gpio,unsigned int on)
  - type: pxa_gpio_type
  - gpio_nums: int

## Enums (1)

### pxa_gpio_type
- Line: 89

## Variables (19)

- static **gpio_id_table** : const struct platform_device_id[] (line 710)
- static **gpio_type** : pxa_gpio_type (line 107)
- static **irq_base** : int (line 62)
- static **mmp2_id** : pxa_gpio_id (line 139)
- static **mmp_id** : pxa_gpio_id (line 134)
- static **pxa1928_id** : pxa_gpio_id (line 144)
- static **pxa25x_id** : pxa_gpio_id (line 109)
- static **pxa26x_id** : pxa_gpio_id (line 114)
- static **pxa27x_id** : pxa_gpio_id (line 119)
- static **pxa3xx_id** : pxa_gpio_id (line 124)
- static **pxa93x_id** : pxa_gpio_id (line 129)
- static **pxa_gpio_chip** : pxa_gpio_chip * (line 106)
- static **pxa_gpio_driver** : platform_driver (line 722)
- static **pxa_gpio_dt_ids** : const struct of_device_id[] (line 575)
- static **pxa_gpio_syscore** : syscore (line 800)
- static **pxa_gpio_syscore_ops** : const struct syscore_ops (line 795)
- static **pxa_irq_domain_ops** : const struct irq_domain_ops (line 569)
- **pxa_last_gpio** : int (line 61)
- static **pxa_muxed_gpio_chip** : irq_chip (line 525)

## Macros (14)

- **BANK_OFF**(n) (line 59)
- **ED_MASK_OFFSET** (line 57)
- **GAFR_OFFSET** (line 56)
- **GEDR_OFFSET** (line 55)
- **GFER_OFFSET** (line 54)
- **GPCR_OFFSET** (line 52)
- **GPDR_OFFSET** (line 50)
- **GPLR_OFFSET** (line 49)
- **GPSR_OFFSET** (line 51)
- **GRER_OFFSET** (line 53)
- **for_each_gpio_bank**(i,b,pc) (line 149)
- **pxa_gpio_probe_dt**(pdev,pchip) (line 607)
- **pxa_gpio_resume** (line 792)
- **pxa_gpio_suspend** (line 791)
