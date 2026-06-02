# drivers/i2c/busses/i2c-diolan-u2c.c

Subsystem: drivers/i2c

## Functions (21)

### diolan_flush_input
- Return type: static void
- Signature: diolan_flush_input(struct i2c_diolan_u2c * dev)
- Line: 198

### diolan_fw_version
- Return type: static void
- Signature: diolan_fw_version(struct i2c_diolan_u2c * dev)
- Line: 271

### diolan_get_serial
- Return type: static void
- Signature: diolan_get_serial(struct i2c_diolan_u2c * dev)
- Line: 283

### diolan_i2c_get_byte_ack
- Return type: static int
- Signature: diolan_i2c_get_byte_ack(struct i2c_diolan_u2c * dev,bool ack,u8 * byte)
- Line: 232

### diolan_i2c_put_byte_ack
- Return type: static int
- Signature: diolan_i2c_put_byte_ack(struct i2c_diolan_u2c * dev,u8 byte)
- Line: 246

### diolan_i2c_repeated_start
- Return type: static int
- Signature: diolan_i2c_repeated_start(struct i2c_diolan_u2c * dev)
- Line: 222

### diolan_i2c_start
- Return type: static int
- Signature: diolan_i2c_start(struct i2c_diolan_u2c * dev)
- Line: 217

### diolan_i2c_stop
- Return type: static int
- Signature: diolan_i2c_stop(struct i2c_diolan_u2c * dev)
- Line: 227

### diolan_init
- Return type: static int
- Signature: diolan_init(struct i2c_diolan_u2c * dev)
- Line: 296

### diolan_set_clock_synch
- Return type: static int
- Signature: diolan_set_clock_synch(struct i2c_diolan_u2c * dev,bool enable)
- Line: 257

### diolan_set_clock_synch_timeout
- Return type: static int
- Signature: diolan_set_clock_synch_timeout(struct i2c_diolan_u2c * dev,int ms)
- Line: 263

### diolan_set_speed
- Return type: static int
- Signature: diolan_set_speed(struct i2c_diolan_u2c * dev,u8 speed)
- Line: 251

### diolan_u2c_disconnect
- Return type: static void
- Signature: diolan_u2c_disconnect(struct usb_interface * interface)
- Line: 490

### diolan_u2c_probe
- Return type: static int
- Signature: diolan_u2c_probe(struct usb_interface * interface,const struct usb_device_id * id)
- Line: 430

### diolan_usb_cmd
- Return type: static int
- Signature: diolan_usb_cmd(struct i2c_diolan_u2c * dev,u8 command,bool flush)
- Line: 164

### diolan_usb_cmd_data
- Return type: static int
- Signature: diolan_usb_cmd_data(struct i2c_diolan_u2c * dev,u8 command,u8 data,bool flush)
- Line: 172

### diolan_usb_cmd_data2
- Return type: static int
- Signature: diolan_usb_cmd_data2(struct i2c_diolan_u2c * dev,u8 command,u8 d1,u8 d2,bool flush)
- Line: 182

### diolan_usb_func
- Return type: static u32
- Signature: diolan_usb_func(struct i2c_adapter * a)
- Line: 410

### diolan_usb_transfer
- Return type: static int
- Signature: diolan_usb_transfer(struct i2c_diolan_u2c * dev)
- Line: 96

### diolan_usb_xfer
- Return type: static int
- Signature: diolan_usb_xfer(struct i2c_adapter * adapter,struct i2c_msg * msgs,int num)
- Line: 339

### diolan_write_cmd
- Return type: static int
- Signature: diolan_write_cmd(struct i2c_diolan_u2c * dev,bool flush)
- Line: 156

## Structs (1)

### i2c_diolan_u2c
- Line: 77
- Members:
  - obuffer: u8[]
  - ibuffer: u8[]
  - ep_in: int
  - ep_out: int
  - usb_dev: usb_device *
  - interface: usb_interface *
  - adapter: i2c_adapter
  - olen: int
  - ocount: int

## Variables (4)

- static **diolan_u2c_driver** : usb_driver (line 501)
- static **diolan_u2c_table** : const struct usb_device_id[] (line 423)
- static **diolan_usb_algorithm** : const struct i2c_algorithm (line 416)
- static **frequency** : uint (line 88)

## Macros (46)

- **CMD_GET_FW_VERSION** (line 36)
- **CMD_GET_SERIAL** (line 37)
- **CMD_I2C_DROP_SCL** (line 33)
- **CMD_I2C_DROP_SDA** (line 32)
- **CMD_I2C_GET_ACK** (line 44)
- **CMD_I2C_GET_BYTE** (line 42)
- **CMD_I2C_GET_BYTE_ACK** (line 46)
- **CMD_I2C_GET_CLK_SYNC** (line 50)
- **CMD_I2C_GET_CLK_SYNC_TO** (line 52)
- **CMD_I2C_GET_SPEED** (line 48)
- **CMD_I2C_PUT_ACK** (line 43)
- **CMD_I2C_PUT_BYTE** (line 41)
- **CMD_I2C_PUT_BYTE_ACK** (line 45)
- **CMD_I2C_READ** (line 27)
- **CMD_I2C_READ_SCL** (line 35)
- **CMD_I2C_READ_SDA** (line 34)
- **CMD_I2C_RELEASE_SCL** (line 31)
- **CMD_I2C_RELEASE_SDA** (line 30)
- **CMD_I2C_REPEATED_START** (line 40)
- **CMD_I2C_SCAN** (line 29)
- **CMD_I2C_SET_CLK_SYNC** (line 49)
- **CMD_I2C_SET_CLK_SYNC_TO** (line 51)
- **CMD_I2C_SET_SPEED** (line 47)
- **CMD_I2C_START** (line 38)
- **CMD_I2C_STOP** (line 39)
- **CMD_I2C_WRITE** (line 28)
- **DIOLAN_FLUSH_LEN** (line 73)
- **DIOLAN_INBUF_LEN** (line 74)
- **DIOLAN_OUTBUF_LEN** (line 72)
- **DIOLAN_SYNC_TIMEOUT** (line 70)
- **DIOLAN_USB_TIMEOUT** (line 69)
- **DRIVER_NAME** (line 20)
- **RESP_BAD_MEMADDR** (line 56)
- **RESP_DATA_ERR** (line 57)
- **RESP_FAILED** (line 55)
- **RESP_NACK** (line 59)
- **RESP_NOT_IMPLEMENTED** (line 58)
- **RESP_OK** (line 54)
- **RESP_TIMEOUT** (line 60)
- **U2C_I2C_FREQ**(s) (line 67)
- **U2C_I2C_SPEED**(f) (line 65)
- **U2C_I2C_SPEED_2KHZ** (line 64)
- **U2C_I2C_SPEED_FAST** (line 62)
- **U2C_I2C_SPEED_STD** (line 63)
- **USB_DEVICE_ID_DIOLAN_U2C** (line 23)
- **USB_VENDOR_ID_DIOLAN** (line 22)
