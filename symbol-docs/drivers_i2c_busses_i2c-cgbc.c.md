# drivers/i2c/busses/i2c-cgbc.c

Subsystem: drivers/i2c

## Functions (10)

### cgbc_i2c_freq_to_reg
- Return type: static u8
- Signature: cgbc_i2c_freq_to_reg(unsigned int bus_frequency)
- Line: 89

### cgbc_i2c_func
- Return type: static u32
- Signature: cgbc_i2c_func(struct i2c_adapter * adap)
- Line: 328

### cgbc_i2c_get_status
- Return type: static int
- Signature: cgbc_i2c_get_status(struct i2c_adapter * adap)
- Line: 116

### cgbc_i2c_probe
- Return type: static int
- Signature: cgbc_i2c_probe(struct platform_device * pdev)
- Line: 362

### cgbc_i2c_reg_to_freq
- Return type: static unsigned int
- Signature: cgbc_i2c_reg_to_freq(u8 reg)
- Line: 103

### cgbc_i2c_remove
- Return type: static void
- Signature: cgbc_i2c_remove(struct platform_device * pdev)
- Line: 386

### cgbc_i2c_set_frequency
- Return type: static int
- Signature: cgbc_i2c_set_frequency(struct i2c_adapter * adap,unsigned int bus_frequency)
- Line: 132

### cgbc_i2c_xfer
- Return type: static int
- Signature: cgbc_i2c_xfer(struct i2c_adapter * adap,struct i2c_msg * msgs,int num)
- Line: 300

### cgbc_i2c_xfer_msg
- Return type: static int
- Signature: cgbc_i2c_xfer_msg(struct i2c_adapter * adap)
- Line: 201

### cgbc_i2c_xfer_to_cmd
- Return type: static unsigned int
- Signature: cgbc_i2c_xfer_to_cmd(struct cgbc_i2c_transfer xfer,u8 * cmd)
- Line: 179

## Structs (3)

### cgbc_i2c_data
- Line: 68
- Members:
  - bus_id: u8
  - read_maxtime_us: unsigned long
  - dev: device *
  - cgbc: cgbc_device_data *
  - adap: i2c_adapter
  - msg: i2c_msg *
  - nmsgs: int
  - pos: int
  - state: cgbc_i2c_state
  - bus_id: u8
  - start: bool
  - stop: bool
  - last_ack: bool
  - read: u8
  - write: u8
  - addr: u8
  - data: u8[]

### cgbc_i2c_transfer
- Line: 78
- Members:
  - bus_id: u8
  - read_maxtime_us: unsigned long
  - dev: device *
  - cgbc: cgbc_device_data *
  - adap: i2c_adapter
  - msg: i2c_msg *
  - nmsgs: int
  - pos: int
  - state: cgbc_i2c_state
  - bus_id: u8
  - start: bool
  - stop: bool
  - last_ack: bool
  - read: u8
  - write: u8
  - addr: u8
  - data: u8[]

### i2c_algo_cgbc_data
- Line: 63
- Members:
  - bus_id: u8
  - read_maxtime_us: unsigned long
  - dev: device *
  - cgbc: cgbc_device_data *
  - adap: i2c_adapter
  - msg: i2c_msg *
  - nmsgs: int
  - pos: int
  - state: cgbc_i2c_state
  - bus_id: u8
  - start: bool
  - stop: bool
  - last_ack: bool
  - read: u8
  - write: u8
  - addr: u8
  - data: u8[]

## Enums (1)

### cgbc_i2c_state
- Line: 54

## Variables (4)

- static **cgbc_i2c_adapter** : const struct i2c_adapter[] (line 343)
- static **cgbc_i2c_algo_data** : i2c_algo_cgbc_data[] (line 338)
- static **cgbc_i2c_algorithm** : const struct i2c_algorithm (line 333)
- static **cgbc_i2c_driver** : platform_driver (line 393)

## Macros (23)

- **CGBC_I2C_CMD_DATA** (line 20)
- **CGBC_I2C_CMD_HEADER_SIZE** (line 51)
- **CGBC_I2C_CMD_SIZE** (line 52)
- **CGBC_I2C_CMD_SPEED** (line 21)
- **CGBC_I2C_CMD_START** (line 18)
- **CGBC_I2C_CMD_STAT** (line 19)
- **CGBC_I2C_FREQ_MAX_HZ** (line 39)
- **CGBC_I2C_FREQ_MIN_HZ** (line 38)
- **CGBC_I2C_FREQ_UNIT_100KHZ** (line 43)
- **CGBC_I2C_FREQ_UNIT_10KHZ** (line 42)
- **CGBC_I2C_FREQ_UNIT_1KHZ** (line 41)
- **CGBC_I2C_FREQ_UNIT_MASK** (line 45)
- **CGBC_I2C_FREQ_VALUE_MASK** (line 46)
- **CGBC_I2C_LAST_ACK** (line 30)
- **CGBC_I2C_PM_BUS_ID** (line 16)
- **CGBC_I2C_PRIMARY_BUS_ID** (line 15)
- **CGBC_I2C_READ_MAX_LEN** (line 48)
- **CGBC_I2C_START** (line 27)
- **CGBC_I2C_STAT_BUSY** (line 25)
- **CGBC_I2C_STAT_DAT** (line 24)
- **CGBC_I2C_STAT_IDL** (line 23)
- **CGBC_I2C_STOP** (line 28)
- **CGBC_I2C_WRITE_MAX_LEN** (line 49)
