# drivers/gpio/gpio-zynq.c

Subsystem: drivers/gpio

## Functions (28)

### gpio_data_ro_bug
- Return type: static int
- Signature: gpio_data_ro_bug(struct zynq_gpio * gpio)
- Line: 174
- Called by: zynq_gpio_get_value

### zynq_gpio_dir_in
- Return type: static int
- Signature: zynq_gpio_dir_in(struct gpio_chip * chip,unsigned int pin)
- Line: 307
- Calls: gpiochip_get_data, zynq_gpio_get_bank_pin, zynq_gpio_is_zynq

### zynq_gpio_dir_out
- Return type: static int
- Signature: zynq_gpio_dir_out(struct gpio_chip * chip,unsigned int pin,int state)
- Line: 346
- Calls: gpiochip_get_data, zynq_gpio_get_bank_pin, zynq_gpio_set_value

### zynq_gpio_free
- Return type: static void
- Signature: zynq_gpio_free(struct gpio_chip * chip,unsigned int offset)
- Line: 811

### zynq_gpio_get_bank_pin
- Return type: static void
- Signature: zynq_gpio_get_bank_pin(unsigned int pin_num,unsigned int * bank_num,unsigned int * bank_pin_num,struct zynq_gpio * gpio)
- Line: 191
- Called by: zynq_gpio_dir_in, zynq_gpio_dir_out, zynq_gpio_get_direction, zynq_gpio_get_value, zynq_gpio_irq_ack, zynq_gpio_irq_mask, zynq_gpio_irq_unmask, zynq_gpio_set_irq_type, zynq_gpio_set_value

### zynq_gpio_get_direction
- Return type: static int
- Signature: zynq_gpio_get_direction(struct gpio_chip * chip,unsigned int pin)
- Line: 382
- Calls: gpiochip_get_data, zynq_gpio_get_bank_pin

### zynq_gpio_get_value
- Return type: static int
- Signature: zynq_gpio_get_value(struct gpio_chip * chip,unsigned int pin)
- Line: 225
- Calls: gpio_data_ro_bug, gpiochip_get_data, zynq_gpio_get_bank_pin, zynq_gpio_is_zynq

### zynq_gpio_handle_bank_irq
- Return type: static void
- Signature: zynq_gpio_handle_bank_irq(struct zynq_gpio * gpio,unsigned int bank_num,unsigned long pending)
- Line: 628
- Called by: zynq_gpio_irqhandler

### zynq_gpio_irq_ack
- Return type: static void
- Signature: zynq_gpio_irq_ack(struct irq_data * irq_data)
- Line: 453
- Calls: gpiochip_get_data, zynq_gpio_get_bank_pin
- Called by: zynq_gpio_irq_enable

### zynq_gpio_irq_enable
- Return type: static void
- Signature: zynq_gpio_irq_enable(struct irq_data * irq_data)
- Line: 472
- Calls: zynq_gpio_irq_ack, zynq_gpio_irq_unmask

### zynq_gpio_irq_mask
- Return type: static void
- Signature: zynq_gpio_irq_mask(struct irq_data * irq_data)
- Line: 406
- Calls: gpiochip_disable_irq, gpiochip_get_data, zynq_gpio_get_bank_pin

### zynq_gpio_irq_relres
- Return type: static void
- Signature: zynq_gpio_irq_relres(struct irq_data * d)
- Line: 592
- Calls: gpiochip_relres_irq

### zynq_gpio_irq_reqres
- Return type: static int
- Signature: zynq_gpio_irq_reqres(struct irq_data * d)
- Line: 580
- Calls: gpiochip_reqres_irq

### zynq_gpio_irq_unmask
- Return type: static void
- Signature: zynq_gpio_irq_unmask(struct irq_data * irq_data)
- Line: 430
- Calls: gpiochip_enable_irq, gpiochip_get_data, zynq_gpio_get_bank_pin
- Called by: zynq_gpio_irq_enable

