# drivers/mmc/host/sdhci-spear.c

Subsystem: drivers/mmc

## Functions (4)

### sdhci_probe
- Return type: static int
- Signature: sdhci_probe(struct platform_device * pdev)
- Line: 43

### sdhci_remove
- Return type: static void
- Signature: sdhci_remove(struct platform_device * pdev)
- Line: 118

### sdhci_resume
- Return type: static int
- Signature: sdhci_resume(struct device * dev)
- Line: 149

### sdhci_suspend
- Return type: static int
- Signature: sdhci_suspend(struct device * dev)
- Line: 133

## Structs (1)

### spear_sdhci
- Line: 31
- Members:
  - clk: clk *

## Variables (3)

- static **sdhci_driver** : platform_driver (line 172)
- static **sdhci_pltfm_ops** : const struct sdhci_ops (line 36)
- static **sdhci_spear_id_table** : const struct of_device_id[] (line 166)
