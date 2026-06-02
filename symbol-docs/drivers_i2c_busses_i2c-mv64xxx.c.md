# drivers/i2c/busses/i2c-mv64xxx.c

Subsystem: drivers/i2c

## Functions (28)

### mv64xxx_calc_freq
- Return type: static int
- Signature: mv64xxx_calc_freq(struct mv64xxx_i2c_data * drv_data,const int tclk,const int n,const int m)
- Line: 817

### mv64xxx_find_baud_factors
- Return type: static bool
- Signature: mv64xxx_find_baud_factors(struct mv64xxx_i2c_data * drv_data,const u32 req_freq,const u32 tclk)
- Line: 827

### mv64xxx_i2c_can_offload
- Return type: static bool
- Signature: mv64xxx_i2c_can_offload(struct mv64xxx_i2c_data * drv_data)
- Line: 700

### mv64xxx_i2c_do_action
- Return type: static void
- Signature: mv64xxx_i2c_do_action(struct mv64xxx_i2c_data * drv_data)
- Line: 351

### mv64xxx_i2c_execute_msg
- Return type: static int
- Signature: mv64xxx_i2c_execute_msg(struct mv64xxx_i2c_data * drv_data,struct i2c_msg * msg,int is_last)
- Line: 600

### mv64xxx_i2c_fsm
- Return type: static void
- Signature: mv64xxx_i2c_fsm(struct mv64xxx_i2c_data * drv_data,u32 status)
- Line: 229

### mv64xxx_i2c_functionality
- Return type: static u32
- Signature: mv64xxx_i2c_functionality(struct i2c_adapter * adap)
- Line: 739

### mv64xxx_i2c_hw_init
- Return type: static void
- Signature: mv64xxx_i2c_hw_init(struct mv64xxx_i2c_data * drv_data)
- Line: 203

### mv64xxx_i2c_init_recovery_info
- Return type: static int
- Signature: mv64xxx_i2c_init_recovery_info(struct mv64xxx_i2c_data * drv_data,struct device * dev)
- Line: 931

### mv64xxx_i2c_intr
- Return type: static irqreturn_t
- Signature: mv64xxx_i2c_intr(int irq,void * dev_id)
- Line: 503

### mv64xxx_i2c_intr_offload
- Return type: static int
- Signature: mv64xxx_i2c_intr_offload(struct mv64xxx_i2c_data * drv_data)
- Line: 451

### mv64xxx_i2c_offload_xfer
- Return type: static int
- Signature: mv64xxx_i2c_offload_xfer(struct mv64xxx_i2c_data * drv_data)
- Line: 635

### mv64xxx_i2c_prepare_for_io
- Return type: static void
- Signature: mv64xxx_i2c_prepare_for_io(struct mv64xxx_i2c_data * drv_data,struct i2c_msg * msg)
- Line: 175

### mv64xxx_i2c_prepare_tx
- Return type: static void
- Signature: mv64xxx_i2c_prepare_tx(struct mv64xxx_i2c_data * drv_data)
- Line: 623

### mv64xxx_i2c_probe
- Return type: static int
- Signature: mv64xxx_i2c_probe(struct platform_device * pd)
- Line: 977

### mv64xxx_i2c_read_offload_rx_data
- Return type: static void
- Signature: mv64xxx_i2c_read_offload_rx_data(struct mv64xxx_i2c_data * drv_data,struct i2c_msg * msg)
- Line: 439

### mv64xxx_i2c_remove
- Return type: static void
- Signature: mv64xxx_i2c_remove(struct platform_device * pd)
- Line: 1080

### mv64xxx_i2c_runtime_resume
- Return type: static int
- Signature: mv64xxx_i2c_runtime_resume(struct device * dev)
- Line: 963

### mv64xxx_i2c_runtime_suspend
- Return type: static int
- Signature: mv64xxx_i2c_runtime_suspend(struct device * dev)
- Line: 951

### mv64xxx_i2c_send_start
- Return type: static void
- Signature: mv64xxx_i2c_send_start(struct mv64xxx_i2c_data * drv_data)
- Line: 337

### mv64xxx_i2c_valid_offload_sz
- Return type: static bool
- Signature: mv64xxx_i2c_valid_offload_sz(struct i2c_msg * msg)
- Line: 694

