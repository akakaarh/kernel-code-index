# drivers/mmc/host/sdhci-of-k1.c

Subsystem: drivers/mmc

## Functions (15)

### spacemit_sdhci_clk_get_max_clock
- Return type: static unsigned int
- Signature: spacemit_sdhci_clk_get_max_clock(struct sdhci_host * host)
- Line: 170

### spacemit_sdhci_clrbits
- Return type: static void
- Signature: spacemit_sdhci_clrbits(struct sdhci_host * host,u32 val,int reg)
- Line: 75

### spacemit_sdhci_clrsetbits
- Return type: static void
- Signature: spacemit_sdhci_clrsetbits(struct sdhci_host * host,u32 clr,u32 set,int reg)
- Line: 80

### spacemit_sdhci_get_clocks
- Return type: static int
- Signature: spacemit_sdhci_get_clocks(struct device * dev,struct sdhci_pltfm_host * pltfm_host)
- Line: 209

### spacemit_sdhci_get_resets
- Return type: static int
- Signature: spacemit_sdhci_get_resets(struct device * dev)
- Line: 227

### spacemit_sdhci_hs400_enhanced_strobe
- Return type: static void
- Signature: spacemit_sdhci_hs400_enhanced_strobe(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 157

### spacemit_sdhci_phy_dll_init
- Return type: static void
- Signature: spacemit_sdhci_phy_dll_init(struct sdhci_host * host)
- Line: 132

### spacemit_sdhci_post_select_hs400
- Return type: static void
- Signature: spacemit_sdhci_post_select_hs400(struct mmc_host * mmc)
- Line: 186

### spacemit_sdhci_pre_hs400_to_hs200
- Return type: static void
- Signature: spacemit_sdhci_pre_hs400_to_hs200(struct mmc_host * mmc)
- Line: 193

### spacemit_sdhci_pre_select_hs400
- Return type: static int
- Signature: spacemit_sdhci_pre_select_hs400(struct mmc_host * mmc)
- Line: 177

### spacemit_sdhci_probe
- Return type: static int
- Signature: spacemit_sdhci_probe(struct platform_device * pdev)
- Line: 280

### spacemit_sdhci_reset
- Return type: static void
- Signature: spacemit_sdhci_reset(struct sdhci_host * host,u8 mask)
- Line: 88

### spacemit_sdhci_set_clock
- Return type: static void
- Signature: spacemit_sdhci_set_clock(struct sdhci_host * host,unsigned int clock)
- Line: 120

### spacemit_sdhci_set_uhs_signaling
- Return type: static void
- Signature: spacemit_sdhci_set_uhs_signaling(struct sdhci_host * host,unsigned int timing)
- Line: 106

### spacemit_sdhci_setbits
- Return type: static void
- Signature: spacemit_sdhci_setbits(struct sdhci_host * host,u32 val,int reg)
- Line: 70

## Structs (1)

### spacemit_sdhci_host
- Line: 64
- Members:
  - clk_core: clk *
  - clk_io: clk *

## Variables (5)

- static **spacemit_sdhci_driver** : platform_driver (line 332)
- static **spacemit_sdhci_k1_pdata** : const struct sdhci_pltfm_data (line 250)
- static **spacemit_sdhci_k3_pdata** : const struct sdhci_pltfm_data (line 262)
- static **spacemit_sdhci_of_match** : const struct of_device_id[] (line 273)
- static **spacemit_sdhci_ops** : const struct sdhci_ops (line 242)

## Macros (32)

- **SDHC_DLL_ENABLE** (line 49)
- **SDHC_DLL_FULLDLY_RANGE** (line 47)
- **SDHC_DLL_LOCK_STATE** (line 58)
- **SDHC_DLL_PREDLY_NUM** (line 46)
- **SDHC_DLL_REG1_CTRL** (line 52)
- **SDHC_DLL_REG2_CTRL** (line 53)
- **SDHC_DLL_REG3_CTRL** (line 54)
- **SDHC_DLL_REG4_CTRL** (line 55)
- **SDHC_DLL_VREG_CTRL** (line 48)
- **SDHC_ENHANCE_STROBE_EN** (line 27)
- **SDHC_HOST_LEGACY_MODE** (line 39)
- **SDHC_HS200_USE_RFIFO** (line 43)
- **SDHC_MISC_INT** (line 26)
- **SDHC_MISC_INT_EN** (line 25)
- **SDHC_MMC_CARD_MODE** (line 30)
- **SDHC_MMC_HS200** (line 29)
- **SDHC_MMC_HS400** (line 28)
- **SDHC_PHY_DRIVE_SEL** (line 61)
- **SDHC_PHY_FUNC_EN** (line 37)
- **SDHC_PHY_PLL_LOCK** (line 38)
- **SDHC_PHY_TEST_EN** (line 42)
- **SDHC_RX_BIAS_CTRL** (line 62)
- **SDHC_TX_INT_CLK_SEL** (line 33)
- **SDHC_TX_MUX_SEL** (line 34)
- **SPACEMIT_SDHC_MMC_CTRL_REG** (line 24)
- **SPACEMIT_SDHC_PHY_CTRL_REG** (line 36)
- **SPACEMIT_SDHC_PHY_DLLCFG** (line 45)
- **SPACEMIT_SDHC_PHY_DLLCFG1** (line 51)
- **SPACEMIT_SDHC_PHY_DLLSTS** (line 57)
- **SPACEMIT_SDHC_PHY_FUNC_REG** (line 41)
- **SPACEMIT_SDHC_PHY_PADCFG_REG** (line 60)
- **SPACEMIT_SDHC_TX_CFG_REG** (line 32)
