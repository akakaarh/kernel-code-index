# drivers/i2c/busses/i2c-at91-slave.c

Subsystem: drivers/i2c

## Functions (6)

### at91_init_twi_bus_slave
- Return type: void
- Signature: at91_init_twi_bus_slave(struct at91_twi_dev * dev)
- Line: 135

### at91_reg_slave
- Return type: static int
- Signature: at91_reg_slave(struct i2c_client * slave)
- Line: 65

### at91_twi_func
- Return type: static u32
- Signature: at91_twi_func(struct i2c_adapter * adapter)
- Line: 107

### at91_twi_probe_slave
- Return type: int
- Signature: at91_twi_probe_slave(struct platform_device * pdev,u32 phy_addr,struct at91_twi_dev * dev)
- Line: 118

### at91_unreg_slave
- Return type: static int
- Signature: at91_unreg_slave(struct i2c_client * slave)
- Line: 89

### atmel_twi_interrupt_slave
- Return type: static irqreturn_t
- Signature: atmel_twi_interrupt_slave(int irq,void * dev_id)
- Line: 15

## Variables (1)

- static **at91_twi_algorithm_slave** : const struct i2c_algorithm (line 112)
