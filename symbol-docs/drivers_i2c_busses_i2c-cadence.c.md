# drivers/i2c/busses/i2c-cadence.c

Subsystem: drivers/i2c

## Functions (32)

### cdns_i2c_calc_divs
- Return type: static int
- Signature: cdns_i2c_calc_divs(unsigned long * f,unsigned long input_clk,unsigned int * a,unsigned int * b)
- Line: 1254

### cdns_i2c_clear_bus_hold
- Return type: static void
- Signature: cdns_i2c_clear_bus_hold(struct cdns_i2c * id)
- Line: 302

### cdns_i2c_clk_notifier_cb
- Return type: static int
- Signature: cdns_i2c_clk_notifier_cb(struct notifier_block * nb,unsigned long event,void * data)
- Line: 1357

### cdns_i2c_detect_transfer_size
- Return type: static void
- Signature: cdns_i2c_detect_transfer_size(struct cdns_i2c * id)
- Line: 1459

### cdns_i2c_error_check
- Return type: static bool
- Signature: cdns_i2c_error_check(struct cdns_i2c * id)
- Line: 629

### cdns_i2c_func
- Return type: static u32
- Signature: cdns_i2c_func(struct i2c_adapter * adap)
- Line: 1176

### cdns_i2c_init
- Return type: static void
- Signature: cdns_i2c_init(struct cdns_i2c * id)
- Line: 243

### cdns_i2c_isr
- Return type: static irqreturn_t
- Signature: cdns_i2c_isr(int irq,void * ptr)
- Line: 618

### cdns_i2c_master_common_xfer
- Return type: static int
- Signature: cdns_i2c_master_common_xfer(struct i2c_adapter * adap,struct i2c_msg * msgs,int num)
- Line: 1005

### cdns_i2c_master_isr
- Return type: static irqreturn_t
- Signature: cdns_i2c_master_isr(void * ptr)
- Line: 463

### cdns_i2c_master_reset
- Return type: static void
- Signature: cdns_i2c_master_reset(struct i2c_adapter * adap)
- Line: 909

### cdns_i2c_master_xfer
- Return type: static int
- Signature: cdns_i2c_master_xfer(struct i2c_adapter * adap,struct i2c_msg * msgs,int num)
- Line: 1092

### cdns_i2c_master_xfer_atomic
- Return type: static int
- Signature: cdns_i2c_master_xfer_atomic(struct i2c_adapter * adap,struct i2c_msg * msgs,int num)
- Line: 1143

### cdns_i2c_mrecv
- Return type: static void
- Signature: cdns_i2c_mrecv(struct cdns_i2c * id)
- Line: 716

### cdns_i2c_mrecv_atomic
- Return type: static void
- Signature: cdns_i2c_mrecv_atomic(struct cdns_i2c * id)
- Line: 643

### cdns_i2c_msend
- Return type: static void
- Signature: cdns_i2c_msend(struct cdns_i2c * id)
- Line: 840

### cdns_i2c_msend_rem_atomic
- Return type: static void
- Signature: cdns_i2c_msend_rem_atomic(struct cdns_i2c * id)
- Line: 812

### cdns_i2c_probe
- Return type: static int
- Signature: cdns_i2c_probe(struct platform_device * pdev)
- Line: 1493

### cdns_i2c_process_msg
- Return type: static int
- Signature: cdns_i2c_process_msg(struct cdns_i2c * id,struct i2c_msg * msg,struct i2c_adapter * adap)
- Line: 931

### cdns_i2c_remove
- Return type: static void
- Signature: cdns_i2c_remove(struct platform_device * pdev)
- Line: 1625

### cdns_i2c_resume
- Return type: static int __maybe_unused
- Signature: cdns_i2c_resume(struct device * dev)
- Line: 1415

### cdns_i2c_runtime_resume
- Return type: static int
- Signature: cdns_i2c_runtime_resume(struct device * dev)
- Line: 281

### cdns_i2c_runtime_suspend
- Return type: static int
- Signature: cdns_i2c_runtime_suspend(struct device * dev)
- Line: 264

