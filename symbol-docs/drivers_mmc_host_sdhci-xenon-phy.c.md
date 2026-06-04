# drivers/mmc/host/sdhci-xenon-phy.c

Subsystem: drivers/mmc

## Functions (18)

### armada_3700_soc_pad_voltage_set
- Return type: static void
- Signature: armada_3700_soc_pad_voltage_set(struct sdhci_host * host,unsigned char signal_voltage)
- Line: 309

### get_dt_pad_ctrl_data
- Return type: static int
- Signature: get_dt_pad_ctrl_data(struct sdhci_host * host,struct device_node * np,struct xenon_emmc_phy_params * params)
- Line: 680

### xenon_add_phy
- Return type: static int
- Signature: xenon_add_phy(struct device * dev,struct sdhci_host * host,const char * phy_name)
- Line: 848

### xenon_alloc_emmc_phy
- Return type: static int
- Signature: xenon_alloc_emmc_phy(struct sdhci_host * host)
- Line: 203

### xenon_check_stability_internal_clk
- Return type: static int
- Signature: xenon_check_stability_internal_clk(struct sdhci_host * host)
- Line: 222

### xenon_emmc_phy_config_tuning
- Return type: static int
- Signature: xenon_emmc_phy_config_tuning(struct sdhci_host * host)
- Line: 406

### xenon_emmc_phy_disable_strobe
- Return type: static void
- Signature: xenon_emmc_phy_disable_strobe(struct sdhci_host * host)
- Line: 443

### xenon_emmc_phy_enable_dll
- Return type: static int
- Signature: xenon_emmc_phy_enable_dll(struct sdhci_host * host)
- Line: 350

### xenon_emmc_phy_init
- Return type: static int
- Signature: xenon_emmc_phy_init(struct sdhci_host * host)
- Line: 243

### xenon_emmc_phy_parse_params
- Return type: static int
- Signature: xenon_emmc_phy_parse_params(struct sdhci_host * host,struct device * dev,struct xenon_emmc_phy_params * params)
- Line: 724

### xenon_emmc_phy_set
- Return type: static void
- Signature: xenon_emmc_phy_set(struct sdhci_host * host,unsigned char timing)
- Line: 574

### xenon_emmc_phy_set_soc_pad
- Return type: static void
- Signature: xenon_emmc_phy_set_soc_pad(struct sdhci_host * host,unsigned char signal_voltage)
- Line: 331

### xenon_emmc_phy_slow_mode
- Return type: static bool
- Signature: xenon_emmc_phy_slow_mode(struct sdhci_host * host,unsigned char timing)
- Line: 519

### xenon_emmc_phy_strobe_delay_adj
- Return type: static void
- Signature: xenon_emmc_phy_strobe_delay_adj(struct sdhci_host * host)
- Line: 467

### xenon_hs_delay_adj
- Return type: static int
- Signature: xenon_hs_delay_adj(struct sdhci_host * host)
- Line: 769

### xenon_phy_adj
- Return type: int
- Signature: xenon_phy_adj(struct sdhci_host * host,struct mmc_ios * ios)
- Line: 810

### xenon_phy_parse_params
- Return type: int
- Signature: xenon_phy_parse_params(struct device * dev,struct sdhci_host * host)
- Line: 870

### xenon_soc_pad_ctrl
- Return type: void
- Signature: xenon_soc_pad_ctrl(struct sdhci_host * host,unsigned char signal_voltage)
- Line: 758

## Structs (3)

### soc_pad_ctrl
- Line: 154
- Members:
  - timing_adj: u16
  - func_ctrl: u16
  - pad_ctrl: u16
  - pad_ctrl2: u16
  - dll_ctrl: u16
  - logic_timing_adj: u16
  - dll_update: u32
  - logic_timing_val: u32
  - reg: void __iomem *
  - pad_type: soc_pad_ctrl_type
  - set_soc_pad: void (*)(struct sdhci_host * host,unsigned char signal_voltage)
  - slow_mode: bool
  - znr: u8
  - zpr: u8
  - nr_tun_times: u8
  - tun_step_divider: u8
  - pad_ctrl: soc_pad_ctrl

