# drivers/mmc/host/sdhci-of-aspeed.c

Subsystem: drivers/mmc

## Functions (18)

### aspeed_sdc_configure_8bit_mode
- Return type: static void
- Signature: aspeed_sdc_configure_8bit_mode(struct aspeed_sdc * sdc,struct aspeed_sdhci * sdhci,bool bus8)
- Line: 112

### aspeed_sdc_exit
- Return type: static void __exit
- Signature: aspeed_sdc_exit(void)
- Line: 621

### aspeed_sdc_init
- Return type: static int __init
- Signature: aspeed_sdc_init(void)
- Line: 605

### aspeed_sdc_probe
- Return type: static int
- Signature: aspeed_sdc_probe(struct platform_device * pdev)
- Line: 520

### aspeed_sdc_remove
- Return type: static void
- Signature: aspeed_sdc_remove(struct platform_device * pdev)
- Line: 574

### aspeed_sdc_set_phase_tap
- Return type: static u32
- Signature: aspeed_sdc_set_phase_tap(const struct aspeed_sdhci_tap_desc * desc,u8 tap,bool enable,u32 reg)
- Line: 130

### aspeed_sdc_set_phase_taps
- Return type: static void
- Signature: aspeed_sdc_set_phase_taps(struct aspeed_sdc * sdc,const struct aspeed_sdhci_phase_desc * desc,const struct aspeed_sdhci_tap_param * taps)
- Line: 143

### aspeed_sdc_set_slot_capability
- Return type: static void
- Signature: aspeed_sdc_set_slot_capability(struct sdhci_host * host,struct aspeed_sdc * sdc,int capability,bool enable,u8 slot)
- Line: 92

### aspeed_sdhci_calculate_slot
- Return type: static int
- Signature: aspeed_sdhci_calculate_slot(struct aspeed_sdhci * dev,struct resource * res)
- Line: 347

### aspeed_sdhci_configure_phase
- Return type: static void
- Signature: aspeed_sdhci_configure_phase(struct sdhci_host * host,unsigned long rate)
- Line: 214

### aspeed_sdhci_get_max_clock
- Return type: static unsigned int
- Signature: aspeed_sdhci_get_max_clock(struct sdhci_host * host)
- Line: 289

### aspeed_sdhci_phase_to_tap
- Return type: static int
- Signature: aspeed_sdhci_phase_to_tap(struct device * dev,unsigned long rate_hz,int phase_deg)
- Line: 163

### aspeed_sdhci_phases_to_taps
- Return type: static void
- Signature: aspeed_sdhci_phases_to_taps(struct device * dev,unsigned long rate,const struct mmc_clk_phase * phases,struct aspeed_sdhci_tap_param * taps)
- Line: 200

### aspeed_sdhci_probe
- Return type: static int
- Signature: aspeed_sdhci_probe(struct platform_device * pdev)
- Line: 365

### aspeed_sdhci_readl
- Return type: static u32
- Signature: aspeed_sdhci_readl(struct sdhci_host * host,int reg)
- Line: 321

### aspeed_sdhci_remove
- Return type: static void
- Signature: aspeed_sdhci_remove(struct platform_device * pdev)
- Line: 450

### aspeed_sdhci_set_bus_width
- Return type: static void
- Signature: aspeed_sdhci_set_bus_width(struct sdhci_host * host,int width)
- Line: 297

### aspeed_sdhci_set_clock
- Return type: static void
- Signature: aspeed_sdhci_set_clock(struct sdhci_host * host,unsigned int clock)
- Line: 237

## Structs (6)

### aspeed_sdc
- Line: 40
- Members:
  - clk: clk *
  - res: resource *
  - lock: spinlock_t
  - regs: void __iomem *
  - valid: bool
  - in: u8
  - out: u8
  - tap_mask: u32
  - enable_mask: u32
  - enable_value: u8
  - in: aspeed_sdhci_tap_desc
  - out: aspeed_sdhci_tap_desc
  - clk_div_start: unsigned int
  - phase_desc: const struct aspeed_sdhci_phase_desc *
  - nr_phase_descs: size_t
  - pdata: const struct aspeed_sdhci_pdata *
  - parent: aspeed_sdc *
  - width_mask: u32
  - phase_map: mmc_clk_phase_map
  - phase_desc: const struct aspeed_sdhci_phase_desc *

### aspeed_sdhci
- Line: 73
- Members:
  - clk: clk *
  - res: resource *
  - lock: spinlock_t
  - regs: void __iomem *
  - valid: bool
  - in: u8
  - out: u8
  - tap_mask: u32
  - enable_mask: u32
  - enable_value: u8
  - in: aspeed_sdhci_tap_desc
  - out: aspeed_sdhci_tap_desc
  - clk_div_start: unsigned int
  - phase_desc: const struct aspeed_sdhci_phase_desc *
  - nr_phase_descs: size_t
  - pdata: const struct aspeed_sdhci_pdata *
  - parent: aspeed_sdc *
  - width_mask: u32
  - phase_map: mmc_clk_phase_map
  - phase_desc: const struct aspeed_sdhci_phase_desc *

