# drivers/i2c/busses/i2c-pxa.c

Subsystem: drivers/i2c

## Functions (50)

### decode_ICR
- Return type: static void
- Signature: decode_ICR(unsigned int val)
- Line: 349

### decode_ISR
- Return type: static void
- Signature: decode_ISR(unsigned int val)
- Line: 325

### decode_bits
- Return type: static void
- Signature: decode_bits(const char * prefix,const struct bits * bits,int num,u32 val)
- Line: 299

### i2c_adap_pxa_exit
- Return type: static void __exit
- Signature: i2c_adap_pxa_exit(void)
- Line: 1615

### i2c_adap_pxa_init
- Return type: static int __init
- Signature: i2c_adap_pxa_init(void)
- Line: 1610

### i2c_pxa_abort
- Return type: static void
- Signature: i2c_pxa_abort(struct pxa_i2c * i2c)
- Line: 401

### i2c_pxa_do_pio_xfer
- Return type: static int
- Signature: i2c_pxa_do_pio_xfer(struct pxa_i2c * i2c,struct i2c_msg * msg,int num)
- Line: 1200

### i2c_pxa_do_reset
- Return type: static void
- Signature: i2c_pxa_do_reset(struct pxa_i2c * i2c)
- Line: 573

### i2c_pxa_do_xfer
- Return type: static int
- Signature: i2c_pxa_do_xfer(struct pxa_i2c * i2c,struct i2c_msg * msg,int num)
- Line: 1054

### i2c_pxa_enable
- Return type: static void
- Signature: i2c_pxa_enable(struct pxa_i2c * i2c)
- Line: 595

### i2c_pxa_functionality
- Return type: static u32
- Signature: i2c_pxa_functionality(struct i2c_adapter * adap)
- Line: 1158

### i2c_pxa_handler
- Return type: static irqreturn_t
- Signature: i2c_pxa_handler(int this_irq,void * dev_id)
- Line: 1002

### i2c_pxa_init_recovery
- Return type: static int
- Signature: i2c_pxa_init_recovery(struct pxa_i2c * i2c)
- Line: 1341

### i2c_pxa_internal_xfer
- Return type: static int
- Signature: i2c_pxa_internal_xfer(struct pxa_i2c * i2c,struct i2c_msg * msgs,int num,int (* xfer)(struct pxa_i2c *,struct i2c_msg *,int num))
- Line: 1119

### i2c_pxa_irq_rxfull
- Return type: static void
- Signature: i2c_pxa_irq_rxfull(struct pxa_i2c * i2c,u32 isr)
- Line: 973

### i2c_pxa_irq_txempty
- Return type: static void
- Signature: i2c_pxa_irq_txempty(struct pxa_i2c * i2c,u32 isr)
- Line: 866

### i2c_pxa_is_slavemode
- Return type: static int
- Signature: i2c_pxa_is_slavemode(struct pxa_i2c * i2c)
- Line: 396

### i2c_pxa_master_complete
- Return type: static void
- Signature: i2c_pxa_master_complete(struct pxa_i2c * i2c,int ret)
- Line: 854

### i2c_pxa_pio_set_master
- Return type: static int
- Signature: i2c_pxa_pio_set_master(struct pxa_i2c * i2c)
- Line: 1174

### i2c_pxa_pio_xfer
- Return type: static int
- Signature: i2c_pxa_pio_xfer(struct i2c_adapter * adap,struct i2c_msg msgs[],int num)
- Line: 1239

### i2c_pxa_prepare_recovery
- Return type: static void
- Signature: i2c_pxa_prepare_recovery(struct i2c_adapter * adap)
- Line: 1302

### i2c_pxa_probe
- Return type: static int
- Signature: i2c_pxa_probe(struct platform_device * dev)
- Line: 1427

### i2c_pxa_probe_dt
- Return type: static int
- Signature: i2c_pxa_probe_dt(struct platform_device * pdev,struct pxa_i2c * i2c,enum pxa_i2c_types * i2c_types)
- Line: 1263

### i2c_pxa_probe_pdata
- Return type: static int
- Signature: i2c_pxa_probe_pdata(struct platform_device * pdev,struct pxa_i2c * i2c,enum pxa_i2c_types * i2c_types)
- Line: 1282

### i2c_pxa_remove
- Return type: static void
- Signature: i2c_pxa_remove(struct platform_device * dev)
- Line: 1566

### i2c_pxa_reset
- Return type: static void
- Signature: i2c_pxa_reset(struct pxa_i2c * i2c)
- Line: 602

