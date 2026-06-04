# drivers/mmc/host/sdhci-of-dwcmshc.c

Subsystem: drivers/mmc

## Functions (70)

### cv18xx_retry_tuning
- Return type: static int
- Signature: cv18xx_retry_tuning(struct mmc_host * mmc,u32 opcode,int * cmd_error)
- Line: 1142

### cv18xx_sdhci_execute_tuning
- Return type: static int
- Signature: cv18xx_sdhci_execute_tuning(struct sdhci_host * host,u32 opcode)
- Line: 1167

### cv18xx_sdhci_post_tuning
- Return type: static void
- Signature: cv18xx_sdhci_post_tuning(struct sdhci_host * host)
- Line: 1156

### cv18xx_sdhci_reset
- Return type: static void
- Signature: cv18xx_sdhci_reset(struct sdhci_host * host,u8 mask)
- Line: 1086

### cv18xx_sdhci_set_tap
- Return type: static void
- Signature: cv18xx_sdhci_set_tap(struct sdhci_host * host,int tap)
- Line: 1115

### dwcmshc_adma_write_desc
- Return type: static void
- Signature: dwcmshc_adma_write_desc(struct sdhci_host * host,void ** desc,dma_addr_t addr,int len,unsigned int cmd)
- Line: 380

### dwcmshc_bf3_hw_reset
- Return type: static void
- Signature: dwcmshc_bf3_hw_reset(struct sdhci_host * host)
- Line: 2018

### dwcmshc_check_auto_cmd23
- Return type: static void
- Signature: dwcmshc_check_auto_cmd23(struct mmc_host * mmc,struct mmc_request * mrq)
- Line: 429

### dwcmshc_cqe_irq_handler
- Return type: static u32
- Signature: dwcmshc_cqe_irq_handler(struct sdhci_host * host,u32 intmask)
- Line: 618

### dwcmshc_cqhci_dumpregs
- Return type: static void
- Signature: dwcmshc_cqhci_dumpregs(struct mmc_host * mmc)
- Line: 679

### dwcmshc_cqhci_init
- Return type: static void
- Signature: dwcmshc_cqhci_init(struct sdhci_host * host,struct platform_device * pdev,const struct dwcmshc_pltfm_data * pltfm_data)
- Line: 2272

### dwcmshc_disable_card_clk
- Return type: static void
- Signature: dwcmshc_disable_card_clk(struct sdhci_host * host)
- Line: 2517

### dwcmshc_enable_card_clk
- Return type: static void
- Signature: dwcmshc_enable_card_clk(struct sdhci_host * host)
- Line: 337

### dwcmshc_execute_tuning
- Return type: static int
- Signature: dwcmshc_execute_tuning(struct mmc_host * mmc,u32 opcode)
- Line: 600

### dwcmshc_get_enable_other_clks
- Return type: static int
- Signature: dwcmshc_get_enable_other_clks(struct device * dev,struct dwcmshc_priv * priv,int num_clks,const char * const clk_ids[])
- Line: 348

### dwcmshc_get_max_clock
- Return type: static unsigned int
- Signature: dwcmshc_get_max_clock(struct sdhci_host * host)
- Line: 412

### dwcmshc_hpe_gsc_init
- Return type: static int
- Signature: dwcmshc_hpe_gsc_init(struct device * dev,struct sdhci_host * host,struct dwcmshc_priv * dwc_priv)
- Line: 1388

### dwcmshc_hpe_reset
- Return type: static void
- Signature: dwcmshc_hpe_reset(struct sdhci_host * host,u8 mask)
- Line: 1334

### dwcmshc_hpe_set_clock
- Return type: static void
- Signature: dwcmshc_hpe_set_clock(struct sdhci_host * host,unsigned int clock)
- Line: 1354

### dwcmshc_hpe_set_emmc
- Return type: static void
- Signature: dwcmshc_hpe_set_emmc(struct sdhci_host * host)
- Line: 1323

### dwcmshc_hpe_set_uhs_signaling
- Return type: static void
- Signature: dwcmshc_hpe_set_uhs_signaling(struct sdhci_host * host,unsigned int timing)
- Line: 1341

### dwcmshc_hpe_vendor_specific
- Return type: static void
- Signature: dwcmshc_hpe_vendor_specific(struct sdhci_host * host)
- Line: 1305

