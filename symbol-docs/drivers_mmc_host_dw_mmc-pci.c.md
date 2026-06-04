# drivers/mmc/host/dw_mmc-pci.c

Subsystem: drivers/mmc

## Functions (2)

### dw_mci_pci_probe
- Return type: static int
- Signature: dw_mci_pci_probe(struct pci_dev * pdev,const struct pci_device_id * entries)
- Line: 32

### dw_mci_pci_remove
- Return type: static void
- Signature: dw_mci_pci_remove(struct pci_dev * pdev)
- Line: 68

## Variables (3)

- static **dw_mci_pci_driver** : pci_driver (line 81)
- static **dw_mci_pci_id** : const struct pci_device_id[] (line 75)
- static **pci_drv_data** : const struct dw_mci_drv_data (line 28)

## Macros (3)

- **DW_MCI_CAPABILITIES** (line 24)
- **SYNOPSYS_DW_MCI_DEVICE_ID** (line 22)
- **SYNOPSYS_DW_MCI_VENDOR_ID** (line 21)