### i2c_pxa_resume_noirq
- Return type: static int
- Signature: i2c_pxa_resume_noirq(struct device * dev)
- Line: 1584

### i2c_pxa_scream_blue_murder
- Return type: static void
- Signature: i2c_pxa_scream_blue_murder(struct pxa_i2c * i2c,const char * why)
- Line: 365

### i2c_pxa_send_mastercode
- Return type: static int
- Signature: i2c_pxa_send_mastercode(struct pxa_i2c * i2c)
- Line: 829

### i2c_pxa_set_master
- Return type: static int
- Signature: i2c_pxa_set_master(struct pxa_i2c * i2c)
- Line: 488

### i2c_pxa_set_slave
- Return type: static void
- Signature: i2c_pxa_set_slave(struct pxa_i2c * i2c,int errcode)
- Line: 539

### i2c_pxa_show_state
- Return type: static void
- Signature: i2c_pxa_show_state(struct pxa_i2c * i2c,int lno,const char * fname)
- Line: 357

### i2c_pxa_slave_reg
- Return type: static int
- Signature: i2c_pxa_slave_reg(struct i2c_client * slave)
- Line: 709

### i2c_pxa_slave_rxfull
- Return type: static void
- Signature: i2c_pxa_slave_rxfull(struct pxa_i2c * i2c,u32 isr)
- Line: 634

### i2c_pxa_slave_rxfull
- Return type: static void
- Signature: i2c_pxa_slave_rxfull(struct pxa_i2c * i2c,u32 isr)
- Line: 751

### i2c_pxa_slave_start
- Return type: static void
- Signature: i2c_pxa_slave_start(struct pxa_i2c * i2c,u32 isr)
- Line: 644

### i2c_pxa_slave_start
- Return type: static void
- Signature: i2c_pxa_slave_start(struct pxa_i2c * i2c,u32 isr)
- Line: 756

### i2c_pxa_slave_stop
- Return type: static void
- Signature: i2c_pxa_slave_stop(struct pxa_i2c * i2c)
- Line: 690

### i2c_pxa_slave_stop
- Return type: static void
- Signature: i2c_pxa_slave_stop(struct pxa_i2c * i2c)
- Line: 785

### i2c_pxa_slave_txempty
- Return type: static void
- Signature: i2c_pxa_slave_txempty(struct pxa_i2c * i2c,u32 isr)
- Line: 618

### i2c_pxa_slave_txempty
- Return type: static void
- Signature: i2c_pxa_slave_txempty(struct pxa_i2c * i2c,u32 isr)
- Line: 741

### i2c_pxa_slave_unreg
- Return type: static int
- Signature: i2c_pxa_slave_unreg(struct i2c_client * slave)
- Line: 727

### i2c_pxa_start_message
- Return type: static void
- Signature: i2c_pxa_start_message(struct pxa_i2c * i2c)
- Line: 796

### i2c_pxa_stop_message
- Return type: static void
- Signature: i2c_pxa_stop_message(struct pxa_i2c * i2c)
- Line: 813

### i2c_pxa_suspend_noirq
- Return type: static int
- Signature: i2c_pxa_suspend_noirq(struct device * dev)
- Line: 1575

### i2c_pxa_unprepare_recovery
- Return type: static void
- Signature: i2c_pxa_unprepare_recovery(struct i2c_adapter * adap)
- Line: 1317

### i2c_pxa_wait_bus_not_busy
- Return type: static int
- Signature: i2c_pxa_wait_bus_not_busy(struct pxa_i2c * i2c)
- Line: 428

### i2c_pxa_wait_master
- Return type: static int
- Signature: i2c_pxa_wait_master(struct pxa_i2c * i2c)
- Line: 453

### i2c_pxa_wait_slave
- Return type: static int
- Signature: i2c_pxa_wait_slave(struct pxa_i2c * i2c)
- Line: 506

### i2c_pxa_xfer
- Return type: static int
- Signature: i2c_pxa_xfer(struct i2c_adapter * adap,struct i2c_msg msgs[],int num)
- Line: 1145

## Structs (3)

