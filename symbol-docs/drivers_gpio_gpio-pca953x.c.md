# drivers/gpio/gpio-pca953x.c

Subsystem: drivers/gpio

## Functions (48)

### device_pca957x_init
- Return type: static int
- Signature: device_pca957x_init(struct pca953x_chip * chip)
- Line: 1143
- Calls: device_pca95xx_init, pca953x_write_regs
- Called by: pca953x_probe

### device_pca95xx_init
- Return type: static int
- Signature: device_pca95xx_init(struct pca953x_chip * chip)
- Line: 1119
- Calls: pca953x_write_regs
- Called by: device_pca957x_init, pca953x_probe

### pca953x_acpi_get_irq
- Return type: static int
- Signature: pca953x_acpi_get_irq(struct device * dev)
- Line: 148
- Calls: devm_acpi_dev_add_driver_gpios
- Called by: pca953x_irq_setup

### pca953x_bank_shift
- Return type: static int
- Signature: pca953x_bank_shift(struct pca953x_chip * chip)
- Line: 251
- Called by: pca953x_check_register, pca953x_recalc_addr

### pca953x_check_register
- Return type: static bool
- Signature: pca953x_check_register(struct pca953x_chip * chip,unsigned int reg,u32 checkbank)
- Line: 317
- Calls: pca953x_bank_shift

### pca953x_disable_regulator
- Return type: static void
- Signature: pca953x_disable_regulator(void * reg)
- Line: 1160

### pca953x_exit
- Return type: static void __exit
- Signature: pca953x_exit(void)
- Line: 1510

### pca953x_get_and_enable_regulator
- Return type: static int
- Signature: pca953x_get_and_enable_regulator(struct pca953x_chip * chip)
- Line: 1165
- Called by: pca953x_probe

### pca953x_get_bit_mask
- Return type: static u8
- Signature: pca953x_get_bit_mask(struct pca953x_chip * chip,unsigned int offset)
- Line: 261
- Called by: pca953x_gpio_direction_input, pca953x_gpio_direction_output, pca953x_gpio_get_direction, pca953x_gpio_get_value, pca953x_gpio_set_value

### pca953x_gpio_direction_input
- Return type: static int
- Signature: pca953x_gpio_direction_input(struct gpio_chip * gc,unsigned off)
- Line: 608
- Calls: gpiochip_get_data, pca953x_get_bit_mask
- Called by: pca953x_irq_bus_sync_unlock

### pca953x_gpio_direction_output
- Return type: static int
- Signature: pca953x_gpio_direction_output(struct gpio_chip * gc,unsigned off,int val)
- Line: 622
- Calls: gpiochip_get_data, pca953x_get_bit_mask

### pca953x_gpio_get_direction
- Return type: static int
- Signature: pca953x_gpio_get_direction(struct gpio_chip * gc,unsigned off)
- Line: 676
- Calls: gpiochip_get_data, pca953x_get_bit_mask

### pca953x_gpio_get_multiple
- Return type: static int
- Signature: pca953x_gpio_get_multiple(struct gpio_chip * gc,unsigned long * mask,unsigned long * bits)
- Line: 702
- Calls: gpiochip_get_data, pca953x_read_regs

### pca953x_gpio_get_value
- Return type: static int
- Signature: pca953x_gpio_get_value(struct gpio_chip * gc,unsigned off)
- Line: 648
- Calls: gpiochip_get_data, pca953x_get_bit_mask

### pca953x_gpio_set_config
- Return type: static int
- Signature: pca953x_gpio_set_config(struct gpio_chip * gc,unsigned int offset,unsigned long config)
- Line: 772
- Calls: gpiochip_get_data, pca953x_gpio_set_pull_up_down

### pca953x_gpio_set_multiple
- Return type: static int
- Signature: pca953x_gpio_set_multiple(struct gpio_chip * gc,unsigned long * mask,unsigned long * bits)
- Line: 718
- Calls: gpiochip_get_data, pca953x_read_regs, pca953x_write_regs

### pca953x_gpio_set_pull_up_down
- Return type: static int
- Signature: pca953x_gpio_set_pull_up_down(struct pca953x_chip * chip,unsigned int offset,unsigned long config)
- Line: 736
- Called by: pca953x_gpio_set_config

