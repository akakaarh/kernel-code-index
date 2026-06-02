# drivers/i2c/busses/i2c-cbus-gpio.c

Subsystem: drivers/i2c

## Functions (9)

### cbus_i2c_func
- Return type: static u32
- Signature: cbus_i2c_func(struct i2c_adapter * adapter)
- Line: 192

### cbus_i2c_probe
- Return type: static int
- Signature: cbus_i2c_probe(struct platform_device * pdev)
- Line: 210

### cbus_i2c_remove
- Return type: static void
- Signature: cbus_i2c_remove(struct platform_device * pdev)
- Line: 203

### cbus_i2c_smbus_xfer
- Return type: static int
- Signature: cbus_i2c_smbus_xfer(struct i2c_adapter * adapter,u16 addr,unsigned short flags,char read_write,u8 command,int size,union i2c_smbus_data * data)
- Line: 167

### cbus_receive_bit
- Return type: static int
- Signature: cbus_receive_bit(struct cbus_host * host)
- Line: 75

### cbus_receive_word
- Return type: static int
- Signature: cbus_receive_word(struct cbus_host * host)
- Line: 89

### cbus_send_bit
- Return type: static void
- Signature: cbus_send_bit(struct cbus_host * host,unsigned bit)
- Line: 50

### cbus_send_data
- Return type: static void
- Signature: cbus_send_data(struct cbus_host * host,unsigned data,unsigned len)
- Line: 63

### cbus_transfer
- Return type: static int
- Signature: cbus_transfer(struct cbus_host * host,char rw,unsigned dev,unsigned reg,unsigned data)
- Line: 114

## Structs (1)

### cbus_host
- Line: 37
- Members:
  - lock: spinlock_t
  - dev: device *
  - clk: gpio_desc *
  - dat: gpio_desc *
  - sel: gpio_desc *

## Variables (3)

- static **cbus_i2c_algo** : const struct i2c_algorithm (line 197)
- static **cbus_i2c_driver** : platform_driver (line 265)
- static **i2c_cbus_dt_ids** : const struct of_device_id[] (line 258)

## Macros (2)

- **CBUS_ADDR_BITS** (line 34)
- **CBUS_REG_BITS** (line 35)