### bits
- Line: 291
- Members:
  - ibmr: u32
  - idbr: u32
  - icr: u32
  - isr: u32
  - isar: u32
  - ilcr: u32
  - iwcr: u32
  - fm: u32
  - hs: u32
  - lock: spinlock_t
  - wait: wait_queue_head_t
  - msg: i2c_msg *
  - msg_num: unsigned int
  - msg_idx: unsigned int
  - msg_ptr: unsigned int
  - slave_addr: unsigned int
  - req_slave_addr: unsigned int
  - adap: i2c_adapter
  - clk: clk *
  - slave: i2c_client *
  - irqlogidx: unsigned int
  - isrlog: u32[32]
  - icrlog: u32[32]
  - reg_base: void __iomem *
  - reg_ibmr: void __iomem *
  - reg_idbr: void __iomem *
  - reg_icr: void __iomem *
  - reg_isr: void __iomem *
  - reg_isar: void __iomem *
  - reg_ilcr: void __iomem *
  - reg_iwcr: void __iomem *
  - iobase: unsigned long
  - iosize: unsigned long
  - irq: int
  - use_pio: unsigned int:1
  - fast_mode: unsigned int:1
  - high_mode: unsigned int:1
  - master_code: unsigned char
  - rate: unsigned long
  - highmode_enter: bool
  - fm_mask: u32
  - hs_mask: u32
  - busy_mask: u32
  - recovery: i2c_bus_recovery_info
  - pinctrl: pinctrl *
  - pinctrl_default: pinctrl_state *
  - pinctrl_recovery: pinctrl_state *
  - reset_before_xfer: bool
  - mask: u32
  - set: const char *
  - unset: const char *

### pxa_i2c
- Line: 226
- Members:
  - ibmr: u32
  - idbr: u32
  - icr: u32
  - isr: u32
  - isar: u32
  - ilcr: u32
  - iwcr: u32
  - fm: u32
  - hs: u32
  - lock: spinlock_t
  - wait: wait_queue_head_t
  - msg: i2c_msg *
  - msg_num: unsigned int
  - msg_idx: unsigned int
  - msg_ptr: unsigned int
  - slave_addr: unsigned int
  - req_slave_addr: unsigned int
  - adap: i2c_adapter
  - clk: clk *
  - slave: i2c_client *
  - irqlogidx: unsigned int
  - isrlog: u32[32]
  - icrlog: u32[32]
  - reg_base: void __iomem *
  - reg_ibmr: void __iomem *
  - reg_idbr: void __iomem *
  - reg_icr: void __iomem *
  - reg_isr: void __iomem *
  - reg_isar: void __iomem *
  - reg_ilcr: void __iomem *
  - reg_iwcr: void __iomem *
  - iobase: unsigned long
  - iosize: unsigned long
  - irq: int
  - use_pio: unsigned int:1
  - fast_mode: unsigned int:1
  - high_mode: unsigned int:1
  - master_code: unsigned char
  - rate: unsigned long
  - highmode_enter: bool
  - fm_mask: u32
  - hs_mask: u32
  - busy_mask: u32
  - recovery: i2c_bus_recovery_info
  - pinctrl: pinctrl *
  - pinctrl_default: pinctrl_state *
  - pinctrl_recovery: pinctrl_state *
  - reset_before_xfer: bool
  - mask: u32
  - set: const char *
  - unset: const char *

### pxa_reg_layout
- Line: 136
- Members:
  - ibmr: u32
  - idbr: u32
  - icr: u32
  - isr: u32
  - isar: u32
  - ilcr: u32
  - iwcr: u32
  - fm: u32
  - hs: u32
  - lock: spinlock_t
  - wait: wait_queue_head_t
  - msg: i2c_msg *
  - msg_num: unsigned int
  - msg_idx: unsigned int
  - msg_ptr: unsigned int
  - slave_addr: unsigned int
  - req_slave_addr: unsigned int
  - adap: i2c_adapter
  - clk: clk *
  - slave: i2c_client *
  - irqlogidx: unsigned int
  - isrlog: u32[32]
  - icrlog: u32[32]
  - reg_base: void __iomem *
  - reg_ibmr: void __iomem *
  - reg_idbr: void __iomem *
  - reg_icr: void __iomem *
  - reg_isr: void __iomem *
  - reg_isar: void __iomem *
  - reg_ilcr: void __iomem *
  - reg_iwcr: void __iomem *
  - iobase: unsigned long
  - iosize: unsigned long
  - irq: int
  - use_pio: unsigned int:1
  - fast_mode: unsigned int:1
  - high_mode: unsigned int:1
  - master_code: unsigned char
  - rate: unsigned long
  - highmode_enter: bool
  - fm_mask: u32
  - hs_mask: u32
  - busy_mask: u32
  - recovery: i2c_bus_recovery_info
  - pinctrl: pinctrl *
  - pinctrl_default: pinctrl_state *
  - pinctrl_recovery: pinctrl_state *
  - reset_before_xfer: bool
  - mask: u32
  - set: const char *
  - unset: const char *