### cdns_i2c_set_mode
- Return type: static void
- Signature: cdns_i2c_set_mode(enum cdns_i2c_mode mode,struct cdns_i2c * id)
- Line: 316

### cdns_i2c_setclk
- Return type: static int
- Signature: cdns_i2c_setclk(unsigned long clk_in,struct cdns_i2c * id)
- Line: 1317

### cdns_i2c_slave_isr
- Return type: static irqreturn_t
- Signature: cdns_i2c_slave_isr(void * ptr)
- Line: 405

### cdns_i2c_slave_rcv_data
- Return type: static void
- Signature: cdns_i2c_slave_rcv_data(struct cdns_i2c * id)
- Line: 359

### cdns_i2c_slave_send_data
- Return type: static void
- Signature: cdns_i2c_slave_send_data(struct cdns_i2c * id)
- Line: 380

### cdns_i2c_suspend
- Return type: static int __maybe_unused
- Signature: cdns_i2c_suspend(struct device * dev)
- Line: 1403

### cdns_is_holdquirk
- Return type: static bool
- Signature: cdns_is_holdquirk(struct cdns_i2c * id,bool hold_wrkaround)
- Line: 309

### cdns_reg_slave
- Return type: static int
- Signature: cdns_reg_slave(struct i2c_client * slave)
- Line: 1190

### cdns_unreg_slave
- Return type: static int
- Signature: cdns_unreg_slave(struct i2c_client * slave)
- Line: 1215

## Structs (2)

### cdns_i2c
- Line: 196
- Members:
  - dev: device *
  - membase: void __iomem *
  - adap: i2c_adapter
  - p_msg: i2c_msg *
  - err_status: int
  - xfer_done: completion
  - p_send_buf: unsigned char *
  - p_recv_buf: unsigned char *
  - send_count: unsigned int
  - recv_count: unsigned int
  - curr_recv_count: unsigned int
  - input_clk: unsigned long
  - i2c_clk: unsigned int
  - bus_hold_flag: unsigned int
  - clk: clk *
  - clk_rate_change_nb: notifier_block
  - reset: reset_control *
  - quirks: u32
  - ctrl_reg: u32
  - rinfo: i2c_bus_recovery_info
  - ctrl_reg_diva_divb: u16
  - slave: i2c_client *
  - dev_mode: cdns_i2c_mode
  - slave_state: cdns_i2c_slave_state
  - fifo_depth: u32
  - transfer_size: unsigned int
  - atomic: bool
  - err_status_atomic: int
  - quirks: u32

### cdns_platform_data
- Line: 229
- Members:
  - dev: device *
  - membase: void __iomem *
  - adap: i2c_adapter
  - p_msg: i2c_msg *
  - err_status: int
  - xfer_done: completion
  - p_send_buf: unsigned char *
  - p_recv_buf: unsigned char *
  - send_count: unsigned int
  - recv_count: unsigned int
  - curr_recv_count: unsigned int
  - input_clk: unsigned long
  - i2c_clk: unsigned int
  - bus_hold_flag: unsigned int
  - clk: clk *
  - clk_rate_change_nb: notifier_block
  - reset: reset_control *
  - quirks: u32
  - ctrl_reg: u32
  - rinfo: i2c_bus_recovery_info
  - ctrl_reg_diva_divb: u16
  - slave: i2c_client *
  - dev_mode: cdns_i2c_mode
  - slave_state: cdns_i2c_slave_state
  - fifo_depth: u32
  - transfer_size: unsigned int
  - atomic: bool
  - err_status_atomic: int
  - quirks: u32

## Enums (2)

### cdns_i2c_mode
- Line: 145

### cdns_i2c_slave_state
- Line: 157

## Variables (5)

- static **cdns_i2c_algo** : const struct i2c_algorithm (line 1232)
- static **cdns_i2c_dev_pm_ops** : const struct dev_pm_ops (line 1435)
- static **cdns_i2c_drv** : platform_driver (line 1638)
- static **cdns_i2c_of_match** : const struct of_device_id[] (line 1445)
- static **r1p10_i2c_def** : const struct cdns_platform_data (line 1441)

