# drivers/mmc/host/sdhci-tegra.c

Subsystem: drivers/mmc

## Functions (47)

### sdhci_tegra_add_host
- Return type: static int
- Signature: sdhci_tegra_add_host(struct sdhci_host * host)
- Line: 1588

### sdhci_tegra_cqe_enable
- Return type: static void
- Signature: sdhci_tegra_cqe_enable(struct mmc_host * mmc)
- Line: 1235

### sdhci_tegra_cqe_post_disable
- Return type: static void
- Signature: sdhci_tegra_cqe_post_disable(struct mmc_host * mmc)
- Line: 1326

### sdhci_tegra_cqe_pre_enable
- Return type: static void
- Signature: sdhci_tegra_cqe_pre_enable(struct mmc_host * mmc)
- Line: 1316

### sdhci_tegra_cqhci_irq
- Return type: static u32
- Signature: sdhci_tegra_cqhci_irq(struct sdhci_host * host,u32 intmask)
- Line: 1275

### sdhci_tegra_dumpregs
- Return type: static void
- Signature: sdhci_tegra_dumpregs(struct mmc_host * mmc)
- Line: 1270

### sdhci_tegra_probe
- Return type: static int
- Signature: sdhci_tegra_probe(struct platform_device * pdev)
- Line: 1649

### sdhci_tegra_program_stream_id
- Return type: static void
- Signature: sdhci_tegra_program_stream_id(struct sdhci_host * host)
- Line: 1637

### sdhci_tegra_remove
- Return type: static void
- Signature: sdhci_tegra_remove(struct platform_device * pdev)
- Line: 1817

### sdhci_tegra_resume
- Return type: static int
- Signature: sdhci_tegra_resume(struct device * dev)
- Line: 1879

### sdhci_tegra_runtime_resume
- Return type: static int
- Signature: sdhci_tegra_runtime_resume(struct device * dev)
- Line: 1844

### sdhci_tegra_runtime_suspend
- Return type: static int
- Signature: sdhci_tegra_runtime_suspend(struct device * dev)
- Line: 1834

