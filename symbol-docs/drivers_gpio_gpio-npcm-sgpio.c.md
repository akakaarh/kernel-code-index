# drivers/gpio/gpio-npcm-sgpio.c

Subsystem: drivers/gpio

## Functions (20)

### bank_reg
- Return type: static void __iomem *
- Signature: bank_reg(struct npcm_sgpio * gpio,const struct npcm_sgpio_bank * bank,const enum npcm_sgpio_reg reg)
- Line: 137
- Called by: npcm_sgpio_get, npcm_sgpio_irq_ack, npcm_sgpio_irq_handler, npcm_sgpio_irq_set_mask, npcm_sgpio_set, npcm_sgpio_set_type, npcm_sgpio_setup_irqs

### npcm_sgpio_dir_in
- Return type: static int
- Signature: npcm_sgpio_dir_in(struct gpio_chip * gc,unsigned int offset)
- Line: 204
- Calls: gpiochip_get_data

### npcm_sgpio_dir_out
- Return type: static int
- Signature: npcm_sgpio_dir_out(struct gpio_chip * gc,unsigned int offset,int val)
- Line: 212

### npcm_sgpio_get
- Return type: static int
- Signature: npcm_sgpio_get(struct gpio_chip * gc,unsigned int offset)
- Line: 247
- Calls: bank_reg, gpiochip_get_data, offset_to_bank

### npcm_sgpio_get_direction
- Return type: static int
- Signature: npcm_sgpio_get_direction(struct gpio_chip * gc,unsigned int offset)
- Line: 217
- Calls: gpiochip_get_data

### npcm_sgpio_init_port
- Return type: static int
- Signature: npcm_sgpio_init_port(struct npcm_sgpio * gpio)
- Line: 180
- Called by: npcm_sgpio_probe

### npcm_sgpio_irq_ack
- Return type: static void
- Signature: npcm_sgpio_irq_ack(struct irq_data * d)
- Line: 354
- Calls: bank_reg, npcm_sgpio_irqd_to_data

### npcm_sgpio_irq_handler
- Return type: static void
- Signature: npcm_sgpio_irq_handler(struct irq_desc * desc)
- Line: 432
- Calls: bank_reg, gpiochip_get_data

### npcm_sgpio_irq_init_valid_mask
- Return type: static void
- Signature: npcm_sgpio_irq_init_valid_mask(struct gpio_chip * gc,unsigned long * valid_mask,unsigned int ngpios)
- Line: 306
- Calls: gpiochip_get_data

### npcm_sgpio_irq_mask
- Return type: static void
- Signature: npcm_sgpio_irq_mask(struct irq_data * d)
- Line: 370
- Calls: npcm_sgpio_irq_set_mask

### npcm_sgpio_irq_set_mask
- Return type: static void
- Signature: npcm_sgpio_irq_set_mask(struct irq_data * d,bool set)
- Line: 317
- Calls: bank_reg, npcm_sgpio_irqd_to_data, npcm_sgpio_setup_enable
- Called by: npcm_sgpio_irq_mask, npcm_sgpio_irq_unmask

### npcm_sgpio_irq_unmask
- Return type: static void
- Signature: npcm_sgpio_irq_unmask(struct irq_data * d)
- Line: 375
- Calls: npcm_sgpio_irq_set_mask

### npcm_sgpio_irqd_to_data
- Return type: static void
- Signature: npcm_sgpio_irqd_to_data(struct irq_data * d,struct npcm_sgpio ** gpio,const struct npcm_sgpio_bank ** bank,u8 * bit,unsigned int * offset)
- Line: 164
- Calls: offset_to_bank
- Called by: npcm_sgpio_irq_ack, npcm_sgpio_irq_set_mask, npcm_sgpio_set_type

### npcm_sgpio_probe
- Return type: static int
- Signature: npcm_sgpio_probe(struct platform_device * pdev)
- Line: 499
- Calls: npcm_sgpio_init_port, npcm_sgpio_setup_clk, npcm_sgpio_setup_enable, npcm_sgpio_setup_irqs

### npcm_sgpio_set
- Return type: static int
- Signature: npcm_sgpio_set(struct gpio_chip * gc,unsigned int offset,int val)
- Line: 227
- Calls: bank_reg, gpiochip_get_data, offset_to_bank

### npcm_sgpio_set_type
- Return type: static int
- Signature: npcm_sgpio_set_type(struct irq_data * d,unsigned int type)
- Line: 380
- Calls: bank_reg, npcm_sgpio_irqd_to_data, npcm_sgpio_setup_enable

### npcm_sgpio_setup_clk
- Return type: static int
- Signature: npcm_sgpio_setup_clk(struct npcm_sgpio * gpio,const struct npcm_clk_cfg * clk_cfg)
- Line: 283
- Called by: npcm_sgpio_probe

