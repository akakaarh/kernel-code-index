# drivers/gpio/gpio-aspeed-sgpio.c

Subsystem: drivers/gpio

## Functions (29)

### aspeed_sgpio_dir_in
- Return type: static int
- Signature: aspeed_sgpio_dir_in(struct gpio_chip * gc,unsigned int offset)
- Line: 260
- Calls: aspeed_sgpio_is_input

### aspeed_sgpio_dir_out
- Return type: static int
- Signature: aspeed_sgpio_dir_out(struct gpio_chip * gc,unsigned int offset,int val)
- Line: 265
- Calls: gpiochip_get_data, sgpio_set_value

### aspeed_sgpio_g4_bank_reg
- Return type: static void __iomem *
- Signature: aspeed_sgpio_g4_bank_reg(struct aspeed_sgpio * gpio,const struct aspeed_sgpio_bank * bank,const enum aspeed_sgpio_reg reg)
- Line: 136
- Called by: aspeed_sgpio_g4_reg_bank_get, aspeed_sgpio_g4_reg_bit_get, aspeed_sgpio_g4_reg_bit_set

### aspeed_sgpio_g4_reg_bank_get
- Return type: static int
- Signature: aspeed_sgpio_g4_reg_bank_get(struct aspeed_sgpio * gpio,unsigned int offset,const enum aspeed_sgpio_reg reg)
- Line: 488
- Calls: aspeed_sgpio_g4_bank_reg, to_bank

### aspeed_sgpio_g4_reg_bit_get
- Return type: static bool
- Signature: aspeed_sgpio_g4_reg_bit_get(struct aspeed_sgpio * gpio,unsigned int offset,const enum aspeed_sgpio_reg reg)
- Line: 479
- Calls: aspeed_sgpio_g4_bank_reg, to_bank

### aspeed_sgpio_g4_reg_bit_set
- Return type: static void
- Signature: aspeed_sgpio_g4_reg_bit_set(struct aspeed_sgpio * gpio,unsigned int offset,const enum aspeed_sgpio_reg reg,bool val)
- Line: 447
- Calls: aspeed_sgpio_g4_bank_reg, to_bank

### aspeed_sgpio_g7_reg_bank_get
- Return type: static int
- Signature: aspeed_sgpio_g7_reg_bank_get(struct aspeed_sgpio * gpio,unsigned int offset,const enum aspeed_sgpio_reg reg)
- Line: 571

### aspeed_sgpio_g7_reg_bit_get
- Return type: static bool
- Signature: aspeed_sgpio_g7_reg_bit_get(struct aspeed_sgpio * gpio,unsigned int offset,const enum aspeed_sgpio_reg reg)
- Line: 555
- Calls: aspeed_sgpio_g7_reg_mask

### aspeed_sgpio_g7_reg_bit_set
- Return type: static void
- Signature: aspeed_sgpio_g7_reg_bit_set(struct aspeed_sgpio * gpio,unsigned int offset,const enum aspeed_sgpio_reg reg,bool val)
- Line: 542
- Calls: aspeed_sgpio_g7_reg_mask

### aspeed_sgpio_g7_reg_mask
- Return type: static u32
- Signature: aspeed_sgpio_g7_reg_mask(const enum aspeed_sgpio_reg reg)
- Line: 163
- Called by: aspeed_sgpio_g7_reg_bit_get, aspeed_sgpio_g7_reg_bit_set

### aspeed_sgpio_get
- Return type: static int
- Signature: aspeed_sgpio_get(struct gpio_chip * gc,unsigned int offset)
- Line: 225
- Calls: aspeed_sgpio_is_input, gpiochip_get_data

### aspeed_sgpio_get_direction
- Return type: static int
- Signature: aspeed_sgpio_get_direction(struct gpio_chip * gc,unsigned int offset)
- Line: 280
- Calls: aspeed_sgpio_is_input

