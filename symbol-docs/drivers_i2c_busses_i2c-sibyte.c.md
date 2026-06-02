# drivers/i2c/busses/i2c-sibyte.c

Subsystem: drivers/i2c

## Functions (5)

### bit_func
- Return type: static u32
- Signature: bit_func(struct i2c_adapter * adap)
- Line: 105

### i2c_sibyte_add_bus
- Return type: static int __init
- Signature: i2c_sibyte_add_bus(struct i2c_adapter * i2c_adap,int speed)
- Line: 122

### i2c_sibyte_exit
- Return type: static void __exit
- Signature: i2c_sibyte_exit(void)
- Line: 174

### i2c_sibyte_init
- Return type: static int __init
- Signature: i2c_sibyte_init(void)
- Line: 161

### smbus_xfer
- Return type: static int
- Signature: smbus_xfer(struct i2c_adapter * i2c_adap,u16 addr,unsigned short flags,char read_write,u8 command,int size,union i2c_smbus_data * data)
- Line: 27

## Structs (1)

### i2c_algo_sibyte_data
- Line: 17
- Members:
  - data: void *
  - bus: int
  - reg_base: void *

## Variables (3)

- static **i2c_sibyte_algo** : const struct i2c_algorithm (line 114)
- static **sibyte_board_adapter** : i2c_adapter[2] (line 142)
- static **sibyte_board_data** : i2c_algo_sibyte_data[2] (line 137)

## Macros (1)

- **SMB_CSR**(a,r) (line 24)
