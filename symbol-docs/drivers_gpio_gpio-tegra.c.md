# drivers/gpio/gpio-tegra.c

Subsystem: drivers/gpio

## Functions (33)

### tegra_dbg_gpio_show
- Return type: static int
- Signature: tegra_dbg_gpio_show(struct seq_file * s,void * unused)
- Line: 643
- Calls: tegra_gpio_compose, tegra_gpio_readl

### tegra_gpio_child_to_parent_hwirq
- Return type: static int
- Signature: tegra_gpio_child_to_parent_hwirq(struct gpio_chip * chip,unsigned int hwirq,unsigned int type,unsigned int * parent_hwirq,unsigned int * parent_type)
- Line: 434

### tegra_gpio_compose
- Return type: static unsigned int
- Signature: tegra_gpio_compose(unsigned int bank,unsigned int port,unsigned int bit)
- Line: 114
- Called by: tegra_dbg_gpio_show, tegra_gpio_irq_handler, tegra_gpio_probe

### tegra_gpio_debuginit
- Return type: static void
- Signature: tegra_gpio_debuginit(struct tegra_gpio_info * tgi)
- Line: 675
- Called by: tegra_gpio_probe

### tegra_gpio_debuginit
- Return type: static void
- Signature: tegra_gpio_debuginit(struct tegra_gpio_info * tgi)
- Line: 667
- Called by: tegra_gpio_probe

### tegra_gpio_direction_input
- Return type: static int
- Signature: tegra_gpio_direction_input(struct gpio_chip * chip,unsigned int offset)
- Line: 171
- Calls: gpiochip_get_data, tegra_gpio_enable, tegra_gpio_mask_write

### tegra_gpio_direction_output
- Return type: static int
- Signature: tegra_gpio_direction_output(struct gpio_chip * chip,unsigned int offset,int value)
- Line: 189
- Calls: gpiochip_get_data, tegra_gpio_enable, tegra_gpio_mask_write, tegra_gpio_set

### tegra_gpio_disable
- Return type: static void
- Signature: tegra_gpio_disable(struct tegra_gpio_info * tgi,unsigned int gpio)
- Line: 136
- Calls: tegra_gpio_mask_write
- Called by: tegra_gpio_free, tegra_gpio_irq_release_resources, tegra_gpio_irq_set_type

### tegra_gpio_enable
- Return type: static void
- Signature: tegra_gpio_enable(struct tegra_gpio_info * tgi,unsigned int gpio)
- Line: 131
- Calls: tegra_gpio_mask_write
- Called by: tegra_gpio_direction_input, tegra_gpio_direction_output, tegra_gpio_irq_request_resources, tegra_gpio_irq_set_type

### tegra_gpio_free
- Return type: static void
- Signature: tegra_gpio_free(struct gpio_chip * chip,unsigned int offset)
- Line: 141
- Calls: gpiochip_get_data, tegra_gpio_disable

### tegra_gpio_get
- Return type: static int
- Signature: tegra_gpio_get(struct gpio_chip * chip,unsigned int offset)
- Line: 159
- Calls: gpiochip_get_data, tegra_gpio_readl

### tegra_gpio_get_direction
- Return type: static int
- Signature: tegra_gpio_get_direction(struct gpio_chip * chip,unsigned int offset)
- Line: 209
- Calls: gpiochip_get_data, tegra_gpio_readl

### tegra_gpio_irq_ack
- Return type: static void
- Signature: tegra_gpio_irq_ack(struct irq_data * d)
- Line: 273
- Calls: gpiochip_get_data, tegra_gpio_writel

### tegra_gpio_irq_handler
- Return type: static void
- Signature: tegra_gpio_irq_handler(struct irq_desc * desc)
- Line: 380
- Calls: tegra_gpio_compose, tegra_gpio_readl, tegra_gpio_writel

### tegra_gpio_irq_mask
- Return type: static void
- Signature: tegra_gpio_irq_mask(struct irq_data * d)
- Line: 282
- Calls: gpiochip_disable_irq, gpiochip_get_data, tegra_gpio_mask_write
- Called by: tegra_gpio_irq_shutdown

### tegra_gpio_irq_print_chip
- Return type: static void
- Signature: tegra_gpio_irq_print_chip(struct irq_data * d,struct seq_file * s)
- Line: 601

### tegra_gpio_irq_release_resources
- Return type: static void
- Signature: tegra_gpio_irq_release_resources(struct irq_data * d)
- Line: 592
- Calls: gpiochip_get_data, gpiochip_relres_irq, tegra_gpio_disable

### tegra_gpio_irq_request_resources
- Return type: static int
- Signature: tegra_gpio_irq_request_resources(struct irq_data * d)
- Line: 582
- Calls: gpiochip_get_data, gpiochip_reqres_irq, tegra_gpio_enable

