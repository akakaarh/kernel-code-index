# drivers/mmc/host/sdhci-pci-o2micro.c

Subsystem: drivers/mmc

## Functions (20)

### __sdhci_o2_execute_tuning
- Return type: static void
- Signature: __sdhci_o2_execute_tuning(struct sdhci_host * host,u32 opcode)
- Line: 210

### o2_pci_led_enable
- Return type: static void
- Signature: o2_pci_led_enable(struct sdhci_pci_chip * chip)
- Line: 431

### o2_pci_set_baseclk
- Return type: static void
- Signature: o2_pci_set_baseclk(struct sdhci_pci_chip * chip,u32 value)
- Line: 167

### sdhci_o2_dll_recovery
- Return type: static int
- Signature: sdhci_o2_dll_recovery(struct sdhci_host * host)
- Line: 244

### sdhci_o2_enable_clk
- Return type: static void
- Signature: sdhci_o2_enable_clk(struct sdhci_host * host,u16 clk)
- Line: 565

### sdhci_o2_enable_internal_clock
- Return type: static void
- Signature: sdhci_o2_enable_internal_clock(struct sdhci_host * host)
- Line: 109

### sdhci_o2_execute_tuning
- Return type: static int
- Signature: sdhci_o2_execute_tuning(struct mmc_host * mmc,u32 opcode)
- Line: 314

### sdhci_o2_get_cd
- Return type: static int
- Signature: sdhci_o2_get_cd(struct mmc_host * mmc)
- Line: 155

### sdhci_o2_pll_dll_wdt_control
- Return type: static u32
- Signature: sdhci_o2_pll_dll_wdt_control(struct sdhci_host * host)
- Line: 181

### sdhci_o2_set_tuning_mode
- Return type: static void
- Signature: sdhci_o2_set_tuning_mode(struct sdhci_host * host)
- Line: 200

### sdhci_o2_wait_card_detect_stable
- Return type: static void
- Signature: sdhci_o2_wait_card_detect_stable(struct sdhci_host * host)
- Line: 84

### sdhci_o2_wait_dll_detect_lock
- Return type: static int
- Signature: sdhci_o2_wait_dll_detect_lock(struct sdhci_host * host)
- Line: 192

### sdhci_pci_o2_enable_msi
- Return type: static void
- Signature: sdhci_pci_o2_enable_msi(struct sdhci_pci_chip * chip,struct sdhci_host * host)
- Line: 542

### sdhci_pci_o2_fujin2_pci_init
- Return type: static void
- Signature: sdhci_pci_o2_fujin2_pci_init(struct sdhci_pci_chip * chip)
- Line: 456

### sdhci_pci_o2_init_sd_express
- Return type: static int
- Signature: sdhci_pci_o2_init_sd_express(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 635

### sdhci_pci_o2_probe
- Return type: static int
- Signature: sdhci_pci_o2_probe(struct sdhci_pci_chip * chip)
- Line: 810

### sdhci_pci_o2_probe_slot
- Return type: static int
- Signature: sdhci_pci_o2_probe_slot(struct sdhci_pci_slot * slot)
- Line: 725

### sdhci_pci_o2_resume
- Return type: static int
- Signature: sdhci_pci_o2_resume(struct sdhci_pci_chip * chip)
- Line: 1073

### sdhci_pci_o2_set_clock
- Return type: static void
- Signature: sdhci_pci_o2_set_clock(struct sdhci_host * host,unsigned int clock)
- Line: 578

### sdhci_pci_o2_set_power
- Return type: static void
- Signature: sdhci_pci_o2_set_power(struct sdhci_host * host,unsigned char mode,unsigned short vdd)
- Line: 696

## Structs (1)

### o2_host
- Line: 80
- Members:
  - dll_adjust_count: u8

## Variables (3)

- static **dmdn_table** : const u32[] (line 76)
- **sdhci_o2** : const struct sdhci_pci_fixes (line 1089)
- static **sdhci_pci_o2_ops** : const struct sdhci_ops (line 1080)

## Macros (49)

- **DMDN_SZ** (line 78)
- **O2_DLL_LOCK_STATUS** (line 72)
- **O2_PLL_DLL_WDT_CONTROL1** (line 68)
- **O2_PLL_FORCE_ACTIVE** (line 69)
- **O2_PLL_LOCK_STATUS** (line 70)
- **O2_PLL_SOFT_RESET** (line 71)
- **O2_SD_ADMA1** (line 34)
- **O2_SD_ADMA2** (line 35)
- **O2_SD_CAPS** (line 33)
- **O2_SD_CAP_REG0** (line 47)
- **O2_SD_CAP_REG2** (line 46)
- **O2_SD_CLKREQ** (line 32)
- **O2_SD_CLK_SETTING** (line 45)
- **O2_SD_DELAY_CTRL** (line 49)
- **O2_SD_DETECT_SETTING** (line 74)
- **O2_SD_DEV_CTRL** (line 27)
- **O2_SD_EXP_INT_REG** (line 40)
- **O2_SD_FIX_PHASE** (line 62)
- **O2_SD_FREG0_LEDOFF** (line 58)
- **O2_SD_FREG4_ENABLE_CLK_SET** (line 60)
- **O2_SD_FUNC_REG0** (line 30)
- **O2_SD_FUNC_REG3** (line 52)
- **O2_SD_FUNC_REG4** (line 53)
- **O2_SD_GPIO_CTRL_REG1** (line 56)
- **O2_SD_HW_TUNING_DISABLE** (line 66)
- **O2_SD_INF_MOD** (line 37)
- **O2_SD_LD0_CTRL** (line 26)
- **O2_SD_LED_ENABLE** (line 57)
- **O2_SD_LOCK_WP** (line 28)
- **O2_SD_MISC_CTRL** (line 39)
- **O2_SD_MISC_CTRL2** (line 36)
- **O2_SD_MISC_CTRL4** (line 38)
- **O2_SD_MISC_REG5** (line 25)
- **O2_SD_MISC_SETTING** (line 44)
- **O2_SD_MULTI_VCC3V** (line 31)
- **O2_SD_OUTPUT_CLK_SOURCE_SWITCH** (line 50)
- **O2_SD_PARA_SET_REG1** (line 54)
- **O2_SD_PCIE_SWITCH** (line 24)
- **O2_SD_PHASE_MASK** (line 61)
- **O2_SD_PLL_SETTING** (line 43)
- **O2_SD_PWR_FORCE_L0** (line 41)
- **O2_SD_SEL_DLL** (line 59)
- **O2_SD_TEST_REG** (line 29)
- **O2_SD_TUNING_CTRL** (line 42)
- **O2_SD_UHS1_CAP_SETTING** (line 48)
- **O2_SD_UHS2_L1_CTRL** (line 51)
- **O2_SD_VDDX_CTRL_REG** (line 55)
- **O2_SD_VENDOR_SETTING** (line 64)
- **O2_SD_VENDOR_SETTING2** (line 65)
