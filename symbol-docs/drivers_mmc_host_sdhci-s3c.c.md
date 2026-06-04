# drivers/mmc/host/sdhci-s3c.c

Subsystem: drivers/mmc

## Functions (17)

### sdhci_cmu_get_max_clock
- Return type: static unsigned int
- Signature: sdhci_cmu_get_max_clock(struct sdhci_host * host)
- Line: 323

### sdhci_cmu_get_min_clock
- Return type: static unsigned int
- Signature: sdhci_cmu_get_min_clock(struct sdhci_host * host)
- Line: 345

### sdhci_cmu_set_clock
- Return type: static void
- Signature: sdhci_cmu_set_clock(struct sdhci_host * host,unsigned int clock)
- Line: 367

### sdhci_s3c_consider_clock
- Return type: static unsigned int
- Signature: sdhci_s3c_consider_clock(struct sdhci_s3c * ourhost,unsigned int src,unsigned int wanted)
- Line: 177

### sdhci_s3c_get_driver_data
- Return type: static const struct sdhci_s3c_drv_data *
- Signature: sdhci_s3c_get_driver_data(struct platform_device * pdev)
- Line: 473

### sdhci_s3c_get_max_clk
- Return type: static unsigned int
- Signature: sdhci_s3c_get_max_clk(struct sdhci_host * host)
- Line: 156

### sdhci_s3c_get_min_clock
- Return type: static unsigned int
- Signature: sdhci_s3c_get_min_clock(struct sdhci_host * host)
- Line: 305

### sdhci_s3c_parse_dt
- Return type: static int
- Signature: sdhci_s3c_parse_dt(struct device * dev,struct sdhci_host * host,struct s3c_sdhci_platdata * pdata)
- Line: 436

### sdhci_s3c_parse_dt
- Return type: static int
- Signature: sdhci_s3c_parse_dt(struct device * dev,struct sdhci_host * host,struct s3c_sdhci_platdata * pdata)
- Line: 466

### sdhci_s3c_probe
- Return type: static int
- Signature: sdhci_s3c_probe(struct platform_device * pdev)
- Line: 484

### sdhci_s3c_remove
- Return type: static void
- Signature: sdhci_s3c_remove(struct platform_device * pdev)
- Line: 664

### sdhci_s3c_resume
- Return type: static int
- Signature: sdhci_s3c_resume(struct device * dev)
- Line: 694

### sdhci_s3c_runtime_resume
- Return type: static int
- Signature: sdhci_s3c_runtime_resume(struct device * dev)
- Line: 718

### sdhci_s3c_runtime_suspend
- Return type: static int
- Signature: sdhci_s3c_runtime_suspend(struct device * dev)
- Line: 701

### sdhci_s3c_set_clock
- Return type: static void
- Signature: sdhci_s3c_set_clock(struct sdhci_host * host,unsigned int clock)
- Line: 225

### sdhci_s3c_suspend
- Return type: static int
- Signature: sdhci_s3c_suspend(struct device * dev)
- Line: 684

### to_s3c
- Return type: static sdhci_s3c *
- Signature: to_s3c(struct sdhci_host * host)
- Line: 145

## Structs (2)

### sdhci_s3c
- Line: 114
- Members:
  - host: sdhci_host *
  - pdev: platform_device *
  - ioarea: resource *
  - pdata: s3c_sdhci_platdata *
  - cur_clk: int
  - ext_cd_irq: int
  - clk_io: clk *
  - clk_bus: clk * []
  - clk_rates: unsigned long[]
  - no_divider: bool
  - sdhci_quirks: unsigned int
  - no_divider: bool
  - ops: const struct sdhci_ops *

### sdhci_s3c_drv_data
- Line: 139
- Members:
  - host: sdhci_host *
  - pdev: platform_device *
  - ioarea: resource *
  - pdata: s3c_sdhci_platdata *
  - cur_clk: int
  - ext_cd_irq: int
  - clk_io: clk *
  - clk_bus: clk * []
  - clk_rates: unsigned long[]
  - no_divider: bool
  - sdhci_quirks: unsigned int
  - no_divider: bool
  - ops: const struct sdhci_ops *

## Variables (7)

- static **__maybe_unused** : const struct sdhci_ops sdhci_s3c_ops_exynos4 (line 426)
- static **exynos4_sdhci_drv_data** : const struct sdhci_s3c_drv_data (line 746)
- static **sdhci_s3c_driver** : platform_driver (line 760)
- static **sdhci_s3c_driver_ids** : const struct platform_device_id[] (line 736)
- static **sdhci_s3c_dt_match** : const struct of_device_id[] (line 751)
- static **sdhci_s3c_ops_s3c6410** : const struct sdhci_ops (line 417)
- static **sdhci_s3c_pmops** : const struct dev_pm_ops (line 731)

## Macros (56)

