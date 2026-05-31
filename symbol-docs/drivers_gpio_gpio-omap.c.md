# drivers/gpio/gpio-omap.c

Subsystem: drivers/gpio

## Functions (61)

### gpio_irq_bus_sync_unlock
- Return type: static void
- Signature: gpio_irq_bus_sync_unlock(struct irq_data * data)
- Line: 668
- Calls: omap_irq_data_get_bank

### gpio_omap_cpu_notifier
- Return type: static int
- Signature: gpio_omap_cpu_notifier(struct notifier_block * nb,unsigned long cmd,void * v)
- Line: 1279
- Calls: omap_get_gpio_irqbank_mask, omap_gpio_idle, omap_gpio_unidle

### omap2_set_gpio_debounce
- Return type: static int
- Signature: omap2_set_gpio_debounce(struct gpio_bank * bank,unsigned offset,unsigned debounce)
- Line: 181
- Calls: omap_gpio_dbck_enable, omap_gpio_rmw
- Called by: omap_gpio_debounce

### omap_clear_gpio_debounce
- Return type: static void
- Signature: omap_clear_gpio_debounce(struct gpio_bank * bank,unsigned offset)
- Line: 233
- Called by: omap_gpio_free, omap_gpio_irq_shutdown

### omap_clear_gpio_irqbank
- Return type: static void
- Signature: omap_clear_gpio_irqbank(struct gpio_bank * bank,int gpio_mask)
- Line: 470
- Called by: omap_clear_gpio_irqstatus, omap_gpio_irq_handler

### omap_clear_gpio_irqstatus
- Return type: static void
- Signature: omap_clear_gpio_irqstatus(struct gpio_bank * bank,unsigned offset)
- Line: 487
- Calls: omap_clear_gpio_irqbank
- Called by: omap_gpio_irq_shutdown, omap_gpio_unmask_irq

### omap_disable_gpio_module
- Return type: static void
- Signature: omap_disable_gpio_module(struct gpio_bank * bank,unsigned offset)
- Line: 395
- Called by: omap_gpio_free, omap_gpio_irq_shutdown

### omap_enable_gpio_module
- Return type: static void
- Signature: omap_enable_gpio_module(struct gpio_bank * bank,unsigned offset)
- Line: 374
- Called by: omap_gpio_init_irq, omap_gpio_irq_startup, omap_gpio_request

### omap_get_gpio_irqbank_mask
- Return type: static u32
- Signature: omap_get_gpio_irqbank_mask(struct gpio_bank * bank)
- Line: 493
- Called by: gpio_omap_cpu_notifier, omap_gpio_irq_handler

### omap_gpio_chip_init
- Return type: static int
- Signature: omap_gpio_chip_init(struct gpio_bank * bank,struct device * pm_dev)
- Line: 1033
- Calls: gpiochip_remove
- Called by: omap_gpio_probe

### omap_gpio_dbck_disable
- Return type: static void
- Signature: omap_gpio_dbck_disable(struct gpio_bank * bank)
- Line: 154
- Called by: omap_gpio_idle

### omap_gpio_dbck_enable
- Return type: static void
- Signature: omap_gpio_dbck_enable(struct gpio_bank * bank)
- Line: 143
- Called by: omap2_set_gpio_debounce, omap_gpio_unidle

### omap_gpio_debounce
- Return type: static int
- Signature: omap_gpio_debounce(struct gpio_chip * chip,unsigned offset,unsigned debounce)
- Line: 915
- Calls: gpiochip_get_data, omap2_set_gpio_debounce
- Called by: omap_gpio_set_config

### omap_gpio_drv_reg
- Return type: static int __init
- Signature: omap_gpio_drv_reg(void)
- Line: 1579

### omap_gpio_exit
- Return type: static void __exit
- Signature: omap_gpio_exit(void)
- Line: 1595

### omap_gpio_free
- Return type: static void
- Signature: omap_gpio_free(struct gpio_chip * chip,unsigned offset)
- Line: 828
- Calls: gpiochip_get_data, omap_clear_gpio_debounce, omap_disable_gpio_module, omap_set_gpio_direction