### dwcmshc_hs400_enhanced_strobe
- Return type: static void
- Signature: dwcmshc_hs400_enhanced_strobe(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 582

### dwcmshc_k230_init
- Return type: static int
- Signature: dwcmshc_k230_init(struct device * dev,struct sdhci_host * host,struct dwcmshc_priv * dwc_priv)
- Line: 1953

### dwcmshc_k230_phy_init
- Return type: static int
- Signature: dwcmshc_k230_phy_init(struct sdhci_host * host)
- Line: 1873

### dwcmshc_k230_sdhci_reset
- Return type: static void
- Signature: dwcmshc_k230_sdhci_reset(struct sdhci_host * host,u8 mask)
- Line: 1932

### dwcmshc_k230_sdhci_set_clock
- Return type: static void
- Signature: dwcmshc_k230_sdhci_set_clock(struct sdhci_host * host,unsigned int clock)
- Line: 1832

### dwcmshc_phy_init
- Return type: static void
- Signature: dwcmshc_phy_init(struct sdhci_host * host)
- Line: 452

### dwcmshc_probe
- Return type: static int
- Signature: dwcmshc_probe(struct platform_device * pdev)
- Line: 2400

### dwcmshc_remove
- Return type: static void
- Signature: dwcmshc_remove(struct platform_device * pdev)
- Line: 2528

### dwcmshc_request
- Return type: static void
- Signature: dwcmshc_request(struct mmc_host * mmc,struct mmc_request * mrq)
- Line: 445

### dwcmshc_reset
- Return type: static void
- Signature: dwcmshc_reset(struct sdhci_host * host,u8 mask)
- Line: 399

### dwcmshc_resume
- Return type: static int
- Signature: dwcmshc_resume(struct device * dev)
- Line: 2575

### dwcmshc_rk3568_set_clock
- Return type: static void
- Signature: dwcmshc_rk3568_set_clock(struct sdhci_host * host,unsigned int clock)
- Line: 751

### dwcmshc_rk3576_postinit
- Return type: static void
- Signature: dwcmshc_rk3576_postinit(struct sdhci_host * host,struct dwcmshc_priv * dwc_priv)
- Line: 960

### dwcmshc_rk35xx_init
- Return type: static int
- Signature: dwcmshc_rk35xx_init(struct device * dev,struct sdhci_host * host,struct dwcmshc_priv * dwc_priv)
- Line: 908

### dwcmshc_rk35xx_postinit
- Return type: static void
- Signature: dwcmshc_rk35xx_postinit(struct sdhci_host * host,struct dwcmshc_priv * dwc_priv)
- Line: 946

### dwcmshc_runtime_resume
- Return type: static int
- Signature: dwcmshc_runtime_resume(struct device * dev)
- Line: 2627

### dwcmshc_runtime_suspend
- Return type: static int
- Signature: dwcmshc_runtime_suspend(struct device * dev)
- Line: 2618

### dwcmshc_sdhci_cqe_enable
- Return type: static void
- Signature: dwcmshc_sdhci_cqe_enable(struct mmc_host * mmc)
- Line: 631

### dwcmshc_set_tran_desc
- Return type: static void
- Signature: dwcmshc_set_tran_desc(struct cqhci_host * cq_host,u8 ** desc,dma_addr_t addr,int len,bool end,bool dma64)
- Line: 659

### dwcmshc_set_uhs_signaling
- Return type: static void
- Signature: dwcmshc_set_uhs_signaling(struct sdhci_host * host,unsigned int timing)
- Line: 531

### dwcmshc_suspend
- Return type: static int
- Signature: dwcmshc_suspend(struct device * dev)
- Line: 2547

### eic7700_convert_drive_impedance_ohm
- Return type: static unsigned int
- Signature: eic7700_convert_drive_impedance_ohm(struct device * dev,unsigned int dr_ohm)
- Line: 1533

### eic7700_init
- Return type: static int
- Signature: eic7700_init(struct device * dev,struct sdhci_host * host,struct dwcmshc_priv * dwc_priv)
- Line: 1767

### rk35xx_get_max_clock
- Return type: static unsigned int
- Signature: rk35xx_get_max_clock(struct sdhci_host * host)
- Line: 422

### rk35xx_sdhci_cqe_disable
- Return type: static void
- Signature: rk35xx_sdhci_cqe_disable(struct mmc_host * mmc,bool recovery)
- Line: 717

### rk35xx_sdhci_cqe_enable
- Return type: static void
- Signature: rk35xx_sdhci_cqe_enable(struct mmc_host * mmc)
- Line: 701

### rk35xx_sdhci_cqe_post_disable
- Return type: static void
- Signature: rk35xx_sdhci_cqe_post_disable(struct mmc_host * mmc)
- Line: 739

### rk35xx_sdhci_cqe_pre_enable
- Return type: static void
- Signature: rk35xx_sdhci_cqe_pre_enable(struct mmc_host * mmc)
- Line: 684

### rk35xx_sdhci_reset
- Return type: static void
- Signature: rk35xx_sdhci_reset(struct sdhci_host * host,u8 mask)
- Line: 886

### sdhci_eic7700_config_phy
- Return type: static void
- Signature: sdhci_eic7700_config_phy(struct sdhci_host * host)
- Line: 1452

### sdhci_eic7700_config_phy_delay
- Return type: static void
- Signature: sdhci_eic7700_config_phy_delay(struct sdhci_host * host,int delay)
- Line: 1442

### sdhci_eic7700_delay_tuning
- Return type: static int
- Signature: sdhci_eic7700_delay_tuning(struct sdhci_host * host,u32 opcode)
- Line: 1552

### sdhci_eic7700_executing_tuning
- Return type: static int
- Signature: sdhci_eic7700_executing_tuning(struct sdhci_host * host,u32 opcode)
- Line: 1674

### sdhci_eic7700_phase_code_tuning
- Return type: static int
- Signature: sdhci_eic7700_phase_code_tuning(struct sdhci_host * host,u32 opcode)
- Line: 1593

### sdhci_eic7700_reset
- Return type: static void
- Signature: sdhci_eic7700_reset(struct sdhci_host * host,u8 mask)
- Line: 1498

### sdhci_eic7700_reset_init
- Return type: static int
- Signature: sdhci_eic7700_reset_init(struct device * dev,struct eic7700_priv * priv)
- Line: 1507

### sdhci_eic7700_set_clock
- Return type: static void
- Signature: sdhci_eic7700_set_clock(struct sdhci_host * host,unsigned int clock)
- Line: 1421

### sdhci_eic7700_set_uhs_signaling
- Return type: static void
- Signature: sdhci_eic7700_set_uhs_signaling(struct sdhci_host * host,unsigned int timing)
- Line: 1707

### sdhci_eic7700_set_uhs_wrapper
- Return type: static void
- Signature: sdhci_eic7700_set_uhs_wrapper(struct sdhci_host * host,unsigned int timing)
- Line: 1757

### sdhci_k230_config_phy_delay
- Return type: static void
- Signature: sdhci_k230_config_phy_delay(struct sdhci_host * host)
- Line: 1848

### sg2042_init
- Return type: static int
- Signature: sg2042_init(struct device * dev,struct sdhci_host * host,struct dwcmshc_priv * dwc_priv)
- Line: 1292

### sg2042_sdhci_phy_init
- Return type: static void
- Signature: sg2042_sdhci_phy_init(struct sdhci_host * host)
- Line: 1222

### sg2042_sdhci_reset
- Return type: static void
- Signature: sg2042_sdhci_reset(struct sdhci_host * host,u8 mask)
- Line: 1284

### th1520_execute_tuning
- Return type: static int
- Signature: th1520_execute_tuning(struct sdhci_host * host,u32 opcode)
- Line: 983

### th1520_init
- Return type: static int
- Signature: th1520_init(struct device * dev,struct sdhci_host * host,struct dwcmshc_priv * dwc_priv)
- Line: 1057

### th1520_sdhci_reset
- Return type: static void
- Signature: th1520_sdhci_reset(struct sdhci_host * host,u8 mask)
- Line: 1040

### th1520_sdhci_set_phy
- Return type: static void
- Signature: th1520_sdhci_set_phy(struct sdhci_host * host)
- Line: 512

### th1520_set_uhs_signaling
- Return type: static void
- Signature: th1520_set_uhs_signaling(struct sdhci_host * host,unsigned int timing)
- Line: 568

## Structs (7)

### dwcmshc_pltfm_data
- Line: 312
- Members:
  - reset: reset_control *
  - txclk_tapnum: u8
  - reset: reset_control *
  - drive_impedance: unsigned int
  - hi_sys_regmap: regmap *
  - bus_clk: clk *
  - vendor_specific_area1: int
  - vendor_specific_area2: int
  - num_other_clks: int
  - other_clks: clk_bulk_data[]
  - dwcmshc_pdata: const struct dwcmshc_pltfm_data *
  - priv: void *
  - delay_line: u16
  - flags: u16
  - pdata: const struct sdhci_pltfm_data
  - cqhci_host_ops: const struct cqhci_host_ops *
  - init: int (*)(struct device * dev,struct sdhci_host * host,struct dwcmshc_priv * dwc_priv)
  - postinit: void (*)(struct sdhci_host * host,struct dwcmshc_priv * dwc_priv)
  - dwcmshc_pdata: dwcmshc_pltfm_data
  - is_emmc: bool
  - ctrl_reg: u32
  - vol_stable_bit: u32
  - write_prot_bit: u32
  - dwcmshc_pdata: dwcmshc_pltfm_data
  - revision: int

### dwcmshc_priv
- Line: 298
- Members:
  - reset: reset_control *
  - txclk_tapnum: u8
  - reset: reset_control *
  - drive_impedance: unsigned int
  - hi_sys_regmap: regmap *
  - bus_clk: clk *
  - vendor_specific_area1: int
  - vendor_specific_area2: int
  - num_other_clks: int
  - other_clks: clk_bulk_data[]
  - dwcmshc_pdata: const struct dwcmshc_pltfm_data *
  - priv: void *
  - delay_line: u16
  - flags: u16
  - pdata: const struct sdhci_pltfm_data
  - cqhci_host_ops: const struct cqhci_host_ops *
  - init: int (*)(struct device * dev,struct sdhci_host * host,struct dwcmshc_priv * dwc_priv)
  - postinit: void (*)(struct sdhci_host * host,struct dwcmshc_priv * dwc_priv)
  - dwcmshc_pdata: dwcmshc_pltfm_data
  - is_emmc: bool
  - ctrl_reg: u32
  - vol_stable_bit: u32
  - write_prot_bit: u32
  - dwcmshc_pdata: dwcmshc_pltfm_data
  - revision: int

### eic7700_priv
- Line: 286
- Members:
  - reset: reset_control *
  - txclk_tapnum: u8
  - reset: reset_control *
  - drive_impedance: unsigned int
  - hi_sys_regmap: regmap *
  - bus_clk: clk *
  - vendor_specific_area1: int
  - vendor_specific_area2: int
  - num_other_clks: int
  - other_clks: clk_bulk_data[]
  - dwcmshc_pdata: const struct dwcmshc_pltfm_data *
  - priv: void *
  - delay_line: u16
  - flags: u16
  - pdata: const struct sdhci_pltfm_data
  - cqhci_host_ops: const struct cqhci_host_ops *
  - init: int (*)(struct device * dev,struct sdhci_host * host,struct dwcmshc_priv * dwc_priv)
  - postinit: void (*)(struct sdhci_host * host,struct dwcmshc_priv * dwc_priv)
  - dwcmshc_pdata: dwcmshc_pltfm_data
  - is_emmc: bool
  - ctrl_reg: u32
  - vol_stable_bit: u32
  - write_prot_bit: u32
  - dwcmshc_pdata: dwcmshc_pltfm_data
  - revision: int

### k230_pltfm_data
- Line: 319
- Members:
  - reset: reset_control *
  - txclk_tapnum: u8
  - reset: reset_control *
  - drive_impedance: unsigned int
  - hi_sys_regmap: regmap *
  - bus_clk: clk *
  - vendor_specific_area1: int
  - vendor_specific_area2: int
  - num_other_clks: int
  - other_clks: clk_bulk_data[]
  - dwcmshc_pdata: const struct dwcmshc_pltfm_data *
  - priv: void *
  - delay_line: u16
  - flags: u16
  - pdata: const struct sdhci_pltfm_data
  - cqhci_host_ops: const struct cqhci_host_ops *
  - init: int (*)(struct device * dev,struct sdhci_host * host,struct dwcmshc_priv * dwc_priv)
  - postinit: void (*)(struct sdhci_host * host,struct dwcmshc_priv * dwc_priv)
  - dwcmshc_pdata: dwcmshc_pltfm_data
  - is_emmc: bool
  - ctrl_reg: u32
  - vol_stable_bit: u32
  - write_prot_bit: u32
  - dwcmshc_pdata: dwcmshc_pltfm_data
  - revision: int

### k230_priv
- Line: 291
- Members:
  - reset: reset_control *
  - txclk_tapnum: u8
  - reset: reset_control *
  - drive_impedance: unsigned int
  - hi_sys_regmap: regmap *
  - bus_clk: clk *
  - vendor_specific_area1: int
  - vendor_specific_area2: int
  - num_other_clks: int
  - other_clks: clk_bulk_data[]
  - dwcmshc_pdata: const struct dwcmshc_pltfm_data *
  - priv: void *
  - delay_line: u16
  - flags: u16
  - pdata: const struct sdhci_pltfm_data
  - cqhci_host_ops: const struct cqhci_host_ops *
  - init: int (*)(struct device * dev,struct sdhci_host * host,struct dwcmshc_priv * dwc_priv)
  - postinit: void (*)(struct sdhci_host * host,struct dwcmshc_priv * dwc_priv)
  - dwcmshc_pdata: dwcmshc_pltfm_data
  - is_emmc: bool
  - ctrl_reg: u32
  - vol_stable_bit: u32
  - write_prot_bit: u32
  - dwcmshc_pdata: dwcmshc_pltfm_data
  - revision: int

### rk35xx_priv
- Line: 281
- Members:
  - reset: reset_control *
  - txclk_tapnum: u8
  - reset: reset_control *
  - drive_impedance: unsigned int
  - hi_sys_regmap: regmap *
  - bus_clk: clk *
  - vendor_specific_area1: int
  - vendor_specific_area2: int
  - num_other_clks: int
  - other_clks: clk_bulk_data[]
  - dwcmshc_pdata: const struct dwcmshc_pltfm_data *
  - priv: void *
  - delay_line: u16
  - flags: u16
  - pdata: const struct sdhci_pltfm_data
  - cqhci_host_ops: const struct cqhci_host_ops *
  - init: int (*)(struct device * dev,struct sdhci_host * host,struct dwcmshc_priv * dwc_priv)
  - postinit: void (*)(struct sdhci_host * host,struct dwcmshc_priv * dwc_priv)
  - dwcmshc_pdata: dwcmshc_pltfm_data
  - is_emmc: bool
  - ctrl_reg: u32
  - vol_stable_bit: u32
  - write_prot_bit: u32
  - dwcmshc_pdata: dwcmshc_pltfm_data
  - revision: int

### rockchip_pltfm_data
- Line: 327
- Members:
  - reset: reset_control *
  - txclk_tapnum: u8
  - reset: reset_control *
  - drive_impedance: unsigned int
  - hi_sys_regmap: regmap *
  - bus_clk: clk *
  - vendor_specific_area1: int
  - vendor_specific_area2: int
  - num_other_clks: int
  - other_clks: clk_bulk_data[]
  - dwcmshc_pdata: const struct dwcmshc_pltfm_data *
  - priv: void *
  - delay_line: u16
  - flags: u16
  - pdata: const struct sdhci_pltfm_data
  - cqhci_host_ops: const struct cqhci_host_ops *
  - init: int (*)(struct device * dev,struct sdhci_host * host,struct dwcmshc_priv * dwc_priv)
  - postinit: void (*)(struct sdhci_host * host,struct dwcmshc_priv * dwc_priv)
  - dwcmshc_pdata: dwcmshc_pltfm_data
  - is_emmc: bool
  - ctrl_reg: u32
  - vol_stable_bit: u32
  - write_prot_bit: u32
  - dwcmshc_pdata: dwcmshc_pltfm_data
  - revision: int

## Variables (27)

- static **dwcmshc_cqhci_ops** : const struct cqhci_host_ops (line 2265)
- static **dwcmshc_pmops** : const struct dev_pm_ops (line 2636)
- static **k230_emmc_data** : const struct k230_pltfm_data (line 2216)
- static **k230_sdio_data** : const struct k230_pltfm_data (line 2231)
- static **rk35xx_cqhci_ops** : const struct cqhci_host_ops (line 2122)
- static **sdhci_dwcmshc_acpi_ids** : const struct acpi_device_id[] (line 2390)
- static **sdhci_dwcmshc_bf3_ops** : const struct sdhci_ops (line 2028)
- static **sdhci_dwcmshc_bf3_pdata** : const struct dwcmshc_pltfm_data (line 2112)
- static **sdhci_dwcmshc_cv18xx_ops** : const struct sdhci_ops (line 2061)
- static **sdhci_dwcmshc_cv18xx_pdata** : const struct dwcmshc_pltfm_data (line 2188)
- static **sdhci_dwcmshc_driver** : platform_driver (line 2641)
- static **sdhci_dwcmshc_dt_ids** : const struct of_device_id[] (line 2336)
- static **sdhci_dwcmshc_eic7700_ops** : const struct sdhci_ops (line 2081)
- static **sdhci_dwcmshc_eic7700_pdata** : const struct dwcmshc_pltfm_data (line 2205)
- static **sdhci_dwcmshc_hpe_gsc_pdata** : const struct dwcmshc_pltfm_data (line 2256)
- static **sdhci_dwcmshc_hpe_ops** : const struct sdhci_ops (line 2246)
- static **sdhci_dwcmshc_k230_ops** : const struct sdhci_ops (line 2094)
- static **sdhci_dwcmshc_ops** : const struct sdhci_ops (line 2007)
- static **sdhci_dwcmshc_pdata** : const struct dwcmshc_pltfm_data (line 2103)
- static **sdhci_dwcmshc_rk3568_pdata** : const struct rockchip_pltfm_data (line 2131)
- static **sdhci_dwcmshc_rk3576_pdata** : const struct rockchip_pltfm_data (line 2147)
- static **sdhci_dwcmshc_rk3588_pdata** : const struct rockchip_pltfm_data (line 2163)
- static **sdhci_dwcmshc_rk35xx_ops** : const struct sdhci_ops (line 2040)
- static **sdhci_dwcmshc_sg2042_ops** : const struct sdhci_ops (line 2071)
- static **sdhci_dwcmshc_sg2042_pdata** : const struct dwcmshc_pltfm_data (line 2196)
- static **sdhci_dwcmshc_th1520_ops** : const struct sdhci_ops (line 2050)
- static **sdhci_dwcmshc_th1520_pdata** : const struct dwcmshc_pltfm_data (line 2179)

## Macros (168)

- **AT_CTRL_AT_EN** (line 52)
- **AT_CTRL_CI_SEL** (line 53)
- **AT_CTRL_POST_CHANGE_DLY** (line 63)
- **AT_CTRL_POST_CHANGE_DLY_MASK** (line 62)
- **AT_CTRL_PRE_CHANGE_DLY** (line 61)
- **AT_CTRL_PRE_CHANGE_DLY_MASK** (line 60)
- **AT_CTRL_RPT_TUNE_ERR** (line 55)
- **AT_CTRL_SWIN_TH_EN** (line 54)
- **AT_CTRL_SWIN_TH_VAL** (line 65)
- **AT_CTRL_SWIN_TH_VAL_MASK** (line 64)
- **AT_CTRL_SW_TUNE_EN** (line 56)
- **AT_CTRL_TUNE_CLK_STOP_EN** (line 59)
- **AT_CTRL_WIN_EDGE_SEL** (line 58)
- **AT_CTRL_WIN_EDGE_SEL_MASK** (line 57)
- **BLUEFIELD_SMC_SET_EMMC_RST_N** (line 246)
- **BOUNDARY_OK**(addr,len) (line 235)
- **CV18XX_EMMC_FUNC_EN** (line 72)
- **CV18XX_LATANCY_1T** (line 73)
- **CV18XX_PHY_RX_DLY_MSK** (line 78)
- **CV18XX_PHY_RX_SRC_INVERT_RX_CLK** (line 80)
- **CV18XX_PHY_RX_SRC_MSK** (line 79)
- **CV18XX_PHY_TX_BPS** (line 82)
- **CV18XX_PHY_TX_DLY_MSK** (line 75)
- **CV18XX_PHY_TX_SRC_INVERT_CLK_TX** (line 77)
- **CV18XX_PHY_TX_SRC_MSK** (line 76)
- **CV18XX_RETRY_TUNING_MAX** (line 86)
- **CV18XX_SDHCI_MSHC_CTRL** (line 71)
- **CV18XX_SDHCI_PHY_CONFIG** (line 81)
- **CV18XX_SDHCI_PHY_TX_RX_DLY** (line 74)
- **CV18XX_TUNE_MAX** (line 84)
- **CV18XX_TUNE_STEP** (line 85)
- **DECMSHC_EMMC_DLL_CMDOUT** (line 93)
- **DECMSHC_EMMC_MISC_CON** (line 94)
- **DLL_CMDOUT_EN_SRC_CLK_NEG** (line 119)
- **DLL_CMDOUT_SRC_CLK_NEG** (line 118)
- **DLL_CMDOUT_TAPNUM_90_DEGREES** (line 115)
- **DLL_CMDOUT_TAPNUM_FROM_SW** (line 117)
- **DLL_ERROR_STS** (line 231)
- **DLL_LOCK_STS** (line 226)
- **DLL_LOCK_WO_TMOUT**(x) (line 121)
- **DLL_RXCLK_INVERTER** (line 114)
- **DLL_RXCLK_NO_INVERTER** (line 113)
- **DLL_RXCLK_ORI_GATE** (line 116)
- **DLL_STRBIN_DELAY_NUM_DEFAULT** (line 112)
- **DLL_STRBIN_DELAY_NUM_OFFSET** (line 111)
- **DLL_STRBIN_DELAY_NUM_SEL** (line 110)
- **DLL_STRBIN_TAPNUM_DEFAULT** (line 108)
- **DLL_STRBIN_TAPNUM_FROM_SW** (line 109)
- **DLL_TXCLK_TAPNUM_90_DEGREES** (line 106)
- **DLL_TXCLK_TAPNUM_DEFAULT** (line 105)
- **DLL_TXCLK_TAPNUM_FROM_SW** (line 107)
- **DWCMSHC_AREA1_MASK** (line 40)
- **DWCMSHC_AT_STAT** (line 50)
- **DWCMSHC_CARD_IS_EMMC** (line 47)
- **DWCMSHC_CTRL_HS400** (line 36)
- **DWCMSHC_EMMC_ATCTRL** (line 49)
- **DWCMSHC_EMMC_CONTROL** (line 44)
- **DWCMSHC_EMMC_DLL_BYPASS** (line 103)
- **DWCMSHC_EMMC_DLL_CTRL** (line 89)
- **DWCMSHC_EMMC_DLL_DLYENA** (line 104)
- **DWCMSHC_EMMC_DLL_INC** (line 102)
- **DWCMSHC_EMMC_DLL_LOCKED** (line 98)
- **DWCMSHC_EMMC_DLL_RXCLK** (line 90)
- **DWCMSHC_EMMC_DLL_RXCLK_SRCSEL** (line 100)
- **DWCMSHC_EMMC_DLL_START** (line 97)
- **DWCMSHC_EMMC_DLL_START_POINT** (line 101)
- **DWCMSHC_EMMC_DLL_STATUS0** (line 96)
- **DWCMSHC_EMMC_DLL_STRBIN** (line 92)
- **DWCMSHC_EMMC_DLL_TIMEOUT** (line 99)
- **DWCMSHC_EMMC_DLL_TXCLK** (line 91)
- **DWCMSHC_ENHANCED_STROBE** (line 48)
- **DWCMSHC_HOST_CTRL3** (line 42)
- **DWCMSHC_HOST_CTRL3_CMD_CONFLICT** (line 43)
- **DWCMSHC_MAX_OTHER_CLKS** (line 296)
- **DWCMSHC_P_VENDOR_AREA1** (line 39)
- **DWCMSHC_P_VENDOR_AREA2** (line 68)
- **DWCMSHC_SDHCI_CQE_TRNS_MODE** (line 238)
- **DWC_MSHC_PTR_PHY_R** (line 126)
- **EIC7700_CARD_CLK_STABLE** (line 257)
- **EIC7700_HOST_VAL_STABLE** (line 265)
- **EIC7700_INT_ACLK_STABLE** (line 259)
- **EIC7700_INT_BCLK_STABLE** (line 258)
- **EIC7700_INT_CLK_STABLE** (line 261)
- **EIC7700_INT_TMCLK_STABLE** (line 260)
- **FLAG_IO_FIXED_1V8** (line 233)
- **HPE_GSC_MSHCCS_SCGSYNCDIS** (line 46)
- **MAX_PHASE_CODE** (line 274)
- **MISC_INTCLK_EN** (line 95)
- **PHYCTRL_DR_100OHM** (line 272)
- **PHYCTRL_DR_33OHM** (line 268)
- **PHYCTRL_DR_40OHM** (line 269)
- **PHYCTRL_DR_50OHM** (line 270)
- **PHYCTRL_DR_66OHM** (line 271)
- **PHY_ATDL_CNFG_INPSEL** (line 197)
- **PHY_ATDL_CNFG_INPSEL_MASK** (line 196)
- **PHY_ATDL_CNFG_INPSEL_SG2042** (line 198)
- **PHY_ATDL_CNFG_R** (line 195)
- **PHY_CLKPAD_CNFG_R** (line 148)
- **PHY_CLK_MAX_DELAY_MASK** (line 276)
- **PHY_CMDPAD_CNFG_R** (line 142)
- **PHY_CNFG_PAD_SN** (line 137)
- **PHY_CNFG_PAD_SN_MASK** (line 136)
- **PHY_CNFG_PAD_SN_SG2042** (line 139)
- **PHY_CNFG_PAD_SN_k230** (line 138)
- **PHY_CNFG_PAD_SP** (line 133)
- **PHY_CNFG_PAD_SP_MASK** (line 132)
- **PHY_CNFG_PAD_SP_SG2042** (line 135)
- **PHY_CNFG_PAD_SP_k230** (line 134)
- **PHY_CNFG_PHY_PWRGOOD_MASK** (line 131)
- **PHY_CNFG_R** (line 129)
- **PHY_CNFG_RSTN_DEASSERT** (line 130)
- **PHY_COMMDL_CNFG** (line 174)
- **PHY_COMMDL_CNFG_DLSTEP_SEL** (line 175)
- **PHY_DATAPAD_CNFG_R** (line 145)
- **PHY_DELAY_CODE_EMMC** (line 278)
- **PHY_DELAY_CODE_MAX** (line 277)
- **PHY_DELAY_CODE_SD** (line 279)
- **PHY_DLLBT_CNFG_R** (line 223)
- **PHY_DLLDL_CNFG_R** (line 216)
- **PHY_DLLDL_CNFG_SLV_INPSEL** (line 218)
- **PHY_DLLDL_CNFG_SLV_INPSEL_MASK** (line 217)
- **PHY_DLL_CNFG1_R** (line 206)
- **PHY_DLL_CNFG1_SLVDLY** (line 208)
- **PHY_DLL_CNFG1_SLVDLY_MASK** (line 207)
- **PHY_DLL_CNFG1_WAITCYCLE** (line 209)
- **PHY_DLL_CNFG2_JUMPSTEP** (line 213)
- **PHY_DLL_CNFG2_R** (line 212)
- **PHY_DLL_CTRL_DISABLE** (line 202)
- **PHY_DLL_CTRL_ENABLE** (line 203)
- **PHY_DLL_CTRL_R** (line 201)
- **PHY_DLL_OFFST_R** (line 221)
- **PHY_DLL_STATUS_R** (line 225)
- **PHY_PAD_RXSEL_1V8** (line 157)
- **PHY_PAD_RXSEL_3V3** (line 158)
- **PHY_PAD_TXSLEW_CTRL_N** (line 169)
- **PHY_PAD_TXSLEW_CTRL_N_MASK** (line 168)
- **PHY_PAD_TXSLEW_CTRL_N_SG2042** (line 170)
- **PHY_PAD_TXSLEW_CTRL_N_k230** (line 171)
- **PHY_PAD_TXSLEW_CTRL_P** (line 166)
- **PHY_PAD_TXSLEW_CTRL_P_MASK** (line 165)
- **PHY_PAD_TXSLEW_CTRL_P_k230** (line 167)
- **PHY_PAD_WEAKPULL_DISABLED** (line 161)
- **PHY_PAD_WEAKPULL_MASK** (line 160)
- **PHY_PAD_WEAKPULL_PULLDOWN** (line 163)
- **PHY_PAD_WEAKPULL_PULLUP** (line 162)
- **PHY_RSTNPAD_CNFG_R** (line 154)
- **PHY_SDCLKDL_CNFG_EXTDLY_EN** (line 179)
- **PHY_SDCLKDL_CNFG_R** (line 178)
- **PHY_SDCLKDL_CNFG_UPDATE** (line 180)
- **PHY_SDCLKDL_DC_DEFAULT** (line 185)
- **PHY_SDCLKDL_DC_HS400** (line 186)
- **PHY_SDCLKDL_DC_INITIAL** (line 184)
- **PHY_SDCLKDL_DC_R** (line 183)
- **PHY_SMPLDL_CNFG_BYPASS_EN** (line 190)
- **PHY_SMPLDL_CNFG_EXTDLY_EN** (line 189)
- **PHY_SMPLDL_CNFG_INPSEL** (line 192)
- **PHY_SMPLDL_CNFG_INPSEL_MASK** (line 191)
- **PHY_SMPLDL_CNFG_R** (line 188)
- **PHY_STBPAD_CNFG_R** (line 151)
- **SD0_CARD_WRITE_PROT** (line 251)
- **SD0_CTRL** (line 249)
- **SD0_HOST_REG_VOL_STABLE** (line 250)
- **SD1_CARD_WRITE_PROT** (line 254)
- **SD1_CTRL** (line 252)
- **SD1_HOST_REG_VOL_STABLE** (line 253)
- **SDHCI_DWCMSHC_ARG2_STUFF** (line 33)
- **TUNING_RANGE_THRESHOLD** (line 275)
- **to_pltfm_data**(priv,name) (line 242)
