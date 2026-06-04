# drivers/mmc/host/sdhci-of-at91.c

Subsystem: drivers/mmc

## Functions (10)

### sdhci_at91_probe
- Return type: static int
- Signature: sdhci_at91_probe(struct platform_device * pdev)
- Line: 308

### sdhci_at91_remove
- Return type: static void
- Signature: sdhci_at91_remove(struct platform_device * pdev)
- Line: 432

### sdhci_at91_reset
- Return type: static void
- Signature: sdhci_at91_reset(struct sdhci_host * host,u8 mask)
- Line: 113

### sdhci_at91_runtime_resume
- Return type: static int
- Signature: sdhci_at91_runtime_resume(struct device * dev)
- Line: 264

### sdhci_at91_runtime_suspend
- Return type: static int
- Signature: sdhci_at91_runtime_suspend(struct device * dev)
- Line: 246

### sdhci_at91_set_clks_presets
- Return type: static int
- Signature: sdhci_at91_set_clks_presets(struct device * dev)
- Line: 167

### sdhci_at91_set_clock
- Return type: static void
- Signature: sdhci_at91_set_clock(struct sdhci_host * host,unsigned int clock)
- Line: 62

### sdhci_at91_set_force_card_detect
- Return type: static void
- Signature: sdhci_at91_set_force_card_detect(struct sdhci_host * host)
- Line: 53

### sdhci_at91_set_uhs_signaling
- Return type: static void
- Signature: sdhci_at91_set_uhs_signaling(struct sdhci_host * host,unsigned int timing)
- Line: 100

### sdhci_at91_suspend
- Return type: static int
- Signature: sdhci_at91_suspend(struct device * dev)
- Line: 232

## Structs (2)

### sdhci_at91_priv
- Line: 44
- Members:
  - pdata: const struct sdhci_pltfm_data *
  - baseclk_is_generated_internally: bool
  - divider_for_baseclk: unsigned int
  - soc_data: const struct sdhci_at91_soc_data *
  - hclock: clk *
  - gck: clk *
  - mainck: clk *
  - restore_needed: bool
  - cal_always_on: bool

### sdhci_at91_soc_data
- Line: 38
- Members:
  - pdata: const struct sdhci_pltfm_data *
  - baseclk_is_generated_internally: bool
  - divider_for_baseclk: unsigned int
  - soc_data: const struct sdhci_at91_soc_data *
  - hclock: clk *
  - gck: clk *
  - mainck: clk *
  - restore_needed: bool
  - cal_always_on: bool

## Variables (7)

- static **sdhci_at91_dev_pm_ops** : const struct dev_pm_ops (line 303)
- static **sdhci_at91_driver** : platform_driver (line 452)
- static **sdhci_at91_dt_match** : const struct of_device_id[] (line 160)
- static **sdhci_at91_sama5d2_ops** : const struct sdhci_ops (line 137)
- static **sdhci_sama5d2_pdata** : const struct sdhci_pltfm_data (line 145)
- static **soc_data_sam9x60** : const struct sdhci_at91_soc_data (line 154)
- static **soc_data_sama5d2** : const struct sdhci_at91_soc_data (line 149)

## Macros (10)

- **SDHCI_AT91_PRESET_COMMON_CONF** (line 36)
- **SDMMC_CACR** (line 29)
- **SDMMC_CACR_CAPWREN** (line 30)
- **SDMMC_CACR_KEY** (line 31)
- **SDMMC_CALCR** (line 32)
- **SDMMC_CALCR_ALWYSON** (line 34)
- **SDMMC_CALCR_EN** (line 33)
- **SDMMC_MC1R** (line 26)
- **SDMMC_MC1R_DDR** (line 27)
- **SDMMC_MC1R_FCD** (line 28)
