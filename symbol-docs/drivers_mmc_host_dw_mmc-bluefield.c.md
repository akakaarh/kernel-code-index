# drivers/mmc/host/dw_mmc-bluefield.c

Subsystem: drivers/mmc

## Functions (3)

### dw_mci_bluefield_hw_reset
- Return type: static void
- Signature: dw_mci_bluefield_hw_reset(struct dw_mci * host)
- Line: 41

### dw_mci_bluefield_probe
- Return type: static int
- Signature: dw_mci_bluefield_probe(struct platform_device * pdev)
- Line: 64

### dw_mci_bluefield_set_ios
- Return type: static void
- Signature: dw_mci_bluefield_set_ios(struct dw_mci * host,struct mmc_ios * ios)
- Line: 27

## Variables (3)

- static **bluefield_drv_data** : const struct dw_mci_drv_data (line 52)
- static **dw_mci_bluefield_match** : const struct of_device_id[] (line 57)
- static **dw_mci_bluefield_pltfm_driver** : platform_driver (line 69)

## Macros (5)

- **BLUEFIELD_SMC_SET_EMMC_RST_N** (line 25)
- **BLUEFIELD_UHS_REG_EXT_DRIVE** (line 22)
- **BLUEFIELD_UHS_REG_EXT_SAMPLE** (line 21)
- **UHS_REG_EXT_DRIVE_MASK** (line 20)
- **UHS_REG_EXT_SAMPLE_MASK** (line 19)
