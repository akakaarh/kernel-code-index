# drivers/i2c/busses/i2c-nforce2.c

Subsystem: drivers/i2c

## Functions (7)

### nforce2_abort
- Return type: static void
- Signature: nforce2_abort(struct i2c_adapter * adap)
- Line: 120

### nforce2_access
- Return type: static s32
- Signature: nforce2_access(struct i2c_adapter * adap,u16 addr,unsigned short flags,char read_write,u8 command,int size,union i2c_smbus_data * data)
- Line: 164

### nforce2_check_status
- Return type: static int
- Signature: nforce2_check_status(struct i2c_adapter * adap)
- Line: 139

### nforce2_func
- Return type: static u32
- Signature: nforce2_func(struct i2c_adapter * adapter)
- Line: 267

### nforce2_probe
- Return type: static int
- Signature: nforce2_probe(struct pci_dev * dev,const struct pci_device_id * id)
- Line: 356

### nforce2_probe_smb
- Return type: static int
- Signature: nforce2_probe_smb(struct pci_dev * dev,int bar,int alt_reg,struct nforce2_smbus * smbus,const char * name)
- Line: 304

### nforce2_remove
- Return type: static void
- Signature: nforce2_remove(struct pci_dev * dev)
- Line: 404

## Structs (1)

### nforce2_smbus
- Line: 54
- Members:
  - adapter: i2c_adapter
  - base: int
  - size: int
  - blockops: int
  - can_abort: int

## Variables (5)

- static **nforce2_dmi_blacklist2** : const struct dmi_system_id[] (line 107)
- static **nforce2_driver** : pci_driver (line 419)
- static **nforce2_driver** : pci_driver (line 118)
- static **nforce2_ids** : const struct pci_device_id[] (line 283)
- static **smbus_algorithm** : const struct i2c_algorithm (line 277)

## Macros (25)

- **MAX_TIMEOUT** (line 104)
- **NFORCE_PCI_SMB1** (line 67)
- **NFORCE_PCI_SMB2** (line 68)
- **NVIDIA_SMB_ADDR** (line 76)
- **NVIDIA_SMB_BCNT** (line 79)
- **NVIDIA_SMB_CMD** (line 77)
- **NVIDIA_SMB_CTRL** (line 84)
- **NVIDIA_SMB_CTRL_ABORT** (line 88)
- **NVIDIA_SMB_DATA** (line 78)
- **NVIDIA_SMB_PRTCL** (line 74)
- **NVIDIA_SMB_PRTCL_BLOCK_DATA** (line 100)
- **NVIDIA_SMB_PRTCL_BYTE** (line 97)
- **NVIDIA_SMB_PRTCL_BYTE_DATA** (line 98)
- **NVIDIA_SMB_PRTCL_PEC** (line 101)
- **NVIDIA_SMB_PRTCL_QUICK** (line 96)
- **NVIDIA_SMB_PRTCL_READ** (line 95)
- **NVIDIA_SMB_PRTCL_WORD_DATA** (line 99)
- **NVIDIA_SMB_PRTCL_WRITE** (line 94)
- **NVIDIA_SMB_STATUS_ABRT** (line 81)
- **NVIDIA_SMB_STATUS_ABRT_STS** (line 86)
- **NVIDIA_SMB_STS** (line 75)
- **NVIDIA_SMB_STS_ALRM** (line 90)
- **NVIDIA_SMB_STS_DONE** (line 89)
- **NVIDIA_SMB_STS_RES** (line 91)
- **NVIDIA_SMB_STS_STATUS** (line 92)
