# drivers/mmc/host/dw_mmc-hi3798mv200.c

Subsystem: drivers/mmc

## Functions (7)

### dw_mci_hi3798mv200_disable_tuning
- Return type: static int
- Signature: dw_mci_hi3798mv200_disable_tuning(struct dw_mci * host)
- Line: 83

### dw_mci_hi3798mv200_enable_tuning
- Return type: static int
- Signature: dw_mci_hi3798mv200_enable_tuning(struct dw_mci * host)
- Line: 76

### dw_mci_hi3798mv200_execute_tuning_mix_mode
- Return type: static int
- Signature: dw_mci_hi3798mv200_execute_tuning_mix_mode(struct dw_mci * host,u32 opcode)
- Line: 90

### dw_mci_hi3798mv200_init
- Return type: static int
- Signature: dw_mci_hi3798mv200_init(struct dw_mci * host)
- Line: 178

### dw_mci_hi3798mv200_probe
- Return type: static int
- Signature: dw_mci_hi3798mv200_probe(struct platform_device * pdev)
- Line: 219

### dw_mci_hi3798mv200_remove
- Return type: static void
- Signature: dw_mci_hi3798mv200_remove(struct platform_device * pdev)
- Line: 224

### dw_mci_hi3798mv200_set_ios
- Return type: static void
- Signature: dw_mci_hi3798mv200_set_ios(struct dw_mci * host,struct mmc_ios * ios)
- Line: 35

## Structs (1)

### dw_mci_hi3798mv200_priv
- Line: 28
- Members:
  - sample_clk: clk *
  - drive_clk: clk *
  - crg_reg: regmap *
  - sap_dll_offset: u32

## Variables (3)

- static **dw_mci_hi3798mv200_driver** : platform_driver (line 230)
- static **dw_mci_hi3798mv200_match** : const struct of_device_id[] (line 214)
- static **hi3798mv200_data** : const struct dw_mci_drv_data (line 207)

## Macros (4)

- **ALL_INT_CLR** (line 23)
- **SAP_DLL_CTRL_DLLMODE** (line 26)
- **SDMMC_TUNING_CTRL** (line 20)
- **SDMMC_TUNING_FIND_EDGE** (line 21)
