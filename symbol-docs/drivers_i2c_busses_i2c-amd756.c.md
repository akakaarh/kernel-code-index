# drivers/i2c/busses/i2c-amd756.c

Subsystem: drivers/i2c

## Functions (5)

### amd756_access
- Return type: static s32
- Signature: amd756_access(struct i2c_adapter * adap,u16 addr,unsigned short flags,char read_write,u8 command,int size,union i2c_smbus_data * data)
- Line: 181

### amd756_func
- Return type: static u32
- Signature: amd756_func(struct i2c_adapter * adapter)
- Line: 274

### amd756_probe
- Return type: static int
- Signature: amd756_probe(struct pci_dev * pdev,const struct pci_device_id * id)
- Line: 314

### amd756_remove
- Return type: static void
- Signature: amd756_remove(struct pci_dev * dev)
- Line: 383

### amd756_transaction
- Return type: static int
- Signature: amd756_transaction(struct i2c_adapter * adap)
- Line: 96

## Enums (1)

### chiptype
- Line: 292

## Variables (7)

- static **amd756_driver** : pci_driver (line 389)
- static **amd756_driver** : pci_driver (line 72)
- static **amd756_ids** : const struct pci_device_id[] (line 298)
- static **amd756_ioport** : unsigned short (line 73)
- static **amd756_smbus** : i2c_adapter (line 286)
- static **chipname** : const char * [] (line 293)
- static **smbus_algorithm** : const struct i2c_algorithm (line 281)

## Macros (34)

- **AMD756_BLOCK_DATA** (line 70)
- **AMD756_BYTE** (line 66)
- **AMD756_BYTE_DATA** (line 67)
- **AMD756_PROCESS_CALL** (line 69)
- **AMD756_QUICK** (line 65)
- **AMD756_WORD_DATA** (line 68)
- **GE_ABORT** (line 93)
- **GE_CYC_TYPE_MASK** (line 91)
- **GE_HOST_STC** (line 92)
- **GS_ABRT_STS** (line 80)
- **GS_CLEAR_STS** (line 88)
- **GS_COL_STS** (line 81)
- **GS_HCYC_STS** (line 84)
- **GS_HST_STS** (line 83)
- **GS_PRERR_STS** (line 82)
- **GS_SMB_STS** (line 86)
- **GS_TO_STS** (line 85)
- **MAX_TIMEOUT** (line 62)
- **SMBBA** (line 52)
- **SMBBANFORCE** (line 53)
- **SMBGCFG** (line 56)
- **SMBREV** (line 59)
- **SMB_ADDR_OFFSET** (line 36)
- **SMB_GLOBAL_ENABLE** (line 39)
- **SMB_GLOBAL_STATUS** (line 38)
- **SMB_HAS_DATA** (line 44)
- **SMB_HAS_DEVICE_ADDRESS** (line 45)
- **SMB_HAS_HOST_ADDRESS** (line 46)
- **SMB_HOST_ADDRESS** (line 40)
- **SMB_HOST_BLOCK_DATA** (line 43)
- **SMB_HOST_COMMAND** (line 42)
- **SMB_HOST_DATA** (line 41)
- **SMB_IOSIZE** (line 37)
- **SMB_SNOOP_ADDRESS** (line 47)
