# drivers/i2c/algos/i2c-algo-pcf.c

Subsystem: drivers/i2c

## Functions (13)

### handle_lab
- Return type: static void
- Signature: handle_lab(struct i2c_algo_pcf_data * adap,const int * status)
- Line: 54

### i2c_pcf_add_bus
- Return type: int
- Signature: i2c_pcf_add_bus(struct i2c_adapter * adap)
- Line: 349

### i2c_repstart
- Return type: static void
- Signature: i2c_repstart(struct i2c_algo_pcf_data * adap)
- Line: 44

### i2c_start
- Return type: static void
- Signature: i2c_start(struct i2c_algo_pcf_data * adap)
- Line: 39

### i2c_stop
- Return type: static void
- Signature: i2c_stop(struct i2c_algo_pcf_data * adap)
- Line: 49

### pcf_func
- Return type: static u32
- Signature: pcf_func(struct i2c_adapter * adap)
- Line: 334

### pcf_init_8584
- Return type: static int
- Signature: pcf_init_8584(struct i2c_algo_pcf_data * adap)
- Line: 132

### pcf_readbytes
- Return type: static int
- Signature: pcf_readbytes(struct i2c_adapter * i2c_adap,char * buf,int count,int last)
- Line: 211

### pcf_send_address
- Return type: static void
- Signature: pcf_send_address(struct i2c_algo_pcf_data * adap,struct i2c_msg * msg)
- Line: 256

### pcf_sendbytes
- Return type: static int
- Signature: pcf_sendbytes(struct i2c_adapter * i2c_adap,const char * buf,int count,int last)
- Line: 180

### pcf_xfer
- Return type: static int
- Signature: pcf_xfer(struct i2c_adapter * i2c_adap,struct i2c_msg * msgs,int num)
- Line: 266

### wait_for_bb
- Return type: static int
- Signature: wait_for_bb(struct i2c_algo_pcf_data * adap)
- Line: 78

### wait_for_pin
- Return type: static int
- Signature: wait_for_pin(struct i2c_algo_pcf_data * adap,int * status)
- Line: 99

## Variables (1)

- static **pcf_algo** : const struct i2c_algorithm (line 341)

## Macros (7)

- **DEF_TIMEOUT** (line 26)
- **get_clock**(adap) (line 33)
- **get_own**(adap) (line 32)
- **get_pcf**(adap,ctl) (line 31)
- **i2c_inb**(adap) (line 35)
- **i2c_outb**(adap,val) (line 34)
- **set_pcf**(adap,ctl,val) (line 30)
