# drivers/i2c/busses/i2c-bcm-kona.c

Subsystem: drivers/i2c

## Functions (22)

### bcm_kona_i2c_assign_bus_speed
- Return type: static int
- Signature: bcm_kona_i2c_assign_bus_speed(struct bcm_kona_i2c_dev * dev)
- Line: 703

### bcm_kona_i2c_config_timing
- Return type: static void
- Signature: bcm_kona_i2c_config_timing(struct bcm_kona_i2c_dev * dev)
- Line: 509

### bcm_kona_i2c_config_timing_hs
- Return type: static void
- Signature: bcm_kona_i2c_config_timing_hs(struct bcm_kona_i2c_dev * dev)
- Line: 526

### bcm_kona_i2c_disable_clock
- Return type: static void
- Signature: bcm_kona_i2c_disable_clock(struct bcm_kona_i2c_dev * dev)
- Line: 202

### bcm_kona_i2c_do_addr
- Return type: static int
- Signature: bcm_kona_i2c_do_addr(struct bcm_kona_i2c_dev * dev,struct i2c_msg * msg)
- Line: 467

### bcm_kona_i2c_enable_autosense
- Return type: static void
- Signature: bcm_kona_i2c_enable_autosense(struct bcm_kona_i2c_dev * dev)
- Line: 503

### bcm_kona_i2c_enable_clock
- Return type: static void
- Signature: bcm_kona_i2c_enable_clock(struct bcm_kona_i2c_dev * dev)
- Line: 196

### bcm_kona_i2c_functionality
- Return type: static uint32_t
- Signature: bcm_kona_i2c_functionality(struct i2c_adapter * adap)
- Line: 692

### bcm_kona_i2c_isr
- Return type: static irqreturn_t
- Signature: bcm_kona_i2c_isr(int irq,void * devid)
- Line: 208

### bcm_kona_i2c_probe
- Return type: static int
- Signature: bcm_kona_i2c_probe(struct platform_device * pdev)
- Line: 737

### bcm_kona_i2c_read_fifo
- Return type: static int
- Signature: bcm_kona_i2c_read_fifo(struct bcm_kona_i2c_dev * dev,struct i2c_msg * msg)
- Line: 316

### bcm_kona_i2c_read_fifo_single
- Return type: static int
- Signature: bcm_kona_i2c_read_fifo_single(struct bcm_kona_i2c_dev * dev,uint8_t * buf,unsigned int len,unsigned int last_byte_nak)
- Line: 280

### bcm_kona_i2c_remove
- Return type: static void
- Signature: bcm_kona_i2c_remove(struct platform_device * pdev)
- Line: 861

### bcm_kona_i2c_send_cmd_to_ctrl
- Return type: static void
- Signature: bcm_kona_i2c_send_cmd_to_ctrl(struct bcm_kona_i2c_dev * dev,enum bcm_kona_cmd_t cmd)
- Line: 159

### bcm_kona_i2c_switch_to_hs
- Return type: static int
- Signature: bcm_kona_i2c_switch_to_hs(struct bcm_kona_i2c_dev * dev)
- Line: 543

### bcm_kona_i2c_switch_to_std
- Return type: static int
- Signature: bcm_kona_i2c_switch_to_std(struct bcm_kona_i2c_dev * dev)
- Line: 573

### bcm_kona_i2c_wait_if_busy
- Return type: static int
- Signature: bcm_kona_i2c_wait_if_busy(struct bcm_kona_i2c_dev * dev)
- Line: 228

### bcm_kona_i2c_write_byte
- Return type: static int
- Signature: bcm_kona_i2c_write_byte(struct bcm_kona_i2c_dev * dev,uint8_t data,unsigned int nak_expected)
- Line: 345

### bcm_kona_i2c_write_fifo
- Return type: static int
- Signature: bcm_kona_i2c_write_fifo(struct bcm_kona_i2c_dev * dev,struct i2c_msg * msg)
- Line: 441

### bcm_kona_i2c_write_fifo_single
- Return type: static int
- Signature: bcm_kona_i2c_write_fifo_single(struct bcm_kona_i2c_dev * dev,uint8_t * buf,unsigned int len)
- Line: 391

### bcm_kona_i2c_xfer
- Return type: static int
- Signature: bcm_kona_i2c_xfer(struct i2c_adapter * adapter,struct i2c_msg msgs[],int num)
- Line: 590

### bcm_kona_send_i2c_cmd
- Return type: static int
- Signature: bcm_kona_send_i2c_cmd(struct bcm_kona_i2c_dev * dev,enum bcm_kona_cmd_t cmd)
- Line: 242

## Structs (3)

### bcm_kona_i2c_dev
- Line: 144
- Members:
  - time_m: uint8_t
  - time_n: uint8_t
  - prescale: uint8_t
  - time_p: uint8_t
  - no_div: uint8_t
  - time_div: uint8_t
  - hs_hold: uint8_t
  - hs_high_phase: uint8_t
  - hs_setup: uint8_t
  - prescale: uint8_t
  - time_p: uint8_t
  - no_div: uint8_t
  - time_div: uint8_t
  - device: device *
  - base: void __iomem *
  - irq: int
  - external_clk: clk *
  - adapter: i2c_adapter
  - done: completion
  - std_cfg: const struct bus_speed_cfg *
  - hs_cfg: const struct hs_bus_speed_cfg *

