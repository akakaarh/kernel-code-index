# drivers/mmc/host/dw_mmc-pltfm.c

Subsystem: drivers/mmc

## Functions (4)

### dw_mci_pltfm_probe
- Return type: static int
- Signature: dw_mci_pltfm_probe(struct platform_device * pdev)
- Line: 101

### dw_mci_pltfm_register
- Return type: int
- Signature: dw_mci_pltfm_register(struct platform_device * pdev,const struct dw_mci_drv_data * drv_data)
- Line: 30

### dw_mci_pltfm_remove
- Return type: void
- Signature: dw_mci_pltfm_remove(struct platform_device * pdev)
- Line: 114

### dw_mci_socfpga_priv_init
- Return type: static int
- Signature: dw_mci_socfpga_priv_init(struct dw_mci * host)
- Line: 59

## Variables (3)

- static **dw_mci_pltfm_driver** : platform_driver (line 122)
- static **dw_mci_pltfm_match** : const struct of_device_id[] (line 93)
- static **socfpga_drv_data** : const struct dw_mci_drv_data (line 89)

## Macros (2)

- **SOCFPGA_DW_MMC_CLK_PHASE_STEP** (line 26)
- **SYSMGR_SDMMC_CTRL_SET**(smplsel,drvsel,reg_shift) (line 27)
