# drivers/mmc/host/sdhci-of-arasan.c

Subsystem: drivers/mmc

## Functions (38)

### arasan_dt_parse_clk_phases
- Return type: static void
- Signature: arasan_dt_parse_clk_phases(struct device * dev,struct sdhci_arasan_clk_data * clk_data)
- Line: 1263

### arasan_zynqmp_dll_reset
- Return type: static void
- Signature: arasan_zynqmp_dll_reset(struct sdhci_host * host,u32 deviceid)
- Line: 1122

### arasan_zynqmp_execute_tuning
- Return type: static int
- Signature: arasan_zynqmp_execute_tuning(struct mmc_host * mmc,u32 opcode)
- Line: 1138

### sdhci_arasan_add_host
- Return type: static int
- Signature: sdhci_arasan_add_host(struct sdhci_arasan_data * sdhci_arasan)
- Line: 1800

### sdhci_arasan_cqe_enable
- Return type: static void
- Signature: sdhci_arasan_cqe_enable(struct mmc_host * mmc)
- Line: 568

### sdhci_arasan_cqhci_irq
- Return type: static u32
- Signature: sdhci_arasan_cqhci_irq(struct sdhci_host * host,u32 intmask)
- Line: 550

### sdhci_arasan_dumpregs
- Return type: static void
- Signature: sdhci_arasan_dumpregs(struct mmc_host * mmc)
- Line: 563