### zynq_gpio_irqhandler
- Return type: static void
- Signature: zynq_gpio_irqhandler(struct irq_desc * desc)
- Line: 653
- Calls: gpiochip_get_data, zynq_gpio_handle_bank_irq

### zynq_gpio_is_zynq
- Return type: static int
- Signature: zynq_gpio_is_zynq(struct zynq_gpio * gpio)
- Line: 163
- Called by: zynq_gpio_dir_in, zynq_gpio_get_value

### zynq_gpio_probe
- Return type: static int
- Signature: zynq_gpio_probe(struct platform_device * pdev)
- Line: 900

### zynq_gpio_remove
- Return type: static void
- Signature: zynq_gpio_remove(struct platform_device * pdev)
- Line: 1005
- Calls: gpiochip_remove

### zynq_gpio_request
- Return type: static int
- Signature: zynq_gpio_request(struct gpio_chip * chip,unsigned int offset)
- Line: 798

### zynq_gpio_restore_context
- Return type: static void
- Signature: zynq_gpio_restore_context(struct zynq_gpio * gpio)
- Line: 705
- Called by: zynq_gpio_resume

### zynq_gpio_resume
- Return type: static int
- Signature: zynq_gpio_resume(struct device * dev)
- Line: 759
- Calls: zynq_gpio_restore_context

### zynq_gpio_runtime_resume
- Return type: static int
- Signature: zynq_gpio_runtime_resume(struct device * dev)
- Line: 791

### zynq_gpio_runtime_suspend
- Return type: static int
- Signature: zynq_gpio_runtime_suspend(struct device * dev)
- Line: 782

### zynq_gpio_save_context
- Return type: static void
- Signature: zynq_gpio_save_context(struct zynq_gpio * gpio)
- Line: 676
- Called by: zynq_gpio_suspend

### zynq_gpio_set_irq_type
- Return type: static int
- Signature: zynq_gpio_set_irq_type(struct irq_data * irq_data,unsigned int type)
- Line: 503
- Calls: gpiochip_get_data, zynq_gpio_get_bank_pin

### zynq_gpio_set_value
- Return type: static int
- Signature: zynq_gpio_set_value(struct gpio_chip * chip,unsigned int pin,int state)
- Line: 268
- Calls: gpiochip_get_data, zynq_gpio_get_bank_pin
- Called by: zynq_gpio_dir_out

### zynq_gpio_set_wake
- Return type: static int
- Signature: zynq_gpio_set_wake(struct irq_data * data,unsigned int on)
- Line: 570
- Calls: gpiochip_get_data

### zynq_gpio_suspend
- Return type: static int
- Signature: zynq_gpio_suspend(struct device * dev)
- Line: 738
- Calls: zynq_gpio_save_context

## Structs (3)

### gpio_regs
- Line: 104
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

### zynq_gpio
- Line: 126
- Members:
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

### zynq_platform_data
- Line: 145
- Members:
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

## Variables (11)

- static **pmc_gpio_def** : const struct zynq_platform_data (line 832)
- static **versal_gpio_def** : const struct zynq_platform_data (line 821)
- static **zynq_gpio_def** : const struct zynq_platform_data (line 865)
- static **zynq_gpio_dev_pm_ops** : const struct dev_pm_ops (line 816)
- static **zynq_gpio_driver** : platform_driver (line 1019)
- static **zynq_gpio_edge_irqchip** : const struct irq_chip (line 615)
- static **zynq_gpio_edge_irqchip** : const struct irq_chip (line 155)
- static **zynq_gpio_level_irqchip** : const struct irq_chip (line 601)
- static **zynq_gpio_level_irqchip** : const struct irq_chip (line 154)
- static **zynq_gpio_of_match** : const struct of_device_id[] (line 880)
- static **zynqmp_gpio_def** : const struct zynq_platform_data (line 846)

## Macros (49)