### sdhci_tegra_start_signal_voltage_switch
- Return type: static int
- Signature: sdhci_tegra_start_signal_voltage_switch(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 1103

### sdhci_tegra_suspend
- Return type: static int
- Signature: sdhci_tegra_suspend(struct device * dev)
- Line: 1852

### sdhci_tegra_update_dcmd_desc
- Return type: static void
- Signature: sdhci_tegra_update_dcmd_desc(struct mmc_host * mmc,struct mmc_request * mrq,u64 * data)
- Line: 1223

### tegra210_sdhci_writew
- Return type: static void
- Signature: tegra210_sdhci_writew(struct sdhci_host * host,u16 val,int reg)
- Line: 272

### tegra_cqhci_writel
- Return type: static void
- Signature: tegra_cqhci_writel(struct cqhci_host * cq_host,u32 val,int reg)
- Line: 1184

### tegra_sdhci_configure_cal_pad
- Return type: static void
- Signature: tegra_sdhci_configure_cal_pad(struct sdhci_host * host,bool enable)
- Line: 422

### tegra_sdhci_configure_card_clk
- Return type: static bool
- Signature: tegra_sdhci_configure_card_clk(struct sdhci_host * host,bool enable)
- Line: 251

### tegra_sdhci_execute_hw_tuning
- Return type: static int
- Signature: tegra_sdhci_execute_hw_tuning(struct mmc_host * mmc,u32 opcode)
- Line: 994

### tegra_sdhci_execute_tuning
- Return type: static int
- Signature: tegra_sdhci_execute_tuning(struct sdhci_host * host,u32 opcode)
- Line: 1069

### tegra_sdhci_get_max_clock
- Return type: static unsigned int
- Signature: tegra_sdhci_get_max_clock(struct sdhci_host * host)
- Line: 818

### tegra_sdhci_get_ro
- Return type: static unsigned int
- Signature: tegra_sdhci_get_ro(struct sdhci_host * host)
- Line: 292

### tegra_sdhci_hs400_dll_cal
- Return type: static void
- Signature: tegra_sdhci_hs400_dll_cal(struct sdhci_host * host)
- Line: 835

### tegra_sdhci_hs400_enhanced_strobe
- Return type: static void
- Signature: tegra_sdhci_hs400_enhanced_strobe(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 792

### tegra_sdhci_init_pinctrl_info
- Return type: static int
- Signature: tegra_sdhci_init_pinctrl_info(struct device * dev,struct sdhci_tegra * tegra_host)
- Line: 1129

### tegra_sdhci_is_pad_and_regulator_valid
- Return type: static bool
- Signature: tegra_sdhci_is_pad_and_regulator_valid(struct sdhci_host * host)
- Line: 302

### tegra_sdhci_pad_autocalib
- Return type: static void
- Signature: tegra_sdhci_pad_autocalib(struct sdhci_host * host)
- Line: 524

### tegra_sdhci_parse_dt
- Return type: static void
- Signature: tegra_sdhci_parse_dt(struct sdhci_host * host)
- Line: 734

### tegra_sdhci_parse_pad_autocal_dt
- Return type: static void
- Signature: tegra_sdhci_parse_pad_autocal_dt(struct sdhci_host * host)
- Line: 586

### tegra_sdhci_parse_tap_and_trim
- Return type: static void
- Signature: tegra_sdhci_parse_tap_and_trim(struct sdhci_host * host)
- Line: 712

### tegra_sdhci_post_tuning
- Return type: static void
- Signature: tegra_sdhci_post_tuning(struct sdhci_host * host)
- Line: 936

### tegra_sdhci_readw
- Return type: static u16
- Signature: tegra_sdhci_readw(struct sdhci_host * host,int reg)
- Line: 188

### tegra_sdhci_request
- Return type: static void
- Signature: tegra_sdhci_request(struct mmc_host * mmc,struct mmc_request * mrq)
- Line: 696

### tegra_sdhci_reset
- Return type: static void
- Signature: tegra_sdhci_reset(struct sdhci_host * host,u8 mask)
- Line: 365

### tegra_sdhci_set_clock
- Return type: static void
- Signature: tegra_sdhci_set_clock(struct sdhci_host * host,unsigned int clock)
- Line: 748

### tegra_sdhci_set_dma_mask
- Return type: static int
- Signature: tegra_sdhci_set_dma_mask(struct sdhci_host * host)
- Line: 1348

### tegra_sdhci_set_dqs_trim
- Return type: static void
- Signature: tegra_sdhci_set_dqs_trim(struct sdhci_host * host,u8 trim)
- Line: 825

### tegra_sdhci_set_pad_autocal_offset
- Return type: static void
- Signature: tegra_sdhci_set_pad_autocal_offset(struct sdhci_host * host,u16 pdpu)
- Line: 443

### tegra_sdhci_set_padctrl
- Return type: static int
- Signature: tegra_sdhci_set_padctrl(struct sdhci_host * host,int voltage,bool state_drvupdn)
- Line: 454

### tegra_sdhci_set_tap
- Return type: static void
- Signature: tegra_sdhci_set_tap(struct sdhci_host * host,unsigned int tap)
- Line: 335

### tegra_sdhci_set_timeout
- Return type: static void
- Signature: tegra_sdhci_set_timeout(struct sdhci_host * host,struct mmc_command * cmd)
- Line: 1288

### tegra_sdhci_set_uhs_signaling
- Return type: static void
- Signature: tegra_sdhci_set_uhs_signaling(struct sdhci_host * host,unsigned timing)
- Line: 1006

### tegra_sdhci_tap_correction
- Return type: static void
- Signature: tegra_sdhci_tap_correction(struct sdhci_host * host,u8 thd_up,u8 thd_low,u8 fixed_tap)
- Line: 853

### tegra_sdhci_voltage_switch
- Return type: static void
- Signature: tegra_sdhci_voltage_switch(struct sdhci_host * host)
- Line: 1174

### tegra_sdhci_writel
- Return type: static void
- Signature: tegra_sdhci_writel(struct sdhci_host * host,u32 val,int reg)
- Line: 224

### tegra_sdhci_writew
- Return type: static void
- Signature: tegra_sdhci_writew(struct sdhci_host * host,u16 val,int reg)
- Line: 203

## Structs (3)

### sdhci_tegra
- Line: 161
- Members:
  - pdata: const struct sdhci_pltfm_data *
  - dma_mask: u64
  - nvquirks: u32
  - min_tap_delay: u8
  - max_tap_delay: u8
  - pull_up_3v3: u32
  - pull_down_3v3: u32
  - pull_up_3v3_timeout: u32
  - pull_down_3v3_timeout: u32
  - pull_up_1v8: u32
  - pull_down_1v8: u32
  - pull_up_1v8_timeout: u32
  - pull_down_1v8_timeout: u32
  - pull_up_sdr104: u32
  - pull_down_sdr104: u32
  - pull_up_hs400: u32
  - pull_down_hs400: u32
  - soc_data: const struct sdhci_tegra_soc_data *
  - power_gpio: gpio_desc *
  - tmclk: clk *
  - ddr_signaling: bool
  - pad_calib_required: bool
  - pad_control_available: bool
  - rst: reset_control *
  - pinctrl_sdmmc: pinctrl *
  - pinctrl_state_3v3: pinctrl_state *
  - pinctrl_state_1v8: pinctrl_state *
  - pinctrl_state_3v3_drv: pinctrl_state *
  - pinctrl_state_1v8_drv: pinctrl_state *
  - autocal_offsets: sdhci_tegra_autocal_offsets
  - last_calib: ktime_t
  - default_tap: u32
  - default_trim: u32
  - dqs_trim: u32
  - enable_hwcq: bool
  - curr_clk_rate: unsigned long
  - tuned_tap_delay: u8
  - stream_id: u32

### sdhci_tegra_autocal_offsets
- Line: 146
- Members:
  - pdata: const struct sdhci_pltfm_data *
  - dma_mask: u64
  - nvquirks: u32
  - min_tap_delay: u8
  - max_tap_delay: u8
  - pull_up_3v3: u32
  - pull_down_3v3: u32
  - pull_up_3v3_timeout: u32
  - pull_down_3v3_timeout: u32
  - pull_up_1v8: u32
  - pull_down_1v8: u32
  - pull_up_1v8_timeout: u32
  - pull_down_1v8_timeout: u32
  - pull_up_sdr104: u32
  - pull_down_sdr104: u32
  - pull_up_hs400: u32
  - pull_down_hs400: u32
  - soc_data: const struct sdhci_tegra_soc_data *
  - power_gpio: gpio_desc *
  - tmclk: clk *
  - ddr_signaling: bool
  - pad_calib_required: bool
  - pad_control_available: bool
  - rst: reset_control *
  - pinctrl_sdmmc: pinctrl *
  - pinctrl_state_3v3: pinctrl_state *
  - pinctrl_state_1v8: pinctrl_state *
  - pinctrl_state_3v3_drv: pinctrl_state *
  - pinctrl_state_1v8_drv: pinctrl_state *
  - autocal_offsets: sdhci_tegra_autocal_offsets
  - last_calib: ktime_t
  - default_tap: u32
  - default_trim: u32
  - dqs_trim: u32
  - enable_hwcq: bool
  - curr_clk_rate: unsigned long
  - tuned_tap_delay: u8
  - stream_id: u32

### sdhci_tegra_soc_data
- Line: 137
- Members:
  - pdata: const struct sdhci_pltfm_data *
  - dma_mask: u64
  - nvquirks: u32
  - min_tap_delay: u8
  - max_tap_delay: u8
  - pull_up_3v3: u32
  - pull_down_3v3: u32
  - pull_up_3v3_timeout: u32
  - pull_down_3v3_timeout: u32
  - pull_up_1v8: u32
  - pull_down_1v8: u32
  - pull_up_1v8_timeout: u32
  - pull_down_1v8_timeout: u32
  - pull_up_sdr104: u32
  - pull_down_sdr104: u32
  - pull_up_hs400: u32
  - pull_down_hs400: u32
  - soc_data: const struct sdhci_tegra_soc_data *
  - power_gpio: gpio_desc *
  - tmclk: clk *
  - ddr_signaling: bool
  - pad_calib_required: bool
  - pad_control_available: bool
  - rst: reset_control *
  - pinctrl_sdmmc: pinctrl *
  - pinctrl_state_3v3: pinctrl_state *
  - pinctrl_state_1v8: pinctrl_state *
  - pinctrl_state_3v3_drv: pinctrl_state *
  - pinctrl_state_1v8_drv: pinctrl_state *
  - autocal_offsets: sdhci_tegra_autocal_offsets
  - last_calib: ktime_t
  - default_tap: u32
  - default_trim: u32
  - dqs_trim: u32
  - enable_hwcq: bool
  - curr_clk_rate: unsigned long
  - tuned_tap_delay: u8
  - stream_id: u32

## Variables (22)

- static **sdhci_tegra114_pdata** : const struct sdhci_pltfm_data (line 1437)
- static **sdhci_tegra124_pdata** : const struct sdhci_pltfm_data (line 1454)
- static **sdhci_tegra186_pdata** : const struct sdhci_pltfm_data (line 1524)
- static **sdhci_tegra20_pdata** : const struct sdhci_pltfm_data (line 1375)
- static **sdhci_tegra210_pdata** : const struct sdhci_pltfm_data (line 1486)
- static **sdhci_tegra30_pdata** : const struct sdhci_pltfm_data (line 1392)
- static **sdhci_tegra_cqhci_ops** : const struct cqhci_host_ops (line 1338)
- static **sdhci_tegra_dev_pm_ops** : const struct dev_pm_ops (line 1913)
- static **sdhci_tegra_driver** : platform_driver (line 1918)
- static **sdhci_tegra_dt_match** : const struct of_device_id[] (line 1575)
- static **soc_data_tegra114** : const struct sdhci_tegra_soc_data (line 1448)
- static **soc_data_tegra124** : const struct sdhci_tegra_soc_data (line 1465)
- static **soc_data_tegra186** : const struct sdhci_tegra_soc_data (line 1534)
- static **soc_data_tegra194** : const struct sdhci_tegra_soc_data (line 1548)
- static **soc_data_tegra20** : const struct sdhci_tegra_soc_data (line 1384)
- static **soc_data_tegra210** : const struct sdhci_tegra_soc_data (line 1496)
- static **soc_data_tegra234** : const struct sdhci_tegra_soc_data (line 1561)
- static **soc_data_tegra30** : const struct sdhci_tegra_soc_data (line 1412)
- static **tegra114_sdhci_ops** : const struct sdhci_ops (line 1422)
- static **tegra186_sdhci_ops** : const struct sdhci_ops (line 1509)
- static **tegra210_sdhci_ops** : const struct sdhci_ops (line 1471)
- static **tegra_sdhci_ops** : const struct sdhci_ops (line 1361)

## Macros (67)

- **NVQUIRK_CQHCI_DCMD_R1B_CMD_TIMING** (line 119)
- **NVQUIRK_DIS_CARD_CLK_CONFIG_TAP** (line 118)
- **NVQUIRK_ENABLE_BLOCK_GAP_DET** (line 102)
- **NVQUIRK_ENABLE_DDR50** (line 106)
- **NVQUIRK_ENABLE_SDHCI_SPEC_300** (line 103)
- **NVQUIRK_ENABLE_SDR104** (line 105)
- **NVQUIRK_ENABLE_SDR50** (line 104)
- **NVQUIRK_FORCE_SDHCI_SPEC_200** (line 101)
- **NVQUIRK_HAS_ANDROID_GPT_SECTOR** (line 127)
- **NVQUIRK_HAS_PADCALIB** (line 111)
- **NVQUIRK_HAS_TMCLK** (line 125)
- **NVQUIRK_NEEDS_PAD_CONTROL** (line 117)
- **NVQUIRK_PROGRAM_STREAMID** (line 128)
- **SDHCI_AUTO_CAL_ENABLE** (line 87)
- **SDHCI_AUTO_CAL_PDPU_OFFSET_MASK** (line 88)
- **SDHCI_AUTO_CAL_START** (line 86)
- **SDHCI_CLOCK_CTRL_PADPIPE_CLKEN_OVERRIDE** (line 43)
- **SDHCI_CLOCK_CTRL_SDR50_TUNING_OVERRIDE** (line 42)
- **SDHCI_CLOCK_CTRL_SPI_MODE_CLKEN_OVERRIDE** (line 44)
- **SDHCI_CLOCK_CTRL_TAP_MASK** (line 38)
- **SDHCI_CLOCK_CTRL_TAP_SHIFT** (line 39)
- **SDHCI_CLOCK_CTRL_TRIM_MASK** (line 40)
- **SDHCI_CLOCK_CTRL_TRIM_SHIFT** (line 41)
- **SDHCI_COMP_PADCTRL_DRVUPDN_OFFSET_MASK** (line 94)
- **SDHCI_MISC_CTRL_ENABLE_DDR50** (line 58)
- **SDHCI_MISC_CTRL_ENABLE_SDHCI_SPEC_300** (line 57)
- **SDHCI_MISC_CTRL_ENABLE_SDR104** (line 55)
- **SDHCI_MISC_CTRL_ENABLE_SDR50** (line 56)
- **SDHCI_MISC_CTRL_ERASE_TIMEOUT_LIMIT** (line 54)
- **SDHCI_TEGRA_AUTO_CAL_ACTIVE** (line 97)
- **SDHCI_TEGRA_AUTO_CAL_CONFIG** (line 85)
- **SDHCI_TEGRA_AUTO_CAL_STATUS** (line 96)
- **SDHCI_TEGRA_CAP_OVERRIDES_DQS_TRIM_MASK** (line 50)
- **SDHCI_TEGRA_CAP_OVERRIDES_DQS_TRIM_SHIFT** (line 51)
- **SDHCI_TEGRA_CIF2AXI_CTRL_0** (line 99)
- **SDHCI_TEGRA_CQE_BASE_ADDR** (line 131)
- **SDHCI_TEGRA_CQE_TRNS_MODE** (line 133)
- **SDHCI_TEGRA_DLLCAL_CALIBRATE** (line 61)
- **SDHCI_TEGRA_DLLCAL_STA_ACTIVE** (line 64)
- **SDHCI_TEGRA_SDMEM_COMP_PADCTRL** (line 90)
- **SDHCI_TEGRA_SDMEM_COMP_PADCTRL_E_INPUT_E_PWRD** (line 93)
- **SDHCI_TEGRA_SDMEM_COMP_PADCTRL_VREF_SEL_MASK** (line 91)
- **SDHCI_TEGRA_SDMEM_COMP_PADCTRL_VREF_SEL_VAL** (line 92)
- **SDHCI_TEGRA_SYS_SW_CTRL_ENHANCED_STROBE** (line 47)
- **SDHCI_TEGRA_VENDOR_CAP_OVERRIDES** (line 49)
- **SDHCI_TEGRA_VENDOR_CLOCK_CTRL** (line 37)
- **SDHCI_TEGRA_VENDOR_DLLCAL_CFG** (line 60)
- **SDHCI_TEGRA_VENDOR_DLLCAL_STA** (line 63)
- **SDHCI_TEGRA_VENDOR_MISC_CTRL** (line 53)
- **SDHCI_TEGRA_VENDOR_SYS_SW_CTRL** (line 46)
- **SDHCI_TEGRA_VNDR_TUN_CTRL1_0** (line 78)
- **SDHCI_TEGRA_VNDR_TUN_STATUS0** (line 79)
- **SDHCI_TEGRA_VNDR_TUN_STATUS1** (line 80)
- **SDHCI_TEGRA_VNDR_TUN_STATUS1_END_TAP_SHIFT** (line 82)
- **SDHCI_TEGRA_VNDR_TUN_STATUS1_TAP_MASK** (line 81)
- **SDHCI_VNDR_TUN_CTRL0_0** (line 66)
- **SDHCI_VNDR_TUN_CTRL0_MUL_M_MASK** (line 70)
- **SDHCI_VNDR_TUN_CTRL0_MUL_M_SHIFT** (line 71)
- **SDHCI_VNDR_TUN_CTRL0_START_TAP_VAL_MASK** (line 68)
- **SDHCI_VNDR_TUN_CTRL0_START_TAP_VAL_SHIFT** (line 69)
- **SDHCI_VNDR_TUN_CTRL0_TUN_HW_TAP** (line 67)
- **SDHCI_VNDR_TUN_CTRL0_TUN_ITER_MASK** (line 72)
- **SDHCI_VNDR_TUN_CTRL0_TUN_ITER_SHIFT** (line 73)
- **SDHCI_VNDR_TUN_CTRL0_TUN_WORD_SEL_MASK** (line 76)
- **TRIES_128** (line 74)
- **TRIES_256** (line 75)
- **TUNING_WORD_BIT_SIZE** (line 83)
