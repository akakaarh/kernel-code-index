# drivers/mmc/host/sdhci-omap.c

Subsystem: drivers/mmc

## Functions (39)

### sdhci_omap_calc_divisor
- Return type: static u16
- Signature: sdhci_omap_calc_divisor(struct sdhci_pltfm_host * host,unsigned int clock)
- Line: 667

### sdhci_omap_card_busy
- Return type: static int
- Signature: sdhci_omap_card_busy(struct mmc_host * mmc)
- Line: 499

### sdhci_omap_conf_bus_power
- Return type: static void
- Signature: sdhci_omap_conf_bus_power(struct sdhci_omap_host * omap_host,unsigned char signal_voltage)
- Line: 219

### sdhci_omap_config_iodelay_pinctrl_state
- Return type: static int
- Signature: sdhci_omap_config_iodelay_pinctrl_state(struct sdhci_omap_host * omap_host)
- Line: 1111

### sdhci_omap_context_restore
- Return type: static void
- Signature: sdhci_omap_context_restore(struct sdhci_omap_host * omap_host)
- Line: 1414

### sdhci_omap_context_save
- Return type: static void
- Signature: sdhci_omap_context_save(struct sdhci_omap_host * omap_host)
- Line: 1403

### sdhci_omap_disable_tuning
- Return type: static void
- Signature: sdhci_omap_disable_tuning(struct sdhci_omap_host * omap_host)
- Line: 303

### sdhci_omap_enable_dma
- Return type: static int
- Signature: sdhci_omap_enable_dma(struct sdhci_host * host)
- Line: 740

### sdhci_omap_enable_iov
- Return type: static int
- Signature: sdhci_omap_enable_iov(struct sdhci_omap_host * omap_host,unsigned int iov_pbias)
- Line: 192

### sdhci_omap_enable_sdio_irq
- Return type: static void
- Signature: sdhci_omap_enable_sdio_irq(struct mmc_host * mmc,int enable)
- Line: 263

### sdhci_omap_execute_tuning
- Return type: static int
- Signature: sdhci_omap_execute_tuning(struct mmc_host * mmc,u32 opcode)
- Line: 316

### sdhci_omap_get_min_clock
- Return type: static unsigned int
- Signature: sdhci_omap_get_min_clock(struct sdhci_host * host)
- Line: 757

### sdhci_omap_has_adma
- Return type: static bool
- Signature: sdhci_omap_has_adma(struct sdhci_omap_host * omap_host,int offset)
- Line: 731

### sdhci_omap_init_74_clocks
- Return type: static void
- Signature: sdhci_omap_init_74_clocks(struct sdhci_host * host,u8 power_mode)
- Line: 780

### sdhci_omap_iodelay_pinctrl_state
- Return type: static pinctrl_state *
- Signature: sdhci_omap_iodelay_pinctrl_state(struct sdhci_omap_host * omap_host,char * mode,u32 * caps,u32 capmask)
- Line: 1083

### sdhci_omap_irq
- Return type: static u32
- Signature: sdhci_omap_irq(struct sdhci_host * host,u32 intmask)
- Line: 886

### sdhci_omap_probe
- Return type: static int
- Signature: sdhci_omap_probe(struct platform_device * pdev)
- Line: 1212

### sdhci_omap_readl
- Return type: static u32
- Signature: sdhci_omap_readl(struct sdhci_omap_host * host,unsigned int offset)
- Line: 139

### sdhci_omap_regulator_get_caps
- Return type: static unsigned int
- Signature: sdhci_omap_regulator_get_caps(struct device * dev,const char * name)
- Line: 942

### sdhci_omap_remove
- Return type: static void
- Signature: sdhci_omap_remove(struct platform_device * pdev)
- Line: 1388

### sdhci_omap_reset
- Return type: static void
- Signature: sdhci_omap_reset(struct sdhci_host * host,u8 mask)
- Line: 841

### sdhci_omap_runtime_resume
- Return type: static int
- Signature: sdhci_omap_runtime_resume(struct device * dev)
- Line: 1445

### sdhci_omap_runtime_suspend
- Return type: static int
- Signature: sdhci_omap_runtime_suspend(struct device * dev)
- Line: 1426

