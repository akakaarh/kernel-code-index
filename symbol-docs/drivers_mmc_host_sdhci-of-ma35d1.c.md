# drivers/mmc/host/sdhci-of-ma35d1.c

Subsystem: drivers/mmc

## Functions (8)

### ma35_adma_write_desc
- Return type: static void
- Signature: ma35_adma_write_desc(struct sdhci_host * host,void ** desc,dma_addr_t addr,int len,unsigned int cmd)
- Line: 72

### ma35_disable_card_clk
- Return type: static void
- Signature: ma35_disable_card_clk(struct sdhci_host * host)
- Line: 271

### ma35_execute_tuning
- Return type: static int
- Signature: ma35_execute_tuning(struct mmc_host * mmc,u32 opcode)
- Line: 138

### ma35_probe
- Return type: static int
- Signature: ma35_probe(struct platform_device * pdev)
- Line: 192

### ma35_remove
- Return type: static void
- Signature: ma35_remove(struct platform_device * pdev)
- Line: 282

### ma35_set_clock
- Return type: static void
- Signature: ma35_set_clock(struct sdhci_host * host,unsigned int clock)
- Line: 91

### ma35_start_signal_voltage_switch
- Return type: static int
- Signature: ma35_start_signal_voltage_switch(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 109

### ma35_voltage_switch
- Return type: static void
- Signature: ma35_voltage_switch(struct sdhci_host * host)
- Line: 132

## Structs (2)

### ma35_priv
- Line: 44
- Members:
  - rst: reset_control *
  - pinctrl: pinctrl *
  - pins_uhs: pinctrl_state *
  - pins_default: pinctrl_state *
  - reg: u32
  - width: u32

### ma35_restore_data
- Line: 51
- Members:
  - rst: reset_control *
  - pinctrl: pinctrl *
  - pins_uhs: pinctrl_state *
  - pins_default: pinctrl_state *
  - reg: u32
  - width: u32

## Variables (5)

- static **restore_data** : const struct ma35_restore_data[] (line 56)
- static **sdhci_ma35_driver** : platform_driver (line 295)
- static **sdhci_ma35_dt_ids** : const struct of_device_id[] (line 290)
- static **sdhci_ma35_ops** : const struct sdhci_ops (line 175)
- static **sdhci_ma35_pdata** : const struct sdhci_pltfm_data (line 185)

## Macros (7)

- **MA35_SDHCI_CMD_CONFLICT_CHK** (line 39)
- **MA35_SDHCI_INCR16** (line 41)
- **MA35_SDHCI_INCR8** (line 42)
- **MA35_SDHCI_INCR_MSK** (line 40)
- **MA35_SDHCI_MBIUCTL** (line 37)
- **MA35_SDHCI_MSHCCTL** (line 36)
- **MA35_SYS_MISCFCR0** (line 35)
