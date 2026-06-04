# drivers/mmc/host/sdhci-of-esdhc.c

Subsystem: drivers/mmc

## Functions (40)

### esdhc_be_readb
- Return type: static u8
- Signature: esdhc_be_readb(struct sdhci_host * host,int reg)
- Line: 385

### esdhc_be_readl
- Return type: static u32
- Signature: esdhc_be_readl(struct sdhci_host * host,int reg)
- Line: 333

### esdhc_be_readw
- Return type: static u16
- Signature: esdhc_be_readw(struct sdhci_host * host,int reg)
- Line: 363

### esdhc_be_writeb
- Return type: static void
- Signature: esdhc_be_writeb(struct sdhci_host * host,u8 val,int reg)
- Line: 475

### esdhc_be_writel
- Return type: static void
- Signature: esdhc_be_writel(struct sdhci_host * host,u32 val,int reg)
- Line: 407

### esdhc_be_writew
- Return type: static void
- Signature: esdhc_be_writew(struct sdhci_host * host,u16 val,int reg)
- Line: 423

### esdhc_clock_enable
- Return type: static void
- Signature: esdhc_clock_enable(struct sdhci_host * host,bool enable)
- Line: 578

### esdhc_execute_sw_tuning
- Return type: static int
- Signature: esdhc_execute_sw_tuning(struct mmc_host * mmc,u32 opcode,u8 window_start,u8 window_end)
- Line: 1035

### esdhc_execute_tuning
- Return type: static int
- Signature: esdhc_execute_tuning(struct mmc_host * mmc,u32 opcode)
- Line: 1062

### esdhc_flush_async_fifo
- Return type: static void
- Signature: esdhc_flush_async_fifo(struct sdhci_host * host)
- Line: 623

### esdhc_hs400_prepare_ddr
- Return type: static int
- Signature: esdhc_hs400_prepare_ddr(struct mmc_host * mmc)
- Line: 1414

### esdhc_init
- Return type: static void
- Signature: esdhc_init(struct platform_device * pdev,struct sdhci_host * host)
- Line: 1338

### esdhc_irq
- Return type: static u32
- Signature: esdhc_irq(struct sdhci_host * host,u32 intmask)
- Line: 1217

### esdhc_le_readb
- Return type: static u8
- Signature: esdhc_le_readb(struct sdhci_host * host,int reg)
- Line: 396

### esdhc_le_readl
- Return type: static u32
- Signature: esdhc_le_readl(struct sdhci_host * host,int reg)
- Line: 348

### esdhc_le_readw
- Return type: static u16
- Signature: esdhc_le_readw(struct sdhci_host * host,int reg)
- Line: 374

### esdhc_le_writeb
- Return type: static void
- Signature: esdhc_le_writeb(struct sdhci_host * host,u8 val,int reg)
- Line: 486

### esdhc_le_writel
- Return type: static void
- Signature: esdhc_le_writel(struct sdhci_host * host,u32 val,int reg)
- Line: 415

### esdhc_le_writew
- Return type: static void
- Signature: esdhc_le_writew(struct sdhci_host * host,u16 val,int reg)
- Line: 449

### esdhc_of_adma_workaround
- Return type: static void
- Signature: esdhc_of_adma_workaround(struct sdhci_host * host,u32 intmask)
- Line: 504

### esdhc_of_enable_dma
- Return type: static int
- Signature: esdhc_of_enable_dma(struct sdhci_host * host)
- Line: 530

### esdhc_of_get_max_clock
- Return type: static unsigned int
- Signature: esdhc_of_get_max_clock(struct sdhci_host * host)
- Line: 554

### esdhc_of_get_min_clock
- Return type: static unsigned int
- Signature: esdhc_of_get_min_clock(struct sdhci_host * host)
- Line: 565

### esdhc_of_resume
- Return type: static int
- Signature: esdhc_of_resume(struct device * dev)
- Line: 1250

### esdhc_of_set_clock
- Return type: static void
- Signature: esdhc_of_set_clock(struct sdhci_host * host,unsigned int clock)
- Line: 649

### esdhc_of_suspend
- Return type: static int
- Signature: esdhc_of_suspend(struct device * dev)
- Line: 1238

### esdhc_pltfm_set_bus_width
- Return type: static void
- Signature: esdhc_pltfm_set_bus_width(struct sdhci_host * host,int width)
- Line: 781

### esdhc_prepare_sw_tuning
- Return type: static void
- Signature: esdhc_prepare_sw_tuning(struct sdhci_host * host,u8 * window_start,u8 * window_end)
- Line: 1000

### esdhc_readb_fixup
- Return type: static u8
- Signature: esdhc_readb_fixup(struct sdhci_host * host,int spec_reg,u32 value)
- Line: 200

### esdhc_readl_fixup
- Return type: static u32
- Signature: esdhc_readl_fixup(struct sdhci_host * host,int spec_reg,u32 value)
- Line: 115

### esdhc_readw_fixup
- Return type: static u16
- Signature: esdhc_readw_fixup(struct sdhci_host * host,int spec_reg,u32 value)
- Line: 176

