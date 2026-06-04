# drivers/mmc/host/sdhci-iproc.c

Subsystem: drivers/mmc

## Functions (10)

### sdhci_iproc_bcm2711_get_min_clock
- Return type: static unsigned int
- Signature: sdhci_iproc_bcm2711_get_min_clock(struct sdhci_host * host)
- Line: 179

### sdhci_iproc_get_max_clock
- Return type: static unsigned int
- Signature: sdhci_iproc_get_max_clock(struct sdhci_host * host)
- Line: 157

### sdhci_iproc_probe
- Return type: static int
- Signature: sdhci_iproc_probe(struct platform_device * pdev)
- Line: 358

### sdhci_iproc_readb
- Return type: static u8
- Signature: sdhci_iproc_readb(struct sdhci_host * host,int reg)
- Line: 64

### sdhci_iproc_readl
- Return type: static u32
- Signature: sdhci_iproc_readl(struct sdhci_host * host,int reg)
- Line: 34

### sdhci_iproc_readw
- Return type: static u16
- Signature: sdhci_iproc_readw(struct sdhci_host * host,int reg)
- Line: 43

### sdhci_iproc_shutdown
- Return type: static void
- Signature: sdhci_iproc_shutdown(struct platform_device * pdev)
- Line: 403

### sdhci_iproc_writeb
- Return type: static void
- Signature: sdhci_iproc_writeb(struct sdhci_host * host,u8 val,int reg)
- Line: 147

### sdhci_iproc_writel
- Return type: static void
- Signature: sdhci_iproc_writel(struct sdhci_host * host,u32 val,int reg)
- Line: 71

### sdhci_iproc_writew
- Return type: static void
- Signature: sdhci_iproc_writew(struct sdhci_host * host,u16 val,int reg)
- Line: 106

## Structs (2)

### sdhci_iproc_data
- Line: 16
- Members:
  - pdata: const struct sdhci_pltfm_data *
  - caps: u32
  - caps1: u32
  - mmc_caps: u32
  - missing_caps: bool
  - data: const struct sdhci_iproc_data *
  - shadow_cmd: u32
  - shadow_blk: u32
  - is_cmd_shadowed: bool
  - is_blk_shadowed: bool

### sdhci_iproc_host
- Line: 24
- Members:
  - pdata: const struct sdhci_pltfm_data *
  - caps: u32
  - caps1: u32
  - mmc_caps: u32
  - missing_caps: bool
  - data: const struct sdhci_iproc_data *
  - shadow_cmd: u32
  - shadow_blk: u32
  - is_cmd_shadowed: bool
  - is_blk_shadowed: bool

## Variables (18)

- static **bcm2711_data** : const struct sdhci_iproc_data (line 293)
- static **bcm2835_data** : const struct sdhci_iproc_data (line 260)
- static **bcm7211a0_data** : const struct sdhci_iproc_data (line 306)
- static **bcm_arasan_data** : const struct sdhci_iproc_data (line 344)
- static **iproc_cygnus_data** : const struct sdhci_iproc_data (line 213)
- static **iproc_data** : const struct sdhci_iproc_data (line 237)
- static **sdhci_bcm2711_pltfm_data** : const struct sdhci_pltfm_data (line 288)
- static **sdhci_bcm2835_pltfm_data** : const struct sdhci_pltfm_data (line 252)
- static **sdhci_bcm7211a0_pltfm_data** : const struct sdhci_pltfm_data (line 298)
- static **sdhci_bcm_arasan_data** : const struct sdhci_pltfm_data (line 336)
- static **sdhci_iproc_32only_ops** : const struct sdhci_ops (line 192)
- static **sdhci_iproc_acpi_ids** : const struct acpi_device_id[] (line 348)
- static **sdhci_iproc_bcm2711_ops** : const struct sdhci_ops (line 272)
- static **sdhci_iproc_cygnus_pltfm_data** : const struct sdhci_pltfm_data (line 206)
- static **sdhci_iproc_driver** : platform_driver (line 408)
- static **sdhci_iproc_of_match** : const struct of_device_id[] (line 321)
- static **sdhci_iproc_ops** : const struct sdhci_ops (line 184)
- static **sdhci_iproc_pltfm_data** : const struct sdhci_pltfm_data (line 229)

## Macros (2)

- **BCM7211A0_BASE_CLK_MHZ** (line 305)
- **REG_OFFSET_IN_BITS**(reg) (line 32)