- **MAX_BUS_CLK** (line 29)
- **S3C64XX_SDHCI_CONTROL4** (line 33)
- **S3C64XX_SDHCI_CONTROL4_BUSY** (line 99)
- **S3C64XX_SDHCI_CONTROL4_DRIVE_2mA** (line 94)
- **S3C64XX_SDHCI_CONTROL4_DRIVE_4mA** (line 95)
- **S3C64XX_SDHCI_CONTROL4_DRIVE_7mA** (line 96)
- **S3C64XX_SDHCI_CONTROL4_DRIVE_9mA** (line 97)
- **S3C64XX_SDHCI_CONTROL4_DRIVE_MASK** (line 92)
- **S3C64XX_SDHCI_CONTROL4_DRIVE_SHIFT** (line 93)
- **S3C64XX_SDHCI_CTRL2_ENCMDCNFMSK** (line 36)
- **S3C64XX_SDHCI_CTRL2_ENSTAASYNCCLR** (line 35)
- **S3C_SDHCI_CONTROL2** (line 31)
- **S3C_SDHCI_CONTROL3** (line 32)
- **S3C_SDHCI_CTRL2_CDINVRXD3** (line 37)
- **S3C_SDHCI_CTRL2_DFCNT_16SDCLK** (line 58)
- **S3C_SDHCI_CTRL2_DFCNT_4SDCLK** (line 57)
- **S3C_SDHCI_CTRL2_DFCNT_64SDCLK** (line 59)
- **S3C_SDHCI_CTRL2_DFCNT_MASK** (line 54)
- **S3C_SDHCI_CTRL2_DFCNT_NONE** (line 56)
- **S3C_SDHCI_CTRL2_DFCNT_SHIFT** (line 55)
- **S3C_SDHCI_CTRL2_DISBUFRD** (line 63)
- **S3C_SDHCI_CTRL2_ENBUSYCHKTXSTART** (line 52)
- **S3C_SDHCI_CTRL2_ENCLKOUTHOLD** (line 61)
- **S3C_SDHCI_CTRL2_ENCLKOUTMSKCON** (line 68)
- **S3C_SDHCI_CTRL2_ENFBCLKRX** (line 49)
- **S3C_SDHCI_CTRL2_ENFBCLKTX** (line 48)
- **S3C_SDHCI_CTRL2_FLTCLKSEL**(_x) (line 42)
- **S3C_SDHCI_CTRL2_FLTCLKSEL_MASK** (line 40)
- **S3C_SDHCI_CTRL2_FLTCLKSEL_SHIFT** (line 41)
- **S3C_SDHCI_CTRL2_HWINITFIN** (line 69)
- **S3C_SDHCI_CTRL2_LVLDAT**(_x) (line 46)
- **S3C_SDHCI_CTRL2_LVLDAT_MASK** (line 44)
- **S3C_SDHCI_CTRL2_LVLDAT_SHIFT** (line 45)
- **S3C_SDHCI_CTRL2_PWRSYNC** (line 67)
- **S3C_SDHCI_CTRL2_RWAITMODE** (line 62)
- **S3C_SDHCI_CTRL2_SDCDSEL** (line 50)
- **S3C_SDHCI_CTRL2_SDSIGPC** (line 51)
- **S3C_SDHCI_CTRL2_SELBASECLK_MASK** (line 65)
- **S3C_SDHCI_CTRL2_SELBASECLK_SHIFT** (line 66)
- **S3C_SDHCI_CTRL2_SLCARDOUT** (line 38)
- **S3C_SDHCI_CTRL3_FCSEL0** (line 74)
- **S3C_SDHCI_CTRL3_FCSEL1** (line 73)
- **S3C_SDHCI_CTRL3_FCSEL2** (line 72)
- **S3C_SDHCI_CTRL3_FCSEL3** (line 71)
- **S3C_SDHCI_CTRL3_FIA0**(_x) (line 90)
- **S3C_SDHCI_CTRL3_FIA0_MASK** (line 88)
- **S3C_SDHCI_CTRL3_FIA0_SHIFT** (line 89)
- **S3C_SDHCI_CTRL3_FIA1**(_x) (line 86)
- **S3C_SDHCI_CTRL3_FIA1_MASK** (line 84)
- **S3C_SDHCI_CTRL3_FIA1_SHIFT** (line 85)
- **S3C_SDHCI_CTRL3_FIA2**(_x) (line 82)
- **S3C_SDHCI_CTRL3_FIA2_MASK** (line 80)
- **S3C_SDHCI_CTRL3_FIA2_SHIFT** (line 81)
- **S3C_SDHCI_CTRL3_FIA3**(_x) (line 78)
- **S3C_SDHCI_CTRL3_FIA3_MASK** (line 76)
- **S3C_SDHCI_CTRL3_FIA3_SHIFT** (line 77)
