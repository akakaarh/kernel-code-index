# drivers/mmc/host/sdhci-pxav3.c

Subsystem: drivers/mmc

## Functions (16)

### armada_38x_quirks
- Return type: static int
- Signature: armada_38x_quirks(struct platform_device * pdev,struct sdhci_host * host)
- Line: 123

### mv_conf_mbus_windows
- Return type: static int
- Signature: mv_conf_mbus_windows(struct platform_device * pdev,const struct mbus_dram_target_info * dram)
- Line: 77

### pxav3_gen_init_74_clocks
- Return type: static void
- Signature: pxav3_gen_init_74_clocks(struct sdhci_host * host,u8 power_mode)
- Line: 194

### pxav3_get_mmc_pdata
- Return type: static sdhci_pxa_platdata *
- Signature: pxav3_get_mmc_pdata(struct device * dev)
- Line: 380

### pxav3_get_mmc_pdata
- Return type: static sdhci_pxa_platdata *
- Signature: pxav3_get_mmc_pdata(struct device * dev)
- Line: 363

### pxav3_lookup_pinstate
- Return type: static pinctrl_state *
- Signature: pxav3_lookup_pinstate(struct device * dev,struct pinctrl * pinctrl,const char * name)
- Line: 386

### pxav3_reset
- Return type: static void
- Signature: pxav3_reset(struct sdhci_host * host,u8 mask)
- Line: 169

### pxav3_set_clock
- Return type: static void
- Signature: pxav3_set_clock(struct sdhci_host * host,unsigned int clock)
- Line: 321

### pxav3_set_power
- Return type: static void
- Signature: pxav3_set_power(struct sdhci_host * host,unsigned char mode,unsigned short vdd)
- Line: 303

### pxav3_set_uhs_signaling
- Return type: static void
- Signature: pxav3_set_uhs_signaling(struct sdhci_host * host,unsigned int uhs)
- Line: 243

### sdhci_pxav3_probe
- Return type: static int
- Signature: sdhci_pxav3_probe(struct platform_device * pdev)
- Line: 399

### sdhci_pxav3_remove
- Return type: static void
- Signature: sdhci_pxav3_remove(struct platform_device * pdev)
- Line: 510

### sdhci_pxav3_resume
- Return type: static int
- Signature: sdhci_pxav3_resume(struct device * dev)
- Line: 540

### sdhci_pxav3_runtime_resume
- Return type: static int
- Signature: sdhci_pxav3_runtime_resume(struct device * dev)
- Line: 570

### sdhci_pxav3_runtime_suspend
- Return type: static int
- Signature: sdhci_pxav3_runtime_suspend(struct device * dev)
- Line: 552

### sdhci_pxav3_suspend
- Return type: static int
- Signature: sdhci_pxav3_suspend(struct device * dev)
- Line: 526

## Structs (1)

### sdhci_pxa
- Line: 51
- Members:
  - clk_core: clk *
  - clk_io: clk *
  - power_mode: u8
  - sdio3_conf_reg: void __iomem *
  - pinctrl: pinctrl *
  - pins_default: pinctrl_state *
  - pins_uhs: pinctrl_state *

## Variables (5)

- static **pxav3_sdhci_ops** : const struct sdhci_ops (line 333)
- static **sdhci_pxav3_driver** : platform_driver (line 589)
- static **sdhci_pxav3_of_match** : const struct of_device_id[] (line 352)
- static **sdhci_pxav3_pdata** : const struct sdhci_pltfm_data (line 343)
- static **sdhci_pxav3_pmops** : const struct dev_pm_ops (line 584)

## Macros (20)

- **MAX_WAIT_COUNT** (line 193)
- **PXAV3_RPM_DELAY_MS** (line 32)
- **SDCE_MISC_INT** (line 48)
- **SDCE_MISC_INT_EN** (line 49)
- **SDCFG_GEN_PAD_CLK_CNT_MASK** (line 41)
- **SDCFG_GEN_PAD_CLK_CNT_SHIFT** (line 42)
- **SDCFG_GEN_PAD_CLK_ON** (line 40)
- **SDCLK_DELAY_MASK** (line 37)
- **SDCLK_DELAY_SHIFT** (line 36)
- **SDCLK_SEL** (line 35)
- **SDHCI_MAX_WIN_NUM** (line 67)
- **SDHCI_WINDOW_BASE**(i) (line 66)
- **SDHCI_WINDOW_CTRL**(i) (line 65)
- **SDIO3_CONF_CLK_INV** (line 74)
- **SDIO3_CONF_SD_FB_CLK** (line 75)
- **SD_CE_ATA_1** (line 45)
- **SD_CE_ATA_2** (line 47)
- **SD_CFG_FIFO_PARAM** (line 39)
- **SD_CLOCK_BURST_SIZE_SETUP** (line 34)
- **SD_SPI_MODE** (line 44)
