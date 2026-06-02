# drivers/i2c/busses/i2c-designware-slave.c

Subsystem: drivers/i2c

## Functions (5)

### i2c_dw_configure_slave
- Return type: void
- Signature: i2c_dw_configure_slave(struct dw_i2c_dev * dev)
- Line: 179

### i2c_dw_isr_slave
- Return type: irqreturn_t
- Signature: i2c_dw_isr_slave(struct dw_i2c_dev * dev)
- Line: 115

### i2c_dw_read_clear_intrbits_slave
- Return type: static u32
- Signature: i2c_dw_read_clear_intrbits_slave(struct dw_i2c_dev * dev)
- Line: 64

### i2c_dw_reg_slave
- Return type: int
- Signature: i2c_dw_reg_slave(struct i2c_client * slave)
- Line: 24

### i2c_dw_unreg_slave
- Return type: int
- Signature: i2c_dw_unreg_slave(struct i2c_client * slave)
- Line: 50

## Macros (1)

- **DEFAULT_SYMBOL_NAMESPACE** (line 10)
