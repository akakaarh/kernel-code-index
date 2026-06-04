# drivers/mmc/host/sdhci_am654.c

Subsystem: drivers/mmc

## Functions (24)

### sdhci_am654_calculate_itap
- Return type: static int
- Signature: sdhci_am654_calculate_itap(struct sdhci_host * host,struct window * fail_window,u8 num_fails,bool circular_buffer)
- Line: 473

### sdhci_am654_cqe_add_host
- Return type: static int
- Signature: sdhci_am654_cqe_add_host(struct sdhci_host * host)
- Line: 706

### sdhci_am654_cqhci_irq
- Return type: static u32
- Signature: sdhci_am654_cqhci_irq(struct sdhci_host * host,u32 intmask)
- Line: 457

### sdhci_am654_do_tuning
- Return type: static int
- Signature: sdhci_am654_do_tuning(struct sdhci_host * host,u32 opcode)
- Line: 528

### sdhci_am654_dumpregs
- Return type: static void
- Signature: sdhci_am654_dumpregs(struct mmc_host * mmc)
- Line: 695

### sdhci_am654_execute_tuning
- Return type: static int
- Signature: sdhci_am654_execute_tuning(struct mmc_host * mmc,u32 opcode)
- Line: 441

### sdhci_am654_get_of_property
- Return type: static int
- Signature: sdhci_am654_get_of_property(struct platform_device * pdev,struct sdhci_am654_data * sdhci_am654)
- Line: 841

### sdhci_am654_get_otap_delay
- Return type: static int
- Signature: sdhci_am654_get_otap_delay(struct sdhci_host * host,struct sdhci_am654_data * sdhci_am654)
- Line: 725

### sdhci_am654_init
- Return type: static int
- Signature: sdhci_am654_init(struct sdhci_host * host)
- Line: 764

### sdhci_am654_platform_execute_tuning
- Return type: static int
- Signature: sdhci_am654_platform_execute_tuning(struct sdhci_host * host,u32 opcode)
- Line: 572

### sdhci_am654_probe
- Return type: static int
- Signature: sdhci_am654_probe(struct platform_device * pdev)
- Line: 928

### sdhci_am654_remove
- Return type: static void
- Signature: sdhci_am654_remove(struct platform_device * pdev)
- Line: 1021

### sdhci_am654_reset
- Return type: static void
- Signature: sdhci_am654_reset(struct sdhci_host * host,u8 mask)
- Line: 426

### sdhci_am654_restore
- Return type: static int
- Signature: sdhci_am654_restore(struct sdhci_host * host)
- Line: 1038

### sdhci_am654_runtime_resume
- Return type: static int
- Signature: sdhci_am654_runtime_resume(struct device * dev)
- Line: 1102

### sdhci_am654_runtime_suspend
- Return type: static int
- Signature: sdhci_am654_runtime_suspend(struct device * dev)
- Line: 1082

### sdhci_am654_set_clock
- Return type: static void
- Signature: sdhci_am654_set_clock(struct sdhci_host * host,unsigned int clock)
- Line: 274

### sdhci_am654_setup_delay_chain
- Return type: static void
- Signature: sdhci_am654_setup_delay_chain(struct sdhci_am654_data * sdhci_am654,unsigned char timing)
- Line: 259

### sdhci_am654_setup_dll
- Return type: static void
- Signature: sdhci_am654_setup_dll(struct sdhci_host * host,unsigned int clock)
- Line: 178

