# drivers/i2c/busses/i2c-pxa-pci.c

Subsystem: drivers/i2c

## Functions (2)

### add_i2c_device
- Return type: static platform_device *
- Signature: add_i2c_device(struct pci_dev * dev,int bar)
- Line: 23

### ce4100_i2c_probe
- Return type: static int
- Signature: ce4100_i2c_probe(struct pci_dev * dev,const struct pci_device_id * ent)
- Line: 100

## Structs (1)

### ce4100_devices
- Line: 19
- Members:
  - pdev: platform_device * []

## Variables (2)

- static **ce4100_i2c_devices** : const struct pci_device_id[] (line 136)
- static **ce4100_i2c_driver** : pci_driver (line 141)

## Macros (1)

- **CE4100_PCI_I2C_DEVS** (line 17)
