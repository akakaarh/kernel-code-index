# drivers/i2c/busses/i2c-isch.c

Subsystem: drivers/i2c

## Functions (8)

### sch_access
- Return type: static s32
- Signature: sch_access(struct i2c_adapter * adap,u16 addr,unsigned short flags,char read_write,u8 command,int size,union i2c_smbus_data * data)
- Line: 159

### sch_func
- Return type: static u32
- Signature: sch_func(struct i2c_adapter * adapter)
- Line: 262

### sch_io_rd16
- Return type: static u16
- Signature: sch_io_rd16(struct sch_i2c * priv,unsigned int offset)
- Line: 64

### sch_io_rd8
- Return type: static u8
- Signature: sch_io_rd8(struct sch_i2c * priv,unsigned int offset)
- Line: 54

### sch_io_wr16
- Return type: static void
- Signature: sch_io_wr16(struct sch_i2c * priv,unsigned int offset,u16 value)
- Line: 69

### sch_io_wr8
- Return type: static void
- Signature: sch_io_wr8(struct sch_i2c * priv,unsigned int offset,u8 value)
- Line: 59

### sch_transaction
- Return type: static int
- Signature: sch_transaction(struct i2c_adapter * adap)
- Line: 83

### smbus_sch_probe
- Return type: static int
- Signature: smbus_sch_probe(struct platform_device * pdev)
- Line: 274

## Structs (1)

### sch_i2c
- Line: 45
- Members:
  - adapter: i2c_adapter
  - smba: void __iomem *

## Variables (3)

- static **backbone_speed** : int (line 50)
- static **smbus_algorithm** : const struct i2c_algorithm (line 269)
- static **smbus_sch_driver** : platform_driver (line 304)

## Macros (13)

- **SCH_BLOCK_DATA** (line 43)
- **SCH_BYTE** (line 40)
- **SCH_BYTE_DATA** (line 41)
- **SCH_QUICK** (line 39)
- **SCH_WORD_DATA** (line 42)
- **SMBBLKDAT** (line 36)
- **SMBHSTADD** (line 32)
- **SMBHSTCLK** (line 31)
- **SMBHSTCMD** (line 33)
- **SMBHSTCNT** (line 29)
- **SMBHSTDAT0** (line 34)
- **SMBHSTDAT1** (line 35)
- **SMBHSTSTS** (line 30)
