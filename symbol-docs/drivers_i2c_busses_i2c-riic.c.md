# drivers/i2c/busses/i2c-riic.c

Subsystem: drivers/i2c

## Functions (22)

### riic_bus_barrier
- Return type: static int
- Signature: riic_bus_barrier(struct riic_dev * riic)
- Line: 147

### riic_clear_set_bit
- Return type: static void
- Signature: riic_clear_set_bit(struct riic_dev * riic,u8 clear,u8 set,u8 reg)
- Line: 142

### riic_eei_isr
- Return type: static irqreturn_t
- Signature: riic_eei_isr(int irq,void * data)
- Line: 329

### riic_func
- Return type: static u32
- Signature: riic_func(struct i2c_adapter * adap)
- Line: 342

### riic_get_scl
- Return type: static int
- Signature: riic_get_scl(struct i2c_adapter * adap)
- Line: 458

### riic_get_sda
- Return type: static int
- Signature: riic_get_sda(struct i2c_adapter * adap)
- Line: 465

### riic_i2c_probe
- Return type: static int
- Signature: riic_i2c_probe(struct platform_device * pdev)
- Line: 519

### riic_i2c_remove
- Return type: static void
- Signature: riic_i2c_remove(struct platform_device * pdev)
- Line: 599

### riic_i2c_resume
- Return type: static int
- Signature: riic_i2c_resume(struct device * dev)
- Line: 696

### riic_i2c_resume_noirq
- Return type: static int
- Signature: riic_i2c_resume_noirq(struct device * dev)
- Line: 718

### riic_i2c_suspend
- Return type: static int
- Signature: riic_i2c_suspend(struct device * dev)
- Line: 671

### riic_i2c_suspend_noirq
- Return type: static int
- Signature: riic_i2c_suspend_noirq(struct device * dev)
- Line: 703

### riic_init_hw
- Return type: static int
- Signature: riic_init_hw(struct riic_dev * riic)
- Line: 352

### riic_rdrf_isr
- Return type: static irqreturn_t
- Signature: riic_rdrf_isr(int irq,void * data)
- Line: 280

### riic_readb
- Return type: static u8
- Signature: riic_readb(struct riic_dev * riic,u8 offset)
- Line: 137

### riic_set_scl
- Return type: static void
- Signature: riic_set_scl(struct i2c_adapter * adap,int val)
- Line: 472

### riic_set_sda
- Return type: static void
- Signature: riic_set_sda(struct i2c_adapter * adap,int val)
- Line: 484

### riic_stop_isr
- Return type: static irqreturn_t
- Signature: riic_stop_isr(int irq,void * data)
- Line: 314

### riic_tdre_isr
- Return type: static irqreturn_t
- Signature: riic_tdre_isr(int irq,void * data)
- Line: 214

### riic_tend_isr
- Return type: static irqreturn_t
- Signature: riic_tend_isr(int irq,void * data)
- Line: 255

### riic_writeb
- Return type: static void
- Signature: riic_writeb(struct riic_dev * riic,u8 val,u8 offset)
- Line: 132

### riic_xfer
- Return type: static int
- Signature: riic_xfer(struct i2c_adapter * adap,struct i2c_msg msgs[],int num)
- Line: 168

## Structs (3)

### riic_dev
- Line: 111
- Members:
  - regs: const u8 *
  - irqs: const struct riic_irq_desc *
  - num_irqs: u8
  - fast_mode_plus: bool
  - base: void __iomem *
  - buf: u8 *
  - msg: i2c_msg *
  - bytes_left: int
  - err: int
  - is_last: int
  - info: const struct riic_of_data *
  - msg_done: completion
  - adapter: i2c_adapter
  - clk: clk *
  - rstc: reset_control *
  - i2c_t: i2c_timings
  - res_num: int
  - isr: irq_handler_t
  - name: char *

### riic_irq_desc
- Line: 126
- Members:
  - regs: const u8 *
  - irqs: const struct riic_irq_desc *
  - num_irqs: u8
  - fast_mode_plus: bool
  - base: void __iomem *
  - buf: u8 *
  - msg: i2c_msg *
  - bytes_left: int
  - err: int
  - is_last: int
  - info: const struct riic_of_data *
  - msg_done: completion
  - adapter: i2c_adapter
  - clk: clk *
  - rstc: reset_control *
  - i2c_t: i2c_timings
  - res_num: int
  - isr: irq_handler_t
  - name: char *

### riic_of_data
- Line: 104
- Members:
  - regs: const u8 *
  - irqs: const struct riic_irq_desc *
  - num_irqs: u8
  - fast_mode_plus: bool
  - base: void __iomem *
  - buf: u8 *
  - msg: i2c_msg *
  - bytes_left: int
  - err: int
  - is_last: int
  - info: const struct riic_of_data *
  - msg_done: completion
  - adapter: i2c_adapter
  - clk: clk *
  - rstc: reset_control *
  - i2c_t: i2c_timings
  - res_num: int
  - isr: irq_handler_t
  - name: char *

## Enums (1)

### riic_reg_list
- Line: 88

## Variables (13)

- static **riic_algo** : const struct i2c_algorithm (line 347)
- static **riic_bri** : i2c_bus_recovery_info (line 496)
- static **riic_i2c_driver** : platform_driver (line 760)
- static **riic_i2c_dt_ids** : const struct of_device_id[] (line 752)
- static **riic_i2c_pm_ops** : const struct dev_pm_ops (line 747)
- static **riic_irqs** : const struct riic_irq_desc[] (line 504)
- static **riic_rz_a1h_info** : const struct riic_of_data (line 637)
- static **riic_rz_a_info** : const struct riic_of_data (line 630)
- static **riic_rz_a_regs** : const u8[] (line 615)
- static **riic_rz_t2h_info** : const struct riic_of_data (line 665)
- static **riic_rz_v2h_info** : const struct riic_of_data (line 658)
- static **riic_rz_v2h_regs** : const u8[] (line 643)
- static **riic_rzt2h_irqs** : const struct riic_irq_desc[] (line 512)

## Macros (27)

- **ICBR_RESERVED** (line 84)
- **ICCR1_ICE** (line 52)
- **ICCR1_IICRST** (line 53)
- **ICCR1_SCLI** (line 57)
- **ICCR1_SCLO** (line 55)
- **ICCR1_SDAI** (line 58)
- **ICCR1_SDAO** (line 56)
- **ICCR1_SOWP** (line 54)
- **ICCR2_BBSY** (line 60)
- **ICCR2_RS** (line 62)
- **ICCR2_SP** (line 61)
- **ICCR2_ST** (line 63)
- **ICFER_FMPE** (line 73)
- **ICIER_NAKIE** (line 78)
- **ICIER_RIE** (line 77)
- **ICIER_SPIE** (line 79)
- **ICIER_TEIE** (line 76)
- **ICIER_TIE** (line 75)
- **ICMR1_BCWP** (line 66)
- **ICMR1_CKS**(_x) (line 67)
- **ICMR1_CKS_MASK** (line 65)
- **ICMR3_ACKBT** (line 71)
- **ICMR3_ACKWP** (line 70)
- **ICMR3_RDRFS** (line 69)
- **ICSR2_NACKF** (line 81)
- **ICSR2_STOP** (line 82)
- **RIIC_INIT_MSG** (line 86)
