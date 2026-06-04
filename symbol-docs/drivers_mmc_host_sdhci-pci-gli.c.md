# drivers/mmc/host/sdhci-pci-gli.c

Subsystem: drivers/mmc

## Functions (81)

### __gl9767_uhs2_set_power
- Return type: static void
- Signature: __gl9767_uhs2_set_power(struct sdhci_host * host,unsigned char mode,unsigned short vdd)
- Line: 1218

### __sdhci_execute_tuning_9750
- Return type: static int
- Signature: __sdhci_execute_tuning_9750(struct sdhci_host * host,u32 opcode)
- Line: 463

### gl9750_disable_ssc_pll
- Return type: static void
- Signature: gl9750_disable_ssc_pll(struct sdhci_host * host)
- Line: 516

### gl9750_execute_tuning
- Return type: static int
- Signature: gl9750_execute_tuning(struct sdhci_host * host,u32 opcode)
- Line: 503

### gl9750_hw_setting
- Return type: static void
- Signature: gl9750_hw_setting(struct sdhci_host * host)
- Line: 631

### gl9750_set_pll
- Return type: static void
- Signature: gl9750_set_pll(struct sdhci_host * host,u8 dir,u16 ldiv,u8 pdiv)
- Line: 527

### gl9750_set_ssc
- Return type: static void
- Signature: gl9750_set_ssc(struct sdhci_host * host,u8 enable,u8 step,u16 ppm)
- Line: 559

### gl9750_set_ssc_pll_100mhz
- Return type: static void
- Signature: gl9750_set_ssc_pll_100mhz(struct sdhci_host * host)
- Line: 587

### gl9750_set_ssc_pll_205mhz
- Return type: static void
- Signature: gl9750_set_ssc_pll_205mhz(struct sdhci_host * host)
- Line: 578

### gl9750_set_ssc_pll_50mhz
- Return type: static void
- Signature: gl9750_set_ssc_pll_50mhz(struct sdhci_host * host)
- Line: 596

### gl9750_ssc_enable
- Return type: static bool
- Signature: gl9750_ssc_enable(struct sdhci_host * host)
- Line: 546

### gl9750_wt_off
- Return type: static void
- Signature: gl9750_wt_off(struct sdhci_host * host)
- Line: 326

### gl9750_wt_on
- Return type: static void
- Signature: gl9750_wt_on(struct sdhci_host * host)
- Line: 309

### gl9755_disable_ssc_pll
- Return type: static void
- Signature: gl9755_disable_ssc_pll(struct pci_dev * pdev)
- Line: 707

### gl9755_hw_setting
- Return type: static void
- Signature: gl9755_hw_setting(struct sdhci_pci_slot * slot)
- Line: 825

### gl9755_set_pll
- Return type: static void
- Signature: gl9755_set_pll(struct pci_dev * pdev,u8 dir,u16 ldiv,u8 pdiv)
- Line: 718

### gl9755_set_power
- Return type: static void
- Signature: gl9755_set_power(struct sdhci_host * host,unsigned char mode,unsigned short vdd)
- Line: 952

### gl9755_set_ssc
- Return type: static void
- Signature: gl9755_set_ssc(struct pci_dev * pdev,u8 enable,u8 step,u16 ppm)
- Line: 750

### gl9755_set_ssc_pll_100mhz
- Return type: static void
- Signature: gl9755_set_ssc_pll_100mhz(struct pci_dev * pdev)
- Line: 778

### gl9755_set_ssc_pll_205mhz
- Return type: static void
- Signature: gl9755_set_ssc_pll_205mhz(struct pci_dev * pdev)
- Line: 769

### gl9755_set_ssc_pll_50mhz
- Return type: static void
- Signature: gl9755_set_ssc_pll_50mhz(struct pci_dev * pdev)
- Line: 787

### gl9755_ssc_enable
- Return type: static bool
- Signature: gl9755_ssc_enable(struct pci_dev * pdev)
- Line: 737

### gl9755_vendor_init
- Return type: static void
- Signature: gl9755_vendor_init(struct sdhci_host * host)
- Line: 867

### gl9755_wt_off
- Return type: static void
- Signature: gl9755_wt_off(struct pci_dev * pdev)
- Line: 690

