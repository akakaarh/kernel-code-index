# drivers/i2c/busses/i2c-dln2.c

Subsystem: drivers/i2c

## Functions (7)

### dln2_i2c_enable
- Return type: static int
- Signature: dln2_i2c_enable(struct dln2_i2c * dln2,bool enable)
- Line: 53

### dln2_i2c_func
- Return type: static u32
- Signature: dln2_i2c_func(struct i2c_adapter * a)
- Line: 170

### dln2_i2c_probe
- Return type: static int
- Signature: dln2_i2c_probe(struct platform_device * pdev)
- Line: 187

### dln2_i2c_read
- Return type: static int
- Signature: dln2_i2c_read(struct dln2_i2c * dln2,u16 addr,u8 * data,u16 data_len)
- Line: 101

### dln2_i2c_remove
- Return type: static void
- Signature: dln2_i2c_remove(struct platform_device * pdev)
- Line: 237

### dln2_i2c_write
- Return type: static int
- Signature: dln2_i2c_write(struct dln2_i2c * dln2,u8 addr,u8 * data,u16 data_len)
- Line: 70

### dln2_i2c_xfer
- Return type: static int
- Signature: dln2_i2c_xfer(struct i2c_adapter * adapter,struct i2c_msg * msgs,int num)
- Line: 140

## Structs (5)

### __anon9380ea5a0108
- Line: 56
- Members:
  - pdev: platform_device *
  - adapter: i2c_adapter
  - port: u8
  - buf: void *
  - port: u8
  - port: u8
  - addr: u8
  - mem_addr_len: u8
  - mem_addr: __le32
  - buf_len: __le16
  - buf: u8[]
  - port: u8
  - addr: u8
  - mem_addr_len: u8
  - mem_addr: __le32
  - buf_len: __le16
  - buf_len: __le16
  - buf: u8[]

### __anon9380ea5a0208
- Line: 74
- Members:
  - pdev: platform_device *
  - adapter: i2c_adapter
  - port: u8
  - buf: void *
  - port: u8
  - port: u8
  - addr: u8
  - mem_addr_len: u8
  - mem_addr: __le32
  - buf_len: __le16
  - buf: u8[]
  - port: u8
  - addr: u8
  - mem_addr_len: u8
  - mem_addr: __le32
  - buf_len: __le16
  - buf_len: __le16
  - buf: u8[]

### __anon9380ea5a0308
- Line: 105
- Members:
  - pdev: platform_device *
  - adapter: i2c_adapter
  - port: u8
  - buf: void *
  - port: u8
  - port: u8
  - addr: u8
  - mem_addr_len: u8
  - mem_addr: __le32
  - buf_len: __le16
  - buf: u8[]
  - port: u8
  - addr: u8
  - mem_addr_len: u8
  - mem_addr: __le32
  - buf_len: __le16
  - buf_len: __le16
  - buf: u8[]

### __anon9380ea5a0408
- Line: 112
- Members:
  - pdev: platform_device *
  - adapter: i2c_adapter
  - port: u8
  - buf: void *
  - port: u8
  - port: u8
  - addr: u8
  - mem_addr_len: u8
  - mem_addr: __le32
  - buf_len: __le16
  - buf: u8[]
  - port: u8
  - addr: u8
  - mem_addr_len: u8
  - mem_addr: __le32
  - buf_len: __le16
  - buf_len: __le16
  - buf: u8[]

### dln2_i2c
- Line: 42
- Members:
  - pdev: platform_device *
  - adapter: i2c_adapter
  - port: u8
  - buf: void *
  - port: u8
  - port: u8
  - addr: u8
  - mem_addr_len: u8
  - mem_addr: __le32
  - buf_len: __le16
  - buf: u8[]
  - port: u8
  - addr: u8
  - mem_addr_len: u8
  - mem_addr: __le32
  - buf_len: __le16
  - buf_len: __le16
  - buf: u8[]

## Variables (3)

- static **dln2_i2c_driver** : platform_driver (line 245)
- static **dln2_i2c_quirks** : const struct i2c_adapter_quirks (line 182)
- static **dln2_i2c_usb_algorithm** : const struct i2c_algorithm (line 177)

## Macros (17)

- **DLN2_I2C_BUF_SIZE** (line 40)
- **DLN2_I2C_CMD**(cmd) (line 22)
- **DLN2_I2C_DISABLE** (line 27)
- **DLN2_I2C_ENABLE** (line 26)
- **DLN2_I2C_GET_MAX_REPLY_COUNT** (line 37)
- **DLN2_I2C_GET_PORT_COUNT** (line 25)
- **DLN2_I2C_IS_ENABLED** (line 28)
- **DLN2_I2C_MAX_XFER_SIZE** (line 39)
- **DLN2_I2C_MODULE_ID** (line 21)
- **DLN2_I2C_PULLUP_DISABLE** (line 33)
- **DLN2_I2C_PULLUP_ENABLE** (line 32)
- **DLN2_I2C_PULLUP_IS_ENABLED** (line 34)
- **DLN2_I2C_READ** (line 30)
- **DLN2_I2C_SCAN_DEVICES** (line 31)
- **DLN2_I2C_SET_MAX_REPLY_COUNT** (line 36)
- **DLN2_I2C_TRANSFER** (line 35)
- **DLN2_I2C_WRITE** (line 29)
