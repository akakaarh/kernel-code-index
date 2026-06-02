# drivers/spi/spi-intel-pci.c

Subsystem: drivers/spi

## Functions (2)

### intel_spi_pci_probe
- Return type: static int
- Signature: intel_spi_pci_probe(struct pci_dev * pdev,const struct pci_device_id * id)
- Line: 43

### intel_spi_pci_set_writeable
- Return type: static bool
- Signature: intel_spi_pci_set_writeable(void __iomem * base,void * data)
- Line: 17

## Variables (4)

- static **bxt_info** : const struct intel_spi_boardinfo (line 33)
- static **cnl_info** : const struct intel_spi_boardinfo (line 38)
- static **intel_spi_pci_driver** : pci_driver (line 106)
- static **intel_spi_pci_ids** : const struct pci_device_id[] (line 68)

## Macros (2)

- **BCR** (line 14)
- **BCR_WPD** (line 15)
