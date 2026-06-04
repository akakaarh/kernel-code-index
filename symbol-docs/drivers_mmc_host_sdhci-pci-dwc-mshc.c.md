# drivers/mmc/host/sdhci-pci-dwc-mshc.c

Subsystem: drivers/mmc

## Functions (1)

### sdhci_snps_set_clock
- Return type: static void
- Signature: sdhci_snps_set_clock(struct sdhci_host * host,unsigned int clock)
- Line: 31

## Variables (2)

- **sdhci_snps** : const struct sdhci_pci_fixes (line 82)
- static **sdhci_snps_ops** : const struct sdhci_ops (line 74)

## Macros (11)

- **CLKFBOUT_100_MHZ** (line 27)
- **CLKFBOUT_200_MHZ** (line 28)
- **DIV_REG_100_MHZ** (line 24)
- **DIV_REG_200_MHZ** (line 25)
- **SDHCI_VENDOR_PTR_R** (line 15)
- **SDHC_AT_CTRL_R** (line 19)
- **SDHC_CCLK_MMCM_RST** (line 29)
- **SDHC_GPIO_OUT** (line 18)
- **SDHC_MMCM_CLKFBOUT** (line 26)
- **SDHC_MMCM_DIV_REG** (line 23)
- **SDHC_SW_TUNE_EN** (line 20)
