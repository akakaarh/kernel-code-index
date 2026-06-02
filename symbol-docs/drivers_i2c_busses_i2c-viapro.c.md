# drivers/i2c/busses/i2c-viapro.c

Subsystem: drivers/i2c

## Functions (8)

### i2c_vt596_exit
- Return type: static void __exit
- Signature: i2c_vt596_exit(void)
- Line: 478

### i2c_vt596_init
- Return type: static int __init
- Signature: i2c_vt596_init(void)
- Line: 472

### vt596_access
- Return type: static s32
- Signature: vt596_access(struct i2c_adapter * adap,u16 addr,unsigned short flags,char read_write,u8 command,int size,union i2c_smbus_data * data)
- Line: 190

### vt596_dump_regs
- Return type: static void
- Signature: vt596_dump_regs(const char * msg,u8 size)
- Line: 124

### vt596_dump_regs
- Return type: static void
- Signature: vt596_dump_regs(const char * msg,u8 size)
- Line: 102

### vt596_func
- Return type: static u32
- Signature: vt596_func(struct i2c_adapter * adapter)
- Line: 289

### vt596_probe
- Return type: static int
- Signature: vt596_probe(struct pci_dev * pdev,const struct pci_device_id * id)
- Line: 311

### vt596_transaction
- Return type: static int
- Signature: vt596_transaction(u8 size)
- Line: 128

## Variables (12)

- static **SMBHSTCFG** : unsigned short (line 65)
- static **force** : bool (line 82)
- static **force_addr** : u16 (line 88)
- static **smbus_algorithm** : const struct i2c_algorithm (line 300)
- static **vt596_adapter** : i2c_adapter (line 305)
- static **vt596_adapter** : i2c_adapter (line 96)
- static **vt596_driver** : pci_driver (line 466)
- static **vt596_driver** : pci_driver (line 95)
- static **vt596_features** : unsigned int (line 99)
- static **vt596_ids** : const struct pci_device_id[] (line 430)
- static **vt596_pdev** : pci_dev * (line 44)
- static **vt596_smba** : unsigned short (line 51)

## Macros (19)

- **FEATURE_I2CBLOCK** (line 98)
- **MAX_TIMEOUT** (line 68)
- **SMBBA1** (line 46)
- **SMBBA2** (line 47)
- **SMBBA3** (line 48)
- **SMBBLKDAT** (line 58)
- **SMBHSTADD** (line 55)
- **SMBHSTCMD** (line 54)
- **SMBHSTCNT** (line 53)
- **SMBHSTDAT0** (line 56)
- **SMBHSTDAT1** (line 57)
- **SMBHSTSTS** (line 52)
- **VT596_BLOCK_DATA** (line 76)
- **VT596_BYTE** (line 72)
- **VT596_BYTE_DATA** (line 73)
- **VT596_I2C_BLOCK_DATA** (line 77)
- **VT596_PROC_CALL** (line 75)
- **VT596_QUICK** (line 71)
- **VT596_WORD_DATA** (line 74)
