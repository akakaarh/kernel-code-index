# drivers/gpio/gpio-lpc32xx.c

Subsystem: drivers/gpio

## Functions (30)

### __get_gpi_state_p3
- Return type: static int
- Signature: __get_gpi_state_p3(struct lpc32xx_gpio_chip * group,unsigned pin)
- Line: 250
- Calls: gpreg_read
- Called by: lpc32xx_gpi_get_value

### __get_gpio_state_p012
- Return type: static int
- Signature: __get_gpio_state_p012(struct lpc32xx_gpio_chip * group,unsigned pin)
- Line: 231
- Calls: gpreg_read
- Called by: lpc32xx_gpio_get_value_p012

### __get_gpio_state_p3
- Return type: static int
- Signature: __get_gpio_state_p3(struct lpc32xx_gpio_chip * group,unsigned pin)
- Line: 238
- Calls: gpreg_read
- Called by: lpc32xx_gpio_get_value_p3

### __get_gpo_state_p3
- Return type: static int
- Signature: __get_gpo_state_p3(struct lpc32xx_gpio_chip * group,unsigned pin)
- Line: 256
- Calls: gpreg_read
- Called by: lpc32xx_gpo_get_value

### __set_gpio_dir_p012
- Return type: static void
- Signature: __set_gpio_dir_p012(struct lpc32xx_gpio_chip * group,unsigned pin,int input)
- Line: 178
- Calls: gpreg_write
- Called by: lpc32xx_gpio_dir_input_p012, lpc32xx_gpio_dir_output_p012

### __set_gpio_dir_p3
- Return type: static void
- Signature: __set_gpio_dir_p3(struct lpc32xx_gpio_chip * group,unsigned pin,int input)
- Line: 189
- Calls: gpreg_write
- Called by: lpc32xx_gpio_dir_input_p3, lpc32xx_gpio_dir_output_p3

### __set_gpio_level_p012
- Return type: static void
- Signature: __set_gpio_level_p012(struct lpc32xx_gpio_chip * group,unsigned pin,int high)
- Line: 200
- Calls: gpreg_write
- Called by: lpc32xx_gpio_dir_output_p012, lpc32xx_gpio_set_value_p012

### __set_gpio_level_p3
- Return type: static void
- Signature: __set_gpio_level_p3(struct lpc32xx_gpio_chip * group,unsigned pin,int high)
- Line: 211
- Calls: gpreg_write
- Called by: lpc32xx_gpio_dir_output_p3, lpc32xx_gpio_set_value_p3

### __set_gpo_level_p3
- Return type: static void
- Signature: __set_gpo_level_p3(struct lpc32xx_gpio_chip * group,unsigned pin,int high)
- Line: 222
- Calls: gpreg_write
- Called by: lpc32xx_gpio_dir_out_always, lpc32xx_gpo_set_value

### gpreg_read
- Return type: static u32
- Signature: gpreg_read(struct lpc32xx_gpio_chip * group,unsigned long offset)
- Line: 168
- Called by: __get_gpi_state_p3, __get_gpio_state_p012, __get_gpio_state_p3, __get_gpo_state_p3

### gpreg_write
- Return type: static void
- Signature: gpreg_write(struct lpc32xx_gpio_chip * group,u32 val,unsigned long offset)
- Line: 173
- Called by: __set_gpio_dir_p012, __set_gpio_dir_p3, __set_gpio_level_p012, __set_gpio_level_p3, __set_gpo_level_p3

### lpc32xx_gpi_get_value
- Return type: static int
- Signature: lpc32xx_gpi_get_value(struct gpio_chip * chip,unsigned pin)
- Line: 305
- Calls: __get_gpi_state_p3, gpiochip_get_data

### lpc32xx_gpio_dir_in_always
- Return type: static int
- Signature: lpc32xx_gpio_dir_in_always(struct gpio_chip * chip,unsigned pin)
- Line: 285

### lpc32xx_gpio_dir_input_p012
- Return type: static int
- Signature: lpc32xx_gpio_dir_input_p012(struct gpio_chip * chip,unsigned pin)
- Line: 265
- Calls: __set_gpio_dir_p012, gpiochip_get_data

### lpc32xx_gpio_dir_input_p3
- Return type: static int
- Signature: lpc32xx_gpio_dir_input_p3(struct gpio_chip * chip,unsigned pin)
- Line: 275
- Calls: __set_gpio_dir_p3, gpiochip_get_data

