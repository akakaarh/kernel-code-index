# drivers/i2c/busses/i2c-ali1563.c

Subsystem: drivers/i2c

## Functions (9)

### ali1563_access
- Return type: static s32
- Signature: ali1563_access(struct i2c_adapter * a,u16 addr,unsigned short flags,char rw,u8 cmd,int size,union i2c_smbus_data * data)
- Line: 232

### ali1563_block
- Return type: static int
- Signature: ali1563_block(struct i2c_adapter * a,union i2c_smbus_data * data,u8 rw)
- Line: 185

### ali1563_block_start
- Return type: static int
- Signature: ali1563_block_start(struct i2c_adapter * a)
- Line: 129

### ali1563_func
- Return type: static u32
- Signature: ali1563_func(struct i2c_adapter * a)
- Line: 324

### ali1563_probe
- Return type: static int
- Signature: ali1563_probe(struct pci_dev * dev,const struct pci_device_id * id_table)
- Line: 396

### ali1563_remove
- Return type: static void
- Signature: ali1563_remove(struct pci_dev * dev)
- Line: 419

### ali1563_setup
- Return type: static int
- Signature: ali1563_setup(struct pci_dev * dev)
- Line: 332

### ali1563_shutdown
- Return type: static void
- Signature: ali1563_shutdown(struct pci_dev * dev)
- Line: 380

### ali1563_transaction
- Return type: static int
- Signature: ali1563_transaction(struct i2c_adapter * a,int size)
- Line: 65

## Variables (6)

- static **ali1563_adapter** : i2c_adapter (line 390)
- static **ali1563_algorithm** : const struct i2c_algorithm (line 385)
- static **ali1563_id_table** : const struct pci_device_id[] (line 425)
- static **ali1563_pci_driver** : pci_driver (line 432)
- static **ali1563_pci_driver** : pci_driver (line 62)
- static **ali1563_smba** : unsigned short (line 63)

## Macros (30)

- **ALI1563_MAX_TIMEOUT** (line 24)
- **ALI1563_SMBBA** (line 25)
- **ALI1563_SMB_HOSTEN** (line 27)
- **ALI1563_SMB_IOEN** (line 26)
- **ALI1563_SMB_IOSIZE** (line 28)
- **HST_CNTL1_LAST** (line 49)
- **HST_CNTL1_TIMEOUT** (line 48)
- **HST_CNTL2_BLOCK** (line 57)
- **HST_CNTL2_BYTE** (line 54)
- **HST_CNTL2_BYTE_DATA** (line 55)
- **HST_CNTL2_KILL** (line 51)
- **HST_CNTL2_QUICK** (line 53)
- **HST_CNTL2_SIZEMASK** (line 60)
- **HST_CNTL2_START** (line 52)
- **HST_CNTL2_WORD_DATA** (line 56)
- **HST_STS_BAD** (line 45)
- **HST_STS_BUSERR** (line 42)
- **HST_STS_BUSY** (line 39)
- **HST_STS_DEVERR** (line 41)
- **HST_STS_DONE** (line 44)
- **HST_STS_FAIL** (line 43)
- **HST_STS_INTR** (line 40)
- **SMB_BLK_DAT** (line 37)
- **SMB_HST_ADD** (line 34)
- **SMB_HST_CMD** (line 33)
- **SMB_HST_CNTL1** (line 31)
- **SMB_HST_CNTL2** (line 32)
- **SMB_HST_DAT0** (line 35)
- **SMB_HST_DAT1** (line 36)
- **SMB_HST_STS** (line 30)
