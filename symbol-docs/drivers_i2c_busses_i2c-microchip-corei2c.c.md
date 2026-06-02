# drivers/i2c/busses/i2c-microchip-corei2c.c

Subsystem: drivers/i2c

## Functions (16)

### mchp_corei2c_core_disable
- Return type: static void
- Signature: mchp_corei2c_core_disable(struct mchp_corei2c_dev * idev)
- Line: 129

### mchp_corei2c_core_enable
- Return type: static void
- Signature: mchp_corei2c_core_enable(struct mchp_corei2c_dev * idev)
- Line: 137

### mchp_corei2c_empty_rx
- Return type: static void
- Signature: mchp_corei2c_empty_rx(struct mchp_corei2c_dev * idev)
- Line: 210

### mchp_corei2c_fill_tx
- Return type: static int
- Signature: mchp_corei2c_fill_tx(struct mchp_corei2c_dev * idev)
- Line: 226

### mchp_corei2c_func
- Return type: static u32
- Signature: mchp_corei2c_func(struct i2c_adapter * adap)
- Line: 424

### mchp_corei2c_handle_isr
- Return type: static irqreturn_t
- Signature: mchp_corei2c_handle_isr(struct mchp_corei2c_dev * idev)
- Line: 276

### mchp_corei2c_init
- Return type: static int
- Signature: mchp_corei2c_init(struct mchp_corei2c_dev * idev)
- Line: 195

### mchp_corei2c_isr
- Return type: static irqreturn_t
- Signature: mchp_corei2c_isr(int irq,void * _dev)
- Line: 348

### mchp_corei2c_next_msg
- Return type: static void
- Signature: mchp_corei2c_next_msg(struct mchp_corei2c_dev * idev)
- Line: 235

### mchp_corei2c_probe
- Return type: static int
- Signature: mchp_corei2c_probe(struct platform_device * pdev)
- Line: 538

### mchp_corei2c_remove
- Return type: static void
- Signature: mchp_corei2c_remove(struct platform_device * pdev)
- Line: 620

### mchp_corei2c_reset
- Return type: static void
- Signature: mchp_corei2c_reset(struct mchp_corei2c_dev * idev)
- Line: 145

### mchp_corei2c_set_divisor
- Return type: static int
- Signature: mchp_corei2c_set_divisor(u32 rate,struct mchp_corei2c_dev * idev)
- Line: 159

### mchp_corei2c_smbus_xfer
- Return type: static int
- Signature: mchp_corei2c_smbus_xfer(struct i2c_adapter * adap,u16 addr,unsigned short flags,char read_write,u8 command,int size,union i2c_smbus_data * data)
- Line: 429

### mchp_corei2c_stop
- Return type: static void
- Signature: mchp_corei2c_stop(struct mchp_corei2c_dev * idev)
- Line: 151

### mchp_corei2c_xfer
- Return type: static int
- Signature: mchp_corei2c_xfer(struct i2c_adapter * adap,struct i2c_msg * msgs,int num)
- Line: 367

## Structs (1)

### mchp_corei2c_dev
- Line: 111
- Members:
  - base: void __iomem *
  - dev: device *
  - i2c_clk: clk *
  - msg_queue: i2c_msg *
  - buf: u8 *
  - msg_complete: completion
  - adapter: i2c_adapter
  - msg_err: int
  - total_num: int
  - current_num: int
  - bus_clk_rate: u32
  - isr_status: u32
  - msg_len: u16
  - addr: u8
  - restart_needed: bool

## Variables (3)

- static **mchp_corei2c_algo** : const struct i2c_algorithm (line 532)
- static **mchp_corei2c_driver** : platform_driver (line 635)
- static **mchp_corei2c_of_match** : const struct of_device_id[] (line 628)

## Macros (68)

