# drivers/i2c/busses/i2c-at91-master.c

Subsystem: drivers/i2c

## Functions (18)

### at91_calc_twi_clock
- Return type: static void
- Signature: at91_calc_twi_clock(struct at91_twi_dev * dev)
- Line: 67

### at91_do_twi_transfer
- Return type: static int
- Signature: at91_do_twi_transfer(struct at91_twi_dev * dev)
- Line: 476

### at91_init_twi_bus_master
- Return type: void
- Signature: at91_init_twi_bus_master(struct at91_twi_dev * dev)
- Line: 33

### at91_init_twi_recovery_gpio
- Return type: static int
- Signature: at91_init_twi_recovery_gpio(struct platform_device * pdev,struct at91_twi_dev * dev)
- Line: 827

### at91_init_twi_recovery_info
- Return type: static int
- Signature: at91_init_twi_recovery_info(struct platform_device * pdev,struct at91_twi_dev * dev)
- Line: 866

### at91_twi_configure_dma
- Return type: static int
- Signature: at91_twi_configure_dma(struct at91_twi_dev * dev,u32 phy_addr)
- Line: 745

### at91_twi_dma_cleanup
- Return type: static void
- Signature: at91_twi_dma_cleanup(struct at91_twi_dev * dev)
- Line: 133

### at91_twi_func
- Return type: static u32
- Signature: at91_twi_func(struct i2c_adapter * adapter)
- Line: 734

### at91_twi_probe_master
- Return type: int
- Signature: at91_twi_probe_master(struct platform_device * pdev,u32 phy_addr,struct at91_twi_dev * dev)
- Line: 881

### at91_twi_read_data_dma
- Return type: static void
- Signature: at91_twi_read_data_dma(struct at91_twi_dev * dev)
- Line: 333

### at91_twi_read_data_dma_callback
- Return type: static void
- Signature: at91_twi_read_data_dma_callback(void * data)
- Line: 316

### at91_twi_read_next_byte
- Return type: static void
- Signature: at91_twi_read_next_byte(struct at91_twi_dev * dev)
- Line: 272

### at91_twi_recover_bus_cmd
- Return type: static int
- Signature: at91_twi_recover_bus_cmd(struct i2c_adapter * adap)
- Line: 846

### at91_twi_write_data_dma
- Return type: static void
- Signature: at91_twi_write_data_dma(struct at91_twi_dev * dev)
- Line: 194

### at91_twi_write_data_dma_callback
- Return type: static void
- Signature: at91_twi_write_data_dma_callback(void * data)
- Line: 175

### at91_twi_write_next_byte
- Return type: static void
- Signature: at91_twi_write_next_byte(struct at91_twi_dev * dev)
- Line: 155

### at91_twi_xfer
- Return type: static int
- Signature: at91_twi_xfer(struct i2c_adapter * adap,struct i2c_msg * msg,int num)
- Line: 651

### atmel_twi_interrupt
- Return type: static irqreturn_t
- Signature: atmel_twi_interrupt(int irq,void * dev_id)
- Line: 390

## Variables (2)

- static **at91_twi_algorithm** : const struct i2c_algorithm (line 740)
- static **at91_twi_quirks** : const struct i2c_adapter_quirks (line 729)
