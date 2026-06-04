# drivers/mmc/host/sdhci-msm.c

Subsystem: drivers/mmc

## Functions (77)

### __sdhci_msm_check_write
- Return type: static int
- Signature: __sdhci_msm_check_write(struct sdhci_host * host,u16 val,int reg)
- Line: 2316

### __sdhci_msm_set_clock
- Return type: static void
- Signature: __sdhci_msm_set_clock(struct sdhci_host * host,unsigned int clock)
- Line: 1858

### msm_cm_dll_set_freq
- Return type: static void
- Signature: msm_cm_dll_set_freq(struct sdhci_host * host)
- Line: 617

### msm_config_cm_dll_phase
- Return type: static int
- Signature: msm_config_cm_dll_phase(struct sdhci_host * host,u8 phase)
- Line: 445

### msm_config_vmmc_regulator
- Return type: static void
- Signature: msm_config_vmmc_regulator(struct mmc_host * mmc,bool hpm)
- Line: 1444

### msm_config_vqmmc_mode
- Return type: static int
- Signature: msm_config_vqmmc_mode(struct sdhci_msm_host * msm_host,struct mmc_host * mmc,bool hpm)
- Line: 1529

### msm_config_vqmmc_regulator
- Return type: static void
- Signature: msm_config_vqmmc_regulator(struct mmc_host * mmc,bool hpm)
- Line: 1462

### msm_dll_poll_ck_out_en
- Return type: static int
- Signature: msm_dll_poll_ck_out_en(struct sdhci_host * host,u8 poll)
- Line: 418

### msm_find_most_appropriate_phase
- Return type: static int
- Signature: msm_find_most_appropriate_phase(struct sdhci_host * host,u8 * phase_table,u8 total_phases)
- Line: 515

### msm_get_clock_mult_for_bus_mode
- Return type: static unsigned int
- Signature: msm_get_clock_mult_for_bus_mode(struct sdhci_host * host,unsigned int clock,unsigned int timing)
- Line: 359

### msm_hc_select_default
- Return type: static void
- Signature: msm_hc_select_default(struct sdhci_host * host)
- Line: 803

### msm_hc_select_hs400
- Return type: static void
- Signature: msm_hc_select_hs400(struct sdhci_host * host)
- Line: 843

### msm_init_cm_dll
- Return type: static int
- Signature: msm_init_cm_dll(struct sdhci_host * host)
- Line: 648

### msm_set_clock_rate_for_bus_mode
- Return type: static void
- Signature: msm_set_clock_rate_for_bus_mode(struct sdhci_host * host,unsigned int clock,unsigned int timing)
- Line: 378

### msm_toggle_vqmmc
- Return type: static int
- Signature: msm_toggle_vqmmc(struct sdhci_msm_host * msm_host,struct mmc_host * mmc,bool level)
- Line: 1489

### sdhci_msm_cdclp533_calibration
- Return type: static int
- Signature: sdhci_msm_cdclp533_calibration(struct sdhci_host * host)
- Line: 925

### sdhci_msm_check_power_status
- Return type: static void
- Signature: sdhci_msm_check_power_status(struct sdhci_host * host,u32 req_type)
- Line: 1592

### sdhci_msm_cm_dll_sdc4_calibration
- Return type: static int
- Signature: sdhci_msm_cm_dll_sdc4_calibration(struct sdhci_host * host)
- Line: 1028

### sdhci_msm_complete_pwr_irq_wait
- Return type: static void
- Signature: sdhci_msm_complete_pwr_irq_wait(struct sdhci_msm_host * msm_host)
- Line: 1577

### sdhci_msm_cqe_add_host
- Return type: static int
- Signature: sdhci_msm_cqe_add_host(struct sdhci_host * host,struct platform_device * pdev)
- Line: 2238

### sdhci_msm_cqe_disable
- Return type: static void
- Signature: sdhci_msm_cqe_disable(struct mmc_host * mmc,bool recovery)
- Line: 2182

### sdhci_msm_cqe_enable
- Return type: static void
- Signature: sdhci_msm_cqe_enable(struct mmc_host * mmc)
- Line: 2172

### sdhci_msm_cqe_irq
- Return type: static u32
- Signature: sdhci_msm_cqe_irq(struct sdhci_host * host,u32 intmask)
- Line: 2160