### sdhci_arasan_hs400_enhanced_strobe
- Return type: static void
- Signature: sdhci_arasan_hs400_enhanced_strobe(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 454

### sdhci_arasan_hw_reset
- Return type: static void
- Signature: sdhci_arasan_hw_reset(struct sdhci_host * host)
- Line: 484

### sdhci_arasan_phy_dll_set_freq
- Return type: static void
- Signature: sdhci_arasan_phy_dll_set_freq(struct sdhci_host * host,int clock)
- Line: 279

### sdhci_arasan_phy_set_delaychain
- Return type: static void
- Signature: sdhci_arasan_phy_set_delaychain(struct sdhci_host * host,bool enable)
- Line: 246

### sdhci_arasan_phy_set_dll
- Return type: static int
- Signature: sdhci_arasan_phy_set_dll(struct sdhci_host * host,bool enable)
- Line: 259

### sdhci_arasan_probe
- Return type: static int
- Signature: sdhci_arasan_probe(struct platform_device * pdev)
- Line: 1843

### sdhci_arasan_register_sampleclk
- Return type: static int
- Signature: sdhci_arasan_register_sampleclk(struct sdhci_arasan_data * sdhci_arasan,struct clk * clk_xin,struct device * dev)
- Line: 1602

### sdhci_arasan_register_sdcardclk
- Return type: static int
- Signature: sdhci_arasan_register_sdcardclk(struct sdhci_arasan_data * sdhci_arasan,struct clk * clk_xin,struct device * dev)
- Line: 1550

### sdhci_arasan_register_sdclk
- Return type: static int
- Signature: sdhci_arasan_register_sdclk(struct sdhci_arasan_data * sdhci_arasan,struct clk * clk_xin,struct device * dev)
- Line: 1713

### sdhci_arasan_remove
- Return type: static void
- Signature: sdhci_arasan_remove(struct platform_device * pdev)
- Line: 2020

### sdhci_arasan_reset
- Return type: static void
- Signature: sdhci_arasan_reset(struct sdhci_host * host,u8 mask)
- Line: 469

### sdhci_arasan_resume
- Return type: static int
- Signature: sdhci_arasan_resume(struct device * dev)
- Line: 660

### sdhci_arasan_sampleclk_recalc_rate
- Return type: static unsigned long
- Signature: sdhci_arasan_sampleclk_recalc_rate(struct clk_hw * hw,unsigned long parent_rate)
- Line: 741

### sdhci_arasan_sdcardclk_recalc_rate
- Return type: static unsigned long
- Signature: sdhci_arasan_sdcardclk_recalc_rate(struct clk_hw * hw,unsigned long parent_rate)
- Line: 714

### sdhci_arasan_set_clk_delays
- Return type: static void
- Signature: sdhci_arasan_set_clk_delays(struct sdhci_host * host)
- Line: 1243

### sdhci_arasan_set_clock
- Return type: static void
- Signature: sdhci_arasan_set_clock(struct sdhci_host * host,unsigned int clock)
- Line: 353

### sdhci_arasan_set_power_and_bus_voltage
- Return type: static void
- Signature: sdhci_arasan_set_power_and_bus_voltage(struct sdhci_host * host,unsigned char mode,unsigned short vdd)
- Line: 521

### sdhci_arasan_suspend
- Return type: static int
- Signature: sdhci_arasan_suspend(struct device * dev)
- Line: 614

### sdhci_arasan_syscon_write
- Return type: static int
- Signature: sdhci_arasan_syscon_write(struct sdhci_host * host,const struct sdhci_arasan_soc_ctl_field * fld,u32 val)
- Line: 315

### sdhci_arasan_unregister_sdclk
- Return type: static void
- Signature: sdhci_arasan_unregister_sdclk(struct device * dev)
- Line: 1648

### sdhci_arasan_update_baseclkfreq
- Return type: static void
- Signature: sdhci_arasan_update_baseclkfreq(struct sdhci_host * host)
- Line: 1221

### sdhci_arasan_update_clockmultiplier
- Return type: static void
- Signature: sdhci_arasan_update_clockmultiplier(struct sdhci_host * host,u32 value)
- Line: 1182

### sdhci_arasan_update_support64b
- Return type: static void
- Signature: sdhci_arasan_update_support64b(struct sdhci_host * host,u32 value)
- Line: 1671

### sdhci_arasan_voltage_switch
- Return type: static int
- Signature: sdhci_arasan_voltage_switch(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 499

### sdhci_versal_net_emmc_sampleclk_set_phase
- Return type: static int
- Signature: sdhci_versal_net_emmc_sampleclk_set_phase(struct clk_hw * hw,int degrees)
- Line: 1072

### sdhci_versal_net_emmc_sdcardclk_set_phase
- Return type: static int
- Signature: sdhci_versal_net_emmc_sdcardclk_set_phase(struct clk_hw * hw,int degrees)
- Line: 1027

### sdhci_versal_sampleclk_set_phase
- Return type: static int
- Signature: sdhci_versal_sampleclk_set_phase(struct clk_hw * hw,int degrees)
- Line: 966

### sdhci_versal_sdcardclk_set_phase
- Return type: static int
- Signature: sdhci_versal_sdcardclk_set_phase(struct clk_hw * hw,int degrees)
- Line: 899

### sdhci_zynqmp_sampleclk_set_phase
- Return type: static int
- Signature: sdhci_zynqmp_sampleclk_set_phase(struct clk_hw * hw,int degrees)
- Line: 833

### sdhci_zynqmp_sdcardclk_set_phase
- Return type: static int
- Signature: sdhci_zynqmp_sdcardclk_set_phase(struct clk_hw * hw,int degrees)
- Line: 767

### sdhci_zynqmp_set_dynamic_config
- Return type: static int
- Signature: sdhci_zynqmp_set_dynamic_config(struct device * dev,struct sdhci_arasan_data * sdhci_arasan)
- Line: 1741

## Structs (6)

### sdhci_arasan_clk_data
- Line: 159
- Members:
  - reg: u32
  - width: u16
  - shift: s16
  - baseclkfreq: sdhci_arasan_soc_ctl_field
  - clockmultiplier: sdhci_arasan_soc_ctl_field
  - support64b: sdhci_arasan_soc_ctl_field
  - hiword_update: bool
  - sdcardclk_ops: const struct clk_ops *
  - sampleclk_ops: const struct clk_ops *
  - sdcardclk_hw: clk_hw
  - sdcardclk: clk *
  - sampleclk_hw: clk_hw
  - sampleclk: clk *
  - phase_map: mmc_clk_phase_map
  - set_clk_delays: void (*)(struct sdhci_host * host)
  - clk_of_data: void *
  - host: sdhci_host *
  - clk_ahb: clk *
  - phy: phy *
  - is_phy_on: bool
  - internal_phy_reg: bool
  - has_cqe: bool
  - clk_data: sdhci_arasan_clk_data
  - clk_ops: const struct sdhci_arasan_clk_ops *
  - soc_ctl_base: regmap *
  - soc_ctl_map: const struct sdhci_arasan_soc_ctl_map *
  - quirks: unsigned int
  - soc_ctl_map: const struct sdhci_arasan_soc_ctl_map *
  - pdata: const struct sdhci_pltfm_data *
  - clk_ops: const struct sdhci_arasan_clk_ops *
  - quirks: u32

### sdhci_arasan_clk_ops
- Line: 143
- Members:
  - reg: u32
  - width: u16
  - shift: s16
  - baseclkfreq: sdhci_arasan_soc_ctl_field
  - clockmultiplier: sdhci_arasan_soc_ctl_field
  - support64b: sdhci_arasan_soc_ctl_field
  - hiword_update: bool
  - sdcardclk_ops: const struct clk_ops *
  - sampleclk_ops: const struct clk_ops *
  - sdcardclk_hw: clk_hw
  - sdcardclk: clk *
  - sampleclk_hw: clk_hw
  - sampleclk: clk *
  - phase_map: mmc_clk_phase_map
  - set_clk_delays: void (*)(struct sdhci_host * host)
  - clk_of_data: void *
  - host: sdhci_host *
  - clk_ahb: clk *
  - phy: phy *
  - is_phy_on: bool
  - internal_phy_reg: bool
  - has_cqe: bool
  - clk_data: sdhci_arasan_clk_data
  - clk_ops: const struct sdhci_arasan_clk_ops *
  - soc_ctl_base: regmap *
  - soc_ctl_map: const struct sdhci_arasan_soc_ctl_map *
  - quirks: unsigned int
  - soc_ctl_map: const struct sdhci_arasan_soc_ctl_map *
  - pdata: const struct sdhci_pltfm_data *
  - clk_ops: const struct sdhci_arasan_clk_ops *
  - quirks: u32

### sdhci_arasan_data
- Line: 184
- Members:
  - reg: u32
  - width: u16
  - shift: s16
  - baseclkfreq: sdhci_arasan_soc_ctl_field
  - clockmultiplier: sdhci_arasan_soc_ctl_field
  - support64b: sdhci_arasan_soc_ctl_field
  - hiword_update: bool
  - sdcardclk_ops: const struct clk_ops *
  - sampleclk_ops: const struct clk_ops *
  - sdcardclk_hw: clk_hw
  - sdcardclk: clk *
  - sampleclk_hw: clk_hw
  - sampleclk: clk *
  - phase_map: mmc_clk_phase_map
  - set_clk_delays: void (*)(struct sdhci_host * host)
  - clk_of_data: void *
  - host: sdhci_host *
  - clk_ahb: clk *
  - phy: phy *
  - is_phy_on: bool
  - internal_phy_reg: bool
  - has_cqe: bool
  - clk_data: sdhci_arasan_clk_data
  - clk_ops: const struct sdhci_arasan_clk_ops *
  - soc_ctl_base: regmap *
  - soc_ctl_map: const struct sdhci_arasan_soc_ctl_map *
  - quirks: unsigned int
  - soc_ctl_map: const struct sdhci_arasan_soc_ctl_map *
  - pdata: const struct sdhci_pltfm_data *
  - clk_ops: const struct sdhci_arasan_clk_ops *
  - quirks: u32

### sdhci_arasan_of_data
- Line: 214
- Members:
  - reg: u32
  - width: u16
  - shift: s16
  - baseclkfreq: sdhci_arasan_soc_ctl_field
  - clockmultiplier: sdhci_arasan_soc_ctl_field
  - support64b: sdhci_arasan_soc_ctl_field
  - hiword_update: bool
  - sdcardclk_ops: const struct clk_ops *
  - sampleclk_ops: const struct clk_ops *
  - sdcardclk_hw: clk_hw
  - sdcardclk: clk *
  - sampleclk_hw: clk_hw
  - sampleclk: clk *
  - phase_map: mmc_clk_phase_map
  - set_clk_delays: void (*)(struct sdhci_host * host)
  - clk_of_data: void *
  - host: sdhci_host *
  - clk_ahb: clk *
  - phy: phy *
  - is_phy_on: bool
  - internal_phy_reg: bool
  - has_cqe: bool
  - clk_data: sdhci_arasan_clk_data
  - clk_ops: const struct sdhci_arasan_clk_ops *
  - soc_ctl_base: regmap *
  - soc_ctl_map: const struct sdhci_arasan_soc_ctl_map *
  - quirks: unsigned int
  - soc_ctl_map: const struct sdhci_arasan_soc_ctl_map *
  - pdata: const struct sdhci_pltfm_data *
  - clk_ops: const struct sdhci_arasan_clk_ops *
  - quirks: u32

### sdhci_arasan_soc_ctl_field
- Line: 112
- Members:
  - reg: u32
  - width: u16
  - shift: s16
  - baseclkfreq: sdhci_arasan_soc_ctl_field
  - clockmultiplier: sdhci_arasan_soc_ctl_field
  - support64b: sdhci_arasan_soc_ctl_field
  - hiword_update: bool
  - sdcardclk_ops: const struct clk_ops *
  - sampleclk_ops: const struct clk_ops *
  - sdcardclk_hw: clk_hw
  - sdcardclk: clk *
  - sampleclk_hw: clk_hw
  - sampleclk: clk *
  - phase_map: mmc_clk_phase_map
  - set_clk_delays: void (*)(struct sdhci_host * host)
  - clk_of_data: void *
  - host: sdhci_host *
  - clk_ahb: clk *
  - phy: phy *
  - is_phy_on: bool
  - internal_phy_reg: bool
  - has_cqe: bool
  - clk_data: sdhci_arasan_clk_data
  - clk_ops: const struct sdhci_arasan_clk_ops *
  - soc_ctl_base: regmap *
  - soc_ctl_map: const struct sdhci_arasan_soc_ctl_map *
  - quirks: unsigned int
  - soc_ctl_map: const struct sdhci_arasan_soc_ctl_map *
  - pdata: const struct sdhci_pltfm_data *
  - clk_ops: const struct sdhci_arasan_clk_ops *
  - quirks: u32

### sdhci_arasan_soc_ctl_map
- Line: 130
- Members:
  - reg: u32
  - width: u16
  - shift: s16
  - baseclkfreq: sdhci_arasan_soc_ctl_field
  - clockmultiplier: sdhci_arasan_soc_ctl_field
  - support64b: sdhci_arasan_soc_ctl_field
  - hiword_update: bool
  - sdcardclk_ops: const struct clk_ops *
  - sampleclk_ops: const struct clk_ops *
  - sdcardclk_hw: clk_hw
  - sdcardclk: clk *
  - sampleclk_hw: clk_hw
  - sampleclk: clk *
  - phase_map: mmc_clk_phase_map
  - set_clk_delays: void (*)(struct sdhci_host * host)
  - clk_of_data: void *
  - host: sdhci_host *
  - clk_ahb: clk *
  - phy: phy *
  - is_phy_on: bool
  - internal_phy_reg: bool
  - has_cqe: bool
  - clk_data: sdhci_arasan_clk_data
  - clk_ops: const struct sdhci_arasan_clk_ops *
  - soc_ctl_base: regmap *
  - soc_ctl_map: const struct sdhci_arasan_soc_ctl_map *
  - quirks: unsigned int
  - soc_ctl_map: const struct sdhci_arasan_soc_ctl_map *
  - pdata: const struct sdhci_pltfm_data *
  - clk_ops: const struct sdhci_arasan_clk_ops *
  - quirks: u32

## Variables (40)

- static **arasan_clk_ops** : const struct sdhci_arasan_clk_ops (line 1328)
- static **arasan_sampleclk_ops** : const struct clk_ops (line 753)
- static **arasan_sdcardclk_ops** : const struct clk_ops (line 726)
- static **intel_keembay_emmc_data** : sdhci_arasan_of_data (line 1448)
- static **intel_keembay_sd_data** : sdhci_arasan_of_data (line 1454)
- static **intel_keembay_sdio_data** : sdhci_arasan_of_data (line 1460)
- static **intel_keembay_soc_ctl_map** : const struct sdhci_arasan_soc_ctl_map (line 239)
- static **intel_lgm_emmc_data** : sdhci_arasan_of_data (line 1388)
- static **intel_lgm_emmc_soc_ctl_map** : const struct sdhci_arasan_soc_ctl_map (line 227)
- static **intel_lgm_sdxc_data** : sdhci_arasan_of_data (line 1394)
- static **intel_lgm_sdxc_soc_ctl_map** : const struct sdhci_arasan_soc_ctl_map (line 233)
- static **rk3399_soc_ctl_map** : const struct sdhci_arasan_soc_ctl_map (line 221)
- static **sdhci_arasan_axiado_data** : sdhci_arasan_of_data (line 1472)
- static **sdhci_arasan_axiado_pdata** : const struct sdhci_pltfm_data (line 1466)
- static **sdhci_arasan_cqe_ops** : const struct sdhci_ops (line 588)
- static **sdhci_arasan_cqe_pdata** : const struct sdhci_pltfm_data (line 599)
- static **sdhci_arasan_cqhci_ops** : const struct cqhci_host_ops (line 582)
- static **sdhci_arasan_driver** : platform_driver (line 2042)
- static **sdhci_arasan_generic_data** : sdhci_arasan_of_data (line 1333)
- static **sdhci_arasan_of_match** : const struct of_device_id[] (line 1477)
- static **sdhci_arasan_ops** : const struct sdhci_ops (line 539)
- static **sdhci_arasan_pdata** : const struct sdhci_pltfm_data (line 1320)
- static **sdhci_arasan_rk3399_data** : sdhci_arasan_of_data (line 1382)
- static **sdhci_arasan_versal_data** : sdhci_arasan_of_data (line 1431)
- static **sdhci_arasan_versal_net_data** : sdhci_arasan_of_data (line 1442)
- static **sdhci_arasan_versal_net_pdata** : const struct sdhci_pltfm_data (line 1407)
- static **sdhci_arasan_zynqmp_data** : sdhci_arasan_of_data (line 1420)
- static **sdhci_arasan_zynqmp_pdata** : const struct sdhci_pltfm_data (line 1400)
- static **sdhci_keembay_emmc_pdata** : const struct sdhci_pltfm_data (line 1338)
- static **sdhci_keembay_sd_pdata** : const struct sdhci_pltfm_data (line 1353)
- static **sdhci_keembay_sdio_pdata** : const struct sdhci_pltfm_data (line 1368)
- static **versal_clk_ops** : const struct sdhci_arasan_clk_ops (line 1426)
- static **versal_net_clk_ops** : const struct sdhci_arasan_clk_ops (line 1437)
- static **versal_net_sampleclk_ops** : const struct clk_ops (line 1117)
- static **versal_net_sdcardclk_ops** : const struct clk_ops (line 1067)
- static **versal_sampleclk_ops** : const struct clk_ops (line 1022)
- static **versal_sdcardclk_ops** : const struct clk_ops (line 951)
- static **zynqmp_clk_ops** : const struct sdhci_arasan_clk_ops (line 1415)
- static **zynqmp_sampleclk_ops** : const struct clk_ops (line 884)
- static **zynqmp_sdcardclk_ops** : const struct clk_ops (line 818)

## Macros (54)

- **CD_STABLE_MAX_SLEEP_US** (line 103)
- **CD_STABLE_TIMEOUT_US** (line 102)
- **FREQSEL_110M_80M** (line 72)
- **FREQSEL_140M_110M** (line 71)
- **FREQSEL_170M_140M** (line 70)
- **FREQSEL_200M_170M** (line 69)
- **FREQSEL_225M_200M** (line 76)
- **FREQSEL_250M_225M** (line 75)
- **FREQSEL_275M_250M** (line 74)
- **FREQSEL_80M_50M** (line 73)
- **HIWORD_UPDATE**(val,mask,shift) (line 99)
- **MIN_PHY_CLK_HZ** (line 44)
- **PHY_CLK_TOO_SLOW_HZ** (line 43)
- **PHY_CTRL_DLL_RDY_MASK** (line 64)
- **PHY_CTRL_EN_DLL_MASK** (line 63)
- **PHY_CTRL_FREQ_SEL_MASK** (line 65)
- **PHY_CTRL_FREQ_SEL_SHIFT** (line 66)
- **PHY_CTRL_ITAPDLY_ENA_MASK** (line 51)
- **PHY_CTRL_ITAPDLY_SEL_MASK** (line 52)
- **PHY_CTRL_ITAPDLY_SEL_SHIFT** (line 53)
- **PHY_CTRL_ITAP_CHG_WIN_MASK** (line 54)
- **PHY_CTRL_OTAPDLY_ENA_MASK** (line 55)
- **PHY_CTRL_OTAPDLY_SEL_MASK** (line 56)
- **PHY_CTRL_OTAPDLY_SEL_SHIFT** (line 57)
- **PHY_CTRL_REG1** (line 50)
- **PHY_CTRL_REG2** (line 62)
- **PHY_CTRL_SEL_DLY_RX_MASK** (line 68)
- **PHY_CTRL_SEL_DLY_TX_MASK** (line 67)
- **PHY_CTRL_STRB_SEL_MASK** (line 58)
- **PHY_CTRL_STRB_SEL_SHIFT** (line 59)
- **PHY_CTRL_TEST_CTRL_MASK** (line 60)
- **PHY_DLL_TIMEOUT_MS** (line 77)
- **SDHCI_ARASAN_CQE_BASE_ADDR** (line 40)
- **SDHCI_ARASAN_ITAPDLY_REGISTER** (line 34)
- **SDHCI_ARASAN_ITAPDLY_SEL_MASK** (line 35)
- **SDHCI_ARASAN_OTAPDLY_REGISTER** (line 37)
- **SDHCI_ARASAN_OTAPDLY_SEL_MASK** (line 38)
- **SDHCI_ARASAN_QUIRK_CLOCK_25_BROKEN** (line 209)
- **SDHCI_ARASAN_QUIRK_CLOCK_UNSTABLE** (line 203)
- **SDHCI_ARASAN_QUIRK_ENSURE_CD_STABLE** (line 211)
- **SDHCI_ARASAN_QUIRK_FORCE_CDTEST** (line 200)
- **SDHCI_ARASAN_VENDOR_REGISTER** (line 32)
- **SDHCI_HW_RST_EN** (line 79)
- **SDHCI_ITAPDLY_CHGWIN** (line 46)
- **SDHCI_ITAPDLY_ENABLE** (line 47)
- **SDHCI_OTAPDLY_ENABLE** (line 48)
- **VENDOR_ENHANCED_STROBE** (line 41)
- **VERSAL_ICLK_PHASE** (line 85)
- **VERSAL_NET_EMMC_ICLK_PHASE** (line 88)
- **VERSAL_NET_EMMC_OCLK_PHASE** (line 89)
- **VERSAL_NET_PHY_CTRL_STRB90_STRB180_VAL** (line 91)
- **VERSAL_OCLK_PHASE** (line 86)
- **ZYNQMP_ICLK_PHASE** (line 82)
- **ZYNQMP_OCLK_PHASE** (line 83)
