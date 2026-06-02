# drivers/i2c/i2c-slave-eeprom.c

Subsystem: drivers/i2c

## Functions (6)

### i2c_slave_eeprom_bin_read
- Return type: static ssize_t
- Signature: i2c_slave_eeprom_bin_read(struct file * filp,struct kobject * kobj,const struct bin_attribute * attr,char * buf,loff_t off,size_t count)
- Line: 93

### i2c_slave_eeprom_bin_write
- Return type: static ssize_t
- Signature: i2c_slave_eeprom_bin_write(struct file * filp,struct kobject * kobj,const struct bin_attribute * attr,char * buf,loff_t off,size_t count)
- Line: 108

### i2c_slave_eeprom_probe
- Return type: static int
- Signature: i2c_slave_eeprom_probe(struct i2c_client * client)
- Line: 143

### i2c_slave_eeprom_remove
- Return type: static void
- Signature: i2c_slave_eeprom_remove(struct i2c_client * client)
- Line: 185

### i2c_slave_eeprom_slave_cb
- Return type: static int
- Signature: i2c_slave_eeprom_slave_cb(struct i2c_client * client,enum i2c_slave_event event,u8 * val)
- Line: 45

### i2c_slave_init_eeprom_data
- Return type: static int
- Signature: i2c_slave_init_eeprom_data(struct eeprom_data * eeprom,struct i2c_client * client,unsigned int size)
- Line: 123

## Structs (1)

### eeprom_data
- Line: 29
- Members:
  - bin: bin_attribute
  - buffer_lock: spinlock_t
  - buffer_idx: u16
  - address_mask: u16
  - num_address_bytes: u8
  - idx_write_cnt: u8
  - read_only: bool
  - buffer: u8[]

## Variables (2)

- static **i2c_slave_eeprom_driver** : i2c_driver (line 206)
- static **i2c_slave_eeprom_id** : const struct i2c_device_id[] (line 193)

## Macros (4)

- **I2C_SLAVE_BYTELEN** (line 40)
- **I2C_SLAVE_DEVICE_MAGIC**(_len,_flags) (line 43)
- **I2C_SLAVE_FLAG_ADDR16** (line 41)
- **I2C_SLAVE_FLAG_RO** (line 42)
