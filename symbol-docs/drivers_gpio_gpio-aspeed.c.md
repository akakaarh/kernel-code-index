# drivers/gpio/gpio-aspeed.c

Subsystem: drivers/gpio

## Functions (53)

### __aspeed_gpio_set
- Return type: static void
- Signature: __aspeed_gpio_set(struct gpio_chip * gc,unsigned int offset,int val)
- Line: 413
- Calls: gpiochip_get_data
- Called by: aspeed_gpio_dir_out, aspeed_gpio_set

### aspeed_g4_copro_release
- Return type: static void
- Signature: aspeed_g4_copro_release(struct aspeed_gpio * gpio,unsigned int offset)
- Line: 1126
- Calls: aspeed_g4_privilege_ctrl

### aspeed_g4_copro_request
- Return type: static bool
- Signature: aspeed_g4_copro_request(struct aspeed_gpio * gpio,unsigned int offset)
- Line: 1105
- Calls: aspeed_g4_privilege_ctrl, aspeed_g4_reg_bank_get

### aspeed_g4_privilege_ctrl
- Return type: static void
- Signature: aspeed_g4_privilege_ctrl(struct aspeed_gpio * gpio,unsigned int offset,int cmdsrc)
- Line: 1080
- Calls: aspeed_g4_reg_bit_set
- Called by: aspeed_g4_copro_release, aspeed_g4_copro_request, aspeed_g4_privilege_init

### aspeed_g4_privilege_init
- Return type: static void
- Signature: aspeed_g4_privilege_init(struct aspeed_gpio * gpio)
- Line: 1092
- Calls: aspeed_g4_privilege_ctrl

### aspeed_g4_reg_bank_get
- Return type: static int
- Signature: aspeed_g4_reg_bank_get(struct aspeed_gpio * gpio,unsigned int offset,const enum aspeed_gpio_reg reg)
- Line: 1068
- Calls: aspeed_gpio_g4_bank_reg, to_bank
- Called by: aspeed_g4_copro_request

### aspeed_g4_reg_bit_get
- Return type: static bool
- Signature: aspeed_g4_reg_bit_get(struct aspeed_gpio * gpio,unsigned int offset,const enum aspeed_gpio_reg reg)
- Line: 1059
- Calls: aspeed_gpio_g4_bank_reg, to_bank

### aspeed_g4_reg_bit_set
- Return type: static void
- Signature: aspeed_g4_reg_bit_set(struct aspeed_gpio * gpio,unsigned int offset,const enum aspeed_gpio_reg reg,bool val)
- Line: 1037
- Calls: aspeed_gpio_g4_bank_reg, to_bank
- Called by: aspeed_g4_privilege_ctrl

### aspeed_g7_reg_bank_get
- Return type: static int
- Signature: aspeed_g7_reg_bank_get(struct aspeed_gpio * gpio,unsigned int offset,const enum aspeed_gpio_reg reg)
- Line: 1181

### aspeed_g7_reg_bit_get
- Return type: static bool
- Signature: aspeed_g7_reg_bit_get(struct aspeed_gpio * gpio,unsigned int offset,const enum aspeed_gpio_reg reg)
- Line: 1165
- Calls: aspeed_gpio_g7_reg_mask

### aspeed_g7_reg_bit_set
- Return type: static void
- Signature: aspeed_g7_reg_bit_set(struct aspeed_gpio * gpio,unsigned int offset,const enum aspeed_gpio_reg reg,bool val)
- Line: 1152
- Calls: aspeed_gpio_g7_reg_mask

### aspeed_gpio_change_cmd_source
- Return type: static void
- Signature: aspeed_gpio_change_cmd_source(struct aspeed_gpio * gpio,unsigned int offset,int cmdsrc)
- Line: 378
- Called by: aspeed_gpio_copro_grab_gpio, aspeed_gpio_copro_release_gpio

