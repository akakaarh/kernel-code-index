# drivers/mmc/host/sdhci-bcm-kona.c

Subsystem: drivers/mmc

## Functions (7)

### sdhci_bcm_kona_card_event
- Return type: static void
- Signature: sdhci_bcm_kona_card_event(struct sdhci_host * host)
- Line: 151

### sdhci_bcm_kona_init_74_clocks
- Return type: static void
- Signature: sdhci_bcm_kona_init_74_clocks(struct sdhci_host * host,u8 power_mode)
- Line: 164

### sdhci_bcm_kona_probe
- Return type: static int
- Signature: sdhci_bcm_kona_probe(struct platform_device * pdev)
- Line: 203

### sdhci_bcm_kona_remove
- Return type: static void
- Signature: sdhci_bcm_kona_remove(struct platform_device * pdev)
- Line: 311

### sdhci_bcm_kona_sd_card_emulate
- Return type: static int
- Signature: sdhci_bcm_kona_sd_card_emulate(struct sdhci_host * host,int insert)
- Line: 112

### sdhci_bcm_kona_sd_init
- Return type: static void
- Signature: sdhci_bcm_kona_sd_init(struct sdhci_host * host)
- Line: 83

### sdhci_bcm_kona_sd_reset
- Return type: static int
- Signature: sdhci_bcm_kona_sd_reset(struct sdhci_host * host)
- Line: 47

## Structs (1)

### sdhci_bcm_kona_dev
- Line: 42
- Members:
  - write_lock: mutex

## Variables (4)

- static **sdhci_bcm_kona_driver** : platform_driver (line 321)
- static **sdhci_bcm_kona_of_match** : const struct of_device_id[] (line 196)
- static **sdhci_bcm_kona_ops** : const struct sdhci_ops (line 176)
- static **sdhci_pltfm_data_kona** : const struct sdhci_pltfm_data (line 187)

## Macros (17)

- **KONA_MMC_AUTOSUSPEND_DELAY** (line 40)
- **KONA_SDHOST_CD_PINCTRL** (line 21)
- **KONA_SDHOST_CD_SW** (line 28)
- **KONA_SDHOST_CORECTRL** (line 20)
- **KONA_SDHOST_COREDBG1** (line 35)
- **KONA_SDHOST_COREGPO_MASK** (line 36)
- **KONA_SDHOST_COREIMR** (line 30)
- **KONA_SDHOST_COREIMSR** (line 34)
- **KONA_SDHOST_COREISR** (line 33)
- **KONA_SDHOST_CORESTAT** (line 26)
- **KONA_SDHOST_EN** (line 24)
- **KONA_SDHOST_IP** (line 31)
- **KONA_SDHOST_RESET** (line 23)
- **KONA_SDHOST_STOP_HCLK** (line 22)
- **KONA_SDHOST_WP** (line 27)
- **SDHCI_SOFT_RESET** (line 19)
- **SD_DETECT_GPIO_DEBOUNCE_128MS** (line 38)
