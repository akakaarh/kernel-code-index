# drivers/mmc/host/sdhci-acpi.c

Subsystem: drivers/mmc

## Functions (31)

### __intel_dsm
- Return type: static int
- Signature: __intel_dsm(struct intel_host * intel_host,struct device * dev,unsigned int fn,u32 * result)
- Line: 119

### amd_sdhci_execute_tuning
- Return type: static int
- Signature: amd_sdhci_execute_tuning(struct mmc_host * mmc,u32 opcode)
- Line: 569

### amd_sdhci_reset
- Return type: static void
- Signature: amd_sdhci_reset(struct sdhci_host * host,u8 mask)
- Line: 586

### amd_select_drive_strength
- Return type: static int
- Signature: amd_select_drive_strength(struct mmc_card * card,unsigned int max_dtr,int host_drv,int card_drv,int * host_driver_strength)
- Line: 474

### amd_set_ios
- Return type: static void
- Signature: amd_set_ios(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 540

### bxt_get_cd
- Return type: static int
- Signature: bxt_get_cd(struct mmc_host * mmc)
- Line: 301

### intel_dsm
- Return type: static int
- Signature: intel_dsm(struct intel_host * intel_host,struct device * dev,unsigned int fn,u32 * result)
- Line: 147

### intel_dsm_init
- Return type: static void
- Signature: intel_dsm_init(struct intel_host * intel_host,struct device * dev,struct mmc_host * mmc)
- Line: 156

### intel_probe_slot
- Return type: static int
- Signature: intel_probe_slot(struct platform_device * pdev,struct acpi_device * adev)
- Line: 311

### intel_setup_host
- Return type: static int
- Signature: intel_setup_host(struct platform_device * pdev)
- Line: 335

### intel_start_signal_voltage_switch
- Return type: static int
- Signature: intel_start_signal_voltage_switch(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 176

### qcom_free_slot
- Return type: static int
- Signature: qcom_free_slot(struct platform_device * pdev)
- Line: 430

### qcom_probe_slot
- Return type: static int
- Signature: qcom_probe_slot(struct platform_device * pdev,struct acpi_device * adev)
- Line: 410

### sdhci_acpi_amd_hs400_dll
- Return type: static void
- Signature: sdhci_acpi_amd_hs400_dll(struct sdhci_host * host,bool enable)
- Line: 513

### sdhci_acpi_byt_defer
- Return type: static bool
- Signature: sdhci_acpi_byt_defer(struct device * dev)
- Line: 275

### sdhci_acpi_byt_defer
- Return type: static bool
- Signature: sdhci_acpi_byt_defer(struct device * dev)
- Line: 294

### sdhci_acpi_byt_setting
- Return type: static void
- Signature: sdhci_acpi_byt_setting(struct device * dev)
- Line: 290

### sdhci_acpi_byt_setting
- Return type: static void
- Signature: sdhci_acpi_byt_setting(struct device * dev)
- Line: 248

### sdhci_acpi_emmc_amd_probe_slot
- Return type: static int
- Signature: sdhci_acpi_emmc_amd_probe_slot(struct platform_device * pdev,struct acpi_device * adev)
- Line: 610

### sdhci_acpi_flag
- Return type: static bool
- Signature: sdhci_acpi_flag(struct sdhci_acpi_host * c,unsigned int flag)
- Line: 93

### sdhci_acpi_get_slot
- Return type: static const struct sdhci_acpi_slot *
- Signature: sdhci_acpi_get_slot(struct acpi_device * adev)
- Line: 806

### sdhci_acpi_int_hw_reset
- Return type: static void
- Signature: sdhci_acpi_int_hw_reset(struct sdhci_host * host)
- Line: 208

### sdhci_acpi_priv
- Return type: static void *
- Signature: sdhci_acpi_priv(struct sdhci_acpi_host * c)
- Line: 88

### sdhci_acpi_probe
- Return type: static int
- Signature: sdhci_acpi_probe(struct platform_device * pdev)
- Line: 817

### sdhci_acpi_qcom_handler
- Return type: static irqreturn_t
- Signature: sdhci_acpi_qcom_handler(int irq,void * ptr)
- Line: 400

### sdhci_acpi_remove
- Return type: static void
- Signature: sdhci_acpi_remove(struct platform_device * pdev)
- Line: 954

### sdhci_acpi_reset_signal_voltage_if_needed
- Return type: static void
- Signature: sdhci_acpi_reset_signal_voltage_if_needed(struct device * dev)
- Line: 976

### sdhci_acpi_resume
- Return type: static int
- Signature: sdhci_acpi_resume(struct device * dev)
- Line: 1008

### sdhci_acpi_runtime_resume
- Return type: static int
- Signature: sdhci_acpi_runtime_resume(struct device * dev)
- Line: 1031

### sdhci_acpi_runtime_suspend
- Return type: static int
- Signature: sdhci_acpi_runtime_suspend(struct device * dev)
- Line: 1017

### sdhci_acpi_suspend
- Return type: static int
- Signature: sdhci_acpi_suspend(struct device * dev)
- Line: 991

## Structs (6)

### amd_sdhci_host
- Line: 466
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
  - tuned_clock: bool
  - dll_enabled: bool
  - hid: const char *
  - uid: const char *
  - slot: const struct sdhci_acpi_slot *

### intel_host
- Line: 110
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

### sdhci_acpi_chip
- Line: 47
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
  - tuned_clock: bool
  - dll_enabled: bool
  - hid: const char *
  - uid: const char *
  - slot: const struct sdhci_acpi_slot *

### sdhci_acpi_host
- Line: 71
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
  - tuned_clock: bool
  - dll_enabled: bool
  - hid: const char *
  - uid: const char *
  - slot: const struct sdhci_acpi_slot *

### sdhci_acpi_slot
- Line: 56
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
  - tuned_clock: bool
  - dll_enabled: bool
  - hid: const char *
  - uid: const char *
  - slot: const struct sdhci_acpi_slot *

### sdhci_acpi_uid_slot
- Line: 678
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
  - tuned_clock: bool
  - dll_enabled: bool
  - hid: const char *
  - uid: const char *
  - slot: const struct sdhci_acpi_slot *

## Enums (3)

### __anonefb065fc0103
- Line: 41

### __anonefb065fc0203
- Line: 81

### __anonefb065fc0303
- Line: 103

## Variables (17)

- static **intel_dsm_guid** : const guid_t (line 115)
- static **sdhci_acpi_chip_amd** : const struct sdhci_acpi_chip (line 606)
- static **sdhci_acpi_chip_int** : const struct sdhci_acpi_chip (line 238)
- static **sdhci_acpi_driver** : platform_driver (line 1046)
- static **sdhci_acpi_ids** : const struct acpi_device_id[] (line 706)
- static **sdhci_acpi_ops_amd** : const struct sdhci_ops (line 599)
- static **sdhci_acpi_ops_dflt** : const struct sdhci_ops (line 223)
- static **sdhci_acpi_ops_int** : const struct sdhci_ops (line 230)
- static **sdhci_acpi_pm_ops** : const struct dev_pm_ops (line 1041)
- static **sdhci_acpi_quirks** : const struct dmi_system_id[] (line 726)
- static **sdhci_acpi_slot_amd_emmc** : const struct sdhci_acpi_slot (line 667)
- static **sdhci_acpi_slot_int_emmc** : const struct sdhci_acpi_slot (line 355)
- static **sdhci_acpi_slot_int_sd** : const struct sdhci_acpi_slot (line 385)
- static **sdhci_acpi_slot_int_sdio** : const struct sdhci_acpi_slot (line 371)
- static **sdhci_acpi_slot_qcom_sd** : const struct sdhci_acpi_slot (line 461)
- static **sdhci_acpi_slot_qcom_sd_3v** : const struct sdhci_acpi_slot (line 452)
- static **sdhci_acpi_uids** : const struct sdhci_acpi_uid_slot[] (line 684)

## Macros (10)

- **BYT_IOSF_OCP_NETCTRL0** (line 245)
- **BYT_IOSF_OCP_TIMEOUT_BASE** (line 246)
- **BYT_IOSF_SCCEP** (line 244)
- **INTEL_DSM_HS_CAPS_DDR50** (line 99)
- **INTEL_DSM_HS_CAPS_SDR104** (line 101)
- **INTEL_DSM_HS_CAPS_SDR25** (line 98)
- **INTEL_DSM_HS_CAPS_SDR50** (line 100)
- **SDHCI_AMD_RESET_DLL_REGISTER** (line 472)
- **VENDOR_SPECIFIC_PWRCTL_CLEAR_REG** (line 398)
- **VENDOR_SPECIFIC_PWRCTL_CTL_REG** (line 399)
