# drivers/i2c/busses/i2c-ali15x3.c

Subsystem: drivers/i2c

## Functions (6)

### ali15x3_access
- Return type: static s32
- Signature: ali15x3_access(struct i2c_adapter * adap,u16 addr,unsigned short flags,char read_write,u8 command,int size,union i2c_smbus_data * data)
- Line: 331

### ali15x3_func
- Return type: static u32
- Signature: ali15x3_func(struct i2c_adapter * adapter)
- Line: 448

### ali15x3_probe
- Return type: static int
- Signature: ali15x3_probe(struct pci_dev * dev,const struct pci_device_id * id)
- Line: 473

### ali15x3_remove
- Return type: static void
- Signature: ali15x3_remove(struct pci_dev * dev)
- Line: 499

### ali15x3_setup
- Return type: static int
- Signature: ali15x3_setup(struct pci_dev * ALI15X3_dev)
- Line: 121

### ali15x3_transaction
- Return type: static int
- Signature: ali15x3_transaction(struct i2c_adapter * adap)
- Line: 220

## Variables (7)

- static **ali15x3_adapter** : i2c_adapter (line 460)
- static **ali15x3_driver** : pci_driver (line 505)
- static **ali15x3_driver** : pci_driver (line 118)
- static **ali15x3_ids** : const struct pci_device_id[] (line 466)
- static **ali15x3_smba** : unsigned short (line 119)
- static **force_addr** : u16 (line 113)
- static **smbus_algorithm** : const struct i2c_algorithm (line 455)

## Macros (34)

- **ALI15X3_ABORT** (line 92)
- **ALI15X3_BLOCK_CLR** (line 99)
- **ALI15X3_BLOCK_DATA** (line 98)
- **ALI15X3_BYTE** (line 95)
- **ALI15X3_BYTE_DATA** (line 96)
- **ALI15X3_LOCK** (line 89)
- **ALI15X3_QUICK** (line 94)
- **ALI15X3_SMB_DEFAULTBASE** (line 86)
- **ALI15X3_SMB_IOSIZE** (line 80)
- **ALI15X3_STS_BUSY** (line 103)
- **ALI15X3_STS_COLL** (line 106)
- **ALI15X3_STS_DEV** (line 105)
- **ALI15X3_STS_DONE** (line 104)
- **ALI15X3_STS_ERR** (line 108)
- **ALI15X3_STS_IDLE** (line 102)
- **ALI15X3_STS_TERM** (line 107)
- **ALI15X3_T_OUT** (line 93)
- **ALI15X3_WORD_DATA** (line 97)
- **MAX_TIMEOUT** (line 79)
- **SMBATPC** (line 72)
- **SMBBA** (line 71)
- **SMBBLKDAT** (line 67)
- **SMBCLK** (line 75)
- **SMBCOM** (line 70)
- **SMBHSTADD** (line 64)
- **SMBHSTCFG** (line 73)
- **SMBHSTCMD** (line 63)
- **SMBHSTCNT** (line 61)
- **SMBHSTDAT0** (line 65)
- **SMBHSTDAT1** (line 66)
- **SMBHSTSTART** (line 62)
- **SMBHSTSTS** (line 60)
- **SMBREV** (line 76)
- **SMBSLVC** (line 74)
