# drivers/gpio/gpio-brcmstb.c

Subsystem: drivers/gpio

## Functions (32)

### __brcmstb_gpio_get_active_irqs
- Return type: static unsigned long
- Signature: __brcmstb_gpio_get_active_irqs(struct brcmstb_gpio_bank * bank)
- Line: 73
- Called by: brcmstb_gpio_get_active_irqs, brcmstb_gpio_probe

### __brcmstb_gpio_set_imask
- Return type: static void
- Signature: __brcmstb_gpio_set_imask(struct brcmstb_gpio_bank * bank,irq_hw_number_t hwirq,bool enable)
- Line: 99
- Calls: brcmstb_gpio_hwirq_to_offset
- Called by: brcmstb_gpio_irq_mask_ack, brcmstb_gpio_set_imask

### brcmstb_gpio_bank_restore
- Return type: static void
- Signature: brcmstb_gpio_bank_restore(struct brcmstb_gpio_priv * priv,struct brcmstb_gpio_bank * bank)
- Line: 561
- Called by: brcmstb_gpio_resume

### brcmstb_gpio_bank_save
- Return type: static void
- Signature: brcmstb_gpio_bank_save(struct brcmstb_gpio_priv * priv,struct brcmstb_gpio_bank * bank)
- Line: 520
- Called by: brcmstb_gpio_quiesce

### brcmstb_gpio_gc_to_priv
- Return type: static brcmstb_gpio_priv *
- Signature: brcmstb_gpio_gc_to_priv(struct gpio_chip * gc)
- Line: 66
- Calls: gpiochip_get_data
- Called by: brcmstb_gpio_of_xlate, brcmstb_gpio_to_irq

### brcmstb_gpio_get_active_irqs
- Return type: static unsigned long
- Signature: brcmstb_gpio_get_active_irqs(struct brcmstb_gpio_bank * bank)
- Line: 82
- Calls: __brcmstb_gpio_get_active_irqs
- Called by: brcmstb_gpio_irq_bank_handler

### brcmstb_gpio_hwirq_to_bank
- Return type: static brcmstb_gpio_bank *
- Signature: brcmstb_gpio_hwirq_to_bank(struct brcmstb_gpio_priv * priv,irq_hw_number_t hwirq)
- Line: 328
- Called by: brcmstb_gpio_irq_map

### brcmstb_gpio_hwirq_to_offset
- Return type: static int
- Signature: brcmstb_gpio_hwirq_to_offset(irq_hw_number_t hwirq,struct brcmstb_gpio_bank * bank)
- Line: 93
- Called by: __brcmstb_gpio_set_imask, brcmstb_gpio_irq_ack, brcmstb_gpio_irq_mask_ack, brcmstb_gpio_irq_set_type, brcmstb_gpio_irq_set_wake

### brcmstb_gpio_irq_ack
- Return type: static void
- Signature: brcmstb_gpio_irq_ack(struct irq_data * d)
- Line: 166
- Calls: brcmstb_gpio_hwirq_to_offset, gpiochip_get_data

### brcmstb_gpio_irq_bank_handler
- Return type: static void
- Signature: brcmstb_gpio_irq_bank_handler(struct brcmstb_gpio_bank * bank)
- Line: 287
- Calls: brcmstb_gpio_get_active_irqs
- Called by: brcmstb_gpio_irq_handler

### brcmstb_gpio_irq_handler
- Return type: static void
- Signature: brcmstb_gpio_irq_handler(struct irq_desc * desc)
- Line: 313
- Calls: brcmstb_gpio_irq_bank_handler

### brcmstb_gpio_irq_map
- Return type: static int
- Signature: brcmstb_gpio_irq_map(struct irq_domain * d,unsigned int irq,irq_hw_number_t hwirq)
- Line: 349
- Calls: brcmstb_gpio_hwirq_to_bank

### brcmstb_gpio_irq_mask
- Return type: static void
- Signature: brcmstb_gpio_irq_mask(struct irq_data * d)
- Line: 136
- Calls: brcmstb_gpio_set_imask, gpiochip_get_data

### brcmstb_gpio_irq_mask_ack
- Return type: static void
- Signature: brcmstb_gpio_irq_mask_ack(struct irq_data * d)
- Line: 144
- Calls: __brcmstb_gpio_set_imask, brcmstb_gpio_hwirq_to_offset, gpiochip_get_data

### brcmstb_gpio_irq_set_type
- Return type: static int
- Signature: brcmstb_gpio_irq_set_type(struct irq_data * d,unsigned int type)
- Line: 177
- Calls: brcmstb_gpio_hwirq_to_offset, gpiochip_get_data

### brcmstb_gpio_irq_set_wake
- Return type: static int
- Signature: brcmstb_gpio_irq_set_wake(struct irq_data * d,unsigned int enable)
- Line: 257
- Calls: brcmstb_gpio_hwirq_to_offset, brcmstb_gpio_priv_set_wake, gpiochip_get_data

### brcmstb_gpio_irq_setup
- Return type: static int
- Signature: brcmstb_gpio_irq_setup(struct platform_device * pdev,struct brcmstb_gpio_priv * priv)
- Line: 460
- Called by: brcmstb_gpio_probe

### brcmstb_gpio_irq_unmap
- Return type: static void
- Signature: brcmstb_gpio_irq_unmap(struct irq_domain * d,unsigned int irq)
- Line: 373

### brcmstb_gpio_irq_unmask
- Return type: static void
- Signature: brcmstb_gpio_irq_unmask(struct irq_data * d)
- Line: 158
- Calls: brcmstb_gpio_set_imask, gpiochip_get_data

