# drivers/i2c/busses/i2c-usbio.c

Subsystem: drivers/i2c

## Functions (8)

### usbio_i2c_func
- Return type: static u32
- Signature: usbio_i2c_func(struct i2c_adapter * adap)
- Line: 205

### usbio_i2c_init
- Return type: static int
- Signature: usbio_i2c_init(struct i2c_adapter * adap,struct i2c_msg * msg)
- Line: 55

### usbio_i2c_probe
- Return type: static int
- Signature: usbio_i2c_probe(struct auxiliary_device * adev,const struct auxiliary_device_id * adev_id)
- Line: 227

### usbio_i2c_read
- Return type: static int
- Signature: usbio_i2c_read(struct i2c_adapter * adap,struct i2c_msg * msg)
- Line: 83

### usbio_i2c_remove
- Return type: static void
- Signature: usbio_i2c_remove(struct auxiliary_device * adev)
- Line: 297

### usbio_i2c_uninit
- Return type: static void
- Signature: usbio_i2c_uninit(struct i2c_adapter * adap,struct i2c_msg * msg)
- Line: 43

### usbio_i2c_write
- Return type: static int
- Signature: usbio_i2c_write(struct i2c_adapter * adap,struct i2c_msg * msg)
- Line: 126

### usbio_i2c_xfer
- Return type: static int
- Signature: usbio_i2c_xfer(struct i2c_adapter * adap,struct i2c_msg * msgs,int num)
- Line: 176

## Structs (1)

### usbio_i2c
- Line: 16
- Members:
  - adap: i2c_adapter
  - adev: auxiliary_device *
  - rwbuf: usbio_i2c_rw *
  - quirks: unsigned long
  - speed: u32
  - txbuf_len: u16
  - rxbuf_len: u16

## Variables (7)

- static **usbio_i2c_acpi_hids** : const struct acpi_device_id[] (line 26)
- static **usbio_i2c_algo** : const struct i2c_algorithm (line 222)
- static **usbio_i2c_driver** : auxiliary_driver (line 310)
- static **usbio_i2c_id_table** : const struct auxiliary_device_id[] (line 304)
- static **usbio_i2c_quirks** : const struct i2c_adapter_quirks (line 210)
- static **usbio_i2c_quirks_max_rw_len52** : const struct i2c_adapter_quirks (line 216)
- static **usbio_i2c_speeds** : const u32[] (line 36)

## Macros (1)

- **I2C_RW_OVERHEAD** (line 14)