### lpc32xx_gpio_dir_out_always
- Return type: static int
- Signature: lpc32xx_gpio_dir_out_always(struct gpio_chip * chip,unsigned pin,int value)
- Line: 334
- Calls: __set_gpo_level_p3, gpiochip_get_data

### lpc32xx_gpio_dir_output_p012
- Return type: static int
- Signature: lpc32xx_gpio_dir_output_p012(struct gpio_chip * chip,unsigned pin,int value)
- Line: 312
- Calls: __set_gpio_dir_p012, __set_gpio_level_p012, gpiochip_get_data

### lpc32xx_gpio_dir_output_p3
- Return type: static int
- Signature: lpc32xx_gpio_dir_output_p3(struct gpio_chip * chip,unsigned pin,int value)
- Line: 323
- Calls: __set_gpio_dir_p3, __set_gpio_level_p3, gpiochip_get_data

### lpc32xx_gpio_get_value_p012
- Return type: static int
- Signature: lpc32xx_gpio_get_value_p012(struct gpio_chip * chip,unsigned pin)
- Line: 291
- Calls: __get_gpio_state_p012, gpiochip_get_data

### lpc32xx_gpio_get_value_p3
- Return type: static int
- Signature: lpc32xx_gpio_get_value_p3(struct gpio_chip * chip,unsigned pin)
- Line: 298
- Calls: __get_gpio_state_p3, gpiochip_get_data

### lpc32xx_gpio_probe
- Return type: static int
- Signature: lpc32xx_gpio_probe(struct platform_device * pdev)
- Line: 511

### lpc32xx_gpio_request
- Return type: static int
- Signature: lpc32xx_gpio_request(struct gpio_chip * chip,unsigned pin)
- Line: 380

### lpc32xx_gpio_set_value_p012
- Return type: static int
- Signature: lpc32xx_gpio_set_value_p012(struct gpio_chip * chip,unsigned int pin,int value)
- Line: 343
- Calls: __set_gpio_level_p012, gpiochip_get_data

### lpc32xx_gpio_set_value_p3
- Return type: static int
- Signature: lpc32xx_gpio_set_value_p3(struct gpio_chip * chip,unsigned int pin,int value)
- Line: 353
- Calls: __set_gpio_level_p3, gpiochip_get_data

### lpc32xx_gpio_to_irq_gpi_p3
- Return type: static int
- Signature: lpc32xx_gpio_to_irq_gpi_p3(struct gpio_chip * chip,unsigned offset)
- Line: 398

### lpc32xx_gpio_to_irq_gpio_p3
- Return type: static int
- Signature: lpc32xx_gpio_to_irq_gpio_p3(struct gpio_chip * chip,unsigned offset)
- Line: 393

### lpc32xx_gpio_to_irq_p01
- Return type: static int
- Signature: lpc32xx_gpio_to_irq_p01(struct gpio_chip * chip,unsigned offset)
- Line: 388

### lpc32xx_gpo_get_value
- Return type: static int
- Signature: lpc32xx_gpo_get_value(struct gpio_chip * chip,unsigned pin)
- Line: 373
- Calls: __get_gpo_state_p3, gpiochip_get_data

### lpc32xx_gpo_set_value
- Return type: static int
- Signature: lpc32xx_gpo_set_value(struct gpio_chip * chip,unsigned int pin,int value)
- Line: 363
- Calls: __set_gpo_level_p3, gpiochip_get_data

### lpc32xx_of_xlate
- Return type: static int
- Signature: lpc32xx_of_xlate(struct gpio_chip * gc,const struct of_phandle_args * gpiospec,u32 * flags)
- Line: 497

## Structs (2)

### gpio_regs
- Line: 71
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

### lpc32xx_gpio_chip
- Line: 162
- Members:
  - inp_state: unsigned long
  - outp_state: unsigned long
  - outp_set: unsigned long
  - outp_clr: unsigned long
  - dir_set: unsigned long
  - dir_clr: unsigned long
  - chip: gpio_chip
  - gpio_grp: gpio_regs *
  - reg_base: void __iomem *

## Variables (13)

