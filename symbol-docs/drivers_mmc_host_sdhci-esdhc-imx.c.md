# drivers/mmc/host/sdhci-esdhc-imx.c

Subsystem: drivers/mmc

## Functions (44)

### esdhc_change_pinstate
- Return type: static int
- Signature: esdhc_change_pinstate(struct sdhci_host * host,unsigned int uhs)
- Line: 1320

### esdhc_clrset_le
- Return type: static void
- Signature: esdhc_clrset_le(struct sdhci_host * host,u32 mask,u32 val,int reg)
- Line: 441

### esdhc_cqe_enable
- Return type: static void
- Signature: esdhc_cqe_enable(struct mmc_host * mmc)
- Line: 1737

### esdhc_cqhci_irq
- Return type: static u32
- Signature: esdhc_cqhci_irq(struct sdhci_host * host,u32 intmask)
- Line: 1498

### esdhc_dump_debug_regs
- Return type: static void
- Signature: esdhc_dump_debug_regs(struct sdhci_host * host)
- Line: 452

### esdhc_executing_tuning
- Return type: static int
- Signature: esdhc_executing_tuning(struct sdhci_host * host,u32 opcode)
- Line: 1230

### esdhc_get_max_timeout_count
- Return type: static unsigned int
- Signature: esdhc_get_max_timeout_count(struct sdhci_host * host)
- Line: 1489

