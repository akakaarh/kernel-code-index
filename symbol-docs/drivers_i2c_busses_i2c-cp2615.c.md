# drivers/i2c/busses/i2c-cp2615.c

Subsystem: drivers/i2c

## Functions (10)

### cp2615_check_iop
- Return type: static int
- Signature: cp2615_check_iop(struct usb_interface * usbif)
- Line: 172

### cp2615_check_status
- Return type: static int
- Signature: cp2615_check_status(enum cp2615_i2c_status status)
- Line: 102

### cp2615_i2c_disconnect
- Return type: static void
- Signature: cp2615_i2c_disconnect(struct usb_interface * usbif)
- Line: 273

### cp2615_i2c_func
- Return type: static u32
- Signature: cp2615_i2c_func(struct i2c_adapter * adap)
- Line: 247

### cp2615_i2c_probe
- Return type: static int
- Signature: cp2615_i2c_probe(struct usb_interface * usbif,const struct usb_device_id * id)
- Line: 282

### cp2615_i2c_recv
- Return type: static int
- Signature: cp2615_i2c_recv(struct usb_interface * usbif,unsigned char tag,void * buf)
- Line: 139

### cp2615_i2c_send
- Return type: static int
- Signature: cp2615_i2c_send(struct usb_interface * usbif,struct cp2615_i2c_transfer * i2c_w)
- Line: 125

### cp2615_i2c_xfer
- Return type: static int
- Signature: cp2615_i2c_xfer(struct i2c_adapter * adap,struct i2c_msg * msgs,int num)
- Line: 214

### cp2615_init_i2c_msg
- Return type: static int
- Signature: cp2615_init_i2c_msg(struct cp2615_iop_msg * ret,const struct cp2615_i2c_transfer * data)
- Line: 96

### cp2615_init_iop_msg
- Return type: static int
- Signature: cp2615_init_iop_msg(struct cp2615_iop_msg * ret,enum cp2615_iop_msg_type msg,const void * data,size_t data_len)
- Line: 79

## Structs (4)

### cp2615_i2c_transfer
- Line: 52
- Members:
  - length: __be16
  - msg: __be16
  - preamble: __be16
  - data: u8[]
  - option_id: __be16
  - part_id: __be16
  - proto_ver: __be16
  - i2caddr: u8
  - read_len: u8
  - tag: u8
  - write_len: u8
  - data: u8[]
  - i2caddr: u8
  - tag: u8
  - status: s8
  - read_len: u8
  - data: u8[]

### cp2615_i2c_transfer_result
- Line: 72
- Members:
  - length: __be16
  - msg: __be16
  - preamble: __be16
  - data: u8[]
  - option_id: __be16
  - part_id: __be16
  - proto_ver: __be16
  - i2caddr: u8
  - read_len: u8
  - tag: u8
  - write_len: u8
  - data: u8[]
  - i2caddr: u8
  - tag: u8
  - status: s8
  - read_len: u8
  - data: u8[]

### cp2615_iop_accessory_info
- Line: 48
- Members:
  - length: __be16
  - msg: __be16
  - preamble: __be16
  - data: u8[]
  - option_id: __be16
  - part_id: __be16
  - proto_ver: __be16
  - i2caddr: u8
  - read_len: u8
  - tag: u8
  - write_len: u8
  - data: u8[]
  - i2caddr: u8
  - tag: u8
  - status: s8
  - read_len: u8
  - data: u8[]

### cp2615_iop_msg
- Line: 40
- Members:
  - length: __be16
  - msg: __be16
  - preamble: __be16
  - data: u8[]
  - option_id: __be16
  - part_id: __be16
  - proto_ver: __be16
  - i2caddr: u8
  - read_len: u8
  - tag: u8
  - write_len: u8
  - data: u8[]
  - i2caddr: u8
  - tag: u8
  - status: s8
  - read_len: u8
  - data: u8[]

## Enums (2)

### cp2615_i2c_status
- Line: 58

### cp2615_iop_msg_type
- Line: 29

## Variables (4)

- static **cp2615_i2c_algo** : const struct i2c_algorithm (line 252)
- static **cp2615_i2c_driver** : usb_driver (line 327)
- static **cp2615_i2c_quirks** : i2c_adapter_quirks (line 265)
- static **id_table** : const struct usb_device_id[] (line 320)

## Macros (11)

- **CP2615_PID** (line 18)
- **CP2615_VID** (line 17)
- **IOP_ALTSETTING** (line 23)
- **IOP_EP_IN** (line 20)
- **IOP_EP_OUT** (line 21)
- **IOP_IFN** (line 22)
- **MAX_I2C_SIZE** (line 27)
- **MAX_IOP_PAYLOAD_SIZE** (line 26)
- **MAX_IOP_SIZE** (line 25)
- **PART_ID_A01** (line 45)
- **PART_ID_A02** (line 46)
