# drivers/spi/spi-amd-pci.c

Subsystem: drivers/spi

## Functions (1)

### amd_spi_pci_probe
- Return type: static int
- Signature: amd_spi_pci_probe(struct pci_dev * pdev,const struct pci_device_id * id)
- Line: 30

## Variables (2)

- static **amd_spi_pci_driver** : pci_driver (line 60)
- static **pci_spi_ids** : pci_device_id[] (line 24)

## Macros (5)

- **AMD_HID2_MEM_SIZE** (line 22)
- **AMD_HID2_PCI_BAR_OFFSET** (line 21)
- **AMD_PCI_DEVICE_ID_LPC_BRIDGE** (line 18)
- **AMD_PCI_LPC_SPI_BASE_ADDR_REG** (line 19)
- **AMD_SPI_BASE_ADDR_MASK** (line 20)
