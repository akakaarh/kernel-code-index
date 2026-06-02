# drivers/i2c/busses/i2c-xiic.c

Subsystem: drivers/i2c

## Functions (36)

### __xiic_start_xfer
- Return type: static void
- Signature: __xiic_start_xfer(struct xiic_i2c * i2c)
- Line: 1207

### xiic_bus_busy
- Return type: static int
- Signature: xiic_bus_busy(struct xiic_i2c * i2c)
- Line: 899

### xiic_clear_rx_fifo
- Return type: static int
- Signature: xiic_clear_rx_fifo(struct xiic_i2c * i2c)
- Line: 354

### xiic_deinit
- Return type: static void
- Signature: xiic_deinit(struct xiic_i2c * i2c)
- Line: 511

### xiic_error_check
- Return type: static bool
- Signature: xiic_error_check(struct xiic_i2c * i2c)
- Line: 650

### xiic_fill_tx_fifo
- Return type: static void
- Signature: xiic_fill_tx_fifo(struct xiic_i2c * i2c)
- Line: 676

### xiic_func
- Return type: static u32
- Signature: xiic_func(struct i2c_adapter * adap)
- Line: 1393

### xiic_getreg32
- Return type: static int
- Signature: xiic_getreg32(struct xiic_i2c * i2c,int reg)
- Line: 316

### xiic_getreg8
- Return type: static u8
- Signature: xiic_getreg8(struct xiic_i2c * i2c,int reg)
- Line: 289

### xiic_i2c_probe
- Return type: static int
- Signature: xiic_i2c_probe(struct platform_device * pdev)
- Line: 1421

### xiic_i2c_remove
- Return type: static void
- Signature: xiic_i2c_remove(struct platform_device * pdev)
- Line: 1531

### xiic_i2c_runtime_resume
- Return type: static int
- Signature: xiic_i2c_runtime_resume(struct device * dev)
- Line: 259

### xiic_i2c_runtime_suspend
- Return type: static int
- Signature: xiic_i2c_runtime_suspend(struct device * dev)
- Line: 250

### xiic_irq_clr
- Return type: static void
- Signature: xiic_irq_clr(struct xiic_i2c * i2c,u32 mask)
- Line: 341

### xiic_irq_clr_en
- Return type: static void
- Signature: xiic_irq_clr_en(struct xiic_i2c * i2c,u32 mask)
- Line: 348

### xiic_irq_dis
- Return type: static void
- Signature: xiic_irq_dis(struct xiic_i2c * i2c,u32 mask)
- Line: 327

### xiic_irq_en
- Return type: static void
- Signature: xiic_irq_en(struct xiic_i2c * i2c,u32 mask)
- Line: 334

### xiic_process
- Return type: static irqreturn_t
- Signature: xiic_process(int irq,void * dev_id)
- Line: 727

### xiic_read_rx
- Return type: static void
- Signature: xiic_read_rx(struct xiic_i2c * i2c)
- Line: 578

### xiic_recv_atomic
- Return type: static void
- Signature: xiic_recv_atomic(struct xiic_i2c * i2c)
- Line: 927

### xiic_reinit
- Return type: static int
- Signature: xiic_reinit(struct xiic_i2c * i2c)
- Line: 478

### xiic_send_rem_atomic
- Return type: static void
- Signature: xiic_send_rem_atomic(struct xiic_i2c * i2c)
- Line: 1081

### xiic_setclk
- Return type: static int
- Signature: xiic_setclk(struct xiic_i2c * i2c)
- Line: 403

### xiic_setreg16
- Return type: static void
- Signature: xiic_setreg16(struct xiic_i2c * i2c,int reg,u16 value)
- Line: 300

### xiic_setreg32
- Return type: static void
- Signature: xiic_setreg32(struct xiic_i2c * i2c,int reg,int value)
- Line: 308

### xiic_setreg8
- Return type: static void
- Signature: xiic_setreg8(struct xiic_i2c * i2c,int reg,u8 value)
- Line: 281

### xiic_smbus_block_read_setup
- Return type: static void
- Signature: xiic_smbus_block_read_setup(struct xiic_i2c * i2c)
- Line: 522

### xiic_start_recv
- Return type: static void
- Signature: xiic_start_recv(struct xiic_i2c * i2c)
- Line: 952

### xiic_start_send
- Return type: static void
- Signature: xiic_start_send(struct xiic_i2c * i2c)
- Line: 1123

### xiic_start_xfer
- Return type: static int
- Signature: xiic_start_xfer(struct xiic_i2c * i2c,struct i2c_msg * msgs,int num)
- Line: 1232