### sdhci_am654_start_signal_voltage_switch
- Return type: static int
- Signature: sdhci_am654_start_signal_voltage_switch(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 361

### sdhci_am654_write_b
- Return type: static void
- Signature: sdhci_am654_write_b(struct sdhci_host * host,u8 val,int reg)
- Line: 392

### sdhci_am654_write_itapdly
- Return type: static void
- Signature: sdhci_am654_write_itapdly(struct sdhci_am654_data * sdhci_am654,u32 itapdly,u32 enable)
- Line: 246

### sdhci_am654_write_power_on
- Return type: static u8
- Signature: sdhci_am654_write_power_on(struct sdhci_host * host,u8 val,int reg)
- Line: 384

### sdhci_j721e_4bit_set_clock
- Return type: static void
- Signature: sdhci_j721e_4bit_set_clock(struct sdhci_host * host,unsigned int clock)
- Line: 325

## Structs (4)

### sdhci_am654_data
- Line: 142
- Members:
  - otap_binding: const char *
  - itap_binding: const char *
  - capability: u32
  - base: regmap *
  - otap_del_sel: u32[]
  - itap_del_sel: u32[]
  - itap_del_ena: u32[]
  - clkbuf_sel: int
  - trm_icp: int
  - drv_strength: int
  - strb_sel: int
  - flags: u32
  - quirks: u32
  - dll_enable: bool
  - tuning_loop: u32
  - start: u8
  - end: u8
  - length: u8
  - pdata: const struct sdhci_pltfm_data *
  - flags: u32
  - quirks: u32

### sdhci_am654_driver_data
- Line: 167
- Members:
  - otap_binding: const char *
  - itap_binding: const char *
  - capability: u32
  - base: regmap *
  - otap_del_sel: u32[]
  - itap_del_sel: u32[]
  - itap_del_ena: u32[]
  - clkbuf_sel: int
  - trm_icp: int
  - drv_strength: int
  - strb_sel: int
  - flags: u32
  - quirks: u32
  - dll_enable: bool
  - tuning_loop: u32
  - start: u8
  - end: u8
  - length: u8
  - pdata: const struct sdhci_pltfm_data *
  - flags: u32
  - quirks: u32

### timing_data
- Line: 100
- Members:
  - otap_binding: const char *
  - itap_binding: const char *
  - capability: u32
  - base: regmap *
  - otap_del_sel: u32[]
  - itap_del_sel: u32[]
  - itap_del_ena: u32[]
  - clkbuf_sel: int
  - trm_icp: int
  - drv_strength: int
  - strb_sel: int
  - flags: u32
  - quirks: u32
  - dll_enable: bool
  - tuning_loop: u32
  - start: u8
  - end: u8
  - length: u8
  - pdata: const struct sdhci_pltfm_data *
  - flags: u32
  - quirks: u32

### window
- Line: 161
- Members:
  - otap_binding: const char *
  - itap_binding: const char *
  - capability: u32
  - base: regmap *
  - otap_del_sel: u32[]
  - itap_del_sel: u32[]
  - itap_del_ena: u32[]
  - clkbuf_sel: int
  - trm_icp: int
  - drv_strength: int
  - strb_sel: int
  - flags: u32
  - quirks: u32
  - dll_enable: bool
  - tuning_loop: u32
  - start: u8
  - end: u8
  - length: u8
  - pdata: const struct sdhci_pltfm_data *
  - flags: u32
  - quirks: u32

## Variables (19)

- static **sdhci_am62_4bit_drvdata** : const struct sdhci_am654_driver_data (line 681)
- static **sdhci_am654_cqhci_ops** : const struct cqhci_host_ops (line 700)
- static **sdhci_am654_descope_hs400** : const struct soc_device_attribute[] (line 893)
- static **sdhci_am654_dev_pm_ops** : const struct dev_pm_ops (line 1126)
- static **sdhci_am654_devices** : const struct soc_device_attribute[] (line 687)
- static **sdhci_am654_driver** : platform_driver (line 1131)
- static **sdhci_am654_drvdata** : const struct sdhci_am654_driver_data (line 626)
- static **sdhci_am654_of_match** : const struct of_device_id[] (line 899)
- static **sdhci_am654_ops** : const struct sdhci_ops (line 600)
- static **sdhci_am654_pdata** : const struct sdhci_pltfm_data (line 613)
- static **sdhci_am654_regmap_config** : const struct regmap_config (line 94)
- static **sdhci_am654_sr1_drvdata** : const struct sdhci_am654_driver_data (line 620)
- static **sdhci_j721e_4bit_drvdata** : const struct sdhci_am654_driver_data (line 676)
- static **sdhci_j721e_4bit_ops** : const struct sdhci_ops (line 656)
- static **sdhci_j721e_4bit_pdata** : const struct sdhci_pltfm_data (line 669)
- static **sdhci_j721e_8bit_drvdata** : const struct sdhci_am654_driver_data (line 651)
- static **sdhci_j721e_8bit_ops** : const struct sdhci_ops (line 631)
- static **sdhci_j721e_8bit_pdata** : const struct sdhci_pltfm_data (line 644)
- static **td** : const struct timing_data[] (line 106)

## Macros (74)

- **CALDONE_MASK** (line 67)
- **CALDONE_SHIFT** (line 66)
- **CLKBUFSEL_MASK** (line 55)
- **CLKBUFSEL_SHIFT** (line 54)
- **CLOCK_TOO_SLOW_HZ** (line 87)
- **CTL_CFG_2** (line 22)
- **CTL_CFG_3** (line 23)
- **DLLRDY_MASK** (line 63)
- **DLLRDY_SHIFT** (line 62)
- **DLL_CALIB** (line 175)
- **DLL_PRESENT** (line 174)
- **DLL_TRIM_ICP_MASK** (line 57)
- **DLL_TRIM_ICP_SHIFT** (line 56)
- **DRIVER_STRENGTH_100_OHM** (line 84)
- **DRIVER_STRENGTH_33_OHM** (line 82)
- **DRIVER_STRENGTH_40_OHM** (line 85)
- **DRIVER_STRENGTH_50_OHM** (line 81)
- **DRIVER_STRENGTH_66_OHM** (line 83)
- **DR_TY_MASK** (line 59)
- **DR_TY_SHIFT** (line 58)
- **ENDLL_MASK** (line 61)
- **ENDLL_SHIFT** (line 60)
- **FREQSEL_2_BIT** (line 172)
- **FREQSEL_MASK** (line 53)
- **FREQSEL_SHIFT** (line 52)
- **IOMUX_ENABLE_MASK** (line 40)
- **IOMUX_ENABLE_SHIFT** (line 39)
- **IOMUX_PRESENT** (line 171)
- **ITAPCHGWIN_MASK** (line 79)
- **ITAPCHGWIN_SHIFT** (line 78)
- **ITAPDLYENA_MASK** (line 77)
- **ITAPDLYENA_SHIFT** (line 76)
- **ITAPDLYSEL_MASK** (line 75)
- **ITAPDLYSEL_SHIFT** (line 74)
- **ITAPDLY_LAST_INDEX** (line 471)
- **ITAPDLY_LENGTH** (line 470)
- **MAX_POWER_ON_TIMEOUT** (line 391)
- **OTAPDLYENA_MASK** (line 42)
- **OTAPDLYENA_SHIFT** (line 41)
- **OTAPDLYSEL_MASK** (line 44)
- **OTAPDLYSEL_SHIFT** (line 43)
- **PDB_MASK** (line 65)
- **PDB_SHIFT** (line 64)
- **PHY_CTRL1** (line 30)
- **PHY_CTRL2** (line 31)
- **PHY_CTRL3** (line 32)
- **PHY_CTRL4** (line 33)
- **PHY_CTRL5** (line 34)
- **PHY_CTRL6** (line 35)
- **PHY_STAT1** (line 36)
- **PHY_STAT2** (line 37)
- **RETRIM_MASK** (line 69)
- **RETRIM_SHIFT** (line 68)
- **RETRY_TUNING_MAX** (line 89)
- **SDHCI_AM654_AUTOSUSPEND_DELAY** (line 88)
- **SDHCI_AM654_CQE_BASE_ADDR** (line 92)
- **SDHCI_AM654_QUIRK_DISABLE_HS400** (line 158)
- **SDHCI_AM654_QUIRK_FORCE_CDTEST** (line 156)
- **SDHCI_AM654_QUIRK_SUPPRESS_V1P8_ENA** (line 157)
- **SEL100_MASK** (line 51)
- **SEL100_SHIFT** (line 50)
- **SEL50_MASK** (line 49)
- **SEL50_SHIFT** (line 48)
- **SELDLYRXCLK_MASK** (line 73)
- **SELDLYRXCLK_SHIFT** (line 72)
- **SELDLYTXCLK_MASK** (line 71)
- **SELDLYTXCLK_SHIFT** (line 70)
- **SLOTTYPE_EMBEDDED** (line 26)
- **SLOTTYPE_MASK** (line 25)
- **STRBSEL_4BIT_MASK** (line 46)
- **STRBSEL_4_BIT** (line 173)
- **STRBSEL_8BIT_MASK** (line 47)
- **STRBSEL_SHIFT** (line 45)
- **TUNINGFORSDR50_MASK** (line 27)