### pca953x_gpio_set_value
- Return type: static int
- Signature: pca953x_gpio_set_value(struct gpio_chip * gc,unsigned int off,int val)
- Line: 664
- Calls: gpiochip_get_data, pca953x_get_bit_mask

### pca953x_init
- Return type: static int __init
- Signature: pca953x_init(void)
- Line: 1499

### pca953x_irq_bus_lock
- Return type: static void
- Signature: pca953x_irq_bus_lock(struct irq_data * d)
- Line: 843
- Calls: gpiochip_get_data

### pca953x_irq_bus_sync_unlock
- Return type: static void
- Signature: pca953x_irq_bus_sync_unlock(struct irq_data * d)
- Line: 851
- Calls: gpiochip_get_data, pca953x_gpio_direction_input, pca953x_read_regs, pca953x_write_regs

### pca953x_irq_handler
- Return type: static irqreturn_t
- Signature: pca953x_irq_handler(int irq,void * devid)
- Line: 1017
- Calls: pca953x_irq_pending

### pca953x_irq_mask
- Return type: static void
- Signature: pca953x_irq_mask(struct irq_data * d)
- Line: 810
- Calls: gpiochip_disable_irq, gpiochip_get_data
- Called by: pca953x_irq_shutdown

### pca953x_irq_pending
- Return type: static bool
- Signature: pca953x_irq_pending(struct pca953x_chip * chip,unsigned long * pending)
- Line: 944
- Calls: pca953x_read_regs
- Called by: pca953x_irq_handler

### pca953x_irq_print_chip
- Return type: static void
- Signature: pca953x_irq_print_chip(struct irq_data * data,struct seq_file * p)
- Line: 924

### pca953x_irq_set_type
- Return type: static int
- Signature: pca953x_irq_set_type(struct irq_data * d,unsigned int type)
- Line: 890
- Calls: gpiochip_get_data

### pca953x_irq_set_wake
- Return type: static int
- Signature: pca953x_irq_set_wake(struct irq_data * d,unsigned int on)
- Line: 830
- Calls: gpiochip_get_data

### pca953x_irq_setup
- Return type: static int
- Signature: pca953x_irq_setup(struct pca953x_chip * chip,int irq_base)
- Line: 1048
- Calls: pca953x_acpi_get_irq, pca953x_read_regs
- Called by: pca953x_probe

### pca953x_irq_setup
- Return type: static int
- Signature: pca953x_irq_setup(struct pca953x_chip * chip,int irq_base)
- Line: 1107
- Calls: pca953x_acpi_get_irq, pca953x_read_regs
- Called by: pca953x_probe

### pca953x_irq_shutdown
- Return type: static void
- Signature: pca953x_irq_shutdown(struct irq_data * d)
- Line: 910
- Calls: gpiochip_get_data, pca953x_irq_mask

### pca953x_irq_unmask
- Return type: static void
- Signature: pca953x_irq_unmask(struct irq_data * d)
- Line: 820
- Calls: gpiochip_enable_irq, gpiochip_get_data

### pca953x_probe
- Return type: static int
- Signature: pca953x_probe(struct i2c_client * client)
- Line: 1187
- Calls: device_pca957x_init, device_pca95xx_init, devm_gpiod_get_optional, pca953x_get_and_enable_regulator, pca953x_irq_setup, pca953x_setup_gpio

### pca953x_read_regs
- Return type: static int
- Signature: pca953x_read_regs(struct pca953x_chip * chip,int reg,unsigned long * val)
- Line: 590
- Called by: pca953x_gpio_get_multiple, pca953x_gpio_set_multiple, pca953x_irq_bus_sync_unlock, pca953x_irq_pending, pca953x_irq_setup

### pca953x_readable_register
- Return type: static bool
- Signature: pca953x_readable_register(struct device * dev,unsigned int reg)
- Line: 407
- Calls: tca6418_check_register

### pca953x_recalc_addr
- Return type: static u8
- Signature: pca953x_recalc_addr(struct pca953x_chip * chip,int reg,int off)
- Line: 517
- Calls: pca953x_bank_shift