### npcm_sgpio_setup_enable
- Return type: static void
- Signature: npcm_sgpio_setup_enable(struct npcm_sgpio * gpio,bool enable)
- Line: 268
- Called by: npcm_sgpio_irq_set_mask, npcm_sgpio_probe, npcm_sgpio_set_type, npcm_sgpio_setup_irqs

### npcm_sgpio_setup_irqs
- Return type: static int
- Signature: npcm_sgpio_setup_irqs(struct npcm_sgpio * gpio,struct platform_device * pdev)
- Line: 464
- Calls: bank_reg, npcm_sgpio_setup_enable
- Called by: npcm_sgpio_probe

### offset_to_bank
- Return type: static const struct npcm_sgpio_bank *
- Signature: offset_to_bank(unsigned int offset)
- Line: 157
- Called by: npcm_sgpio_get, npcm_sgpio_irqd_to_data, npcm_sgpio_set

## Structs (3)

### npcm_clk_cfg
- Line: 51
- Members:
  - sft_clk: unsigned int *
  - clk_sel: unsigned int *
  - cfg_opt: unsigned int
  - chip: gpio_chip
  - pclk: clk *
  - intc: irq_chip
  - lock: raw_spinlock_t
  - base: void __iomem *
  - irq: int
  - nin_sgpio: u8
  - nout_sgpio: u8
  - in_port: u8
  - out_port: u8
  - int_type: u8[]
  - rdata_reg: u8
  - wdata_reg: u8
  - event_config: u8
  - event_status: u8

### npcm_sgpio
- Line: 57
- Members:
  - sft_clk: unsigned int *
  - clk_sel: unsigned int *
  - cfg_opt: unsigned int
  - chip: gpio_chip
  - pclk: clk *
  - intc: irq_chip
  - lock: raw_spinlock_t
  - base: void __iomem *
  - irq: int
  - nin_sgpio: u8
  - nout_sgpio: u8
  - in_port: u8
  - out_port: u8
  - int_type: u8[]
  - rdata_reg: u8
  - wdata_reg: u8
  - event_config: u8
  - event_status: u8

### npcm_sgpio_bank
- Line: 72
- Members:
  - sft_clk: unsigned int *
  - clk_sel: unsigned int *
  - cfg_opt: unsigned int
  - chip: gpio_chip
  - pclk: clk *
  - intc: irq_chip
  - lock: raw_spinlock_t
  - base: void __iomem *
  - irq: int
  - nin_sgpio: u8
  - nout_sgpio: u8
  - in_port: u8
  - out_port: u8
  - int_type: u8[]
  - rdata_reg: u8
  - wdata_reg: u8
  - event_config: u8
  - event_status: u8

## Enums (1)

### npcm_sgpio_reg
- Line: 79

## Variables (10)

- static **npcm750_CLK_SEL** : unsigned int[] (line 574)
- static **npcm750_SFT_CLK** : unsigned int[] (line 570)
- static **npcm750_sgpio_pdata** : npcm_clk_cfg (line 586)
- static **npcm845_CLK_SEL** : unsigned int[] (line 582)
- static **npcm845_SFT_CLK** : unsigned int[] (line 578)
- static **npcm845_sgpio_pdata** : const struct npcm_clk_cfg (line 592)
- static **npcm_sgpio_banks** : const struct npcm_sgpio_bank[] (line 86)
- static **npcm_sgpio_driver** : platform_driver (line 605)
- static **npcm_sgpio_of_table** : const struct of_device_id[] (line 598)
- static **sgpio_irq_chip** : const struct irq_chip (line 454)

## Macros (20)

- **GPIO_BANK**(x) (line 44)
- **GPIO_BIT**(x) (line 45)
- **MAX_NR_HW_SGPIO** (line 20)
- **NPCM_750_OPT** (line 41)
- **NPCM_845_OPT** (line 42)
- **NPCM_CLK_MHZ** (line 40)
- **NPCM_IOXCFG1** (line 22)
- **NPCM_IOXCFG1_LDSH_POL** (line 25)
- **NPCM_IOXCFG1_SCLK_POL** (line 24)
- **NPCM_IOXCFG1_SFT_CLK** (line 23)
- **NPCM_IOXCFG2** (line 32)
- **NPCM_IOXCFG2_PORT** (line 33)
- **NPCM_IOXCTS** (line 27)
- **NPCM_IOXCTS_IOXIF_EN** (line 28)
- **NPCM_IOXCTS_RD_MODE** (line 29)
- **NPCM_IOXCTS_RD_MODE_PERIODIC** (line 30)
- **NPCM_IXOEVCFG_BOTH** (line 38)
- **NPCM_IXOEVCFG_FALLING** (line 36)
- **NPCM_IXOEVCFG_MASK** (line 35)
- **NPCM_IXOEVCFG_RISING** (line 37)
