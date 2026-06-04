# drivers/mmc/host/sdhci-pxav2.c

Subsystem: drivers/mmc

## Functions (8)

### pxav1_irq
- Return type: static u32
- Signature: pxav1_irq(struct sdhci_host * host,u32 intmask)
- Line: 101

### pxav1_readw
- Return type: static u16
- Signature: pxav1_readw(struct sdhci_host * host,int reg)
- Line: 92

### pxav1_request_done
- Return type: static void
- Signature: pxav1_request_done(struct sdhci_host * host,struct mmc_request * mrq)
- Line: 123

### pxav2_get_mmc_pdata
- Return type: static sdhci_pxa_platdata *
- Signature: pxav2_get_mmc_pdata(struct device * dev)
- Line: 246

### pxav2_get_mmc_pdata
- Return type: static sdhci_pxa_platdata *
- Signature: pxav2_get_mmc_pdata(struct device * dev)
- Line: 219

### pxav2_mmc_set_bus_width
- Return type: static void
- Signature: pxav2_mmc_set_bus_width(struct sdhci_host * host,int width)
- Line: 157

### pxav2_reset
- Return type: static void
- Signature: pxav2_reset(struct sdhci_host * host,u8 mask)
- Line: 53

### sdhci_pxav2_probe
- Return type: static int
- Signature: sdhci_pxav2_probe(struct platform_device * pdev)
- Line: 252

## Structs (2)

### sdhci_pxa_variant
- Line: 178
- Members:
  - sdio_mrq: mmc_request *
  - pinctrl: pinctrl *
  - pins_default: pinctrl_state *
  - pins_cmd_gpio: pinctrl_state *
  - ops: const struct sdhci_ops *
  - extra_quirks: unsigned int

### sdhci_pxav2_host
- Line: 46
- Members:
  - sdio_mrq: mmc_request *
  - pinctrl: pinctrl *
  - pins_default: pinctrl_state *
  - pins_cmd_gpio: pinctrl_state *
  - ops: const struct sdhci_ops *
  - extra_quirks: unsigned int

## Variables (6)

- static **pxav1_sdhci_ops** : const struct sdhci_ops (line 183)
- static **pxav1_variant** : const struct sdhci_pxa_variant __maybe_unused (line 194)
- static **pxav2_sdhci_ops** : const struct sdhci_ops (line 199)
- static **pxav2_variant** : const struct sdhci_pxa_variant (line 207)
- static **sdhci_pxav2_driver** : platform_driver (line 332)
- static **sdhci_pxav2_of_match** : const struct of_device_id[] (line 212)

## Macros (13)

- **CLK_GATE_CTL** (line 32)
- **CLK_GATE_ON** (line 31)
- **CLK_GATE_SETTING_BITS** (line 33)
- **DIS_PAD_SD_CLK_GATE** (line 30)
- **MMC_CARD** (line 43)
- **MMC_WIDTH** (line 44)
- **SDCLK_DELAY_MASK** (line 40)
- **SDCLK_DELAY_SHIFT** (line 39)
- **SDCLK_SEL_MASK** (line 38)
- **SDCLK_SEL_SHIFT** (line 37)
- **SD_CE_ATA_2** (line 42)
- **SD_CLOCK_BURST_SIZE_SETUP** (line 36)
- **SD_FIFO_PARAM** (line 29)
