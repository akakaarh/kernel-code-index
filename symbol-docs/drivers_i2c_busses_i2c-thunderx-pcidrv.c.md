# drivers/i2c/busses/i2c-thunderx-pcidrv.c

Subsystem: drivers/i2c

## Functions (12)

### thunder_i2c_clock_disable
- Return type: static void
- Signature: thunder_i2c_clock_disable(struct device * dev,struct clk * clk)
- Line: 112

### thunder_i2c_clock_enable
- Return type: static void
- Signature: thunder_i2c_clock_enable(struct device * dev,struct octeon_i2c * i2c)
- Line: 85

### thunder_i2c_hlc_int_disable
- Return type: static void
- Signature: thunder_i2c_hlc_int_disable(struct octeon_i2c * i2c)
- Line: 62

### thunder_i2c_hlc_int_enable
- Return type: static void
- Signature: thunder_i2c_hlc_int_enable(struct octeon_i2c * i2c)
- Line: 56

### thunder_i2c_int_disable
- Return type: static void
- Signature: thunder_i2c_int_disable(struct octeon_i2c * i2c)
- Line: 50

### thunder_i2c_int_enable
- Return type: static void
- Signature: thunder_i2c_int_enable(struct octeon_i2c * i2c)
- Line: 41

### thunder_i2c_probe_pci
- Return type: static int
- Signature: thunder_i2c_probe_pci(struct pci_dev * pdev,const struct pci_device_id * ent)
- Line: 156

### thunder_i2c_remove_pci
- Return type: static void
- Signature: thunder_i2c_remove_pci(struct pci_dev * pdev)
- Line: 250

### thunder_i2c_smbus_remove
- Return type: static void
- Signature: thunder_i2c_smbus_remove(struct octeon_i2c * i2c)
- Line: 151

### thunder_i2c_smbus_setup
- Return type: static int
- Signature: thunder_i2c_smbus_setup(struct octeon_i2c * i2c,struct device_node * node)
- Line: 141

### thunder_i2c_smbus_setup_of
- Return type: static int
- Signature: thunder_i2c_smbus_setup_of(struct octeon_i2c * i2c,struct device_node * node)
- Line: 120

### thunderx_i2c_functionality
- Return type: static u32
- Signature: thunderx_i2c_functionality(struct i2c_adapter * adap)
- Line: 68

## Variables (4)

- static **thunder_i2c_pci_driver** : pci_driver (line 266)
- static **thunder_i2c_pci_id_table** : const struct pci_device_id[] (line 259)
- static **thunderx_i2c_algo** : const struct i2c_algorithm (line 74)
- static **thunderx_i2c_ops** : const struct i2c_adapter (line 79)

## Macros (6)

- **DRV_NAME** (line 26)
- **OTX2_REF_FREQ_DEFAULT** (line 31)
- **PCI_DEVICE_ID_THUNDER_TWSI** (line 28)
- **SYS_FREQ_DEFAULT** (line 30)
- **TWSI_INT_ENA_W1C** (line 33)
- **TWSI_INT_ENA_W1S** (line 34)
