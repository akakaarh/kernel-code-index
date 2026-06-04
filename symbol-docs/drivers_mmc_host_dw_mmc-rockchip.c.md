# drivers/mmc/host/dw_mmc-rockchip.c

Subsystem: drivers/mmc

## Functions (14)

### dw_mci_common_parse_dt
- Return type: static int
- Signature: dw_mci_common_parse_dt(struct dw_mci * host)
- Line: 422

### dw_mci_rk3288_execute_tuning
- Return type: static int
- Signature: dw_mci_rk3288_execute_tuning(struct dw_mci * host,u32 opcode)
- Line: 296

### dw_mci_rk3288_parse_dt
- Return type: static int
- Signature: dw_mci_rk3288_parse_dt(struct dw_mci * host)
- Line: 444

### dw_mci_rk3288_set_ios
- Return type: static void
- Signature: dw_mci_rk3288_set_ios(struct dw_mci * host,struct mmc_ios * ios)
- Line: 179

### dw_mci_rk3576_parse_dt
- Return type: static int
- Signature: dw_mci_rk3576_parse_dt(struct dw_mci * host)
- Line: 468

### dw_mci_rockchip_init
- Return type: static int
- Signature: dw_mci_rockchip_init(struct dw_mci * host)
- Line: 482

### dw_mci_rockchip_probe
- Return type: static int
- Signature: dw_mci_rockchip_probe(struct platform_device * pdev)
- Line: 546

### dw_mci_rockchip_remove
- Return type: static void
- Signature: dw_mci_rockchip_remove(struct platform_device * pdev)
- Line: 577

### dw_mci_rockchip_runtime_resume
- Return type: static int
- Signature: dw_mci_rockchip_runtime_resume(struct device * dev)
- Line: 600

### dw_mci_rockchip_runtime_suspend
- Return type: static int
- Signature: dw_mci_rockchip_runtime_suspend(struct device * dev)
- Line: 586

### rockchip_mmc_get_internal_phase
- Return type: static int
- Signature: rockchip_mmc_get_internal_phase(struct dw_mci * host,bool sample)
- Line: 47

### rockchip_mmc_get_phase
- Return type: static int
- Signature: rockchip_mmc_get_phase(struct dw_mci * host,bool sample)
- Line: 79

### rockchip_mmc_set_internal_phase
- Return type: static int
- Signature: rockchip_mmc_set_internal_phase(struct dw_mci * host,bool sample,int degrees)
- Line: 90

### rockchip_mmc_set_phase
- Return type: static int
- Signature: rockchip_mmc_set_phase(struct dw_mci * host,bool sample,int degrees)
- Line: 168

## Structs (2)

### dw_mci_rockchip_priv_data
- Line: 33
- Members:
  - drv_clk: clk *
  - sample_clk: clk *
  - default_sample_phase: int
  - num_phases: int
  - internal_phase: bool
  - sample_phase: int
  - drv_phase: int
  - start: int
  - end: int

### range_t
- Line: 303
- Members:
  - drv_clk: clk *
  - sample_clk: clk *
  - default_sample_phase: int
  - num_phases: int
  - internal_phase: bool
  - sample_phase: int
  - drv_phase: int
  - start: int
  - end: int

## Variables (7)

- static **dw_mci_rockchip_dev_pm_ops** : const struct dev_pm_ops (line 620)
- static **dw_mci_rockchip_match** : const struct of_device_id[] (line 535)
- static **dw_mci_rockchip_pltfm_driver** : platform_driver (line 625)
- static **freqs** : const unsigned int[] (line 31)
- static **rk2928_drv_data** : const struct dw_mci_drv_data (line 515)
- static **rk3288_drv_data** : const struct dw_mci_drv_data (line 519)
- static **rk3576_drv_data** : const struct dw_mci_drv_data (line 527)

## Macros (12)

- **MEM_CLK_AUTOGATE_ENABLE** (line 23)
- **RK3288_CLKGEN_DIV** (line 19)
- **ROCKCHIP_MMC_DEGREE_MASK** (line 25)
- **ROCKCHIP_MMC_DEGREE_OFFSET** (line 26)
- **ROCKCHIP_MMC_DELAYNUM_MASK** (line 28)
- **ROCKCHIP_MMC_DELAYNUM_OFFSET** (line 27)
- **ROCKCHIP_MMC_DELAY_ELEMENT_PSEC** (line 29)
- **ROCKCHIP_MMC_DELAY_SEL** (line 24)
- **SDMMC_MISC_CON** (line 22)
- **SDMMC_TIMING_CON0** (line 20)
- **SDMMC_TIMING_CON1** (line 21)
- **TUNING_ITERATION_TO_PHASE**(i,num_phases) (line 293)