### aspeed_gpio_copro_grab_gpio
- Return type: int
- Signature: aspeed_gpio_copro_grab_gpio(struct gpio_desc * desc,u16 * vreg_offset,u16 * dreg_offset,u8 * bit)
- Line: 936
- Calls: aspeed_gpio_change_cmd_source, aspeed_gpio_support_copro, gpiochip_get_data, gpiod_hwgpio, gpiod_to_chip, to_bank

### aspeed_gpio_copro_release
- Return type: static void
- Signature: aspeed_gpio_copro_release(struct aspeed_gpio * gpio,unsigned int offset)
- Line: 393
- Called by: aspeed_gpio_dir_in, aspeed_gpio_dir_out, aspeed_gpio_irq_ack, aspeed_gpio_irq_set_mask, aspeed_gpio_reset_tolerance, aspeed_gpio_set, aspeed_gpio_set_type

### aspeed_gpio_copro_release_gpio
- Return type: int
- Signature: aspeed_gpio_copro_release_gpio(struct gpio_desc * desc)
- Line: 982
- Calls: aspeed_gpio_change_cmd_source, aspeed_gpio_support_copro, gpiochip_get_data, gpiod_hwgpio, gpiod_to_chip

### aspeed_gpio_copro_request
- Return type: static bool
- Signature: aspeed_gpio_copro_request(struct aspeed_gpio * gpio,unsigned int offset)
- Line: 384
- Called by: aspeed_gpio_dir_in, aspeed_gpio_dir_out, aspeed_gpio_irq_ack, aspeed_gpio_irq_set_mask, aspeed_gpio_reset_tolerance, aspeed_gpio_set, aspeed_gpio_set_type

### aspeed_gpio_copro_set_ops
- Return type: int
- Signature: aspeed_gpio_copro_set_ops(const struct aspeed_gpio_copro_ops * ops,void * data)
- Line: 918

### aspeed_gpio_dir_in
- Return type: static int
- Signature: aspeed_gpio_dir_in(struct gpio_chip * gc,unsigned int offset)
- Line: 440
- Calls: aspeed_gpio_copro_release, aspeed_gpio_copro_request, gpiochip_get_data, have_input

### aspeed_gpio_dir_out
- Return type: static int
- Signature: aspeed_gpio_dir_out(struct gpio_chip * gc,unsigned int offset,int val)
- Line: 458
- Calls: __aspeed_gpio_set, aspeed_gpio_copro_release, aspeed_gpio_copro_request, gpiochip_get_data, have_output

### aspeed_gpio_free
- Return type: static void
- Signature: aspeed_gpio_free(struct gpio_chip * chip,unsigned int offset)
- Line: 700

### aspeed_gpio_g4_bank_reg
- Return type: static void __iomem *
- Signature: aspeed_gpio_g4_bank_reg(struct aspeed_gpio * gpio,const struct aspeed_gpio_bank * bank,const enum aspeed_gpio_reg reg)
- Line: 252
- Called by: aspeed_g4_reg_bank_get, aspeed_g4_reg_bit_get, aspeed_g4_reg_bit_set

### aspeed_gpio_g7_reg_mask
- Return type: static u32
- Signature: aspeed_gpio_g7_reg_mask(const enum aspeed_gpio_reg reg)
- Line: 287
- Called by: aspeed_g7_reg_bit_get, aspeed_g7_reg_bit_set

### aspeed_gpio_get
- Return type: static int
- Signature: aspeed_gpio_get(struct gpio_chip * gc,unsigned int offset)
- Line: 406
- Calls: gpiochip_get_data

### aspeed_gpio_get_direction
- Return type: static int
- Signature: aspeed_gpio_get_direction(struct gpio_chip * gc,unsigned int offset)
- Line: 479
- Calls: gpiochip_get_data, have_input, have_output

### aspeed_gpio_irq_ack
- Return type: static void
- Signature: aspeed_gpio_irq_ack(struct irq_data * d)
- Line: 516
- Calls: aspeed_gpio_copro_release, aspeed_gpio_copro_request, irqd_to_aspeed_gpio_data