- static **gpi_p3_names** : const char * [] (line 109)
- static **gpio_grp_regs_p0** : gpio_regs (line 129)
- static **gpio_grp_regs_p1** : gpio_regs (line 137)
- static **gpio_grp_regs_p2** : gpio_regs (line 145)
- static **gpio_grp_regs_p3** : gpio_regs (line 153)
- static **gpio_p0_names** : const char * [] (line 83)
- static **gpio_p1_names** : const char * [] (line 88)
- static **gpio_p2_names** : const char * [] (line 97)
- static **gpio_p3_names** : const char * [] (line 104)
- static **gpo_p3_names** : const char * [] (line 120)
- static **lpc32xx_gpio_driver** : platform_driver (line 540)
- static **lpc32xx_gpio_of_match** : const struct of_device_id[] (line 534)
- static **lpc32xx_gpiochip** : lpc32xx_gpio_chip[] (line 403)

## Macros (48)

- **GPI3_PIN_IN_SEL**(x,y) (line 54)
- **GPIO012_PIN_IN_SEL**(x,y) (line 50)
- **GPIO012_PIN_TO_BIT**(x) (line 47)
- **GPIO3_PIN5_IN_SEL**(x) (line 53)
- **GPIO3_PIN_IN_SEL**(x,y) (line 52)
- **GPIO3_PIN_IN_SHIFT**(x) (line 51)
- **GPIO3_PIN_TO_BIT**(x) (line 48)
- **GPO3_PIN_IN_SEL**(x,y) (line 55)
- **GPO3_PIN_TO_BIT**(x) (line 49)
- **LPC32XX_GPIO_P0_DIR_CLR** (line 37)
- **LPC32XX_GPIO_P0_DIR_SET** (line 36)
- **LPC32XX_GPIO_P0_DIR_STATE** (line 38)
- **LPC32XX_GPIO_P0_GRP** (line 64)
- **LPC32XX_GPIO_P0_INP_STATE** (line 32)
- **LPC32XX_GPIO_P0_MAX** (line 57)
- **LPC32XX_GPIO_P0_OUTP_CLR** (line 34)
- **LPC32XX_GPIO_P0_OUTP_SET** (line 33)
- **LPC32XX_GPIO_P0_OUTP_STATE** (line 35)
- **LPC32XX_GPIO_P1_DIR_CLR** (line 44)
- **LPC32XX_GPIO_P1_DIR_SET** (line 43)
- **LPC32XX_GPIO_P1_DIR_STATE** (line 45)
- **LPC32XX_GPIO_P1_GRP** (line 65)
- **LPC32XX_GPIO_P1_INP_STATE** (line 39)
- **LPC32XX_GPIO_P1_MAX** (line 58)
- **LPC32XX_GPIO_P1_OUTP_CLR** (line 41)
- **LPC32XX_GPIO_P1_OUTP_SET** (line 40)
- **LPC32XX_GPIO_P1_OUTP_STATE** (line 42)
- **LPC32XX_GPIO_P2_DIR_CLR** (line 24)
- **LPC32XX_GPIO_P2_DIR_SET** (line 23)
- **LPC32XX_GPIO_P2_DIR_STATE** (line 25)
- **LPC32XX_GPIO_P2_GRP** (line 66)
- **LPC32XX_GPIO_P2_INP_STATE** (line 26)
- **LPC32XX_GPIO_P2_MAX** (line 59)
- **LPC32XX_GPIO_P2_MUX_CLR** (line 30)
- **LPC32XX_GPIO_P2_MUX_SET** (line 29)
- **LPC32XX_GPIO_P2_MUX_STATE** (line 31)
- **LPC32XX_GPIO_P2_OUTP_CLR** (line 28)
- **LPC32XX_GPIO_P2_OUTP_SET** (line 27)
- **LPC32XX_GPIO_P3_GRP** (line 67)
- **LPC32XX_GPIO_P3_INP_STATE** (line 19)
- **LPC32XX_GPIO_P3_MAX** (line 60)
- **LPC32XX_GPIO_P3_OUTP_CLR** (line 21)
- **LPC32XX_GPIO_P3_OUTP_SET** (line 20)
- **LPC32XX_GPIO_P3_OUTP_STATE** (line 22)
- **LPC32XX_GPI_P3_GRP** (line 68)
- **LPC32XX_GPI_P3_MAX** (line 61)
- **LPC32XX_GPO_P3_GRP** (line 69)
- **LPC32XX_GPO_P3_MAX** (line 62)
