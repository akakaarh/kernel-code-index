# drivers/i2c/busses/i2c-mpc.c

Subsystem: drivers/i2c

## Functions (27)

### fsl_i2c_bus_recovery
- Return type: static int
- Signature: fsl_i2c_bus_recovery(struct i2c_adapter * adap)
- Line: 748

### fsl_i2c_probe
- Return type: static int
- Signature: fsl_i2c_probe(struct platform_device * op)
- Line: 774

### fsl_i2c_remove
- Return type: static void
- Signature: fsl_i2c_remove(struct platform_device * op)
- Line: 876

### i2c_mpc_wait_sr
- Return type: static int
- Signature: i2c_mpc_wait_sr(struct mpc_i2c * i2c,int mask)
- Line: 146

### mpc_functionality
- Return type: static u32
- Signature: mpc_functionality(struct i2c_adapter * adap)
- Line: 742

### mpc_i2c_do_action
- Return type: static void
- Signature: mpc_i2c_do_action(struct mpc_i2c * i2c)
- Line: 496

### mpc_i2c_do_intr
- Return type: static void
- Signature: mpc_i2c_do_intr(struct mpc_i2c * i2c,u8 status)
- Line: 608

### mpc_i2c_execute_msg
- Return type: static int
- Signature: mpc_i2c_execute_msg(struct mpc_i2c * i2c)
- Line: 666

### mpc_i2c_finish
- Return type: static void
- Signature: mpc_i2c_finish(struct mpc_i2c * i2c,int rc)
- Line: 487

### mpc_i2c_fixup
- Return type: static void
- Signature: mpc_i2c_fixup(struct mpc_i2c * i2c)
- Line: 122

### mpc_i2c_fixup_A004447
- Return type: static void
- Signature: mpc_i2c_fixup_A004447(struct mpc_i2c * i2c)
- Line: 174

### mpc_i2c_get_fdr_52xx
- Return type: static int
- Signature: mpc_i2c_get_fdr_52xx(struct device_node * node,u32 clock,u32 * real_clk)
- Line: 237

### mpc_i2c_get_fdr_8xxx
- Return type: static int
- Signature: mpc_i2c_get_fdr_8xxx(struct device_node * node,u32 clock,u32 * real_clk)
- Line: 422

### mpc_i2c_get_prescaler_8xxx
- Return type: static u32
- Signature: mpc_i2c_get_prescaler_8xxx(void)
- Line: 387

### mpc_i2c_get_sec_cfg_8xxx
- Return type: static u32
- Signature: mpc_i2c_get_sec_cfg_8xxx(void)
- Line: 356

### mpc_i2c_isr
- Return type: static irqreturn_t
- Signature: mpc_i2c_isr(int irq,void * dev_id)
- Line: 637

### mpc_i2c_resume
- Return type: static int __maybe_unused
- Signature: mpc_i2c_resume(struct device * dev)
- Line: 893

### mpc_i2c_setup_512x
- Return type: static void
- Signature: mpc_i2c_setup_512x(struct device_node * node,struct mpc_i2c * i2c,u32 clock)
- Line: 302

### mpc_i2c_setup_512x
- Return type: static void
- Signature: mpc_i2c_setup_512x(struct device_node * node,struct mpc_i2c * i2c,u32 clock)
- Line: 328

### mpc_i2c_setup_52xx
- Return type: static void
- Signature: mpc_i2c_setup_52xx(struct device_node * node,struct mpc_i2c * i2c,u32 clock)
- Line: 272

### mpc_i2c_setup_52xx
- Return type: static void
- Signature: mpc_i2c_setup_52xx(struct device_node * node,struct mpc_i2c * i2c,u32 clock)
- Line: 294

### mpc_i2c_setup_8xxx
- Return type: static void
- Signature: mpc_i2c_setup_8xxx(struct device_node * node,struct mpc_i2c * i2c,u32 clock)
- Line: 455

### mpc_i2c_setup_8xxx
- Return type: static void
- Signature: mpc_i2c_setup_8xxx(struct device_node * node,struct mpc_i2c * i2c,u32 clock)
- Line: 480

### mpc_i2c_suspend
- Return type: static int __maybe_unused
- Signature: mpc_i2c_suspend(struct device * dev)
- Line: 883

### mpc_i2c_wait_for_completion
- Return type: static int
- Signature: mpc_i2c_wait_for_completion(struct mpc_i2c * i2c)
- Line: 653

### mpc_xfer
- Return type: static int
- Signature: mpc_xfer(struct i2c_adapter * adap,struct i2c_msg * msgs,int num)
- Line: 715

