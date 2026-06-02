# drivers/spi/spi-pxa2xx-pci.c

Subsystem: drivers/spi

## Functions (10)

### ce4100_spi_setup
- Return type: static int
- Signature: ce4100_spi_setup(struct pci_dev * dev,struct pxa2xx_spi_controller * c)
- Line: 177

### lpss_dma_filter
- Return type: static bool
- Signature: lpss_dma_filter(struct dma_chan * chan,void * param)
- Line: 80

### lpss_dma_put_device
- Return type: static void
- Signature: lpss_dma_put_device(void * dma_dev)
- Line: 91

### lpss_spi_setup
- Return type: static int
- Signature: lpss_spi_setup(struct pci_dev * dev,struct pxa2xx_spi_controller * c)
- Line: 96

### mrfld_spi_setup
- Return type: static int
- Signature: mrfld_spi_setup(struct pci_dev * dev,struct pxa2xx_spi_controller * c)
- Line: 192

### pxa2xx_spi_pci_clk_register
- Return type: static int
- Signature: pxa2xx_spi_pci_clk_register(struct pci_dev * dev,struct ssp_device * ssp,unsigned long rate)
- Line: 67

### pxa2xx_spi_pci_clk_unregister
- Return type: static void
- Signature: pxa2xx_spi_pci_clk_unregister(void * clk)
- Line: 62

### pxa2xx_spi_pci_probe
- Return type: static int
- Signature: pxa2xx_spi_pci_probe(struct pci_dev * dev,const struct pci_device_id * ent)
- Line: 264

### pxa2xx_spi_pci_remove
- Return type: static void
- Signature: pxa2xx_spi_pci_remove(struct pci_dev * dev)
- Line: 311

### qrk_spi_setup
- Return type: static int
- Signature: qrk_spi_setup(struct pci_dev * dev,struct pxa2xx_spi_controller * c)
- Line: 249

## Structs (1)

### pxa_spi_info
- Line: 36
- Members:
  - setup: int (*)(struct pci_dev * pdev,struct pxa2xx_spi_controller * c)

## Variables (24)

- static **bsw0_rx_param** : dw_dma_slave (line 51)
- static **bsw0_tx_param** : dw_dma_slave (line 50)
- static **bsw1_rx_param** : dw_dma_slave (line 53)
- static **bsw1_tx_param** : dw_dma_slave (line 52)
- static **bsw2_rx_param** : dw_dma_slave (line 55)
- static **bsw2_tx_param** : dw_dma_slave (line 54)
- static **byt_rx_param** : dw_dma_slave (line 41)
- static **byt_tx_param** : dw_dma_slave (line 40)
- static **ce4100_info_config** : const struct pxa_spi_info (line 188)
- static **lpss_info_config** : const struct pxa_spi_info (line 173)
- static **lpt0_rx_param** : dw_dma_slave (line 60)
- static **lpt0_tx_param** : dw_dma_slave (line 59)
- static **lpt1_rx_param** : dw_dma_slave (line 58)
- static **lpt1_tx_param** : dw_dma_slave (line 57)
- static **mrfld3_rx_param** : dw_dma_slave (line 44)
- static **mrfld3_tx_param** : dw_dma_slave (line 43)
- static **mrfld5_rx_param** : dw_dma_slave (line 46)
- static **mrfld5_tx_param** : dw_dma_slave (line 45)
- static **mrfld6_rx_param** : dw_dma_slave (line 48)
- static **mrfld6_tx_param** : dw_dma_slave (line 47)
- static **mrfld_info_config** : const struct pxa_spi_info (line 245)
- static **pxa2xx_spi_pci_devices** : const struct pci_device_id[] (line 319)
- static **pxa2xx_spi_pci_driver** : pci_driver (line 335)
- static **qrk_info_config** : const struct pxa_spi_info (line 260)

## Macros (11)

- **PCI_DEVICE_ID_INTEL_BSW0** (line 27)
- **PCI_DEVICE_ID_INTEL_BSW1** (line 28)
- **PCI_DEVICE_ID_INTEL_BSW2** (line 29)
- **PCI_DEVICE_ID_INTEL_BYT** (line 25)
- **PCI_DEVICE_ID_INTEL_CE4100** (line 30)
- **PCI_DEVICE_ID_INTEL_LPT0_0** (line 31)
- **PCI_DEVICE_ID_INTEL_LPT0_1** (line 32)
- **PCI_DEVICE_ID_INTEL_LPT1_0** (line 33)
- **PCI_DEVICE_ID_INTEL_LPT1_1** (line 34)
- **PCI_DEVICE_ID_INTEL_MRFLD** (line 26)
- **PCI_DEVICE_ID_INTEL_QUARK_X1000** (line 24)