### xiic_tx_fifo_space
- Return type: static int
- Signature: xiic_tx_fifo_space(struct xiic_i2c * i2c)
- Line: 670

### xiic_wait_not_busy
- Return type: static int
- Signature: xiic_wait_not_busy(struct xiic_i2c * i2c)
- Line: 906

### xiic_wait_tx_empty
- Return type: static int
- Signature: xiic_wait_tx_empty(struct xiic_i2c * i2c)
- Line: 373

### xiic_wakeup
- Return type: static void
- Signature: xiic_wakeup(struct xiic_i2c * i2c,enum xilinx_i2c_state code)
- Line: 718

### xiic_xfer
- Return type: static int
- Signature: xiic_xfer(struct i2c_adapter * adap,struct i2c_msg * msgs,int num)
- Line: 1322

### xiic_xfer_atomic
- Return type: static int
- Signature: xiic_xfer_atomic(struct i2c_adapter * adap,struct i2c_msg * msgs,int num)
- Line: 1355

## Structs (3)

### timing_regs
- Line: 120
- Members:
  - dev: device *
  - base: void __iomem *
  - completion: completion
  - adap: i2c_adapter
  - tx_msg: i2c_msg *
  - lock: mutex
  - tx_pos: unsigned int
  - nmsgs: unsigned int
  - rx_msg: i2c_msg *
  - rx_pos: int
  - endianness: xiic_endian
  - clk: clk *
  - state: xilinx_i2c_state
  - singlemaster: bool
  - dynamic: bool
  - prev_msg_tx: bool
  - quirks: u32
  - smbus_block_read: bool
  - input_clk: unsigned long
  - i2c_clk: unsigned int
  - atomic: bool
  - atomic_lock: spinlock_t
  - atomic_xfer_state: xilinx_i2c_state
  - quirks: u32
  - tsusta: unsigned int
  - tsusto: unsigned int
  - thdsta: unsigned int
  - tsudat: unsigned int
  - tbuf: unsigned int

### xiic_i2c
- Line: 82
- Members:
  - dev: device *
  - base: void __iomem *
  - completion: completion
  - adap: i2c_adapter
  - tx_msg: i2c_msg *
  - lock: mutex
  - tx_pos: unsigned int
  - nmsgs: unsigned int
  - rx_msg: i2c_msg *
  - rx_pos: int
  - endianness: xiic_endian
  - clk: clk *
  - state: xilinx_i2c_state
  - singlemaster: bool
  - dynamic: bool
  - prev_msg_tx: bool
  - quirks: u32
  - smbus_block_read: bool
  - input_clk: unsigned long
  - i2c_clk: unsigned int
  - atomic: bool
  - atomic_lock: spinlock_t
  - atomic_xfer_state: xilinx_i2c_state
  - quirks: u32
  - tsusta: unsigned int
  - tsusto: unsigned int
  - thdsta: unsigned int
  - tsudat: unsigned int
  - tbuf: unsigned int

### xiic_version_data
- Line: 108
- Members:
  - dev: device *
  - base: void __iomem *
  - completion: completion
  - adap: i2c_adapter
  - tx_msg: i2c_msg *
  - lock: mutex
  - tx_pos: unsigned int
  - nmsgs: unsigned int
  - rx_msg: i2c_msg *
  - rx_pos: int
  - endianness: xiic_endian
  - clk: clk *
  - state: xilinx_i2c_state
  - singlemaster: bool
  - dynamic: bool
  - prev_msg_tx: bool
  - quirks: u32
  - smbus_block_read: bool
  - input_clk: unsigned long
  - i2c_clk: unsigned int
  - atomic: bool
  - atomic_lock: spinlock_t
  - atomic_xfer_state: xilinx_i2c_state
  - quirks: u32
  - tsusta: unsigned int
  - tsusto: unsigned int
  - thdsta: unsigned int
  - tsudat: unsigned int
  - tbuf: unsigned int

## Enums (3)

### i2c_scl_freq
- Line: 50

### xiic_endian
- Line: 45

### xilinx_i2c_state
- Line: 39

## Variables (7)

- static **timing_reg_values** : const struct timing_regs[] (line 129)
- static **xiic_2_00** : const struct xiic_version_data (line 1410)
- static **xiic_adapter** : const struct i2c_adapter (line 1404)
- static **xiic_algorithm** : const struct i2c_algorithm (line 1398)
- static **xiic_dev_pm_ops** : const struct dev_pm_ops (line 1550)
- static **xiic_i2c_driver** : platform_driver (line 1555)
- static **xiic_of_match** : const struct of_device_id[] (line 1414)

