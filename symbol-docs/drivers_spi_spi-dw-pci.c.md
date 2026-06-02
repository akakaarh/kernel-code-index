# drivers/spi/spi-dw-pci.c

Subsystem: drivers/spi

## Functions (6)

### dw_spi_pci_generic_init
- Return type: static int
- Signature: dw_spi_pci_generic_init(struct dw_spi * dws)
- Line: 56

### dw_spi_pci_mid_init
- Return type: static int
- Signature: dw_spi_pci_mid_init(struct dw_spi * dws)
- Line: 34

### dw_spi_pci_probe
- Return type: static int
- Signature: dw_spi_pci_probe(struct pci_dev * pdev,const struct pci_device_id * ent)
- Line: 82

### dw_spi_pci_remove
- Return type: static void
- Signature: dw_spi_pci_remove(struct pci_dev * pdev)
- Line: 152

### dw_spi_pci_resume
- Return type: static int
- Signature: dw_spi_pci_resume(struct device * dev)
- Line: 171

### dw_spi_pci_suspend
- Return type: static int
- Signature: dw_spi_pci_suspend(struct device * dev)
- Line: 164

## Structs (1)

### dw_spi_pci_desc
- Line: 27
- Members:
  - setup: int (*)(struct dw_spi *)
  - num_cs: u16
  - bus_num: u16
  - max_freq: u32

## Variables (5)

- static **dw_spi_pci_driver** : pci_driver (line 200)
- static **dw_spi_pci_ehl_desc** : dw_spi_pci_desc (line 75)
- static **dw_spi_pci_ids** : const struct pci_device_id[] (line 181)
- static **dw_spi_pci_mid_desc_1** : dw_spi_pci_desc (line 63)
- static **dw_spi_pci_mid_desc_2** : dw_spi_pci_desc (line 69)

## Macros (8)

- **CLK_SPI_BDIV_MASK** (line 22)
- **CLK_SPI_BDIV_OFFSET** (line 21)
- **CLK_SPI_CDIV_MASK** (line 24)
- **CLK_SPI_CDIV_OFFSET** (line 23)
- **CLK_SPI_DISABLE_OFFSET** (line 25)
- **DRIVER_NAME** (line 16)
- **MRST_CLK_SPI_REG** (line 20)
- **MRST_SPI_CLK_BASE** (line 19)
