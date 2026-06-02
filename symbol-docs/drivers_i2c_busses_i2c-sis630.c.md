# drivers/i2c/busses/i2c-sis630.c

Subsystem: drivers/i2c

## Functions (12)

### sis630_access
- Return type: static s32
- Signature: sis630_access(struct i2c_adapter * adap,u16 addr,unsigned short flags,char read_write,u8 command,int size,union i2c_smbus_data * data)
- Line: 323

### sis630_block_data
- Return type: static int
- Signature: sis630_block_data(struct i2c_adapter * adap,union i2c_smbus_data * data,int read_write)
- Line: 229

### sis630_func
- Return type: static u32
- Signature: sis630_func(struct i2c_adapter * adapter)
- Line: 397

### sis630_probe
- Return type: static int
- Signature: sis630_probe(struct pci_dev * dev,const struct pci_device_id * id)
- Line: 510

### sis630_read
- Return type: static u8
- Signature: sis630_read(u8 reg)
- Line: 111

### sis630_remove
- Return type: static void
- Signature: sis630_remove(struct pci_dev * dev)
- Line: 538

### sis630_setup
- Return type: static int
- Signature: sis630_setup(struct pci_dev * sis630_dev)
- Line: 404

### sis630_transaction
- Return type: static int
- Signature: sis630_transaction(struct i2c_adapter * adap,int size)
- Line: 215

### sis630_transaction_end
- Return type: static void
- Signature: sis630_transaction_end(struct i2c_adapter * adap,u8 oldclock)
- Line: 196

### sis630_transaction_start
- Return type: static int
- Signature: sis630_transaction_start(struct i2c_adapter * adap,int size,u8 * oldclock)
- Line: 121

### sis630_transaction_wait
- Return type: static int
- Signature: sis630_transaction_wait(struct i2c_adapter * adap,int size)
- Line: 164

### sis630_write
- Return type: static void
- Signature: sis630_write(u8 reg,u8 data)
- Line: 116

## Variables (9)

- static **force** : bool (line 93)
- static **high_clock** : bool (line 92)
- static **sis630_adapter** : i2c_adapter (line 494)
- static **sis630_driver** : pci_driver (line 548)
- static **sis630_driver** : pci_driver (line 89)
- static **sis630_ids** : const struct pci_device_id[] (line 501)
- static **smbus_algorithm** : const struct i2c_algorithm (line 489)
- static **smbus_base** : unsigned short (line 101)
- static **supported** : int[] (line 104)

## Macros (27)

- **BYTE_DONE_STS** (line 53)
- **MAX_TIMEOUT** (line 79)
- **MSTO_EN** (line 58)
- **PCI_DEVICE_ID_SI_964** (line 41)
- **SIS630_ACPI_BASE_REG** (line 74)
- **SIS630_BIOS_CTL_REG** (line 76)
- **SIS630_BLOCK_DATA** (line 87)
- **SIS630_BYTE** (line 83)
- **SIS630_BYTE_DATA** (line 84)
- **SIS630_PCALL** (line 86)
- **SIS630_QUICK** (line 82)
- **SIS630_SMB_IOREGION** (line 70)
- **SIS630_WORD_DATA** (line 85)
- **SMBCLK_SEL** (line 59)
- **SMBCOL_STS** (line 54)
- **SMBERR_STS** (line 55)
- **SMBHOST_CNT** (line 46)
- **SMB_ADDR** (line 47)
- **SMB_BYTE** (line 50)
- **SMB_CMD** (line 48)
- **SMB_CNT** (line 45)
- **SMB_COUNT** (line 49)
- **SMB_HOSTBUSY** (line 61)
- **SMB_KILL** (line 64)
- **SMB_PROBE** (line 60)
- **SMB_START** (line 65)
- **SMB_STS** (line 44)