## Macros (56)

- **CDNS_I2C_ADDR_MASK** (line 65)
- **CDNS_I2C_ADDR_OFFSET** (line 24)
- **CDNS_I2C_BROKEN_HOLD_BIT** (line 130)
- **CDNS_I2C_CR_ACK_EN** (line 35)
- **CDNS_I2C_CR_CLR_FIFO** (line 41)
- **CDNS_I2C_CR_DIVA_MASK** (line 43)
- **CDNS_I2C_CR_DIVA_SHIFT** (line 42)
- **CDNS_I2C_CR_DIVB_MASK** (line 45)
- **CDNS_I2C_CR_DIVB_SHIFT** (line 44)
- **CDNS_I2C_CR_HOLD** (line 34)
- **CDNS_I2C_CR_MASTER_EN_MASK** (line 47)
- **CDNS_I2C_CR_MS** (line 37)
- **CDNS_I2C_CR_NEA** (line 36)
- **CDNS_I2C_CR_OFFSET** (line 22)
- **CDNS_I2C_CR_RW** (line 39)
- **CDNS_I2C_CR_SLAVE_EN_MASK** (line 51)
- **CDNS_I2C_DATA_OFFSET** (line 25)
- **CDNS_I2C_DIVA_MAX** (line 125)
- **CDNS_I2C_DIVB_MAX** (line 126)
- **CDNS_I2C_ENABLED_INTR_MASK** (line 98)
- **CDNS_I2C_FIFO_DEPTH_DEFAULT** (line 118)
- **CDNS_I2C_IDR_OFFSET** (line 31)
- **CDNS_I2C_IER_OFFSET** (line 30)
- **CDNS_I2C_IMR_OFFSET** (line 29)
- **CDNS_I2C_ISR_OFFSET** (line 26)
- **CDNS_I2C_IXR_ALL_INTR_MASK** (line 82)
- **CDNS_I2C_IXR_ARB_LOST** (line 72)
- **CDNS_I2C_IXR_COMP** (line 80)
- **CDNS_I2C_IXR_DATA** (line 79)
- **CDNS_I2C_IXR_ERR_INTR_MASK** (line 92)
- **CDNS_I2C_IXR_NACK** (line 78)
- **CDNS_I2C_IXR_RX_OVF** (line 75)
- **CDNS_I2C_IXR_RX_UNF** (line 73)
- **CDNS_I2C_IXR_SLAVE_INTR_MASK** (line 106)
- **CDNS_I2C_IXR_SLV_RDY** (line 76)
- **CDNS_I2C_IXR_TO** (line 77)
- **CDNS_I2C_IXR_TX_OVF** (line 74)
- **CDNS_I2C_MAX_TRANSFER_SIZE** (line 119)
- **CDNS_I2C_POLL_US** (line 131)
- **CDNS_I2C_POLL_US_ATOMIC** (line 132)
- **CDNS_I2C_SR_BA** (line 54)
- **CDNS_I2C_SR_OFFSET** (line 23)
- **CDNS_I2C_SR_RXDV** (line 56)
- **CDNS_I2C_SR_RXRW** (line 57)
- **CDNS_I2C_SR_TXDV** (line 55)
- **CDNS_I2C_TIMEOUT** (line 114)
- **CDNS_I2C_TIMEOUT_MAX** (line 128)
- **CDNS_I2C_TIMEOUT_US** (line 133)
- **CDNS_I2C_TIME_OUT_OFFSET** (line 28)
- **CDNS_I2C_TRANSFER_SIZE**(max) (line 121)
- **CDNS_I2C_XFER_SIZE_OFFSET** (line 27)
- **CNDS_I2C_PM_TIMEOUT** (line 116)
- **DRIVER_NAME** (line 123)
- **cdns_i2c_readreg**(offset) (line 135)
- **cdns_i2c_writereg**(val,offset) (line 136)
- **to_cdns_i2c**(_nb) (line 233)
