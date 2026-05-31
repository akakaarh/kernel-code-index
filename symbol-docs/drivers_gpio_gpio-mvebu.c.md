# drivers/gpio/gpio-mvebu.c

Subsystem: drivers/gpio

## Functions (40)

### mvebu_gpio_blink
- Return type: static void
- Signature: mvebu_gpio_blink(struct gpio_chip * chip,unsigned int pin,int value)
- Line: 331
- Calls: gpiochip_get_data
- Called by: mvebu_gpio_direction_output, mvebu_pwm_apply

### mvebu_gpio_dbg_show
- Return type: static void
- Signature: mvebu_gpio_dbg_show(struct seq_file * s,struct gpio_chip * chip)
- Line: 877
- Calls: gpiochip_get_data, mvebu_gpio_read_edge_cause, mvebu_gpio_read_edge_mask, mvebu_gpio_read_level_mask

### mvebu_gpio_direction_input
- Return type: static int
- Signature: mvebu_gpio_direction_input(struct gpio_chip * chip,unsigned int pin)
- Line: 340
- Calls: gpiochip_get_data

### mvebu_gpio_direction_output
- Return type: static int
- Signature: mvebu_gpio_direction_output(struct gpio_chip * chip,unsigned int pin,int value)
- Line: 359
- Calls: gpiochip_get_data, mvebu_gpio_blink, mvebu_gpio_set

### mvebu_gpio_edge_irq_mask
- Return type: static void
- Signature: mvebu_gpio_edge_irq_mask(struct irq_data * d)
- Line: 415
- Calls: mvebu_gpio_write_edge_mask

### mvebu_gpio_edge_irq_unmask
- Return type: static void
- Signature: mvebu_gpio_edge_irq_unmask(struct irq_data * d)
- Line: 427
- Calls: mvebu_gpio_write_edge_cause, mvebu_gpio_write_edge_mask

### mvebu_gpio_get
- Return type: static int
- Signature: mvebu_gpio_get(struct gpio_chip * chip,unsigned int pin)
- Line: 309
- Calls: gpiochip_get_data

### mvebu_gpio_get_direction
- Return type: static int
- Signature: mvebu_gpio_get_direction(struct gpio_chip * chip,unsigned int pin)
- Line: 382
- Calls: gpiochip_get_data

### mvebu_gpio_irq_ack
- Return type: static void
- Signature: mvebu_gpio_irq_ack(struct irq_data * d)
- Line: 405
- Calls: mvebu_gpio_write_edge_cause

### mvebu_gpio_irq_handler
- Return type: static void
- Signature: mvebu_gpio_irq_handler(struct irq_desc * desc)
- Line: 554
- Calls: mvebu_gpio_read_edge_cause, mvebu_gpio_read_edge_mask, mvebu_gpio_read_level_mask

### mvebu_gpio_irq_set_type
- Return type: static int
- Signature: mvebu_gpio_irq_set_type(struct irq_data * d,unsigned int type)
- Line: 490

### mvebu_gpio_level_irq_mask
- Return type: static void
- Signature: mvebu_gpio_level_irq_mask(struct irq_data * d)
- Line: 440
- Calls: mvebu_gpio_write_level_mask

### mvebu_gpio_level_irq_unmask
- Return type: static void
- Signature: mvebu_gpio_level_irq_unmask(struct irq_data * d)
- Line: 452
- Calls: mvebu_gpio_write_level_mask

### mvebu_gpio_probe
- Return type: static int
- Signature: mvebu_gpio_probe(struct platform_device * pdev)
- Line: 1116
- Calls: mvebu_gpio_probe_raw, mvebu_gpio_probe_syscon, mvebu_pwm_probe

### mvebu_gpio_probe_raw
- Return type: static int
- Signature: mvebu_gpio_probe_raw(struct platform_device * pdev,struct mvebu_gpio_chip * mvchip)
- Line: 1057
- Called by: mvebu_gpio_probe

### mvebu_gpio_probe_syscon
- Return type: static int
- Signature: mvebu_gpio_probe_syscon(struct platform_device * pdev,struct mvebu_gpio_chip * mvchip)
- Line: 1096
- Called by: mvebu_gpio_probe

### mvebu_gpio_read_edge_cause
- Return type: static u32
- Signature: mvebu_gpio_read_edge_cause(struct mvebu_gpio_chip * mvchip)
- Line: 162
- Calls: mvebu_gpioreg_edge_cause
- Called by: mvebu_gpio_dbg_show, mvebu_gpio_irq_handler

### mvebu_gpio_read_edge_mask
- Return type: static u32
- Signature: mvebu_gpio_read_edge_mask(struct mvebu_gpio_chip * mvchip)
- Line: 212
- Calls: mvebu_gpioreg_edge_mask
- Called by: mvebu_gpio_dbg_show, mvebu_gpio_irq_handler

### mvebu_gpio_read_level_mask
- Return type: static u32
- Signature: mvebu_gpio_read_level_mask(struct mvebu_gpio_chip * mvchip)
- Line: 262
- Calls: mvebu_gpioreg_level_mask
- Called by: mvebu_gpio_dbg_show, mvebu_gpio_irq_handler