### bus_speed_cfg
- Line: 111
- Members:
  - time_m: uint8_t
  - time_n: uint8_t
  - prescale: uint8_t
  - time_p: uint8_t
  - no_div: uint8_t
  - time_div: uint8_t
  - hs_hold: uint8_t
  - hs_high_phase: uint8_t
  - hs_setup: uint8_t
  - prescale: uint8_t
  - time_p: uint8_t
  - no_div: uint8_t
  - time_div: uint8_t
  - device: device *
  - base: void __iomem *
  - irq: int
  - external_clk: clk *
  - adapter: i2c_adapter
  - done: completion
  - std_cfg: const struct bus_speed_cfg *
  - hs_cfg: const struct hs_bus_speed_cfg *

### hs_bus_speed_cfg
- Line: 121
- Members:
  - time_m: uint8_t
  - time_n: uint8_t
  - prescale: uint8_t
  - time_p: uint8_t
  - no_div: uint8_t
  - time_div: uint8_t
  - hs_hold: uint8_t
  - hs_high_phase: uint8_t
  - hs_setup: uint8_t
  - prescale: uint8_t
  - time_p: uint8_t
  - no_div: uint8_t
  - time_div: uint8_t
  - device: device *
  - base: void __iomem *
  - irq: int
  - external_clk: clk *
  - adapter: i2c_adapter
  - done: completion
  - std_cfg: const struct bus_speed_cfg *
  - hs_cfg: const struct hs_bus_speed_cfg *

## Enums (3)

### bcm_kona_cmd_t
- Line: 93

### bus_speed_index
- Line: 100

### hs_bus_speed_index
- Line: 106

## Variables (5)

- static **bcm_algo** : const struct i2c_algorithm (line 698)
- static **bcm_kona_i2c_driver** : platform_driver (line 874)
- static **bcm_kona_i2c_of_match** : const struct of_device_id[] (line 868)
- static **hs_cfg_table** : const struct hs_bus_speed_cfg[] (line 140)
- static **std_cfg_table** : const struct bus_speed_cfg[] (line 134)

## Macros (59)

- **CLKEN_AUTOSENSE_OFF_MASK** (line 58)
- **CLKEN_CLKEN_MASK** (line 61)
- **CLKEN_M_SHIFT** (line 59)
- **CLKEN_N_SHIFT** (line 60)
- **CLKEN_OFFSET** (line 57)
- **CONTROLLER_CODE** (line 88)
- **CS_ACK_CMD_GEN_RESTART** (line 20)
- **CS_ACK_CMD_GEN_START** (line 19)
- **CS_ACK_MASK** (line 18)
- **CS_ACK_SHIFT** (line 17)
- **CS_CMD_CMD_NO_ACTION** (line 22)
- **CS_CMD_CMD_START_RESTART** (line 23)
- **CS_CMD_CMD_STOP** (line 24)
- **CS_CMD_SHIFT** (line 21)
- **CS_EN_CMD_ENABLE_BSC** (line 26)
- **CS_EN_SHIFT** (line 25)
- **CS_OFFSET** (line 16)
- **DAT_OFFSET** (line 34)
- **FIFO_STATUS_OFFSET** (line 63)
- **FIFO_STATUS_RXFIFO_EMPTY_MASK** (line 64)
- **FIFO_STATUS_TXFIFO_EMPTY_MASK** (line 65)
- **HSTIM_HS_HIGH_PHASE_SHIFT** (line 70)
- **HSTIM_HS_HOLD_SHIFT** (line 69)
- **HSTIM_HS_MODE_MASK** (line 68)
- **HSTIM_HS_SETUP_SHIFT** (line 71)
- **HSTIM_OFFSET** (line 67)
- **HS_EXT_CLK_FREQ** (line 86)
- **I2C_TIMEOUT** (line 90)
- **IER_FIFO_INT_EN_MASK** (line 45)
- **IER_I2C_INT_EN_MASK** (line 44)
- **IER_NOACK_EN_MASK** (line 46)
- **IER_OFFSET** (line 42)
- **IER_READ_COMPLETE_INT_MASK** (line 43)
- **ISR_CMDBUSY_MASK** (line 50)
- **ISR_ERR_MASK** (line 53)
- **ISR_NOACK_MASK** (line 55)
- **ISR_OFFSET** (line 48)
- **ISR_READ_COMPLETE_MASK** (line 51)
- **ISR_RESERVED_MASK** (line 49)
- **ISR_SES_DONE_MASK** (line 52)
- **ISR_TXFIFOEMPTY_MASK** (line 54)
- **MAX_RX_FIFO_SIZE** (line 82)
- **MAX_TX_FIFO_SIZE** (line 83)
- **PADCTL_OFFSET** (line 73)
- **PADCTL_PAD_OUT_EN_MASK** (line 74)
- **RXFCR_NACK_EN_SHIFT** (line 77)
- **RXFCR_OFFSET** (line 76)
- **RXFCR_READ_COUNT_SHIFT** (line 78)
- **RXFIFORDOUT_OFFSET** (line 79)
- **STD_EXT_CLK_FREQ** (line 85)
- **TIM_DIV_SHIFT** (line 32)
- **TIM_NO_DIV_SHIFT** (line 31)
- **TIM_OFFSET** (line 28)
- **TIM_PRESCALE_SHIFT** (line 29)
- **TIM_P_SHIFT** (line 30)
- **TOUT_OFFSET** (line 36)
- **TXFCR_FIFO_EN_MASK** (line 40)
- **TXFCR_FIFO_FLUSH_MASK** (line 39)
- **TXFCR_OFFSET** (line 38)
