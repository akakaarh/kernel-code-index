# drivers/i2c/busses/i2c-via.c

Subsystem: drivers/i2c

## Functions (6)

### bit_via_getscl
- Return type: static int
- Signature: bit_via_getscl(void * data)
- Line: 51

### bit_via_getsda
- Return type: static int
- Signature: bit_via_getsda(void * data)
- Line: 56

### bit_via_setscl
- Return type: static void
- Signature: bit_via_setscl(void * data,int state)
- Line: 41

### bit_via_setsda
- Return type: static void
- Signature: bit_via_setsda(void * data,int state)
- Line: 46

### vt586b_probe
- Return type: static int
- Signature: vt586b_probe(struct pci_dev * dev,const struct pci_device_id * id)
- Line: 86

### vt586b_remove
- Return type: static void
- Signature: vt586b_remove(struct pci_dev * dev)
- Line: 135

## Variables (6)

- static **bit_data** : i2c_algo_bit_data (line 62)
- static **pm_io_base** : u16 (line 32)
- static **vt586b_adapter** : i2c_adapter (line 71)
- static **vt586b_driver** : pci_driver (line 143)
- static **vt586b_driver** : pci_driver (line 31)
- static **vt586b_ids** : const struct pci_device_id[] (line 79)

## Macros (9)

- **I2C_DIR** (line 22)
- **I2C_IN** (line 24)
- **I2C_OUT** (line 23)
- **I2C_SCL** (line 25)
- **I2C_SDA** (line 26)
- **IOSPACE** (line 29)
- **PM_CFG_IOBASE0** (line 19)
- **PM_CFG_IOBASE1** (line 20)
- **PM_CFG_REVID** (line 18)