### aspeed_sdhci_pdata
- Line: 67
- Members:
  - clk: clk *
  - res: resource *
  - lock: spinlock_t
  - regs: void __iomem *
  - valid: bool
  - in: u8
  - out: u8
  - tap_mask: u32
  - enable_mask: u32
  - enable_value: u8
  - in: aspeed_sdhci_tap_desc
  - out: aspeed_sdhci_tap_desc
  - clk_div_start: unsigned int
  - phase_desc: const struct aspeed_sdhci_phase_desc *
  - nr_phase_descs: size_t
  - pdata: const struct aspeed_sdhci_pdata *
  - parent: aspeed_sdc *
  - width_mask: u32
  - phase_map: mmc_clk_phase_map
  - phase_desc: const struct aspeed_sdhci_phase_desc *

### aspeed_sdhci_phase_desc
- Line: 62
- Members:
  - clk: clk *
  - res: resource *
  - lock: spinlock_t
  - regs: void __iomem *
  - valid: bool
  - in: u8
  - out: u8
  - tap_mask: u32
  - enable_mask: u32
  - enable_value: u8
  - in: aspeed_sdhci_tap_desc
  - out: aspeed_sdhci_tap_desc
  - clk_div_start: unsigned int
  - phase_desc: const struct aspeed_sdhci_phase_desc *
  - nr_phase_descs: size_t
  - pdata: const struct aspeed_sdhci_pdata *
  - parent: aspeed_sdc *
  - width_mask: u32
  - phase_map: mmc_clk_phase_map
  - phase_desc: const struct aspeed_sdhci_phase_desc *

### aspeed_sdhci_tap_desc
- Line: 56
- Members:
  - clk: clk *
  - res: resource *
  - lock: spinlock_t
  - regs: void __iomem *
  - valid: bool
  - in: u8
  - out: u8
  - tap_mask: u32
  - enable_mask: u32
  - enable_value: u8
  - in: aspeed_sdhci_tap_desc
  - out: aspeed_sdhci_tap_desc
  - clk_div_start: unsigned int
  - phase_desc: const struct aspeed_sdhci_phase_desc *
  - nr_phase_descs: size_t
  - pdata: const struct aspeed_sdhci_pdata *
  - parent: aspeed_sdc *
  - width_mask: u32
  - phase_map: mmc_clk_phase_map
  - phase_desc: const struct aspeed_sdhci_phase_desc *

### aspeed_sdhci_tap_param
- Line: 48
- Members:
  - clk: clk *
  - res: resource *
  - lock: spinlock_t
  - regs: void __iomem *
  - valid: bool
  - in: u8
  - out: u8
  - tap_mask: u32
  - enable_mask: u32
  - enable_value: u8
  - in: aspeed_sdhci_tap_desc
  - out: aspeed_sdhci_tap_desc
  - clk_div_start: unsigned int
  - phase_desc: const struct aspeed_sdhci_phase_desc *
  - nr_phase_descs: size_t
  - pdata: const struct aspeed_sdhci_pdata *
  - parent: aspeed_sdc *
  - width_mask: u32
  - phase_map: mmc_clk_phase_map
  - phase_desc: const struct aspeed_sdhci_phase_desc *

## Variables (9)

- static **aspeed_sdc_driver** : platform_driver (line 590)
- static **aspeed_sdc_of_match** : const struct of_device_id[] (line 581)
- static **aspeed_sdhci_driver** : platform_driver (line 510)
- static **aspeed_sdhci_of_match** : const struct of_device_id[] (line 502)
- static **aspeed_sdhci_ops** : const struct sdhci_ops (line 332)
- static **aspeed_sdhci_pdata** : const struct sdhci_pltfm_data (line 342)
- static **ast2400_sdhci_pdata** : const struct aspeed_sdhci_pdata (line 463)
- static **ast2600_sdhci_pdata** : const struct aspeed_sdhci_pdata (line 496)
- static **ast2600_sdhci_phase** : const struct aspeed_sdhci_phase_desc[] (line 467)

## Macros (19)

- **ASPEED_SDC_CAP1_1_8V** (line 36)
- **ASPEED_SDC_CAP2_SDR104** (line 38)
- **ASPEED_SDC_INFO** (line 21)
- **ASPEED_SDC_PHASE** (line 24)
- **ASPEED_SDC_PHASE_MAX** (line 33)
- **ASPEED_SDC_S0_MMC8** (line 23)
- **ASPEED_SDC_S0_PHASE_IN** (line 26)
- **ASPEED_SDC_S0_PHASE_IN_EN** (line 31)
- **ASPEED_SDC_S0_PHASE_OUT** (line 30)
- **ASPEED_SDC_S0_PHASE_OUT_EN** (line 32)
- **ASPEED_SDC_S1_MMC8** (line 22)
- **ASPEED_SDC_S1_PHASE_IN** (line 25)
- **ASPEED_SDC_S1_PHASE_IN_EN** (line 28)
- **ASPEED_SDC_S1_PHASE_OUT** (line 27)
- **ASPEED_SDC_S1_PHASE_OUT_EN** (line 29)
- **ASPEED_SDHCI_MAX_TAP_DELAY_PS** (line 162)
- **ASPEED_SDHCI_NR_TAPS** (line 160)
- **ASPEED_SDHCI_TAP_PARAM_INVERT_CLK** (line 51)
- **PICOSECONDS_PER_SECOND** (line 159)
