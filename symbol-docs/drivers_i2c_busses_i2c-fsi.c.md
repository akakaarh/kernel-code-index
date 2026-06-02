# drivers/i2c/busses/i2c-fsi.c

Subsystem: drivers/i2c

## Functions (24)

### fsi_i2c_abort
- Return type: static int
- Signature: fsi_i2c_abort(struct fsi_i2c_port * port,u32 status)
- Line: 475

### fsi_i2c_dev_init
- Return type: static int
- Signature: fsi_i2c_dev_init(struct fsi_i2c_ctrl * i2c)
- Line: 186

### fsi_i2c_find_port_of_node
- Return type: static device_node *
- Signature: fsi_i2c_find_port_of_node(struct device_node * fsi,int port)
- Line: 661

### fsi_i2c_functionality
- Return type: static u32
- Signature: fsi_i2c_functionality(struct i2c_adapter * adap)
- Line: 640

### fsi_i2c_get_op_bytes
- Return type: static int
- Signature: fsi_i2c_get_op_bytes(int op_bytes)
- Line: 256

### fsi_i2c_get_scl
- Return type: static int
- Signature: fsi_i2c_get_scl(struct i2c_adapter * adap)
- Line: 329

### fsi_i2c_get_sda
- Return type: static int
- Signature: fsi_i2c_get_sda(struct i2c_adapter * adap)
- Line: 352

### fsi_i2c_handle_status
- Return type: static int
- Signature: fsi_i2c_handle_status(struct fsi_i2c_port * port,struct i2c_msg * msg,u32 status)
- Line: 525

### fsi_i2c_prepare_recovery
- Return type: static void
- Signature: fsi_i2c_prepare_recovery(struct i2c_adapter * adap)
- Line: 375

### fsi_i2c_probe
- Return type: static int
- Signature: fsi_i2c_probe(struct fsi_device * fsi_dev)
- Line: 677

### fsi_i2c_read_fifo
- Return type: static int
- Signature: fsi_i2c_read_fifo(struct fsi_i2c_port * port,struct i2c_msg * msg,u8 fifo_count)
- Line: 292

### fsi_i2c_read_reg
- Return type: static int
- Signature: fsi_i2c_read_reg(struct fsi_device * fsi,unsigned int reg,u32 * data)
- Line: 163

### fsi_i2c_remove
- Return type: static void
- Signature: fsi_i2c_remove(struct fsi_device * fsi_dev)
- Line: 745

### fsi_i2c_reset_bus
- Return type: static int
- Signature: fsi_i2c_reset_bus(struct fsi_i2c_ctrl * i2c,struct fsi_i2c_port * port)
- Line: 405

### fsi_i2c_reset_engine
- Return type: static int
- Signature: fsi_i2c_reset_engine(struct fsi_i2c_ctrl * i2c,u16 port)
- Line: 438

### fsi_i2c_set_port
- Return type: static int
- Signature: fsi_i2c_set_port(struct fsi_i2c_port * port)
- Line: 214

### fsi_i2c_set_scl
- Return type: static void
- Signature: fsi_i2c_set_scl(struct i2c_adapter * adap,int val)
- Line: 340

### fsi_i2c_set_sda
- Return type: static void
- Signature: fsi_i2c_set_sda(struct i2c_adapter * adap,int val)
- Line: 363

### fsi_i2c_start
- Return type: static int
- Signature: fsi_i2c_start(struct fsi_i2c_port * port,struct i2c_msg * msg,bool stop)
- Line: 236

### fsi_i2c_unprepare_recovery
- Return type: static void
- Signature: fsi_i2c_unprepare_recovery(struct i2c_adapter * adap)
- Line: 390

### fsi_i2c_wait
- Return type: static int
- Signature: fsi_i2c_wait(struct fsi_i2c_port * port,struct i2c_msg * msg,unsigned long timeout)
- Line: 574

### fsi_i2c_write_fifo
- Return type: static int
- Signature: fsi_i2c_write_fifo(struct fsi_i2c_port * port,struct i2c_msg * msg,u8 fifo_count)
- Line: 266

### fsi_i2c_write_reg
- Return type: static int
- Signature: fsi_i2c_write_reg(struct fsi_device * fsi,unsigned int reg,u32 * data)
- Line: 178

### fsi_i2c_xfer
- Return type: static int
- Signature: fsi_i2c_xfer(struct i2c_adapter * adap,struct i2c_msg * msgs,int num)
- Line: 606

## Structs (2)

### fsi_i2c_ctrl
- Line: 148
- Members:
  - fsi: fsi_device *
  - fifo_size: u8
  - ports: list_head
  - lock: mutex
  - list: list_head
  - adapter: i2c_adapter
  - ctrl: fsi_i2c_ctrl *
  - port: u16
  - xfrd: u16

### fsi_i2c_port
- Line: 155
- Members:
  - fsi: fsi_device *
  - fifo_size: u8
  - ports: list_head
  - lock: mutex
  - list: list_head
  - adapter: i2c_adapter
  - ctrl: fsi_i2c_ctrl *
  - port: u16
  - xfrd: u16

## Variables (4)

