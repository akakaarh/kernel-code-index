# drivers/mmc/core/regulator.c

Subsystem: drivers/mmc

## Functions (14)

### mmc_handle_regulator_event
- Return type: static int
- Signature: mmc_handle_regulator_event(struct notifier_block * nb,unsigned long event,void * data)
- Line: 278

### mmc_ocrbitnum_to_vdd
- Return type: static int
- Signature: mmc_ocrbitnum_to_vdd(int vdd_bit,int * min_uV,int * max_uV)
- Line: 28

### mmc_regulator_disable_vqmmc
- Return type: void
- Signature: mmc_regulator_disable_vqmmc(struct mmc_host * mmc)
- Line: 425

### mmc_regulator_enable_vqmmc
- Return type: int
- Signature: mmc_regulator_enable_vqmmc(struct mmc_host * mmc)
- Line: 401

### mmc_regulator_get_ocrmask
- Return type: static int
- Signature: mmc_regulator_get_ocrmask(struct regulator * supply)
- Line: 259

### mmc_regulator_get_ocrmask
- Return type: static int
- Signature: mmc_regulator_get_ocrmask(struct regulator * supply)
- Line: 62

### mmc_regulator_get_supply
- Return type: int
- Signature: mmc_regulator_get_supply(struct mmc_host * mmc)
- Line: 352

### mmc_regulator_register_undervoltage_notifier
- Return type: void
- Signature: mmc_regulator_register_undervoltage_notifier(struct mmc_host * host)
- Line: 314

### mmc_regulator_set_ocr
- Return type: int
- Signature: mmc_regulator_set_ocr(struct mmc_host * mmc,struct regulator * supply,unsigned short vdd_bit)
- Line: 107

### mmc_regulator_set_voltage_if_supported
- Return type: static int
- Signature: mmc_regulator_set_voltage_if_supported(struct regulator * regulator,int min_uV,int target_uV,int max_uV)
- Line: 139

### mmc_regulator_set_vqmmc
- Return type: int
- Signature: mmc_regulator_set_vqmmc(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 183

### mmc_regulator_set_vqmmc2
- Return type: int
- Signature: mmc_regulator_set_vqmmc2(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 242

### mmc_regulator_unregister_undervoltage_notifier
- Return type: void
- Signature: mmc_regulator_unregister_undervoltage_notifier(struct mmc_host * host)
- Line: 333

### mmc_undervoltage_workfn
- Return type: void
- Signature: mmc_undervoltage_workfn(struct work_struct * work)
- Line: 267
