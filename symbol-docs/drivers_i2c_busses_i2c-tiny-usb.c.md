# drivers/i2c/busses/i2c-tiny-usb.c

Subsystem: drivers/i2c

## Functions (6)

### i2c_tiny_usb_disconnect
- Return type: static void
- Signature: i2c_tiny_usb_disconnect(struct usb_interface * interface)
- Line: 279

### i2c_tiny_usb_probe
- Return type: static int
- Signature: i2c_tiny_usb_probe(struct usb_interface * interface,const struct usb_device_id * id)
- Line: 216

### usb_func
- Return type: static u32
- Signature: usb_func(struct i2c_adapter * adapter)
- Line: 121

### usb_read
- Return type: static int
- Signature: usb_read(struct i2c_adapter * adapter,int cmd,int value,int index,void * data,int len)
- Line: 177

### usb_write
- Return type: static int
- Signature: usb_write(struct i2c_adapter * adapter,int cmd,int value,int index,void * data,int len)
- Line: 197

### usb_xfer
- Return type: static int
- Signature: usb_xfer(struct i2c_adapter * adapter,struct i2c_msg * msgs,int num)
- Line: 52

## Structs (1)

### i2c_tiny_usb
- Line: 171
- Members:
  - usb_dev: usb_device *
  - interface: usb_interface *
  - adapter: i2c_adapter

## Variables (5)

- static **delay** : unsigned short (line 35)
- static **i2c_tiny_usb_driver** : usb_driver (line 290)
- static **i2c_tiny_usb_table** : const struct usb_device_id[] (line 162)
- static **usb_algorithm** : const struct i2c_algorithm (line 148)
- static **usb_quirks** : const struct i2c_adapter_quirks (line 143)

## Macros (10)

- **CMD_ECHO** (line 23)
- **CMD_GET_FUNC** (line 24)
- **CMD_GET_STATUS** (line 26)
- **CMD_I2C_IO** (line 28)
- **CMD_I2C_IO_BEGIN** (line 29)
- **CMD_I2C_IO_END** (line 30)
- **CMD_SET_DELAY** (line 25)
- **STATUS_ADDRESS_ACK** (line 49)
- **STATUS_ADDRESS_NAK** (line 50)
- **STATUS_IDLE** (line 48)
