# drivers/i2c/busses/i2c-designware-common.c

Subsystem: drivers/i2c

## Functions (43)

### __i2c_dw_disable
- Return type: void
- Signature: __i2c_dw_disable(struct dw_i2c_dev * dev)
- Line: 620

### dw_reg_read
- Return type: static int
- Signature: dw_reg_read(void * context,unsigned int reg,unsigned int * val)
- Line: 73

### dw_reg_read_swab
- Return type: static int
- Signature: dw_reg_read_swab(void * context,unsigned int reg,unsigned int * val)
- Line: 91

### dw_reg_read_word
- Return type: static int
- Signature: dw_reg_read_word(void * context,unsigned int reg,unsigned int * val)
- Line: 109

### dw_reg_write
- Return type: static int
- Signature: dw_reg_write(void * context,unsigned int reg,unsigned int val)
- Line: 82

### dw_reg_write_swab
- Return type: static int
- Signature: dw_reg_write_swab(void * context,unsigned int reg,unsigned int val)
- Line: 100

### dw_reg_write_word
- Return type: static int
- Signature: dw_reg_write_word(void * context,unsigned int reg,unsigned int val)
- Line: 119

### i2c_dw_acpi_configure
- Return type: static void
- Signature: i2c_dw_acpi_configure(struct device * device)
- Line: 356

### i2c_dw_acpi_configure
- Return type: static void
- Signature: i2c_dw_acpi_configure(struct device * device)
- Line: 304

### i2c_dw_acpi_params
- Return type: static void
- Signature: i2c_dw_acpi_params(struct device * device,char method[],u16 * hcnt,u16 * lcnt,u32 * sda_hold)
- Line: 279

### i2c_dw_acpi_round_bus_speed
- Return type: static u32
- Signature: i2c_dw_acpi_round_bus_speed(struct device * device)
- Line: 358

### i2c_dw_acpi_round_bus_speed
- Return type: static u32
- Signature: i2c_dw_acpi_round_bus_speed(struct device * device)
- Line: 336

### i2c_dw_acquire_lock
- Return type: int
- Signature: i2c_dw_acquire_lock(struct dw_i2c_dev * dev)
- Line: 717

### i2c_dw_adjust_bus_speed
- Return type: static void
- Signature: i2c_dw_adjust_bus_speed(struct dw_i2c_dev * dev)
- Line: 465

### i2c_dw_clk_rate
- Return type: u32
- Signature: i2c_dw_clk_rate(struct dw_i2c_dev * dev)
- Line: 680

### i2c_dw_configure_mode
- Return type: static void
- Signature: i2c_dw_configure_mode(struct dw_i2c_dev * dev,int mode)
- Line: 362

### i2c_dw_disable
- Return type: void
- Signature: i2c_dw_disable(struct dw_i2c_dev * dev)
- Line: 836

### i2c_dw_func
- Return type: u32
- Signature: i2c_dw_func(struct i2c_adapter * adap)
- Line: 829

### i2c_dw_fw_parse_and_configure
- Return type: int
- Signature: i2c_dw_fw_parse_and_configure(struct dw_i2c_dev * dev)
- Line: 482

### i2c_dw_handle_tx_abort
- Return type: int
- Signature: i2c_dw_handle_tx_abort(struct dw_i2c_dev * dev)
- Line: 764

### i2c_dw_init
- Return type: int
- Signature: i2c_dw_init(struct dw_i2c_dev * dev)
- Line: 433

### i2c_dw_init_regmap
- Return type: static int
- Signature: i2c_dw_init_regmap(struct dw_i2c_dev * dev)
- Line: 139

### i2c_dw_isr
- Return type: static irqreturn_t
- Signature: i2c_dw_isr(int this_irq,void * dev_id)
- Line: 856

### i2c_dw_of_configure
- Return type: static void
- Signature: i2c_dw_of_configure(struct device * device)
- Line: 255

### i2c_dw_of_configure
- Return type: static void
- Signature: i2c_dw_of_configure(struct device * device)
- Line: 241

