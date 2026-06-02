# drivers/i2c/busses/i2c-designware-master.c

Subsystem: drivers/i2c

## Functions (22)

### __i2c_dw_xfer_one_part
- Return type: static int
- Signature: __i2c_dw_xfer_one_part(struct dw_i2c_dev * dev,struct i2c_msg * msgs,size_t num)
- Line: 749

### amd_i2c_dw_xfer_quirk
- Return type: static int
- Signature: amd_i2c_dw_xfer_quirk(struct dw_i2c_dev * dev,struct i2c_msg * msgs,int num_msgs)
- Line: 292

### i2c_dw_check_stopbit
- Return type: static int
- Signature: i2c_dw_check_stopbit(struct dw_i2c_dev * dev)
- Line: 263

### i2c_dw_configure_master
- Return type: void
- Signature: i2c_dw_configure_master(struct dw_i2c_dev * dev)
- Line: 924

### i2c_dw_init_recovery_info
- Return type: static int
- Signature: i2c_dw_init_recovery_info(struct dw_i2c_dev * dev)
- Line: 970

### i2c_dw_is_controller_active
- Return type: static bool
- Signature: i2c_dw_is_controller_active(struct dw_i2c_dev * dev)
- Line: 250

### i2c_dw_isr_master
- Return type: irqreturn_t
- Signature: i2c_dw_isr_master(struct dw_i2c_dev * dev)
- Line: 685

### i2c_dw_msg_is_valid
- Return type: static bool
- Signature: i2c_dw_msg_is_valid(struct dw_i2c_dev * dev,const struct i2c_msg * msgs,size_t idx)
- Line: 827

### i2c_dw_prepare_recovery
- Return type: static void
- Signature: i2c_dw_prepare_recovery(struct i2c_adapter * adap)
- Line: 952

### i2c_dw_probe_master
- Return type: int
- Signature: i2c_dw_probe_master(struct dw_i2c_dev * dev)
- Line: 1009

### i2c_dw_process_transfer
- Return type: static void
- Signature: i2c_dw_process_transfer(struct dw_i2c_dev * dev,unsigned int stat)
- Line: 634

### i2c_dw_read
- Return type: static void
- Signature: i2c_dw_read(struct dw_i2c_dev * dev)
- Line: 516

### i2c_dw_read_clear_intrbits
- Return type: static u32
- Signature: i2c_dw_read_clear_intrbits(struct dw_i2c_dev * dev)
- Line: 573

### i2c_dw_recv_len
- Return type: static u8
- Signature: i2c_dw_recv_len(struct dw_i2c_dev * dev,u8 len)
- Line: 489

### i2c_dw_set_timings_master
- Return type: static int
- Signature: i2c_dw_set_timings_master(struct dw_i2c_dev * dev)
- Line: 34

### i2c_dw_status
- Return type: static int
- Signature: i2c_dw_status(struct dw_i2c_dev * dev)
- Line: 277

### i2c_dw_unprepare_recovery
- Return type: static void
- Signature: i2c_dw_unprepare_recovery(struct i2c_adapter * adap)
- Line: 961

### i2c_dw_wait_transfer
- Return type: static int
- Signature: i2c_dw_wait_transfer(struct dw_i2c_dev * dev)
- Line: 716

### i2c_dw_xfer
- Return type: int
- Signature: i2c_dw_xfer(struct i2c_adapter * adap,struct i2c_msg * msgs,int num)
- Line: 914

### i2c_dw_xfer_common
- Return type: static int
- Signature: i2c_dw_xfer_common(struct dw_i2c_dev * dev,struct i2c_msg msgs[],int num)
- Line: 859

### i2c_dw_xfer_init
- Return type: static void
- Signature: i2c_dw_xfer_init(struct dw_i2c_dev * dev)
- Line: 188

### i2c_dw_xfer_msg
- Return type: static void
- Signature: i2c_dw_xfer_msg(struct dw_i2c_dev * dev)
- Line: 375

## Macros (4)

- **AMD_MASTERCFG_MASK** (line 32)
- **AMD_TIMEOUT_MAX_US** (line 31)
- **AMD_TIMEOUT_MIN_US** (line 30)
- **DEFAULT_SYMBOL_NAMESPACE** (line 12)