### aspeed_sgpio_init_valid_mask
- Return type: static int
- Signature: aspeed_sgpio_init_valid_mask(struct gpio_chip * gc,unsigned long * valid_mask,unsigned int ngpios)
- Line: 201

### aspeed_sgpio_irq_ack
- Return type: static void
- Signature: aspeed_sgpio_irq_ack(struct irq_data * d)
- Line: 286

### aspeed_sgpio_irq_handler
- Return type: static void
- Signature: aspeed_sgpio_irq_handler(struct irq_desc * desc)
- Line: 366
- Calls: gpiochip_get_data

### aspeed_sgpio_irq_init_valid_mask
- Return type: static void
- Signature: aspeed_sgpio_irq_init_valid_mask(struct gpio_chip * gc,unsigned long * valid_mask,unsigned int ngpios)
- Line: 208

### aspeed_sgpio_irq_mask
- Return type: static void
- Signature: aspeed_sgpio_irq_mask(struct irq_data * d)
- Line: 315
- Calls: aspeed_sgpio_irq_set_mask

### aspeed_sgpio_irq_print_chip
- Return type: static void
- Signature: aspeed_sgpio_irq_print_chip(struct irq_data * d,struct seq_file * p)
- Line: 387

### aspeed_sgpio_irq_set_mask
- Return type: static void
- Signature: aspeed_sgpio_irq_set_mask(struct irq_data * d,bool set)
- Line: 296
- Calls: gpiochip_disable_irq, gpiochip_enable_irq
- Called by: aspeed_sgpio_irq_mask, aspeed_sgpio_irq_unmask

### aspeed_sgpio_irq_unmask
- Return type: static void
- Signature: aspeed_sgpio_irq_unmask(struct irq_data * d)
- Line: 320
- Calls: aspeed_sgpio_irq_set_mask

### aspeed_sgpio_is_input
- Return type: static bool
- Signature: aspeed_sgpio_is_input(unsigned int offset)
- Line: 220
- Called by: aspeed_sgpio_dir_in, aspeed_sgpio_get, aspeed_sgpio_get_direction, sgpio_set_value

### aspeed_sgpio_probe
- Return type: static int
- Signature: aspeed_sgpio_probe(struct platform_device * pdev)
- Line: 606
- Calls: aspeed_sgpio_setup_irqs

### aspeed_sgpio_reset_tolerance
- Return type: static int
- Signature: aspeed_sgpio_reset_tolerance(struct gpio_chip * chip,unsigned int offset,bool enable)
- Line: 512
- Calls: gpiochip_get_data
- Called by: aspeed_sgpio_set_config

### aspeed_sgpio_set
- Return type: static int
- Signature: aspeed_sgpio_set(struct gpio_chip * gc,unsigned int offset,int val)
- Line: 251
- Calls: gpiochip_get_data, sgpio_set_value

### aspeed_sgpio_set_config
- Return type: static int
- Signature: aspeed_sgpio_set_config(struct gpio_chip * chip,unsigned int offset,unsigned long config)
- Line: 524
- Calls: aspeed_sgpio_reset_tolerance

### aspeed_sgpio_set_type
- Return type: static int
- Signature: aspeed_sgpio_set_type(struct irq_data * d,unsigned int type)
- Line: 325

### aspeed_sgpio_setup_irqs
- Return type: static int
- Signature: aspeed_sgpio_setup_irqs(struct aspeed_sgpio * gpio,struct platform_device * pdev)
- Line: 404
- Called by: aspeed_sgpio_probe

### sgpio_set_value
- Return type: static int
- Signature: sgpio_set_value(struct gpio_chip * gc,unsigned int offset,int val)
- Line: 239
- Calls: aspeed_sgpio_is_input, gpiochip_get_data
- Called by: aspeed_sgpio_dir_out, aspeed_sgpio_set