### mvebu_gpio_remove_irq_domain
- Return type: static void
- Signature: mvebu_gpio_remove_irq_domain(void * data)
- Line: 1109

### mvebu_gpio_resume
- Return type: static int
- Signature: mvebu_gpio_resume(struct platform_device * pdev)
- Line: 1005
- Calls: mvebu_pwm_resume

### mvebu_gpio_set
- Return type: static int
- Signature: mvebu_gpio_set(struct gpio_chip * chip,unsigned int pin,int value)
- Line: 301
- Calls: gpiochip_get_data
- Called by: mvebu_gpio_direction_output

### mvebu_gpio_suspend
- Return type: static int
- Signature: mvebu_gpio_suspend(struct platform_device * pdev,pm_message_t state)
- Line: 953
- Calls: mvebu_pwm_suspend

### mvebu_gpio_to_irq
- Return type: static int
- Signature: mvebu_gpio_to_irq(struct gpio_chip * chip,unsigned int pin)
- Line: 395
- Calls: gpiochip_get_data

### mvebu_gpio_write_edge_cause
- Return type: static void
- Signature: mvebu_gpio_write_edge_cause(struct mvebu_gpio_chip * mvchip,u32 val)
- Line: 175
- Calls: mvebu_gpioreg_edge_cause
- Called by: mvebu_gpio_edge_irq_unmask, mvebu_gpio_irq_ack

### mvebu_gpio_write_edge_mask
- Return type: static void
- Signature: mvebu_gpio_write_edge_mask(struct mvebu_gpio_chip * mvchip,u32 val)
- Line: 225
- Calls: mvebu_gpioreg_edge_mask
- Called by: mvebu_gpio_edge_irq_mask, mvebu_gpio_edge_irq_unmask

### mvebu_gpio_write_level_mask
- Return type: static void
- Signature: mvebu_gpio_write_level_mask(struct mvebu_gpio_chip * mvchip,u32 val)
- Line: 275
- Calls: mvebu_gpioreg_level_mask
- Called by: mvebu_gpio_level_irq_mask, mvebu_gpio_level_irq_unmask

### mvebu_gpioreg_edge_cause
- Return type: static void
- Signature: mvebu_gpioreg_edge_cause(struct mvebu_gpio_chip * mvchip,struct regmap ** map,unsigned int * offset)
- Line: 139
- Called by: mvebu_gpio_read_edge_cause, mvebu_gpio_write_edge_cause

### mvebu_gpioreg_edge_mask
- Return type: static void
- Signature: mvebu_gpioreg_edge_mask(struct mvebu_gpio_chip * mvchip,struct regmap ** map,unsigned int * offset)
- Line: 185
- Called by: mvebu_gpio_read_edge_mask, mvebu_gpio_write_edge_mask

### mvebu_gpioreg_level_mask
- Return type: static void
- Signature: mvebu_gpioreg_level_mask(struct mvebu_gpio_chip * mvchip,struct regmap ** map,unsigned int * offset)
- Line: 235
- Called by: mvebu_gpio_read_level_mask, mvebu_gpio_write_level_mask

### mvebu_pwm_apply
- Return type: static int
- Signature: mvebu_pwm_apply(struct pwm_chip * chip,struct pwm_device * pwm,const struct pwm_state * state)
- Line: 695
- Calls: mvebu_gpio_blink, mvebu_pwmreg_blink_off_duration, mvebu_pwmreg_blink_on_duration, to_mvebu_pwm

### mvebu_pwm_free
- Return type: static void
- Signature: mvebu_pwm_free(struct pwm_chip * chip,struct pwm_device * pwm)
- Line: 643
- Calls: gpiochip_free_own_desc, to_mvebu_pwm

### mvebu_pwm_get_state
- Return type: static int
- Signature: mvebu_pwm_get_state(struct pwm_chip * chip,struct pwm_device * pwm,struct pwm_state * state)
- Line: 654
- Calls: mvebu_pwmreg_blink_off_duration, mvebu_pwmreg_blink_on_duration, to_mvebu_pwm

### mvebu_pwm_probe
- Return type: static int
- Signature: mvebu_pwm_probe(struct platform_device * pdev,struct mvebu_gpio_chip * mvchip,int id)
- Line: 779
- Calls: to_mvebu_pwm
- Called by: mvebu_gpio_probe

### mvebu_pwm_request
- Return type: static int
- Signature: mvebu_pwm_request(struct pwm_chip * chip,struct pwm_device * pwm)
- Line: 614
- Calls: gpiochip_request_own_desc, to_mvebu_pwm

### mvebu_pwm_resume
- Return type: static void __maybe_unused
- Signature: mvebu_pwm_resume(struct mvebu_gpio_chip * mvchip)
- Line: 767
- Calls: mvebu_pwmreg_blink_off_duration, mvebu_pwmreg_blink_on_duration
- Called by: mvebu_gpio_resume

### mvebu_pwm_suspend
- Return type: static void __maybe_unused
- Signature: mvebu_pwm_suspend(struct mvebu_gpio_chip * mvchip)
- Line: 755
- Calls: mvebu_pwmreg_blink_off_duration, mvebu_pwmreg_blink_on_duration
- Called by: mvebu_gpio_suspend

