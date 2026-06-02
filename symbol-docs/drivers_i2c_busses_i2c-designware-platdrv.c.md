# drivers/i2c/busses/i2c-designware-platdrv.c

Subsystem: drivers/i2c

## Functions (9)

### dw_i2c_exit_driver
- Return type: static void __exit
- Signature: dw_i2c_exit_driver(void)
- Line: 310

### dw_i2c_get_parent_regmap
- Return type: static int
- Signature: dw_i2c_get_parent_regmap(struct dw_i2c_dev * dev)
- Line: 40

### dw_i2c_init_driver
- Return type: static int __init
- Signature: dw_i2c_init_driver(void)
- Line: 304

### dw_i2c_plat_pm_cleanup
- Return type: static void
- Signature: dw_i2c_plat_pm_cleanup(struct dw_i2c_dev * dev)
- Line: 49

### dw_i2c_plat_probe
- Return type: static int
- Signature: dw_i2c_plat_probe(struct platform_device * pdev)
- Line: 133

### dw_i2c_plat_remove
- Return type: static void
- Signature: dw_i2c_plat_remove(struct platform_device * pdev)
- Line: 236

### dw_i2c_plat_request_regs
- Return type: static int
- Signature: dw_i2c_plat_request_regs(struct dw_i2c_dev * dev)
- Line: 57

### i2c_dw_get_clk_rate_khz
- Return type: static u32
- Signature: i2c_dw_get_clk_rate_khz(struct dw_i2c_dev * dev)
- Line: 35

### i2c_dw_probe_lock_support
- Return type: static int
- Signature: i2c_dw_probe_lock_support(struct dw_i2c_dev * dev)
- Line: 103

## Variables (6)

- static **dw_i2c_acpi_match** : const struct acpi_device_id[] (line 262)
- static **dw_i2c_driver** : platform_driver (line 292)
- static **dw_i2c_hwmon_class_dmi** : const struct dmi_system_id[] (line 78)
- static **dw_i2c_of_match** : const struct of_device_id[] (line 254)
- static **dw_i2c_platform_ids** : const struct platform_device_id[] (line 286)
- static **i2c_dw_semaphore_cb_table** : const struct i2c_dw_semaphore_callbacks[] (line 89)