- static **fsi_i2c_algorithm** : const struct i2c_algorithm (line 656)
- static **fsi_i2c_bus_recovery_info** : i2c_bus_recovery_info (line 646)
- static **fsi_i2c_driver** : fsi_driver (line 762)
- static **fsi_i2c_ids** : const struct fsi_device_id[] (line 757)

## Macros (86)

- **FSI_ENGID_I2C** (line 28)
- **I2C_ABORT_TIMEOUT** (line 146)
- **I2C_CMD_ADDR** (line 59)
- **I2C_CMD_FORCELAUNCH** (line 58)
- **I2C_CMD_LEN** (line 61)
- **I2C_CMD_RD_CONT** (line 56)
- **I2C_CMD_READ** (line 60)
- **I2C_CMD_SLEEP_MAX_US** (line 138)
- **I2C_CMD_SLEEP_MIN_US** (line 139)
- **I2C_CMD_WITH_ADDR** (line 55)
- **I2C_CMD_WITH_START** (line 54)
- **I2C_CMD_WITH_STOP** (line 57)
- **I2C_DEFAULT_CLK_DIV** (line 30)
- **I2C_ESTAT_FIFO_SZ** (line 121)
- **I2C_ESTAT_HI_WATER** (line 128)
- **I2C_ESTAT_LO_WATER** (line 129)
- **I2C_ESTAT_M_SCL** (line 126)
- **I2C_ESTAT_M_SDA** (line 127)
- **I2C_ESTAT_PORT_BUSY** (line 130)
- **I2C_ESTAT_SCL_IN_SY** (line 122)
- **I2C_ESTAT_SDA_IN_SY** (line 123)
- **I2C_ESTAT_SELF_BUSY** (line 131)
- **I2C_ESTAT_S_SCL** (line 124)
- **I2C_ESTAT_S_SDA** (line 125)
- **I2C_ESTAT_VERSION** (line 132)
- **I2C_FIFO_HI_LVL** (line 75)
- **I2C_FIFO_LO_LVL** (line 76)
- **I2C_FSI_AND_INT_MASK** (line 41)
- **I2C_FSI_CMD** (line 34)
- **I2C_FSI_ESTAT** (line 44)
- **I2C_FSI_FIFO** (line 33)
- **I2C_FSI_INTS** (line 40)
- **I2C_FSI_INT_COND** (line 38)
- **I2C_FSI_INT_MASK** (line 37)
- **I2C_FSI_MODE** (line 35)
- **I2C_FSI_OR_INT_MASK** (line 39)
- **I2C_FSI_PORT_BUSY** (line 48)
- **I2C_FSI_RESET_ERR** (line 45)
- **I2C_FSI_RESET_I2C** (line 43)
- **I2C_FSI_RESET_SCL** (line 49)
- **I2C_FSI_RESET_SDA** (line 51)
- **I2C_FSI_RESID_LEN** (line 46)
- **I2C_FSI_SET_SCL** (line 47)
- **I2C_FSI_SET_SDA** (line 50)
- **I2C_FSI_STAT** (line 42)
- **I2C_FSI_WATER_MARK** (line 36)
- **I2C_INT_BE_ACCESS** (line 82)
- **I2C_INT_BE_OVERRUN** (line 81)
- **I2C_INT_BUSY** (line 88)
- **I2C_INT_CMD_COMP** (line 86)
- **I2C_INT_DAT_REQ** (line 85)
- **I2C_INT_IDLE** (line 89)
- **I2C_INT_INV_CMD** (line 79)
- **I2C_INT_LOST_ARB** (line 83)
- **I2C_INT_NACK** (line 84)
- **I2C_INT_PARITY** (line 80)
- **I2C_INT_STOP_ERR** (line 87)
- **I2C_MODE_CLKDIV** (line 64)
- **I2C_MODE_DIAG** (line 67)
- **I2C_MODE_ENHANCED** (line 66)
- **I2C_MODE_PACE_ALLOW** (line 68)
- **I2C_MODE_PORT** (line 65)
- **I2C_MODE_WRAP** (line 69)
- **I2C_PORT_BUSY_RESET** (line 135)
- **I2C_RESET_SLEEP_MAX_US** (line 142)
- **I2C_RESET_SLEEP_MIN_US** (line 143)
- **I2C_STAT_ANY_INT** (line 102)
- **I2C_STAT_ANY_RESP** (line 116)
- **I2C_STAT_BE_ACCESS** (line 95)
- **I2C_STAT_BE_OVERRUN** (line 94)
- **I2C_STAT_CMD_COMP** (line 99)
- **I2C_STAT_DAT_REQ** (line 98)
- **I2C_STAT_ERR** (line 109)
- **I2C_STAT_FIFO_COUNT** (line 107)
- **I2C_STAT_INV_CMD** (line 92)
- **I2C_STAT_LOST_ARB** (line 96)
- **I2C_STAT_MAX_PORT** (line 101)
- **I2C_STAT_NACK** (line 97)
- **I2C_STAT_PARITY** (line 93)
- **I2C_STAT_PORT_BUSY** (line 105)
- **I2C_STAT_SCL_IN** (line 103)
- **I2C_STAT_SDA_IN** (line 104)
- **I2C_STAT_SELF_BUSY** (line 106)
- **I2C_STAT_STOP_ERR** (line 100)
- **I2C_WATERMARK_HI** (line 72)
- **I2C_WATERMARK_LO** (line 73)
