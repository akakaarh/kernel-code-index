# drivers/i2c/busses/i2c-sis5595.c

Subsystem: drivers/i2c

## Functions (9)

### i2c_sis5595_exit
- Return type: static void __exit
- Signature: i2c_sis5595_exit(void)
- Line: 406

### i2c_sis5595_init
- Return type: static int __init
- Signature: i2c_sis5595_init(void)
- Line: 401

### sis5595_access
- Return type: static s32
- Signature: sis5595_access(struct i2c_adapter * adap,u16 addr,unsigned short flags,char read_write,u8 command,int size,union i2c_smbus_data * data)
- Line: 278

### sis5595_func
- Return type: static u32
- Signature: sis5595_func(struct i2c_adapter * adapter)
- Line: 342

### sis5595_probe
- Return type: static int
- Signature: sis5595_probe(struct pci_dev * dev,const struct pci_device_id * id)
- Line: 367

### sis5595_read
- Return type: static u8
- Signature: sis5595_read(u8 reg)
- Line: 121

### sis5595_setup
- Return type: static int
- Signature: sis5595_setup(struct pci_dev * SIS5595_dev)
- Line: 133

### sis5595_transaction
- Return type: static int
- Signature: sis5595_transaction(struct i2c_adapter * adap)
- Line: 217

### sis5595_write
- Return type: static void
- Signature: sis5595_write(u8 reg,u8 data)
- Line: 127

## Variables (9)

- static **blacklist** : int[] (line 54)
- static **force_addr** : u16 (line 113)
- static **sis5595_adapter** : i2c_adapter (line 354)
- static **sis5595_base** : unsigned short (line 118)
- static **sis5595_driver** : pci_driver (line 395)
- static **sis5595_driver** : pci_driver (line 117)
- static **sis5595_ids** : const struct pci_device_id[] (line 360)
- static **sis5595_pdev** : pci_dev * (line 119)
- static **smbus_algorithm** : const struct i2c_algorithm (line 349)

## Macros (25)

- **ACPI_BASE** (line 96)
- **MAX_TIMEOUT** (line 99)
- **SIS5595_BLOCK_DATA** (line 107)
- **SIS5595_BYTE** (line 103)
- **SIS5595_BYTE_DATA** (line 104)
- **SIS5595_ENABLE_REG** (line 95)
- **SIS5595_EXTENT** (line 76)
- **SIS5595_PROC_CALL** (line 106)
- **SIS5595_QUICK** (line 102)
- **SIS5595_WORD_DATA** (line 105)
- **SMB_ADDR** (line 82)
- **SMB_BYTE** (line 86)
- **SMB_CMD** (line 83)
- **SMB_CNT** (line 85)
- **SMB_CTL_HI** (line 81)
- **SMB_CTL_LO** (line 80)
- **SMB_DAT** (line 94)
- **SMB_DB0** (line 88)
- **SMB_DB1** (line 89)
- **SMB_DEV** (line 87)
- **SMB_HAA** (line 90)
- **SMB_INDEX** (line 93)
- **SMB_PCNT** (line 84)
- **SMB_STS_HI** (line 79)
- **SMB_STS_LO** (line 78)