### xenon_emmc_phy_params
- Line: 189
- Members:
  - timing_adj: u16
  - func_ctrl: u16
  - pad_ctrl: u16
  - pad_ctrl2: u16
  - dll_ctrl: u16
  - logic_timing_adj: u16
  - dll_update: u32
  - logic_timing_val: u32
  - reg: void __iomem *
  - pad_type: soc_pad_ctrl_type
  - set_soc_pad: void (*)(struct sdhci_host * host,unsigned char signal_voltage)
  - slow_mode: bool
  - znr: u8
  - zpr: u8
  - nr_tun_times: u8
  - tun_step_divider: u8
  - pad_ctrl: soc_pad_ctrl

### xenon_emmc_phy_regs
- Line: 119
- Members:
  - timing_adj: u16
  - func_ctrl: u16
  - pad_ctrl: u16
  - pad_ctrl2: u16
  - dll_ctrl: u16
  - logic_timing_adj: u16
  - dll_update: u32
  - logic_timing_val: u32
  - reg: void __iomem *
  - pad_type: soc_pad_ctrl_type
  - set_soc_pad: void (*)(struct sdhci_host * host,unsigned char signal_voltage)
  - slow_mode: bool
  - znr: u8
  - zpr: u8
  - nr_tun_times: u8
  - tun_step_divider: u8
  - pad_ctrl: soc_pad_ctrl

## Enums (2)

### soc_pad_ctrl_type
- Line: 149

### xenon_phy_type_enum
- Line: 143

## Variables (3)

- static **phy_types** : const char * const[] (line 138)
- static **xenon_emmc_5_0_phy_regs** : xenon_emmc_phy_regs (line 164)
- static **xenon_emmc_5_1_phy_regs** : xenon_emmc_phy_regs (line 175)

## Macros (76)

