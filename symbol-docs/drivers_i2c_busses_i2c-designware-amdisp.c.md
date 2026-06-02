# drivers/i2c/busses/i2c-designware-amdisp.c

Subsystem: drivers/i2c

## Functions (9)

### amd_isp_dw_i2c_get_clk_rate
- Return type: static u32
- Signature: amd_isp_dw_i2c_get_clk_rate(struct dw_i2c_dev * i2c_dev)
- Line: 24

### amd_isp_dw_i2c_plat_pm_cleanup
- Return type: static void
- Signature: amd_isp_dw_i2c_plat_pm_cleanup(struct dw_i2c_dev * i2c_dev)
- Line: 19

### amd_isp_dw_i2c_plat_prepare
- Return type: static int
- Signature: amd_isp_dw_i2c_plat_prepare(struct device * dev)
- Line: 111

### amd_isp_dw_i2c_plat_probe
- Return type: static int
- Signature: amd_isp_dw_i2c_plat_probe(struct platform_device * pdev)
- Line: 29

### amd_isp_dw_i2c_plat_remove
- Return type: static void
- Signature: amd_isp_dw_i2c_plat_remove(struct platform_device * pdev)
- Line: 97

### amd_isp_dw_i2c_plat_resume
- Return type: static int
- Signature: amd_isp_dw_i2c_plat_resume(struct device * dev)
- Line: 160

### amd_isp_dw_i2c_plat_runtime_resume
- Return type: static int
- Signature: amd_isp_dw_i2c_plat_runtime_resume(struct device * dev)
- Line: 147

### amd_isp_dw_i2c_plat_runtime_suspend
- Return type: static int
- Signature: amd_isp_dw_i2c_plat_runtime_suspend(struct device * dev)
- Line: 122

### amd_isp_dw_i2c_plat_suspend
- Return type: static int
- Signature: amd_isp_dw_i2c_plat_suspend(struct device * dev)
- Line: 132

## Variables (2)

- static **amd_isp_dw_i2c_dev_pm_ops** : const struct dev_pm_ops (line 170)
- static **amd_isp_dw_i2c_driver** : platform_driver (line 179)

## Macros (2)

- **AMD_ISP_I2C_INPUT_CLK** (line 17)
- **DRV_NAME** (line 16)