### tegra_gpio_irq_set_affinity
- Return type: static int
- Signature: tegra_gpio_irq_set_affinity(struct irq_data * data,const struct cpumask * dest,bool force)
- Line: 572

### tegra_gpio_irq_set_type
- Return type: static int
- Signature: tegra_gpio_irq_set_type(struct irq_data * d,unsigned int type)
- Line: 302
- Calls: gpiochip_get_data, gpiochip_lock_as_irq, tegra_gpio_disable, tegra_gpio_enable, tegra_gpio_mask_write, tegra_gpio_readl, tegra_gpio_writel

### tegra_gpio_irq_set_wake
- Return type: static int
- Signature: tegra_gpio_irq_set_wake(struct irq_data * d,unsigned int enable)
- Line: 536
- Calls: gpiochip_get_data

### tegra_gpio_irq_shutdown
- Return type: static void
- Signature: tegra_gpio_irq_shutdown(struct irq_data * d)
- Line: 370
- Calls: gpiochip_get_data, gpiochip_unlock_as_irq, tegra_gpio_irq_mask

### tegra_gpio_irq_unmask
- Return type: static void
- Signature: tegra_gpio_irq_unmask(struct irq_data * d)
- Line: 292
- Calls: gpiochip_enable_irq, gpiochip_get_data, tegra_gpio_mask_write

### tegra_gpio_mask_write
- Return type: static void
- Signature: tegra_gpio_mask_write(struct tegra_gpio_info * tgi,u32 reg,unsigned int gpio,u32 value)
- Line: 120
- Calls: tegra_gpio_writel
- Called by: tegra_gpio_direction_input, tegra_gpio_direction_output, tegra_gpio_disable, tegra_gpio_enable, tegra_gpio_irq_mask, tegra_gpio_irq_set_type, tegra_gpio_irq_unmask, tegra_gpio_set, tegra_gpio_set_debounce

### tegra_gpio_populate_parent_fwspec
- Return type: static int
- Signature: tegra_gpio_populate_parent_fwspec(struct gpio_chip * chip,union gpio_irq_fwspec * gfwspec,unsigned int parent_hwirq,unsigned int parent_type)
- Line: 446

### tegra_gpio_probe
- Return type: static int
- Signature: tegra_gpio_probe(struct platform_device * pdev)
- Line: 690
- Calls: tegra_gpio_compose, tegra_gpio_debuginit, tegra_gpio_writel

### tegra_gpio_readl
- Return type: static u32
- Signature: tegra_gpio_readl(struct tegra_gpio_info * tgi,u32 reg)
- Line: 109
- Called by: tegra_dbg_gpio_show, tegra_gpio_get, tegra_gpio_get_direction, tegra_gpio_irq_handler, tegra_gpio_irq_set_type, tegra_gpio_suspend

### tegra_gpio_resume
- Return type: static int
- Signature: tegra_gpio_resume(struct device * dev)
- Line: 463
- Calls: tegra_gpio_writel

### tegra_gpio_set
- Return type: static int
- Signature: tegra_gpio_set(struct gpio_chip * chip,unsigned int offset,int value)
- Line: 149
- Calls: gpiochip_get_data, tegra_gpio_mask_write
- Called by: tegra_gpio_direction_output

### tegra_gpio_set_config
- Return type: static int
- Signature: tegra_gpio_set_config(struct gpio_chip * chip,unsigned int offset,unsigned long config)
- Line: 261
- Calls: tegra_gpio_set_debounce

### tegra_gpio_set_debounce
- Return type: static int
- Signature: tegra_gpio_set_debounce(struct gpio_chip * chip,unsigned int offset,unsigned int debounce)
- Line: 228
- Calls: gpiochip_get_data, tegra_gpio_mask_write, tegra_gpio_writel
- Called by: tegra_gpio_set_config

### tegra_gpio_suspend
- Return type: static int
- Signature: tegra_gpio_suspend(struct device * dev)
- Line: 498
- Calls: tegra_gpio_readl, tegra_gpio_writel

### tegra_gpio_writel
- Return type: static void
- Signature: tegra_gpio_writel(struct tegra_gpio_info * tgi,u32 val,u32 reg)
- Line: 103
- Called by: tegra_gpio_irq_ack, tegra_gpio_irq_handler, tegra_gpio_irq_set_type, tegra_gpio_mask_write, tegra_gpio_probe, tegra_gpio_resume, tegra_gpio_set_debounce, tegra_gpio_suspend

## Structs (3)

