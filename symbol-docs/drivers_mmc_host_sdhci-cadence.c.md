# drivers/mmc/host/sdhci-cadence.c

Subsystem: drivers/mmc

## Functions (22)

### cdns_writel
- Return type: static void
- Signature: cdns_writel(struct sdhci_cdns_priv * priv,u32 val,void __iomem * reg)
- Line: 121

### elba_drv_init
- Return type: static int
- Signature: elba_drv_init(struct platform_device * pdev)
- Line: 452

### elba_priv_writel
- Return type: static void
- Signature: elba_priv_writel(struct sdhci_cdns_priv * priv,u32 val,void __iomem * reg)
- Line: 397

### elba_write_b
- Return type: static void
- Signature: elba_write_b(struct sdhci_host * host,u8 val,int reg)
- Line: 427

### elba_write_l
- Return type: static void
- Signature: elba_write_l(struct sdhci_host * host,u32 val,int reg)
- Line: 408

### elba_write_w
- Return type: static void
- Signature: elba_write_w(struct sdhci_host * host,u16 val,int reg)
- Line: 413

### sdhci_cdns_execute_tuning
- Return type: static int
- Signature: sdhci_cdns_execute_tuning(struct sdhci_host * host,u32 opcode)
- Line: 313

### sdhci_cdns_get_emmc_mode
- Return type: static u32
- Signature: sdhci_cdns_get_emmc_mode(struct sdhci_cdns_priv * priv)
- Line: 231

### sdhci_cdns_get_timeout_clock
- Return type: static unsigned int
- Signature: sdhci_cdns_get_timeout_clock(struct sdhci_host * host)
- Line: 211