### mvebu_pwmreg_blink_off_duration
- Return type: static unsigned int
- Signature: mvebu_pwmreg_blink_off_duration(struct mvebu_pwm * mvpwm)
- Line: 293
- Called by: mvebu_pwm_apply, mvebu_pwm_get_state, mvebu_pwm_resume, mvebu_pwm_suspend

### mvebu_pwmreg_blink_on_duration
- Return type: static unsigned int
- Signature: mvebu_pwmreg_blink_on_duration(struct mvebu_pwm * mvpwm)
- Line: 288
- Called by: mvebu_pwm_apply, mvebu_pwm_get_state, mvebu_pwm_resume, mvebu_pwm_suspend

### to_mvebu_pwm
- Return type: static mvebu_pwm *
- Signature: to_mvebu_pwm(struct pwm_chip * chip)
- Line: 609
- Called by: mvebu_pwm_apply, mvebu_pwm_free, mvebu_pwm_get_state, mvebu_pwm_probe, mvebu_pwm_request

## Structs (2)

### mvebu_gpio_chip
- Line: 112
- Members:
  - regs: regmap *
  - offset: u32
  - clk_rate: unsigned long
  - gpiod: gpio_desc *
  - lock: spinlock_t
  - mvchip: mvebu_gpio_chip *
  - blink_select: u32
  - blink_on_duration: u32
  - blink_off_duration: u32
  - chip: gpio_chip
  - regs: regmap *
  - offset: u32
  - percpu_regs: regmap *
  - irqbase: int
  - domain: irq_domain *
  - soc_variant: int
  - clk: clk *
  - mvpwm: mvebu_pwm *
  - out_reg: u32
  - io_conf_reg: u32
  - blink_en_reg: u32
  - in_pol_reg: u32
  - edge_mask_regs: u32[4]
  - level_mask_regs: u32[4]

### mvebu_pwm
- Line: 98
- Members:
  - regs: regmap *
  - offset: u32
  - clk_rate: unsigned long
  - gpiod: gpio_desc *
  - lock: spinlock_t
  - mvchip: mvebu_gpio_chip *
  - blink_select: u32
  - blink_on_duration: u32
  - blink_off_duration: u32
  - chip: gpio_chip
  - regs: regmap *
  - offset: u32
  - percpu_regs: regmap *
  - irqbase: int
  - domain: irq_domain *
  - soc_variant: int
  - clk: clk *
  - mvpwm: mvebu_pwm *
  - out_reg: u32
  - io_conf_reg: u32
  - blink_en_reg: u32
  - in_pol_reg: u32
  - edge_mask_regs: u32[4]
  - level_mask_regs: u32[4]

## Variables (4)

- static **mvebu_gpio_driver** : platform_driver (line 1298)
- static **mvebu_gpio_of_match** : const struct of_device_id[] (line 927)
- static **mvebu_gpio_regmap_config** : const struct regmap_config (line 600)
- static **mvebu_pwm_ops** : const struct pwm_ops (line 748)

## Macros (26)

- **AP80X_GPIO0_OFF_A8K** (line 75)
- **CP11X_GPIO0_OFF_A8K** (line 76)
- **CP11X_GPIO1_OFF_A8K** (line 77)
- **GPIO_BLINK_CNT_SELECT_OFF** (line 65)
- **GPIO_BLINK_EN_OFF** (line 59)
- **GPIO_DATA_IN_OFF** (line 61)
- **GPIO_EDGE_CAUSE_ARMADAXP_OFF**(cpu) (line 87)
- **GPIO_EDGE_CAUSE_OFF** (line 62)
- **GPIO_EDGE_MASK_ARMADAXP_OFF**(cpu) (line 88)
- **GPIO_EDGE_MASK_MV78200_OFF**(cpu) (line 80)
- **GPIO_EDGE_MASK_OFF** (line 63)
- **GPIO_IN_POL_OFF** (line 60)
- **GPIO_IO_CONF_OFF** (line 58)
- **GPIO_LEVEL_MASK_ARMADAXP_OFF**(cpu) (line 89)
- **GPIO_LEVEL_MASK_MV78200_OFF**(cpu) (line 81)
- **GPIO_LEVEL_MASK_OFF** (line 64)
- **GPIO_OUT_OFF** (line 57)
- **MVEBU_GPIO_SOC_VARIANT_A8K** (line 94)
- **MVEBU_GPIO_SOC_VARIANT_ARMADAXP** (line 93)
- **MVEBU_GPIO_SOC_VARIANT_MV78200** (line 92)
- **MVEBU_GPIO_SOC_VARIANT_ORION** (line 91)
- **MVEBU_MAX_GPIO_PER_BANK** (line 96)
- **PWM_BLINK_COUNTER_B_OFF** (line 72)
- **PWM_BLINK_OFF_DURATION_OFF** (line 71)
- **PWM_BLINK_ON_DURATION_OFF** (line 70)
- **mvebu_gpio_dbg_show** (line 924)
