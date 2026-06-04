# drivers/mmc/host/sdhci-xenon.c

Subsystem: drivers/mmc

## Functions (28)

### xenon_disable_sdhc
- Return type: static void
- Signature: xenon_disable_sdhc(struct sdhci_host * host,unsigned char sdhc_id)
- Line: 103

### xenon_enable_internal_clk
- Return type: static int
- Signature: xenon_enable_internal_clk(struct sdhci_host * host)
- Line: 27

### xenon_enable_sdhc
- Return type: static void
- Signature: xenon_enable_sdhc(struct sdhci_host * host,unsigned char sdhc_id)
- Line: 85

### xenon_enable_sdhc_parallel_tran
- Return type: static void
- Signature: xenon_enable_sdhc_parallel_tran(struct sdhci_host * host,unsigned char sdhc_id)
- Line: 114

### xenon_enable_sdio_irq
- Return type: static void
- Signature: xenon_enable_sdio_irq(struct mmc_host * mmc,int enable)
- Line: 376

### xenon_execute_tuning
- Return type: static int
- Signature: xenon_execute_tuning(struct mmc_host * mmc,u32 opcode)
- Line: 357

### xenon_get_max_clock
- Return type: static unsigned int
- Signature: xenon_get_max_clock(struct sdhci_host * host)
- Line: 248

### xenon_init_card
- Return type: static void
- Signature: xenon_init_card(struct mmc_host * mmc,struct mmc_card * card)
- Line: 347

### xenon_mask_cmd_conflict_err
- Return type: static void
- Signature: xenon_mask_cmd_conflict_err(struct sdhci_host * host)
- Line: 125

### xenon_probe
- Return type: static int
- Signature: xenon_probe(struct platform_device * pdev)
- Line: 509

### xenon_probe_params
- Return type: static int
- Signature: xenon_probe_params(struct platform_device * pdev)
- Line: 418

### xenon_remove
- Return type: static void
- Signature: xenon_remove(struct platform_device * pdev)
- Line: 608

### xenon_replace_mmc_host_ops
- Return type: static void
- Signature: xenon_replace_mmc_host_ops(struct sdhci_host * host)
- Line: 402

### xenon_reset
- Return type: static void
- Signature: xenon_reset(struct sdhci_host * host,u8 mask)
- Line: 185

### xenon_reset_exit
- Return type: static void
- Signature: xenon_reset_exit(struct sdhci_host * host,unsigned char sdhc_id,u8 mask)
- Line: 163

### xenon_retune_setup
- Return type: static void
- Signature: xenon_retune_setup(struct sdhci_host * host)
- Line: 134

### xenon_runtime_resume
- Return type: static int
- Signature: xenon_runtime_resume(struct device * dev)
- Line: 659

### xenon_runtime_suspend
- Return type: static int
- Signature: xenon_runtime_suspend(struct device * dev)
- Line: 638

### xenon_sdhc_prepare
- Return type: static int
- Signature: xenon_sdhc_prepare(struct sdhci_host * host)
- Line: 476

### xenon_sdhc_unprepare
- Return type: static void
- Signature: xenon_sdhc_unprepare(struct sdhci_host * host)
- Line: 499

### xenon_set_acg
- Return type: static void
- Signature: xenon_set_acg(struct sdhci_host * host,bool enable)
- Line: 72

### xenon_set_ios
- Return type: static void
- Signature: xenon_set_ios(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 278

### xenon_set_power
- Return type: static void
- Signature: xenon_set_power(struct sdhci_host * host,unsigned char mode,unsigned short vdd)
- Line: 224

### xenon_set_sdclk_off_idle
- Return type: static void
- Signature: xenon_set_sdclk_off_idle(struct sdhci_host * host,unsigned char sdhc_id,bool enable)
- Line: 54

### xenon_set_uhs_signaling
- Return type: static void
- Signature: xenon_set_uhs_signaling(struct sdhci_host * host,unsigned int timing)
- Line: 198

### xenon_start_signal_voltage_switch
- Return type: static int
- Signature: xenon_start_signal_voltage_switch(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 313

### xenon_suspend
- Return type: static int
- Signature: xenon_suspend(struct device * dev)
- Line: 625

### xenon_voltage_switch
- Return type: static void
- Signature: xenon_voltage_switch(struct sdhci_host * host)
- Line: 242

## Variables (6)

- static **sdhci_xenon_acpi_ids** : const struct acpi_device_id[] (line 702)
- static **sdhci_xenon_dev_pm_ops** : const struct dev_pm_ops (line 686)
- static **sdhci_xenon_driver** : platform_driver (line 711)
- static **sdhci_xenon_dt_ids** : const struct of_device_id[] (line 691)
- static **sdhci_xenon_ops** : const struct sdhci_ops (line 258)
- static **sdhci_xenon_pdata** : const struct sdhci_pltfm_data (line 268)
