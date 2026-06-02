# drivers/i2c/busses/i2c-keba.c

Subsystem: drivers/i2c

## Functions (25)

### ki2c_func
- Return type: static u32
- Signature: ki2c_func(struct i2c_adapter * adap)
- Line: 497

### ki2c_get_scl
- Return type: static int
- Signature: ki2c_get_scl(struct ki2c * ki2c)
- Line: 143

### ki2c_get_sda
- Return type: static int
- Signature: ki2c_get_sda(struct ki2c * ki2c)
- Line: 151

### ki2c_has_capability
- Return type: static int
- Signature: ki2c_has_capability(struct ki2c * ki2c,unsigned int cap)
- Line: 136

### ki2c_inuse_lock
- Return type: static int
- Signature: ki2c_inuse_lock(struct ki2c * ki2c)
- Line: 58

### ki2c_inuse_unlock
- Return type: static void
- Signature: ki2c_inuse_unlock(struct ki2c * ki2c)
- Line: 86

### ki2c_probe
- Return type: static int
- Signature: ki2c_probe(struct auxiliary_device * auxdev,const struct auxiliary_device_id * id)
- Line: 507

### ki2c_read
- Return type: static int
- Signature: ki2c_read(struct ki2c * ki2c,u8 * data,int len)
- Line: 384

### ki2c_register_devices
- Return type: static int
- Signature: ki2c_register_devices(struct ki2c * ki2c)
- Line: 471

### ki2c_remove
- Return type: static void
- Signature: ki2c_remove(struct auxiliary_device * auxdev)
- Line: 566

### ki2c_repstart_addr
- Return type: static int
- Signature: ki2c_repstart_addr(struct ki2c * ki2c,struct i2c_msg * m)
- Line: 328

### ki2c_reset_bus
- Return type: static int
- Signature: ki2c_reset_bus(struct ki2c * ki2c)
- Line: 264

### ki2c_reset_bus_bitwise
- Return type: static int
- Signature: ki2c_reset_bus_bitwise(struct ki2c * ki2c)
- Line: 182

### ki2c_reset_bus_bytewise
- Return type: static int
- Signature: ki2c_reset_bus_bytewise(struct ki2c * ki2c)
- Line: 237

### ki2c_set_scl
- Return type: static void
- Signature: ki2c_set_scl(struct ki2c * ki2c,int val)
- Line: 159

### ki2c_start_addr
- Return type: static int
- Signature: ki2c_start_addr(struct ki2c * ki2c,struct i2c_msg * m)
- Line: 298

### ki2c_stop
- Return type: static void
- Signature: ki2c_stop(struct ki2c * ki2c)
- Line: 361

### ki2c_unregister_devices
- Return type: static void
- Signature: ki2c_unregister_devices(struct ki2c * ki2c)
- Line: 463

### ki2c_wait_for_bit
- Return type: static int
- Signature: ki2c_wait_for_bit(void __iomem * addr,u8 mask,unsigned long timeout)
- Line: 92

### ki2c_wait_for_data
- Return type: static int
- Signature: ki2c_wait_for_data(struct ki2c * ki2c)
- Line: 106

### ki2c_wait_for_data_ack
- Return type: static int
- Signature: ki2c_wait_for_data_ack(struct ki2c * ki2c)
- Line: 119

### ki2c_wait_for_mcf
- Return type: static int
- Signature: ki2c_wait_for_mcf(struct ki2c * ki2c)
- Line: 100

### ki2c_write
- Return type: static int
- Signature: ki2c_write(struct ki2c * ki2c,const u8 * data,int len)
- Line: 367

### ki2c_write_target_addr
- Return type: static void
- Signature: ki2c_write_target_addr(struct ki2c * ki2c,struct i2c_msg * m)
- Line: 286

### ki2c_xfer
- Return type: static int
- Signature: ki2c_xfer(struct i2c_adapter * adap,struct i2c_msg msgs[],int num)
- Line: 428

## Structs (1)

### ki2c
- Line: 49
- Members:
  - auxdev: keba_i2c_auxdev *
  - base: void __iomem *
  - adapter: i2c_adapter
  - client: i2c_client **
  - client_size: int

## Variables (3)

- static **ki2c_algo** : const struct i2c_algorithm (line 502)
- static **ki2c_devtype_aux** : const struct auxiliary_device_id[] (line 578)
- static **ki2c_driver_aux** : auxiliary_driver (line 584)

## Macros (28)

- **KI2C** (line 14)
- **KI2C_CAPABILITY_CRYPTO** (line 17)
- **KI2C_CAPABILITY_DC** (line 18)
- **KI2C_CAPABILITY_REG** (line 16)
- **KI2C_CONTROL_DC_REG** (line 28)
- **KI2C_CONTROL_DC_SCL** (line 30)
- **KI2C_CONTROL_DC_SDA** (line 29)
- **KI2C_CONTROL_DISABLE** (line 26)
- **KI2C_CONTROL_MEN** (line 21)
- **KI2C_CONTROL_MSTA** (line 22)
- **KI2C_CONTROL_MTX** (line 24)
- **KI2C_CONTROL_REG** (line 20)
- **KI2C_CONTROL_RSTA** (line 23)
- **KI2C_CONTROL_TXAK** (line 25)
- **KI2C_DATA_REG** (line 42)
- **KI2C_INUSE_SLEEP_US** (line 44)
- **KI2C_INUSE_TIMEOUT_US** (line 45)
- **KI2C_POLL_DELAY_US** (line 47)
- **KI2C_RECOVERY_CLK_CNT** (line 180)
- **KI2C_RECOVERY_UDELAY** (line 181)
- **KI2C_STATUS_ACK_CYC** (line 34)
- **KI2C_STATUS_DC_REG** (line 38)
- **KI2C_STATUS_DC_SCL** (line 40)
- **KI2C_STATUS_DC_SDA** (line 39)
- **KI2C_STATUS_IN_USE** (line 33)
- **KI2C_STATUS_MCF** (line 36)
- **KI2C_STATUS_REG** (line 32)
- **KI2C_STATUS_RXAK** (line 35)
