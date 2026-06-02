# drivers/i2c/i2c-core-smbus.c

Subsystem: drivers/i2c

## Functions (22)

### __i2c_smbus_xfer
- Return type: s32
- Signature: __i2c_smbus_xfer(struct i2c_adapter * adapter,u16 addr,unsigned short flags,char read_write,u8 command,int protocol,union i2c_smbus_data * data)
- Line: 555

### crc8
- Return type: static u8
- Signature: crc8(u16 data)
- Line: 30

### i2c_new_smbus_alert_device
- Return type: i2c_client *
- Signature: i2c_new_smbus_alert_device(struct i2c_adapter * adapter,struct i2c_smbus_alert_setup * setup)
- Line: 707

### i2c_setup_smbus_alert
- Return type: int
- Signature: i2c_setup_smbus_alert(struct i2c_adapter * adapter)
- Line: 720

### i2c_smbus_add_pec
- Return type: static void
- Signature: i2c_smbus_add_pec(struct i2c_msg * msg)
- Line: 72

### i2c_smbus_check_pec
- Return type: static int
- Signature: i2c_smbus_check_pec(u8 cpec,struct i2c_msg * msg)
- Line: 83

### i2c_smbus_msg_pec
- Return type: static u8
- Signature: i2c_smbus_msg_pec(u8 pec,struct i2c_msg * msg)
- Line: 61

### i2c_smbus_pec
- Return type: u8
- Signature: i2c_smbus_pec(u8 crc,u8 * p,size_t count)
- Line: 50

### i2c_smbus_read_block_data
- Return type: s32
- Signature: i2c_smbus_read_block_data(const struct i2c_client * client,u8 command,u8 * values)
- Line: 225

### i2c_smbus_read_byte
- Return type: s32
- Signature: i2c_smbus_read_byte(const struct i2c_client * client)
- Line: 103

### i2c_smbus_read_byte_data
- Return type: s32
- Signature: i2c_smbus_read_byte_data(const struct i2c_client * client,u8 command)
- Line: 138

### i2c_smbus_read_i2c_block_data
- Return type: s32
- Signature: i2c_smbus_read_i2c_block_data(const struct i2c_client * client,u8 command,u8 length,u8 * values)
- Line: 268

### i2c_smbus_read_i2c_block_data_or_emulated
- Return type: s32
- Signature: i2c_smbus_read_i2c_block_data_or_emulated(const struct i2c_client * client,u8 command,u8 length,u8 * values)
- Line: 654

### i2c_smbus_read_word_data
- Return type: s32
- Signature: i2c_smbus_read_word_data(const struct i2c_client * client,u8 command)
- Line: 178

### i2c_smbus_try_get_dmabuf
- Return type: static void
- Signature: i2c_smbus_try_get_dmabuf(struct i2c_msg * msg,u8 init_val)
- Line: 303

### i2c_smbus_write_block_data
- Return type: s32
- Signature: i2c_smbus_write_block_data(const struct i2c_client * client,u8 command,u8 length,const u8 * values)
- Line: 252

### i2c_smbus_write_byte
- Return type: s32
- Signature: i2c_smbus_write_byte(const struct i2c_client * client,u8 value)
- Line: 123

### i2c_smbus_write_byte_data
- Return type: s32
- Signature: i2c_smbus_write_byte_data(const struct i2c_client * client,u8 command,u8 value)
- Line: 159

### i2c_smbus_write_i2c_block_data
- Return type: s32
- Signature: i2c_smbus_write_i2c_block_data(const struct i2c_client * client,u8 command,u8 length,const u8 * values)
- Line: 288

### i2c_smbus_write_word_data
- Return type: s32
- Signature: i2c_smbus_write_word_data(const struct i2c_client * client,u8 command,u16 value)
- Line: 199

### i2c_smbus_xfer
- Return type: s32
- Signature: i2c_smbus_xfer(struct i2c_adapter * adapter,u16 addr,unsigned short flags,char read_write,u8 command,int protocol,union i2c_smbus_data * data)
- Line: 537

### i2c_smbus_xfer_emulated
- Return type: static s32
- Signature: i2c_smbus_xfer_emulated(struct i2c_adapter * adapter,u16 addr,unsigned short flags,char read_write,u8 command,int size,union i2c_smbus_data * data)
- Line: 323

## Macros (2)

- **CREATE_TRACE_POINTS** (line 23)
- **POLY** (line 29)
