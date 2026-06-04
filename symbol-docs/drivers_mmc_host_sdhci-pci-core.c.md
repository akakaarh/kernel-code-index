# drivers/mmc/host/sdhci-pci-core.c

Subsystem: drivers/mmc

## Functions (103)

### __intel_dsm
- Return type: static int
- Signature: __intel_dsm(struct intel_host * intel_host,struct device * dev,unsigned int fn,u32 * result)
- Line: 469

### amd_config_tuning_phase
- Return type: static void
- Signature: amd_config_tuning_phase(struct pci_dev * pdev,u8 phase)
- Line: 1697

### amd_enable_manual_tuning
- Return type: static void
- Signature: amd_enable_manual_tuning(struct pci_dev * pdev)
- Line: 1707

### amd_execute_tuning
- Return type: static int
- Signature: amd_execute_tuning(struct mmc_host * mmc,u32 opcode)
- Line: 1755

### amd_execute_tuning_hs200
- Return type: static int
- Signature: amd_execute_tuning_hs200(struct sdhci_host * host,u32 opcode)
- Line: 1716

### amd_probe
- Return type: static int
- Signature: amd_probe(struct sdhci_pci_chip * chip)
- Line: 1776

### amd_probe_slot
- Return type: static int
- Signature: amd_probe_slot(struct sdhci_pci_slot * slot)
- Line: 1767

### amd_sdhci_reset
- Return type: static void
- Signature: amd_sdhci_reset(struct sdhci_host * host,u8 mask)
- Line: 1811

### amd_tuning_reset
- Return type: static void
- Signature: amd_tuning_reset(struct sdhci_host * host)
- Line: 1684

### bxt_get_cd
- Return type: static int
- Signature: bxt_get_cd(struct mmc_host * mmc)
- Line: 559

### byt_add_debugfs
- Return type: static void
- Signature: byt_add_debugfs(struct sdhci_pci_slot * slot)
- Line: 864

### byt_add_host
- Return type: static int
- Signature: byt_add_host(struct sdhci_pci_slot * slot)
- Line: 879

### byt_emmc_probe_slot
- Return type: static int
- Signature: byt_emmc_probe_slot(struct sdhci_pci_slot * slot)
- Line: 896

### byt_needs_pwr_off
- Return type: static void
- Signature: byt_needs_pwr_off(struct sdhci_pci_slot * slot)
- Line: 1112

### byt_ocp_setting
- Return type: static void
- Signature: byt_ocp_setting(struct pci_dev * pdev)
- Line: 439

### byt_ocp_setting
- Return type: static void
- Signature: byt_ocp_setting(struct pci_dev * pdev)
- Line: 407

### byt_probe_slot
- Return type: static void
- Signature: byt_probe_slot(struct sdhci_pci_slot * slot)
- Line: 843

### byt_read_dsm
- Return type: static void
- Signature: byt_read_dsm(struct sdhci_pci_slot * slot)
- Line: 713

### byt_remove_slot
- Return type: static void
- Signature: byt_remove_slot(struct sdhci_pci_slot * slot,int dead)
- Line: 888

### byt_resume
- Return type: static int
- Signature: byt_resume(struct sdhci_pci_chip * chip)
- Line: 1144

### byt_runtime_resume
- Return type: static int
- Signature: byt_runtime_resume(struct sdhci_pci_chip * chip)
- Line: 1155

### byt_sd_probe_slot
- Return type: static int
- Signature: byt_sd_probe_slot(struct sdhci_pci_slot * slot)
- Line: 1120

### byt_sdio_probe_slot
- Return type: static int
- Signature: byt_sdio_probe_slot(struct sdhci_pci_slot * slot)
- Line: 1104

### ene_714_probe_slot
- Return type: static int
- Signature: ene_714_probe_slot(struct sdhci_pci_slot * slot)
- Line: 300