### omap_gpio_get
- Return type: static int
- Signature: omap_gpio_get(struct gpio_chip * chip,unsigned offset)
- Line: 867
- Calls: gpiochip_get_data, omap_gpio_is_input

### omap_gpio_get_direction
- Return type: static int
- Signature: omap_gpio_get_direction(struct gpio_chip * chip,unsigned offset)
- Line: 845
- Calls: gpiochip_get_data

### omap_gpio_get_multiple
- Return type: static int
- Signature: omap_gpio_get_multiple(struct gpio_chip * chip,unsigned long * mask,unsigned long * bits)
- Line: 893
- Calls: gpiochip_get_data

### omap_gpio_idle
- Return type: static void
- Signature: omap_gpio_idle(struct gpio_bank * bank,bool may_lose_context)
- Line: 1141
- Calls: omap_gpio_dbck_disable, omap_gpio_rmw
- Called by: gpio_omap_cpu_notifier, omap_gpio_runtime_suspend

### omap_gpio_init_context
- Return type: static void
- Signature: omap_gpio_init_context(struct gpio_bank * p)
- Line: 1096
- Called by: omap_gpio_unidle

### omap_gpio_init_irq
- Return type: static void
- Signature: omap_gpio_init_irq(struct gpio_bank * bank,unsigned offset)
- Line: 416
- Calls: omap_enable_gpio_module, omap_set_gpio_direction
- Called by: omap_gpio_irq_type

### omap_gpio_input
- Return type: static int
- Signature: omap_gpio_input(struct gpio_chip * chip,unsigned offset)
- Line: 855
- Calls: gpiochip_get_data, omap_set_gpio_direction

### omap_gpio_irq_bus_lock
- Return type: static void
- Signature: omap_gpio_irq_bus_lock(struct irq_data * data)
- Line: 661
- Calls: omap_irq_data_get_bank

### omap_gpio_irq_handler
- Return type: static irqreturn_t
- Signature: omap_gpio_irq_handler(int irq,void * gpiobank)
- Line: 559
- Calls: omap_clear_gpio_irqbank, omap_get_gpio_irqbank_mask, omap_toggle_gpio_edge_triggering

### omap_gpio_irq_print_chip
- Return type: static void
- Signature: omap_gpio_irq_print_chip(struct irq_data * d,struct seq_file * p)
- Line: 714
- Calls: omap_irq_data_get_bank

### omap_gpio_irq_shutdown
- Return type: static void
- Signature: omap_gpio_irq_shutdown(struct irq_data * d)
- Line: 644
- Calls: omap_clear_gpio_debounce, omap_clear_gpio_irqstatus, omap_disable_gpio_module, omap_irq_data_get_bank, omap_set_gpio_irqenable, omap_set_gpio_triggering

### omap_gpio_irq_startup
- Return type: static unsigned int
- Signature: omap_gpio_irq_startup(struct irq_data * d)
- Line: 625
- Calls: omap_enable_gpio_module, omap_gpio_unmask_irq, omap_irq_data_get_bank, omap_set_gpio_direction

### omap_gpio_irq_type
- Return type: static int
- Signature: omap_gpio_irq_type(struct irq_data * d,unsigned type)
- Line: 425
- Calls: omap_gpio_init_irq, omap_gpio_is_input, omap_irq_data_get_bank, omap_set_gpio_triggering

### omap_gpio_is_input
- Return type: static int
- Signature: omap_gpio_is_input(struct gpio_bank * bank,unsigned offset)
- Line: 409
- Called by: omap_gpio_get, omap_gpio_irq_type

### omap_gpio_is_off_wakeup_capable
- Return type: static bool
- Signature: omap_gpio_is_off_wakeup_capable(struct gpio_bank * bank,u32 gpio_mask)
- Line: 263
- Called by: omap_set_gpio_trigger

### omap_gpio_mask_irq
- Return type: static void
- Signature: omap_gpio_mask_irq(struct irq_data * d)
- Line: 675
- Calls: gpiochip_disable_irq, omap_irq_data_get_bank, omap_set_gpio_irqenable, omap_set_gpio_triggering

