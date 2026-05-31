# drivers/gpio/gpio-mxc.c

Subsystem: drivers/gpio

## Functions (23)

### gpio_mxc_init
- Return type: static int __init
- Signature: gpio_mxc_init(void)
- Line: 731

### gpio_set_irq_type
- Return type: static int
- Signature: gpio_set_irq_type(struct irq_data * d,u32 type)
- Line: 162

### gpio_set_wake_irq
- Return type: static int
- Signature: gpio_set_wake_irq(struct irq_data * d,u32 enable)
- Line: 321

### mx2_gpio_irq_handler
- Return type: static void
- Signature: mx2_gpio_irq_handler(struct irq_desc * desc)
- Line: 291
- Calls: mxc_gpio_irq_handler

### mx3_gpio_irq_handler
- Return type: static void
- Signature: mx3_gpio_irq_handler(struct irq_desc * desc)
- Line: 272
- Calls: mxc_gpio_irq_handler

### mxc_flip_edge
- Return type: static void
- Signature: mxc_flip_edge(struct mxc_gpio_port * port,u32 gpio)
- Line: 229
- Called by: mxc_gpio_irq_handler

### mxc_gpio_free
- Return type: static void
- Signature: mxc_gpio_free(struct gpio_chip * chip,unsigned int offset)
- Line: 392
- Calls: gpiochip_generic_free

### mxc_gpio_generic_config
- Return type: static bool
- Signature: mxc_gpio_generic_config(struct mxc_gpio_port * port,unsigned int offset,unsigned long conf)
- Line: 568
- Calls: gpiochip_generic_config
- Called by: mxc_gpio_set_pad_wakeup

### mxc_gpio_init_gc
- Return type: static int
- Signature: mxc_gpio_init_gc(struct mxc_gpio_port * port,int irq_base)
- Line: 345
- Called by: mxc_gpio_probe

### mxc_gpio_irq_handler
- Return type: static void
- Signature: mxc_gpio_irq_handler(struct mxc_gpio_port * port,u32 irq_stat)
- Line: 257
- Calls: mxc_flip_edge
- Called by: mx2_gpio_irq_handler, mx3_gpio_irq_handler

### mxc_gpio_noirq_resume
- Return type: static int
- Signature: mxc_gpio_noirq_resume(struct device * dev)
- Line: 661
- Calls: mxc_gpio_set_pad_wakeup

### mxc_gpio_noirq_suspend
- Return type: static int
- Signature: mxc_gpio_noirq_suspend(struct device * dev)
- Line: 650
- Calls: mxc_gpio_set_pad_wakeup

### mxc_gpio_probe
- Return type: static int
- Signature: mxc_gpio_probe(struct platform_device * pdev)
- Line: 416
- Calls: gpio_generic_chip_init, mxc_gpio_init_gc, mxc_update_irq_chained_handler

### mxc_gpio_request
- Return type: static int
- Signature: mxc_gpio_request(struct gpio_chip * chip,unsigned int offset)
- Line: 381
- Calls: gpiochip_generic_request

### mxc_gpio_restore_regs
- Return type: static void
- Signature: mxc_gpio_restore_regs(struct mxc_gpio_port * port)
- Line: 555
- Called by: mxc_gpio_runtime_resume, mxc_gpio_syscore_resume

### mxc_gpio_runtime_resume
- Return type: static int
- Signature: mxc_gpio_runtime_resume(struct device * dev)
- Line: 633
- Calls: mxc_gpio_restore_regs, mxc_update_irq_chained_handler

### mxc_gpio_runtime_suspend
- Return type: static int
- Signature: mxc_gpio_runtime_suspend(struct device * dev)
- Line: 622
- Calls: mxc_gpio_save_regs, mxc_update_irq_chained_handler

### mxc_gpio_save_regs
- Return type: static void
- Signature: mxc_gpio_save_regs(struct mxc_gpio_port * port)
- Line: 542
- Called by: mxc_gpio_runtime_suspend, mxc_gpio_syscore_suspend

### mxc_gpio_set_pad_wakeup
- Return type: static bool
- Signature: mxc_gpio_set_pad_wakeup(struct mxc_gpio_port * port,bool enable)
- Line: 582
- Calls: mxc_gpio_generic_config
- Called by: mxc_gpio_noirq_resume, mxc_gpio_noirq_suspend

### mxc_gpio_syscore_resume
- Return type: static void
- Signature: mxc_gpio_syscore_resume(void * data)
- Line: 695
- Calls: mxc_gpio_restore_regs

### mxc_gpio_syscore_suspend
- Return type: static int
- Signature: mxc_gpio_syscore_suspend(void * data)
- Line: 678
- Calls: mxc_gpio_save_regs

### mxc_gpio_to_irq
- Return type: static int
- Signature: mxc_gpio_to_irq(struct gpio_chip * gc,unsigned offset)
- Line: 374
- Calls: gpiochip_get_data

### mxc_update_irq_chained_handler
- Return type: static void
- Signature: mxc_update_irq_chained_handler(struct mxc_gpio_port * port,bool enable)
- Line: 398
- Called by: mxc_gpio_probe, mxc_gpio_runtime_resume, mxc_gpio_runtime_suspend

