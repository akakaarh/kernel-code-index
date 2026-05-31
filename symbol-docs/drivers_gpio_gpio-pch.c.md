# drivers/gpio/gpio-pch.c

Subsystem: drivers/gpio

## Functions (17)

### pch_gpio_alloc_generic_chip
- Return type: static int
- Signature: pch_gpio_alloc_generic_chip(struct pch_gpio * chip,unsigned int irq_start,unsigned int num)
- Line: 324
- Called by: pch_gpio_probe

### pch_gpio_direction_input
- Return type: static int
- Signature: pch_gpio_direction_input(struct gpio_chip * gpio,unsigned int nr)
- Line: 155
- Calls: gpiochip_get_data

### pch_gpio_direction_output
- Return type: static int
- Signature: pch_gpio_direction_output(struct gpio_chip * gpio,unsigned int nr,int val)
- Line: 128
- Calls: gpiochip_get_data

### pch_gpio_get
- Return type: static int
- Signature: pch_gpio_get(struct gpio_chip * gpio,unsigned int nr)
- Line: 121
- Calls: gpiochip_get_data

### pch_gpio_handler
- Return type: static irqreturn_t
- Signature: pch_gpio_handler(int irq,void * dev_id)
- Line: 308

### pch_gpio_probe
- Return type: static int
- Signature: pch_gpio_probe(struct pci_dev * pdev,const struct pci_device_id * id)
- Line: 352
- Calls: pch_gpio_alloc_generic_chip, pch_gpio_setup

### pch_gpio_restore_reg_conf
- Return type: static void
- Signature: pch_gpio_restore_reg_conf(struct pch_gpio * chip)
- Line: 190
- Called by: pch_gpio_resume

### pch_gpio_resume
- Return type: static int
- Signature: pch_gpio_resume(struct device * dev)
- Line: 417
- Calls: pch_gpio_restore_reg_conf

### pch_gpio_save_reg_conf
- Return type: static void
- Signature: pch_gpio_save_reg_conf(struct pch_gpio * chip)
- Line: 174
- Called by: pch_gpio_suspend

### pch_gpio_set
- Return type: static int
- Signature: pch_gpio_set(struct gpio_chip * gpio,unsigned int nr,int val)
- Line: 102
- Calls: gpiochip_get_data

### pch_gpio_setup
- Return type: static void
- Signature: pch_gpio_setup(struct pch_gpio * chip)
- Line: 212
- Called by: pch_gpio_probe

### pch_gpio_suspend
- Return type: static int
- Signature: pch_gpio_suspend(struct device * dev)
- Line: 405
- Calls: pch_gpio_save_reg_conf

### pch_gpio_to_irq
- Return type: static int
- Signature: pch_gpio_to_irq(struct gpio_chip * gpio,unsigned int offset)
- Line: 205
- Calls: gpiochip_get_data

### pch_irq_ack
- Return type: static void
- Signature: pch_irq_ack(struct irq_data * d)
- Line: 300

### pch_irq_mask
- Return type: static void
- Signature: pch_irq_mask(struct irq_data * d)
- Line: 292

### pch_irq_type
- Return type: static int
- Signature: pch_irq_type(struct irq_data * d,unsigned int type)
- Line: 229

### pch_irq_unmask
- Return type: static void
- Signature: pch_irq_unmask(struct irq_data * d)
- Line: 284

## Structs (3)

### pch_gpio
- Line: 91
- Members:
  - ien: u32
  - istatus: u32
  - idisp: u32
  - iclr: u32
  - imask: u32
  - imaskclr: u32
  - po: u32
  - pi: u32
  - pm: u32
  - im0: u32
  - im1: u32
  - reserved: u32[3]
  - gpio_use_sel: u32
  - reset: u32
  - ien_reg: u32
  - imask_reg: u32
  - po_reg: u32
  - pm_reg: u32
  - im0_reg: u32
  - im1_reg: u32
  - gpio_use_sel_reg: u32
  - base: void __iomem *
  - reg: pch_regs __iomem *
  - dev: device *
  - gpio: gpio_chip
  - pch_gpio_reg: pch_gpio_reg_data
  - irq_base: int
  - ioh: pch_type_t
  - spinlock: spinlock_t

### pch_gpio_reg_data
- Line: 69
- Members:
  - ien: u32
  - istatus: u32
  - idisp: u32
  - iclr: u32
  - imask: u32
  - imaskclr: u32
  - po: u32
  - pi: u32
  - pm: u32
  - im0: u32
  - im1: u32
  - reserved: u32[3]
  - gpio_use_sel: u32
  - reset: u32
  - ien_reg: u32
  - imask_reg: u32
  - po_reg: u32
  - pm_reg: u32
  - im0_reg: u32
  - im1_reg: u32
  - gpio_use_sel_reg: u32
  - base: void __iomem *
  - reg: pch_regs __iomem *
  - dev: device *
  - gpio: gpio_chip
  - pch_gpio_reg: pch_gpio_reg_data
  - irq_base: int
  - ioh: pch_type_t
  - spinlock: spinlock_t

### pch_regs
- Line: 23
- Members:
  - ien: u32
  - istatus: u32
  - idisp: u32
  - iclr: u32
  - imask: u32
  - imaskclr: u32
  - po: u32
  - pi: u32
  - pm: u32
  - im0: u32
  - im1: u32
  - reserved: u32[3]
  - gpio_use_sel: u32
  - reset: u32
  - ien_reg: u32
  - imask_reg: u32
  - po_reg: u32
  - pm_reg: u32
  - im0_reg: u32
  - im1_reg: u32
  - gpio_use_sel_reg: u32
  - base: void __iomem *
  - reg: pch_regs __iomem *
  - dev: device *
  - gpio: gpio_chip
  - pch_gpio_reg: pch_gpio_reg_data
  - irq_base: int
  - ioh: pch_type_t
  - spinlock: spinlock_t

## Enums (1)

### pch_type_t
- Line: 45

## Variables (3)

- static **gpio_pins** : int[] (line 52)
- static **pch_gpio_driver** : pci_driver (line 442)
- static **pch_gpio_pcidev_id** : const struct pci_device_id[] (line 433)

## Macros (11)

- **PCH_EDGE_BOTH** (line 18)
- **PCH_EDGE_FALLING** (line 14)
- **PCH_EDGE_RISING** (line 15)
- **PCH_IM_MASK** (line 19)
- **PCH_IRQ_BASE** (line 21)
- **PCH_LEVEL_H** (line 17)
- **PCH_LEVEL_L** (line 16)
- **PCI_DEVICE_ID_INTEL_EG20T_PCH** (line 40)
- **PCI_DEVICE_ID_ROHM_EG20T_PCH** (line 43)
- **PCI_DEVICE_ID_ROHM_ML7223m_IOH** (line 41)
- **PCI_DEVICE_ID_ROHM_ML7223n_IOH** (line 42)
