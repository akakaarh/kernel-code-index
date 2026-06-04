# drivers/mmc/host/dw_mmc-k3.c

Subsystem: drivers/mmc

## Functions (13)

### dw_mci_get_best_clksmpl
- Return type: static int
- Signature: dw_mci_get_best_clksmpl(unsigned int sample_flag)
- Line: 312

### dw_mci_hi3660_execute_tuning
- Return type: static int
- Signature: dw_mci_hi3660_execute_tuning(struct dw_mci * host,u32 opcode)
- Line: 358

### dw_mci_hi3660_init
- Return type: static int
- Signature: dw_mci_hi3660_init(struct dw_mci * host)
- Line: 259

### dw_mci_hi3660_set_ios
- Return type: static void
- Signature: dw_mci_hi3660_set_ios(struct dw_mci * host,struct mmc_ios * ios)
- Line: 288

### dw_mci_hi3660_switch_voltage
- Return type: static int
- Signature: dw_mci_hi3660_switch_voltage(struct dw_mci * host,struct mmc_ios * ios)
- Line: 391

### dw_mci_hi6220_execute_tuning
- Return type: static int
- Signature: dw_mci_hi6220_execute_tuning(struct dw_mci * host,u32 opcode)
- Line: 192

### dw_mci_hi6220_parse_dt
- Return type: static int
- Signature: dw_mci_hi6220_parse_dt(struct dw_mci * host)
- Line: 116

### dw_mci_hi6220_set_ios
- Return type: static void
- Signature: dw_mci_hi6220_set_ios(struct dw_mci * host,struct mmc_ios * ios)
- Line: 178

### dw_mci_hi6220_switch_voltage
- Return type: static int
- Signature: dw_mci_hi6220_switch_voltage(struct dw_mci * host,struct mmc_ios * ios)
- Line: 133

### dw_mci_hs_set_timing
- Return type: static int
- Signature: dw_mci_hs_set_timing(struct dw_mci * host,int timing,int smpl_phase)
- Line: 206

### dw_mci_k3_probe
- Return type: static int
- Signature: dw_mci_k3_probe(struct platform_device * pdev)
- Line: 440

### dw_mci_k3_set_ios
- Return type: static void
- Signature: dw_mci_k3_set_ios(struct dw_mci * host,struct mmc_ios * ios)
- Line: 101

### dw_mci_set_sel18
- Return type: static int
- Signature: dw_mci_set_sel18(struct dw_mci * host,bool set)
- Line: 269

## Structs (2)

### hs_timing
- Line: 66
- Members:
  - cur_speed: u32
  - reg: regmap *
  - drv_phase: u32
  - smpl_dly: u32
  - smpl_phase_max: u32
  - smpl_phase_min: u32

### k3_priv
- Line: 55
- Members:
  - cur_speed: u32
  - reg: regmap *
  - drv_phase: u32
  - smpl_dly: u32
  - smpl_phase_max: u32
  - smpl_phase_min: u32

## Variables (7)

- static **dw_mci_hi6220_caps** : unsigned long[] (line 60)
- static **dw_mci_k3_match** : const struct of_device_id[] (line 432)
- static **dw_mci_k3_pltfm_driver** : platform_driver (line 451)
- static **hi3660_data** : const struct dw_mci_drv_data (line 424)
- static **hi6220_data** : const struct dw_mci_drv_data (line 197)
- static **hs_timing_cfg** : hs_timing[][] (line 73)
- static **k3_drv_data** : const struct dw_mci_drv_data (line 112)

## Macros (20)

- **AO_SCTRL_CTRL3** (line 27)
- **AO_SCTRL_SEL18** (line 26)
- **DWMMC_SDIO_ID** (line 29)
- **ENABLE_SHIFT_MAX_SMPL** (line 51)
- **ENABLE_SHIFT_MIN_SMPL** (line 50)
- **GENCLK_DIV** (line 36)
- **GPIO_CLK_DIV_MASK** (line 39)
- **GPIO_CLK_ENABLE** (line 38)
- **GPIO_USE_SAMPLE_DLY_MASK** (line 40)
- **NUM_PHASES** (line 48)
- **SDCARD_IO_SEL18** (line 32)
- **SDCARD_RD_THRESHOLD** (line 34)
- **SOC_SCTRL_SCPERCTRL5** (line 31)
- **TIMING_CFG_NUM** (line 46)
- **TIMING_MODE** (line 45)
- **UHS_REG_EXT_SAMPLE_DLY_MASK** (line 43)
- **UHS_REG_EXT_SAMPLE_DRVPHASE_MASK** (line 42)
- **UHS_REG_EXT_SAMPLE_PHASE_MASK** (line 41)
- **USE_DLY_MAX_SMPL** (line 53)
- **USE_DLY_MIN_SMPL** (line 52)