## Enums (1)

### pxa_i2c_types
- Line: 148

## Variables (10)

- static **i2c_debug** : unsigned int (line 355)
- static **i2c_pxa_algorithm** : const struct i2c_algorithm (line 1164)
- static **i2c_pxa_dev_pm_ops** : const struct dev_pm_ops (line 1594)
- static **i2c_pxa_driver** : platform_driver (line 1599)
- static **i2c_pxa_dt_ids** : const struct of_device_id[] (line 207)
- static **i2c_pxa_id_table** : const struct platform_device_id[] (line 216)
- static **i2c_pxa_pio_algorithm** : const struct i2c_algorithm (line 1254)
- static **icr_bits** : const struct bits[] (line 331)
- static **isr_bits** : const struct bits[] (line 311)
- static **pxa_reg_layout** : pxa_reg_layout[] (line 157)

## Macros (72)

- **BUS_ERROR** (line 98)
- **DEF_TIMEOUT** (line 95)
- **I2C_ICR_INIT** (line 123)
- **I2C_ISR_INIT** (line 134)
- **I2C_PXA_SLAVE_ADDR** (line 287)
- **I2C_RETRY** (line 100)
- **IBMR_SCLS** (line 40)
- **IBMR_SDAS** (line 39)
- **ICR_A3700_FM** (line 59)
- **ICR_A3700_HS** (line 60)
- **ICR_ACKNAK** (line 44)
- **ICR_ALDIE** (line 54)
- **ICR_BEIE** (line 52)
- **ICR_FM** (line 57)
- **ICR_GCD** (line 49)
- **ICR_GPIOEN** (line 61)
- **ICR_HS** (line 58)
- **ICR_IRFIE** (line 51)
- **ICR_ITEIE** (line 50)
- **ICR_IUE** (line 48)
- **ICR_MA** (line 46)
- **ICR_SADIE** (line 55)
- **ICR_SCLE** (line 47)
- **ICR_SSDIE** (line 53)
- **ICR_START** (line 42)
- **ICR_STOP** (line 43)
- **ICR_TB** (line 45)
- **ICR_UR** (line 56)
- **ILCR_FLV_MASK** (line 79)
- **ILCR_FLV_SHIFT** (line 78)
- **ILCR_HLVH_MASK** (line 83)
- **ILCR_HLVH_SHIFT** (line 82)
- **ILCR_HLVL_MASK** (line 81)
- **ILCR_HLVL_SHIFT** (line 80)
- **ILCR_SLV_MASK** (line 77)
- **ILCR_SLV_SHIFT** (line 76)
- **ISR_A3700_EBB** (line 74)
- **ISR_ACKNAK** (line 64)
- **ISR_ALD** (line 68)
- **ISR_BED** (line 73)
- **ISR_GCAD** (line 71)
- **ISR_IBB** (line 66)
- **ISR_IRF** (line 70)
- **ISR_ITE** (line 69)
- **ISR_RWM** (line 63)
- **ISR_SAD** (line 72)
- **ISR_SSD** (line 67)
- **ISR_UB** (line 65)
- **IWCR_CNT_MASK** (line 86)
- **IWCR_CNT_SHIFT** (line 85)
- **IWCR_HS_CNT1_MASK** (line 88)
- **IWCR_HS_CNT1_SHIFT** (line 87)
- **IWCR_HS_CNT2_MASK** (line 90)
- **IWCR_HS_CNT2_SHIFT** (line 89)
- **NO_SLAVE** (line 97)
- **PXA_BIT**(m,s,u) (line 296)
- **VALID_INT_SOURCE** (line 1000)
- **XFER_NAKED** (line 99)
- **_IBMR**(i2c) (line 276)
- **_ICR**(i2c) (line 278)
- **_IDBR**(i2c) (line 277)
- **_ILCR**(i2c) (line 281)
- **_ISAR**(i2c) (line 280)
- **_ISR**(i2c) (line 279)
- **_IWCR**(i2c) (line 282)
- **decode_ICR**(val) (line 389)
- **decode_ISR**(val) (line 388)
- **i2c_debug** (line 385)
- **i2c_pxa_scream_blue_murder**(i2c,why) (line 390)
- **i2c_pxa_set_slave**(i2c,err) (line 570)
- **show_state**(i2c) (line 387)
- **show_state**(i2c) (line 363)
