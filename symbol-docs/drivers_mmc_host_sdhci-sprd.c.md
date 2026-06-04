# drivers/mmc/host/sdhci-sprd.c

Subsystem: drivers/mmc

## Functions (36)

### _sdhci_sprd_set_clock
- Return type: static void
- Signature: _sdhci_sprd_set_clock(struct sdhci_host * host,unsigned int clk)
- Line: 229

### mmc_send_tuning_cmd
- Return type: static int
- Signature: mmc_send_tuning_cmd(struct mmc_card * card)
- Line: 571

### mmc_send_tuning_data
- Return type: static int
- Signature: mmc_send_tuning_data(struct mmc_card * card)
- Line: 576

### sdhci_sprd_calc_div
- Return type: static u32
- Signature: sdhci_sprd_calc_div(u32 base_clk,u32 clk)
- Line: 205

### sdhci_sprd_check_auto_cmd23
- Return type: static void
- Signature: sdhci_sprd_check_auto_cmd23(struct mmc_host * mmc,struct mmc_request * mrq)
- Line: 460

### sdhci_sprd_enable_phy_dll
- Return type: static void
- Signature: sdhci_sprd_enable_phy_dll(struct sdhci_host * host)
- Line: 257

### sdhci_sprd_execute_sd_hs_data_tuning
- Return type: static int
- Signature: sdhci_sprd_execute_sd_hs_data_tuning(struct mmc_host * mmc,struct mmc_card * card)
- Line: 699

### sdhci_sprd_get_best_clk_sample
- Return type: static int
- Signature: sdhci_sprd_get_best_clk_sample(struct mmc_host * mmc,u8 * value)
- Line: 592

### sdhci_sprd_get_max_clock
- Return type: static unsigned int
- Signature: sdhci_sprd_get_max_clock(struct sdhci_host * host)
- Line: 319

### sdhci_sprd_get_max_timeout_count
- Return type: static unsigned int
- Signature: sdhci_sprd_get_max_timeout_count(struct sdhci_host * host)
- Line: 401

### sdhci_sprd_get_min_clock
- Return type: static unsigned int
- Signature: sdhci_sprd_get_min_clock(struct sdhci_host * host)
- Line: 326

### sdhci_sprd_get_ro
- Return type: static unsigned int
- Signature: sdhci_sprd_get_ro(struct sdhci_host * host)
- Line: 407

