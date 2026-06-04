# drivers/mmc/host/sdhci-of-sparx5.c

Subsystem: drivers/mmc

## Functions (7)

### sdhci_sparx5_adma_write_desc
- Return type: static void
- Signature: sdhci_sparx5_adma_write_desc(struct sdhci_host * host,void ** desc,dma_addr_t addr,int len,unsigned int cmd)
- Line: 52

### sdhci_sparx5_probe
- Return type: static int
- Signature: sdhci_sparx5_probe(struct platform_device * pdev)
- Line: 158

### sdhci_sparx5_reset
- Return type: static void
- Signature: sdhci_sparx5_reset(struct sdhci_host * host,u8 mask)
- Line: 132

### sdhci_sparx5_reset_emmc
- Return type: static void
- Signature: sdhci_sparx5_reset_emmc(struct sdhci_host * host)
- Line: 116

### sdhci_sparx5_set_emmc
- Return type: static void
- Signature: sdhci_sparx5_set_emmc(struct sdhci_host * host)
- Line: 101

### sparx5_set_cacheable
- Return type: static void
- Signature: sparx5_set_cacheable(struct sdhci_host * host,u32 value)
- Line: 75

### sparx5_set_delay
- Return type: static void
- Signature: sparx5_set_delay(struct sdhci_host * host,u8 value)
- Line: 87

## Structs (1)

### sdhci_sparx5_data
- Line: 39
- Members:
  - host: sdhci_host *
  - cpu_ctrl: regmap *
  - delay_clock: int

## Variables (4)

- static **sdhci_sparx5_driver** : platform_driver (line 242)
- static **sdhci_sparx5_of_match** : const struct of_device_id[] (line 236)
- static **sdhci_sparx5_ops** : const struct sdhci_ops (line 142)
- static **sdhci_sparx5_pdata** : const struct sdhci_pltfm_data (line 151)

## Macros (15)

- **ACP_ARCACHE** (line 30)
- **ACP_AWCACHE** (line 29)
- **ACP_CACHE_FORCE_ENA** (line 28)
- **ACP_CACHE_MASK** (line 31)
- **BOUNDARY_OK**(addr,len) (line 45)
- **CPU_REGS_GENERAL_CTRL** (line 22)
- **CPU_REGS_PROC_CTRL** (line 27)
- **MSHC2_EMMC_CTRL** (line 35)
- **MSHC2_EMMC_CTRL_EMMC_RST_N** (line 36)
- **MSHC2_EMMC_CTRL_IS_EMMC** (line 37)
- **MSHC2_TYPE** (line 34)
- **MSHC2_VERSION** (line 33)
- **MSHC_DLY_CC_MASK** (line 23)
- **MSHC_DLY_CC_MAX** (line 25)
- **MSHC_DLY_CC_SHIFT** (line 24)