### mv64xxx_i2c_wait_for_completion
- Return type: static void
- Signature: mv64xxx_i2c_wait_for_completion(struct mv64xxx_i2c_data * drv_data)
- Line: 550

### mv64xxx_i2c_wait_polling
- Return type: static void
- Signature: mv64xxx_i2c_wait_polling(struct mv64xxx_i2c_data * drv_data)
- Line: 588

### mv64xxx_i2c_xfer
- Return type: static int
- Signature: mv64xxx_i2c_xfer(struct i2c_adapter * adap,struct i2c_msg msgs[],int num)
- Line: 775

### mv64xxx_i2c_xfer_atomic
- Return type: static int
- Signature: mv64xxx_i2c_xfer_atomic(struct i2c_adapter * adap,struct i2c_msg msgs[],int num)
- Line: 783

### mv64xxx_i2c_xfer_core
- Return type: static int
- Signature: mv64xxx_i2c_xfer_core(struct i2c_adapter * adap,struct i2c_msg msgs[],int num)
- Line: 745

### mv64xxx_of_config
- Return type: static int
- Signature: mv64xxx_of_config(struct mv64xxx_i2c_data * drv_data,struct device * dev)
- Line: 851

### mv64xxx_of_config
- Return type: static int
- Signature: mv64xxx_of_config(struct mv64xxx_i2c_data * drv_data,struct device * dev)
- Line: 924

## Structs (2)

### mv64xxx_i2c_data
- Line: 118
- Members:
  - addr: u8
  - ext_addr: u8
  - data: u8
  - control: u8
  - status: u8
  - clock: u8
  - soft_reset: u8
  - msgs: i2c_msg *
  - num_msgs: int
  - irq: int
  - state: u32
  - action: u32
  - aborting: u32
  - cntl_bits: u32
  - reg_base: void __iomem *
  - reg_offsets: mv64xxx_i2c_regs
  - addr1: u32
  - addr2: u32
  - bytes_left: u32
  - byte_posn: u32
  - send_stop: u32
  - block: u32
  - rc: int
  - freq_m: u32
  - freq_n: u32
  - clk: clk *
  - reg_clk: clk *
  - waitq: wait_queue_head_t
  - lock: spinlock_t
  - msg: i2c_msg *
  - adapter: i2c_adapter
  - offload_enabled: bool
  - errata_delay: bool
  - rstc: reset_control *
  - irq_clear_inverted: bool
  - clk_n_base_0: bool
  - rinfo: i2c_bus_recovery_info
  - atomic: bool

### mv64xxx_i2c_regs
- Line: 108
- Members:
  - addr: u8
  - ext_addr: u8
  - data: u8
  - control: u8
  - status: u8
  - clock: u8
  - soft_reset: u8
  - msgs: i2c_msg *
  - num_msgs: int
  - irq: int
  - state: u32
  - action: u32
  - aborting: u32
  - cntl_bits: u32
  - reg_base: void __iomem *
  - reg_offsets: mv64xxx_i2c_regs
  - addr1: u32
  - addr2: u32
  - bytes_left: u32
  - byte_posn: u32
  - send_stop: u32
  - block: u32
  - rc: int
  - freq_m: u32
  - freq_n: u32
  - clk: clk *
  - reg_clk: clk *
  - waitq: wait_queue_head_t
  - lock: spinlock_t
  - msg: i2c_msg *
  - adapter: i2c_adapter
  - offload_enabled: bool
  - errata_delay: bool
  - rstc: reset_control *
  - irq_clear_inverted: bool
  - clk_n_base_0: bool
  - rinfo: i2c_bus_recovery_info
  - atomic: bool

## Enums (2)

### __anonea29f2ff0103
- Line: 84

### __anonea29f2ff0203
- Line: 96

## Variables (6)

- static **mv64xxx_i2c_algo** : const struct i2c_algorithm (line 792)
- static **mv64xxx_i2c_driver** : platform_driver (line 1098)
- static **mv64xxx_i2c_of_match_table** : const struct of_device_id[] (line 805)
- static **mv64xxx_i2c_pm_ops** : const struct dev_pm_ops (line 1091)
- static **mv64xxx_i2c_regs_mv64xxx** : mv64xxx_i2c_regs (line 154)
- static **mv64xxx_i2c_regs_sun4i** : mv64xxx_i2c_regs (line 164)