### pca953x_regcache_sync
- Return type: static int
- Signature: pca953x_regcache_sync(struct pca953x_chip * chip)
- Line: 1315
- Called by: pca953x_restore_context

### pca953x_restore_context
- Return type: static int
- Signature: pca953x_restore_context(struct pca953x_chip * chip)
- Line: 1364
- Calls: pca953x_regcache_sync
- Called by: pca953x_resume

### pca953x_resume
- Return type: static int
- Signature: pca953x_resume(struct device * dev)
- Line: 1405
- Calls: pca953x_restore_context

### pca953x_save_context
- Return type: static void
- Signature: pca953x_save_context(struct pca953x_chip * chip)
- Line: 1381
- Called by: pca953x_suspend

### pca953x_setup_gpio
- Return type: static void
- Signature: pca953x_setup_gpio(struct pca953x_chip * chip,int gpios)
- Line: 788
- Called by: pca953x_probe

### pca953x_suspend
- Return type: static int
- Signature: pca953x_suspend(struct device * dev)
- Line: 1391
- Calls: pca953x_save_context

### pca953x_volatile_register
- Return type: static bool
- Signature: pca953x_volatile_register(struct device * dev,unsigned int reg)
- Line: 462
- Calls: tca6418_check_register

### pca953x_write_regs
- Return type: static int
- Signature: pca953x_write_regs(struct pca953x_chip * chip,int reg,unsigned long * val)
- Line: 572
- Called by: device_pca957x_init, device_pca95xx_init, pca953x_gpio_set_multiple, pca953x_irq_bus_sync_unlock

### pca953x_writeable_register
- Return type: static bool
- Signature: pca953x_writeable_register(struct device * dev,unsigned int reg)
- Line: 436
- Calls: tca6418_check_register

### pcal6534_check_register
- Return type: static bool
- Signature: pcal6534_check_register(struct pca953x_chip * chip,unsigned int reg,u32 checkbank)
- Line: 349

### pcal6534_recalc_addr
- Return type: static u8
- Signature: pcal6534_recalc_addr(struct pca953x_chip * chip,int reg,int off)
- Line: 531

### tca6418_check_register
- Return type: static bool
- Signature: tca6418_check_register(struct pca953x_chip * chip,unsigned int reg,u32 access_type_mask)
- Line: 389
- Called by: pca953x_readable_register, pca953x_volatile_register, pca953x_writeable_register

### tca6418_recalc_addr
- Return type: static u8
- Signature: tca6418_recalc_addr(struct pca953x_chip * chip,int reg_base,int offset)
- Line: 562

## Structs (2)

### pca953x_chip
- Line: 223
- Members:
  - direction: int
  - output: int
  - input: int
  - invert: int
  - gpio_start: unsigned
  - i2c_lock: mutex
  - regmap: regmap *
  - irq_lock: mutex
  - wakeup_path: atomic_t
  - client: i2c_client *
  - gpio_chip: gpio_chip
  - driver_data: unsigned long
  - regulator: regulator *
  - regs: const struct pca953x_reg_config *
  - recalc_addr: u8 (*)(struct pca953x_chip * chip,int reg,int off)
  - check_reg: bool (*)(struct pca953x_chip * chip,unsigned int reg,u32 checkbank)

### pca953x_reg_config
- Line: 195
- Members:
  - direction: int
  - output: int
  - input: int
  - invert: int
  - gpio_start: unsigned
  - i2c_lock: mutex
  - regmap: regmap *
  - irq_lock: mutex
  - wakeup_path: atomic_t
  - client: i2c_client *
  - gpio_chip: gpio_chip
  - driver_data: unsigned long
  - regulator: regulator *
  - regs: const struct pca953x_reg_config *
  - recalc_addr: u8 (*)(struct pca953x_chip * chip,int reg,int off)
  - check_reg: bool (*)(struct pca953x_chip * chip,unsigned int reg,u32 checkbank)

## Variables (13)