### tegra_gpio_bank
- Line: 63
- Members:
  - bank: unsigned int
  - lvl_lock: raw_spinlock_t[4]
  - dbc_lock: spinlock_t[4]
  - cnf: u32[4]
  - out: u32[4]
  - oe: u32[4]
  - int_enb: u32[4]
  - int_lvl: u32[4]
  - wake_enb: u32[4]
  - dbc_enb: u32[4]
  - dbc_cnt: u32[4]
  - debounce_supported: bool
  - bank_stride: u32
  - upper_offset: u32
  - dev: device *
  - regs: void __iomem *
  - bank_info: tegra_gpio_bank *
  - soc: const struct tegra_gpio_soc_config *
  - gc: gpio_chip
  - bank_count: u32
  - irqs: unsigned int *

### tegra_gpio_info
- Line: 93
- Members:
  - bank: unsigned int
  - lvl_lock: raw_spinlock_t[4]
  - dbc_lock: spinlock_t[4]
  - cnf: u32[4]
  - out: u32[4]
  - oe: u32[4]
  - int_enb: u32[4]
  - int_lvl: u32[4]
  - wake_enb: u32[4]
  - dbc_enb: u32[4]
  - dbc_cnt: u32[4]
  - debounce_supported: bool
  - bank_stride: u32
  - upper_offset: u32
  - dev: device *
  - regs: void __iomem *
  - bank_info: tegra_gpio_bank *
  - soc: const struct tegra_gpio_soc_config *
  - gc: gpio_chip
  - bank_count: u32
  - irqs: unsigned int *

### tegra_gpio_soc_config
- Line: 87
- Members:
  - bank: unsigned int
  - lvl_lock: raw_spinlock_t[4]
  - dbc_lock: spinlock_t[4]
  - cnf: u32[4]
  - out: u32[4]
  - oe: u32[4]
  - int_enb: u32[4]
  - int_lvl: u32[4]
  - wake_enb: u32[4]
  - dbc_enb: u32[4]
  - dbc_cnt: u32[4]
  - debounce_supported: bool
  - bank_stride: u32
  - upper_offset: u32
  - dev: device *
  - regs: void __iomem *
  - bank_info: tegra_gpio_bank *
  - soc: const struct tegra_gpio_soc_config *
  - gc: gpio_chip
  - bank_count: u32
  - irqs: unsigned int *

## Variables (9)

- static **tegra20_gpio_config** : const struct tegra_gpio_soc_config (line 805)
- static **tegra210_gpio_config** : const struct tegra_gpio_soc_config (line 815)
- static **tegra210_gpio_irq_chip** : const struct irq_chip (line 623)
- static **tegra30_gpio_config** : const struct tegra_gpio_soc_config (line 810)
- static **tegra_gpio_driver** : platform_driver (line 829)
- static **tegra_gpio_irq_chip** : const struct irq_chip (line 608)
- static **tegra_gpio_of_match** : const struct of_device_id[] (line 821)
- static **tegra_gpio_pm_ops** : const struct dev_pm_ops (line 681)
- static **tegra_pmc_of_match** : const struct of_device_id[] (line 685)

## Macros (26)

- **GPIO_BANK**(x) (line 28)
- **GPIO_BIT**(x) (line 30)
- **GPIO_CNF**(t,x) (line 35)
- **GPIO_DBC_CNT**(t,x) (line 43)
- **GPIO_IN**(t,x) (line 38)
- **GPIO_INT_CLR**(t,x) (line 42)
- **GPIO_INT_ENB**(t,x) (line 40)
- **GPIO_INT_LVL**(t,x) (line 41)
- **GPIO_INT_LVL_EDGE_BOTH** (line 57)
- **GPIO_INT_LVL_EDGE_FALLING** (line 56)
- **GPIO_INT_LVL_EDGE_RISING** (line 55)
- **GPIO_INT_LVL_LEVEL_HIGH** (line 58)
- **GPIO_INT_LVL_LEVEL_LOW** (line 59)
- **GPIO_INT_LVL_MASK** (line 54)
- **GPIO_INT_STA**(t,x) (line 39)
- **GPIO_MSK_CNF**(t,x) (line 46)
- **GPIO_MSK_DBC_EN**(t,x) (line 49)
- **GPIO_MSK_INT_ENB**(t,x) (line 51)
- **GPIO_MSK_INT_LVL**(t,x) (line 52)
- **GPIO_MSK_INT_STA**(t,x) (line 50)
- **GPIO_MSK_OE**(t,x) (line 47)
- **GPIO_MSK_OUT**(t,x) (line 48)
- **GPIO_OE**(t,x) (line 36)
- **GPIO_OUT**(t,x) (line 37)
- **GPIO_PORT**(x) (line 29)
- **GPIO_REG**(tgi,x) (line 32)
