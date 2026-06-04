# drivers/mmc/host/sdhci-pltfm.c

Subsystem: drivers/mmc

## Functions (9)

### sdhci_get_compatibility
- Return type: static void
- Signature: sdhci_get_compatibility(struct platform_device * pdev)
- Line: 56

### sdhci_get_property
- Return type: void
- Signature: sdhci_get_property(struct platform_device * pdev)
- Line: 71

### sdhci_pltfm_clk_get_max_clock
- Return type: unsigned int
- Signature: sdhci_pltfm_clk_get_max_clock(struct sdhci_host * host)
- Line: 27

### sdhci_pltfm_init
- Return type: sdhci_host *
- Signature: sdhci_pltfm_init(struct platform_device * pdev,const struct sdhci_pltfm_data * pdata,size_t priv_size)
- Line: 101

### sdhci_pltfm_init_and_add_host
- Return type: int
- Signature: sdhci_pltfm_init_and_add_host(struct platform_device * pdev,const struct sdhci_pltfm_data * pdata,size_t priv_size)
- Line: 142

### sdhci_pltfm_remove
- Return type: void
- Signature: sdhci_pltfm_remove(struct platform_device * pdev)
- Line: 158

### sdhci_pltfm_resume
- Return type: int
- Signature: sdhci_pltfm_resume(struct device * dev)
- Line: 187

### sdhci_pltfm_suspend
- Return type: int
- Signature: sdhci_pltfm_suspend(struct device * dev)
- Line: 168

### sdhci_wp_inverted
- Return type: static bool
- Signature: sdhci_wp_inverted(struct device * dev)
- Line: 42

## Variables (2)

- static **sdhci_pltfm_ops** : const struct sdhci_ops (line 35)
- **sdhci_pltfm_pmops** : const struct dev_pm_ops (line 206)