### omap_gpio_mod_init
- Return type: static void
- Signature: omap_gpio_mod_init(struct gpio_bank * bank)
- Line: 1006
- Calls: omap_gpio_rmw
- Called by: omap_gpio_probe

### omap_gpio_output
- Return type: static int
- Signature: omap_gpio_output(struct gpio_chip * chip,unsigned offset,int value)
- Line: 880
- Calls: gpiochip_get_data, omap_set_gpio_direction

### omap_gpio_probe
- Return type: static int
- Signature: omap_gpio_probe(struct platform_device * pdev)
- Line: 1400
- Calls: omap_gpio_chip_init, omap_gpio_mod_init, omap_gpio_show_rev, omap_mpuio_init

### omap_gpio_remove
- Return type: static void
- Signature: omap_gpio_remove(struct platform_device * pdev)
- Line: 1498
- Calls: gpiochip_remove

### omap_gpio_request
- Return type: static int
- Signature: omap_gpio_request(struct gpio_chip * chip,unsigned offset)
- Line: 813
- Calls: gpiochip_get_data, omap_enable_gpio_module

### omap_gpio_restore_context
- Return type: static void
- Signature: omap_gpio_restore_context(struct gpio_bank * bank)
- Line: 1116
- Called by: omap_gpio_unidle

### omap_gpio_resume
- Return type: static int
- Signature: omap_gpio_resume(struct device * dev)
- Line: 1547
- Calls: omap_gpio_runtime_resume

### omap_gpio_rmw
- Return type: static u32
- Signature: omap_gpio_rmw(void __iomem * reg,u32 mask,bool set)
- Line: 95
- Called by: omap2_set_gpio_debounce, omap_gpio_idle, omap_gpio_mod_init, omap_set_gpio_dataout_mask, omap_set_gpio_direction, omap_set_gpio_irqenable, omap_set_gpio_trigger

### omap_gpio_runtime_resume
- Return type: static int
- Signature: omap_gpio_runtime_resume(struct device * dev)
- Line: 1522
- Calls: omap_gpio_unidle
- Called by: omap_gpio_resume

### omap_gpio_runtime_suspend
- Return type: static int
- Signature: omap_gpio_runtime_suspend(struct device * dev)
- Line: 1509
- Calls: omap_gpio_idle
- Called by: omap_gpio_suspend

### omap_gpio_set
- Return type: static int
- Signature: omap_gpio_set(struct gpio_chip * chip,unsigned int offset,int value)
- Line: 959
- Calls: gpiochip_get_data

### omap_gpio_set_config
- Return type: static int
- Signature: omap_gpio_set_config(struct gpio_chip * chip,unsigned offset,unsigned long config)
- Line: 936
- Calls: gpiochip_generic_config, omap_gpio_debounce

### omap_gpio_set_multiple
- Return type: static int
- Signature: omap_gpio_set_multiple(struct gpio_chip * chip,unsigned long * mask,unsigned long * bits)
- Line: 972
- Calls: gpiochip_get_data

### omap_gpio_show_rev
- Return type: static void
- Signature: omap_gpio_show_rev(struct gpio_bank * bank)
- Line: 991
- Called by: omap_gpio_probe

### omap_gpio_suspend
- Return type: static int
- Signature: omap_gpio_suspend(struct device * dev)
- Line: 1535
- Calls: omap_gpio_runtime_suspend

### omap_gpio_unidle
- Return type: static void
- Signature: omap_gpio_unidle(struct gpio_bank * bank)
- Line: 1188
- Calls: omap_gpio_dbck_enable, omap_gpio_init_context, omap_gpio_restore_context
- Called by: gpio_omap_cpu_notifier, omap_gpio_runtime_resume

### omap_gpio_unmask_irq
- Return type: static void
- Signature: omap_gpio_unmask_irq(struct irq_data * d)
- Line: 688
- Calls: gpiochip_enable_irq, omap_clear_gpio_irqstatus, omap_irq_data_get_bank, omap_set_gpio_irqenable, omap_set_gpio_triggering
- Called by: omap_gpio_irq_startup

### omap_gpio_wake_enable
- Return type: static int
- Signature: omap_gpio_wake_enable(struct irq_data * d,unsigned int enable)
- Line: 543
- Calls: omap_irq_data_get_bank