### esdhc_hs400_enhanced_strobe
- Return type: static void
- Signature: esdhc_hs400_enhanced_strobe(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 1307

### esdhc_hw_reset
- Return type: static void
- Signature: esdhc_hw_reset(struct sdhci_host * host)
- Line: 1511

### esdhc_is_usdhc
- Return type: static int
- Signature: esdhc_is_usdhc(struct pltfm_imx_data * data)
- Line: 436

### esdhc_pltfm_get_max_clock
- Return type: static unsigned int
- Signature: esdhc_pltfm_get_max_clock(struct sdhci_host * host)
- Line: 952

### esdhc_pltfm_get_min_clock
- Return type: static unsigned int
- Signature: esdhc_pltfm_get_min_clock(struct sdhci_host * host)
- Line: 959

### esdhc_pltfm_get_ro
- Return type: static unsigned int
- Signature: esdhc_pltfm_get_ro(struct sdhci_host * host)
- Line: 1052

### esdhc_pltfm_set_bus_width
- Return type: static void
- Signature: esdhc_pltfm_set_bus_width(struct sdhci_host * host,int width)
- Line: 1071

### esdhc_pltfm_set_clock
- Return type: static void
- Signature: esdhc_pltfm_set_clock(struct sdhci_host * host,unsigned int clock)
- Line: 966

### esdhc_post_tuning
- Return type: static void
- Signature: esdhc_post_tuning(struct sdhci_host * host)
- Line: 1217

### esdhc_prepare_tuning
- Return type: static void
- Signature: esdhc_prepare_tuning(struct sdhci_host * host,u32 val)
- Line: 1180

### esdhc_readb_le
- Return type: static u8
- Signature: esdhc_readb_le(struct sdhci_host * host,int reg)
- Line: 849

### esdhc_readl_le
- Return type: static u32
- Signature: esdhc_readl_le(struct sdhci_host * host,int reg)
- Line: 533

### esdhc_readw_le
- Return type: static u16
- Signature: esdhc_readw_le(struct sdhci_host * host,int reg)
- Line: 670

### esdhc_reset
- Return type: static void
- Signature: esdhc_reset(struct sdhci_host * host,u8 mask)
- Line: 1465

### esdhc_reset_tuning
- Return type: static void
- Signature: esdhc_reset_tuning(struct sdhci_host * host)
- Line: 1091

### esdhc_sdhci_dumpregs
- Return type: static void
- Signature: esdhc_sdhci_dumpregs(struct mmc_host * mmc)
- Line: 1788

### esdhc_set_strobe_dll
- Return type: static void
- Signature: esdhc_set_strobe_dll(struct sdhci_host * host)
- Line: 1361

### esdhc_set_uhs_signaling
- Return type: static void
- Signature: esdhc_set_uhs_signaling(struct sdhci_host * host,unsigned timing)
- Line: 1402

### esdhc_wait_for_card_clock_gate_off
- Return type: static void
- Signature: esdhc_wait_for_card_clock_gate_off(struct sdhci_host * host)
- Line: 477

### esdhc_writeb_le
- Return type: static void
- Signature: esdhc_writeb_le(struct sdhci_host * host,u8 val,int reg)
- Line: 868

### esdhc_writel_le
- Return type: static void
- Signature: esdhc_writel_le(struct sdhci_host * host,u32 val,int reg)
- Line: 619

### esdhc_writew_le
- Return type: static void
- Signature: esdhc_writew_le(struct sdhci_host * host,u16 val,int reg)
- Line: 730

### is_imx25_esdhc
- Return type: static int
- Signature: is_imx25_esdhc(struct pltfm_imx_data * data)
- Line: 426

### is_imx53_esdhc
- Return type: static int
- Signature: is_imx53_esdhc(struct pltfm_imx_data * data)
- Line: 431

### sdhc_esdhc_tuning_restore
- Return type: static void
- Signature: sdhc_esdhc_tuning_restore(struct sdhci_host * host)
- Line: 1702

### sdhc_esdhc_tuning_save
- Return type: static void
- Signature: sdhc_esdhc_tuning_save(struct sdhci_host * host)
- Line: 1680

### sdhci_esdhc_imx_hwinit
- Return type: static void
- Signature: sdhci_esdhc_imx_hwinit(struct sdhci_host * host)
- Line: 1550

### sdhci_esdhc_imx_probe
- Return type: static int
- Signature: sdhci_esdhc_imx_probe(struct platform_device * pdev)
- Line: 1851

### sdhci_esdhc_imx_probe_dt
- Return type: static int
- Signature: sdhci_esdhc_imx_probe_dt(struct platform_device * pdev,struct sdhci_host * host,struct pltfm_imx_data * imx_data)
- Line: 1800

### sdhci_esdhc_imx_remove
- Return type: static void
- Signature: sdhci_esdhc_imx_remove(struct platform_device * pdev)
- Line: 2018

### sdhci_esdhc_resume
- Return type: static int
- Signature: sdhci_esdhc_resume(struct device * dev)
- Line: 2102

### sdhci_esdhc_runtime_resume
- Return type: static int
- Signature: sdhci_esdhc_runtime_resume(struct device * dev)
- Line: 2166

### sdhci_esdhc_runtime_suspend
- Return type: static int
- Signature: sdhci_esdhc_runtime_suspend(struct device * dev)
- Line: 2136

### sdhci_esdhc_suspend
- Return type: static int
- Signature: sdhci_esdhc_suspend(struct device * dev)
- Line: 2040

### usdhc_auto_tuning_mode_sel_and_en
- Return type: static void
- Signature: usdhc_auto_tuning_mode_sel_and_en(struct sdhci_host * host)
- Line: 489

### usdhc_execute_tuning
- Return type: static int
- Signature: usdhc_execute_tuning(struct mmc_host * mmc,u32 opcode)
- Line: 1154

### usdhc_init_card
- Return type: static void
- Signature: usdhc_init_card(struct mmc_host * mmc,struct mmc_card * card)
- Line: 1145

## Structs (3)

### esdhc_platform_data
- Line: 244
- Members:
  - wp_type: wp_types
  - cd_type: cd_types
  - max_bus_width: int
  - delay_line: unsigned int
  - tuning_step: unsigned int
  - tuning_start_tap: unsigned int
  - strobe_dll_delay_target: unsigned int
  - saved_tuning_delay_cell: unsigned int
  - saved_auto_tuning_window: unsigned int
  - flags: u32
  - quirks: u32
  - scratchpad: u32
  - pinctrl: pinctrl *
  - pins_100mhz: pinctrl_state *
  - pins_200mhz: pinctrl_state *
  - socdata: const struct esdhc_soc_data *
  - boarddata: esdhc_platform_data
  - clk_ipg: clk *
  - clk_ahb: clk *
  - clk_per: clk *
  - actual_clock: unsigned int
  - init_card_type: unsigned int
  - multiblock_status: pltfm_imx_data::__anon901222a10103
  - is_ddr: u32
  - pm_qos_req: pm_qos_request

### esdhc_soc_data
- Line: 256
- Members:
  - wp_type: wp_types
  - cd_type: cd_types
  - max_bus_width: int
  - delay_line: unsigned int
  - tuning_step: unsigned int
  - tuning_start_tap: unsigned int
  - strobe_dll_delay_target: unsigned int
  - saved_tuning_delay_cell: unsigned int
  - saved_auto_tuning_window: unsigned int
  - flags: u32
  - quirks: u32
  - scratchpad: u32
  - pinctrl: pinctrl *
  - pins_100mhz: pinctrl_state *
  - pins_200mhz: pinctrl_state *
  - socdata: const struct esdhc_soc_data *
  - boarddata: esdhc_platform_data
  - clk_ipg: clk *
  - clk_ahb: clk *
  - clk_per: clk *
  - actual_clock: unsigned int
  - init_card_type: unsigned int
  - multiblock_status: pltfm_imx_data::__anon901222a10103
  - is_ddr: u32
  - pm_qos_req: pm_qos_request

### pltfm_imx_data
- Line: 373
- Members:
  - wp_type: wp_types
  - cd_type: cd_types
  - max_bus_width: int
  - delay_line: unsigned int
  - tuning_step: unsigned int
  - tuning_start_tap: unsigned int
  - strobe_dll_delay_target: unsigned int
  - saved_tuning_delay_cell: unsigned int
  - saved_auto_tuning_window: unsigned int
  - flags: u32
  - quirks: u32
  - scratchpad: u32
  - pinctrl: pinctrl *
  - pins_100mhz: pinctrl_state *
  - pins_200mhz: pinctrl_state *
  - socdata: const struct esdhc_soc_data *
  - boarddata: esdhc_platform_data
  - clk_ipg: clk *
  - clk_ahb: clk *
  - clk_per: clk *
  - actual_clock: unsigned int
  - init_card_type: unsigned int
  - multiblock_status: pltfm_imx_data::__anon901222a10103
  - is_ddr: u32
  - pm_qos_req: pm_qos_request

## Enums (3)

### __anon901222a10103
- Line: 394

### cd_types
- Line: 228

### wp_types
- Line: 222

## Variables (23)

- static **esdhc_cqhci_ops** : const struct cqhci_host_ops (line 1793)
- static **esdhc_imx25_data** : const struct esdhc_soc_data (line 261)
- static **esdhc_imx35_data** : const struct esdhc_soc_data (line 265)
- static **esdhc_imx51_data** : const struct esdhc_soc_data (line 269)
- static **esdhc_imx53_data** : const struct esdhc_soc_data (line 273)
- static **imx_esdhc_dt_ids** : const struct of_device_id[] (line 403)
- static **sdhci_esdhc_imx_driver** : platform_driver (line 2215)
- static **sdhci_esdhc_imx_pdata** : const struct sdhci_pltfm_data (line 1542)
- static **sdhci_esdhc_ops** : sdhci_ops (line 1522)
- static **sdhci_esdhc_pmops** : const struct dev_pm_ops (line 2210)
- static **usdhc_imx6q_data** : const struct esdhc_soc_data (line 277)
- static **usdhc_imx6sl_data** : const struct esdhc_soc_data (line 282)
- static **usdhc_imx6sll_data** : const struct esdhc_soc_data (line 289)
- static **usdhc_imx6sx_data** : const struct esdhc_soc_data (line 296)
- static **usdhc_imx6ull_data** : const struct esdhc_soc_data (line 303)
- static **usdhc_imx7d_data** : const struct esdhc_soc_data (line 310)
- static **usdhc_imx7ulp_data** : esdhc_soc_data (line 334)
- static **usdhc_imx8mm_data** : esdhc_soc_data (line 356)
- static **usdhc_imx8qxp_data** : esdhc_soc_data (line 347)
- static **usdhc_imx95_data** : esdhc_soc_data (line 364)
- static **usdhc_imxrt1050_data** : esdhc_soc_data (line 341)
- static **usdhc_s32g2_data** : esdhc_soc_data (line 318)
- static **usdhc_s32n79_data** : esdhc_soc_data (line 326)

## Macros (106)

- **DRIVER_NAME** (line 449)
- **ESDHC_AUTO_TUNING_WINDOW** (line 218)
- **ESDHC_BURST_LEN_EN_INCR** (line 38)
- **ESDHC_CQHCI_ADDR_OFFSET** (line 143)
- **ESDHC_CTRL_4BITBUS** (line 129)
- **ESDHC_CTRL_8BITBUS** (line 130)
- **ESDHC_CTRL_BUSWIDTH_MASK** (line 131)
- **ESDHC_CTRL_D3CD** (line 37)
- **ESDHC_DATA_INHIBIT_WAIT_US** (line 220)
- **ESDHC_DEBUG_SEL_ADMA_STATE** (line 51)
- **ESDHC_DEBUG_SEL_AND_STATUS_REG** (line 44)
- **ESDHC_DEBUG_SEL_ASYNC_FIFO_STATE** (line 53)
- **ESDHC_DEBUG_SEL_CMD_STATE** (line 47)
- **ESDHC_DEBUG_SEL_DATA_STATE** (line 48)
- **ESDHC_DEBUG_SEL_DMA_STATE** (line 50)
- **ESDHC_DEBUG_SEL_FIFO_STATE** (line 52)
- **ESDHC_DEBUG_SEL_MASK** (line 46)
- **ESDHC_DEBUG_SEL_REG** (line 45)
- **ESDHC_DEBUG_SEL_TRANS_STATE** (line 49)
- **ESDHC_DLL_CTRL** (line 77)
- **ESDHC_DLL_OVERRIDE_EN_SHIFT** (line 79)
- **ESDHC_DLL_OVERRIDE_VAL_SHIFT** (line 78)
- **ESDHC_FLAG_BROKEN_AUTO_CMD23** (line 207)
- **ESDHC_FLAG_CLK_RATE_LOST_IN_PM_RUNTIME** (line 195)
- **ESDHC_FLAG_CQHCI** (line 189)
- **ESDHC_FLAG_DUMMY_PAD** (line 216)
- **ESDHC_FLAG_ERR004536** (line 175)
- **ESDHC_FLAG_ERR010450** (line 185)
- **ESDHC_FLAG_HAVE_CAP1** (line 167)
- **ESDHC_FLAG_HS200** (line 177)
- **ESDHC_FLAG_HS400** (line 179)
- **ESDHC_FLAG_HS400_ES** (line 187)
- **ESDHC_FLAG_MAN_TUNING** (line 163)
- **ESDHC_FLAG_MULTIBLK_NO_INT** (line 156)
- **ESDHC_FLAG_PMQOS** (line 191)
- **ESDHC_FLAG_SKIP_CD_WAKE** (line 213)
- **ESDHC_FLAG_SKIP_ERR004536** (line 210)
- **ESDHC_FLAG_STATE_LOST_IN_LPMODE** (line 193)
- **ESDHC_FLAG_STD_TUNING** (line 165)
- **ESDHC_FLAG_USDHC** (line 161)
- **ESDHC_IMX_DUMP**(f,x...) (line 450)
- **ESDHC_INT_VENDOR_SPEC_DMA_ERR** (line 140)
- **ESDHC_MIX_CTRL** (line 62)
- **ESDHC_MIX_CTRL_AC23EN** (line 64)
- **ESDHC_MIX_CTRL_AUTO_TUNE_EN** (line 67)
- **ESDHC_MIX_CTRL_DDREN** (line 63)
- **ESDHC_MIX_CTRL_EXE_TUNE** (line 65)
- **ESDHC_MIX_CTRL_FBCLK_SEL** (line 68)
- **ESDHC_MIX_CTRL_HS400_EN** (line 69)
- **ESDHC_MIX_CTRL_HS400_ES_EN** (line 70)
- **ESDHC_MIX_CTRL_SDHCI_MASK** (line 72)
- **ESDHC_MIX_CTRL_SMPCLK_SEL** (line 66)
- **ESDHC_MIX_CTRL_TUNING_MASK** (line 74)
- **ESDHC_PINCTRL_STATE_100MHZ** (line 123)
- **ESDHC_PINCTRL_STATE_200MHZ** (line 124)
- **ESDHC_STD_TUNING_EN** (line 112)
- **ESDHC_STROBE_DLL_CTRL** (line 92)
- **ESDHC_STROBE_DLL_CTRL_ENABLE** (line 93)
- **ESDHC_STROBE_DLL_CTRL_RESET** (line 94)
- **ESDHC_STROBE_DLL_CTRL_SLV_DLY_TARGET_DEFAULT** (line 95)
- **ESDHC_STROBE_DLL_CTRL_SLV_DLY_TARGET_SHIFT** (line 96)
- **ESDHC_STROBE_DLL_CTRL_SLV_UPDATE_INT_DEFAULT** (line 97)
- **ESDHC_STROBE_DLL_STATUS** (line 99)
- **ESDHC_STROBE_DLL_STS_REF_LOCK** (line 100)
- **ESDHC_STROBE_DLL_STS_SLV_LOCK** (line 101)
- **ESDHC_SYS_CTRL_DTOCV_MASK** (line 33)
- **ESDHC_SYS_CTRL_IPP_RST_N** (line 35)
- **ESDHC_SYS_CTRL_RESET_TUNING** (line 36)
- **ESDHC_SYS_CTRL_RST_FIFO** (line 34)
- **ESDHC_TUNE_CTRL_MAX** (line 85)
- **ESDHC_TUNE_CTRL_MIN** (line 84)
- **ESDHC_TUNE_CTRL_STATUS** (line 82)
- **ESDHC_TUNE_CTRL_STATUS_DLY_CELL_SET_OUT_MASK** (line 89)
- **ESDHC_TUNE_CTRL_STATUS_DLY_CELL_SET_POST_MASK** (line 90)
- **ESDHC_TUNE_CTRL_STATUS_DLY_CELL_SET_PRE_MASK** (line 88)
- **ESDHC_TUNE_CTRL_STATUS_TAP_SEL_MASK** (line 86)
- **ESDHC_TUNE_CTRL_STATUS_TAP_SEL_PRE_MASK** (line 87)
- **ESDHC_TUNE_CTRL_STEP** (line 83)
- **ESDHC_TUNING_CMD_CRC_CHECK_DISABLE** (line 117)
- **ESDHC_TUNING_CTRL** (line 111)
- **ESDHC_TUNING_START_TAP_DEFAULT** (line 115)
- **ESDHC_TUNING_START_TAP_MASK** (line 116)
- **ESDHC_TUNING_STEP_DEFAULT** (line 118)
- **ESDHC_TUNING_STEP_MASK** (line 119)
- **ESDHC_TUNING_STEP_SHIFT** (line 120)
- **ESDHC_TUNING_WINDOW_MASK** (line 113)
- **ESDHC_VENDOR_SPEC** (line 40)
- **ESDHC_VENDOR_SPEC_FRC_SDCLK_ON** (line 43)
- **ESDHC_VENDOR_SPEC_SDIO_QUIRK** (line 41)
- **ESDHC_VENDOR_SPEC_VSELECT** (line 42)
- **ESDHC_VEND_SPEC2** (line 103)
- **ESDHC_VEND_SPEC2_AUTO_TUNE_1BIT_EN** (line 107)
- **ESDHC_VEND_SPEC2_AUTO_TUNE_4BIT_EN** (line 106)
- **ESDHC_VEND_SPEC2_AUTO_TUNE_8BIT_EN** (line 105)
- **ESDHC_VEND_SPEC2_AUTO_TUNE_CMD_EN** (line 108)
- **ESDHC_VEND_SPEC2_AUTO_TUNE_MODE_MASK** (line 109)
- **ESDHC_VEND_SPEC2_EN_BUSY_IRQ** (line 104)
- **ESDHC_WTMK_DEFAULT_VAL** (line 55)
- **ESDHC_WTMK_LVL** (line 54)
- **ESDHC_WTMK_LVL_RD_WML_MASK** (line 56)
- **ESDHC_WTMK_LVL_RD_WML_SHIFT** (line 57)
- **ESDHC_WTMK_LVL_WML_VAL_DEF** (line 60)
- **ESDHC_WTMK_LVL_WML_VAL_MAX** (line 61)
- **ESDHC_WTMK_LVL_WR_WML_MASK** (line 58)
- **ESDHC_WTMK_LVL_WR_WML_SHIFT** (line 59)
- **USDHC_GET_BUSWIDTH**(c) (line 132)