### brcmstb_gpio_of_xlate
- Return type: static int
- Signature: brcmstb_gpio_of_xlate(struct gpio_chip * gc,const struct of_phandle_args * gpiospec,u32 * flags)
- Line: 428
- Calls: brcmstb_gpio_gc_to_priv, gpiochip_get_data

### brcmstb_gpio_priv_set_wake
- Return type: static int
- Signature: brcmstb_gpio_priv_set_wake(struct brcmstb_gpio_priv * priv,unsigned int enable)
- Line: 239
- Called by: brcmstb_gpio_irq_set_wake

### brcmstb_gpio_probe
- Return type: static int
- Signature: brcmstb_gpio_probe(struct platform_device * pdev)
- Line: 626
- Calls: __brcmstb_gpio_get_active_irqs, brcmstb_gpio_irq_setup, brcmstb_gpio_remove, brcmstb_gpio_sanity_check_banks, gpio_generic_chip_init

### brcmstb_gpio_quiesce
- Return type: static void
- Signature: brcmstb_gpio_quiesce(struct brcmstb_gpio_priv * priv,bool save)
- Line: 530
- Calls: brcmstb_gpio_bank_save
- Called by: brcmstb_gpio_shutdown, brcmstb_gpio_suspend_noirq

### brcmstb_gpio_remove
- Return type: static void
- Signature: brcmstb_gpio_remove(struct platform_device * pdev)
- Line: 402
- Calls: gpiochip_remove
- Called by: brcmstb_gpio_probe

### brcmstb_gpio_resume
- Return type: static int
- Signature: brcmstb_gpio_resume(struct device * dev)
- Line: 601
- Calls: brcmstb_gpio_bank_restore

### brcmstb_gpio_sanity_check_banks
- Return type: static int
- Signature: brcmstb_gpio_sanity_check_banks(struct device * dev,struct device_node * np,struct resource * res)
- Line: 386
- Called by: brcmstb_gpio_probe

### brcmstb_gpio_set_imask
- Return type: static void
- Signature: brcmstb_gpio_set_imask(struct brcmstb_gpio_bank * bank,irq_hw_number_t hwirq,bool enable)
- Line: 116
- Calls: __brcmstb_gpio_set_imask
- Called by: brcmstb_gpio_irq_mask, brcmstb_gpio_irq_unmask

### brcmstb_gpio_shutdown
- Return type: static void
- Signature: brcmstb_gpio_shutdown(struct platform_device * pdev)
- Line: 550
- Calls: brcmstb_gpio_quiesce

### brcmstb_gpio_suspend
- Return type: static int
- Signature: brcmstb_gpio_suspend(struct device * dev)
- Line: 572

### brcmstb_gpio_suspend_noirq
- Return type: static int
- Signature: brcmstb_gpio_suspend_noirq(struct device * dev)
- Line: 582
- Calls: brcmstb_gpio_quiesce

### brcmstb_gpio_to_irq
- Return type: static int
- Signature: brcmstb_gpio_to_irq(struct gpio_chip * gc,unsigned offset)
- Line: 123
- Calls: brcmstb_gpio_gc_to_priv

### brcmstb_gpio_wake_irq_handler
- Return type: static irqreturn_t
- Signature: brcmstb_gpio_wake_irq_handler(int irq,void * data)
- Line: 276

## Structs (2)

### brcmstb_gpio_bank
- Line: 38
- Members:
  - node: list_head
  - id: int
  - chip: gpio_generic_chip
  - parent_priv: brcmstb_gpio_priv *
  - width: u32
  - wake_active: u32
  - saved_regs: u32[]
  - bank_list: list_head
  - reg_base: void __iomem *
  - pdev: platform_device *
  - irq_domain: irq_domain *
  - irq_chip: irq_chip
  - parent_irq: int
  - num_gpios: int
  - parent_wake_irq: int
  - suspended: bool

### brcmstb_gpio_priv
- Line: 48
- Members:
  - node: list_head
  - id: int
  - chip: gpio_generic_chip
  - parent_priv: brcmstb_gpio_priv *
  - width: u32
  - wake_active: u32
  - saved_regs: u32[]
  - bank_list: list_head
  - reg_base: void __iomem *
  - pdev: platform_device *
  - irq_domain: irq_domain *
  - irq_chip: irq_chip
  - parent_irq: int
  - num_gpios: int
  - parent_wake_irq: int
  - suspended: bool

## Enums (1)

### gio_reg_index
- Line: 15

## Variables (6)

- static **brcmstb_gpio_driver** : platform_driver (line 795)
- static **brcmstb_gpio_irq_domain_ops** : const struct irq_domain_ops (line 379)
- static **brcmstb_gpio_irq_lock_class** : lock_class_key (line 345)
- static **brcmstb_gpio_irq_request_class** : lock_class_key (line 346)
- static **brcmstb_gpio_of_match** : const struct of_device_id[] (line 788)
- static **brcmstb_gpio_pm_ops** : const struct dev_pm_ops (line 620)

## Macros (13)

- **GIO_BANK_OFF**(bank,off) (line 28)
- **GIO_BANK_SIZE** (line 27)
- **GIO_DATA**(bank) (line 30)
- **GIO_EC**(bank) (line 32)
- **GIO_EI**(bank) (line 33)
- **GIO_IODIR**(bank) (line 31)
- **GIO_LEVEL**(bank) (line 35)
- **GIO_MASK**(bank) (line 34)
- **GIO_ODEN**(bank) (line 29)
- **GIO_STAT**(bank) (line 36)
- **GPIO_BANK**(gpio) (line 61)
- **GPIO_BIT**(gpio) (line 63)
- **MAX_GPIO_PER_BANK** (line 60)