## Structs (3)

### mxc_gpio_hwdata
- Line: 37
- Members:
  - dr_reg: unsigned
  - gdir_reg: unsigned
  - psr_reg: unsigned
  - icr1_reg: unsigned
  - icr2_reg: unsigned
  - imr_reg: unsigned
  - isr_reg: unsigned
  - edge_sel_reg: int
  - low_level: unsigned
  - high_level: unsigned
  - rise_edge: unsigned
  - fall_edge: unsigned
  - icr1: u32
  - icr2: u32
  - imr: u32
  - gdir: u32
  - edge_sel: u32
  - dr: u32
  - node: list_head
  - base: void __iomem *
  - clk: clk *
  - irq: int
  - irq_high: int
  - mx_irq_handler: void (*)(struct irq_desc * desc)
  - domain: irq_domain *
  - gen_gc: gpio_generic_chip
  - dev: device *
  - both_edges: u32
  - gpio_saved_reg: mxc_gpio_reg_saved
  - power_off: bool
  - wakeup_pads: u32
  - is_pad_wakeup: bool
  - pad_type: u32[32]
  - hwdata: const struct mxc_gpio_hwdata *

### mxc_gpio_port
- Line: 61
- Members:
  - dr_reg: unsigned
  - gdir_reg: unsigned
  - psr_reg: unsigned
  - icr1_reg: unsigned
  - icr2_reg: unsigned
  - imr_reg: unsigned
  - isr_reg: unsigned
  - edge_sel_reg: int
  - low_level: unsigned
  - high_level: unsigned
  - rise_edge: unsigned
  - fall_edge: unsigned
  - icr1: u32
  - icr2: u32
  - imr: u32
  - gdir: u32
  - edge_sel: u32
  - dr: u32
  - node: list_head
  - base: void __iomem *
  - clk: clk *
  - irq: int
  - irq_high: int
  - mx_irq_handler: void (*)(struct irq_desc * desc)
  - domain: irq_domain *
  - gen_gc: gpio_generic_chip
  - dev: device *
  - both_edges: u32
  - gpio_saved_reg: mxc_gpio_reg_saved
  - power_off: bool
  - wakeup_pads: u32
  - is_pad_wakeup: bool
  - pad_type: u32[32]
  - hwdata: const struct mxc_gpio_hwdata *

### mxc_gpio_reg_saved
- Line: 52
- Members:
  - dr_reg: unsigned
  - gdir_reg: unsigned
  - psr_reg: unsigned
  - icr1_reg: unsigned
  - icr2_reg: unsigned
  - imr_reg: unsigned
  - isr_reg: unsigned
  - edge_sel_reg: int
  - low_level: unsigned
  - high_level: unsigned
  - rise_edge: unsigned
  - fall_edge: unsigned
  - icr1: u32
  - icr2: u32
  - imr: u32
  - gdir: u32
  - edge_sel: u32
  - dr: u32
  - node: list_head
  - base: void __iomem *
  - clk: clk *
  - irq: int
  - irq_high: int
  - mx_irq_handler: void (*)(struct irq_desc * desc)
  - domain: irq_domain *
  - gen_gc: gpio_generic_chip
  - dev: device *
  - both_edges: u32
  - gpio_saved_reg: mxc_gpio_reg_saved
  - power_off: bool
  - wakeup_pads: u32
  - is_pad_wakeup: bool
  - pad_type: u32[32]
  - hwdata: const struct mxc_gpio_hwdata *

## Variables (8)

- static **imx1_imx21_gpio_hwdata** : mxc_gpio_hwdata (line 80)
- static **imx31_gpio_hwdata** : mxc_gpio_hwdata (line 95)
- static **imx35_gpio_hwdata** : mxc_gpio_hwdata (line 110)
- static **mxc_gpio_dev_pm_ops** : const struct dev_pm_ops (line 673)
- static **mxc_gpio_driver** : platform_driver (line 721)
- static **mxc_gpio_dt_ids** : const struct of_device_id[] (line 140)
- static **mxc_gpio_syscore** : syscore (line 717)
- static **mxc_gpio_syscore_ops** : const struct syscore_ops (line 712)

## Macros (18)

- **GPIO_DR** (line 125)
- **GPIO_EDGE_SEL** (line 132)
- **GPIO_GDIR** (line 126)
- **GPIO_ICR1** (line 128)
- **GPIO_ICR2** (line 129)
- **GPIO_IMR** (line 130)
- **GPIO_INT_BOTH_EDGES** (line 138)
- **GPIO_INT_FALL_EDGE** (line 137)
- **GPIO_INT_HIGH_LEV** (line 135)
- **GPIO_INT_LOW_LEV** (line 134)
- **GPIO_INT_RISE_EDGE** (line 136)
- **GPIO_ISR** (line 131)
- **GPIO_PSR** (line 127)
- **IMX_SCU_WAKEUP_FALL_EDGE** (line 32)
- **IMX_SCU_WAKEUP_HIGH_LVL** (line 34)
- **IMX_SCU_WAKEUP_LOW_LVL** (line 31)
- **IMX_SCU_WAKEUP_OFF** (line 30)
- **IMX_SCU_WAKEUP_RISE_EDGE** (line 33)
