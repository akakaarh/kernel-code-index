# drivers/mmc/host/sdhci-milbeaut.c

Subsystem: drivers/mmc

## Functions (9)

### sdhci_milbeaut_bridge_init
- Return type: static void
- Signature: sdhci_milbeaut_bridge_init(struct sdhci_host * host,int rate)
- Line: 143

### sdhci_milbeaut_bridge_reset
- Return type: static void
- Signature: sdhci_milbeaut_bridge_reset(struct sdhci_host * host,int reset_flag)
- Line: 134

### sdhci_milbeaut_get_min_clock
- Return type: static unsigned int
- Signature: sdhci_milbeaut_get_min_clock(struct sdhci_host * host)
- Line: 80

### sdhci_milbeaut_init
- Return type: static void
- Signature: sdhci_milbeaut_init(struct sdhci_host * host)
- Line: 210

### sdhci_milbeaut_probe
- Return type: static int
- Signature: sdhci_milbeaut_probe(struct platform_device * pdev)
- Line: 230

### sdhci_milbeaut_remove
- Return type: static void
- Signature: sdhci_milbeaut_remove(struct platform_device * pdev)
- Line: 310

### sdhci_milbeaut_reset
- Return type: static void
- Signature: sdhci_milbeaut_reset(struct sdhci_host * host,u8 mask)
- Line: 85

### sdhci_milbeaut_soft_voltage_switch
- Return type: static void
- Signature: sdhci_milbeaut_soft_voltage_switch(struct sdhci_host * host)
- Line: 60

### sdhci_milbeaut_vendor_init
- Return type: static void
- Signature: sdhci_milbeaut_vendor_init(struct sdhci_host * host)
- Line: 176

## Structs (1)

### f_sdhost_priv
- Line: 53
- Members:
  - clk_iface: clk *
  - clk: clk *
  - rst: reset_control *
  - vendor_hs200: u32
  - dev: device *
  - enable_cmd_dat_delay: bool
  - clk_iface: clk *
  - clk: clk *
  - dev: device *
  - enable_cmd_dat_delay: bool

## Variables (3)

- static **mlb_dt_ids** : const struct of_device_id[] (line 202)
- static **sdhci_milbeaut_driver** : platform_driver (line 324)
- static **sdhci_milbeaut_ops** : const struct sdhci_ops (line 124)

## Macros (24)

- **MLB_BCLKFREQ_MAX** (line 47)
- **MLB_BCLKFREQ_MIN** (line 48)
- **MLB_CAL_BCLKFREQ**(rate) (line 46)
- **MLB_CAL_TOCLKFREQ_KHZ**(rate) (line 41)
- **MLB_CAL_TOCLKFREQ_MHZ**(rate) (line 40)
- **MLB_CDR_SET** (line 50)
- **MLB_CDR_SET_CLK2POW16** (line 51)
- **MLB_CR_SET** (line 29)
- **MLB_CR_SET_CR_BCLKFREQ_MASK** (line 34)
- **MLB_CR_SET_CR_BCLKFREQ_SFT** (line 33)
- **MLB_CR_SET_CR_RTUNTIMER_MASK** (line 36)
- **MLB_CR_SET_CR_RTUNTIMER_SFT** (line 35)
- **MLB_CR_SET_CR_TOCLKFREQ_MASK** (line 32)
- **MLB_CR_SET_CR_TOCLKFREQ_SFT** (line 31)
- **MLB_CR_SET_CR_TOCLKUNIT** (line 30)
- **MLB_SD_BCLK_I_DIV** (line 45)
- **MLB_SD_TOCLK_I_DIV** (line 38)
- **MLB_SOFT_RESET** (line 23)
- **MLB_SOFT_RESET_RSTX** (line 24)
- **MLB_TOCLKFREQ_MAX** (line 42)
- **MLB_TOCLKFREQ_MIN** (line 43)
- **MLB_TOCLKFREQ_UNIT_THRES** (line 39)
- **MLB_WP_CD_LED_SET** (line 26)
- **MLB_WP_CD_LED_SET_LED_INV** (line 27)
