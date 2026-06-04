# drivers/mmc/host/sdhci-of-bst.c

Subsystem: drivers/mmc

## Functions (16)

### sdhci_bst_alloc_bounce_buffer
- Return type: static int
- Signature: sdhci_bst_alloc_bounce_buffer(struct sdhci_host * host)
- Line: 411

### sdhci_bst_crm_read
- Return type: static u32
- Signature: sdhci_bst_crm_read(struct sdhci_pltfm_host * pltfm_host,u32 offset)
- Line: 90

### sdhci_bst_crm_write
- Return type: static void
- Signature: sdhci_bst_crm_write(struct sdhci_pltfm_host * pltfm_host,u32 offset,u32 value)
- Line: 97

### sdhci_bst_enable_clk
- Return type: static void
- Signature: sdhci_bst_enable_clk(struct sdhci_host * host,unsigned int clk)
- Line: 125

### sdhci_bst_execute_tuning
- Return type: static int
- Signature: sdhci_bst_execute_tuning(struct sdhci_host * host,u32 opcode)
- Line: 311

### sdhci_bst_free_bounce_buffer
- Return type: static void
- Signature: sdhci_bst_free_bounce_buffer(struct sdhci_host * host)
- Line: 401

### sdhci_bst_get_max_clock
- Return type: static unsigned int
- Signature: sdhci_bst_get_max_clock(struct sdhci_host * host)
- Line: 115

### sdhci_bst_get_min_clock
- Return type: static unsigned int
- Signature: sdhci_bst_get_min_clock(struct sdhci_host * host)
- Line: 120

### sdhci_bst_probe
- Return type: static int
- Signature: sdhci_bst_probe(struct platform_device * pdev)
- Line: 438

### sdhci_bst_remove
- Return type: static void
- Signature: sdhci_bst_remove(struct platform_device * pdev)
- Line: 497

### sdhci_bst_reset
- Return type: static void
- Signature: sdhci_bst_reset(struct sdhci_host * host,u8 mask)
- Line: 237

### sdhci_bst_set_clock
- Return type: static void
- Signature: sdhci_bst_set_clock(struct sdhci_host * host,unsigned int clock)
- Line: 220

### sdhci_bst_set_power
- Return type: static void
- Signature: sdhci_bst_set_power(struct sdhci_host * host,unsigned char mode,unsigned short vdd)
- Line: 269

### sdhci_bst_set_timeout
- Return type: static void
- Signature: sdhci_bst_set_timeout(struct sdhci_host * host,struct mmc_command * cmd)
- Line: 260

### sdhci_bst_voltage_switch
- Return type: static void
- Signature: sdhci_bst_voltage_switch(struct sdhci_host * host)
- Line: 369

### sdhci_bst_wait_int_clk
- Return type: static int
- Signature: sdhci_bst_wait_int_clk(struct sdhci_host * host)
- Line: 104

## Structs (2)

### __anond34806aa0108
- Line: 77
- Members:
  - crm_reg_base: void __iomem *
  - rx_revert: u32:1
  - rx_clk_sel_sec: u32:1
  - rx_clk_div: u32:4
  - rx_clk_phase_inner: u32:2
  - rx_clk_sel_first: u32:1
  - rx_clk_phase_out: u32:2
  - rx_clk_en: u32:1
  - res0: u32:20
  - reg: u32

### sdhci_bst_priv
- Line: 72
- Members:
  - crm_reg_base: void __iomem *
  - rx_revert: u32:1
  - rx_clk_sel_sec: u32:1
  - rx_clk_div: u32:4
  - rx_clk_phase_inner: u32:2
  - rx_clk_sel_first: u32:1
  - rx_clk_phase_out: u32:2
  - rx_clk_en: u32:1
  - res0: u32:20
  - reg: u32

## Unions (1)

### sdhci_bst_rx_ctrl
- Line: 76
- Members:
  - crm_reg_base: void __iomem *
  - rx_revert: u32:1
  - rx_clk_sel_sec: u32:1
  - rx_clk_div: u32:4
  - rx_clk_phase_inner: u32:2
  - rx_clk_sel_first: u32:1
  - rx_clk_phase_out: u32:2
  - rx_clk_en: u32:1
  - res0: u32:20
  - reg: u32

## Variables (4)

- static **sdhci_bst_driver** : platform_driver (line 511)
- static **sdhci_bst_ids** : const struct of_device_id[] (line 505)
- static **sdhci_bst_ops** : const struct sdhci_ops (line 377)
- static **sdhci_bst_pdata** : const struct sdhci_pltfm_data (line 390)

## Macros (32)

- **BST_BCLK_DIV_MASK** (line 63)
- **BST_BCLK_EN_BIT** (line 52)
- **BST_CLK_STABLE_POLL_US** (line 69)
- **BST_CLK_STABLE_TIMEOUT_US** (line 70)
- **BST_CLOCK_DIV_MASK** (line 61)
- **BST_CLOCK_DIV_SHIFT** (line 62)
- **BST_CLOCK_THRESHOLD_LOW** (line 66)
- **BST_DEFAULT_MAX_FREQ** (line 57)
- **BST_DEFAULT_MIN_FREQ** (line 58)
- **BST_EMMC_CTRL_RST_N** (line 54)
- **BST_RX_UPDATE_BIT** (line 53)
- **BST_TIMER_DIV_MASK** (line 49)
- **BST_TIMER_DIV_VAL** (line 50)
- **BST_TIMER_LOAD_BIT** (line 51)
- **BST_TUNING_COUNT** (line 25)
- **BST_VOL_STABLE_ON** (line 48)
- **BURST_EN** (line 35)
- **BURST_INCR16_EN** (line 32)
- **BURST_INCR4_EN** (line 34)
- **BURST_INCR8_EN** (line 33)
- **DELAY_CHAIN_SEL** (line 44)
- **MBIU_BURST_MASK** (line 36)
- **MBIU_CTRL** (line 29)
- **REG_WR_PROTECT** (line 43)
- **REG_WR_PROTECT_KEY** (line 47)
- **SDEMMC_CRM_BCLK_DIV_CTRL** (line 39)
- **SDEMMC_CRM_RX_CLK_CTRL** (line 41)
- **SDEMMC_CRM_TIMER_DIV_CTRL** (line 40)
- **SDEMMC_CRM_VOL_CTRL** (line 42)
- **SDHCI_CLOCK_PLL_EN** (line 21)
- **SDHCI_VENDOR_PTR_R** (line 22)
- **SDHC_EMMC_CTRL_R_OFFSET** (line 28)