### aspeed_gpio_irq_handler
- Return type: static void
- Signature: aspeed_gpio_irq_handler(struct irq_desc * desc)
- Line: 628
- Calls: gpiochip_get_data

### aspeed_gpio_irq_mask
- Return type: static void
- Signature: aspeed_gpio_irq_mask(struct irq_data * d)
- Line: 564
- Calls: aspeed_gpio_irq_set_mask

### aspeed_gpio_irq_print_chip
- Return type: static void
- Signature: aspeed_gpio_irq_print_chip(struct irq_data * d,struct seq_file * p)
- Line: 1015
- Calls: irqd_to_aspeed_gpio_data

### aspeed_gpio_irq_set_mask
- Return type: static void
- Signature: aspeed_gpio_irq_set_mask(struct irq_data * d,bool set)
- Line: 536
- Calls: aspeed_gpio_copro_release, aspeed_gpio_copro_request, gpiochip_disable_irq, gpiochip_enable_irq, irqd_to_aspeed_gpio_data
- Called by: aspeed_gpio_irq_mask, aspeed_gpio_irq_unmask

### aspeed_gpio_irq_unmask
- Return type: static void
- Signature: aspeed_gpio_irq_unmask(struct irq_data * d)
- Line: 569
- Calls: aspeed_gpio_irq_set_mask

### aspeed_gpio_probe
- Return type: static int
- Signature: aspeed_gpio_probe(struct platform_device * pdev)
- Line: 1303

### aspeed_gpio_request
- Return type: static int
- Signature: aspeed_gpio_request(struct gpio_chip * chip,unsigned int offset)
- Line: 692
- Calls: gpiochip_get_data, have_gpio

### aspeed_gpio_reset_tolerance
- Return type: static int
- Signature: aspeed_gpio_reset_tolerance(struct gpio_chip * chip,unsigned int offset,bool enable)
- Line: 674
- Calls: aspeed_gpio_copro_release, aspeed_gpio_copro_request, gpiochip_get_data
- Called by: aspeed_gpio_set_config

### aspeed_gpio_set
- Return type: static int
- Signature: aspeed_gpio_set(struct gpio_chip * gc,unsigned int offset,int val)
- Line: 423
- Calls: __aspeed_gpio_set, aspeed_gpio_copro_release, aspeed_gpio_copro_request, gpiochip_get_data

### aspeed_gpio_set_config
- Return type: static int
- Signature: aspeed_gpio_set_config(struct gpio_chip * chip,unsigned int offset,unsigned long config)
- Line: 890
- Calls: aspeed_gpio_reset_tolerance, set_debounce

### aspeed_gpio_set_type
- Return type: static int
- Signature: aspeed_gpio_set_type(struct irq_data * d,unsigned int type)
- Line: 574
- Calls: aspeed_gpio_copro_release, aspeed_gpio_copro_request, irqd_to_aspeed_gpio_data

### aspeed_gpio_support_copro
- Return type: static bool
- Signature: aspeed_gpio_support_copro(struct aspeed_gpio * gpio)
- Line: 400
- Called by: aspeed_gpio_copro_grab_gpio, aspeed_gpio_copro_release_gpio

### aspeed_init_irq_valid_mask
- Return type: static void
- Signature: aspeed_init_irq_valid_mask(struct gpio_chip * gc,unsigned long * valid_mask,unsigned int ngpios)
- Line: 649
- Calls: gpiochip_get_data, is_bank_props_sentinel

### configure_timer
- Return type: static void
- Signature: configure_timer(struct aspeed_gpio * gpio,unsigned int offset,unsigned int timer)
- Line: 774
- Called by: disable_debounce, enable_debounce

### disable_debounce
- Return type: static int
- Signature: disable_debounce(struct gpio_chip * chip,unsigned int offset)
- Line: 862
- Calls: configure_timer, gpiochip_get_data, unregister_allocated_timer
- Called by: set_debounce

