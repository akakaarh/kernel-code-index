# drivers/i2c/algos/i2c-algo-bit.c

Subsystem: drivers/i2c

## Functions (21)

### __i2c_bit_add_bus
- Return type: static int
- Signature: __i2c_bit_add_bus(struct i2c_adapter * adap,int (* add_adapter)(struct i2c_adapter *))
- Line: 635

### acknak
- Return type: static int
- Signature: acknak(struct i2c_adapter * i2c_adap,int is_ack)
- Line: 385

### bit_doAddress
- Return type: static int
- Signature: bit_doAddress(struct i2c_adapter * i2c_adap,struct i2c_msg * msg)
- Line: 466

### bit_func
- Return type: static u32
- Signature: bit_func(struct i2c_adapter * adap)
- Line: 612

### bit_xfer
- Return type: static int
- Signature: bit_xfer(struct i2c_adapter * i2c_adap,struct i2c_msg msgs[],int num)
- Line: 520

### bit_xfer_atomic
- Return type: static int
- Signature: bit_xfer_atomic(struct i2c_adapter * i2c_adap,struct i2c_msg msgs[],int num)
- Line: 601

### i2c_bit_add_bus
- Return type: int
- Signature: i2c_bit_add_bus(struct i2c_adapter * adap)
- Line: 674

### i2c_bit_add_numbered_bus
- Return type: int
- Signature: i2c_bit_add_numbered_bus(struct i2c_adapter * adap)
- Line: 680

### i2c_inb
- Return type: static int
- Signature: i2c_inb(struct i2c_adapter * i2c_adap)
- Line: 199

### i2c_outb
- Return type: static int
- Signature: i2c_outb(struct i2c_adapter * i2c_adap,unsigned char c)
- Line: 152

### i2c_repstart
- Return type: static void
- Signature: i2c_repstart(struct i2c_algo_bit_data * adap)
- Line: 123

### i2c_start
- Return type: static void
- Signature: i2c_start(struct i2c_algo_bit_data * adap)
- Line: 115

### i2c_stop
- Return type: static void
- Signature: i2c_stop(struct i2c_algo_bit_data * adap)
- Line: 134

### readbytes
- Return type: static int
- Signature: readbytes(struct i2c_adapter * i2c_adap,struct i2c_msg * msg)
- Line: 401

### sclhi
- Return type: static int
- Signature: sclhi(struct i2c_algo_bit_data * adap)
- Line: 75

### scllo
- Return type: static void
- Signature: scllo(struct i2c_algo_bit_data * adap)
- Line: 65

### sdahi
- Return type: static void
- Signature: sdahi(struct i2c_algo_bit_data * adap)
- Line: 59

### sdalo
- Return type: static void
- Signature: sdalo(struct i2c_algo_bit_data * adap)
- Line: 53

### sendbytes
- Return type: static int
- Signature: sendbytes(struct i2c_adapter * i2c_adap,struct i2c_msg * msg)
- Line: 344

### test_bus
- Return type: static int
- Signature: test_bus(struct i2c_adapter * i2c_adap)
- Line: 230

### try_address
- Return type: static int
- Signature: try_address(struct i2c_adapter * i2c_adap,unsigned char addr,int retries)
- Line: 319

## Variables (4)

- static **bit_test** : int (line 35)
- **i2c_bit_algo** : const struct i2c_algorithm (line 621)
- static **i2c_bit_quirk_no_clk_stretch** : const struct i2c_adapter_quirks (line 628)
- static **i2c_debug** : int (line 40)

## Macros (6)

- **bit_dbg**(level,dev,format,args...) (line 23)
- **bit_dbg**(level,dev,format,args...) (line 29)
- **getscl**(adap) (line 51)
- **getsda**(adap) (line 50)
- **setscl**(adap,val) (line 49)
- **setsda**(adap,val) (line 48)
