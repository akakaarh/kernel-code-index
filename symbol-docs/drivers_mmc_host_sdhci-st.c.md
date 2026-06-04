# drivers/mmc/host/sdhci-st.c

Subsystem: drivers/mmc

## Functions (11)

### sdhci_st_probe
- Return type: static int
- Signature: sdhci_st_probe(struct platform_device * pdev)
- Line: 342

### sdhci_st_readl
- Return type: static u32
- Signature: sdhci_st_readl(struct sdhci_host * host,int reg)
- Line: 307

### sdhci_st_remove
- Return type: static void
- Signature: sdhci_st_remove(struct platform_device * pdev)
- Line: 432

### sdhci_st_resume
- Return type: static int
- Signature: sdhci_st_resume(struct device * dev)
- Line: 470

### sdhci_st_set_dll_for_clock
- Return type: static int
- Signature: sdhci_st_set_dll_for_clock(struct sdhci_host * host)
- Line: 242

### sdhci_st_set_uhs_signaling
- Return type: static void
- Signature: sdhci_st_set_uhs_signaling(struct sdhci_host * host,unsigned int uhs)
- Line: 256

### sdhci_st_suspend
- Return type: static int
- Signature: sdhci_st_suspend(struct device * dev)
- Line: 448

### st_mmcss_cconfig
- Return type: static void
- Signature: st_mmcss_cconfig(struct device_node * np,struct sdhci_host * host)
- Line: 142

### st_mmcss_lock_dll
- Return type: static int
- Signature: st_mmcss_lock_dll(void __iomem * ioaddr)
- Line: 224

### st_mmcss_set_dll
- Return type: static void
- Signature: st_mmcss_set_dll(void __iomem * ioaddr)
- Line: 214

### st_mmcss_set_static_delay
- Return type: static void
- Signature: st_mmcss_set_static_delay(void __iomem * ioaddr)
- Line: 123

## Structs (1)

### st_mmc_platform_data
- Line: 20
- Members:
  - rstc: reset_control *
  - icnclk: clk *
  - top_ioaddr: void __iomem *

## Variables (4)

- static **sdhci_st_driver** : platform_driver (line 504)
- static **sdhci_st_ops** : const struct sdhci_ops (line 323)
- static **sdhci_st_pdata** : const struct sdhci_pltfm_data (line 332)
- static **st_sdhci_match** : const struct of_device_id[] (line 497)

## Macros (59)

- **BASE_CLK_FREQ_100** (line 46)
- **BASE_CLK_FREQ_200** (line 45)
- **BASE_CLK_FREQ_50** (line 47)
- **CLK_TO_CHECK_DLL_LOCK** (line 121)
- **MAX_BLK_LEN_1024** (line 43)
- **MAX_BLK_LEN_2048** (line 44)
- **RETUNING_TIMER_CNT_MAX** (line 79)
- **ST_MMC_CCONFIG_1P8_VOLT** (line 57)
- **ST_MMC_CCONFIG_1_DEFAULT** (line 33)
- **ST_MMC_CCONFIG_2_DEFAULT** (line 48)
- **ST_MMC_CCONFIG_3P0_VOLT** (line 58)
- **ST_MMC_CCONFIG_3P3_VOLT** (line 59)
- **ST_MMC_CCONFIG_3_DEFAULT** (line 62)
- **ST_MMC_CCONFIG_4_DEFAULT** (line 75)
- **ST_MMC_CCONFIG_5_DEFAULT** (line 80)
- **ST_MMC_CCONFIG_64BIT** (line 55)
- **ST_MMC_CCONFIG_8BIT** (line 41)
- **ST_MMC_CCONFIG_ADMA2** (line 40)
- **ST_MMC_CCONFIG_ASYNCH_INTR_SUPPORT** (line 56)
- **ST_MMC_CCONFIG_ASYNC_WAKEUP** (line 32)
- **ST_MMC_CCONFIG_A_DRIVER** (line 71)
- **ST_MMC_CCONFIG_C_DRIVER** (line 70)
- **ST_MMC_CCONFIG_DDR50** (line 72)
- **ST_MMC_CCONFIG_D_DRIVER** (line 69)
- **ST_MMC_CCONFIG_EMMC_SLOT_TYPE** (line 54)
- **ST_MMC_CCONFIG_HIGH_SPEED** (line 39)
- **ST_MMC_CCONFIG_MAX_BLK_LEN** (line 42)
- **ST_MMC_CCONFIG_REG_1** (line 28)
- **ST_MMC_CCONFIG_REG_2** (line 38)
- **ST_MMC_CCONFIG_REG_3** (line 53)
- **ST_MMC_CCONFIG_REG_4** (line 68)
- **ST_MMC_CCONFIG_REG_5** (line 77)
- **ST_MMC_CCONFIG_SDMA** (line 61)
- **ST_MMC_CCONFIG_SDR104** (line 73)
- **ST_MMC_CCONFIG_SDR50** (line 74)
- **ST_MMC_CCONFIG_SUSP_RES_SUPPORT** (line 60)
- **ST_MMC_CCONFIG_TIMEOUT_CLK_FREQ** (line 30)
- **ST_MMC_CCONFIG_TIMEOUT_CLK_UNIT** (line 29)
- **ST_MMC_CCONFIG_TUNING_COUNT_DEFAULT** (line 31)
- **ST_MMC_CCONFIG_TUNING_FOR_SDR50** (line 78)
- **ST_MMC_GP_OUTPUT** (line 83)
- **ST_MMC_GP_OUTPUT_CD** (line 84)
- **ST_MMC_STATUS_R** (line 86)
- **ST_TOP_MMC_DLY_CTRL** (line 94)
- **ST_TOP_MMC_DLY_CTRL_ATUNE_NOT_CFG_DLY** (line 99)
- **ST_TOP_MMC_DLY_CTRL_DLL_BYPASS_CMD** (line 95)
- **ST_TOP_MMC_DLY_CTRL_DLL_BYPASS_PH_SEL** (line 96)
- **ST_TOP_MMC_DLY_CTRL_RX_DLL_ENABLE** (line 98)
- **ST_TOP_MMC_DLY_CTRL_TX_DLL_ENABLE** (line 97)
- **ST_TOP_MMC_DLY_FIX_OFF**(x) (line 88)
- **ST_TOP_MMC_DLY_MAX** (line 110)
- **ST_TOP_MMC_DYN_DLY_CONF** (line 112)
- **ST_TOP_MMC_RX_CLK_DLY** (line 92)
- **ST_TOP_MMC_RX_CMD_STEP_DLY** (line 105)
- **ST_TOP_MMC_RX_DLL_STEP_DLY** (line 104)
- **ST_TOP_MMC_START_DLL_LOCK** (line 100)
- **ST_TOP_MMC_TX_CLK_DLY** (line 91)
- **ST_TOP_MMC_TX_DLL_STEP_DLY** (line 103)
- **ST_TOP_MMC_TX_DLL_STEP_DLY_VALID** (line 108)
