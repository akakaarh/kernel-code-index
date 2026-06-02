# drivers/i2c/busses/i2c-img-scb.c

Subsystem: drivers/i2c

## Functions (34)

### img_i2c_atomic
- Return type: static unsigned int
- Signature: img_i2c_atomic(struct img_i2c * i2c,u32 int_status,u32 line_status)
- Line: 732

### img_i2c_atomic_op
- Return type: static void
- Signature: img_i2c_atomic_op(struct img_i2c * i2c,int cmd,u8 data)
- Line: 472

### img_i2c_atomic_op_name
- Return type: static const char *
- Signature: img_i2c_atomic_op_name(unsigned int cmd)
- Line: 464

### img_i2c_atomic_start
- Return type: static void
- Signature: img_i2c_atomic_start(struct img_i2c * i2c)
- Line: 504

### img_i2c_auto
- Return type: static unsigned int
- Signature: img_i2c_auto(struct img_i2c * i2c,unsigned int int_status,unsigned int line_status)
- Line: 853

### img_i2c_check_timer
- Return type: static void
- Signature: img_i2c_check_timer(struct timer_list * t)
- Line: 832

### img_i2c_complete_transaction
- Return type: static void
- Signature: img_i2c_complete_transaction(struct img_i2c * i2c,int status)
- Line: 623

### img_i2c_func
- Return type: static u32
- Signature: img_i2c_func(struct i2c_adapter * adap)
- Line: 1139

### img_i2c_init
- Return type: static int
- Signature: img_i2c_init(struct img_i2c * i2c)
- Line: 1149

### img_i2c_isr
- Return type: static irqreturn_t
- Signature: img_i2c_isr(int irq,void * dev_id)
- Line: 914

### img_i2c_probe
- Return type: static int
- Signature: img_i2c_probe(struct platform_device * pdev)
- Line: 1323

### img_i2c_raw
- Return type: static unsigned int
- Signature: img_i2c_raw(struct img_i2c * i2c,u32 int_status,u32 line_status)
- Line: 642

### img_i2c_raw_atomic_delay_handler
- Return type: static unsigned int
- Signature: img_i2c_raw_atomic_delay_handler(struct img_i2c * i2c,u32 int_status,u32 line_status)
- Line: 633

### img_i2c_raw_op
- Return type: static void
- Signature: img_i2c_raw_op(struct img_i2c * i2c)
- Line: 451

### img_i2c_read
- Return type: static void
- Signature: img_i2c_read(struct img_i2c * i2c)
- Line: 588

### img_i2c_read_fifo
- Return type: static void
- Signature: img_i2c_read_fifo(struct img_i2c * i2c)
- Line: 546

### img_i2c_readl
- Return type: static u32
- Signature: img_i2c_readl(struct img_i2c * i2c,u32 offset)
- Line: 419

### img_i2c_remove
- Return type: static void
- Signature: img_i2c_remove(struct platform_device * dev)
- Line: 1410

### img_i2c_reset_bus
- Return type: static int
- Signature: img_i2c_reset_bus(struct img_i2c * i2c)
- Line: 1007

### img_i2c_reset_start
- Return type: static void
- Signature: img_i2c_reset_start(struct img_i2c * i2c)
- Line: 704

### img_i2c_resume
- Return type: static int
- Signature: img_i2c_resume(struct device * dev)
- Line: 1465

### img_i2c_runtime_resume
- Return type: static int
- Signature: img_i2c_runtime_resume(struct device * dev)
- Line: 1430

### img_i2c_runtime_suspend
- Return type: static int
- Signature: img_i2c_runtime_suspend(struct device * dev)
- Line: 1420

### img_i2c_sequence
- Return type: static unsigned int
- Signature: img_i2c_sequence(struct img_i2c * i2c,u32 int_status)
- Line: 654

### img_i2c_soft_reset
- Return type: static void
- Signature: img_i2c_soft_reset(struct img_i2c * i2c)
- Line: 511

### img_i2c_stop_start
- Return type: static void
- Signature: img_i2c_stop_start(struct img_i2c * i2c)
- Line: 718

### img_i2c_suspend
- Return type: static int
- Signature: img_i2c_suspend(struct device * dev)
- Line: 1451

### img_i2c_switch_mode
- Return type: static void
- Signature: img_i2c_switch_mode(struct img_i2c * i2c,enum img_i2c_mode mode)
- Line: 444

### img_i2c_transaction_halt
- Return type: static void
- Signature: img_i2c_transaction_halt(struct img_i2c * i2c,bool t_halt)
- Line: 530

### img_i2c_wr_rd_fence
- Return type: static void
- Signature: img_i2c_wr_rd_fence(struct img_i2c * i2c)
- Line: 436

### img_i2c_write
- Return type: static void
- Signature: img_i2c_write(struct img_i2c * i2c)
- Line: 602

### img_i2c_write_fifo
- Return type: static void
- Signature: img_i2c_write_fifo(struct img_i2c * i2c)
- Line: 567

### img_i2c_writel
- Return type: static void
- Signature: img_i2c_writel(struct img_i2c * i2c,u32 offset,u32 value)
- Line: 414

