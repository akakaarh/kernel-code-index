# drivers/mmc/host/sdhci_f_sdh30.c

Subsystem: drivers/mmc

## Functions (6)

### sdhci_f_sdh30_get_min_clock
- Return type: static unsigned int
- Signature: sdhci_f_sdh30_get_min_clock(struct sdhci_host * host)
- Line: 67

### sdhci_f_sdh30_probe
- Return type: static int
- Signature: sdhci_f_sdh30_probe(struct platform_device * pdev)
- Line: 113

### sdhci_f_sdh30_remove
- Return type: static void
- Signature: sdhci_f_sdh30_remove(struct platform_device * pdev)
- Line: 204

### sdhci_f_sdh30_reset
- Return type: static void
- Signature: sdhci_f_sdh30_reset(struct sdhci_host * host,u8 mask)
- Line: 72

### sdhci_f_sdh30_soft_voltage_switch
- Return type: static void
- Signature: sdhci_f_sdh30_soft_voltage_switch(struct sdhci_host * host)
- Line: 39

### sdhci_f_sdhost_priv
- Return type: static void *
- Signature: sdhci_f_sdhost_priv(struct sdhci_host * host)
- Line: 32

## Structs (1)

### f_sdhost_priv
- Line: 23
- Members:
  - clk_iface: clk *
  - clk: clk *
  - rst: reset_control *
  - vendor_hs200: u32
  - dev: device *
  - enable_cmd_dat_delay: bool
  - clk_iface: clk *
  - clk: clk *
  - dev: device *
  - enable_cmd_dat_delay: bool

## Variables (5)

- static **f_sdh30_acpi_ids** : const struct acpi_device_id[] (line 229)
- static **f_sdh30_dt_ids** : const struct of_device_id[] (line 220)
- static **sdhci_f_sdh30_driver** : platform_driver (line 236)
- static **sdhci_f_sdh30_ops** : const struct sdhci_ops (line 96)
- static **sdhci_f_sdh30_pltfm_data** : const struct sdhci_pltfm_data (line 105)
