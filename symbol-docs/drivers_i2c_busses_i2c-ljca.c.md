# drivers/i2c/busses/i2c-ljca.c

Subsystem: drivers/i2c

## Functions (11)

### ljca_i2c_func
- Return type: static u32
- Signature: ljca_i2c_func(struct i2c_adapter * adap)
- Line: 257

### ljca_i2c_init
- Return type: static int
- Signature: ljca_i2c_init(struct ljca_i2c_dev * ljca_i2c,u8 id)
- Line: 63

### ljca_i2c_probe
- Return type: static int
- Signature: ljca_i2c_probe(struct auxiliary_device * auxdev,const struct auxiliary_device_id * aux_dev_id)
- Line: 273

### ljca_i2c_pure_read
- Return type: static int
- Signature: ljca_i2c_pure_read(struct ljca_i2c_dev * ljca_i2c,u8 * data,u8 len)
- Line: 140

### ljca_i2c_pure_write
- Return type: static int
- Signature: ljca_i2c_pure_write(struct ljca_i2c_dev * ljca_i2c,u8 * data,u8 len)
- Line: 186

### ljca_i2c_read
- Return type: static int
- Signature: ljca_i2c_read(struct ljca_i2c_dev * ljca_i2c,u8 target_addr,u8 * data,u8 len)
- Line: 172

### ljca_i2c_remove
- Return type: static void
- Signature: ljca_i2c_remove(struct auxiliary_device * auxdev)
- Line: 318

### ljca_i2c_start
- Return type: static int
- Signature: ljca_i2c_start(struct ljca_i2c_dev * ljca_i2c,u8 target_addr,enum ljca_xfer_type type)
- Line: 79

### ljca_i2c_stop
- Return type: static void
- Signature: ljca_i2c_stop(struct ljca_i2c_dev * ljca_i2c)
- Line: 110

### ljca_i2c_write
- Return type: static int
- Signature: ljca_i2c_write(struct ljca_i2c_dev * ljca_i2c,u8 target_addr,u8 * data,u8 len)
- Line: 216

### ljca_i2c_xfer
- Return type: static int
- Signature: ljca_i2c_xfer(struct i2c_adapter * adapter,struct i2c_msg * msg,int num)
- Line: 230

## Structs (2)

### ljca_i2c_dev
- Line: 54
- Members:
  - id: u8
  - len: __le16
  - ljca: ljca_client *
  - i2c_info: ljca_i2c_info *
  - adap: i2c_adapter
  - obuf: u8[]
  - ibuf: u8[]

### ljca_i2c_rw_packet
- Line: 48
- Members:
  - id: u8
  - len: __le16
  - ljca: ljca_client *
  - i2c_info: ljca_i2c_info *
  - adap: i2c_adapter
  - obuf: u8[]
  - ibuf: u8[]

## Enums (2)

### ljca_i2c_cmd
- Line: 33

### ljca_xfer_type
- Line: 42

## Variables (5)

- **__packed** : ljca_i2c_rw_packet (line 52)
- static **ljca_i2c_algo** : const struct i2c_algorithm (line 268)
- static **ljca_i2c_driver** : auxiliary_driver (line 331)
- static **ljca_i2c_id_table** : const struct auxiliary_device_id[] (line 325)
- static **ljca_i2c_quirks** : const struct i2c_adapter_quirks (line 262)

## Macros (10)

- **LJCA_I2C_BUF_SIZE** (line 29)
- **LJCA_I2C_INIT_FLAG_ADDR_16BIT** (line 22)
- **LJCA_I2C_INIT_FLAG_FREQ** (line 24)
- **LJCA_I2C_INIT_FLAG_FREQ_100K** (line 25)
- **LJCA_I2C_INIT_FLAG_FREQ_1M** (line 27)
- **LJCA_I2C_INIT_FLAG_FREQ_400K** (line 26)
- **LJCA_I2C_INIT_FLAG_MODE** (line 18)
- **LJCA_I2C_INIT_FLAG_MODE_INTERRUPT** (line 20)
- **LJCA_I2C_INIT_FLAG_MODE_POLLING** (line 19)
- **LJCA_I2C_MAX_XFER_SIZE** (line 30)
