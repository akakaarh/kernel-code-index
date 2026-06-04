# drivers/mmc/host/dw_mmc-exynos.c

Subsystem: drivers/mmc

## Functions (21)

### dw_mci_exynos_adjust_clock
- Return type: static void
- Signature: dw_mci_exynos_adjust_clock(struct dw_mci * host,unsigned int wanted)
- Line: 299

### dw_mci_exynos_config_hs400
- Return type: static void
- Signature: dw_mci_exynos_config_hs400(struct dw_mci * host,u32 timing)
- Line: 266

### dw_mci_exynos_config_smu
- Return type: static void
- Signature: dw_mci_exynos_config_smu(struct dw_mci * host)
- Line: 104

### dw_mci_exynos_execute_tuning
- Return type: static int
- Signature: dw_mci_exynos_execute_tuning(struct dw_mci * host,u32 opcode)
- Line: 533

### dw_mci_exynos_get_best_clksmpl
- Return type: static s8
- Signature: dw_mci_exynos_get_best_clksmpl(u8 candidates)
- Line: 495

### dw_mci_exynos_get_ciu_div
- Return type: static u8
- Signature: dw_mci_exynos_get_ciu_div(struct dw_mci * host)
- Line: 86

### dw_mci_exynos_get_clksmpl
- Return type: static u8
- Signature: dw_mci_exynos_get_clksmpl(struct dw_mci * host)
- Line: 427

### dw_mci_exynos_get_drto_clks
- Return type: static u32
- Signature: dw_mci_exynos_get_drto_clks(struct dw_mci * host)
- Line: 614

### dw_mci_exynos_move_next_clksmpl
- Return type: static u8
- Signature: dw_mci_exynos_move_next_clksmpl(struct dw_mci * host)
- Line: 465

### dw_mci_exynos_parse_dt
- Return type: static int
- Signature: dw_mci_exynos_parse_dt(struct dw_mci * host)
- Line: 373

### dw_mci_exynos_prepare_hs400_tuning
- Return type: static int
- Signature: dw_mci_exynos_prepare_hs400_tuning(struct dw_mci * host,struct mmc_ios * ios)
- Line: 565

### dw_mci_exynos_priv_init
- Return type: static int
- Signature: dw_mci_exynos_priv_init(struct dw_mci * host)
- Line: 124

### dw_mci_exynos_probe
- Return type: static int
- Signature: dw_mci_exynos_probe(struct platform_device * pdev)
- Line: 675

### dw_mci_exynos_remove
- Return type: static void
- Signature: dw_mci_exynos_remove(struct platform_device * pdev)
- Line: 700

### dw_mci_exynos_resume_noirq
- Return type: static int
- Signature: dw_mci_exynos_resume_noirq(struct device * dev)
- Line: 230

### dw_mci_exynos_runtime_resume
- Return type: static int
- Signature: dw_mci_exynos_runtime_resume(struct device * dev)
- Line: 192

### dw_mci_exynos_set_clksel_timing
- Return type: static void
- Signature: dw_mci_exynos_set_clksel_timing(struct dw_mci * host,u32 timing)
- Line: 156

### dw_mci_exynos_set_clksmpl
- Return type: static void
- Signature: dw_mci_exynos_set_clksmpl(struct dw_mci * host,u8 sample)
- Line: 441

### dw_mci_exynos_set_data_timeout
- Return type: static void
- Signature: dw_mci_exynos_set_data_timeout(struct dw_mci * host,unsigned int timeout_ns)
- Line: 576

### dw_mci_exynos_set_ios
- Return type: static void
- Signature: dw_mci_exynos_set_ios(struct dw_mci * host,struct mmc_ios * ios)
- Line: 331

### dw_mci_exynos_suspend_noirq
- Return type: static int
- Signature: dw_mci_exynos_suspend_noirq(struct device * dev)
- Line: 213

## Structs (2)

### dw_mci_exynos_compatible
- Line: 49
- Members:
  - ctrl_type: dw_mci_exynos_type
  - ciu_div: u8
  - sdr_timing: u32
  - ddr_timing: u32
  - hs400_timing: u32
  - tuned_sample: u32
  - cur_speed: u32
  - dqs_delay: u32
  - saved_dqs_en: u32
  - saved_strobe_ctrl: u32
  - compatible: char *
  - ctrl_type: dw_mci_exynos_type

### dw_mci_exynos_priv_data
- Line: 36
- Members:
  - ctrl_type: dw_mci_exynos_type
  - ciu_div: u8
  - sdr_timing: u32
  - ddr_timing: u32
  - hs400_timing: u32
  - tuned_sample: u32
  - cur_speed: u32
  - dqs_delay: u32
  - saved_dqs_en: u32
  - saved_strobe_ctrl: u32
  - compatible: char *
  - ctrl_type: dw_mci_exynos_type

## Enums (1)

### dw_mci_exynos_type
- Line: 22

## Variables (7)

- static **artpec_drv_data** : const struct dw_mci_drv_data (line 642)
- static **dw_mci_exynos_match** : const struct of_device_id[] (line 652)
- static **dw_mci_exynos_pltfm_driver** : platform_driver (line 714)
- static **dw_mci_exynos_pmops** : const struct dev_pm_ops (line 709)
- **exynos_compat** : dw_mci_exynos_compatible[] (line 52)
- static **exynos_drv_data** : const struct dw_mci_drv_data (line 631)
- static **exynos_dwmmc_caps** : unsigned long[4] (line 624)