### omap_irq_data_get_bank
- Return type: static gpio_bank *
- Signature: omap_irq_data_get_bank(struct irq_data * d)
- Line: 89
- Calls: gpiochip_get_data
- Called by: gpio_irq_bus_sync_unlock, omap_gpio_irq_bus_lock, omap_gpio_irq_print_chip, omap_gpio_irq_shutdown, omap_gpio_irq_startup, omap_gpio_irq_type, omap_gpio_mask_irq, omap_gpio_unmask_irq, omap_gpio_wake_enable

### omap_mpuio_init
- Return type: static void
- Signature: omap_mpuio_init(struct gpio_bank * bank)
- Line: 800
- Called by: omap_gpio_probe

### omap_mpuio_resume_noirq
- Return type: static int
- Signature: omap_mpuio_resume_noirq(struct device * dev)
- Line: 764

### omap_mpuio_suspend_noirq
- Return type: static int
- Signature: omap_mpuio_suspend_noirq(struct device * dev)
- Line: 750

### omap_set_gpio_dataout_mask
- Return type: static void
- Signature: omap_set_gpio_dataout_mask(struct gpio_bank * bank,unsigned offset,int enable)
- Line: 136
- Calls: omap_gpio_rmw

### omap_set_gpio_dataout_reg
- Return type: static void
- Signature: omap_set_gpio_dataout_reg(struct gpio_bank * bank,unsigned offset,int enable)
- Line: 118

### omap_set_gpio_direction
- Return type: static void
- Signature: omap_set_gpio_direction(struct gpio_bank * bank,int gpio,int is_input)
- Line: 109
- Calls: omap_gpio_rmw
- Called by: omap_gpio_free, omap_gpio_init_irq, omap_gpio_input, omap_gpio_irq_startup, omap_gpio_output

### omap_set_gpio_irqenable
- Return type: static void
- Signature: omap_set_gpio_irqenable(struct gpio_bank * bank,unsigned offset,int enable)
- Line: 507
- Calls: omap_gpio_rmw
- Called by: omap_gpio_irq_shutdown, omap_gpio_mask_irq, omap_gpio_unmask_irq

### omap_set_gpio_trigger
- Return type: static void
- Signature: omap_set_gpio_trigger(struct gpio_bank * bank,int gpio,unsigned trigger)
- Line: 273
- Calls: omap_gpio_is_off_wakeup_capable, omap_gpio_rmw
- Called by: omap_set_gpio_triggering

### omap_set_gpio_triggering
- Return type: static int
- Signature: omap_set_gpio_triggering(struct gpio_bank * bank,int gpio,unsigned trigger)
- Line: 334
- Calls: omap_set_gpio_trigger
- Called by: omap_gpio_irq_shutdown, omap_gpio_irq_type, omap_gpio_mask_irq, omap_gpio_unmask_irq

### omap_toggle_gpio_edge_triggering
- Return type: static void
- Signature: omap_toggle_gpio_edge_triggering(struct gpio_bank * bank,int gpio)
- Line: 325
- Called by: omap_gpio_irq_handler

## Structs (2)

### gpio_bank
- Line: 47
- Members:
  - sysconfig: u32
  - irqenable1: u32
  - irqenable2: u32
  - wake_en: u32
  - ctrl: u32
  - oe: u32
  - leveldetect0: u32
  - leveldetect1: u32
  - risingdetect: u32
  - fallingdetect: u32
  - dataout: u32
  - debounce: u32
  - debounce_en: u32
  - base: void __iomem *
  - regs: const struct omap_gpio_reg_offs *
  - dev: device *
  - irq: int
  - non_wakeup_gpios: u32
  - enabled_non_wakeup_gpios: u32
  - context: gpio_regs
  - saved_datain: u32
  - level_mask: u32
  - toggle_mask: u32
  - lock: raw_spinlock_t
  - wa_lock: raw_spinlock_t
  - chip: gpio_chip
  - dbck: clk *
  - nb: notifier_block
  - is_suspended: unsigned int:1
  - needs_resume: unsigned int:1
  - mod_usage: u32
  - irq_usage: u32
  - dbck_enable_mask: u32
  - dbck_enabled: bool
  - is_mpuio: bool
  - dbck_flag: bool
  - loses_context: bool
  - context_valid: bool
  - stride: int
  - width: u32
  - context_loss_count: int
  - set_dataout: void (*)(struct gpio_bank * bank,unsigned gpio,int enable)
  - get_context_loss_count: int (*)(struct device * dev)

