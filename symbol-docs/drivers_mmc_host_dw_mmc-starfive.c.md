# drivers/mmc/host/dw_mmc-starfive.c

Subsystem: drivers/mmc

## Functions (4)

### dw_mci_starfive_execute_tuning
- Return type: static int
- Signature: dw_mci_starfive_execute_tuning(struct dw_mci * host,u32 opcode)
- Line: 56

### dw_mci_starfive_probe
- Return type: static int
- Signature: dw_mci_starfive_probe(struct platform_device * pdev)
- Line: 110

### dw_mci_starfive_set_ios
- Return type: static void
- Signature: dw_mci_starfive_set_ios(struct dw_mci * host,struct mmc_ios * ios)
- Line: 26

### dw_mci_starfive_set_sample_phase
- Return type: static void
- Signature: dw_mci_starfive_set_sample_phase(struct dw_mci * host,u32 smpl_phase)
- Line: 42

## Variables (3)

- static **dw_mci_starfive_driver** : platform_driver (line 115)
- static **dw_mci_starfive_match** : const struct of_device_id[] (line 103)
- static **starfive_data** : const struct dw_mci_drv_data (line 97)

## Macros (3)

- **ALL_INT_CLR** (line 21)
- **MAX_DELAY_CHAIN** (line 22)
- **STARFIVE_SMPL_PHASE** (line 24)
