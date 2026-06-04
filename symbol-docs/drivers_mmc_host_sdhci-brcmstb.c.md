# drivers/mmc/host/sdhci-brcmstb.c

Subsystem: drivers/mmc

## Functions (21)

### brcmstb_reset
- Return type: static void
- Signature: brcmstb_reset(struct sdhci_host * host,u8 mask)
- Line: 158

### brcmstb_reset_74165b0
- Return type: static void
- Signature: brcmstb_reset_74165b0(struct sdhci_host * host,u8 mask)
- Line: 195

### brcmstb_sdhci_reset_cmd_data
- Return type: static void
- Signature: brcmstb_sdhci_reset_cmd_data(struct sdhci_host * host,u8 mask)
- Line: 166

### enable_clock_gating
- Return type: static void
- Signature: enable_clock_gating(struct sdhci_host * host)
- Line: 144

### sdhci_brcmstb_add_host
- Return type: static int
- Signature: sdhci_brcmstb_add_host(struct sdhci_host * host,struct sdhci_brcmstb_priv * priv)
- Line: 438

### sdhci_brcmstb_cfginit_2712
- Return type: static void
- Signature: sdhci_brcmstb_cfginit_2712(struct sdhci_host * host)
- Line: 269

### sdhci_brcmstb_cqe_enable
- Return type: static void
- Signature: sdhci_brcmstb_cqe_enable(struct mmc_host * mmc)
- Line: 316

### sdhci_brcmstb_cqhci_irq
- Return type: static u32
- Signature: sdhci_brcmstb_cqhci_irq(struct sdhci_host * host,u32 intmask)
- Line: 425

### sdhci_brcmstb_dumpregs
- Return type: static void
- Signature: sdhci_brcmstb_dumpregs(struct mmc_host * mmc)
- Line: 311