### enable_debounce
- Return type: static int
- Signature: enable_debounce(struct gpio_chip * chip,unsigned int offset,unsigned long usecs)
- Line: 784
- Calls: configure_timer, gpiochip_get_data, register_allocated_timer, timer_allocation_registered, unregister_allocated_timer, usecs_to_cycles
- Called by: set_debounce

### find_bank_props
- Return type: static const struct aspeed_bank_props *
- Signature: find_bank_props(struct aspeed_gpio * gpio,unsigned int offset)
- Line: 337
- Calls: is_bank_props_sentinel
- Called by: have_gpio, have_input, have_output

### have_gpio
- Return type: static bool
- Signature: have_gpio(struct aspeed_gpio * gpio,unsigned int offset)
- Line: 351
- Calls: find_bank_props
- Called by: aspeed_gpio_request

### have_input
- Return type: static bool
- Signature: have_input(struct aspeed_gpio * gpio,unsigned int offset)
- Line: 361
- Calls: find_bank_props
- Called by: aspeed_gpio_dir_in, aspeed_gpio_get_direction

### have_output
- Return type: static bool
- Signature: have_output(struct aspeed_gpio * gpio,unsigned int offset)
- Line: 371
- Calls: find_bank_props
- Called by: aspeed_gpio_dir_out, aspeed_gpio_get_direction

### irqd_to_aspeed_gpio_data
- Return type: static int
- Signature: irqd_to_aspeed_gpio_data(struct irq_data * d,struct aspeed_gpio ** gpio,int * offset)
- Line: 497
- Called by: aspeed_gpio_irq_ack, aspeed_gpio_irq_print_chip, aspeed_gpio_irq_set_mask, aspeed_gpio_set_type

### is_bank_props_sentinel
- Return type: static bool
- Signature: is_bank_props_sentinel(const struct aspeed_bank_props * props)
- Line: 332
- Called by: aspeed_init_irq_valid_mask, find_bank_props

### register_allocated_timer
- Return type: static int
- Signature: register_allocated_timer(struct aspeed_gpio * gpio,unsigned int offset,unsigned int timer)
- Line: 729
- Called by: enable_debounce

### set_debounce
- Return type: static int
- Signature: set_debounce(struct gpio_chip * chip,unsigned int offset,unsigned long usecs)
- Line: 876
- Calls: disable_debounce, enable_debounce, gpiochip_get_data
- Called by: aspeed_gpio_set_config

### timer_allocation_registered
- Return type: static bool
- Signature: timer_allocation_registered(struct aspeed_gpio * gpio,unsigned int offset)
- Line: 767
- Called by: enable_debounce

### to_bank
- Return type: static const struct aspeed_gpio_bank *
- Signature: to_bank(unsigned int offset)
- Line: 324
- Called by: aspeed_g4_reg_bank_get, aspeed_g4_reg_bit_get, aspeed_g4_reg_bit_set, aspeed_gpio_copro_grab_gpio, aspeed_sgpio_g4_reg_bank_get, aspeed_sgpio_g4_reg_bit_get, aspeed_sgpio_g4_reg_bit_set

### unregister_allocated_timer
- Return type: static int
- Signature: unregister_allocated_timer(struct aspeed_gpio * gpio,unsigned int offset)
- Line: 748
- Called by: disable_debounce, enable_debounce

### usecs_to_cycles
- Return type: static int
- Signature: usecs_to_cycles(struct aspeed_gpio * gpio,unsigned long usecs,u32 * cycles)
- Line: 705
- Called by: enable_debounce

## Structs (5)

