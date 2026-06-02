# drivers/i2c/i2c-slave-testunit.c

Subsystem: drivers/i2c

## Functions (5)

### i2c_slave_testunit_probe
- Return type: static int
- Signature: i2c_slave_testunit_probe(struct i2c_client * client)
- Line: 236

### i2c_slave_testunit_remove
- Return type: static void
- Signature: i2c_slave_testunit_remove(struct i2c_client * client)
- Line: 264

### i2c_slave_testunit_slave_cb
- Return type: static int
- Signature: i2c_slave_testunit_slave_cb(struct i2c_client * client,enum i2c_slave_event event,u8 * val)
- Line: 82

### i2c_slave_testunit_smbalert_cb
- Return type: static int
- Signature: i2c_slave_testunit_smbalert_cb(struct i2c_client * client,enum i2c_slave_event event,u8 * val)
- Line: 57

### i2c_slave_testunit_work
- Return type: static void
- Signature: i2c_slave_testunit_work(struct work_struct * work)
- Line: 168

## Structs (1)

### testunit_data
- Line: 44
- Members:
  - flags: unsigned long
  - regs: u8[]
  - reg_idx: u8
  - read_idx: u8
  - client: i2c_client *
  - worker: delayed_work
  - gpio: gpio_desc *
  - alert_done: completion

## Enums (3)

### testunit_cmds
- Line: 22

### testunit_flags
- Line: 39

### testunit_regs
- Line: 31

## Variables (3)

- static **i2c_slave_testunit_driver** : i2c_driver (line 278)
- static **i2c_slave_testunit_id** : const struct i2c_device_id[] (line 272)
- static **tu_version_info** : char[] (line 55)

## Macros (1)

- **TU_VERSION_MAX_LENGTH** (line 20)
