# drivers/i2c/busses/i2c-nct6694.c

Subsystem: drivers/i2c

## Functions (5)

### nct6694_i2c_func
- Return type: static u32
- Signature: nct6694_i2c_func(struct i2c_adapter * adapter)
- Line: 104

### nct6694_i2c_ida_free
- Return type: static void
- Signature: nct6694_i2c_ida_free(void * d)
- Line: 137

### nct6694_i2c_probe
- Return type: static int
- Signature: nct6694_i2c_probe(struct platform_device * pdev)
- Line: 145

### nct6694_i2c_set_baudrate
- Return type: static int
- Signature: nct6694_i2c_set_baudrate(struct nct6694_i2c_data * data)
- Line: 119

### nct6694_i2c_xfer
- Return type: static int
- Signature: nct6694_i2c_xfer(struct i2c_adapter * adap,struct i2c_msg * msgs,int num)
- Line: 65

## Structs (2)

### nct6694_i2c_data
- Line: 56
- Members:
  - port: u8
  - br: u8
  - addr: u8
  - w_cnt: u8
  - r_cnt: u8
  - rsv: u8[11]
  - write_data: u8[]
  - read_data: u8[]
  - dev: device *
  - nct6694: nct6694 *
  - adapter: i2c_adapter
  - deliver: nct6694_i2c_deliver
  - port: unsigned char
  - br: unsigned char

### nct6694_i2c_deliver
- Line: 45
- Members:
  - port: u8
  - br: u8
  - addr: u8
  - w_cnt: u8
  - r_cnt: u8
  - rsv: u8[11]
  - write_data: u8[]
  - read_data: u8[]
  - dev: device *
  - nct6694: nct6694 *
  - adapter: i2c_adapter
  - deliver: nct6694_i2c_deliver
  - port: unsigned char
  - br: unsigned char

## Enums (1)

### nct6694_i2c_baudrate
- Line: 35

## Variables (4)

- static **br_reg** : unsigned char[] (line 29)
- static **nct6694_i2c_algo** : const struct i2c_algorithm (line 114)
- static **nct6694_i2c_driver** : platform_driver (line 184)
- static **nct6694_i2c_quirks** : const struct i2c_adapter_quirks (line 109)

## Macros (5)

- **NCT6694_I2C_DELIVER** (line 23)
- **NCT6694_I2C_DELIVER_SEL** (line 24)
- **NCT6694_I2C_MAX_DEVS** (line 27)
- **NCT6694_I2C_MAX_XFER_SIZE** (line 26)
- **NCT6694_I2C_MOD** (line 20)
