# drivers/i2c/busses/i2c-taos-evm.c

Subsystem: drivers/i2c

## Functions (7)

### taos_adapter_name
- Return type: static char *
- Signature: taos_adapter_name(char * buffer)
- Line: 183

### taos_connect
- Return type: static int
- Signature: taos_connect(struct serio * serio,struct serio_driver * drv)
- Line: 199

### taos_disconnect
- Return type: static void
- Signature: taos_disconnect(struct serio * serio)
- Line: 273

### taos_instantiate_device
- Return type: static i2c_client *
- Signature: taos_instantiate_device(struct i2c_adapter * adapter)
- Line: 47

### taos_interrupt
- Return type: static irqreturn_t
- Signature: taos_interrupt(struct serio * serio,unsigned char data,unsigned int flags)
- Line: 149

### taos_smbus_func
- Return type: static u32
- Signature: taos_smbus_func(struct i2c_adapter * adapter)
- Line: 139

### taos_smbus_xfer
- Return type: static int
- Signature: taos_smbus_xfer(struct i2c_adapter * adapter,u16 addr,unsigned short flags,char read_write,u8 command,int size,union i2c_smbus_data * data)
- Line: 58

## Structs (1)

### taos_data
- Line: 32
- Members:
  - adapter: i2c_adapter
  - client: i2c_client *
  - state: int
  - addr: u8
  - buffer: unsigned char[]
  - pos: unsigned int

## Variables (4)

- static **taos_algorithm** : const struct i2c_algorithm (line 144)
- static **taos_drv** : serio_driver (line 296)
- static **taos_serio_ids** : const struct serio_device_id[] (line 285)
- static **tsl2550_info** : const struct i2c_board_info (line 42)

## Macros (8)

- **TAOS_BUFFER_SIZE** (line 19)
- **TAOS_CMD_ECHO_OFF** (line 28)
- **TAOS_CMD_ECHO_ON** (line 27)
- **TAOS_CMD_RESET** (line 26)
- **TAOS_STATE_EOFF** (line 23)
- **TAOS_STATE_IDLE** (line 22)
- **TAOS_STATE_INIT** (line 21)
- **TAOS_STATE_RECV** (line 24)