- **ARMADA_3700_SOC_PAD_1_8V** (line 306)
- **ARMADA_3700_SOC_PAD_3_3V** (line 307)
- **XENON_ASYNC_DDRMODE_MASK** (line 44)
- **XENON_ASYNC_DDRMODE_SHIFT** (line 45)
- **XENON_AUTO_RECEN_CTRL** (line 61)
- **XENON_CMD_DDR_MODE** (line 46)
- **XENON_DLL_BYPASS_EN** (line 105)
- **XENON_DLL_ENABLE** (line 95)
- **XENON_DLL_FAST_LOCK** (line 103)
- **XENON_DLL_GAIN2X** (line 104)
- **XENON_DLL_PHASE_90_DEGREE** (line 102)
- **XENON_DLL_PHASE_MASK** (line 101)
- **XENON_DLL_PHSEL0_SHIFT** (line 100)
- **XENON_DLL_PHSEL1_SHIFT** (line 99)
- **XENON_DLL_REFCLK_SEL** (line 97)
- **XENON_DLL_UPDATE** (line 98)
- **XENON_DLL_UPDATE_STROBE_5_0** (line 96)
- **XENON_DQ_ASYNC_MODE** (line 49)
- **XENON_DQ_DDR_MODE_MASK** (line 48)
- **XENON_DQ_DDR_MODE_SHIFT** (line 47)
- **XENON_EMMC5_1_FC_CMD_PD** (line 74)
- **XENON_EMMC5_1_FC_CMD_PU** (line 75)
- **XENON_EMMC5_1_FC_DQ_PD** (line 76)
- **XENON_EMMC5_1_FC_DQ_PU** (line 77)
- **XENON_EMMC5_1_FC_QSP_PD** (line 72)
- **XENON_EMMC5_1_FC_QSP_PU** (line 73)
- **XENON_EMMC5_FC_CMD_PD** (line 66)
- **XENON_EMMC5_FC_CMD_PU** (line 67)
- **XENON_EMMC5_FC_DQ_PD** (line 68)
- **XENON_EMMC5_FC_DQ_PU** (line 69)
- **XENON_EMMC5_FC_QSP_PD** (line 64)
- **XENON_EMMC5_FC_QSP_PU** (line 65)
- **XENON_EMMC_5_0_PHY_DLL_CONTROL** (line 93)
- **XENON_EMMC_5_0_PHY_FUNC_CONTROL** (line 42)
- **XENON_EMMC_5_0_PHY_LOGIC_TIMING_ADJUST** (line 107)
- **XENON_EMMC_5_0_PHY_LOGIC_TIMING_VALUE** (line 109)
- **XENON_EMMC_5_0_PHY_PAD_CONTROL** (line 52)
- **XENON_EMMC_5_0_PHY_PAD_CONTROL2** (line 80)
- **XENON_EMMC_5_0_PHY_REG_BASE** (line 21)
- **XENON_EMMC_5_0_PHY_TIMING_ADJUST** (line 26)
- **XENON_EMMC_PHY_DLL_CONTROL** (line 92)
- **XENON_EMMC_PHY_FUNC_CONTROL** (line 41)
- **XENON_EMMC_PHY_LOGIC_TIMING_ADJUST** (line 110)
- **XENON_EMMC_PHY_PAD_CONTROL** (line 51)
- **XENON_EMMC_PHY_PAD_CONTROL1** (line 71)
- **XENON_EMMC_PHY_PAD_CONTROL2** (line 79)
- **XENON_EMMC_PHY_REG_BASE** (line 23)
- **XENON_EMMC_PHY_TIMING_ADJUST** (line 25)
- **XENON_FC_ALL_CMOS_RECEIVER** (line 62)
- **XENON_FC_CMD_RECEN** (line 57)
- **XENON_FC_DQ_RECEN** (line 56)
- **XENON_FC_QSN_RECEN** (line 59)
- **XENON_FC_QSP_RECEN** (line 58)
- **XENON_FC_SYNC_EN_DURATION_MASK** (line 34)
- **XENON_FC_SYNC_EN_DURATION_SHIFT** (line 35)
- **XENON_FC_SYNC_RST_DURATION_MASK** (line 38)
- **XENON_FC_SYNC_RST_DURATION_SHIFT** (line 39)
- **XENON_FC_SYNC_RST_EN_DURATION_MASK** (line 36)
- **XENON_FC_SYNC_RST_EN_DURATION_SHIFT** (line 37)
- **XENON_LOGIC_TIMING_VALUE** (line 111)
- **XENON_MAX_PHY_TIMEOUT_LOOPS** (line 113)
- **XENON_OEN_QSN** (line 60)
- **XENON_PHY_INITIALIZAION** (line 31)
- **XENON_REC_EN_MASK** (line 55)
- **XENON_REC_EN_SHIFT** (line 54)
- **XENON_SAMPL_INV_QSP_PHASE_SELECT** (line 29)
- **XENON_SAMPL_INV_QSP_PHASE_SELECT_SHIFT** (line 30)
- **XENON_TIMING_ADJUST_SDIO_MODE** (line 28)
- **XENON_TIMING_ADJUST_SLOW_MODE** (line 27)
- **XENON_WAIT_CYCLE_BEFORE_USING_MASK** (line 32)
- **XENON_WAIT_CYCLE_BEFORE_USING_SHIFT** (line 33)
- **XENON_ZNR_DEF_VALUE** (line 89)
- **XENON_ZNR_MASK** (line 82)
- **XENON_ZNR_SHIFT** (line 83)
- **XENON_ZPR_DEF_VALUE** (line 90)
- **XENON_ZPR_MASK** (line 84)
