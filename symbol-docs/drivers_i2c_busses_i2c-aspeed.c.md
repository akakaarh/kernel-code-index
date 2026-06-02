# drivers/i2c/busses/i2c-aspeed.c

Subsystem: drivers/i2c

## Functions (21)

### __aspeed_i2c_reg_slave
- Return type: static void
- Signature: __aspeed_i2c_reg_slave(struct aspeed_i2c_bus * bus,u16 slave_addr)
- Line: 751

### aspeed_i2c_24xx_get_clk_reg_val
- Return type: static u32
- Signature: aspeed_i2c_24xx_get_clk_reg_val(struct device * dev,u32 divisor)
- Line: 892

### aspeed_i2c_25xx_get_clk_reg_val
- Return type: static u32
- Signature: aspeed_i2c_25xx_get_clk_reg_val(struct device * dev,u32 divisor)
- Line: 901

### aspeed_i2c_bus_irq
- Return type: static irqreturn_t
- Signature: aspeed_i2c_bus_irq(int irq,void * dev_id)
- Line: 619

### aspeed_i2c_do_start
- Return type: static void
- Signature: aspeed_i2c_do_start(struct aspeed_i2c_bus * bus)
- Line: 368

### aspeed_i2c_do_stop
- Return type: static void
- Signature: aspeed_i2c_do_stop(struct aspeed_i2c_bus * bus)
- Line: 174

### aspeed_i2c_functionality
- Return type: static u32
- Signature: aspeed_i2c_functionality(struct i2c_adapter * adap)
- Line: 744

### aspeed_i2c_get_clk_reg_val
- Return type: static u32
- Signature: aspeed_i2c_get_clk_reg_val(struct device * dev,u32 clk_high_low_mask,u32 divisor)
- Line: 825

### aspeed_i2c_init
- Return type: static int
- Signature: aspeed_i2c_init(struct aspeed_i2c_bus * bus,struct platform_device * pdev)
- Line: 928

### aspeed_i2c_init_clk
- Return type: static int
- Signature: aspeed_i2c_init_clk(struct aspeed_i2c_bus * bus)
- Line: 911

### aspeed_i2c_is_irq_error
- Return type: static int
- Signature: aspeed_i2c_is_irq_error(u32 irq_status)
- Line: 411

### aspeed_i2c_master_irq
- Return type: static u32
- Signature: aspeed_i2c_master_irq(struct aspeed_i2c_bus * bus,u32 irq_status)
- Line: 424

### aspeed_i2c_master_xfer
- Return type: static int
- Signature: aspeed_i2c_master_xfer(struct i2c_adapter * adap,struct i2c_msg * msgs,int num)
- Line: 682

### aspeed_i2c_next_msg_or_stop
- Return type: static void
- Signature: aspeed_i2c_next_msg_or_stop(struct aspeed_i2c_bus * bus)
- Line: 401

### aspeed_i2c_probe_bus
- Return type: static int
- Signature: aspeed_i2c_probe_bus(struct platform_device * pdev)
- Line: 998

### aspeed_i2c_recover_bus
- Return type: static int
- Signature: aspeed_i2c_recover_bus(struct aspeed_i2c_bus * bus)
- Line: 180

### aspeed_i2c_reg_slave
- Return type: static int
- Signature: aspeed_i2c_reg_slave(struct i2c_client * client)
- Line: 773

### aspeed_i2c_remove_bus
- Return type: static void
- Signature: aspeed_i2c_remove_bus(struct platform_device * pdev)
- Line: 1085

### aspeed_i2c_reset
- Return type: static int
- Signature: aspeed_i2c_reset(struct aspeed_i2c_bus * bus)
- Line: 962

### aspeed_i2c_slave_irq
- Return type: static u32
- Signature: aspeed_i2c_slave_irq(struct aspeed_i2c_bus * bus,u32 irq_status)
- Line: 249

### aspeed_i2c_unreg_slave
- Return type: static int
- Signature: aspeed_i2c_unreg_slave(struct i2c_client * client)
- Line: 792

## Structs (1)

### aspeed_i2c_bus
- Line: 141
- Members:
  - adap: i2c_adapter
  - dev: device *
  - base: void __iomem *
  - rst: reset_control *
  - lock: spinlock_t
  - cmd_complete: completion
  - get_clk_reg_val: u32 (*)(struct device * dev,u32 divisor)
  - parent_clk_frequency: unsigned long
  - bus_frequency: u32
  - master_state: aspeed_i2c_master_state
  - msgs: i2c_msg *
  - buf_index: size_t
  - msgs_index: size_t
  - msgs_count: size_t
  - send_stop: bool
  - cmd_err: int
  - master_xfer_result: int
  - multi_master: bool
  - slave: i2c_client *
  - slave_state: aspeed_i2c_slave_state

