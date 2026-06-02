# drivers/i2c/busses/i2c-octeon-core.c

Subsystem: drivers/i2c

## Functions (33)

### octeon_i2c_block_disable
- Return type: static void
- Signature: octeon_i2c_block_disable(struct octeon_i2c * i2c)
- Line: 151

### octeon_i2c_block_enable
- Return type: static void
- Signature: octeon_i2c_block_enable(struct octeon_i2c * i2c)
- Line: 138

### octeon_i2c_check_status
- Return type: static int
- Signature: octeon_i2c_check_status(struct octeon_i2c * i2c,int final_read)
- Line: 208

### octeon_i2c_get_scl
- Return type: static int
- Signature: octeon_i2c_get_scl(struct i2c_adapter * adap)
- Line: 936

### octeon_i2c_get_sda
- Return type: static int
- Signature: octeon_i2c_get_sda(struct i2c_adapter * adap)
- Line: 952

### octeon_i2c_hlc_block_comp_read
- Return type: static int
- Signature: octeon_i2c_hlc_block_comp_read(struct octeon_i2c * i2c,struct i2c_msg * msgs)
- Line: 646

### octeon_i2c_hlc_block_comp_write
- Return type: static int
- Signature: octeon_i2c_hlc_block_comp_write(struct octeon_i2c * i2c,struct i2c_msg * msgs)
- Line: 700

### octeon_i2c_hlc_cmd_send
- Return type: static int
- Signature: octeon_i2c_hlc_cmd_send(struct octeon_i2c * i2c,u64 cmd)
- Line: 519

### octeon_i2c_hlc_comp_read
- Return type: static int
- Signature: octeon_i2c_hlc_comp_read(struct octeon_i2c * i2c,struct i2c_msg * msgs)
- Line: 558

### octeon_i2c_hlc_comp_write
- Return type: static int
- Signature: octeon_i2c_hlc_comp_write(struct octeon_i2c * i2c,struct i2c_msg * msgs)
- Line: 594

### octeon_i2c_hlc_disable
- Return type: static void
- Signature: octeon_i2c_hlc_disable(struct octeon_i2c * i2c)
- Line: 129

### octeon_i2c_hlc_enable
- Return type: static void
- Signature: octeon_i2c_hlc_enable(struct octeon_i2c * i2c)
- Line: 100

### octeon_i2c_hlc_ext
- Return type: static bool
- Signature: octeon_i2c_hlc_ext(struct octeon_i2c * i2c,struct i2c_msg msg,u64 * cmd_in,u64 * ext)
- Line: 528

### octeon_i2c_hlc_int_clear
- Return type: static void
- Signature: octeon_i2c_hlc_int_clear(struct octeon_i2c * i2c)
- Line: 91

### octeon_i2c_hlc_read
- Return type: static int
- Signature: octeon_i2c_hlc_read(struct octeon_i2c * i2c,struct i2c_msg * msgs)
- Line: 443

### octeon_i2c_hlc_read_cmd
- Return type: static int
- Signature: octeon_i2c_hlc_read_cmd(struct octeon_i2c * i2c,struct i2c_msg msg,u64 cmd)
- Line: 547

### octeon_i2c_hlc_test_valid
- Return type: static bool
- Signature: octeon_i2c_hlc_test_valid(struct octeon_i2c * i2c)
- Line: 86

### octeon_i2c_hlc_wait
- Return type: static int
- Signature: octeon_i2c_hlc_wait(struct octeon_i2c * i2c)
- Line: 170

### octeon_i2c_hlc_write
- Return type: static int
- Signature: octeon_i2c_hlc_write(struct octeon_i2c * i2c,struct i2c_msg * msgs)
- Line: 480

### octeon_i2c_init_lowlevel
- Return type: int
- Signature: octeon_i2c_init_lowlevel(struct octeon_i2c * i2c)
- Line: 909

### octeon_i2c_isr
- Return type: irqreturn_t
- Signature: octeon_i2c_isr(int irq,void * dev_id)
- Line: 29

### octeon_i2c_prepare_recovery
- Return type: static void
- Signature: octeon_i2c_prepare_recovery(struct i2c_adapter * adap)
- Line: 961

### octeon_i2c_read
- Return type: static int
- Signature: octeon_i2c_read(struct octeon_i2c * i2c,int target,u8 * data,u16 * rlength,bool recv_len)
- Line: 346

### octeon_i2c_recovery
- Return type: static int
- Signature: octeon_i2c_recovery(struct octeon_i2c * i2c)
- Line: 287

### octeon_i2c_set_clock
- Return type: void
- Signature: octeon_i2c_set_clock(struct octeon_i2c * i2c)
- Line: 824

### octeon_i2c_set_scl
- Return type: static void
- Signature: octeon_i2c_set_scl(struct i2c_adapter * adap,int val)
- Line: 945

### octeon_i2c_start
- Return type: static int
- Signature: octeon_i2c_start(struct octeon_i2c * i2c)
- Line: 304

### octeon_i2c_stop
- Return type: static void
- Signature: octeon_i2c_stop(struct octeon_i2c * i2c)
- Line: 329

### octeon_i2c_test_iflg
- Return type: static bool
- Signature: octeon_i2c_test_iflg(struct octeon_i2c * i2c)
- Line: 39

### octeon_i2c_unprepare_recovery
- Return type: static void
- Signature: octeon_i2c_unprepare_recovery(struct i2c_adapter * adap)
- Line: 979

### octeon_i2c_wait
- Return type: static int
- Signature: octeon_i2c_wait(struct octeon_i2c * i2c)
- Line: 50

### octeon_i2c_write
- Return type: static int
- Signature: octeon_i2c_write(struct octeon_i2c * i2c,int target,const u8 * data,int length)
- Line: 414

### octeon_i2c_xfer
- Return type: int
- Signature: octeon_i2c_xfer(struct i2c_adapter * adap,struct i2c_msg * msgs,int num)
- Line: 761

## Variables (1)

- **octeon_i2c_recovery_info** : i2c_bus_recovery_info (line 995)

## Macros (3)

- **INITIAL_DELTA_HZ** (line 24)
- **TWSI_MASTER_CLK_REG_DEF_VAL** (line 25)
- **TWSI_MASTER_CLK_REG_OTX2_VAL** (line 26)
