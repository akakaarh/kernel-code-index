# drivers/mmc/host/sdhci-dove.c

Subsystem: drivers/mmc

## Functions (3)

### sdhci_dove_probe
- Return type: static int
- Signature: sdhci_dove_probe(struct platform_device * pdev)
- Line: 67

### sdhci_dove_readl
- Return type: static u32
- Signature: sdhci_dove_readl(struct sdhci_host * host,int reg)
- Line: 34

### sdhci_dove_readw
- Return type: static u16
- Signature: sdhci_dove_readw(struct sdhci_host * host,int reg)
- Line: 19

## Variables (4)

- static **sdhci_dove_driver** : platform_driver (line 93)
- static **sdhci_dove_of_match_table** : const struct of_device_id[] (line 87)
- static **sdhci_dove_ops** : const struct sdhci_ops (line 49)
- static **sdhci_dove_pdata** : const struct sdhci_pltfm_data (line 58)