### sdhci_sprd_hs400_enhanced_strobe
- Return type: static void
- Signature: sdhci_sprd_hs400_enhanced_strobe(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 545

### sdhci_sprd_hw_reset
- Return type: static void
- Signature: sdhci_sprd_hw_reset(struct sdhci_host * host)
- Line: 380

### sdhci_sprd_init_config
- Return type: static void
- Signature: sdhci_sprd_init_config(struct sdhci_host * host)
- Line: 118

### sdhci_sprd_phy_param_parse
- Return type: static void
- Signature: sdhci_sprd_phy_param_parse(struct sdhci_sprd_host * sprd_host,struct device_node * np)
- Line: 704

### sdhci_sprd_prepare_sd_hs_cmd_tuning
- Return type: static int
- Signature: sdhci_sprd_prepare_sd_hs_cmd_tuning(struct mmc_host * mmc,struct mmc_card * card)
- Line: 694

### sdhci_sprd_probe
- Return type: static int
- Signature: sdhci_sprd_probe(struct platform_device * pdev)
- Line: 731

### sdhci_sprd_readl
- Return type: static u32
- Signature: sdhci_sprd_readl(struct sdhci_host * host,int reg)
- Line: 128

### sdhci_sprd_remove
- Return type: static void
- Signature: sdhci_sprd_remove(struct platform_device * pdev)
- Line: 888

### sdhci_sprd_request
- Return type: static void
- Signature: sdhci_sprd_request(struct mmc_host * mmc,struct mmc_request * mrq)
- Line: 479

### sdhci_sprd_request_atomic
- Return type: static int
- Signature: sdhci_sprd_request_atomic(struct mmc_host * mmc,struct mmc_request * mrq)
- Line: 486

### sdhci_sprd_request_done
- Return type: static void
- Signature: sdhci_sprd_request_done(struct sdhci_host * host,struct mmc_request * mrq)
- Line: 412

### sdhci_sprd_runtime_resume
- Return type: static int
- Signature: sdhci_sprd_runtime_resume(struct device * dev)
- Line: 921

### sdhci_sprd_runtime_suspend
- Return type: static int
- Signature: sdhci_sprd_runtime_suspend(struct device * dev)
- Line: 906

### sdhci_sprd_sd_clk_off
- Return type: static void
- Signature: sdhci_sprd_sd_clk_off(struct sdhci_host * host)
- Line: 175

### sdhci_sprd_sd_clk_on
- Return type: static void
- Signature: sdhci_sprd_sd_clk_on(struct sdhci_host * host)
- Line: 183

### sdhci_sprd_set_clock
- Return type: static void
- Signature: sdhci_sprd_set_clock(struct sdhci_host * host,unsigned int clock)
- Line: 290

### sdhci_sprd_set_dll_invert
- Return type: static void
- Signature: sdhci_sprd_set_dll_invert(struct sdhci_host * host,u32 mask,bool en)
- Line: 193

### sdhci_sprd_set_power
- Return type: static void
- Signature: sdhci_sprd_set_power(struct sdhci_host * host,unsigned char mode,unsigned short vdd)
- Line: 422

### sdhci_sprd_set_uhs_signaling
- Return type: static void
- Signature: sdhci_sprd_set_uhs_signaling(struct sdhci_host * host,unsigned int timing)
- Line: 331

### sdhci_sprd_tuning
- Return type: static int
- Signature: sdhci_sprd_tuning(struct mmc_host * mmc,struct mmc_card * card,enum sdhci_sprd_tuning_type type)
- Line: 627

### sdhci_sprd_voltage_switch
- Return type: static int
- Signature: sdhci_sprd_voltage_switch(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 494

### sdhci_sprd_writeb
- Return type: static void
- Signature: sdhci_sprd_writeb(struct sdhci_host * host,u8 val,int reg)
- Line: 157

### sdhci_sprd_writel
- Return type: static void
- Signature: sdhci_sprd_writel(struct sdhci_host * host,u32 val,int reg)
- Line: 136

### sdhci_sprd_writew
- Return type: static void
- Signature: sdhci_sprd_writew(struct sdhci_host * host,u16 val,int reg)
- Line: 148

## Structs (2)

### sdhci_sprd_host
- Line: 81
- Members:
  - version: u32
  - clk_sdio: clk *
  - clk_enable: clk *
  - clk_2x_enable: clk *
  - pinctrl: pinctrl *
  - pins_uhs: pinctrl_state *
  - pins_default: pinctrl_state *
  - base_rate: u32
  - flags: int
  - phy_delay: u32[]
  - property: const char *
  - timing: u8

### sdhci_sprd_phy_cfg
- Line: 99
- Members:
  - version: u32
  - clk_sdio: clk *
  - clk_enable: clk *
  - clk_2x_enable: clk *
  - pinctrl: pinctrl *
  - pins_uhs: pinctrl_state *
  - pins_default: pinctrl_state *
  - base_rate: u32
  - flags: int
  - phy_delay: u32[]
  - property: const char *
  - timing: u8

## Enums (1)

### sdhci_sprd_tuning_type
- Line: 94

## Variables (6)

- static **sdhci_sprd_driver** : platform_driver (line 958)
- static **sdhci_sprd_of_match** : const struct of_device_id[] (line 900)
- static **sdhci_sprd_ops** : const struct sdhci_ops (line 442)
- static **sdhci_sprd_pdata** : const struct sdhci_pltfm_data (line 722)
- static **sdhci_sprd_phy_cfgs** : const struct sdhci_sprd_phy_cfg[] (line 104)
- static **sdhci_sprd_pm_ops** : const struct dev_pm_ops (line 953)

## Macros (35)

- **SDHCIBSPRD_IT_WR_DLY_INV** (line 38)
- **SDHCI_HW_RESET_CARD** (line 68)
- **SDHCI_SPRD_ARG2_STUFF** (line 26)
- **SDHCI_SPRD_BIT_CMD_DLY_INV** (line 39)
- **SDHCI_SPRD_BIT_DLL_BAK** (line 51)
- **SDHCI_SPRD_BIT_DLL_VAL** (line 52)
- **SDHCI_SPRD_BIT_INNR_CLK_AUTO_EN** (line 48)
- **SDHCI_SPRD_BIT_NEGRD_DLY_INV** (line 41)
- **SDHCI_SPRD_BIT_OUTR_CLK_AUTO_EN** (line 47)
- **SDHCI_SPRD_BIT_POSRD_DLY_INV** (line 40)
- **SDHCI_SPRD_CLK_DEF_RATE** (line 73)
- **SDHCI_SPRD_CLK_MAX_DIV** (line 71)
- **SDHCI_SPRD_CMD_DLY_MASK** (line 77)
- **SDHCI_SPRD_CPST_EN** (line 79)
- **SDHCI_SPRD_CTRL_HS200** (line 57)
- **SDHCI_SPRD_CTRL_HS400** (line 58)
- **SDHCI_SPRD_CTRL_HS400ES** (line 59)
- **SDHCI_SPRD_DLL_ALL_CPST_EN** (line 29)
- **SDHCI_SPRD_DLL_EN** (line 30)
- **SDHCI_SPRD_DLL_INIT_COUNT** (line 32)
- **SDHCI_SPRD_DLL_LOCKED** (line 44)
- **SDHCI_SPRD_DLL_PHASE_INTERNAL** (line 33)
- **SDHCI_SPRD_DLL_SEARCH_MODE** (line 31)
- **SDHCI_SPRD_INT_SIGNAL_MASK** (line 54)
- **SDHCI_SPRD_MAX_CUR** (line 70)
- **SDHCI_SPRD_MAX_RANGE** (line 76)
- **SDHCI_SPRD_PHY_DLL_CLK** (line 74)
- **SDHCI_SPRD_POSRD_DLY_MASK** (line 78)
- **SDHCI_SPRD_REG_32_BUSY_POSI** (line 46)
- **SDHCI_SPRD_REG_32_DLL_CFG** (line 28)
- **SDHCI_SPRD_REG_32_DLL_DLY** (line 35)
- **SDHCI_SPRD_REG_32_DLL_DLY_OFFSET** (line 37)
- **SDHCI_SPRD_REG_32_DLL_STS0** (line 43)
- **SDHCI_SPRD_REG_DEBOUNCE** (line 50)
- **TO_SPRD_HOST**(host) (line 116)