- static **pca953x_acpi_ids** : const struct acpi_device_id[] (line 183)
- static **pca953x_acpi_irq_gpios** : const struct acpi_gpio_mapping[] (line 143)
- static **pca953x_ai_i2c_regmap** : const struct regmap_config (line 501)
- static **pca953x_dmi_acpi_irq_info** : const struct dmi_system_id[] (line 164)
- static **pca953x_driver** : i2c_driver (line 1488)
- static **pca953x_dt_ids** : const struct of_device_id[] (line 1432)
- static **pca953x_i2c_regmap** : const struct regmap_config (line 485)
- static **pca953x_id** : const struct i2c_device_id[] (line 88)
- static **pca953x_irq_chip** : const struct irq_chip (line 931)
- static **pca953x_irq_gpios** : const struct acpi_gpio_params (line 141)
- static **pca953x_regs** : const struct pca953x_reg_config (line 202)
- static **pca957x_regs** : const struct pca953x_reg_config (line 209)
- static **tca6418_regs** : const struct pca953x_reg_config (line 216)

## Macros (63)

- **BANK_SZ** (line 190)
- **MAX_BANK** (line 189)
- **MAX_LINE** (line 191)
- **NBANK**(chip) (line 193)
- **OF_653X**(__nrgpio,__int) (line 1428)
- **OF_953X**(__nrgpio,__int) (line 1429)
- **OF_957X**(__nrgpio,__int) (line 1430)
- **PCA953X_DIRECTION** (line 39)
- **PCA953X_INPUT** (line 36)
- **PCA953X_INVERT** (line 38)
- **PCA953X_OUTPUT** (line 37)
- **PCA953X_TYPE** (line 80)
- **PCA953x_BANK_CONFIG** (line 275)
- **PCA953x_BANK_INPUT** (line 272)
- **PCA953x_BANK_OUTPUT** (line 273)
- **PCA953x_BANK_POLARITY** (line 274)
- **PCA957X_BKEN** (line 51)
- **PCA957X_CFG** (line 53)
- **PCA957X_IN** (line 49)
- **PCA957X_INTS** (line 56)
- **PCA957X_INVRT** (line 50)
- **PCA957X_MSK** (line 55)
- **PCA957X_OUT** (line 54)
- **PCA957X_PUPD** (line 52)
- **PCA957X_TYPE** (line 81)
- **PCA957x_BANK_BUSHOLD** (line 279)
- **PCA957x_BANK_CONFIG** (line 280)
- **PCA957x_BANK_INPUT** (line 277)
- **PCA957x_BANK_OUTPUT** (line 281)
- **PCA957x_BANK_POLARITY** (line 278)
- **PCAL6524_DEBOUNCE** (line 70)
- **PCAL6524_INT_CLR** (line 67)
- **PCAL6524_INT_EDGE** (line 66)
- **PCAL6524_IN_STATUS** (line 68)
- **PCAL6524_OUT_INDCONF** (line 69)
- **PCAL653X_TYPE** (line 82)
- **PCAL953X_INT_MASK** (line 62)
- **PCAL953X_INT_STAT** (line 63)
- **PCAL953X_IN_LATCH** (line 59)
- **PCAL953X_OUT_CONF** (line 64)
- **PCAL953X_OUT_STRENGTH** (line 58)
- **PCAL953X_PULL_EN** (line 60)
- **PCAL953X_PULL_SEL** (line 61)
- **PCAL9xxx_BANK_IN_LATCH** (line 283)
- **PCAL9xxx_BANK_IRQ_MASK** (line 286)
- **PCAL9xxx_BANK_IRQ_STAT** (line 287)
- **PCAL9xxx_BANK_PULL_EN** (line 284)
- **PCAL9xxx_BANK_PULL_SEL** (line 285)
- **PCAL_GPIO_MASK** (line 74)
- **PCAL_PINCTRL_MASK** (line 75)
- **PCA_CHIP_TYPE**(x) (line 86)
- **PCA_GPIO_MASK** (line 72)
- **PCA_INT** (line 77)
- **PCA_LATCH_INT** (line 79)
- **PCA_PCAL** (line 78)
- **PCA_TYPE_MASK** (line 84)
- **REG_ADDR_AI** (line 47)
- **REG_ADDR_EXT** (line 46)
- **REG_ADDR_MASK** (line 45)
- **TCA6418_DIRECTION** (line 43)
- **TCA6418_INPUT** (line 41)
- **TCA6418_OUTPUT** (line 42)
- **TCA6418_TYPE** (line 83)
