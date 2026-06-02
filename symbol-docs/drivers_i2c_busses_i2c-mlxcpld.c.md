# drivers/i2c/busses/i2c-mlxcpld.c

Subsystem: drivers/i2c

## Functions (17)

### mlxcpld_i2c_check_busy
- Return type: static int
- Signature: mlxcpld_i2c_check_busy(struct mlxcpld_i2c_priv * priv)
- Line: 253

### mlxcpld_i2c_check_msg_params
- Return type: static int
- Signature: mlxcpld_i2c_check_msg_params(struct mlxcpld_i2c_priv * priv,struct i2c_msg * msgs,int num)
- Line: 154

### mlxcpld_i2c_check_status
- Return type: static int
- Signature: mlxcpld_i2c_check_status(struct mlxcpld_i2c_priv * priv,int * status)
- Line: 191

### mlxcpld_i2c_func
- Return type: static u32
- Signature: mlxcpld_i2c_func(struct i2c_adapter * adap)
- Line: 439

### mlxcpld_i2c_lpc_read_buf
- Return type: static void
- Signature: mlxcpld_i2c_lpc_read_buf(u8 * data,u8 len,u32 addr)
- Line: 90

### mlxcpld_i2c_lpc_write_buf
- Return type: static void
- Signature: mlxcpld_i2c_lpc_write_buf(u8 * data,u8 len,u32 addr)
- Line: 80

### mlxcpld_i2c_probe
- Return type: static int
- Signature: mlxcpld_i2c_probe(struct platform_device * pdev)
- Line: 525

### mlxcpld_i2c_read_comm
- Return type: static void
- Signature: mlxcpld_i2c_read_comm(struct mlxcpld_i2c_priv * priv,u8 offs,u8 * data,u8 datalen)
- Line: 100

### mlxcpld_i2c_remove
- Return type: static void
- Signature: mlxcpld_i2c_remove(struct platform_device * pdev)
- Line: 584

### mlxcpld_i2c_reset
- Return type: static void
- Signature: mlxcpld_i2c_reset(struct mlxcpld_i2c_priv * priv)
- Line: 239

### mlxcpld_i2c_set_frequency
- Return type: static int
- Signature: mlxcpld_i2c_set_frequency(struct mlxcpld_i2c_priv * priv,struct mlxreg_core_hotplug_platform_data * pdata)
- Line: 488

### mlxcpld_i2c_set_transf_data
- Return type: static void
- Signature: mlxcpld_i2c_set_transf_data(struct mlxcpld_i2c_priv * priv,struct i2c_msg * msgs,int num,u8 comm_len)
- Line: 214

### mlxcpld_i2c_wait_for_free
- Return type: static int
- Signature: mlxcpld_i2c_wait_for_free(struct mlxcpld_i2c_priv * priv)
- Line: 265

### mlxcpld_i2c_wait_for_tc
- Return type: static int
- Signature: mlxcpld_i2c_wait_for_tc(struct mlxcpld_i2c_priv * priv)
- Line: 287

### mlxcpld_i2c_write_comm
- Return type: static void
- Signature: mlxcpld_i2c_write_comm(struct mlxcpld_i2c_priv * priv,u8 offs,u8 * data,u8 datalen)
- Line: 125

### mlxcpld_i2c_xfer
- Return type: static int
- Signature: mlxcpld_i2c_xfer(struct i2c_adapter * adap,struct i2c_msg * msgs,int num)
- Line: 389

### mlxcpld_i2c_xfer_msg
- Return type: static void
- Signature: mlxcpld_i2c_xfer_msg(struct mlxcpld_i2c_priv * priv)
- Line: 349

## Structs (2)

### mlxcpld_i2c_curr_xfer
- Line: 62
- Members:
  - cmd: u8
  - addr_width: u8
  - data_len: u8
  - msg_num: u8
  - msg: i2c_msg *
  - adap: i2c_adapter
  - base_addr: u32
  - lock: mutex
  - xfer: mlxcpld_i2c_curr_xfer
  - dev: device *
  - smbus_block: bool
  - polling_time: int

### mlxcpld_i2c_priv
- Line: 70
- Members:
  - cmd: u8
  - addr_width: u8
  - data_len: u8
  - msg_num: u8
  - msg: i2c_msg *
  - adap: i2c_adapter
  - base_addr: u32
  - lock: mutex
  - xfer: mlxcpld_i2c_curr_xfer
  - dev: device *
  - smbus_block: bool
  - polling_time: int

## Enums (1)

### mlxcpld_i2c_frequency
- Line: 56

## Variables (6)

- static **mlxcpld_i2c_adapter** : i2c_adapter (line 477)
- static **mlxcpld_i2c_algo** : const struct i2c_algorithm (line 451)
- static **mlxcpld_i2c_driver** : platform_driver (line 592)
- static **mlxcpld_i2c_quirks** : const struct i2c_adapter_quirks (line 456)
- static **mlxcpld_i2c_quirks_ext** : const struct i2c_adapter_quirks (line 463)
- static **mlxcpld_i2c_quirks_ext2** : const struct i2c_adapter_quirks (line 470)

## Macros (31)

- **MLXCPLD_I2C_BUS_NUM** (line 22)
- **MLXCPLD_I2C_DATA_EXT2_SZ_BIT** (line 25)
- **MLXCPLD_I2C_DATA_REG_SZ** (line 23)
- **MLXCPLD_I2C_DATA_SZ_BIT** (line 24)
- **MLXCPLD_I2C_DATA_SZ_MASK** (line 26)
- **MLXCPLD_I2C_DEVICE_NAME** (line 20)
- **MLXCPLD_I2C_FREQ_1000KHZ_SET** (line 52)
- **MLXCPLD_I2C_FREQ_100KHZ_SET** (line 54)
- **MLXCPLD_I2C_FREQ_400KHZ_SET** (line 53)
- **MLXCPLD_I2C_MAX_ADDR_LEN** (line 28)
- **MLXCPLD_I2C_POLL_TIME** (line 31)
- **MLXCPLD_I2C_RETR_NUM** (line 29)
- **MLXCPLD_I2C_SMBUS_BLK_BIT** (line 27)
- **MLXCPLD_I2C_VALID_FLAG** (line 21)
- **MLXCPLD_I2C_XFER_TO** (line 30)
- **MLXCPLD_LPCI2C_ACK_IND** (line 49)
- **MLXCPLD_LPCI2C_CMD_REG** (line 38)
- **MLXCPLD_LPCI2C_CPBLTY_REG** (line 34)
- **MLXCPLD_LPCI2C_CTRL_REG** (line 35)
- **MLXCPLD_LPCI2C_DATA_REG** (line 42)
- **MLXCPLD_LPCI2C_HALF_CYC_REG** (line 36)
- **MLXCPLD_LPCI2C_I2C_HOLD_REG** (line 37)
- **MLXCPLD_LPCI2C_NACK_IND** (line 50)
- **MLXCPLD_LPCI2C_NO_IND** (line 48)
- **MLXCPLD_LPCI2C_NUM_ADDR_REG** (line 40)
- **MLXCPLD_LPCI2C_NUM_DAT_REG** (line 39)
- **MLXCPLD_LPCI2C_RST_SEL_MASK** (line 45)
- **MLXCPLD_LPCI2C_STATUS_NACK** (line 47)
- **MLXCPLD_LPCI2C_STATUS_REG** (line 41)
- **MLXCPLD_LPCI2C_TRANS_END** (line 46)
- **MLXPLAT_CPLD_LPC_I2C_BASE_ADDR** (line 19)
