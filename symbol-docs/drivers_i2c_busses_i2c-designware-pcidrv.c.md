# drivers/i2c/busses/i2c-designware-pcidrv.c

Subsystem: drivers/i2c

## Functions (8)

### ehl_get_clk_rate_khz
- Return type: static u32
- Signature: ehl_get_clk_rate_khz(struct dw_i2c_dev * dev)
- Line: 143

### i2c_dw_pci_probe
- Return type: static int
- Signature: i2c_dw_pci_probe(struct pci_dev * pdev,const struct pci_device_id * id)
- Line: 207

### i2c_dw_pci_remove
- Return type: static void
- Signature: i2c_dw_pci_remove(struct pci_dev * pdev)
- Line: 296

### mfld_get_clk_rate_khz
- Return type: static u32
- Signature: mfld_get_clk_rate_khz(struct dw_i2c_dev * dev)
- Line: 98

### mfld_setup
- Return type: static int
- Signature: mfld_setup(struct pci_dev * pdev,struct dw_pci_controller * c)
- Line: 103

### mrfld_setup
- Return type: static int
- Signature: mrfld_setup(struct pci_dev * pdev,struct dw_pci_controller * c)
- Line: 124

### navi_amd_get_clk_rate_khz
- Return type: static u32
- Signature: navi_amd_get_clk_rate_khz(struct dw_i2c_dev * dev)
- Line: 148

### navi_amd_setup
- Return type: static int
- Signature: navi_amd_setup(struct pci_dev * pdev,struct dw_pci_controller * c)
- Line: 153

## Structs (2)

### dw_pci_controller
- Line: 57
- Members:
  - ss_hcnt: u16
  - fs_hcnt: u16
  - ss_lcnt: u16
  - fs_lcnt: u16
  - sda_hold_time: u32
  - bus_num: u32
  - flags: u32
  - scl_sda_cfg: dw_scl_sda_cfg *
  - setup: int (*)(struct pci_dev * pdev,struct dw_pci_controller * c)
  - get_clk_rate_khz: u32 (*)(struct dw_i2c_dev * dev)

### dw_scl_sda_cfg
- Line: 49
- Members:
  - ss_hcnt: u16
  - fs_hcnt: u16
  - ss_lcnt: u16
  - fs_lcnt: u16
  - sda_hold_time: u32
  - bus_num: u32
  - flags: u32
  - scl_sda_cfg: dw_scl_sda_cfg *
  - setup: int (*)(struct pci_dev * pdev,struct dw_pci_controller * c)
  - get_clk_rate_khz: u32 (*)(struct dw_i2c_dev * dev)

## Enums (1)

### dw_pci_ctl_id_t
- Line: 32

## Variables (9)

- static **byt_config** : dw_scl_sda_cfg (line 74)
- static **dgpu_node** : const struct software_node (line 203)
- static **dgpu_properties** : const struct property_entry[] (line 197)
- static **dw_i2c_driver** : pci_driver (line 359)
- static **dw_pci_controllers** : dw_pci_controller[] (line 162)
- static **hsw_config** : dw_scl_sda_cfg (line 83)
- static **i2c_designware_pci_ids** : const struct pci_device_id[] (line 309)
- static **mrfld_config** : dw_scl_sda_cfg (line 66)
- static **navi_amd_config** : dw_scl_sda_cfg (line 92)

## Macros (1)

- **DRIVER_NAME** (line 30)