### aspeed_bank_props
- Line: 51
- Members:
  - bank: unsigned int
  - input: u32
  - output: u32
  - nr_gpios: unsigned int
  - props: const struct aspeed_bank_props *
  - llops: const struct aspeed_gpio_llops *
  - debounce_timers_array: const int *
  - debounce_timers_num: int
  - require_dcache: bool
  - chip: gpio_chip
  - dev: device *
  - lock: raw_spinlock_t
  - base: void __iomem *
  - irq: int
  - config: const struct aspeed_gpio_config *
  - offset_timer: u8 *
  - timer_users: unsigned int[4]
  - clk: clk *
  - dcache: u32 *
  - cf_copro_bankmap: u8 *
  - val_regs: uint16_t
  - rdata_reg: uint16_t
  - irq_regs: uint16_t
  - debounce_regs: uint16_t
  - tolerance_regs: uint16_t
  - cmdsrc_regs: uint16_t
  - reg_bit_set: void (*)(struct aspeed_gpio * gpio,unsigned int offset,const enum aspeed_gpio_reg reg,bool val)
  - reg_bit_get: bool (*)(struct aspeed_gpio * gpio,unsigned int offset,const enum aspeed_gpio_reg reg)
  - reg_bank_get: int (*)(struct aspeed_gpio * gpio,unsigned int offset,const enum aspeed_gpio_reg reg)
  - privilege_ctrl: void (*)(struct aspeed_gpio * gpio,unsigned int offset,int owner)
  - privilege_init: void (*)(struct aspeed_gpio * gpio)
  - copro_request: bool (*)(struct aspeed_gpio * gpio,unsigned int offset)
  - copro_release: void (*)(struct aspeed_gpio * gpio,unsigned int offset)

### aspeed_gpio
- Line: 77
- Members:
  - bank: unsigned int
  - input: u32
  - output: u32
  - nr_gpios: unsigned int
  - props: const struct aspeed_bank_props *
  - llops: const struct aspeed_gpio_llops *
  - debounce_timers_array: const int *
  - debounce_timers_num: int
  - require_dcache: bool
  - chip: gpio_chip
  - dev: device *
  - lock: raw_spinlock_t
  - base: void __iomem *
  - irq: int
  - config: const struct aspeed_gpio_config *
  - offset_timer: u8 *
  - timer_users: unsigned int[4]
  - clk: clk *
  - dcache: u32 *
  - cf_copro_bankmap: u8 *
  - val_regs: uint16_t
  - rdata_reg: uint16_t
  - irq_regs: uint16_t
  - debounce_regs: uint16_t
  - tolerance_regs: uint16_t
  - cmdsrc_regs: uint16_t
  - reg_bit_set: void (*)(struct aspeed_gpio * gpio,unsigned int offset,const enum aspeed_gpio_reg reg,bool val)
  - reg_bit_get: bool (*)(struct aspeed_gpio * gpio,unsigned int offset,const enum aspeed_gpio_reg reg)
  - reg_bank_get: int (*)(struct aspeed_gpio * gpio,unsigned int offset,const enum aspeed_gpio_reg reg)
  - privilege_ctrl: void (*)(struct aspeed_gpio * gpio,unsigned int offset,int owner)
  - privilege_init: void (*)(struct aspeed_gpio * gpio)
  - copro_request: bool (*)(struct aspeed_gpio * gpio,unsigned int offset)
  - copro_release: void (*)(struct aspeed_gpio * gpio,unsigned int offset)

### aspeed_gpio_bank
- Line: 93
- Members:
  - bank: unsigned int
  - input: u32
  - output: u32
  - nr_gpios: unsigned int
  - props: const struct aspeed_bank_props *
  - llops: const struct aspeed_gpio_llops *
  - debounce_timers_array: const int *
  - debounce_timers_num: int
  - require_dcache: bool
  - chip: gpio_chip
  - dev: device *
  - lock: raw_spinlock_t
  - base: void __iomem *
  - irq: int
  - config: const struct aspeed_gpio_config *
  - offset_timer: u8 *
  - timer_users: unsigned int[4]
  - clk: clk *
  - dcache: u32 *
  - cf_copro_bankmap: u8 *
  - val_regs: uint16_t
  - rdata_reg: uint16_t
  - irq_regs: uint16_t
  - debounce_regs: uint16_t
  - tolerance_regs: uint16_t
  - cmdsrc_regs: uint16_t
  - reg_bit_set: void (*)(struct aspeed_gpio * gpio,unsigned int offset,const enum aspeed_gpio_reg reg,bool val)
  - reg_bit_get: bool (*)(struct aspeed_gpio * gpio,unsigned int offset,const enum aspeed_gpio_reg reg)
  - reg_bank_get: int (*)(struct aspeed_gpio * gpio,unsigned int offset,const enum aspeed_gpio_reg reg)
  - privilege_ctrl: void (*)(struct aspeed_gpio * gpio,unsigned int offset,int owner)
  - privilege_init: void (*)(struct aspeed_gpio * gpio)
  - copro_request: bool (*)(struct aspeed_gpio * gpio,unsigned int offset)
  - copro_release: void (*)(struct aspeed_gpio * gpio,unsigned int offset)