## Macros (65)

- **DRIVER_NAME** (line 35)
- **DYNAMIC_MODE_READ_BROKEN_BIT** (line 36)
- **IIC_RX_FIFO_DEPTH** (line 196)
- **IIC_TX_FIFO_DEPTH** (line 197)
- **MAX_READ_LENGTH_DYNAMIC** (line 214)
- **SMBUS_BLOCK_READ_MIN_LEN** (line 37)
- **XIIC_ADR_REG_OFFSET** (line 146)
- **XIIC_CR_DIR_IS_TX_MASK** (line 170)
- **XIIC_CR_ENABLE_DEVICE_MASK** (line 167)
- **XIIC_CR_GENERAL_CALL_MASK** (line 173)
- **XIIC_CR_MSMS_MASK** (line 169)
- **XIIC_CR_NO_ACK_MASK** (line 171)
- **XIIC_CR_REG_OFFSET** (line 142)
- **XIIC_CR_REPEATED_START_MASK** (line 172)
- **XIIC_CR_TX_FIFO_RESET_MASK** (line 168)
- **XIIC_DGIER_OFFSET** (line 222)
- **XIIC_DRR_REG_OFFSET** (line 145)
- **XIIC_DTR_REG_OFFSET** (line 144)
- **XIIC_GINTR_ENABLE_MASK** (line 242)
- **XIIC_GPO_REG_OFFSET** (line 151)
- **XIIC_I2C_TIMEOUT** (line 231)
- **XIIC_IIER_OFFSET** (line 224)
- **XIIC_IISR_OFFSET** (line 223)
- **XIIC_INTR_AAS_MASK** (line 191)
- **XIIC_INTR_ARB_LOST_MASK** (line 186)
- **XIIC_INTR_BNB_MASK** (line 190)
- **XIIC_INTR_NAAS_MASK** (line 192)
- **XIIC_INTR_RX_FULL_MASK** (line 189)
- **XIIC_INTR_TX_EMPTY_MASK** (line 188)
- **XIIC_INTR_TX_ERROR_MASK** (line 187)
- **XIIC_INTR_TX_HALF_MASK** (line 193)
- **XIIC_MSB_OFFSET** (line 135)
- **XIIC_PM_TIMEOUT** (line 229)
- **XIIC_REG_OFFSET** (line 136)
- **XIIC_RESETR_OFFSET** (line 225)
- **XIIC_RESET_MASK** (line 227)
- **XIIC_RFD_REG_OFFSET** (line 150)
- **XIIC_RFO_REG_OFFSET** (line 148)
- **XIIC_SR_ADDR_AS_SLAVE_MASK** (line 177)
- **XIIC_SR_BUS_BUSY_MASK** (line 178)
- **XIIC_SR_GEN_CALL_MASK** (line 176)
- **XIIC_SR_MSTR_RDING_SLAVE_MASK** (line 179)
- **XIIC_SR_REG_OFFSET** (line 143)
- **XIIC_SR_RX_FIFO_EMPTY_MASK** (line 182)
- **XIIC_SR_RX_FIFO_FULL_MASK** (line 181)
- **XIIC_SR_TX_FIFO_EMPTY_MASK** (line 183)
- **XIIC_SR_TX_FIFO_FULL_MASK** (line 180)
- **XIIC_TBA_REG_OFFSET** (line 149)
- **XIIC_TBUF_REG_OFFSET** (line 161)
- **XIIC_TFO_REG_OFFSET** (line 147)
- **XIIC_THDDAT_REG_OFFSET** (line 164)
- **XIIC_THDSTA_REG_OFFSET** (line 159)
- **XIIC_THIGH_REG_OFFSET** (line 162)
- **XIIC_TLOW_REG_OFFSET** (line 163)
- **XIIC_TSUDAT_REG_OFFSET** (line 160)
- **XIIC_TSUSTA_REG_OFFSET** (line 157)
- **XIIC_TSUSTO_REG_OFFSET** (line 158)
- **XIIC_TX_DYN_START_MASK** (line 210)
- **XIIC_TX_DYN_STOP_MASK** (line 211)
- **XIIC_TX_INTERRUPTS** (line 202)
- **XIIC_TX_RX_INTERRUPTS** (line 205)
- **XIIC_XFER_TIMEOUT** (line 233)
- **XIIC_XFER_TIMEOUT_US** (line 235)
- **xiic_rx_space**(i2c) (line 245)
- **xiic_tx_space**(i2c) (line 244)