### i2c_dw_prepare
- Return type: static int
- Signature: i2c_dw_prepare(struct device * device)
- Line: 970

### i2c_dw_prepare_clk
- Return type: int
- Signature: i2c_dw_prepare_clk(struct dw_i2c_dev * dev,bool prepare)
- Line: 693

### i2c_dw_probe
- Return type: int
- Signature: i2c_dw_probe(struct dw_i2c_dev * dev)
- Line: 879

### i2c_dw_read_scl_reg
- Return type: static u32
- Signature: i2c_dw_read_scl_reg(struct dw_i2c_dev * dev,u32 reg)
- Line: 512

### i2c_dw_release_lock
- Return type: void
- Signature: i2c_dw_release_lock(struct dw_i2c_dev * dev)
- Line: 733

### i2c_dw_resume
- Return type: static int
- Signature: i2c_dw_resume(struct device * device)
- Line: 1015

### i2c_dw_runtime_resume
- Return type: static int
- Signature: i2c_dw_runtime_resume(struct device * device)
- Line: 1003

### i2c_dw_runtime_suspend
- Return type: static int
- Signature: i2c_dw_runtime_suspend(struct device * device)
- Line: 981

### i2c_dw_scl_hcnt
- Return type: u32
- Signature: i2c_dw_scl_hcnt(struct dw_i2c_dev * dev,unsigned int reg,u32 ic_clk,u32 tSYMBOL,u32 tf,int offset)
- Line: 527

### i2c_dw_scl_lcnt
- Return type: u32
- Signature: i2c_dw_scl_lcnt(struct dw_i2c_dev * dev,unsigned int reg,u32 ic_clk,u32 tLOW,u32 tf,int offset)
- Line: 550

### i2c_dw_set_fifo_size
- Return type: static int
- Signature: i2c_dw_set_fifo_size(struct dw_i2c_dev * dev)
- Line: 787

### i2c_dw_set_mode
- Return type: void
- Signature: i2c_dw_set_mode(struct dw_i2c_dev * dev,int mode)
- Line: 414

### i2c_dw_set_sda_hold
- Return type: static int
- Signature: i2c_dw_set_sda_hold(struct dw_i2c_dev * dev)
- Line: 570

### i2c_dw_suspend
- Return type: static int
- Signature: i2c_dw_suspend(struct device * device)
- Line: 994

### i2c_dw_validate_speed
- Return type: static int
- Signature: i2c_dw_validate_speed(struct dw_i2c_dev * dev)
- Line: 204

### i2c_dw_wait_bus_not_busy
- Return type: int
- Signature: i2c_dw_wait_bus_not_busy(struct dw_i2c_dev * dev)
- Line: 742

### i2c_dw_write_timings
- Return type: static void
- Signature: i2c_dw_write_timings(struct dw_i2c_dev * dev)
- Line: 385

### mscc_twi_set_sda_hold_time
- Return type: static int
- Signature: mscc_twi_set_sda_hold_time(struct dw_i2c_dev * dev)
- Line: 233

## Variables (5)

- static **abort_sources** : const char * const[] (line 42)
- static **i2c_dw_algo** : const struct i2c_algorithm (line 866)
- static **i2c_dw_no_acpi_params** : const struct dmi_system_id[] (line 268)
- static **i2c_dw_quirks** : const struct i2c_adapter_quirks (line 875)
- static **supported_speeds** : const u32[] (line 197)

## Macros (7)

- **DEFAULT_SYMBOL_NAMESPACE** (line 12)
- **DW_IC_ABORT_TIMEOUT_US** (line 39)
- **DW_IC_BUSY_POLL_TIMEOUT_US** (line 40)
- **DW_IC_DEFAULT_BUS_CAPACITANCE_pF** (line 38)
- **MSCC_ICPU_CFG_TWI_DELAY** (line 229)
- **MSCC_ICPU_CFG_TWI_DELAY_ENABLE** (line 230)
- **MSCC_ICPU_CFG_TWI_SPIKE_FILTER** (line 231)