### aspeed_gpio_config
- Line: 57
- Members:
  - bank: unsigned int
  - input: u32
  - output: u32
  - nr_gpios: unsigned int
  - props: const struct aspeed_bank_props *
  - llops: const struct aspeed_gpio_llops *
  - debounce_timers_array: const int *
  - debounce_timers_num: int
  - require_dcache: bool
  - chip: gpio_chip
  - dev: device *
  - lock: raw_spinlock_t
  - base: void __iomem *
  - irq: int
  - config: const struct aspeed_gpio_config *
  - offset_timer: u8 *
  - timer_users: unsigned int[4]
  - clk: clk *
  - dcache: u32 *
  - cf_copro_bankmap: u8 *
  - val_regs: uint16_t
  - rdata_reg: uint16_t
  - irq_regs: uint16_t
  - debounce_regs: uint16_t
  - tolerance_regs: uint16_t
  - cmdsrc_regs: uint16_t
  - reg_bit_set: void (*)(struct aspeed_gpio * gpio,unsigned int offset,const enum aspeed_gpio_reg reg,bool val)
  - reg_bit_get: bool (*)(struct aspeed_gpio * gpio,unsigned int offset,const enum aspeed_gpio_reg reg)
  - reg_bank_get: int (*)(struct aspeed_gpio * gpio,unsigned int offset,const enum aspeed_gpio_reg reg)
  - privilege_ctrl: void (*)(struct aspeed_gpio * gpio,unsigned int offset,int owner)
  - privilege_init: void (*)(struct aspeed_gpio * gpio)
  - copro_request: bool (*)(struct aspeed_gpio * gpio,unsigned int offset)
  - copro_release: void (*)(struct aspeed_gpio * gpio,unsigned int offset)

### aspeed_gpio_llops
- Line: 219
- Members:
  - bank: unsigned int
  - input: u32
  - output: u32
  - nr_gpios: unsigned int
  - props: const struct aspeed_bank_props *
  - llops: const struct aspeed_gpio_llops *
  - debounce_timers_array: const int *
  - debounce_timers_num: int
  - require_dcache: bool
  - chip: gpio_chip
  - dev: device *
  - lock: raw_spinlock_t
  - base: void __iomem *
  - irq: int
  - config: const struct aspeed_gpio_config *
  - offset_timer: u8 *
  - timer_users: unsigned int[4]
  - clk: clk *
  - dcache: u32 *
  - cf_copro_bankmap: u8 *
  - val_regs: uint16_t
  - rdata_reg: uint16_t
  - irq_regs: uint16_t
  - debounce_regs: uint16_t
  - tolerance_regs: uint16_t
  - cmdsrc_regs: uint16_t
  - reg_bit_set: void (*)(struct aspeed_gpio * gpio,unsigned int offset,const enum aspeed_gpio_reg reg,bool val)
  - reg_bit_get: bool (*)(struct aspeed_gpio * gpio,unsigned int offset,const enum aspeed_gpio_reg reg)
  - reg_bank_get: int (*)(struct aspeed_gpio * gpio,unsigned int offset,const enum aspeed_gpio_reg reg)
  - privilege_ctrl: void (*)(struct aspeed_gpio * gpio,unsigned int offset,int owner)
  - privilege_init: void (*)(struct aspeed_gpio * gpio)
  - copro_request: bool (*)(struct aspeed_gpio * gpio,unsigned int offset)
  - copro_release: void (*)(struct aspeed_gpio * gpio,unsigned int offset)