### ene_714_set_ios
- Return type: static void
- Signature: ene_714_set_ios(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 285

### glk_broken_cqhci
- Return type: static bool
- Signature: glk_broken_cqhci(struct sdhci_pci_slot * slot)
- Line: 911

### glk_emmc_add_host
- Return type: static int
- Signature: glk_emmc_add_host(struct sdhci_pci_slot * slot)
- Line: 950

### glk_emmc_probe_slot
- Return type: static int
- Signature: glk_emmc_probe_slot(struct sdhci_pci_slot * slot)
- Line: 925

### glk_rpm_retune_chk
- Return type: static void
- Signature: glk_rpm_retune_chk(struct sdhci_pci_chip * chip,bool susp)
- Line: 1042

### glk_rpm_retune_wa
- Return type: static void
- Signature: glk_rpm_retune_wa(struct sdhci_pci_chip * chip,bool susp)
- Line: 999

### glk_runtime_resume
- Return type: static int
- Signature: glk_runtime_resume(struct sdhci_pci_chip * chip)
- Line: 1056

### glk_runtime_suspend
- Return type: static int
- Signature: glk_runtime_suspend(struct sdhci_pci_chip * chip)
- Line: 1049

### intel_cache_ltr
- Return type: static void
- Signature: intel_cache_ltr(struct sdhci_pci_slot * slot)
- Line: 750

### intel_dsm
- Return type: static int
- Signature: intel_dsm(struct intel_host * intel_host,struct device * dev,unsigned int fn,u32 * result)
- Line: 496

### intel_dsm_init
- Return type: static void
- Signature: intel_dsm_init(struct intel_host * intel_host,struct device * dev,struct mmc_host * mmc)
- Line: 505

### intel_execute_tuning
- Return type: static int
- Signature: intel_execute_tuning(struct mmc_host * mmc,u32 opcode)
- Line: 723

### intel_hs400_enhanced_strobe
- Return type: static void
- Signature: intel_hs400_enhanced_strobe(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 634

### intel_ltr_expose
- Return type: static void
- Signature: intel_ltr_expose(struct sdhci_pci_chip * chip)
- Line: 821

### intel_ltr_hide
- Return type: static void
- Signature: intel_ltr_hide(struct sdhci_pci_chip * chip)
- Line: 832

### intel_ltr_set
- Return type: static void
- Signature: intel_ltr_set(struct device * dev,s32 val)
- Line: 759

### intel_mrfld_mmc_fix_up_power_slot
- Return type: static void
- Signature: intel_mrfld_mmc_fix_up_power_slot(struct sdhci_pci_slot * slot)
- Line: 1305

### intel_mrfld_mmc_fix_up_power_slot
- Return type: static void
- Signature: intel_mrfld_mmc_fix_up_power_slot(struct sdhci_pci_slot * slot)
- Line: 1296

### intel_mrfld_mmc_probe_slot
- Return type: static int
- Signature: intel_mrfld_mmc_probe_slot(struct sdhci_pci_slot * slot)
- Line: 1308

### intel_select_drive_strength
- Return type: static int
- Signature: intel_select_drive_strength(struct mmc_card * card,unsigned int max_dtr,int host_drv,int card_drv,int * drv_type)
- Line: 545

### intel_start_signal_voltage_switch
- Return type: static int
- Signature: intel_start_signal_voltage_switch(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 648

### intel_use_ltr
- Return type: static bool
- Signature: intel_use_ltr(struct sdhci_pci_chip * chip)
- Line: 805

### jmicron_enable_mmc
- Return type: static void
- Signature: jmicron_enable_mmc(struct sdhci_host * host,int on)
- Line: 1456

### jmicron_jmb388_get_ro
- Return type: static int
- Signature: jmicron_jmb388_get_ro(struct mmc_host * mmc)
- Line: 1354

### jmicron_pmos
- Return type: static int
- Signature: jmicron_pmos(struct sdhci_pci_chip * chip,int on)
- Line: 1369

### jmicron_probe
- Return type: static int
- Signature: jmicron_probe(struct sdhci_pci_chip * chip)
- Line: 1393

### jmicron_probe_slot
- Return type: static int
- Signature: jmicron_probe_slot(struct sdhci_pci_slot * slot)
- Line: 1470

### jmicron_remove_slot
- Return type: static void
- Signature: jmicron_remove_slot(struct sdhci_pci_slot * slot,int dead)
- Line: 1515

### jmicron_resume
- Return type: static int
- Signature: jmicron_resume(struct sdhci_pci_chip * chip)
- Line: 1543

### jmicron_suspend
- Return type: static int
- Signature: jmicron_suspend(struct sdhci_pci_chip * chip)
- Line: 1526

### jsl_broken_hs400es
- Return type: static bool
- Signature: jsl_broken_hs400es(struct sdhci_pci_slot * slot)
- Line: 919

### mfd_emmc_probe_slot
- Return type: static int
- Signature: mfd_emmc_probe_slot(struct sdhci_pci_slot * slot)
- Line: 354

### mfd_sdio_probe_slot
- Return type: static int
- Signature: mfd_sdio_probe_slot(struct sdhci_pci_slot * slot)
- Line: 361

### mrfld_get_cd
- Return type: static int
- Signature: mrfld_get_cd(struct mmc_host * mmc)
- Line: 569

### mrst_hc_probe
- Return type: static int
- Signature: mrst_hc_probe(struct sdhci_pci_chip * chip)
- Line: 338

### mrst_hc_probe_slot
- Return type: static int
- Signature: mrst_hc_probe_slot(struct sdhci_pci_slot * slot)
- Line: 328

### ni_byt_sdio_probe_slot
- Return type: static int
- Signature: ni_byt_sdio_probe_slot(struct sdhci_pci_slot * slot)
- Line: 1089

### ni_set_max_freq
- Return type: static int
- Signature: ni_set_max_freq(struct sdhci_pci_slot * slot)
- Line: 1083

### ni_set_max_freq
- Return type: static int
- Signature: ni_set_max_freq(struct sdhci_pci_slot * slot)
- Line: 1065

### pch_hc_probe_slot
- Return type: static int
- Signature: pch_hc_probe_slot(struct sdhci_pci_slot * slot)
- Line: 348

### ricoh_mmc_probe_slot
- Return type: static int
- Signature: ricoh_mmc_probe_slot(struct sdhci_pci_slot * slot)
- Line: 242

### ricoh_mmc_resume
- Return type: static int
- Signature: ricoh_mmc_resume(struct sdhci_pci_chip * chip)
- Line: 258

### ricoh_probe
- Return type: static int
- Signature: ricoh_probe(struct sdhci_pci_chip * chip)
- Line: 234

### rtsx_probe_slot
- Return type: static int
- Signature: rtsx_probe_slot(struct sdhci_pci_slot * slot)
- Line: 1654

### sdhci_cqhci_irq
- Return type: static u32
- Signature: sdhci_cqhci_irq(struct sdhci_host * host,u32 intmask)
- Line: 210

### sdhci_cqhci_resume
- Return type: static int
- Signature: sdhci_cqhci_resume(struct sdhci_pci_chip * chip)
- Line: 137

### sdhci_cqhci_runtime_resume
- Return type: static int
- Signature: sdhci_cqhci_runtime_resume(struct sdhci_pci_chip * chip)
- Line: 198

### sdhci_cqhci_runtime_suspend
- Return type: static int
- Signature: sdhci_cqhci_runtime_suspend(struct sdhci_pci_chip * chip)
- Line: 187

### sdhci_cqhci_suspend
- Return type: static int
- Signature: sdhci_cqhci_suspend(struct sdhci_pci_chip * chip)
- Line: 126

### sdhci_intel_set_clock
- Return type: static void
- Signature: sdhci_intel_set_clock(struct sdhci_host * host,unsigned int clock)
- Line: 681

### sdhci_intel_set_power
- Return type: static void
- Signature: sdhci_intel_set_power(struct sdhci_host * host,unsigned char mode,unsigned short vdd)
- Line: 577

### sdhci_intel_set_uhs_signaling
- Return type: static void
- Signature: sdhci_intel_set_uhs_signaling(struct sdhci_host * host,unsigned int timing)
- Line: 622

### sdhci_pci_add_gpio_lookup_table
- Return type: static gpiod_lookup_table *
- Signature: sdhci_pci_add_gpio_lookup_table(struct sdhci_pci_chip * chip)
- Line: 2087

### sdhci_pci_dumpregs
- Return type: static void
- Signature: sdhci_pci_dumpregs(struct mmc_host * mmc)
- Line: 223

### sdhci_pci_enable_dma
- Return type: int
- Signature: sdhci_pci_enable_dma(struct sdhci_host * host)
- Line: 1976

### sdhci_pci_hw_reset
- Return type: static void
- Signature: sdhci_pci_hw_reset(struct sdhci_host * host)
- Line: 1996

### sdhci_pci_init_wakeup
- Return type: static int
- Signature: sdhci_pci_init_wakeup(struct sdhci_pci_chip * chip)
- Line: 48

### sdhci_pci_int_hw_reset
- Return type: static void
- Signature: sdhci_pci_int_hw_reset(struct sdhci_host * host)
- Line: 530

### sdhci_pci_probe
- Return type: static int
- Signature: sdhci_pci_probe(struct pci_dev * pdev,const struct pci_device_id * ent)
- Line: 2293

### sdhci_pci_probe_slot
- Return type: static sdhci_pci_slot *
- Signature: sdhci_pci_probe_slot(struct pci_dev * pdev,struct sdhci_pci_chip * chip,int first_bar,int slotno)
- Line: 2123

### sdhci_pci_remove
- Return type: static void
- Signature: sdhci_pci_remove(struct pci_dev * pdev)
- Line: 2374

### sdhci_pci_remove_gpio_lookup_table
- Return type: static void
- Signature: sdhci_pci_remove_gpio_lookup_table(struct gpiod_lookup_table * lookup_table)
- Line: 2115

### sdhci_pci_remove_slot
- Return type: static void
- Signature: sdhci_pci_remove_slot(struct sdhci_pci_slot * slot)
- Line: 2248

### sdhci_pci_resume
- Return type: static int
- Signature: sdhci_pci_resume(struct device * dev)
- Line: 2033

### sdhci_pci_resume_host
- Return type: int
- Signature: sdhci_pci_resume_host(struct sdhci_pci_chip * chip)
- Line: 106

### sdhci_pci_runtime_pm_allow
- Return type: static void
- Signature: sdhci_pci_runtime_pm_allow(struct device * dev)
- Line: 2277

### sdhci_pci_runtime_pm_forbid
- Return type: static void
- Signature: sdhci_pci_runtime_pm_forbid(struct device * dev)
- Line: 2287

### sdhci_pci_runtime_resume
- Return type: static int
- Signature: sdhci_pci_runtime_resume(struct device * dev)
- Line: 2061

### sdhci_pci_runtime_resume_host
- Return type: static int
- Signature: sdhci_pci_runtime_resume_host(struct sdhci_pci_chip * chip)
- Line: 172

### sdhci_pci_runtime_suspend
- Return type: static int
- Signature: sdhci_pci_runtime_suspend(struct device * dev)
- Line: 2048

### sdhci_pci_runtime_suspend_host
- Return type: static int
- Signature: sdhci_pci_runtime_suspend_host(struct sdhci_pci_chip * chip)
- Line: 150

### sdhci_pci_suspend
- Return type: static int
- Signature: sdhci_pci_suspend(struct device * dev)
- Line: 2020

### sdhci_pci_suspend_host
- Return type: static int
- Signature: sdhci_pci_suspend_host(struct sdhci_pci_chip * chip)
- Line: 72

### sdhci_pci_uhs2_add_host
- Return type: int
- Signature: sdhci_pci_uhs2_add_host(struct sdhci_pci_slot * slot)
- Line: 2267

### sdhci_pci_uhs2_remove_host
- Return type: void
- Signature: sdhci_pci_uhs2_remove_host(struct sdhci_pci_slot * slot,int dead)
- Line: 2272

### sdhci_read_present_state
- Return type: static u32
- Signature: sdhci_read_present_state(struct sdhci_host * host)
- Line: 1806

### syskt_probe
- Return type: static int
- Signature: syskt_probe(struct sdhci_pci_chip * chip)
- Line: 1594

### syskt_probe_slot
- Return type: static int
- Signature: syskt_probe_slot(struct sdhci_pci_slot * slot)
- Line: 1603

### via_probe
- Return type: static int
- Signature: via_probe(struct sdhci_pci_chip * chip)
- Line: 1642

## Structs (1)

### intel_host
- Line: 453
- Members:
  - ops: const struct sdhci_ops *
  - quirks: unsigned int
  - quirks2: unsigned int
  - caps: unsigned long
  - caps2: unsigned int
  - pm_caps: mmc_pm_flag_t
  - chip: const struct sdhci_acpi_chip *
  - quirks: unsigned int
  - quirks2: unsigned int
  - caps: unsigned long
  - caps2: unsigned int
  - pm_caps: mmc_pm_flag_t
  - flags: unsigned int
  - priv_size: size_t
  - probe_slot: int (*)(struct platform_device *,struct acpi_device *)
  - remove_slot: int (*)(struct platform_device *)
  - free_slot: int (*)(struct platform_device * pdev)
  - setup_host: int (*)(struct platform_device * pdev)
  - host: sdhci_host *
  - slot: const struct sdhci_acpi_slot *
  - pdev: platform_device *
  - use_runtime_pm: bool
  - is_intel: bool
  - reset_signal_volt_on_suspend: bool
  - private: unsigned long[]____cacheline_aligned
  - dsm_fns: u32
  - hs_caps: u32
  - dsm_fns: u32
  - drv_strength: int
  - d3_retune: bool
  - rpm_retune_ok: bool
  - needs_pwr_off: bool
  - glk_rx_ctrl1: u32
  - glk_tun_val: u32
  - active_ltr: u32
  - idle_ltr: u32
  - tuned_clock: bool
  - dll_enabled: bool
  - hid: const char *
  - uid: const char *
  - slot: const struct sdhci_acpi_slot *

## Enums (2)

### __anonb6113c110103
- Line: 445

### amd_chipset_gen
- Line: 1668

## Variables (34)

- static **amd_sdhci_pci_ops** : const struct sdhci_ops (line 1854)
- static **glk_cqhci_ops** : const struct cqhci_host_ops (line 944)
- static **intel_dsm_guid** : const guid_t (line 465)
- static **pci_ids** : const struct pci_device_id[] (line 1868)
- static **sdhci_amd** : const struct sdhci_pci_fixes (line 1862)
- static **sdhci_cafe** : const struct sdhci_pci_fixes (line 317)
- static **sdhci_driver** : pci_driver (line 2386)
- static **sdhci_ene_712** : const struct sdhci_pci_fixes (line 306)
- static **sdhci_ene_714** : const struct sdhci_pci_fixes (line 311)
- static **sdhci_intel_byt_cd_gpio_override** : const struct dmi_system_id[] (line 1253)
- static **sdhci_intel_byt_emmc** : const struct sdhci_pci_fixes (line 1164)
- static **sdhci_intel_byt_ops** : const struct sdhci_ops (line 692)
- static **sdhci_intel_byt_sd** : const struct sdhci_pci_fixes (line 1267)
- static **sdhci_intel_byt_sdio** : const struct sdhci_pci_fixes (line 1225)
- static **sdhci_intel_glk_emmc** : const struct sdhci_pci_fixes (line 1184)
- static **sdhci_intel_glk_ops** : const struct sdhci_ops (line 702)
- static **sdhci_intel_mfd_emmc** : const struct sdhci_pci_fixes (line 390)
- static **sdhci_intel_mfd_sd** : const struct sdhci_pci_fixes (line 377)
- static **sdhci_intel_mfd_sdio** : const struct sdhci_pci_fixes (line 383)
- static **sdhci_intel_mrfld_mmc** : const struct sdhci_pci_fixes (line 1344)
- static **sdhci_intel_mrst_hc0** : const struct sdhci_pci_fixes (line 367)
- static **sdhci_intel_mrst_hc1_hc2** : const struct sdhci_pci_fixes (line 372)
- static **sdhci_intel_pch_sdio** : const struct sdhci_pci_fixes (line 396)
- static **sdhci_intel_qrk** : const struct sdhci_pci_fixes (line 324)
- static **sdhci_jmicron** : const struct sdhci_pci_fixes (line 1563)
- static **sdhci_ni_byt_sdio** : const struct sdhci_pci_fixes (line 1206)
- static **sdhci_pci_ops** : const struct sdhci_ops (line 2004)
- static **sdhci_pci_pm_ops** : const struct dev_pm_ops (line 2075)
- static **sdhci_ricoh** : const struct sdhci_pci_fixes (line 268)
- static **sdhci_ricoh_mmc** : const struct sdhci_pci_fixes (line 275)
- static **sdhci_rtsx** : const struct sdhci_pci_fixes (line 1660)
- static **sdhci_syskt** : const struct sdhci_pci_fixes (line 1636)
- static **sdhci_via** : const struct sdhci_pci_fixes (line 1650)
- static **vexia_edu_atla10_cd_gpios** : const struct gpiod_lookup_table (line 1245)

## Macros (47)

- **AMD_AUTO_TUNE_SEL** (line 1680)
- **AMD_BIT_MASK** (line 1682)
- **AMD_FIFO_PTR** (line 1681)
- **AMD_MAX_TUNE_VALUE** (line 1679)
- **AMD_MSLEEP_DURATION** (line 1677)
- **AMD_SD_AUTO_PATTERN** (line 1676)
- **AMD_SD_MISC_CONTROL** (line 1678)
- **BYT_IOSF_OCP_NETCTRL0** (line 404)
- **BYT_IOSF_OCP_TIMEOUT_BASE** (line 405)
- **BYT_IOSF_SCCEP** (line 403)
- **GLK_DLY** (line 997)
- **GLK_PATH_PLL** (line 996)
- **GLK_RX_CTRL1** (line 994)
- **GLK_TUN_VAL** (line 995)
- **INTEL_ACTIVELTR** (line 741)
- **INTEL_HS400_ES_BIT** (line 632)
- **INTEL_HS400_ES_REG** (line 631)
- **INTEL_IDLELTR** (line 742)
- **INTEL_LTR_REQ** (line 744)
- **INTEL_LTR_SCALE_1US** (line 746)
- **INTEL_LTR_SCALE_32US** (line 747)
- **INTEL_LTR_SCALE_MASK** (line 745)
- **INTEL_LTR_VALUE_MASK** (line 748)
- **INTEL_MRFLD_EMMC_0** (line 1290)
- **INTEL_MRFLD_EMMC_1** (line 1291)
- **INTEL_MRFLD_SD** (line 1292)
- **INTEL_MRFLD_SDIO** (line 1293)
- **JMB388_SAMPLE_COUNT** (line 1352)
- **SDHCI_INTEL_PWR_TIMEOUT_CNT** (line 574)
- **SDHCI_INTEL_PWR_TIMEOUT_UDELAY** (line 575)
- **SYSKT_BOARD_REV** (line 1587)
- **SYSKT_CHIP_REV** (line 1588)
- **SYSKT_CONF_DATA** (line 1589)
- **SYSKT_CONF_DATA_1V8** (line 1590)
- **SYSKT_CONF_DATA_2V5** (line 1591)
- **SYSKT_CONF_DATA_3V3** (line 1592)
- **SYSKT_CTRL** (line 1576)
- **SYSKT_POWER_184** (line 1582)
- **SYSKT_POWER_300** (line 1581)
- **SYSKT_POWER_330** (line 1580)
- **SYSKT_POWER_CMD** (line 1583)
- **SYSKT_POWER_DATA** (line 1579)
- **SYSKT_POWER_START** (line 1584)
- **SYSKT_POWER_STATUS** (line 1585)
- **SYSKT_POWER_STATUS_OK** (line 1586)
- **SYSKT_RDFIFO_STAT** (line 1577)
- **SYSKT_WRFIFO_STAT** (line 1578)
