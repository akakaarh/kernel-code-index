# drivers/i2c/i2c-smbus.c

Subsystem: drivers/i2c

## Functions (13)

### i2c_free_slave_host_notify_device
- Return type: void
- Signature: i2c_free_slave_host_notify_device(struct i2c_client * client)
- Line: 353

### i2c_handle_smbus_alert
- Return type: int
- Signature: i2c_handle_smbus_alert(struct i2c_client * ara)
- Line: 249

### i2c_new_slave_host_notify_device
- Return type: i2c_client *
- Signature: i2c_new_slave_host_notify_device(struct i2c_adapter * adapter)
- Line: 312

### i2c_register_spd
- Return type: static void
- Signature: i2c_register_spd(struct i2c_adapter * adap,bool write_disabled)
- Line: 374

### i2c_register_spd_write_disable
- Return type: void
- Signature: i2c_register_spd_write_disable(struct i2c_adapter * adap)
- Line: 477

### i2c_register_spd_write_enable
- Return type: void
- Signature: i2c_register_spd_write_enable(struct i2c_adapter * adap)
- Line: 483

### i2c_slave_host_notify_cb
- Return type: static int
- Signature: i2c_slave_host_notify_cb(struct i2c_client * client,enum i2c_slave_event event,u8 * val)
- Line: 266

### smbalert_probe
- Return type: static int
- Signature: smbalert_probe(struct i2c_client * ara)
- Line: 166

### smbalert_remove
- Return type: static void
- Signature: smbalert_remove(struct i2c_client * ara)
- Line: 215

### smbalert_work
- Return type: static void
- Signature: smbalert_work(struct work_struct * work)
- Line: 155

### smbus_alert
- Return type: static irqreturn_t
- Signature: smbus_alert(int irq,void * d)
- Line: 99

### smbus_do_alert
- Return type: static int
- Signature: smbus_do_alert(struct device * dev,void * addrp)
- Line: 33

### smbus_do_alert_force
- Return type: static int
- Signature: smbus_do_alert_force(struct device * dev,void * addrp)
- Line: 71

## Structs (3)

### alert_data
- Line: 26
- Members:
  - alert: work_struct
  - ara: i2c_client *
  - addr: unsigned short
  - type: i2c_alert_protocol
  - data: unsigned int
  - index: u8
  - addr: u8

### i2c_slave_host_notify_status
- Line: 261
- Members:
  - alert: work_struct
  - ara: i2c_client *
  - addr: unsigned short
  - type: i2c_alert_protocol
  - data: unsigned int
  - index: u8
  - addr: u8

### i2c_smbus_alert
- Line: 21
- Members:
  - alert: work_struct
  - ara: i2c_client *
  - addr: unsigned short
  - type: i2c_alert_protocol
  - data: unsigned int
  - index: u8
  - addr: u8

## Variables (2)

- static **smbalert_driver** : i2c_driver (line 228)
- static **smbalert_ids** : const struct i2c_device_id[] (line 222)

## Macros (1)

- **SMBUS_HOST_NOTIFY_LEN** (line 260)
