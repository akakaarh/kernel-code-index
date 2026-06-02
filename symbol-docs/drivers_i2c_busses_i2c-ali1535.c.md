# drivers/i2c/busses/i2c-ali1535.c

Subsystem: drivers/i2c

## Functions (6)

### ali1535_access
- Return type: static s32
- Signature: ali1535_access(struct i2c_adapter * adap,u16 addr,unsigned short flags,char read_write,u8 command,int size,union i2c_smbus_data * data)
- Line: 337

### ali1535_func
- Return type: static u32
- Signature: ali1535_func(struct i2c_adapter * adapter)
- Line: 462

### ali1535_probe
- Return type: static int
- Signature: ali1535_probe(struct pci_dev * dev,const struct pci_device_id * id)
- Line: 486

### ali1535_remove
- Return type: static void
- Signature: ali1535_remove(struct pci_dev * dev)
- Line: 512

### ali1535_setup
- Return type: static int
- Signature: ali1535_setup(struct pci_dev * dev)
- Line: 128

### ali1535_transaction
- Return type: static int
- Signature: ali1535_transaction(struct i2c_adapter * adap)
- Line: 212

## Variables (7)

- static **ali1535_adapter** : i2c_adapter (line 474)
- static **ali1535_driver** : pci_driver (line 523)
- static **ali1535_driver** : pci_driver (line 120)
- static **ali1535_ids** : const struct pci_device_id[] (line 480)
- static **ali1535_offset** : unsigned short (line 122)
- static **ali1535_smba** : unsigned long (line 121)
- static **smbus_algorithm** : const struct i2c_algorithm (line 469)

## Macros (40)

- **ALI1535_A_HIGH_BIT8** (line 94)
- **ALI1535_A_HIGH_BIT9** (line 90)
- **ALI1535_BLOCK_CLR** (line 111)
- **ALI1535_BLOCK_DATA** (line 84)
- **ALI1535_BYTE** (line 81)
- **ALI1535_BYTE_DATA** (line 82)
- **ALI1535_DEV10B_EN** (line 87)
- **ALI1535_D_HI_MASK** (line 98)
- **ALI1535_I2C_READ** (line 85)
- **ALI1535_KILL** (line 93)
- **ALI1535_LOCK** (line 77)
- **ALI1535_QUICK** (line 80)
- **ALI1535_RD_ADDR** (line 114)
- **ALI1535_SMBIO_EN** (line 118)
- **ALI1535_SMB_DEFAULTBASE** (line 74)
- **ALI1535_SMB_IOSIZE** (line 72)
- **ALI1535_STS_BUSERR** (line 107)
- **ALI1535_STS_BUSY** (line 104)
- **ALI1535_STS_DEV** (line 106)
- **ALI1535_STS_DONE** (line 105)
- **ALI1535_STS_ERR** (line 109)
- **ALI1535_STS_FAIL** (line 108)
- **ALI1535_STS_IDLE** (line 103)
- **ALI1535_T_OUT** (line 89)
- **ALI1535_WORD_DATA** (line 83)
- **MAX_TIMEOUT** (line 71)
- **SMBBA** (line 66)
- **SMBBLKDAT** (line 60)
- **SMBCFG** (line 65)
- **SMBCLK** (line 68)
- **SMBCOM** (line 63)
- **SMBHSTADD** (line 57)
- **SMBHSTCFG** (line 67)
- **SMBHSTCMD** (line 56)
- **SMBHSTDAT0** (line 58)
- **SMBHSTDAT1** (line 59)
- **SMBHSTPORT** (line 55)
- **SMBHSTSTS** (line 53)
- **SMBHSTTYP** (line 54)
- **SMBREV** (line 64)
