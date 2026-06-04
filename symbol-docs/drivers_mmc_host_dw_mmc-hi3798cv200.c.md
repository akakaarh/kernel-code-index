# drivers/mmc/host/dw_mmc-hi3798cv200.c

Subsystem: drivers/mmc

## Functions (5)

### dw_mci_hi3798cv200_execute_tuning
- Return type: static int
- Signature: dw_mci_hi3798cv200_execute_tuning(struct dw_mci * host,u32 opcode)
- Line: 60

### dw_mci_hi3798cv200_init
- Return type: static int
- Signature: dw_mci_hi3798cv200_init(struct dw_mci * host)
- Line: 118

### dw_mci_hi3798cv200_probe
- Return type: static int
- Signature: dw_mci_hi3798cv200_probe(struct platform_device * pdev)
- Line: 166

### dw_mci_hi3798cv200_remove
- Return type: static void
- Signature: dw_mci_hi3798cv200_remove(struct platform_device * pdev)
- Line: 171

### dw_mci_hi3798cv200_set_ios
- Return type: static void
- Signature: dw_mci_hi3798cv200_set_ios(struct dw_mci * host,struct mmc_ios * ios)
- Line: 26

## Structs (1)

### hi3798cv200_priv
- Line: 21
- Members:
  - sample_clk: clk *
  - drive_clk: clk *

## Variables (3)

- static **dw_mci_hi3798cv200_driver** : platform_driver (line 188)
- static **dw_mci_hi3798cv200_match** : const struct of_device_id[] (line 182)
- static **hi3798cv200_data** : const struct dw_mci_drv_data (line 159)

## Macros (1)

- **ALL_INT_CLR** (line 19)