- **BCLK_DIV_8** (line 89)
- **CLK_MASK** (line 90)
- **CORE_I2C_CTRL** (line 20)
- **CORE_I2C_DATA** (line 61)
- **CORE_I2C_FREQ** (line 76)
- **CORE_I2C_GLITCHREG** (line 77)
- **CORE_I2C_SLAVE0_ADDR** (line 65)
- **CORE_I2C_SLAVE1_ADDR** (line 78)
- **CORE_I2C_SMBUS** (line 67)
- **CORE_I2C_SMBUS_MSG_RD** (line 80)
- **CORE_I2C_SMBUS_MSG_WR** (line 79)
- **CORE_I2C_STATUS** (line 60)
- **CTRL_AA** (line 23)
- **CTRL_CR0** (line 21)
- **CTRL_CR1** (line 22)
- **CTRL_CR2** (line 28)
- **CTRL_ENS1** (line 27)
- **CTRL_SI** (line 24)
- **CTRL_STA** (line 26)
- **CTRL_STO** (line 25)
- **GENERAL_CALL_BIT** (line 66)
- **PCLK_DIV_120** (line 87)
- **PCLK_DIV_160** (line 86)
- **PCLK_DIV_192** (line 85)
- **PCLK_DIV_224** (line 84)
- **PCLK_DIV_256** (line 83)
- **PCLK_DIV_60** (line 88)
- **PCLK_DIV_960** (line 82)
- **READ_BIT** (line 63)
- **SLAVE_ADDR_SHIFT** (line 64)
- **SMBALERT_INT_ENB** (line 68)
- **SMBALERT_NI_STATUS** (line 71)
- **SMBALERT_NO_CTRL** (line 72)
- **SMBSUS_INT_ENB** (line 69)
- **SMBSUS_NI_STATUS** (line 73)
- **SMBSUS_NO_CTRL** (line 74)
- **SMBUS_ENB** (line 70)
- **SMBUS_RESET** (line 75)
- **STATUS_BUS_ERROR** (line 30)
- **STATUS_LAST_DATA_ACK** (line 55)
- **STATUS_M_ARB_LOST** (line 37)
- **STATUS_M_REPEATED_START_SENT** (line 32)
- **STATUS_M_RX_DATA_ACKED** (line 40)
- **STATUS_M_RX_DATA_NACKED** (line 41)
- **STATUS_M_SLAR_ACK** (line 38)
- **STATUS_M_SLAR_NACK** (line 39)
- **STATUS_M_SLAW_ACK** (line 33)
- **STATUS_M_SLAW_NACK** (line 34)
- **STATUS_M_SMB_MASTER_RESET** (line 56)
- **STATUS_M_START_SENT** (line 31)
- **STATUS_M_TX_DATA_ACK** (line 35)
- **STATUS_M_TX_DATA_NACK** (line 36)
- **STATUS_NO_STATE_INFO** (line 58)
- **STATUS_S_ARB_LOST_GENERAL_CALL_ACKED** (line 45)
- **STATUS_S_ARB_LOST_SLAR_ACKED** (line 52)
- **STATUS_S_ARB_LOST_SLAW_ACKED** (line 43)
- **STATUS_S_GENERAL_CALL_ACKED** (line 44)
- **STATUS_S_GENERAL_CALL_RX_DATA_ACKED** (line 48)
- **STATUS_S_GENERAL_CALL_RX_DATA_NACKED** (line 49)
- **STATUS_S_RX_DATA_ACKED** (line 46)
- **STATUS_S_RX_DATA_NACKED** (line 47)
- **STATUS_S_RX_STOP** (line 50)
- **STATUS_S_SCL_LOW_TIMEOUT** (line 57)
- **STATUS_S_SLAR_ACKED** (line 51)
- **STATUS_S_SLAW_ACKED** (line 42)
- **STATUS_S_TX_DATA_ACK** (line 53)
- **STATUS_S_TX_DATA_NACK** (line 54)
- **WRITE_BIT** (line 62)