## Enums (1)

### aspeed_gpio_reg
- Line: 203

## Variables (18)

- static **aspeed_g4_llops** : const struct aspeed_gpio_llops (line 1142)
- static **aspeed_g7_llops** : const struct aspeed_gpio_llops (line 1194)
- static **aspeed_gpio_banks** : const struct aspeed_gpio_bank[] (line 136)
- static **aspeed_gpio_driver** : platform_driver (line 1400)
- static **aspeed_gpio_irq_chip** : const struct irq_chip (line 1027)
- static **aspeed_gpio_of_table** : const struct of_device_id[] (line 1294)
- static **ast2400_bank_props** : const struct aspeed_bank_props[] (line 1211)
- static **ast2400_config** : const struct aspeed_gpio_config (line 1218)
- static **ast2500_bank_props** : const struct aspeed_bank_props[] (line 1229)
- static **ast2500_config** : const struct aspeed_gpio_config (line 1237)
- static **ast2600_bank_props** : const struct aspeed_bank_props[] (line 1248)
- static **ast2600_config** : const struct aspeed_gpio_config (line 1256)
- static **ast2700_bank_props** : const struct aspeed_bank_props[] (line 1271)
- static **ast2700_config** : const struct aspeed_gpio_config (line 1278)
- static **copro_data** : void * (line 134)
- static **copro_ops** : const struct aspeed_gpio_copro_ops * (line 133)
- static **debounce_timers** : const int[4] (line 115)
- static **g7_debounce_timers** : const int[4] (line 116)

## Macros (36)

- **GPIO_BANK**(x) (line 320)
- **GPIO_BIT**(x) (line 322)
- **GPIO_CMDSRC_0** (line 244)
- **GPIO_CMDSRC_1** (line 245)
- **GPIO_CMDSRC_ARM** (line 246)
- **GPIO_CMDSRC_COLDFIRE** (line 248)
- **GPIO_CMDSRC_LPC** (line 247)
- **GPIO_CMDSRC_RESERVED** (line 249)
- **GPIO_DEBOUNCE_SEL1** (line 241)
- **GPIO_DEBOUNCE_SEL2** (line 242)
- **GPIO_G7_CTRL_DEBOUNCE_SEL1** (line 46)
- **GPIO_G7_CTRL_DEBOUNCE_SEL2** (line 45)
- **GPIO_G7_CTRL_DIR** (line 39)
- **GPIO_G7_CTRL_INPUT_MASK** (line 47)
- **GPIO_G7_CTRL_IN_DATA** (line 49)
- **GPIO_G7_CTRL_IRQ_EN** (line 40)
- **GPIO_G7_CTRL_IRQ_STS** (line 48)
- **GPIO_G7_CTRL_IRQ_TYPE0** (line 41)
- **GPIO_G7_CTRL_IRQ_TYPE1** (line 42)
- **GPIO_G7_CTRL_IRQ_TYPE2** (line 43)
- **GPIO_G7_CTRL_OUT_DATA** (line 38)
- **GPIO_G7_CTRL_REG_BASE** (line 36)
- **GPIO_G7_CTRL_REG_OFFSET**(x) (line 37)
- **GPIO_G7_CTRL_RST_TOLERANCE** (line 44)
- **GPIO_G7_IRQ_STS_BASE** (line 34)
- **GPIO_G7_IRQ_STS_OFFSET**(x) (line 35)
- **GPIO_IRQ_ENABLE** (line 235)
- **GPIO_IRQ_STATUS** (line 239)
- **GPIO_IRQ_TYPE0** (line 236)
- **GPIO_IRQ_TYPE1** (line 237)
- **GPIO_IRQ_TYPE2** (line 238)
- **GPIO_OFFSET**(x) (line 321)
- **GPIO_VAL_DIR** (line 233)
- **GPIO_VAL_VALUE** (line 232)
- **have_debounce**(g,o) (line 369)
- **have_irq**(g,o) (line 368)