### img_i2c_xfer
- Return type: static int
- Signature: img_i2c_xfer(struct i2c_adapter * adap,struct i2c_msg * msgs,int num)
- Line: 1024

## Structs (2)

### img_i2c
- Line: 365
- Members:
  - name: const char *
  - max_bitrate: unsigned int
  - tckh: unsigned int
  - tckl: unsigned int
  - tsdh: unsigned int
  - tsdl: unsigned int
  - tp2s: unsigned int
  - tph: unsigned int
  - tpl: unsigned int
  - adap: i2c_adapter
  - base: void __iomem *
  - scb_clk: clk *
  - sys_clk: clk *
  - bitrate: unsigned int
  - need_wr_rd_fence: bool
  - msg_complete: completion
  - lock: spinlock_t
  - msg: i2c_msg
  - last_msg: bool
  - msg_status: int
  - mode: img_i2c_mode
  - int_enable: u32
  - line_status: u32
  - check_timer: timer_list
  - t_halt: bool
  - at_t_done: bool
  - at_slave_event: bool
  - at_cur_cmd: int
  - at_cur_data: u8
  - seq: u8 *
  - raw_timeout: unsigned int

### img_i2c_timings
- Line: 295
- Members:
  - name: const char *
  - max_bitrate: unsigned int
  - tckh: unsigned int
  - tckl: unsigned int
  - tsdh: unsigned int
  - tsdl: unsigned int
  - tp2s: unsigned int
  - tph: unsigned int
  - tpl: unsigned int
  - adap: i2c_adapter
  - base: void __iomem *
  - scb_clk: clk *
  - sys_clk: clk *
  - bitrate: unsigned int
  - need_wr_rd_fence: bool
  - msg_complete: completion
  - lock: spinlock_t
  - msg: i2c_msg
  - last_msg: bool
  - msg_status: int
  - mode: img_i2c_mode
  - int_enable: u32
  - line_status: u32
  - check_timer: timer_list
  - t_halt: bool
  - at_t_done: bool
  - at_slave_event: bool
  - at_cur_cmd: int
  - at_cur_data: u8
  - seq: u8 *
  - raw_timeout: unsigned int

## Enums (1)

### img_i2c_mode
- Line: 283

## Variables (9)

- static **img_i2c_algo** : const struct i2c_algorithm (line 1144)
- static **img_i2c_atomic_cmd_names** : const char * const[] (line 354)
- static **img_i2c_int_enable_by_mode** : unsigned int[] (line 342)
- static **img_i2c_pm** : const struct dev_pm_ops (line 1479)
- static **img_i2c_reset_seq** : u8[] (line 331)
- static **img_i2c_stop_seq** : u8[] (line 338)
- static **img_scb_i2c_driver** : platform_driver (line 1490)
- static **img_scb_i2c_match** : const struct of_device_id[] (line 1484)
- static **timings** : img_i2c_timings[] (line 303)

## Macros (124)