### sdhci_msm_dump_pwr_ctrl_regs
- Return type: static void
- Signature: sdhci_msm_dump_pwr_ctrl_regs(struct sdhci_host * host)
- Line: 1664

### sdhci_msm_dump_vendor_regs
- Return type: static void
- Signature: sdhci_msm_dump_vendor_regs(struct sdhci_host * host)
- Line: 2495

### sdhci_msm_execute_tuning
- Return type: static int
- Signature: sdhci_msm_execute_tuning(struct mmc_host * mmc,u32 opcode)
- Line: 1214

### sdhci_msm_gcc_reset
- Return type: static int
- Signature: sdhci_msm_gcc_reset(struct device * dev,struct sdhci_host * host)
- Line: 2606

### sdhci_msm_get_max_clock
- Return type: static unsigned int
- Signature: sdhci_msm_get_max_clock(struct sdhci_host * host)
- Line: 1836

### sdhci_msm_get_min_clock
- Return type: static unsigned int
- Signature: sdhci_msm_get_min_clock(struct sdhci_host * host)
- Line: 1845

### sdhci_msm_get_of_property
- Return type: static void
- Signature: sdhci_msm_get_of_property(struct platform_device * pdev,struct sdhci_host * host)
- Line: 2589

### sdhci_msm_handle_pwr_irq
- Return type: static void
- Signature: sdhci_msm_handle_pwr_irq(struct sdhci_host * host,int irq)
- Line: 1678

### sdhci_msm_hc_select_mode
- Return type: static void
- Signature: sdhci_msm_hc_select_mode(struct sdhci_host * host)
- Line: 914

### sdhci_msm_host_from_crypto_profile
- Return type: static sdhci_msm_host *
- Signature: sdhci_msm_host_from_crypto_profile(struct blk_crypto_profile * profile)
- Line: 1988

### sdhci_msm_hs400
- Return type: static void
- Signature: sdhci_msm_hs400(struct sdhci_host * host,struct mmc_ios * ios)
- Line: 1336

### sdhci_msm_hs400_dll_calibration
- Return type: static int
- Signature: sdhci_msm_hs400_dll_calibration(struct sdhci_host * host)
- Line: 1104

### sdhci_msm_ice_cfg
- Return type: static void
- Signature: sdhci_msm_ice_cfg(struct sdhci_host * host,struct mmc_request * mrq)
- Line: 2074

### sdhci_msm_ice_derive_sw_secret
- Return type: static int
- Signature: sdhci_msm_ice_derive_sw_secret(struct blk_crypto_profile * profile,const u8 * eph_key,size_t eph_key_size,u8 sw_secret[BLK_CRYPTO_SW_SECRET_SIZE])
- Line: 2022

### sdhci_msm_ice_enable
- Return type: static void
- Signature: sdhci_msm_ice_enable(struct sdhci_msm_host * msm_host)
- Line: 2137

### sdhci_msm_ice_enable
- Return type: static void
- Signature: sdhci_msm_ice_enable(struct sdhci_msm_host * msm_host)
- Line: 1965

### sdhci_msm_ice_generate_key
- Return type: static int
- Signature: sdhci_msm_ice_generate_key(struct blk_crypto_profile * profile,u8 lt_key[BLK_CRYPTO_MAX_HW_WRAPPED_KEY_SIZE])
- Line: 2041

### sdhci_msm_ice_import_key
- Return type: static int
- Signature: sdhci_msm_ice_import_key(struct blk_crypto_profile * profile,const u8 * raw_key,size_t raw_key_size,u8 lt_key[BLK_CRYPTO_MAX_HW_WRAPPED_KEY_SIZE])
- Line: 2032

### sdhci_msm_ice_init
- Return type: static int
- Signature: sdhci_msm_ice_init(struct sdhci_msm_host * msm_host,struct cqhci_host * cq_host)
- Line: 2131

### sdhci_msm_ice_init
- Return type: static int
- Signature: sdhci_msm_ice_init(struct sdhci_msm_host * msm_host,struct cqhci_host * cq_host)
- Line: 1905