## Enums (2)

### aspeed_i2c_master_state
- Line: 120

### aspeed_i2c_slave_state
- Line: 131

## Variables (3)

- static **aspeed_i2c_algo** : const struct i2c_algorithm (line 816)
- static **aspeed_i2c_bus_driver** : platform_driver (line 1103)
- static **aspeed_i2c_bus_of_table** : const struct of_device_id[] (line 981)

## Macros (49)

- **ASPEED_I2CD_BUS_BUSY_STS** (line 100)
- **ASPEED_I2CD_BUS_RECOVER_CMD** (line 101)
- **ASPEED_I2CD_DEV_ADDR_MASK** (line 118)
- **ASPEED_I2CD_INTR_ABNORMAL** (line 75)
- **ASPEED_I2CD_INTR_ALL** (line 86)
- **ASPEED_I2CD_INTR_ARBIT_LOSS** (line 77)
- **ASPEED_I2CD_INTR_BUS_RECOVER_DONE** (line 72)
- **ASPEED_I2CD_INTR_MASTER_ERRORS** (line 81)
- **ASPEED_I2CD_INTR_NORMAL_STOP** (line 76)
- **ASPEED_I2CD_INTR_RECV_MASK** (line 70)
- **ASPEED_I2CD_INTR_RX_DONE** (line 78)
- **ASPEED_I2CD_INTR_SCL_TIMEOUT** (line 74)
- **ASPEED_I2CD_INTR_SDA_DL_TIMEOUT** (line 71)
- **ASPEED_I2CD_INTR_SLAVE_MATCH** (line 73)
- **ASPEED_I2CD_INTR_TX_ACK** (line 80)
- **ASPEED_I2CD_INTR_TX_NAK** (line 79)
- **ASPEED_I2CD_MASTER_CMDS_MASK** (line 110)
- **ASPEED_I2CD_MASTER_EN** (line 49)
- **ASPEED_I2CD_MULTI_MASTER_DIS** (line 44)
- **ASPEED_I2CD_M_HIGH_SPEED_EN** (line 47)
- **ASPEED_I2CD_M_RX_CMD** (line 106)
- **ASPEED_I2CD_M_SDA_DRIVE_1T_EN** (line 46)
- **ASPEED_I2CD_M_START_CMD** (line 109)
- **ASPEED_I2CD_M_STOP_CMD** (line 104)
- **ASPEED_I2CD_M_S_RX_CMD_LAST** (line 105)
- **ASPEED_I2CD_M_TX_CMD** (line 108)
- **ASPEED_I2CD_SCL_LINE_STS** (line 98)
- **ASPEED_I2CD_SDA_DRIVE_1T_EN** (line 45)
- **ASPEED_I2CD_SDA_LINE_STS** (line 99)
- **ASPEED_I2CD_SLAVE_EN** (line 48)
- **ASPEED_I2CD_S_TX_CMD** (line 107)
- **ASPEED_I2CD_TIME_BASE_DIVISOR_MASK** (line 59)
- **ASPEED_I2CD_TIME_SCL_HIGH_MASK** (line 56)
- **ASPEED_I2CD_TIME_SCL_HIGH_SHIFT** (line 55)
- **ASPEED_I2CD_TIME_SCL_LOW_MASK** (line 58)
- **ASPEED_I2CD_TIME_SCL_LOW_SHIFT** (line 57)
- **ASPEED_I2CD_TIME_SCL_REG_MAX** (line 60)
- **ASPEED_I2CD_TIME_TACST_MASK** (line 54)
- **ASPEED_I2CD_TIME_TBUF_MASK** (line 52)
- **ASPEED_I2CD_TIME_THDSTA_MASK** (line 53)
- **ASPEED_I2C_AC_TIMING_REG1** (line 30)
- **ASPEED_I2C_AC_TIMING_REG2** (line 31)
- **ASPEED_I2C_BYTE_BUF_REG** (line 36)
- **ASPEED_I2C_CMD_REG** (line 34)
- **ASPEED_I2C_DEV_ADDR_REG** (line 35)
- **ASPEED_I2C_FUN_CTRL_REG** (line 29)
- **ASPEED_I2C_INTR_CTRL_REG** (line 32)
- **ASPEED_I2C_INTR_STS_REG** (line 33)
- **ASPEED_NO_TIMEOUT_CTRL** (line 62)