### gl9755_wt_on
- Return type: static void
- Signature: gl9755_wt_on(struct pci_dev * pdev)
- Line: 673

### gl9763e_add_host
- Return type: static int
- Signature: gl9763e_add_host(struct sdhci_pci_slot * slot)
- Line: 1788

### gl9763e_hs400_enhanced_strobe
- Return type: static void
- Signature: gl9763e_hs400_enhanced_strobe(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 1672

### gl9763e_hw_setting
- Return type: static void
- Signature: gl9763e_hw_setting(struct sdhci_pci_slot * slot)
- Line: 1831

### gl9763e_resume
- Return type: static int
- Signature: gl9763e_resume(struct sdhci_pci_chip * chip)
- Line: 1930

### gl9763e_runtime_resume
- Return type: static int
- Signature: gl9763e_runtime_resume(struct sdhci_pci_chip * chip)
- Line: 1886

### gl9763e_runtime_suspend
- Return type: static int
- Signature: gl9763e_runtime_suspend(struct sdhci_pci_chip * chip)
- Line: 1870

### gl9763e_set_low_power_negotiation
- Return type: static void
- Signature: gl9763e_set_low_power_negotiation(struct sdhci_pci_slot * slot,bool enable)
- Line: 1687

### gl9763e_suspend
- Return type: static int
- Signature: gl9763e_suspend(struct sdhci_pci_chip * chip)
- Line: 1952

### gl9767_disable_ssc_pll
- Return type: static void
- Signature: gl9767_disable_ssc_pll(struct pci_dev * pdev)
- Line: 1164

### gl9767_hw_setting
- Return type: static void
- Signature: gl9767_hw_setting(struct sdhci_pci_slot * slot)
- Line: 1326

### gl9767_init_sd_express
- Return type: static int
- Signature: gl9767_init_sd_express(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 1402

### gl9767_set_low_power_negotiation
- Return type: static void
- Signature: gl9767_set_low_power_negotiation(struct pci_dev * pdev,bool enable)
- Line: 1177

### gl9767_set_pll
- Return type: static void
- Signature: gl9767_set_pll(struct pci_dev * pdev,u8 dir,u16 ldiv,u8 pdiv)
- Line: 1134

### gl9767_set_ssc
- Return type: static void
- Signature: gl9767_set_ssc(struct pci_dev * pdev,u8 enable,u8 step,u16 ppm)
- Line: 1113

### gl9767_set_ssc_pll_205mhz
- Return type: static void
- Signature: gl9767_set_ssc_pll_205mhz(struct pci_dev * pdev)
- Line: 1155

### gl9767_ssc_enable
- Return type: static bool
- Signature: gl9767_ssc_enable(struct pci_dev * pdev)
- Line: 1098

### gl9767_vendor_init
- Return type: static void
- Signature: gl9767_vendor_init(struct sdhci_host * host)
- Line: 1492

### gl9767_vhs_read
- Return type: static void
- Signature: gl9767_vhs_read(struct pci_dev * pdev)
- Line: 1064

### gl9767_vhs_write
- Return type: static void
- Signature: gl9767_vhs_write(struct pci_dev * pdev)
- Line: 1081

### gli_pcie_enable_msi
- Return type: static void
- Signature: gli_pcie_enable_msi(struct sdhci_pci_slot * slot)
- Line: 658

### gli_probe_slot_gl9750
- Return type: static int
- Signature: gli_probe_slot_gl9750(struct sdhci_pci_slot * slot)
- Line: 1572

### gli_probe_slot_gl9755
- Return type: static int
- Signature: gli_probe_slot_gl9755(struct sdhci_pci_slot * slot)
- Line: 1584

### gli_probe_slot_gl9763e
- Return type: static int
- Signature: gli_probe_slot_gl9763e(struct sdhci_pci_slot * slot)
- Line: 1983

### gli_probe_slot_gl9767
- Return type: static int
- Signature: gli_probe_slot_gl9767(struct sdhci_pci_slot * slot)
- Line: 1597

### gli_set_9750
- Return type: static void
- Signature: gli_set_9750(struct sdhci_host * host)
- Line: 343

### gli_set_9750_rx_inv
- Return type: static void
- Signature: gli_set_9750_rx_inv(struct sdhci_host * host,bool b)
- Line: 443

### gli_set_9767
- Return type: static void
- Signature: gli_set_9767(struct sdhci_host * host)
- Line: 1311

### sdhci_gl9750_readl
- Return type: static u32
- Signature: sdhci_gl9750_readl(struct sdhci_host * host,int reg)
- Line: 1661

### sdhci_gl9750_reset
- Return type: static void
- Signature: sdhci_gl9750_reset(struct sdhci_host * host,u8 mask)
- Line: 1655

### sdhci_gl9750_set_clock
- Return type: static void
- Signature: sdhci_gl9750_set_clock(struct sdhci_host * host,unsigned int clock)
- Line: 605

### sdhci_gl9755_reset
- Return type: static void
- Signature: sdhci_gl9755_reset(struct sdhci_host * host,u8 mask)
- Line: 1046

### sdhci_gl9755_set_clock
- Return type: static void
- Signature: sdhci_gl9755_set_clock(struct sdhci_host * host,unsigned int clock)
- Line: 796

### sdhci_gl9763e_cqe_enable
- Return type: static void
- Signature: sdhci_gl9763e_cqe_enable(struct mmc_host * mmc)
- Line: 1747

### sdhci_gl9763e_cqe_post_disable
- Return type: static void
- Signature: sdhci_gl9763e_cqe_post_disable(struct mmc_host * mmc)
- Line: 1768

### sdhci_gl9763e_cqe_pre_enable
- Return type: static void
- Signature: sdhci_gl9763e_cqe_pre_enable(struct mmc_host * mmc)
- Line: 1737

### sdhci_gl9763e_cqhci_irq
- Return type: static u32
- Signature: sdhci_gl9763e_cqhci_irq(struct sdhci_host * host,u32 intmask)
- Line: 1755

### sdhci_gl9763e_dumpregs
- Return type: static void
- Signature: sdhci_gl9763e_dumpregs(struct mmc_host * mmc)
- Line: 1732

### sdhci_gl9767_card_event
- Return type: static void
- Signature: sdhci_gl9767_card_event(struct sdhci_host * host)
- Line: 1306

### sdhci_gl9767_reset
- Return type: static void
- Signature: sdhci_gl9767_reset(struct sdhci_host * host,u8 mask)
- Line: 1360

### sdhci_gl9767_set_card_detect_debounce_time
- Return type: static void
- Signature: sdhci_gl9767_set_card_detect_debounce_time(struct sdhci_host * host)
- Line: 1286

### sdhci_gl9767_set_clock
- Return type: static void
- Signature: sdhci_gl9767_set_clock(struct sdhci_host * host,unsigned int clock)
- Line: 1252

### sdhci_gl9767_set_power
- Return type: static void
- Signature: sdhci_gl9767_set_power(struct sdhci_host * host,unsigned char mode,unsigned short vdd)
- Line: 1537

### sdhci_gl9767_uhs2_phy_reset
- Return type: static void
- Signature: sdhci_gl9767_uhs2_phy_reset(struct sdhci_host * host,bool assert)
- Line: 1193

### sdhci_gl9767_voltage_switch
- Return type: static void
- Signature: sdhci_gl9767_voltage_switch(struct sdhci_host * host)
- Line: 1636

### sdhci_gli_enable_internal_clock
- Return type: static void
- Signature: sdhci_gli_enable_internal_clock(struct sdhci_host * host)
- Line: 1001

### sdhci_gli_mask_replay_timer_timeout
- Return type: static void
- Signature: sdhci_gli_mask_replay_timer_timeout(struct pci_dev * pdev)
- Line: 295

### sdhci_gli_overcurrent_event_enable
- Return type: static void
- Signature: sdhci_gli_overcurrent_event_enable(struct sdhci_host * host,bool enable)
- Line: 931

### sdhci_gli_pre_detect_init
- Return type: static void
- Signature: sdhci_gli_pre_detect_init(struct sdhci_host * host)
- Line: 925

### sdhci_gli_readb
- Return type: static u8
- Signature: sdhci_gli_readb(struct sdhci_host * host,int reg)
- Line: 2023

### sdhci_gli_readw
- Return type: static u16
- Signature: sdhci_gli_readw(struct sdhci_host * host,int reg)
- Line: 2014

### sdhci_gli_uhs2_reset_sd_tran
- Return type: static void
- Signature: sdhci_gli_uhs2_reset_sd_tran(struct sdhci_host * host)
- Line: 1033

### sdhci_gli_voltage_switch
- Return type: static void
- Signature: sdhci_gli_voltage_switch(struct sdhci_host * host)
- Line: 1613

### sdhci_gli_wait_software_reset_done
- Return type: static int
- Signature: sdhci_gli_wait_software_reset_done(struct sdhci_host * host,u8 mask)
- Line: 1016

### sdhci_pci_gli_resume
- Return type: static int
- Signature: sdhci_pci_gli_resume(struct sdhci_pci_chip * chip)
- Line: 1920

### sdhci_set_gl9763e_signaling
- Return type: static void
- Signature: sdhci_set_gl9763e_signaling(struct sdhci_host * host,unsigned int timing)
- Line: 1713

### sdhci_wait_clock_stable
- Return type: static bool
- Signature: sdhci_wait_clock_stable(struct sdhci_host * host)
- Line: 988

## Variables (9)

- **sdhci_gl9750** : const struct sdhci_pci_fixes (line 2072)
- static **sdhci_gl9750_ops** : const struct sdhci_ops (line 2059)
- **sdhci_gl9755** : const struct sdhci_pci_fixes (line 2047)
- static **sdhci_gl9755_ops** : const struct sdhci_ops (line 2031)
- **sdhci_gl9763e** : const struct sdhci_pci_fixes (line 2092)
- static **sdhci_gl9763e_cqhci_ops** : const struct cqhci_host_ops (line 1780)
- static **sdhci_gl9763e_ops** : const struct sdhci_ops (line 2082)
- **sdhci_gl9767** : const struct sdhci_pci_fixes (line 2123)
- static **sdhci_gl9767_ops** : const struct sdhci_ops (line 2108)

## Macros (221)

- **GLI_9750_CFG2_L1DLY_VALUE** (line 31)
- **GLI_9750_DRIVING_1_VALUE** (line 36)
- **GLI_9750_DRIVING_2_VALUE** (line 37)
- **GLI_9750_MISC_RX_INV_OFF** (line 66)
- **GLI_9750_MISC_RX_INV_ON** (line 65)
- **GLI_9750_MISC_RX_INV_VALUE** (line 67)
- **GLI_9750_MISC_TX1_DLY_VALUE** (line 68)
- **GLI_9750_MISC_TX1_INV_VALUE** (line 64)
- **GLI_9750_PLL_TX2_DLY_VALUE** (line 49)
- **GLI_9750_PLL_TX2_INV_VALUE** (line 48)
- **GLI_9750_SW_CTRL_4_VALUE** (line 58)
- **GLI_9750_TUNING_CONTROL_EN_OFF** (line 77)
- **GLI_9750_TUNING_CONTROL_EN_ON** (line 76)
- **GLI_9750_TUNING_CONTROL_GLITCH_1_VALUE** (line 80)
- **GLI_9750_TUNING_CONTROL_GLITCH_2_VALUE** (line 81)
- **GLI_9750_TUNING_PARAMETERS_RX_DLY_VALUE** (line 85)
- **GLI_9750_WT_EN_OFF** (line 27)
- **GLI_9750_WT_EN_ON** (line 26)
- **GLI_9755_CFG2_L1DLY_VALUE** (line 135)
- **GLI_9755_PLLSSC_RECV_VALUE** (line 151)
- **GLI_9755_PLLSSC_RTL_VALUE** (line 147)
- **GLI_9755_PLLSSC_TRANS_PASS_VALUE** (line 149)
- **GLI_9755_PLLSSC_TRAN_VALUE** (line 153)
- **GLI_9755_UHS2_PLL_DELAY_VALUE** (line 159)
- **GLI_9755_UHS2_PLL_PDRST_VALUE** (line 161)
- **GLI_9755_UHS2_PLL_SSC_VALUE** (line 157)
- **GLI_9755_UHS2_SERDES_INTR_VALUE** (line 165)
- **GLI_9755_UHS2_SERDES_RECV_VALUE** (line 175)
- **GLI_9755_UHS2_SERDES_TRAN_VALUE** (line 173)
- **GLI_9755_UHS2_SERDES_ZC1_VALUE** (line 167)
- **GLI_9755_UHS2_SERDES_ZC2_DEFAULT** (line 169)
- **GLI_9755_UHS2_SERDES_ZC2_SANDISK** (line 170)
- **GLI_9755_WT_EN_OFF** (line 125)
- **GLI_9755_WT_EN_ON** (line 124)
- **GLI_9763E_CFG2_L1DLY** (line 107)
- **GLI_9763E_CFG2_L1DLY_MID** (line 108)
- **GLI_9763E_CFG_LPSN_DIS** (line 104)
- **GLI_9763E_CQE_TRNS_MODE** (line 118)
- **GLI_9763E_HS400_RXDLY** (line 114)
- **GLI_9763E_HS400_RXDLY_5** (line 115)
- **GLI_9763E_HS400_SLOW** (line 111)
- **GLI_9763E_MB_CMDQ_OFF** (line 98)
- **GLI_9763E_MB_ERP_ON** (line 99)
- **GLI_9763E_SCR_AXI_REQ** (line 101)
- **GLI_9763E_VHS_REV** (line 93)
- **GLI_9763E_VHS_REV_M** (line 95)
- **GLI_9763E_VHS_REV_R** (line 94)
- **GLI_9763E_VHS_REV_W** (line 96)
- **GLI_9767_VHS_REV** (line 193)
- **GLI_9767_VHS_REV_M** (line 195)
- **GLI_9767_VHS_REV_R** (line 194)
- **GLI_9767_VHS_REV_W** (line 196)
- **GLI_MAX_TUNING_LOOP** (line 292)
- **PCIE_GLI_9763E_CFG** (line 103)
- **PCIE_GLI_9763E_CFG2** (line 106)
- **PCIE_GLI_9763E_CLKRXDLY** (line 113)
- **PCIE_GLI_9763E_MB** (line 97)
- **PCIE_GLI_9763E_MMC_CTRL** (line 110)
- **PCIE_GLI_9763E_SCR** (line 100)
- **PCIE_GLI_9763E_VHS** (line 92)
- **PCIE_GLI_9767_CFG** (line 201)
- **PCIE_GLI_9767_CFG_LOW_PWR_OFF** (line 202)
- **PCIE_GLI_9767_COMBO_MUX_CTL** (line 204)
- **PCIE_GLI_9767_COMBO_MUX_CTL_RST_EN** (line 205)
- **PCIE_GLI_9767_COMBO_MUX_CTL_WAIT_PERST_EN** (line 206)
- **PCIE_GLI_9767_COM_MAILBOX** (line 198)
- **PCIE_GLI_9767_COM_MAILBOX_SSC_EN** (line 199)
- **PCIE_GLI_9767_NORMAL_ERR_INT_SIGNAL_EN_REG2** (line 265)
- **PCIE_GLI_9767_NORMAL_ERR_INT_SIGNAL_EN_REG2_SDEI_COMPLETE_SIGNAL_EN** (line 266)
- **PCIE_GLI_9767_NORMAL_ERR_INT_STATUS_EN_REG2** (line 262)
- **PCIE_GLI_9767_NORMAL_ERR_INT_STATUS_EN_REG2_SDEI_COMPLETE_STATUS_EN** (line 263)
- **PCIE_GLI_9767_NORMAL_ERR_INT_STATUS_REG2** (line 259)
- **PCIE_GLI_9767_NORMAL_ERR_INT_STATUS_REG2_SDEI_COMPLETE** (line 260)
- **PCIE_GLI_9767_PWR_MACRO_CTL** (line 208)
- **PCIE_GLI_9767_PWR_MACRO_CTL_LD0_LOW_OUTPUT_VOLTAGE** (line 210)
- **PCIE_GLI_9767_PWR_MACRO_CTL_LD0_LOW_OUTPUT_VOLTAGE_VALUE** (line 211)
- **PCIE_GLI_9767_PWR_MACRO_CTL_LOW_VOLTAGE** (line 209)
- **PCIE_GLI_9767_PWR_MACRO_CTL_RCLK_AMPLITUDE_CTL** (line 212)
- **PCIE_GLI_9767_PWR_MACRO_CTL_RCLK_AMPLITUDE_CTL_VALUE** (line 213)
- **PCIE_GLI_9767_RESET_REG** (line 225)
- **PCIE_GLI_9767_RESET_REG_SD_HOST_SW_RESET** (line 226)
- **PCIE_GLI_9767_SCR** (line 215)
- **PCIE_GLI_9767_SCR_AUTO_AXI_R_BURST** (line 217)
- **PCIE_GLI_9767_SCR_AUTO_AXI_W_BURST** (line 216)
- **PCIE_GLI_9767_SCR_AXI_REQ** (line 218)
- **PCIE_GLI_9767_SCR_CARD_DET_PWR_SAVING_EN** (line 219)
- **PCIE_GLI_9767_SCR_CFG_RST_DATA_LINK_DOWN** (line 223)
- **PCIE_GLI_9767_SCR_CORE_PWR_D3_OFF** (line 222)
- **PCIE_GLI_9767_SCR_SYSTEM_CLK_SELECT_MODE0** (line 220)
- **PCIE_GLI_9767_SCR_SYSTEM_CLK_SELECT_MODE1** (line 221)
- **PCIE_GLI_9767_SDHC_CAP** (line 232)
- **PCIE_GLI_9767_SDHC_CAP_SDEI_RESULT** (line 233)
- **PCIE_GLI_9767_SD_DATA_MULTI_CTL** (line 249)
- **PCIE_GLI_9767_SD_DATA_MULTI_CTL_DISCONNECT_TIME** (line 252)
- **PCIE_GLI_9767_SD_DATA_MULTI_CTL_DISCONNECT_TIME_VALUE** (line 253)
- **PCIE_GLI_9767_SD_DATA_MULTI_CTL_SELECT_UHS2** (line 250)
- **PCIE_GLI_9767_SD_DATA_MULTI_CTL_UHS2_SWITCH_CTL** (line 251)
- **PCIE_GLI_9767_SD_EXPRESS_CTL** (line 245)
- **PCIE_GLI_9767_SD_EXPRESS_CTL_SDEI_EXE** (line 246)
- **PCIE_GLI_9767_SD_EXPRESS_CTL_SD_EXPRESS_MODE** (line 247)
- **PCIE_GLI_9767_SD_PLL_CTL** (line 235)
- **PCIE_GLI_9767_SD_PLL_CTL2** (line 242)
- **PCIE_GLI_9767_SD_PLL_CTL2_PLLSSC_PPM** (line 243)
- **PCIE_GLI_9767_SD_PLL_CTL_PLL_DIR_EN** (line 238)
- **PCIE_GLI_9767_SD_PLL_CTL_PLL_LDIV** (line 236)
- **PCIE_GLI_9767_SD_PLL_CTL_PLL_PDIV** (line 237)
- **PCIE_GLI_9767_SD_PLL_CTL_SSC_EN** (line 239)
- **PCIE_GLI_9767_SD_PLL_CTL_SSC_STEP_SETTING** (line 240)
- **PCIE_GLI_9767_UHS2_CTL1** (line 268)
- **PCIE_GLI_9767_UHS2_CTL1_DECODING_CTL** (line 271)
- **PCIE_GLI_9767_UHS2_CTL1_DECODING_CTL_VALUE** (line 272)
- **PCIE_GLI_9767_UHS2_CTL1_DIR_RECV** (line 279)
- **PCIE_GLI_9767_UHS2_CTL1_DIR_RECV_VALUE** (line 280)
- **PCIE_GLI_9767_UHS2_CTL1_DIR_TRANS** (line 277)
- **PCIE_GLI_9767_UHS2_CTL1_DIR_TRANS_VALUE** (line 278)
- **PCIE_GLI_9767_UHS2_CTL1_PDRST** (line 281)
- **PCIE_GLI_9767_UHS2_CTL1_PDRST_VALUE** (line 282)
- **PCIE_GLI_9767_UHS2_CTL1_SERDES_RECV** (line 275)
- **PCIE_GLI_9767_UHS2_CTL1_SERDES_RECV_VALUE** (line 276)
- **PCIE_GLI_9767_UHS2_CTL1_SERDES_TRAN** (line 273)
- **PCIE_GLI_9767_UHS2_CTL1_SERDES_TRAN_VALUE** (line 274)
- **PCIE_GLI_9767_UHS2_CTL1_TRANS_PASS** (line 269)
- **PCIE_GLI_9767_UHS2_CTL1_TRANS_PASS_VALUE** (line 270)
- **PCIE_GLI_9767_UHS2_CTL2** (line 284)
- **PCIE_GLI_9767_UHS2_CTL2_FORCE_PHY_RESETN** (line 289)
- **PCIE_GLI_9767_UHS2_CTL2_FORCE_RESETN_VALUE** (line 290)
- **PCIE_GLI_9767_UHS2_CTL2_ZC** (line 285)
- **PCIE_GLI_9767_UHS2_CTL2_ZC_CTL** (line 287)
- **PCIE_GLI_9767_UHS2_CTL2_ZC_CTL_VALUE** (line 288)
- **PCIE_GLI_9767_UHS2_CTL2_ZC_VALUE** (line 286)
- **PCIE_GLI_9767_UHS2_PHY_SET_REG1** (line 228)
- **PCIE_GLI_9767_UHS2_PHY_SET_REG1_SERDES_INTR** (line 229)
- **PCIE_GLI_9767_UHS2_PHY_SET_REG1_SERDES_INTR_VALUE** (line 230)
- **PCIE_GLI_9767_UHS2_PHY_SET_REG2** (line 255)
- **PCIE_GLI_9767_UHS2_PHY_SET_REG2_SSC_PPM_SETTING** (line 256)
- **PCIE_GLI_9767_UHS2_PHY_SET_REG2_SSC_PPM_SETTING_VALUE** (line 257)
- **PCIE_GLI_9767_VHS** (line 192)
- **PCI_GLI_9755_CFG2** (line 133)
- **PCI_GLI_9755_CFG2_L1DLY** (line 134)
- **PCI_GLI_9755_DMACLK** (line 129)
- **PCI_GLI_9755_INVERT_CD** (line 130)
- **PCI_GLI_9755_INVERT_WP** (line 131)
- **PCI_GLI_9755_LFCLK** (line 128)
- **PCI_GLI_9755_MISC** (line 177)
- **PCI_GLI_9755_MISC_SSC_OFF** (line 178)
- **PCI_GLI_9755_PECONF** (line 127)
- **PCI_GLI_9755_PLL** (line 137)
- **PCI_GLI_9755_PLLSSC** (line 144)
- **PCI_GLI_9755_PLLSSC_EN** (line 142)
- **PCI_GLI_9755_PLLSSC_PPM** (line 145)
- **PCI_GLI_9755_PLLSSC_RECV** (line 150)
- **PCI_GLI_9755_PLLSSC_RTL** (line 146)
- **PCI_GLI_9755_PLLSSC_STEP** (line 141)
- **PCI_GLI_9755_PLLSSC_TRAN** (line 152)
- **PCI_GLI_9755_PLLSSC_TRANS_PASS** (line 148)
- **PCI_GLI_9755_PLL_DIR** (line 140)
- **PCI_GLI_9755_PLL_LDIV** (line 138)
- **PCI_GLI_9755_PLL_PDIV** (line 139)
- **PCI_GLI_9755_SCP_DIS** (line 171)
- **PCI_GLI_9755_SerDes** (line 163)
- **PCI_GLI_9755_UHS2_PLL** (line 155)
- **PCI_GLI_9755_UHS2_PLL_DELAY** (line 158)
- **PCI_GLI_9755_UHS2_PLL_PDRST** (line 160)
- **PCI_GLI_9755_UHS2_PLL_SSC** (line 156)
- **PCI_GLI_9755_UHS2_SERDES_INTR** (line 164)
- **PCI_GLI_9755_UHS2_SERDES_RECV** (line 174)
- **PCI_GLI_9755_UHS2_SERDES_TRAN** (line 172)
- **PCI_GLI_9755_UHS2_SERDES_ZC1** (line 166)
- **PCI_GLI_9755_UHS2_SERDES_ZC2** (line 168)
- **PCI_GLI_9755_WT** (line 122)
- **PCI_GLI_9755_WT_EN** (line 123)
- **REG_OFFSET_IN_BITS**(reg) (line 2012)
- **SDHCI_GLI_9750_ALL_RST** (line 40)
- **SDHCI_GLI_9750_CFG2** (line 29)
- **SDHCI_GLI_9750_CFG2_L1DLY** (line 30)
- **SDHCI_GLI_9750_DRIVING** (line 33)
- **SDHCI_GLI_9750_DRIVING_1** (line 34)
- **SDHCI_GLI_9750_DRIVING_2** (line 35)
- **SDHCI_GLI_9750_GM_BURST_SIZE** (line 71)
- **SDHCI_GLI_9750_GM_BURST_SIZE_R_OSRC_LMT** (line 72)
- **SDHCI_GLI_9750_MISC** (line 60)
- **SDHCI_GLI_9750_MISC_RX_INV** (line 62)
- **SDHCI_GLI_9750_MISC_SSC_OFF** (line 69)
- **SDHCI_GLI_9750_MISC_TX1_DLY** (line 63)
- **SDHCI_GLI_9750_MISC_TX1_INV** (line 61)
- **SDHCI_GLI_9750_PLL** (line 42)
- **SDHCI_GLI_9750_PLLSSC** (line 53)
- **SDHCI_GLI_9750_PLLSSC_EN** (line 51)
- **SDHCI_GLI_9750_PLLSSC_PPM** (line 54)
- **SDHCI_GLI_9750_PLLSSC_STEP** (line 50)
- **SDHCI_GLI_9750_PLL_DIR** (line 45)
- **SDHCI_GLI_9750_PLL_LDIV** (line 43)
- **SDHCI_GLI_9750_PLL_PDIV** (line 44)
- **SDHCI_GLI_9750_PLL_TX2_DLY** (line 47)
- **SDHCI_GLI_9750_PLL_TX2_INV** (line 46)
- **SDHCI_GLI_9750_SEL_1** (line 38)
- **SDHCI_GLI_9750_SEL_2** (line 39)
- **SDHCI_GLI_9750_SW_CTRL** (line 56)
- **SDHCI_GLI_9750_SW_CTRL_4** (line 57)
- **SDHCI_GLI_9750_TUNING_CONTROL** (line 74)
- **SDHCI_GLI_9750_TUNING_CONTROL_EN** (line 75)
- **SDHCI_GLI_9750_TUNING_CONTROL_GLITCH_1** (line 78)
- **SDHCI_GLI_9750_TUNING_CONTROL_GLITCH_2** (line 79)
- **SDHCI_GLI_9750_TUNING_PARAMETERS** (line 83)
- **SDHCI_GLI_9750_TUNING_PARAMETERS_RX_DLY** (line 84)
- **SDHCI_GLI_9750_WT** (line 24)
- **SDHCI_GLI_9750_WT_EN** (line 25)
- **SDHCI_GLI_9763E_CQE_BASE_ADDR** (line 117)
- **SDHCI_GLI_9763E_CTRL_HS400** (line 87)
- **SDHCI_GLI_9763E_HS400_ES_BIT** (line 90)
- **SDHCI_GLI_9763E_HS400_ES_REG** (line 89)
- **SDHCI_GLI_9767_GM_BURST_SIZE** (line 189)
- **SDHCI_GLI_9767_GM_BURST_SIZE_AXI_ALWAYS_SET** (line 190)
- **SDHCI_GLI_9767_SD_HOST_OPERATION_CTL** (line 180)
- **SDHCI_GLI_9767_SD_HOST_OPERATION_CTL_CMD_CONFLICT_CHECK** (line 181)
- **SDHCI_GLI_9767_SD_HOST_OPERATION_CTL_DEBOUNCE** (line 182)
- **SDHCI_GLI_9767_SD_HOST_OPERATION_CTL_DEBOUNCE_PLUG_IN_VALUE** (line 183)
- **SDHCI_GLI_9767_SD_HOST_OPERATION_CTL_DEBOUNCE_PLUG_OUT_VALUE** (line 184)
- **SDHCI_GLI_9767_SD_HOST_OPERATION_CTL_DEBOUNCE_SCALE** (line 185)
- **SDHCI_GLI_9767_SD_HOST_OPERATION_CTL_DEBOUNCE_SCALE_10MS** (line 187)
- **SDHCI_GLI_9767_SD_HOST_OPERATION_CTL_DEBOUNCE_SCALE_1MS** (line 186)
