# drivers/spi/spi-cavium-thunderx.c

Subsystem: drivers/spi

## Functions (2)

### thunderx_spi_probe
- Return type: static int
- Signature: thunderx_spi_probe(struct pci_dev * pdev,const struct pci_device_id * ent)
- Line: 19

### thunderx_spi_remove
- Return type: static void
- Signature: thunderx_spi_remove(struct pci_dev * pdev)
- Line: 84

## Variables (2)

- static **thunderx_spi_driver** : pci_driver (line 110)
- static **thunderx_spi_pci_id_table** : const struct pci_device_id[] (line 103)

## Macros (2)

- **DRV_NAME** (line 15)
- **SYS_FREQ_DEFAULT** (line 17)