### sdhci_msm_ice_keyslot_evict
- Return type: static int
- Signature: sdhci_msm_ice_keyslot_evict(struct blk_crypto_profile * profile,const struct blk_crypto_key * key,unsigned int slot)
- Line: 2012

### sdhci_msm_ice_keyslot_program
- Return type: static int
- Signature: sdhci_msm_ice_keyslot_program(struct blk_crypto_profile * profile,const struct blk_crypto_key * key,unsigned int slot)
- Line: 2002

### sdhci_msm_ice_prepare_key
- Return type: static int
- Signature: sdhci_msm_ice_prepare_key(struct blk_crypto_profile * profile,const u8 * lt_key,size_t lt_key_size,u8 eph_key[BLK_CRYPTO_MAX_HW_WRAPPED_KEY_SIZE])
- Line: 2049

### sdhci_msm_ice_resume
- Return type: static int
- Signature: sdhci_msm_ice_resume(struct sdhci_msm_host * msm_host)
- Line: 2142

### sdhci_msm_ice_resume
- Return type: static int
- Signature: sdhci_msm_ice_resume(struct sdhci_msm_host * msm_host)
- Line: 1971

### sdhci_msm_ice_suspend
- Return type: static int
- Signature: sdhci_msm_ice_suspend(struct sdhci_msm_host * msm_host)
- Line: 2148

### sdhci_msm_ice_suspend
- Return type: static int
- Signature: sdhci_msm_ice_suspend(struct sdhci_msm_host * msm_host)
- Line: 1979

### sdhci_msm_init_pwr_irq_wait
- Return type: static void
- Signature: sdhci_msm_init_pwr_irq_wait(struct sdhci_msm_host * msm_host)
- Line: 1572

### sdhci_msm_is_tuning_needed
- Return type: static bool
- Signature: sdhci_msm_is_tuning_needed(struct sdhci_host * host)
- Line: 1147

### sdhci_msm_mci_variant_readl_relaxed
- Return type: static u32
- Signature: sdhci_msm_mci_variant_readl_relaxed(struct sdhci_host * host,u32 offset)
- Line: 329

### sdhci_msm_mci_variant_writel_relaxed
- Return type: static void
- Signature: sdhci_msm_mci_variant_writel_relaxed(u32 val,struct sdhci_host * host,u32 offset)
- Line: 344

### sdhci_msm_non_cqe_ice_init
- Return type: static void
- Signature: sdhci_msm_non_cqe_ice_init(struct sdhci_host * host)
- Line: 2058

### sdhci_msm_probe
- Return type: static int
- Signature: sdhci_msm_probe(struct platform_device * pdev)
- Line: 2644

### sdhci_msm_pwr_irq
- Return type: static irqreturn_t
- Signature: sdhci_msm_pwr_irq(int irq,void * data)
- Line: 1822

### sdhci_msm_register_vreg
- Return type: static int
- Signature: sdhci_msm_register_vreg(struct sdhci_msm_host * msm_host)
- Line: 2426

### sdhci_msm_remove
- Return type: static void
- Signature: sdhci_msm_remove(struct platform_device * pdev)
- Line: 2914

### sdhci_msm_request
- Return type: static void
- Signature: sdhci_msm_request(struct mmc_host * mmc,struct mmc_request * mrq)
- Line: 2109

### sdhci_msm_restore_sdr_dll_config
- Return type: static int
- Signature: sdhci_msm_restore_sdr_dll_config(struct sdhci_host * host)
- Line: 1169

### sdhci_msm_runtime_resume
- Return type: static int
- Signature: sdhci_msm_runtime_resume(struct device * dev)
- Line: 2953

### sdhci_msm_runtime_suspend
- Return type: static int
- Signature: sdhci_msm_runtime_suspend(struct device * dev)
- Line: 2934

### sdhci_msm_set_cdr
- Return type: static void
- Signature: sdhci_msm_set_cdr(struct sdhci_host * host,bool enable)
- Line: 1193

### sdhci_msm_set_clock
- Return type: static void
- Signature: sdhci_msm_set_clock(struct sdhci_host * host,unsigned int clock)
- Line: 1877

### sdhci_msm_set_pincfg
- Return type: static int
- Signature: sdhci_msm_set_pincfg(struct sdhci_msm_host * msm_host,bool level)
- Line: 1431