### to_bank
- Return type: static const struct aspeed_sgpio_bank *
- Signature: to_bank(unsigned int offset)
- Line: 191
- Called by: aspeed_g4_reg_bank_get, aspeed_g4_reg_bit_get, aspeed_g4_reg_bit_set, aspeed_gpio_copro_grab_gpio, aspeed_sgpio_g4_reg_bank_get, aspeed_sgpio_g4_reg_bit_get, aspeed_sgpio_g4_reg_bit_set

## Structs (4)

### aspeed_sgpio
- Line: 58
- Members:
  - pin_mask: const u32
  - llops: const struct aspeed_sgpio_llops *
  - cfg_offset: const u32
  - chip: gpio_chip
  - dev: device *
  - pclk: clk *
  - lock: raw_spinlock_t
  - base: void __iomem *
  - irq: int
  - pdata: const struct aspeed_sgpio_pdata *
  - val_regs: u16
  - rdata_reg: u16
  - irq_regs: u16
  - tolerance_regs: u16
  - reg_bit_set: void (*)(struct aspeed_sgpio * gpio,unsigned int offset,const enum aspeed_sgpio_reg reg,bool val)
  - reg_bit_get: bool (*)(struct aspeed_sgpio * gpio,unsigned int offset,const enum aspeed_sgpio_reg reg)
  - reg_bank_get: int (*)(struct aspeed_sgpio * gpio,unsigned int offset,const enum aspeed_sgpio_reg reg)

### aspeed_sgpio_bank
- Line: 68
- Members:
  - pin_mask: const u32
  - llops: const struct aspeed_sgpio_llops *
  - cfg_offset: const u32
  - chip: gpio_chip
  - dev: device *
  - pclk: clk *
  - lock: raw_spinlock_t
  - base: void __iomem *
  - irq: int
  - pdata: const struct aspeed_sgpio_pdata *
  - val_regs: u16
  - rdata_reg: u16
  - irq_regs: u16
  - tolerance_regs: u16
  - reg_bit_set: void (*)(struct aspeed_sgpio * gpio,unsigned int offset,const enum aspeed_sgpio_reg reg,bool val)
  - reg_bit_get: bool (*)(struct aspeed_sgpio * gpio,unsigned int offset,const enum aspeed_sgpio_reg reg)
  - reg_bank_get: int (*)(struct aspeed_sgpio * gpio,unsigned int offset,const enum aspeed_sgpio_reg reg)

### aspeed_sgpio_llops
- Line: 120
- Members:
  - pin_mask: const u32
  - llops: const struct aspeed_sgpio_llops *
  - cfg_offset: const u32
  - chip: gpio_chip
  - dev: device *
  - pclk: clk *
  - lock: raw_spinlock_t
  - base: void __iomem *
  - irq: int
  - pdata: const struct aspeed_sgpio_pdata *
  - val_regs: u16
  - rdata_reg: u16
  - irq_regs: u16
  - tolerance_regs: u16
  - reg_bit_set: void (*)(struct aspeed_sgpio * gpio,unsigned int offset,const enum aspeed_sgpio_reg reg,bool val)
  - reg_bit_get: bool (*)(struct aspeed_sgpio * gpio,unsigned int offset,const enum aspeed_sgpio_reg reg)
  - reg_bank_get: int (*)(struct aspeed_sgpio * gpio,unsigned int offset,const enum aspeed_sgpio_reg reg)

### aspeed_sgpio_pdata
- Line: 52
- Members:
  - pin_mask: const u32
  - llops: const struct aspeed_sgpio_llops *
  - cfg_offset: const u32
  - chip: gpio_chip
  - dev: device *
  - pclk: clk *
  - lock: raw_spinlock_t
  - base: void __iomem *
  - irq: int
  - pdata: const struct aspeed_sgpio_pdata *
  - val_regs: u16
  - rdata_reg: u16
  - irq_regs: u16
  - tolerance_regs: u16
  - reg_bit_set: void (*)(struct aspeed_sgpio * gpio,unsigned int offset,const enum aspeed_sgpio_reg reg,bool val)
  - reg_bit_get: bool (*)(struct aspeed_sgpio * gpio,unsigned int offset,const enum aspeed_sgpio_reg reg)
  - reg_bank_get: int (*)(struct aspeed_sgpio * gpio,unsigned int offset,const enum aspeed_sgpio_reg reg)