### gpio_regs
- Line: 31
- Members:
  - sysconfig: u32
  - irqenable1: u32
  - irqenable2: u32
  - wake_en: u32
  - ctrl: u32
  - oe: u32
  - leveldetect0: u32
  - leveldetect1: u32
  - risingdetect: u32
  - fallingdetect: u32
  - dataout: u32
  - debounce: u32
  - debounce_en: u32
  - base: void __iomem *
  - regs: const struct omap_gpio_reg_offs *
  - dev: device *
  - irq: int
  - non_wakeup_gpios: u32
  - enabled_non_wakeup_gpios: u32
  - context: gpio_regs
  - saved_datain: u32
  - level_mask: u32
  - toggle_mask: u32
  - lock: raw_spinlock_t
  - wa_lock: raw_spinlock_t
  - chip: gpio_chip
  - dbck: clk *
  - nb: notifier_block
  - is_suspended: unsigned int:1
  - needs_resume: unsigned int:1
  - mod_usage: u32
  - irq_usage: u32
  - dbck_enable_mask: u32
  - dbck_enabled: bool
  - is_mpuio: bool
  - dbck_flag: bool
  - inp_state: unsigned long
  - loses_context: bool
  - context_valid: bool
  - outp_state: unsigned long
  - outp_set: unsigned long
  - stride: int
  - outp_clr: unsigned long
  - width: u32
  - context_loss_count: int
  - dir_set: unsigned long
  - dir_clr: unsigned long
  - set_dataout: void (*)(struct gpio_bank * bank,unsigned gpio,int enable)
  - get_context_loss_count: int (*)(struct device * dev)
  - datamsw: u32[]
  - datalsw: u32[]
  - dirm: u32[]
  - outen: u32[]
  - int_en: u32[]
  - int_dis: u32[]
  - int_type: u32[]
  - int_polarity: u32[]
  - int_any: u32[]
  - chip: gpio_chip
  - base_addr: void __iomem *
  - clk: clk *
  - irq: int
  - p_data: const struct zynq_platform_data *
  - context: gpio_regs
  - dirlock: spinlock_t
  - label: const char *
  - quirks: u32
  - ngpio: u16
  - max_bank: int
  - bank_min: int[]
  - bank_max: int[]
  - chip: gpio_chip
  - gpio_grp: gpio_regs *
  - reg_base: void __iomem *

## Variables (13)

- static **gpio_pm_ops** : const struct dev_pm_ops (line 1559)
- static **omap2_gpio_regs** : const struct omap_gpio_reg_offs (line 1315)
- static **omap2_pdata** : const struct omap_gpio_platform_data (line 1365)
- static **omap3_pdata** : const struct omap_gpio_platform_data (line 1371)
- static **omap4_gpio_regs** : const struct omap_gpio_reg_offs (line 1339)
- static **omap4_pdata** : const struct omap_gpio_platform_data (line 1377)
- static **omap_gpio_driver** : platform_driver (line 1564)
- static **omap_gpio_irq_chip** : const struct irq_chip (line 721)
- static **omap_gpio_irq_chip_nowake** : const struct irq_chip (line 735)
- static **omap_gpio_match** : const struct of_device_id[] (line 1383)
- static **omap_mpuio_dev_pm_ops** : const struct dev_pm_ops (line 778)
- static **omap_mpuio_device** : platform_device (line 791)
- static **omap_mpuio_driver** : platform_driver (line 784)

## Macros (4)

- **BANK_USED**(bank) (line 84)
- **GPIO_MOD_CTRL_BIT** (line 82)
- **LINE_USED**(line,offset) (line 85)
- **OMAP4_GPIO_DEBOUNCINGTIME_MASK** (line 29)