### sdhci_cdns_hs400_enhanced_strobe
- Return type: static void
- Signature: sdhci_cdns_hs400_enhanced_strobe(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 509

### sdhci_cdns_mmc_hw_reset
- Return type: static void
- Signature: sdhci_cdns_mmc_hw_reset(struct mmc_host * mmc)
- Line: 529

### sdhci_cdns_phy_init
- Return type: static int
- Signature: sdhci_cdns_phy_init(struct sdhci_cdns_priv * priv)
- Line: 190

### sdhci_cdns_phy_param_count
- Return type: static unsigned int
- Signature: sdhci_cdns_phy_param_count(struct device_node * np)
- Line: 159

### sdhci_cdns_phy_param_parse
- Return type: static void
- Signature: sdhci_cdns_phy_param_parse(struct device_node * np,struct sdhci_cdns_priv * priv)
- Line: 171

### sdhci_cdns_priv
- Return type: static void *
- Signature: sdhci_cdns_priv(struct sdhci_host * host)
- Line: 204

### sdhci_cdns_probe
- Return type: static int
- Signature: sdhci_cdns_probe(struct platform_device * pdev)
- Line: 545

### sdhci_cdns_resume
- Return type: static int
- Signature: sdhci_cdns_resume(struct device * dev)
- Line: 614

### sdhci_cdns_set_emmc_mode
- Return type: static void
- Signature: sdhci_cdns_set_emmc_mode(struct sdhci_cdns_priv * priv,u32 mode)
- Line: 220

### sdhci_cdns_set_tune_val
- Return type: static int
- Signature: sdhci_cdns_set_tune_val(struct sdhci_host * host,unsigned int val)
- Line: 239

### sdhci_cdns_set_uhs_signaling
- Return type: static void
- Signature: sdhci_cdns_set_uhs_signaling(struct sdhci_host * host,unsigned int timing)
- Line: 354

### sdhci_cdns_tune_blkgap
- Return type: static int
- Signature: sdhci_cdns_tune_blkgap(struct mmc_host * mmc)
- Line: 282

### sdhci_cdns_write_phy_reg
- Return type: static int
- Signature: sdhci_cdns_write_phy_reg(struct sdhci_cdns_priv * priv,u8 addr,u8 data)
- Line: 127

## Structs (4)

### sdhci_cdns_drv_data
- Line: 102
- Members:
  - addr: u8
  - data: u8
  - hrs_addr: void __iomem *
  - ctl_addr: void __iomem *
  - wrlock: spinlock_t
  - enhanced_strobe: bool
  - priv_writel: void (*)(struct sdhci_cdns_priv * priv,u32 val,void __iomem * reg)
  - rst_hw: reset_control *
  - nr_phy_params: unsigned int
  - phy_params: sdhci_cdns_phy_param[]
  - property: const char *
  - addr: u8
  - init: int (*)(struct platform_device * pdev)
  - pltfm_data: const struct sdhci_pltfm_data

### sdhci_cdns_phy_cfg
- Line: 97
- Members:
  - addr: u8
  - data: u8
  - hrs_addr: void __iomem *
  - ctl_addr: void __iomem *
  - wrlock: spinlock_t
  - enhanced_strobe: bool
  - priv_writel: void (*)(struct sdhci_cdns_priv * priv,u32 val,void __iomem * reg)
  - rst_hw: reset_control *
  - nr_phy_params: unsigned int
  - phy_params: sdhci_cdns_phy_param[]
  - property: const char *
  - addr: u8
  - init: int (*)(struct platform_device * pdev)
  - pltfm_data: const struct sdhci_pltfm_data

### sdhci_cdns_phy_param
- Line: 81
- Members:
  - addr: u8
  - data: u8
  - hrs_addr: void __iomem *
  - ctl_addr: void __iomem *
  - wrlock: spinlock_t
  - enhanced_strobe: bool
  - priv_writel: void (*)(struct sdhci_cdns_priv * priv,u32 val,void __iomem * reg)
  - rst_hw: reset_control *
  - nr_phy_params: unsigned int
  - phy_params: sdhci_cdns_phy_param[]
  - property: const char *
  - addr: u8
  - init: int (*)(struct platform_device * pdev)
  - pltfm_data: const struct sdhci_pltfm_data

### sdhci_cdns_priv
- Line: 86
- Members:
  - addr: u8
  - data: u8
  - hrs_addr: void __iomem *
  - ctl_addr: void __iomem *
  - wrlock: spinlock_t
  - enhanced_strobe: bool
  - priv_writel: void (*)(struct sdhci_cdns_priv * priv,u32 val,void __iomem * reg)
  - rst_hw: reset_control *
  - nr_phy_params: unsigned int
  - phy_params: sdhci_cdns_phy_param[]
  - property: const char *
  - addr: u8
  - init: int (*)(struct platform_device * pdev)
  - pltfm_data: const struct sdhci_pltfm_data

## Variables (9)

- static **sdhci_cdns_driver** : platform_driver (line 661)
- static **sdhci_cdns_drv_data** : const struct sdhci_cdns_drv_data (line 503)
- static **sdhci_cdns_match** : const struct of_device_id[] (line 643)
- static **sdhci_cdns_ops** : const struct sdhci_ops (line 473)
- static **sdhci_cdns_phy_cfgs** : const struct sdhci_cdns_phy_cfg[] (line 107)
- static **sdhci_cdns_uniphier_drv_data** : const struct sdhci_cdns_drv_data (line 482)
- static **sdhci_elba_drv_data** : const struct sdhci_cdns_drv_data (line 489)
- static **sdhci_elba_ops** : const struct sdhci_ops (line 441)
- static **sdhci_eyeq_drv_data** : const struct sdhci_cdns_drv_data (line 496)

## Macros (48)

- **ELBA_BYTE_ENABLE_MASK**(x) (line 389)
- **SDHCI_CDNS_HRS04** (line 20)
- **SDHCI_CDNS_HRS04_ACK** (line 21)
- **SDHCI_CDNS_HRS04_ADDR** (line 26)
- **SDHCI_CDNS_HRS04_RD** (line 22)
- **SDHCI_CDNS_HRS04_RDATA** (line 24)
- **SDHCI_CDNS_HRS04_WDATA** (line 25)
- **SDHCI_CDNS_HRS04_WR** (line 23)
- **SDHCI_CDNS_HRS06** (line 28)
- **SDHCI_CDNS_HRS06_MODE** (line 31)
- **SDHCI_CDNS_HRS06_MODE_MMC_DDR** (line 34)
- **SDHCI_CDNS_HRS06_MODE_MMC_HS200** (line 35)
- **SDHCI_CDNS_HRS06_MODE_MMC_HS400** (line 36)
- **SDHCI_CDNS_HRS06_MODE_MMC_HS400ES** (line 37)
- **SDHCI_CDNS_HRS06_MODE_MMC_SDR** (line 33)
- **SDHCI_CDNS_HRS06_MODE_SD** (line 32)
- **SDHCI_CDNS_HRS06_TUNE** (line 30)
- **SDHCI_CDNS_HRS06_TUNE_UP** (line 29)
- **SDHCI_CDNS_HRS37** (line 40)
- **SDHCI_CDNS_HRS37_MODE_DS** (line 41)
- **SDHCI_CDNS_HRS37_MODE_HS** (line 42)
- **SDHCI_CDNS_HRS37_MODE_MMC_DDR** (line 50)
- **SDHCI_CDNS_HRS37_MODE_MMC_HS200** (line 51)
- **SDHCI_CDNS_HRS37_MODE_MMC_HS400** (line 52)
- **SDHCI_CDNS_HRS37_MODE_MMC_HS400ES** (line 53)
- **SDHCI_CDNS_HRS37_MODE_MMC_LEGACY** (line 48)
- **SDHCI_CDNS_HRS37_MODE_MMC_SDR** (line 49)
- **SDHCI_CDNS_HRS37_MODE_UDS_DDR50** (line 47)
- **SDHCI_CDNS_HRS37_MODE_UDS_SDR104** (line 46)
- **SDHCI_CDNS_HRS37_MODE_UDS_SDR12** (line 43)
- **SDHCI_CDNS_HRS37_MODE_UDS_SDR25** (line 44)
- **SDHCI_CDNS_HRS37_MODE_UDS_SDR50** (line 45)
- **SDHCI_CDNS_HRS38** (line 54)
- **SDHCI_CDNS_HRS38_BLKGAP_MAX** (line 55)
- **SDHCI_CDNS_MAX_TUNING_LOOP** (line 79)
- **SDHCI_CDNS_PHY_DLY_EMMC_DDR** (line 69)
- **SDHCI_CDNS_PHY_DLY_EMMC_LEGACY** (line 67)
- **SDHCI_CDNS_PHY_DLY_EMMC_SDR** (line 68)
- **SDHCI_CDNS_PHY_DLY_HSMMC** (line 71)
- **SDHCI_CDNS_PHY_DLY_SDCLK** (line 70)
- **SDHCI_CDNS_PHY_DLY_SD_DEFAULT** (line 62)
- **SDHCI_CDNS_PHY_DLY_SD_HS** (line 61)
- **SDHCI_CDNS_PHY_DLY_STROBE** (line 72)
- **SDHCI_CDNS_PHY_DLY_UHS_DDR50** (line 66)
- **SDHCI_CDNS_PHY_DLY_UHS_SDR12** (line 63)
- **SDHCI_CDNS_PHY_DLY_UHS_SDR25** (line 64)
- **SDHCI_CDNS_PHY_DLY_UHS_SDR50** (line 65)
- **SDHCI_CDNS_SRS_BASE** (line 58)