- **CMD_GEN_ACK** (line 244)
- **CMD_GEN_DATA** (line 241)
- **CMD_GEN_NACK** (line 245)
- **CMD_GEN_START** (line 242)
- **CMD_GEN_STOP** (line 243)
- **CMD_PAUSE** (line 240)
- **CMD_RET_ACK** (line 247)
- **CMD_RET_DATA** (line 246)
- **FIFO_READ_EMPTY** (line 126)
- **FIFO_READ_FULL** (line 125)
- **FIFO_WRITE_EMPTY** (line 128)
- **FIFO_WRITE_FULL** (line 127)
- **IMG_I2C_PM_TIMEOUT** (line 281)
- **IMG_I2C_TIMEOUT** (line 257)
- **INT_ADDR_ACK_ERR** (line 145)
- **INT_BUS_INACTIVE** (line 140)
- **INT_ENABLE_MASK_ATOMIC** (line 168)
- **INT_ENABLE_MASK_AUTOMATIC** (line 173)
- **INT_ENABLE_MASK_INACTIVE** (line 162)
- **INT_ENABLE_MASK_RAW** (line 166)
- **INT_ENABLE_MASK_WAITSTOP** (line 182)
- **INT_FIFO_EMPTY** (line 148)
- **INT_FIFO_EMPTYING** (line 149)
- **INT_FIFO_FILLING** (line 147)
- **INT_FIFO_FULL** (line 146)
- **INT_FIFO_FULL_FILLING** (line 156)
- **INT_LEVEL** (line 159)
- **INT_MASTER_HALTED** (line 152)
- **INT_SCLK_LOW_TIMEOUT** (line 142)
- **INT_SDAT_LOW_TIMEOUT** (line 143)
- **INT_SLAVE_EVENT** (line 151)
- **INT_STOP_DETECTED** (line 154)
- **INT_TIMING** (line 153)
- **INT_TRANSACTION_DONE** (line 150)
- **INT_UNEXPECTED_START** (line 141)
- **INT_WRITE_ACK_ERR** (line 144)
- **ISR_COMPLETE**(err) (line 278)
- **ISR_COMPLETE_M** (line 274)
- **ISR_FATAL**(err) (line 279)
- **ISR_FATAL_M** (line 275)
- **ISR_STATUS_M** (line 277)
- **ISR_WAITSTOP** (line 276)
- **LINESTAT_ABORT_DET** (line 206)
- **LINESTAT_ACK_DET** (line 203)
- **LINESTAT_ACK_OR_NACK_DET** (line 207)
- **LINESTAT_BUS_IDLE** (line 196)
- **LINESTAT_CLEAR_SHIFT** (line 211)
- **LINESTAT_DET_ACK_STATUS** (line 194)
- **LINESTAT_DET_NACK_STATUS** (line 195)
- **LINESTAT_DET_START_STATUS** (line 192)
- **LINESTAT_DET_STOP_STATUS** (line 193)
- **LINESTAT_GEN_LINE_MASK_STATUS** (line 200)
- **LINESTAT_INPUT_DATA** (line 208)
- **LINESTAT_INPUT_DATA_SHIFT** (line 209)
- **LINESTAT_INPUT_HELD_V** (line 205)
- **LINESTAT_LATCHED** (line 212)
- **LINESTAT_NACK_DET** (line 204)
- **LINESTAT_SCLK_EN** (line 189)
- **LINESTAT_SCLK_LINE_STATUS** (line 188)
- **LINESTAT_SCLK_OUT_STATUS** (line 198)
- **LINESTAT_SDAT_EN** (line 191)
- **LINESTAT_SDAT_LINE_STATUS** (line 190)
- **LINESTAT_SDAT_OUT_STATUS** (line 199)
- **LINESTAT_START_BIT_DET** (line 201)
- **LINESTAT_STOP_BIT_DET** (line 202)
- **LINESTAT_T_DONE_STATUS** (line 197)
- **OVERRIDE_CMD_MASK** (line 224)
- **OVERRIDE_CMD_SHIFT** (line 223)
- **OVERRIDE_DATA_SHIFT** (line 225)
- **OVERRIDE_DIRECT** (line 222)
- **OVERRIDE_LINE_OVR_EN** (line 221)
- **OVERRIDE_MASTER** (line 220)
- **OVERRIDE_SCLKEN_OVR** (line 217)
- **OVERRIDE_SCLK_DOWN** (line 227)
- **OVERRIDE_SCLK_OVR** (line 216)
- **OVERRIDE_SCLK_UP** (line 229)
- **OVERRIDE_SDATEN_OVR** (line 219)
- **OVERRIDE_SDAT_DOWN** (line 232)
- **OVERRIDE_SDAT_OVR** (line 218)
- **OVERRIDE_SDAT_UP** (line 234)
- **SCB_CLEAR_REG** (line 118)
- **SCB_CLK_SET_REG** (line 97)
- **SCB_CONTROL_CLK_ENABLE** (line 122)
- **SCB_CONTROL_REG** (line 101)
- **SCB_CONTROL_SOFT_RESET** (line 96)
- **SCB_CONTROL_TRANSACTION_HALT** (line 123)
- **SCB_CORE_REV_REG** (line 113)
- **SCB_FIFO_FLUSH_REG** (line 116)
- **SCB_FIFO_STATUS_REG** (line 95)
- **SCB_FILT_BYPASS** (line 132)
- **SCB_FILT_DISABLE** (line 131)
- **SCB_FILT_GLITCH** (line 267)
- **SCB_FILT_INC_MASK** (line 133)
- **SCB_FILT_INC_SHIFT** (line 134)
- **SCB_INC_MASK** (line 135)
- **SCB_INC_SHIFT** (line 136)
- **SCB_INT_CLEAR_REG** (line 99)
- **SCB_INT_MASK_REG** (line 100)
- **SCB_INT_STATUS_REG** (line 98)
- **SCB_OPT_INC** (line 264)
- **SCB_OVERRIDE_REG** (line 89)
- **SCB_READ_ADDR_REG** (line 90)
- **SCB_READ_COUNT_REG** (line 91)
- **SCB_READ_DATA_REG** (line 93)
- **SCB_READ_FIFO_REG** (line 117)
- **SCB_READ_XADDR_REG** (line 110)
- **SCB_STATUS_REG** (line 88)
- **SCB_TIME_TBI_REG** (line 105)
- **SCB_TIME_TCKH_REG** (line 114)
- **SCB_TIME_TCKL_REG** (line 115)
- **SCB_TIME_TDL_REG** (line 107)
- **SCB_TIME_TP2S_REG** (line 104)
- **SCB_TIME_TPH_REG** (line 103)
- **SCB_TIME_TPL_REG** (line 102)
- **SCB_TIME_TSDH_REG** (line 109)
- **SCB_TIME_TSDL_REG** (line 108)
- **SCB_TIME_TSL_REG** (line 106)
- **SCB_WRITE_ADDR_REG** (line 92)
- **SCB_WRITE_COUNT_REG** (line 112)
- **SCB_WRITE_DATA_REG** (line 94)
- **SCB_WRITE_XADDR_REG** (line 111)
- **TIMEOUT_TBI** (line 251)
- **TIMEOUT_TDL** (line 253)
- **TIMEOUT_TSL** (line 252)
