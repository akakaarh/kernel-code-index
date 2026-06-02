# drivers/i2c/busses/i2c-sis96x.c

Subsystem: drivers/i2c

## Functions (7)

### sis96x_access
- Return type: static s32
- Signature: sis96x_access(struct i2c_adapter * adap,u16 addr,unsigned short flags,char read_write,u8 command,int size,union i2c_smbus_data * data)
- Line: 150

### sis96x_func
- Return type: static u32
- Signature: sis96x_func(struct i2c_adapter * adapter)
- Line: 217

### sis96x_probe
- Return type: static int
- Signature: sis96x_probe(struct pci_dev * dev,const struct pci_device_id * id)
- Line: 242

### sis96x_read
- Return type: static u8
- Signature: sis96x_read(u8 reg)
- Line: 66

### sis96x_remove
- Return type: static void
- Signature: sis96x_remove(struct pci_dev * dev)
- Line: 298

### sis96x_transaction
- Return type: static int
- Signature: sis96x_transaction(int size)
- Line: 79

### sis96x_write
- Return type: static void
- Signature: sis96x_write(u8 reg,u8 data)
- Line: 71

## Variables (7)

- static **sis96x_adapter** : i2c_adapter (line 229)
- static **sis96x_adapter** : i2c_adapter (line 63)
- static **sis96x_driver** : pci_driver (line 307)
- static **sis96x_driver** : pci_driver (line 62)
- static **sis96x_ids** : const struct pci_device_id[] (line 235)
- static **sis96x_smbus_base** : u16 (line 64)
- static **smbus_algorithm** : const struct i2c_algorithm (line 224)

## Macros (22)

- **MAX_TIMEOUT** (line 52)
- **SIS96x_BAR** (line 31)
- **SIS96x_BLOCK_DATA** (line 60)
- **SIS96x_BYTE** (line 56)
- **SIS96x_BYTE_DATA** (line 57)
- **SIS96x_PROC_CALL** (line 59)
- **SIS96x_QUICK** (line 55)
- **SIS96x_WORD_DATA** (line 58)
- **SMB_ADDR** (line 38)
- **SMB_BYTE** (line 42)
- **SMB_CMD** (line 39)
- **SMB_CNT** (line 36)
- **SMB_COUNT** (line 41)
- **SMB_DB0** (line 44)
- **SMB_DB1** (line 45)
- **SMB_DEV_ADDR** (line 43)
- **SMB_EN** (line 35)
- **SMB_HOST_CNT** (line 37)
- **SMB_IOSIZE** (line 49)
- **SMB_PCOUNT** (line 40)
- **SMB_SAA** (line 46)
- **SMB_STS** (line 34)
