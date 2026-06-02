# drivers/i2c/busses/i2c-amd8111.c

Subsystem: drivers/i2c

## Functions (8)

### amd8111_access
- Return type: static s32
- Signature: amd8111_access(struct i2c_adapter * adap,u16 addr,unsigned short flags,char read_write,u8 command,int size,union i2c_smbus_data * data)
- Line: 189

### amd8111_func
- Return type: static u32
- Signature: amd8111_func(struct i2c_adapter * adapter)
- Line: 400

### amd8111_probe
- Return type: static int
- Signature: amd8111_probe(struct pci_dev * dev,const struct pci_device_id * id)
- Line: 422

### amd8111_remove
- Return type: static void
- Signature: amd8111_remove(struct pci_dev * dev)
- Line: 464

### amd_ec_read
- Return type: static int
- Signature: amd_ec_read(struct amd_smbus * smbus,unsigned char address,unsigned char * data)
- Line: 100

### amd_ec_wait_read
- Return type: static int
- Signature: amd_ec_wait_read(struct amd_smbus * smbus)
- Line: 84

### amd_ec_wait_write
- Return type: static int
- Signature: amd_ec_wait_write(struct amd_smbus * smbus)
- Line: 68

### amd_ec_write
- Return type: static int
- Signature: amd_ec_write(struct amd_smbus * smbus,unsigned char address,unsigned char data)
- Line: 123

## Structs (1)

### amd_smbus
- Line: 23
- Members:
  - dev: pci_dev *
  - adapter: i2c_adapter
  - base: int
  - size: int

## Variables (4)

- static **amd8111_driver** : pci_driver (line 471)
- static **amd8111_driver** : pci_driver (line 30)
- static **amd8111_ids** : const struct pci_device_id[] (line 415)
- static **smbus_algorithm** : const struct i2c_algorithm (line 409)

## Macros (53)

- **AMD_EC_CMD** (line 48)
- **AMD_EC_CMD_BD** (line 61)
- **AMD_EC_CMD_BE** (line 60)
- **AMD_EC_CMD_QR** (line 62)
- **AMD_EC_CMD_RD** (line 58)
- **AMD_EC_CMD_WR** (line 59)
- **AMD_EC_DATA** (line 46)
- **AMD_EC_ICR** (line 49)
- **AMD_EC_SC** (line 47)
- **AMD_EC_SC_BURST** (line 53)
- **AMD_EC_SC_CMD** (line 54)
- **AMD_EC_SC_IBF** (line 55)
- **AMD_EC_SC_OBF** (line 56)
- **AMD_EC_SC_SCI** (line 52)
- **AMD_EC_SC_SMI** (line 51)
- **AMD_PCI_MISC** (line 36)
- **AMD_PCI_MISC_INT** (line 39)
- **AMD_PCI_MISC_SCI** (line 38)
- **AMD_PCI_MISC_SPEEDUP** (line 40)
- **AMD_SMB_ADDR** (line 152)
- **AMD_SMB_ALRM_A** (line 156)
- **AMD_SMB_ALRM_D** (line 157)
- **AMD_SMB_BCNT** (line 155)
- **AMD_SMB_CMD** (line 153)
- **AMD_SMB_DATA** (line 154)
- **AMD_SMB_PRTCL** (line 150)
- **AMD_SMB_PRTCL_BLOCK_DATA** (line 182)
- **AMD_SMB_PRTCL_BLOCK_PROC_CALL** (line 184)
- **AMD_SMB_PRTCL_BYTE** (line 179)
- **AMD_SMB_PRTCL_BYTE_DATA** (line 180)
- **AMD_SMB_PRTCL_I2C_BLOCK_DATA** (line 185)
- **AMD_SMB_PRTCL_PEC** (line 186)
- **AMD_SMB_PRTCL_PROC_CALL** (line 183)
- **AMD_SMB_PRTCL_QUICK** (line 178)
- **AMD_SMB_PRTCL_READ** (line 177)
- **AMD_SMB_PRTCL_WORD_DATA** (line 181)
- **AMD_SMB_PRTCL_WRITE** (line 176)
- **AMD_SMB_STATUS_ACC_DENY** (line 170)
- **AMD_SMB_STATUS_BUSY** (line 173)
- **AMD_SMB_STATUS_CMD_DENY** (line 168)
- **AMD_SMB_STATUS_DERR** (line 167)
- **AMD_SMB_STATUS_DNAK** (line 166)
- **AMD_SMB_STATUS_FAIL** (line 165)
- **AMD_SMB_STATUS_NOTSUP** (line 172)
- **AMD_SMB_STATUS_OK** (line 164)
- **AMD_SMB_STATUS_PEC** (line 174)
- **AMD_SMB_STATUS_TIMEOUT** (line 171)
- **AMD_SMB_STATUS_UNKNOWN** (line 169)
- **AMD_SMB_STS** (line 151)
- **AMD_SMB_STS_ALRM** (line 160)
- **AMD_SMB_STS_DONE** (line 159)
- **AMD_SMB_STS_RES** (line 161)
- **AMD_SMB_STS_STATUS** (line 162)
