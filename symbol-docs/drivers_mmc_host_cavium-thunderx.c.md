# drivers/mmc/host/cavium-thunderx.c

Subsystem: drivers/mmc

## Functions (6)

### thunder_mmc_acquire_bus
- Return type: static void
- Signature: thunder_mmc_acquire_bus(struct cvm_mmc_host * host)
- Line: 21

### thunder_mmc_int_enable
- Return type: static void
- Signature: thunder_mmc_int_enable(struct cvm_mmc_host * host,u64 val)
- Line: 31

### thunder_mmc_probe
- Return type: static int
- Signature: thunder_mmc_probe(struct pci_dev * pdev,const struct pci_device_id * id)
- Line: 57

### thunder_mmc_register_interrupts
- Return type: static int
- Signature: thunder_mmc_register_interrupts(struct cvm_mmc_host * host,struct pci_dev * pdev)
- Line: 37

### thunder_mmc_release_bus
- Return type: static void
- Signature: thunder_mmc_release_bus(struct cvm_mmc_host * host)
- Line: 26

### thunder_mmc_remove
- Return type: static void
- Signature: thunder_mmc_remove(struct pci_dev * pdev)
- Line: 170

## Variables (2)

- static **thunder_mmc_driver** : pci_driver (line 192)
- static **thunder_mmc_id_table** : const struct pci_device_id[] (line 187)