### writeccr
- Return type: static void
- Signature: writeccr(struct mpc_i2c * i2c,u32 x)
- Line: 112

## Structs (3)

### mpc_i2c
- Line: 81
- Members:
  - dev: device *
  - base: void __iomem *
  - interrupt: u32
  - waitq: wait_queue_head_t
  - lock: spinlock_t
  - adap: i2c_adapter
  - irq: int
  - real_clk: u32
  - dfsrr: u8
  - fdr: u8
  - cntl_bits: u32
  - action: mpc_i2c_action
  - msgs: i2c_msg *
  - num_msgs: int
  - curr_msg: int
  - byte_posn: u32
  - block: u32
  - rc: int
  - expect_rxack: int
  - has_errata_A004447: bool
  - divider: u16
  - fdr: u16
  - setup: void (*)(struct device_node * node,struct mpc_i2c * i2c,u32 clock)

### mpc_i2c_data
- Line: 108
- Members:
  - dev: device *
  - base: void __iomem *
  - interrupt: u32
  - waitq: wait_queue_head_t
  - lock: spinlock_t
  - adap: i2c_adapter
  - irq: int
  - real_clk: u32
  - dfsrr: u8
  - fdr: u8
  - cntl_bits: u32
  - action: mpc_i2c_action
  - msgs: i2c_msg *
  - num_msgs: int
  - curr_msg: int
  - byte_posn: u32
  - block: u32
  - rc: int
  - expect_rxack: int
  - has_errata_A004447: bool
  - divider: u16
  - fdr: u16
  - setup: void (*)(struct device_node * node,struct mpc_i2c * i2c,u32 clock)

### mpc_i2c_divider
- Line: 103
- Members:
  - dev: device *
  - base: void __iomem *
  - interrupt: u32
  - waitq: wait_queue_head_t
  - lock: spinlock_t
  - adap: i2c_adapter
  - irq: int
  - real_clk: u32
  - dfsrr: u8
  - fdr: u8
  - cntl_bits: u32
  - action: mpc_i2c_action
  - msgs: i2c_msg *
  - num_msgs: int
  - curr_msg: int
  - byte_posn: u32
  - block: u32
  - rc: int
  - expect_rxack: int
  - has_errata_A004447: bool
  - divider: u16
  - fdr: u16
  - setup: void (*)(struct device_node * node,struct mpc_i2c * i2c,u32 clock)

## Enums (1)

### mpc_i2c_action
- Line: 58

## Variables (13)

- static **action_str** : const char * const[] (line 69)
- static **fsl_i2c_recovery_info** : i2c_bus_recovery_info (line 770)
- static **mpc_algo** : const struct i2c_algorithm (line 760)
- static **mpc_i2c_data_512x** : const struct mpc_i2c_data (line 904)
- static **mpc_i2c_data_52xx** : const struct mpc_i2c_data (line 908)
- static **mpc_i2c_data_8313** : const struct mpc_i2c_data (line 912)
- static **mpc_i2c_data_8543** : const struct mpc_i2c_data (line 916)
- static **mpc_i2c_data_8544** : const struct mpc_i2c_data (line 920)
- static **mpc_i2c_dividers_52xx** : const struct mpc_i2c_divider[] (line 216)
- static **mpc_i2c_dividers_8xxx** : const struct mpc_i2c_divider[] (line 336)
- static **mpc_i2c_driver** : platform_driver (line 939)
- static **mpc_i2c_of_match** : const struct of_device_id[] (line 924)
- static **mpc_ops** : i2c_adapter (line 765)

## Macros (21)

- **CCR_MEN** (line 42)
- **CCR_MIEN** (line 43)
- **CCR_MSTA** (line 44)
- **CCR_MTX** (line 45)
- **CCR_RSTA** (line 47)
- **CCR_RSVD** (line 48)
- **CCR_TXAK** (line 46)
- **CSR_MAAS** (line 51)
- **CSR_MAL** (line 53)
- **CSR_MBB** (line 52)
- **CSR_MCF** (line 50)
- **CSR_MIF** (line 55)
- **CSR_RXAK** (line 56)
- **CSR_SRW** (line 54)
- **MPC_I2C_CLOCK_LEGACY** (line 33)
- **MPC_I2C_CLOCK_PRESERVE** (line 34)
- **MPC_I2C_CR** (line 37)
- **MPC_I2C_DFSRR** (line 40)
- **MPC_I2C_DR** (line 39)
- **MPC_I2C_FDR** (line 36)
- **MPC_I2C_SR** (line 38)