## Macros (43)

- **MV64XXX_I2C_BAUD_DIV_M**(val) (line 31)
- **MV64XXX_I2C_BAUD_DIV_N**(val) (line 30)
- **MV64XXX_I2C_BRIDGE_CONTROL_ADDR_EXT** (line 74)
- **MV64XXX_I2C_BRIDGE_CONTROL_ADDR_SHIFT** (line 73)
- **MV64XXX_I2C_BRIDGE_CONTROL_ENABLE** (line 77)
- **MV64XXX_I2C_BRIDGE_CONTROL_RD** (line 72)
- **MV64XXX_I2C_BRIDGE_CONTROL_REPEATED_START** (line 78)
- **MV64XXX_I2C_BRIDGE_CONTROL_RX_SIZE_SHIFT** (line 76)
- **MV64XXX_I2C_BRIDGE_CONTROL_TX_SIZE_SHIFT** (line 75)
- **MV64XXX_I2C_BRIDGE_CONTROL_WR** (line 71)
- **MV64XXX_I2C_BRIDGE_STATUS_ERROR** (line 81)
- **MV64XXX_I2C_REG_BRIDGE_CONTROL** (line 64)
- **MV64XXX_I2C_REG_BRIDGE_INTR_CAUSE** (line 66)
- **MV64XXX_I2C_REG_BRIDGE_INTR_MASK** (line 67)
- **MV64XXX_I2C_REG_BRIDGE_STATUS** (line 65)
- **MV64XXX_I2C_REG_BRIDGE_TIMING** (line 68)
- **MV64XXX_I2C_REG_CONTROL_ACK** (line 33)
- **MV64XXX_I2C_REG_CONTROL_IFLG** (line 34)
- **MV64XXX_I2C_REG_CONTROL_INTEN** (line 38)
- **MV64XXX_I2C_REG_CONTROL_START** (line 36)
- **MV64XXX_I2C_REG_CONTROL_STOP** (line 35)
- **MV64XXX_I2C_REG_CONTROL_TWSIEN** (line 37)
- **MV64XXX_I2C_REG_RX_DATA_HI** (line 63)
- **MV64XXX_I2C_REG_RX_DATA_LO** (line 62)
- **MV64XXX_I2C_REG_TX_DATA_HI** (line 61)
- **MV64XXX_I2C_REG_TX_DATA_LO** (line 60)
- **MV64XXX_I2C_STATUS_BUS_ERR** (line 41)
- **MV64XXX_I2C_STATUS_MAST_LOST_ARB** (line 48)
- **MV64XXX_I2C_STATUS_MAST_RD_ADDR_2_ACK** (line 55)
- **MV64XXX_I2C_STATUS_MAST_RD_ADDR_2_NO_ACK** (line 56)
- **MV64XXX_I2C_STATUS_MAST_RD_ADDR_ACK** (line 49)
- **MV64XXX_I2C_STATUS_MAST_RD_ADDR_NO_ACK** (line 50)
- **MV64XXX_I2C_STATUS_MAST_RD_DATA_ACK** (line 51)
- **MV64XXX_I2C_STATUS_MAST_RD_DATA_NO_ACK** (line 52)
- **MV64XXX_I2C_STATUS_MAST_REPEAT_START** (line 43)
- **MV64XXX_I2C_STATUS_MAST_START** (line 42)
- **MV64XXX_I2C_STATUS_MAST_WR_ACK** (line 46)
- **MV64XXX_I2C_STATUS_MAST_WR_ADDR_2_ACK** (line 53)
- **MV64XXX_I2C_STATUS_MAST_WR_ADDR_2_NO_ACK** (line 54)
- **MV64XXX_I2C_STATUS_MAST_WR_ADDR_ACK** (line 44)
- **MV64XXX_I2C_STATUS_MAST_WR_ADDR_NO_ACK** (line 45)
- **MV64XXX_I2C_STATUS_MAST_WR_NO_ACK** (line 47)
- **MV64XXX_I2C_STATUS_NO_STATUS** (line 57)