### sdhci_msm_set_regulator_caps
- Return type: static void
- Signature: sdhci_msm_set_regulator_caps(struct sdhci_msm_host * msm_host)
- Line: 2384

### sdhci_msm_set_timeout
- Return type: static void
- Signature: sdhci_msm_set_timeout(struct sdhci_host * host,struct mmc_command * cmd)
- Line: 2213

### sdhci_msm_set_uhs_signaling
- Return type: static void
- Signature: sdhci_msm_set_uhs_signaling(struct sdhci_host * host,unsigned int uhs)
- Line: 1354

### sdhci_msm_set_vmmc
- Return type: static int
- Signature: sdhci_msm_set_vmmc(struct sdhci_msm_host * msm_host,struct mmc_host * mmc,bool hpm)
- Line: 1478

### sdhci_msm_set_vqmmc
- Return type: static int
- Signature: sdhci_msm_set_vqmmc(struct sdhci_msm_host * msm_host,struct mmc_host * mmc,bool level)
- Line: 1542

### sdhci_msm_start_signal_voltage_switch
- Return type: static int
- Signature: sdhci_msm_start_signal_voltage_switch(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 2439

### sdhci_msm_v5_variant_readl_relaxed
- Return type: static u32
- Signature: sdhci_msm_v5_variant_readl_relaxed(struct sdhci_host * host,u32 offset)
- Line: 338

### sdhci_msm_v5_variant_writel_relaxed
- Return type: static void
- Signature: sdhci_msm_v5_variant_writel_relaxed(u32 val,struct sdhci_host * host,u32 offset)
- Line: 353

### sdhci_msm_writeb
- Return type: static void
- Signature: sdhci_msm_writeb(struct sdhci_host * host,u8 val,int reg)
- Line: 2372

### sdhci_msm_writew
- Return type: static void
- Signature: sdhci_msm_writew(struct sdhci_host * host,u16 val,int reg)
- Line: 2360

### sdhci_priv_msm_offset
- Return type: static const struct sdhci_msm_offset *
- Signature: sdhci_priv_msm_offset(struct sdhci_host * host)
- Line: 317

## Structs (4)

### sdhci_msm_host
- Line: 280
- Members:
  - core_hc_mode: u32
  - core_mci_data_cnt: u32
  - core_mci_status: u32
  - core_mci_fifo_cnt: u32
  - core_mci_version: u32
  - core_generics: u32
  - core_testbus_config: u32
  - core_testbus_sel2_bit: u32
  - core_testbus_ena: u32
  - core_testbus_sel2: u32
  - core_pwrctl_status: u32
  - core_pwrctl_mask: u32
  - core_pwrctl_clear: u32
  - core_pwrctl_ctl: u32
  - core_sdcc_debug_reg: u32
  - core_dll_config: u32
  - core_dll_status: u32
  - core_vendor_spec: u32
  - core_vendor_spec_adma_err_addr0: u32
  - core_vendor_spec_adma_err_addr1: u32
  - core_vendor_spec_func2: u32
  - core_vendor_spec_capabilities0: u32
  - core_ddr_200_cfg: u32
  - core_vendor_spec3: u32
  - core_dll_config_2: u32
  - core_dll_config_3: u32
  - core_ddr_config_old: u32
  - core_ddr_config: u32
  - core_dll_usr_ctl: u32
  - msm_readl_relaxed: u32 (*)(struct sdhci_host * host,u32 offset)
  - msm_writel_relaxed: void (*)(u32 val,struct sdhci_host * host,u32 offset)
  - mci_removed: bool
  - restore_dll_config: bool
  - var_ops: const struct sdhci_msm_variant_ops *
  - offset: const struct sdhci_msm_offset *
  - pdev: platform_device *
  - core_mem: void __iomem *
  - pwr_irq: int
  - bus_clk: clk *
  - xo_clk: clk *
  - bulk_clks: clk_bulk_data[4]
  - ice: qcom_ice *
  - clk_rate: unsigned long
  - mmc: mmc_host *
  - use_14lpp_dll_reset: bool
  - tuning_done: bool
  - calibration_done: bool
  - saved_tuning_phase: u8
  - use_cdclp533: bool
  - curr_pwr_state: u32
  - curr_io_level: u32
  - pwr_irq_wait: wait_queue_head_t
  - pwr_irq_flag: bool
  - caps_0: u32
  - mci_removed: bool
  - restore_dll_config: bool
  - var_ops: const struct sdhci_msm_variant_ops *
  - offset: const struct sdhci_msm_offset *
  - use_cdr: bool
  - transfer_mode: u32
  - updated_ddr_cfg: bool
  - uses_tassadar_dll: bool
  - dll_config: u32
  - ddr_config: u32
  - vqmmc_enabled: bool
  - non_cqe_ice_init_done: bool

### sdhci_msm_offset
- Line: 171
- Members:
  - core_hc_mode: u32
  - core_mci_data_cnt: u32
  - core_mci_status: u32
  - core_mci_fifo_cnt: u32
  - core_mci_version: u32
  - core_generics: u32
  - core_testbus_config: u32
  - core_testbus_sel2_bit: u32
  - core_testbus_ena: u32
  - core_testbus_sel2: u32
  - core_pwrctl_status: u32
  - core_pwrctl_mask: u32
  - core_pwrctl_clear: u32
  - core_pwrctl_ctl: u32
  - core_sdcc_debug_reg: u32
  - core_dll_config: u32
  - core_dll_status: u32
  - core_vendor_spec: u32
  - core_vendor_spec_adma_err_addr0: u32
  - core_vendor_spec_adma_err_addr1: u32
  - core_vendor_spec_func2: u32
  - core_vendor_spec_capabilities0: u32
  - core_ddr_200_cfg: u32
  - core_vendor_spec3: u32
  - core_dll_config_2: u32
  - core_dll_config_3: u32
  - core_ddr_config_old: u32
  - core_ddr_config: u32
  - core_dll_usr_ctl: u32
  - msm_readl_relaxed: u32 (*)(struct sdhci_host * host,u32 offset)
  - msm_writel_relaxed: void (*)(u32 val,struct sdhci_host * host,u32 offset)
  - mci_removed: bool
  - restore_dll_config: bool
  - var_ops: const struct sdhci_msm_variant_ops *
  - offset: const struct sdhci_msm_offset *
  - pdev: platform_device *
  - core_mem: void __iomem *
  - pwr_irq: int
  - bus_clk: clk *
  - xo_clk: clk *
  - bulk_clks: clk_bulk_data[4]
  - ice: qcom_ice *
  - clk_rate: unsigned long
  - mmc: mmc_host *
  - use_14lpp_dll_reset: bool
  - tuning_done: bool
  - calibration_done: bool
  - saved_tuning_phase: u8
  - use_cdclp533: bool
  - curr_pwr_state: u32
  - curr_io_level: u32
  - pwr_irq_wait: wait_queue_head_t
  - pwr_irq_flag: bool
  - caps_0: u32
  - mci_removed: bool
  - restore_dll_config: bool
  - var_ops: const struct sdhci_msm_variant_ops *
  - offset: const struct sdhci_msm_offset *
  - use_cdr: bool
  - transfer_mode: u32
  - updated_ddr_cfg: bool
  - uses_tassadar_dll: bool
  - dll_config: u32
  - ddr_config: u32
  - vqmmc_enabled: bool
  - non_cqe_ice_init_done: bool

### sdhci_msm_variant_info
- Line: 273
- Members:
  - core_hc_mode: u32
  - core_mci_data_cnt: u32
  - core_mci_status: u32
  - core_mci_fifo_cnt: u32
  - core_mci_version: u32
  - core_generics: u32
  - core_testbus_config: u32
  - core_testbus_sel2_bit: u32
  - core_testbus_ena: u32
  - core_testbus_sel2: u32
  - core_pwrctl_status: u32
  - core_pwrctl_mask: u32
  - core_pwrctl_clear: u32
  - core_pwrctl_ctl: u32
  - core_sdcc_debug_reg: u32
  - core_dll_config: u32
  - core_dll_status: u32
  - core_vendor_spec: u32
  - core_vendor_spec_adma_err_addr0: u32
  - core_vendor_spec_adma_err_addr1: u32
  - core_vendor_spec_func2: u32
  - core_vendor_spec_capabilities0: u32
  - core_ddr_200_cfg: u32
  - core_vendor_spec3: u32
  - core_dll_config_2: u32
  - core_dll_config_3: u32
  - core_ddr_config_old: u32
  - core_ddr_config: u32
  - core_dll_usr_ctl: u32
  - msm_readl_relaxed: u32 (*)(struct sdhci_host * host,u32 offset)
  - msm_writel_relaxed: void (*)(u32 val,struct sdhci_host * host,u32 offset)
  - mci_removed: bool
  - restore_dll_config: bool
  - var_ops: const struct sdhci_msm_variant_ops *
  - offset: const struct sdhci_msm_offset *
  - pdev: platform_device *
  - core_mem: void __iomem *
  - pwr_irq: int
  - bus_clk: clk *
  - xo_clk: clk *
  - bulk_clks: clk_bulk_data[4]
  - ice: qcom_ice *
  - clk_rate: unsigned long
  - mmc: mmc_host *
  - use_14lpp_dll_reset: bool
  - tuning_done: bool
  - calibration_done: bool
  - saved_tuning_phase: u8
  - use_cdclp533: bool
  - curr_pwr_state: u32
  - curr_io_level: u32
  - pwr_irq_wait: wait_queue_head_t
  - pwr_irq_flag: bool
  - caps_0: u32
  - mci_removed: bool
  - restore_dll_config: bool
  - var_ops: const struct sdhci_msm_variant_ops *
  - offset: const struct sdhci_msm_offset *
  - use_cdr: bool
  - transfer_mode: u32
  - updated_ddr_cfg: bool
  - uses_tassadar_dll: bool
  - dll_config: u32
  - ddr_config: u32
  - vqmmc_enabled: bool
  - non_cqe_ice_init_done: bool

### sdhci_msm_variant_ops
- Line: 263
- Members:
  - core_hc_mode: u32
  - core_mci_data_cnt: u32
  - core_mci_status: u32
  - core_mci_fifo_cnt: u32
  - core_mci_version: u32
  - core_generics: u32
  - core_testbus_config: u32
  - core_testbus_sel2_bit: u32
  - core_testbus_ena: u32
  - core_testbus_sel2: u32
  - core_pwrctl_status: u32
  - core_pwrctl_mask: u32
  - core_pwrctl_clear: u32
  - core_pwrctl_ctl: u32
  - core_sdcc_debug_reg: u32
  - core_dll_config: u32
  - core_dll_status: u32
  - core_vendor_spec: u32
  - core_vendor_spec_adma_err_addr0: u32
  - core_vendor_spec_adma_err_addr1: u32
  - core_vendor_spec_func2: u32
  - core_vendor_spec_capabilities0: u32
  - core_ddr_200_cfg: u32
  - core_vendor_spec3: u32
  - core_dll_config_2: u32
  - core_dll_config_3: u32
  - core_ddr_config_old: u32
  - core_ddr_config: u32
  - core_dll_usr_ctl: u32
  - msm_readl_relaxed: u32 (*)(struct sdhci_host * host,u32 offset)
  - msm_writel_relaxed: void (*)(u32 val,struct sdhci_host * host,u32 offset)
  - mci_removed: bool
  - restore_dll_config: bool
  - var_ops: const struct sdhci_msm_variant_ops *
  - offset: const struct sdhci_msm_offset *
  - pdev: platform_device *
  - core_mem: void __iomem *
  - pwr_irq: int
  - bus_clk: clk *
  - xo_clk: clk *
  - bulk_clks: clk_bulk_data[4]
  - ice: qcom_ice *
  - clk_rate: unsigned long
  - mmc: mmc_host *
  - use_14lpp_dll_reset: bool
  - tuning_done: bool
  - calibration_done: bool
  - saved_tuning_phase: u8
  - use_cdclp533: bool
  - curr_pwr_state: u32
  - curr_io_level: u32
  - pwr_irq_wait: wait_queue_head_t
  - pwr_irq_flag: bool
  - caps_0: u32
  - mci_removed: bool
  - restore_dll_config: bool
  - var_ops: const struct sdhci_msm_variant_ops *
  - offset: const struct sdhci_msm_offset *
  - use_cdr: bool
  - transfer_mode: u32
  - updated_ddr_cfg: bool
  - uses_tassadar_dll: bool
  - dll_config: u32
  - ddr_config: u32
  - vqmmc_enabled: bool
  - non_cqe_ice_init_done: bool

## Variables (15)

- static **mci_var_ops** : const struct sdhci_msm_variant_ops (line 2521)
- static **sdhci_msm_cqhci_ops** : const struct cqhci_host_ops (line 2230)
- static **sdhci_msm_crypto_ops** : const struct blk_crypto_ll_ops (line 2120)
- static **sdhci_msm_crypto_ops** : const struct blk_crypto_ll_ops (line 1903)
- static **sdhci_msm_driver** : platform_driver (line 2993)
- static **sdhci_msm_dt_match** : const struct of_device_id[] (line 2549)
- static **sdhci_msm_mci_offset** : const struct sdhci_msm_offset (line 233)
- static **sdhci_msm_mci_var** : const struct sdhci_msm_variant_info (line 2531)
- static **sdhci_msm_ops** : const struct sdhci_ops (line 2564)
- static **sdhci_msm_pdata** : const struct sdhci_pltfm_data (line 2579)
- static **sdhci_msm_pm_ops** : const struct dev_pm_ops (line 2988)
- static **sdhci_msm_v5_offset** : const struct sdhci_msm_offset (line 203)
- static **sdhci_msm_v5_var** : const struct sdhci_msm_variant_info (line 2536)
- static **sdm845_sdhci_var** : const struct sdhci_msm_variant_info (line 2542)
- static **v5_var_ops** : const struct sdhci_msm_variant_ops (line 2526)

## Macros (105)

- **BIAS_OK_SIGNAL** (line 71)
- **CDR_SELEXT_MASK** (line 129)
- **CDR_SELEXT_SHIFT** (line 128)
- **CMUX_SHIFT_PHASE_MASK** (line 131)
- **CMUX_SHIFT_PHASE_SHIFT** (line 130)
- **CORE_1_8V_SUPPORT** (line 89)
- **CORE_3_0V_SUPPORT** (line 88)
- **CORE_CALIBRATION_DONE** (line 107)
- **CORE_CDC_ERROR_CODE_MASK** (line 109)
- **CORE_CDC_OFFSET_CFG** (line 103)
- **CORE_CDC_SLAVE_DDA_CFG** (line 105)
- **CORE_CDC_SWITCH_BYPASS_OFF** (line 112)
- **CORE_CDC_SWITCH_RC_EN** (line 113)
- **CORE_CDC_T4_DLY_SEL** (line 115)
- **CORE_CDR_EN** (line 57)
- **CORE_CDR_EXT_EN** (line 59)
- **CORE_CK_OUT_EN** (line 58)
- **CORE_CLK_PWRSAVE** (line 77)
- **CORE_CMDIN_RCLK_EN** (line 116)
- **CORE_CMD_DAT_TRACK_SEL** (line 62)
- **CORE_CSR_CDC_CAL_TIMER_CFG0** (line 97)
- **CORE_CSR_CDC_CAL_TIMER_CFG1** (line 100)
- **CORE_CSR_CDC_COARSE_CAL_CFG** (line 102)
- **CORE_CSR_CDC_CTLR_CFG0** (line 92)
- **CORE_CSR_CDC_CTLR_CFG1** (line 96)
- **CORE_CSR_CDC_DELAY_CFG** (line 104)
- **CORE_CSR_CDC_GEN_CFG** (line 111)
- **CORE_CSR_CDC_REFCOUNT_CFG** (line 101)
- **CORE_CSR_CDC_STATUS0** (line 106)
- **CORE_DDR_CAL_EN** (line 64)
- **CORE_DDR_DLL_LOCK** (line 55)
- **CORE_DLL_CLOCK_DISABLE** (line 66)
- **CORE_DLL_EN** (line 56)
- **CORE_DLL_LOCK** (line 54)
- **CORE_DLL_PDN** (line 60)
- **CORE_DLL_RST** (line 61)
- **CORE_FLL_CYCLE_CNT** (line 65)
- **CORE_FREQ_100MHZ** (line 126)
- **CORE_HC_MCLK_SEL_DFLT** (line 78)
- **CORE_HC_MCLK_SEL_HS400** (line 79)
- **CORE_HC_MCLK_SEL_MASK** (line 80)
- **CORE_HC_SELECT_IN_EN** (line 83)
- **CORE_HC_SELECT_IN_HS400** (line 85)
- **CORE_HC_SELECT_IN_MASK** (line 86)
- **CORE_HC_SELECT_IN_SDR50** (line 84)
- **CORE_HW_AUTOCAL_ENA** (line 94)
- **CORE_IO_PAD_PWR_SWITCH** (line 82)
- **CORE_IO_PAD_PWR_SWITCH_EN** (line 81)
- **CORE_MCI_GENERICS** (line 32)
- **CORE_MCI_VERSION** (line 27)
- **CORE_POWER** (line 36)
- **CORE_PWRCTL_BUS_FAIL** (line 45)
- **CORE_PWRCTL_BUS_OFF** (line 40)
- **CORE_PWRCTL_BUS_ON** (line 41)
- **CORE_PWRCTL_BUS_SUCCESS** (line 44)
- **CORE_PWRCTL_IO_FAIL** (line 47)
- **CORE_PWRCTL_IO_HIGH** (line 43)
- **CORE_PWRCTL_IO_LOW** (line 42)
- **CORE_PWRCTL_IO_SUCCESS** (line 46)
- **CORE_PWRSAVE_DLL** (line 119)
- **CORE_START_CDC_TRAFFIC** (line 117)
- **CORE_SW_RST** (line 37)
- **CORE_SW_TRIG_FULL_CALIB** (line 93)
- **CORE_TIMER_ENA** (line 98)
- **CORE_VENDOR_SPEC_POR_VAL** (line 76)
- **CORE_VERSION_MAJOR_MASK** (line 29)
- **CORE_VERSION_MAJOR_SHIFT** (line 28)
- **CORE_VERSION_MINOR_MASK** (line 30)
- **CORE_VOLT_SUPPORT** (line 90)
- **CQHCI_VENDOR_CFG1** (line 157)
- **CQHCI_VENDOR_DIS_RST_ON_CQ_EN** (line 158)
- **CRYPTO_GENERAL_ENABLE** (line 165)
- **DDR_CONFIG_POR_VAL** (line 121)
- **DISABLE_CRYPTO** (line 164)
- **DLL_CONFIG_3_HIGH_FREQ_VAL** (line 74)
- **DLL_CONFIG_3_LOW_FREQ_VAL** (line 73)
- **DLL_USR_CTL_POR_VAL** (line 68)
- **DRIVER_NAME** (line 2491)
- **ENABLE_DLL_LOCK_STATUS** (line 69)
- **FF_CLK_SW_RST_DIS** (line 38)
- **FINE_TUNE_MODE_EN** (line 70)
- **HC_MODE_EN** (line 35)
- **HC_VENDOR_SPECIFIC_FUNC4** (line 166)
- **ICE_HCI_PARAM_CCI** (line 168)
- **ICE_HCI_PARAM_CE** (line 169)
- **INT_MASK** (line 52)
- **INVALID_TUNING_PHASE** (line 124)
- **MAX_PHASES** (line 53)
- **MMC_VMMC_MAX_LOAD_UA** (line 139)
- **MMC_VQMMC_MAX_LOAD_UA** (line 142)
- **MSM_MMC_AUTOSUSPEND_DELAY_MS** (line 133)
- **MSM_PWR_IRQ_TIMEOUT_MS** (line 136)
- **NONCQ_CRYPTO_DUN** (line 162)
- **NONCQ_CRYPTO_PARM** (line 161)
- **REQ_BUS_OFF** (line 48)
- **REQ_BUS_ON** (line 49)
- **REQ_IO_HIGH** (line 51)
- **REQ_IO_LOW** (line 50)
- **SDHCI_MSM_DUMP**(f,x...) (line 2492)
- **SDHCI_MSM_MIN_CLOCK** (line 125)
- **SD_VMMC_MAX_LOAD_UA** (line 145)
- **SD_VQMMC_MAX_LOAD_UA** (line 148)
- **SWITCHABLE_SIGNALING_VOLTAGE** (line 33)
- **msm_host_readl**(msm_host,host,offset) (line 150)
- **msm_host_writel**(msm_host,val,host,offset) (line 153)
