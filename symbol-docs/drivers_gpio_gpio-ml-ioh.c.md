# drivers/gpio/gpio-ml-ioh.c

Subsystem: drivers/gpio

## Functions (18)

### ioh_gpio_alloc_generic_chip
- Return type: static int
- Signature: ioh_gpio_alloc_generic_chip(struct ioh_gpio * chip,unsigned int irq_start,unsigned int num)
- Line: 374
- Called by: ioh_gpio_probe

### ioh_gpio_direction_input
- Return type: static int
- Signature: ioh_gpio_direction_input(struct gpio_chip * gpio,unsigned nr)
- Line: 144
- Calls: gpiochip_get_data

### ioh_gpio_direction_output
- Return type: static int
- Signature: ioh_gpio_direction_output(struct gpio_chip * gpio,unsigned nr,int val)
- Line: 118
- Calls: gpiochip_get_data

### ioh_gpio_get
- Return type: static int
- Signature: ioh_gpio_get(struct gpio_chip * gpio,unsigned nr)
- Line: 111
- Calls: gpiochip_get_data

### ioh_gpio_handler
- Return type: static irqreturn_t
- Signature: ioh_gpio_handler(int irq,void * dev_id)
- Line: 350

### ioh_gpio_probe
- Return type: static int
- Signature: ioh_gpio_probe(struct pci_dev * pdev,const struct pci_device_id * id)
- Line: 403
- Calls: ioh_gpio_alloc_generic_chip, ioh_gpio_setup

### ioh_gpio_restore_reg_conf
- Return type: static void
- Signature: ioh_gpio_restore_reg_conf(struct ioh_gpio * chip)
- Line: 189
- Called by: ioh_gpio_resume

### ioh_gpio_resume
- Return type: static int
- Signature: ioh_gpio_resume(struct device * dev)
- Line: 494
- Calls: ioh_gpio_restore_reg_conf

### ioh_gpio_save_reg_conf
- Return type: static void
- Signature: ioh_gpio_save_reg_conf(struct ioh_gpio * chip)
- Line: 163
- Called by: ioh_gpio_suspend

### ioh_gpio_set
- Return type: static int
- Signature: ioh_gpio_set(struct gpio_chip * gpio,unsigned int nr,int val)
- Line: 92
- Calls: gpiochip_get_data

### ioh_gpio_setup
- Return type: static void
- Signature: ioh_gpio_setup(struct ioh_gpio * chip,int num_port)
- Line: 218
- Called by: ioh_gpio_probe

### ioh_gpio_suspend
- Return type: static int
- Signature: ioh_gpio_suspend(struct device * dev)
- Line: 482
- Calls: ioh_gpio_save_reg_conf

### ioh_gpio_to_irq
- Return type: static int
- Signature: ioh_gpio_to_irq(struct gpio_chip * gpio,unsigned offset)
- Line: 212
- Calls: gpiochip_get_data

### ioh_irq_disable
- Return type: static void
- Signature: ioh_irq_disable(struct irq_data * d)
- Line: 322

### ioh_irq_enable
- Return type: static void
- Signature: ioh_irq_enable(struct irq_data * d)
- Line: 336

### ioh_irq_mask
- Return type: static void
- Signature: ioh_irq_mask(struct irq_data * d)
- Line: 313

### ioh_irq_type
- Return type: static int
- Signature: ioh_irq_type(struct irq_data * d,unsigned int type)
- Line: 235

### ioh_irq_unmask
- Return type: static void
- Signature: ioh_irq_unmask(struct irq_data * d)
- Line: 304

## Structs (4)

### ioh_gpio
- Line: 78
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
  - im_0: u32
  - im_1: u32
  - reserved: u32
  - regs: ioh_reg_comn[8]
  - reserve1: u32[16]
  - ioh_sel_reg: u32[4]
  - reserve2: u32[11]
  - srst: u32
  - ien_reg: u32
  - imask_reg: u32
  - po_reg: u32
  - pm_reg: u32
  - im0_reg: u32
  - im1_reg: u32
  - use_sel_reg: u32
  - base: void __iomem *
  - reg: ioh_regs __iomem *
  - dev: device *
  - gpio: gpio_chip
  - ioh_gpio_reg: ioh_gpio_reg_data
  - gpio_use_sel: u32
  - ch: int
  - irq_base: int
  - spinlock: spinlock_t

### ioh_gpio_reg_data
- Line: 55
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
  - im_0: u32
  - im_1: u32
  - reserved: u32
  - regs: ioh_reg_comn[8]
  - reserve1: u32[16]
  - ioh_sel_reg: u32[4]
  - reserve2: u32[11]
  - srst: u32
  - ien_reg: u32
  - imask_reg: u32
  - po_reg: u32
  - pm_reg: u32
  - im0_reg: u32
  - im1_reg: u32
  - use_sel_reg: u32
  - base: void __iomem *
  - reg: ioh_regs __iomem *
  - dev: device *
  - gpio: gpio_chip
  - ioh_gpio_reg: ioh_gpio_reg_data
  - gpio_use_sel: u32
  - ch: int
  - irq_base: int
  - spinlock: spinlock_t

### ioh_reg_comn
- Line: 22
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
  - im_0: u32
  - im_1: u32
  - reserved: u32
  - regs: ioh_reg_comn[8]
  - reserve1: u32[16]
  - ioh_sel_reg: u32[4]
  - reserve2: u32[11]
  - srst: u32
  - ien_reg: u32
  - imask_reg: u32
  - po_reg: u32
  - pm_reg: u32
  - im0_reg: u32
  - im1_reg: u32
  - use_sel_reg: u32
  - base: void __iomem *
  - reg: ioh_regs __iomem *
  - dev: device *
  - gpio: gpio_chip
  - ioh_gpio_reg: ioh_gpio_reg_data
  - gpio_use_sel: u32
  - ch: int
  - irq_base: int
  - spinlock: spinlock_t

### ioh_regs
- Line: 37
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
  - im_0: u32
  - im_1: u32
  - reserved: u32
  - regs: ioh_reg_comn[8]
  - reserve1: u32[16]
  - ioh_sel_reg: u32[4]
  - reserve2: u32[11]
  - srst: u32
  - ien_reg: u32
  - imask_reg: u32
  - po_reg: u32
  - pm_reg: u32
  - im0_reg: u32
  - im1_reg: u32
  - use_sel_reg: u32
  - base: void __iomem *
  - reg: ioh_regs __iomem *
  - dev: device *
  - gpio: gpio_chip
  - ioh_gpio_reg: ioh_gpio_reg_data
  - gpio_use_sel: u32
  - ch: int
  - irq_base: int
  - spinlock: spinlock_t

## Variables (3)

- static **ioh_gpio_driver** : pci_driver (line 516)
- static **ioh_gpio_pcidev_id** : const struct pci_device_id[] (line 510)
- static **num_ports** : const int[] (line 90)

## Macros (7)

- **IOH_EDGE_BOTH** (line 17)
- **IOH_EDGE_FALLING** (line 13)
- **IOH_EDGE_RISING** (line 14)
- **IOH_IM_MASK** (line 18)
- **IOH_IRQ_BASE** (line 20)
- **IOH_LEVEL_H** (line 16)
- **IOH_LEVEL_L** (line 15)
