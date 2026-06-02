# drivers/i2c/busses/i2c-piix4.c

Subsystem: drivers/i2c

## Functions (21)

### piix4_access
- Return type: static s32
- Signature: piix4_access(struct i2c_adapter * adap,u16 addr,unsigned short flags,char read_write,u8 command,int size,union i2c_smbus_data * data)
- Line: 597

### piix4_access_sb800
- Return type: static s32
- Signature: piix4_access_sb800(struct i2c_adapter * adap,u16 addr,unsigned short flags,char read_write,u8 command,int size,union i2c_smbus_data * data)
- Line: 780

### piix4_adap_remove
- Return type: static void
- Signature: piix4_adap_remove(struct i2c_adapter * adap)
- Line: 1116

### piix4_add_adapter
- Return type: static int
- Signature: piix4_add_adapter(struct pci_dev * dev,unsigned short smba,bool sb800_main,u8 port,bool notify_imc,u8 hw_port_nr,const char * name,struct i2c_adapter ** padap)
- Line: 913

### piix4_add_adapters_sb800
- Return type: static int
- Signature: piix4_add_adapters_sb800(struct pci_dev * dev,unsigned short smba,bool notify_imc)
- Line: 980

### piix4_func
- Return type: static u32
- Signature: piix4_func(struct i2c_adapter * adapter)
- Line: 866

### piix4_imc_read
- Return type: static uint8_t
- Signature: piix4_imc_read(uint8_t idx)
- Line: 687

### piix4_imc_sleep
- Return type: static int
- Signature: piix4_imc_sleep(void)
- Line: 699

### piix4_imc_wakeup
- Return type: static void
- Signature: piix4_imc_wakeup(void)
- Line: 725

### piix4_imc_write
- Return type: static void
- Signature: piix4_imc_write(uint8_t idx,uint8_t value)
- Line: 693

### piix4_probe
- Return type: static int
- Signature: piix4_probe(struct pci_dev * dev,const struct pci_device_id * id)
- Line: 1024

### piix4_remove
- Return type: static void
- Signature: piix4_remove(struct pci_dev * dev)
- Line: 1129

### piix4_sb800_port_sel
- Return type: int
- Signature: piix4_sb800_port_sel(u8 port,struct sb800_mmio_cfg * mmio_cfg)
- Line: 748

### piix4_sb800_region_release
- Return type: void
- Signature: piix4_sb800_region_release(struct device * dev,struct sb800_mmio_cfg * mmio_cfg)
- Line: 200

### piix4_sb800_region_request
- Return type: int
- Signature: piix4_sb800_region_request(struct device * dev,struct sb800_mmio_cfg * mmio_cfg)
- Line: 160

### piix4_sb800_use_mmio
- Return type: static bool
- Signature: piix4_sb800_use_mmio(struct pci_dev * PIIX4_dev)
- Line: 213

### piix4_setup
- Return type: static int
- Signature: piix4_setup(struct pci_dev * PIIX4_dev,const struct pci_device_id * id)
- Line: 225

### piix4_setup_aux
- Return type: static int
- Signature: piix4_setup_aux(struct pci_dev * PIIX4_dev,const struct pci_device_id * id,unsigned short base_reg_addr)
- Line: 481

### piix4_setup_sb800
- Return type: static int
- Signature: piix4_setup_sb800(struct pci_dev * PIIX4_dev,const struct pci_device_id * id,u8 aux)
- Line: 371

### piix4_setup_sb800_smba
- Return type: static int
- Signature: piix4_setup_sb800_smba(struct pci_dev * PIIX4_dev,u8 smb_en,u8 aux,u8 * smb_en_status,unsigned short * piix4_smba)
- Line: 324

### piix4_transaction
- Return type: int
- Signature: piix4_transaction(struct i2c_adapter * piix4_adapter,unsigned short piix4_smba)
- Line: 521

## Structs (1)

### i2c_piix4_adapdata
- Line: 150
- Members:
  - smba: unsigned short
  - sb800_main: bool
  - notify_imc: bool
  - port: u8
  - mmio_cfg: sb800_mmio_cfg

## Variables (18)

- static **force** : int (line 96)
- static **force_addr** : int (line 102)
- static **piix4_adapter_count** : int (line 911)
- static **piix4_aux_adapter** : i2c_adapter * (line 910)
- static **piix4_aux_port_name_sb800** : const char * (line 148)
- static **piix4_dmi_blacklist** : const struct dmi_system_id[] (line 111)
- static **piix4_dmi_ibm** : const struct dmi_system_id[] (line 131)
- static **piix4_driver** : pci_driver (line 1146)
- static **piix4_driver** : pci_driver (line 109)
- static **piix4_ids** : const struct pci_device_id[] (line 883)
- static **piix4_main_adapters** : i2c_adapter * [] (line 909)
- static **piix4_main_port_names_sb800** : const char * [] (line 145)
- static **piix4_port_mask_sb800** : u8 (line 143)
- static **piix4_port_sel_sb800** : u8 (line 142)
- static **piix4_port_shift_sb800** : u8 (line 144)
- static **piix4_smbus_algorithm_sb800** : const struct i2c_algorithm (line 878)
- static **smbus_algorithm** : const struct i2c_algorithm (line 873)
- static **srvrworks_csb5_delay** : int (line 108)

## Macros (29)

- **ENABLE_INT9** (line 54)
- **HUDSON2_MAIN_PORTS** (line 64)
- **KERNCZ_IMC_DATA** (line 71)
- **KERNCZ_IMC_IDX** (line 70)
- **MAX_TIMEOUT** (line 53)
- **PIIX4_BYTE** (line 58)
- **PIIX4_BYTE_DATA** (line 59)
- **PIIX4_MAX_ADAPTERS** (line 63)
- **PIIX4_QUICK** (line 57)
- **PIIX4_WORD_DATA** (line 60)
- **SB800_ASF_ACPI_PATH** (line 90)
- **SB800_PIIX4_FCH_PM_SIZE** (line 89)
- **SB800_PIIX4_PORT_IDX** (line 78)
- **SB800_PIIX4_PORT_IDX_ALT** (line 79)
- **SB800_PIIX4_PORT_IDX_KERNCZ** (line 85)
- **SB800_PIIX4_PORT_IDX_MASK** (line 81)
- **SB800_PIIX4_PORT_IDX_MASK_KERNCZ** (line 86)
- **SB800_PIIX4_PORT_IDX_SEL** (line 80)
- **SB800_PIIX4_PORT_IDX_SHIFT** (line 82)
- **SB800_PIIX4_PORT_IDX_SHIFT_KERNCZ** (line 87)
- **SB800_PIIX4_SMB_IDX** (line 67)
- **SB800_PIIX4_SMB_MAP_SIZE** (line 68)
- **SMBBA** (line 45)
- **SMBHSTCFG** (line 46)
- **SMBIOSIZE** (line 42)
- **SMBREV** (line 50)
- **SMBSHDW1** (line 48)
- **SMBSHDW2** (line 49)
- **SMBSLVC** (line 47)
