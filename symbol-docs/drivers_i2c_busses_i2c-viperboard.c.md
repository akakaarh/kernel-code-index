# drivers/i2c/busses/i2c-viperboard.c

Subsystem: drivers/i2c

## Functions (11)

### vprbrd_i2c_addr
- Return type: static int
- Signature: vprbrd_i2c_addr(struct usb_device * usb_dev,struct vprbrd_i2c_addr_msg * amsg)
- Line: 96

### vprbrd_i2c_exit
- Return type: static void __exit
- Signature: vprbrd_i2c_exit(void)
- Line: 453

### vprbrd_i2c_func
- Return type: static u32
- Signature: vprbrd_i2c_func(struct i2c_adapter * i2c)
- Line: 340

### vprbrd_i2c_init
- Return type: static int __init
- Signature: vprbrd_i2c_init(void)
- Line: 420

### vprbrd_i2c_probe
- Return type: static int
- Signature: vprbrd_i2c_probe(struct platform_device * pdev)
- Line: 356

### vprbrd_i2c_read
- Return type: static int
- Signature: vprbrd_i2c_read(struct vprbrd * vb,struct i2c_msg * msg)
- Line: 114

### vprbrd_i2c_receive
- Return type: static int
- Signature: vprbrd_i2c_receive(struct usb_device * usb_dev,struct vprbrd_i2c_read_msg * rmsg,int bytes_xfer)
- Line: 66

### vprbrd_i2c_remove
- Return type: static void
- Signature: vprbrd_i2c_remove(struct platform_device * pdev)
- Line: 407

### vprbrd_i2c_status
- Return type: static int
- Signature: vprbrd_i2c_status(struct i2c_adapter * i2c,struct vprbrd_i2c_status * status,bool prev_error)
- Line: 36

### vprbrd_i2c_write
- Return type: static int
- Signature: vprbrd_i2c_write(struct vprbrd * vb,struct i2c_msg * msg)
- Line: 219

### vprbrd_i2c_xfer
- Return type: static int
- Signature: vprbrd_i2c_xfer(struct i2c_adapter * i2c,struct i2c_msg * msgs,int num)
- Line: 266

## Structs (1)

### vprbrd_i2c
- Line: 24
- Members:
  - i2c: i2c_adapter
  - bus_freq_param: u8

## Variables (5)

- static **i2c_bus_freq** : unsigned int (line 31)
- static **i2c_bus_param** : u8 (line 30)
- static **vprbrd_algorithm** : const struct i2c_algorithm (line 346)
- static **vprbrd_i2c_driver** : platform_driver (line 414)
- static **vprbrd_quirks** : const struct i2c_adapter_quirks (line 351)
