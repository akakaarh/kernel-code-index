# drivers/i2c/algos/i2c-algo-pca.c

Subsystem: drivers/i2c

## Functions (14)

### i2c_pca_add_bus
- Return type: int
- Signature: i2c_pca_add_bus(struct i2c_adapter * adap)
- Line: 532

### i2c_pca_add_numbered_bus
- Return type: int
- Signature: i2c_pca_add_numbered_bus(struct i2c_adapter * adap)
- Line: 544

### pca_address
- Return type: static int
- Signature: pca_address(struct i2c_algo_pca_data * adap,struct i2c_msg * msg)
- Line: 116

### pca_func
- Return type: static u32
- Signature: pca_func(struct i2c_adapter * adap)
- Line: 358

### pca_init
- Return type: static int
- Signature: pca_init(struct i2c_adapter * adap)
- Line: 391

### pca_probe_chip
- Return type: static unsigned int
- Signature: pca_probe_chip(struct i2c_adapter * adap)
- Line: 368

### pca_repeated_start
- Return type: static int
- Signature: pca_repeated_start(struct i2c_algo_pca_data * adap)
- Line: 83

### pca_reset
- Return type: static void
- Signature: pca_reset(struct i2c_algo_pca_data * adap)
- Line: 35

### pca_rx_ack
- Return type: static int
- Signature: pca_rx_ack(struct i2c_algo_pca_data * adap,int ack)
- Line: 168

### pca_rx_byte
- Return type: static void
- Signature: pca_rx_byte(struct i2c_algo_pca_data * adap,__u8 * b,int ack)
- Line: 156

### pca_start
- Return type: static int
- Signature: pca_start(struct i2c_algo_pca_data * adap)
- Line: 68

### pca_stop
- Return type: static void
- Signature: pca_stop(struct i2c_algo_pca_data * adap)
- Line: 102

### pca_tx_byte
- Return type: static int
- Signature: pca_tx_byte(struct i2c_algo_pca_data * adap,__u8 b)
- Line: 138

### pca_xfer
- Return type: static int
- Signature: pca_xfer(struct i2c_adapter * i2c_adap,struct i2c_msg * msgs,int num)
- Line: 182

## Variables (2)

- static **i2c_debug** : int (line 24)
- static **pca_algo** : const struct i2c_algorithm (line 363)

## Macros (10)

- **DEB1**(fmt,args...) (line 17)
- **DEB2**(fmt,args...) (line 19)
- **DEB3**(fmt,args...) (line 21)
- **pca_clock**(adap) (line 30)
- **pca_get_con**(adap) (line 32)
- **pca_inw**(adap,reg) (line 27)
- **pca_outw**(adap,reg,val) (line 26)
- **pca_set_con**(adap,val) (line 31)
- **pca_status**(adap) (line 29)
- **pca_wait**(adap) (line 33)