### esdhc_reset
- Return type: static void
- Signature: esdhc_reset(struct sdhci_host * host,u8 mask)
- Line: 803

### esdhc_set_uhs_signaling
- Return type: static void
- Signature: esdhc_set_uhs_signaling(struct sdhci_host * host,unsigned int timing)
- Line: 1174

### esdhc_signal_voltage_switch
- Return type: static int
- Signature: esdhc_signal_voltage_switch(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 885

### esdhc_tuning_block_enable
- Return type: static void
- Signature: esdhc_tuning_block_enable(struct sdhci_host * host,bool enable)
- Line: 956

### esdhc_tuning_window_ptr
- Return type: static void
- Signature: esdhc_tuning_window_ptr(struct sdhci_host * host,u8 * window_start,u8 * window_end)
- Line: 973

### esdhc_writeb_fixup
- Return type: static u32
- Signature: esdhc_writeb_fixup(struct sdhci_host * host,int spec_reg,u8 value,u32 old_value)
- Line: 291

### esdhc_writel_fixup
- Return type: static u32
- Signature: esdhc_writel_fixup(struct sdhci_host * host,int spec_reg,u32 value,u32 old_value)
- Line: 239

### esdhc_writew_fixup
- Return type: static u32
- Signature: esdhc_writew_fixup(struct sdhci_host * host,int spec_reg,u16 value,u32 old_value)
- Line: 257

### sdhci_esdhc_probe
- Return type: static int
- Signature: sdhci_esdhc_probe(struct platform_device * pdev)
- Line: 1420

## Structs (2)

### esdhc_clk_fixup
- Line: 34
- Members:
  - sd_dflt_max_clk: const unsigned int
  - max_clk: const unsigned int[]
  - vendor_ver: u8
  - spec_ver: u8
  - quirk_incorrect_hostver: bool
  - quirk_limited_clk_division: bool
  - quirk_unreliable_pulse_detection: bool
  - quirk_tuning_erratum_type1: bool
  - quirk_tuning_erratum_type2: bool
  - quirk_ignore_data_inhibit: bool
  - quirk_delay_before_data_reset: bool
  - quirk_trans_complete_erratum: bool
  - in_sw_tuning: bool
  - peripheral_clock: unsigned int
  - clk_fixup: const struct esdhc_clk_fixup *
  - div_ratio: u32

### sdhci_esdhc
- Line: 83
- Members:
  - sd_dflt_max_clk: const unsigned int
  - max_clk: const unsigned int[]
  - vendor_ver: u8
  - spec_ver: u8
  - quirk_incorrect_hostver: bool
  - quirk_limited_clk_division: bool
  - quirk_unreliable_pulse_detection: bool
  - quirk_tuning_erratum_type1: bool
  - quirk_tuning_erratum_type2: bool
  - quirk_ignore_data_inhibit: bool
  - quirk_delay_before_data_reset: bool
  - quirk_trans_complete_erratum: bool
  - in_sw_tuning: bool
  - peripheral_clock: unsigned int
  - clk_fixup: const struct esdhc_clk_fixup *
  - div_ratio: u32

## Variables (18)

- static **esdhc_proctl** : u32 (line 1237)
- static **ls1012a_esdhc_clk** : const struct esdhc_clk_fixup (line 57)
- static **ls1021a_esdhc_clk** : const struct esdhc_clk_fixup (line 39)
- static **ls1043a_esdhc_clk** : const struct esdhc_clk_fixup (line 45)
- static **ls1046a_esdhc_clk** : const struct esdhc_clk_fixup (line 51)
- static **p1010_esdhc_clk** : const struct esdhc_clk_fixup (line 63)
- static **scfg_device_ids** : const struct of_device_id[] (line 872)
- static **sdhci_esdhc_be_ops** : const struct sdhci_ops (line 1265)
- static **sdhci_esdhc_be_pdata** : const struct sdhci_pltfm_data (line 1301)
- static **sdhci_esdhc_driver** : platform_driver (line 1505)
- static **sdhci_esdhc_le_ops** : const struct sdhci_ops (line 1283)
- static **sdhci_esdhc_le_pdata** : const struct sdhci_pltfm_data (line 1311)
- static **sdhci_esdhc_of_match** : const struct of_device_id[] (line 70)
- static **soc_fixup_sdhc_clkdivs** : soc_device_attribute[] (line 1324)
- static **soc_incorrect_hostver** : soc_device_attribute[] (line 1318)
- static **soc_tuning_erratum_type1** : soc_device_attribute[] (line 938)
- static **soc_tuning_erratum_type2** : soc_device_attribute[] (line 946)
- static **soc_unreliable_pulse_detection** : soc_device_attribute[] (line 1331)

## Macros (7)

- **MMC_TIMING_NUM** (line 32)
- **SCFG_SDHCIOVSELCR** (line 880)
- **SDHCIOVSELCR_SDHC_VS** (line 883)
- **SDHCIOVSELCR_TGLEN** (line 881)
- **SDHCIOVSELCR_VSELVAL** (line 882)
- **VENDOR_V_22** (line 29)
- **VENDOR_V_23** (line 30)
