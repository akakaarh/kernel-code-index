# drivers/i2c/busses/i2c-ismt.c

Subsystem: drivers/i2c

## Functions (17)

### __ismt_desc_dump
- Return type: static void
- Signature: __ismt_desc_dump(struct device * dev,const struct ismt_desc * desc)
- Line: 205

### ismt_access
- Return type: static int
- Signature: ismt_access(struct i2c_adapter * adap,u16 addr,unsigned short flags,char read_write,u8 command,int size,union i2c_smbus_data * data)
- Line: 403

### ismt_desc_dump
- Return type: static void
- Signature: ismt_desc_dump(struct ismt_priv * priv)
- Line: 224

### ismt_dev_init
- Return type: static int
- Signature: ismt_dev_init(struct ismt_priv * priv)
- Line: 807

### ismt_do_interrupt
- Return type: static irqreturn_t
- Signature: ismt_do_interrupt(int vec,void * data)
- Line: 690

### ismt_do_msi_interrupt
- Return type: static irqreturn_t
- Signature: ismt_do_msi_interrupt(int vec,void * data)
- Line: 715

### ismt_func
- Return type: static u32
- Signature: ismt_func(struct i2c_adapter * adap)
- Line: 655

### ismt_gen_reg_dump
- Return type: static void
- Signature: ismt_gen_reg_dump(struct ismt_priv * priv)
- Line: 237

### ismt_handle_isr
- Return type: static irqreturn_t
- Signature: ismt_handle_isr(struct ismt_priv * priv)
- Line: 677

### ismt_hw_init
- Return type: static void
- Signature: ismt_hw_init(struct ismt_priv * priv)
- Line: 724

### ismt_int_init
- Return type: static int
- Signature: ismt_int_init(struct ismt_priv * priv)
- Line: 834

### ismt_kill_transaction
- Return type: static void
- Signature: ismt_kill_transaction(struct ismt_priv * priv)
- Line: 388

### ismt_mstr_reg_dump
- Return type: static void
- Signature: ismt_mstr_reg_dump(struct ismt_priv * priv)
- Line: 266

### ismt_probe
- Return type: static int
- Signature: ismt_probe(struct pci_dev * pdev,const struct pci_device_id * id)
- Line: 883

### ismt_process_desc
- Return type: static int
- Signature: ismt_process_desc(const struct ismt_desc * desc,union i2c_smbus_data * data,struct ismt_priv * priv,int size,char read_write)
- Line: 324

### ismt_remove
- Return type: static void
- Signature: ismt_remove(struct pci_dev * pdev)
- Line: 976

### ismt_submit_desc
- Return type: static void
- Signature: ismt_submit_desc(struct ismt_priv * priv)
- Line: 295

## Structs (2)

### ismt_desc
- Line: 157
- Members:
  - tgtaddr_rw: u8
  - wr_len_cmd: u8
  - rd_len: u8
  - control: u8
  - status: u8
  - retry: u8
  - rxbytes: u8
  - txbytes: u8
  - dptr_low: u32
  - dptr_high: u32
  - adapter: i2c_adapter
  - smba: void __iomem *
  - pci_dev: pci_dev *
  - hw: ismt_desc *
  - io_rng_dma: dma_addr_t
  - head: u8
  - cmp: completion
  - buffer: u8[]
  - log_dma: dma_addr_t
  - log: u32 *

### ismt_priv
- Line: 170
- Members:
  - tgtaddr_rw: u8
  - wr_len_cmd: u8
  - rd_len: u8
  - control: u8
  - status: u8
  - retry: u8
  - rxbytes: u8
  - txbytes: u8
  - dptr_low: u32
  - dptr_high: u32
  - adapter: i2c_adapter
  - smba: void __iomem *
  - pci_dev: pci_dev *
  - hw: ismt_desc *
  - io_rng_dma: dma_addr_t
  - head: u8
  - cmp: completion
  - buffer: u8[]
  - log_dma: dma_addr_t
  - log: u32 *

## Variables (6)

- **__packed** : ismt_desc (line 168)
- static **bus_speed** : unsigned int (line 196)
- static **ismt_driver** : pci_driver (line 983)
- static **ismt_driver** : pci_driver (line 875)
- static **ismt_ids** : const struct pci_device_id[] (line 183)
- static **smbus_algorithm** : const struct i2c_algorithm (line 668)

## Macros (54)

- **ISMT_DESC_ADDR_RW**(addr,rw) (line 106)
- **ISMT_DESC_BLK** (line 89)
- **ISMT_DESC_CLTO** (line 101)
- **ISMT_DESC_COL** (line 102)
- **ISMT_DESC_CRC** (line 100)
- **ISMT_DESC_CWRL** (line 88)
- **ISMT_DESC_DLTO** (line 98)
- **ISMT_DESC_ENTRIES** (line 83)
- **ISMT_DESC_FAIR** (line 90)
- **ISMT_DESC_I2C** (line 92)
- **ISMT_DESC_INT** (line 93)
- **ISMT_DESC_LPR** (line 103)
- **ISMT_DESC_NAK** (line 99)
- **ISMT_DESC_PEC** (line 91)
- **ISMT_DESC_SCS** (line 97)
- **ISMT_DESC_SOE** (line 94)
- **ISMT_GCTRL_KILL** (line 128)
- **ISMT_GCTRL_SRST** (line 129)
- **ISMT_GCTRL_TRST** (line 127)
- **ISMT_GR_ERRAERMSK** (line 112)
- **ISMT_GR_ERRINFO** (line 114)
- **ISMT_GR_ERRINTMSK** (line 111)
- **ISMT_GR_ERRSTS** (line 113)
- **ISMT_GR_GCTRL** (line 109)
- **ISMT_GR_SMTICL** (line 110)
- **ISMT_LOG_ENTRIES** (line 85)
- **ISMT_MAX_RETRIES** (line 84)
- **ISMT_MCTRL_FMHP** (line 134)
- **ISMT_MCTRL_MEIE** (line 133)
- **ISMT_MCTRL_SS** (line 132)
- **ISMT_MDS_MASK** (line 143)
- **ISMT_MSICTL_MSIE** (line 154)
- **ISMT_MSTR_MCTRL** (line 118)
- **ISMT_MSTR_MDBA** (line 117)
- **ISMT_MSTR_MDS** (line 120)
- **ISMT_MSTR_MSTS** (line 119)
- **ISMT_MSTR_RPOLICY** (line 121)
- **ISMT_MSTS_HMTP** (line 137)
- **ISMT_MSTS_IP** (line 140)
- **ISMT_MSTS_MEIS** (line 139)
- **ISMT_MSTS_MIS** (line 138)
- **ISMT_SPGT** (line 124)
- **ISMT_SPGT_SPD_100K** (line 148)
- **ISMT_SPGT_SPD_1M** (line 150)
- **ISMT_SPGT_SPD_400K** (line 149)
- **ISMT_SPGT_SPD_80K** (line 147)
- **ISMT_SPGT_SPD_MASK** (line 146)
- **PCI_DEVICE_ID_INTEL_AVOTON_SMT** (line 81)
- **PCI_DEVICE_ID_INTEL_CDF_SMT** (line 78)
- **PCI_DEVICE_ID_INTEL_DNV_SMT** (line 79)
- **PCI_DEVICE_ID_INTEL_EBG_SMT** (line 80)
- **PCI_DEVICE_ID_INTEL_S1200_SMT0** (line 76)
- **PCI_DEVICE_ID_INTEL_S1200_SMT1** (line 77)
- **SMBBAR** (line 73)