- **DRIVER_NAME** (line 20)
- **GPIO_QUIRK_DATA_RO_BUG** (line 101)
- **GPIO_QUIRK_VERSAL** (line 102)
- **PMC_GPIO_MAX_BANK** (line 26)
- **VERSAL_GPIO_MAX_BANK** (line 25)
- **VERSAL_UNUSED_BANKS** (line 27)
- **ZYNQMP_GPIO_BANK0_NGPIO** (line 34)
- **ZYNQMP_GPIO_BANK1_NGPIO** (line 35)
- **ZYNQMP_GPIO_BANK2_NGPIO** (line 36)
- **ZYNQMP_GPIO_BANK3_NGPIO** (line 37)
- **ZYNQMP_GPIO_BANK4_NGPIO** (line 38)
- **ZYNQMP_GPIO_BANK5_NGPIO** (line 39)
- **ZYNQMP_GPIO_MAX_BANK** (line 24)
- **ZYNQMP_GPIO_NR_GPIOS** (line 42)
- **ZYNQ_GPIO_BANK0_NGPIO** (line 29)
- **ZYNQ_GPIO_BANK0_PIN_MAX**(str) (line 45)
- **ZYNQ_GPIO_BANK0_PIN_MIN**(str) (line 44)
- **ZYNQ_GPIO_BANK1_NGPIO** (line 30)
- **ZYNQ_GPIO_BANK1_PIN_MAX**(str) (line 48)
- **ZYNQ_GPIO_BANK1_PIN_MIN**(str) (line 47)
- **ZYNQ_GPIO_BANK2_NGPIO** (line 31)
- **ZYNQ_GPIO_BANK2_PIN_MAX**(str) (line 51)
- **ZYNQ_GPIO_BANK2_PIN_MIN**(str) (line 50)
- **ZYNQ_GPIO_BANK3_NGPIO** (line 32)
- **ZYNQ_GPIO_BANK3_PIN_MAX**(str) (line 54)
- **ZYNQ_GPIO_BANK3_PIN_MIN**(str) (line 53)
- **ZYNQ_GPIO_BANK4_PIN_MAX**(str) (line 57)
- **ZYNQ_GPIO_BANK4_PIN_MIN**(str) (line 56)
- **ZYNQ_GPIO_BANK5_PIN_MAX**(str) (line 60)
- **ZYNQ_GPIO_BANK5_PIN_MIN**(str) (line 59)
- **ZYNQ_GPIO_DATA_LSW_OFFSET**(BANK) (line 65)
- **ZYNQ_GPIO_DATA_MSW_OFFSET**(BANK) (line 67)
- **ZYNQ_GPIO_DATA_OFFSET**(BANK) (line 69)
- **ZYNQ_GPIO_DATA_RO_OFFSET**(BANK) (line 70)
- **ZYNQ_GPIO_DIRM_OFFSET**(BANK) (line 72)
- **ZYNQ_GPIO_INTANY_OFFSET**(BANK) (line 88)
- **ZYNQ_GPIO_INTDIS_OFFSET**(BANK) (line 80)
- **ZYNQ_GPIO_INTEN_OFFSET**(BANK) (line 78)
- **ZYNQ_GPIO_INTMASK_OFFSET**(BANK) (line 76)
- **ZYNQ_GPIO_INTPOL_OFFSET**(BANK) (line 86)
- **ZYNQ_GPIO_INTSTS_OFFSET**(BANK) (line 82)
- **ZYNQ_GPIO_INTTYPE_OFFSET**(BANK) (line 84)
- **ZYNQ_GPIO_IXR_DISABLE_ALL** (line 91)
- **ZYNQ_GPIO_MAX_BANK** (line 23)
- **ZYNQ_GPIO_MID_PIN_NUM** (line 94)
- **ZYNQ_GPIO_NR_GPIOS** (line 41)
- **ZYNQ_GPIO_OUTEN_OFFSET**(BANK) (line 74)
- **ZYNQ_GPIO_QUIRK_IS_ZYNQ** (line 100)
- **ZYNQ_GPIO_UPPER_MASK** (line 97)