### sdhci_brcmstb_hs400es
- Return type: static void
- Signature: sdhci_brcmstb_hs400es(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 209

### sdhci_brcmstb_probe
- Return type: static int
- Signature: sdhci_brcmstb_probe(struct platform_device * pdev)
- Line: 485

### sdhci_brcmstb_restore_regs
- Return type: static void
- Signature: sdhci_brcmstb_restore_regs(struct mmc_host * mmc,enum cfg_core_ver ver)
- Line: 106

### sdhci_brcmstb_resume
- Return type: static int
- Signature: sdhci_brcmstb_resume(struct device * dev)
- Line: 648

### sdhci_brcmstb_save_regs
- Return type: static void
- Signature: sdhci_brcmstb_save_regs(struct mmc_host * mmc,enum cfg_core_ver ver)
- Line: 84

### sdhci_brcmstb_save_restore_regs_v1
- Return type: static void
- Signature: sdhci_brcmstb_save_restore_regs_v1(struct mmc_host * mmc,int save)
- Line: 128

### sdhci_brcmstb_save_restore_regs_v2
- Return type: static void
- Signature: sdhci_brcmstb_save_restore_regs_v2(struct mmc_host * mmc,int save)
- Line: 136

### sdhci_brcmstb_set_72116_uhs_signaling
- Return type: static void
- Signature: sdhci_brcmstb_set_72116_uhs_signaling(struct sdhci_host * host,unsigned int timing)
- Line: 296

### sdhci_brcmstb_set_clock
- Return type: static void
- Signature: sdhci_brcmstb_set_clock(struct sdhci_host * host,unsigned int clock)
- Line: 225

### sdhci_brcmstb_set_uhs_signaling
- Return type: static void
- Signature: sdhci_brcmstb_set_uhs_signaling(struct sdhci_host * host,unsigned int timing)
- Line: 240

### sdhci_brcmstb_shutdown
- Return type: static void
- Signature: sdhci_brcmstb_shutdown(struct platform_device * pdev)
- Line: 619

### sdhci_brcmstb_suspend
- Return type: static int
- Signature: sdhci_brcmstb_suspend(struct device * dev)
- Line: 626

## Structs (3)

### brcmstb_match_priv
- Line: 66
- Members:
  - sd_pin_sel: u32
  - phy_sw_mode0_rxctrl: u32
  - max_50mhz_mode: u32
  - boot_main_ctl: u32
  - cfginit: void (*)(struct sdhci_host * host)
  - hs400es: void (*)(struct mmc_host * mmc,struct mmc_ios * ios)
  - save_restore_regs: void (*)(struct mmc_host * mmc,int save)
  - ops: sdhci_ops *
  - flags: const unsigned int
  - cfg_regs: void __iomem *
  - boot_regs: void __iomem *
  - saved_regs: sdhci_brcmstb_saved_regs
  - flags: unsigned int
  - base_clk: clk *
  - base_freq_hz: u32
  - match_priv: const struct brcmstb_match_priv *

### sdhci_brcmstb_priv
- Line: 74
- Members:
  - sd_pin_sel: u32
  - phy_sw_mode0_rxctrl: u32
  - max_50mhz_mode: u32
  - boot_main_ctl: u32
  - cfginit: void (*)(struct sdhci_host * host)
  - hs400es: void (*)(struct mmc_host * mmc,struct mmc_ios * ios)
  - save_restore_regs: void (*)(struct mmc_host * mmc,int save)
  - ops: sdhci_ops *
  - flags: const unsigned int
  - cfg_regs: void __iomem *
  - boot_regs: void __iomem *
  - saved_regs: sdhci_brcmstb_saved_regs
  - flags: unsigned int
  - base_clk: clk *
  - base_freq_hz: u32
  - match_priv: const struct brcmstb_match_priv *

### sdhci_brcmstb_saved_regs
- Line: 59
- Members:
  - sd_pin_sel: u32
  - phy_sw_mode0_rxctrl: u32
  - max_50mhz_mode: u32
  - boot_main_ctl: u32
  - cfginit: void (*)(struct sdhci_host * host)
  - hs400es: void (*)(struct mmc_host * mmc,struct mmc_ios * ios)
  - save_restore_regs: void (*)(struct mmc_host * mmc,int save)
  - ops: sdhci_ops *
  - flags: const unsigned int
  - cfg_regs: void __iomem *
  - boot_regs: void __iomem *
  - saved_regs: sdhci_brcmstb_saved_regs
  - flags: unsigned int
  - base_clk: clk *
  - base_freq_hz: u32
  - match_priv: const struct brcmstb_match_priv *

## Enums (1)

### cfg_core_ver
- Line: 54

## Variables (15)

- static **match_priv_2712** : const struct brcmstb_match_priv (line 372)
- static **match_priv_72116** : brcmstb_match_priv (line 394)
- static **match_priv_7216** : const struct brcmstb_match_priv (line 400)
- static **match_priv_74165b0** : brcmstb_match_priv (line 407)
- static **match_priv_7425** : brcmstb_match_priv (line 377)
- static **match_priv_74371** : brcmstb_match_priv (line 383)
- static **match_priv_7445** : brcmstb_match_priv (line 388)
- static **sdhci_brcm_of_match** : const struct of_device_id __maybe_unused[] (line 414)
- static **sdhci_brcmstb_cqhci_ops** : const struct cqhci_host_ops (line 330)
- static **sdhci_brcmstb_driver** : platform_driver (line 681)
- static **sdhci_brcmstb_ops** : sdhci_ops (line 336)
- static **sdhci_brcmstb_ops_2712** : sdhci_ops (line 343)
- static **sdhci_brcmstb_ops_72116** : sdhci_ops (line 351)
- static **sdhci_brcmstb_ops_7216** : sdhci_ops (line 358)
- static **sdhci_brcmstb_ops_74165b0** : sdhci_ops (line 365)

## Macros (26)

- **BRCMSTB_MATCH_FLAGS_BROKEN_TIMEOUT** (line 25)
- **BRCMSTB_MATCH_FLAGS_HAS_CLOCK_GATE** (line 26)
- **BRCMSTB_MATCH_FLAGS_NO_64BIT** (line 24)
- **BRCMSTB_MATCH_FLAGS_USE_CARD_BUSY** (line 27)
- **BRCMSTB_PRIV_FLAGS_GATE_CLOCK** (line 30)
- **BRCMSTB_PRIV_FLAGS_HAS_CQE** (line 29)
- **MMC_CAP_HSE_MASK** (line 50)
- **MMC_CAP_UHS_I_SDR_MASK** (line 52)
- **SDHCI_ARASAN_CQE_BASE_ADDR** (line 32)
- **SDHCI_VENDOR** (line 20)
- **SDHCI_VENDOR_ENHANCED_STRB** (line 21)
- **SDHCI_VENDOR_GATE_SDCLK_EN** (line 22)
- **SDIO_BOOT_MAIN_CTL** (line 48)
- **SDIO_CFG_CQ_CAPABILITY** (line 39)
- **SDIO_CFG_CQ_CAPABILITY_FMUL** (line 40)
- **SDIO_CFG_CTRL** (line 34)
- **SDIO_CFG_CTRL_SDCD_N_TEST_EN** (line 35)
- **SDIO_CFG_CTRL_SDCD_N_TEST_LEV** (line 36)
- **SDIO_CFG_MAX_50MHZ_MODE** (line 44)
- **SDIO_CFG_MAX_50MHZ_MODE_ENABLE** (line 46)
- **SDIO_CFG_MAX_50MHZ_MODE_STRAP_OVERRIDE** (line 45)
- **SDIO_CFG_OP_DLY** (line 37)
- **SDIO_CFG_OP_DLY_DEFAULT** (line 38)
- **SDIO_CFG_PHY_SW_MODE_0_RX_CTRL** (line 43)
- **SDIO_CFG_SD_PIN_SEL** (line 41)
- **SDIO_CFG_V1_SD_PIN_SEL** (line 42)