### sdhci_omap_set_bus_mode
- Return type: static void
- Signature: sdhci_omap_set_bus_mode(struct sdhci_omap_host * omap_host,unsigned int mode)
- Line: 634

### sdhci_omap_set_bus_width
- Return type: static void
- Signature: sdhci_omap_set_bus_width(struct sdhci_host * host,int width)
- Line: 764

### sdhci_omap_set_capabilities
- Return type: static int
- Signature: sdhci_omap_set_capabilities(struct sdhci_host * host)
- Line: 964

### sdhci_omap_set_clock
- Return type: static void
- Signature: sdhci_omap_set_clock(struct sdhci_host * host,unsigned int clock)
- Line: 697

### sdhci_omap_set_dll
- Return type: static void
- Signature: sdhci_omap_set_dll(struct sdhci_omap_host * omap_host,int count)
- Line: 280

### sdhci_omap_set_ios
- Return type: static void
- Signature: sdhci_omap_set_ios(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 652

### sdhci_omap_set_pbias
- Return type: static int
- Signature: sdhci_omap_set_pbias(struct sdhci_omap_host * omap_host,bool power_on,unsigned int iov)
- Line: 151

### sdhci_omap_set_power
- Return type: static void
- Signature: sdhci_omap_set_power(struct sdhci_host * host,unsigned char mode,unsigned short vdd)
- Line: 715

### sdhci_omap_set_power_mode
- Return type: static void
- Signature: sdhci_omap_set_power_mode(struct sdhci_omap_host * omap_host,u8 power_mode)
- Line: 626

### sdhci_omap_set_timeout
- Return type: static void
- Signature: sdhci_omap_set_timeout(struct sdhci_host * host,struct mmc_command * cmd)
- Line: 919

### sdhci_omap_set_timing
- Return type: static void
- Signature: sdhci_omap_set_timing(struct sdhci_omap_host * omap_host,u8 timing)
- Line: 601

### sdhci_omap_set_uhs_signaling
- Return type: static void
- Signature: sdhci_omap_set_uhs_signaling(struct sdhci_host * host,unsigned int timing)
- Line: 820

### sdhci_omap_start_clock
- Return type: static void
- Signature: sdhci_omap_start_clock(struct sdhci_omap_host * omap_host)
- Line: 679

### sdhci_omap_start_signal_voltage_switch
- Return type: static int
- Signature: sdhci_omap_start_signal_voltage_switch(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 544

### sdhci_omap_stop_clock
- Return type: static void
- Signature: sdhci_omap_stop_clock(struct sdhci_omap_host * omap_host)
- Line: 688

### sdhci_omap_writel
- Return type: static void
- Signature: sdhci_omap_writel(struct sdhci_omap_host * host,unsigned int offset,u32 data)
- Line: 145

## Structs (2)

### sdhci_omap_data
- Line: 101
- Members:
  - omap_offset: int
  - offset: u32
  - flags: u8
  - version: char *
  - base: void __iomem *
  - dev: device *
  - pbias: regulator *
  - pbias_enabled: bool
  - host: sdhci_host *
  - bus_mode: u8
  - power_mode: u8
  - timing: u8
  - flags: u8
  - pinctrl: pinctrl *
  - pinctrl_state: pinctrl_state **
  - wakeirq: int
  - is_tuning: bool
  - omap_offset: int
  - con: u32
  - hctl: u32
  - sysctl: u32
  - capa: u32
  - ie: u32
  - ise: u32

### sdhci_omap_host
- Line: 107
- Members:
  - omap_offset: int
  - offset: u32
  - flags: u8
  - version: char *
  - base: void __iomem *
  - dev: device *
  - pbias: regulator *
  - pbias_enabled: bool
  - host: sdhci_host *
  - bus_mode: u8
  - power_mode: u8
  - timing: u8
  - flags: u8
  - pinctrl: pinctrl *
  - pinctrl_state: pinctrl_state **
  - wakeirq: int
  - is_tuning: bool
  - omap_offset: int
  - con: u32
  - hctl: u32
  - sysctl: u32
  - capa: u32
  - ie: u32
  - ise: u32

## Variables (14)

- static **am335_data** : const struct sdhci_omap_data (line 1051)
- static **am437_data** : const struct sdhci_omap_data (line 1057)
- static **dra7_data** : const struct sdhci_omap_data (line 1063)
- static **k2g_data** : const struct sdhci_omap_data (line 1046)
- static **omap2430_data** : const struct sdhci_omap_data (line 1024)
- static **omap3_data** : const struct sdhci_omap_data (line 1029)
- static **omap4_data** : const struct sdhci_omap_data (line 1034)
- static **omap5_data** : const struct sdhci_omap_data (line 1040)
- static **omap_sdhci_match** : const struct of_device_id[] (line 1069)
- static **sdhci_omap_dev_pm_ops** : const struct dev_pm_ops (line 1461)
- static **sdhci_omap_driver** : platform_driver (line 1466)
- static **sdhci_omap_ops** : const struct sdhci_ops (line 928)
- static **sdhci_omap_pdata** : const struct sdhci_pltfm_data (line 1011)
- static **sdhci_omap_soc_devices** : const struct soc_device_attribute[] (line 1202)

## Macros (55)

- **AC12_SCLK_SEL** (line 77)
- **AC12_V1V8_SIGEN** (line 76)
- **CAPA2_TSDR50** (line 85)
- **CAPA_VS18** (line 82)
- **CAPA_VS30** (line 81)
- **CAPA_VS33** (line 80)
- **CMD_ERR_MASK** (line 882)
- **CMD_MASK** (line 884)
- **CON_CLKEXTFREE** (line 36)
- **CON_CTPL** (line 38)
- **CON_DDR** (line 35)
- **CON_DMA_MASTER** (line 34)
- **CON_DW8** (line 33)
- **CON_INIT** (line 39)
- **CON_OD** (line 40)
- **CON_PADEN** (line 37)
- **DLL_CALIB** (line 47)
- **DLL_FORCE_SR_C_MASK** (line 45)
- **DLL_FORCE_SR_C_SHIFT** (line 44)
- **DLL_FORCE_VALUE** (line 46)
- **DLL_SWT** (line 43)
- **HCTL_SDBP** (line 56)
- **HCTL_SDVS_18** (line 61)
- **HCTL_SDVS_30** (line 60)
- **HCTL_SDVS_33** (line 59)
- **HCTL_SDVS_MASK** (line 58)
- **HCTL_SDVS_SHIFT** (line 57)
- **INT_CC_EN** (line 71)
- **IOV_1V8** (line 91)
- **IOV_3V0** (line 92)
- **IOV_3V3** (line 93)
- **MAX_PHASE_DELAY** (line 95)
- **MMC_TIMEOUT_US** (line 840)
- **PSTATE_DATI** (line 53)
- **PSTATE_DLEV_DAT0** (line 52)
- **SDHCI_OMAP_AC12** (line 75)
- **SDHCI_OMAP_CAPA** (line 79)
- **SDHCI_OMAP_CAPA2** (line 84)
- **SDHCI_OMAP_CMD** (line 49)
- **SDHCI_OMAP_CON** (line 32)
- **SDHCI_OMAP_DLL** (line 42)
- **SDHCI_OMAP_HCTL** (line 55)
- **SDHCI_OMAP_IE** (line 70)
- **SDHCI_OMAP_ISE** (line 73)
- **SDHCI_OMAP_PSTATE** (line 51)
- **SDHCI_OMAP_REQUIRE_IODELAY** (line 98)
- **SDHCI_OMAP_SPECIAL_RESET** (line 99)
- **SDHCI_OMAP_STAT** (line 68)
- **SDHCI_OMAP_SYSCONFIG** (line 30)
- **SDHCI_OMAP_SYSCTL** (line 63)
- **SDHCI_OMAP_TIMEOUT** (line 87)
- **SYSCTL_CEN** (line 64)
- **SYSCTL_CLKD_MASK** (line 66)
- **SYSCTL_CLKD_MAX** (line 89)
- **SYSCTL_CLKD_SHIFT** (line 65)