## Enums (1)

### aspeed_sgpio_reg
- Line: 109

## Variables (9)

- static **aspeed_sgpio_banks** : const struct aspeed_sgpio_bank[] (line 82)
- static **aspeed_sgpio_driver** : platform_driver (line 698)
- static **aspeed_sgpio_g4_llops** : const struct aspeed_sgpio_llops (line 500)
- static **aspeed_sgpio_g7_llops** : const struct aspeed_sgpio_llops (line 584)
- static **aspeed_sgpio_irq_chip** : const struct irq_chip (line 394)
- static **aspeed_sgpio_of_table** : const struct of_device_id[] (line 596)
- static **ast2400_sgpio_pdata** : const struct aspeed_sgpio_pdata (line 506)
- static **ast2600_sgpiom_pdata** : const struct aspeed_sgpio_pdata (line 536)
- static **ast2700_sgpiom_pdata** : const struct aspeed_sgpio_pdata (line 590)

## Macros (36)

- **ASPEED_SGPIO_CLK_DIV_MASK** (line 48)
- **ASPEED_SGPIO_ENABLE** (line 49)
- **ASPEED_SGPIO_G4_CFG_OFFSET** (line 45)
- **ASPEED_SGPIO_G7_CFG_OFFSET** (line 46)
- **ASPEED_SGPIO_PINS_SHIFT** (line 50)
- **GPIO_BANK**(x) (line 187)
- **GPIO_BIT**(x) (line 189)
- **GPIO_IRQ_ENABLE** (line 130)
- **GPIO_IRQ_STATUS** (line 134)
- **GPIO_IRQ_TYPE0** (line 131)
- **GPIO_IRQ_TYPE1** (line 132)
- **GPIO_IRQ_TYPE2** (line 133)
- **GPIO_OFFSET**(x) (line 188)
- **GPIO_VAL_VALUE** (line 129)
- **SELECT_FROM_CSR** (line 41)
- **SELECT_FROM_PARALLEL_IN** (line 42)
- **SELECT_FROM_SERIAL_IN** (line 43)
- **SGPIO_G7_CTRL_REG_BASE** (line 24)
- **SGPIO_G7_CTRL_REG_OFFSET**(x) (line 25)
- **SGPIO_G7_HW_BYPASS_EN** (line 34)
- **SGPIO_G7_HW_IN_SEL** (line 35)
- **SGPIO_G7_INPUT_MASK** (line 33)
- **SGPIO_G7_IN_DATA** (line 37)
- **SGPIO_G7_IRQ_EN** (line 28)
- **SGPIO_G7_IRQ_STS** (line 36)
- **SGPIO_G7_IRQ_STS_BASE** (line 22)
- **SGPIO_G7_IRQ_STS_OFFSET**(x) (line 23)
- **SGPIO_G7_IRQ_TYPE0** (line 29)
- **SGPIO_G7_IRQ_TYPE1** (line 30)
- **SGPIO_G7_IRQ_TYPE2** (line 31)
- **SGPIO_G7_OUT_DATA** (line 26)
- **SGPIO_G7_PARALLEL_IN_DATA** (line 38)
- **SGPIO_G7_PARALLEL_OUT_DATA** (line 27)
- **SGPIO_G7_PARALLEL_OUT_SEL** (line 40)
- **SGPIO_G7_RST_TOLERANCE** (line 32)
- **SGPIO_G7_SERIAL_OUT_SEL** (line 39)
