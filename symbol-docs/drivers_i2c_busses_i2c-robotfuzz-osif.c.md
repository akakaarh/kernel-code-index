# drivers/i2c/busses/i2c-robotfuzz-osif.c

Subsystem: drivers/i2c

## Functions (6)

### osif_disconnect
- Return type: static void
- Signature: osif_disconnect(struct usb_interface * interface)
- Line: 180

### osif_func
- Return type: static u32
- Signature: osif_func(struct i2c_adapter * adapter)
- Line: 109

### osif_probe
- Return type: static int
- Signature: osif_probe(struct usb_interface * interface,const struct usb_device_id * id)
- Line: 133

### osif_usb_read
- Return type: static int
- Signature: osif_usb_read(struct i2c_adapter * adapter,int cmd,int value,int index,void * data,int len)
- Line: 36

### osif_usb_write
- Return type: static int
- Signature: osif_usb_write(struct i2c_adapter * adapter,int cmd,int value,int index,void * data,int len)
- Line: 46

### osif_xfer
- Return type: static int
- Signature: osif_xfer(struct i2c_adapter * adapter,struct i2c_msg * msgs,int num)
- Line: 57

## Structs (1)

### osif_priv
- Line: 29
- Members:
  - usb_dev: usb_device *
  - interface: usb_interface *
  - adapter: i2c_adapter
  - status: unsigned char

## Variables (4)

- static **osif_algorithm** : const struct i2c_algorithm (line 119)
- static **osif_driver** : usb_driver (line 188)
- static **osif_quirks** : const struct i2c_adapter_quirks (line 115)
- static **osif_table** : const struct usb_device_id[] (line 127)

## Macros (9)

- **OSIFI2C_READ** (line 20)
- **OSIFI2C_SET_BIT_RATE** (line 24)
- **OSIFI2C_STATUS** (line 23)
- **OSIFI2C_STOP** (line 22)
- **OSIFI2C_WRITE** (line 21)
- **STATUS_ADDRESS_ACK** (line 26)
- **STATUS_ADDRESS_NAK** (line 27)
- **USB_OSIF_PRODUCT_ID** (line 125)
- **USB_OSIF_VENDOR_ID** (line 124)
