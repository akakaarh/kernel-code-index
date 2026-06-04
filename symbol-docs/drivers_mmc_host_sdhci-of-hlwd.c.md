# drivers/mmc/host/sdhci-of-hlwd.c

Subsystem: drivers/mmc

## Functions (4)

### sdhci_hlwd_probe
- Return type: static int
- Signature: sdhci_hlwd_probe(struct platform_device * pdev)
- Line: 69

### sdhci_hlwd_writeb
- Return type: static void
- Signature: sdhci_hlwd_writeb(struct sdhci_host * host,u8 val,int reg)
- Line: 44

### sdhci_hlwd_writel
- Return type: static void
- Signature: sdhci_hlwd_writel(struct sdhci_host * host,u32 val,int reg)
- Line: 32

### sdhci_hlwd_writew
- Return type: static void
- Signature: sdhci_hlwd_writew(struct sdhci_host * host,u16 val,int reg)
- Line: 38

## Variables (4)

- static **sdhci_hlwd_driver** : platform_driver (line 80)
- static **sdhci_hlwd_of_match** : const struct of_device_id[] (line 74)
- static **sdhci_hlwd_ops** : const struct sdhci_ops (line 50)
- static **sdhci_hlwd_pdata** : const struct sdhci_pltfm_data (line 63)

## Macros (1)

- **SDHCI_HLWD_WRITE_DELAY** (line 30)
