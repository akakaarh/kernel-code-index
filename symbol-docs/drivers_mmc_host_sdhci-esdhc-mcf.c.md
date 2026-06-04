# drivers/mmc/host/sdhci-esdhc-mcf.c

Subsystem: drivers/mmc

## Functions (20)

### esdhc_clrset_be
- Return type: static void
- Signature: esdhc_clrset_be(struct sdhci_host * host,u32 mask,u32 val,int reg)
- Line: 46

### esdhc_mcf_buffer_swap32
- Return type: static void
- Signature: esdhc_mcf_buffer_swap32(u32 * buf,int len)
- Line: 33

### esdhc_mcf_copy_to_bounce_buffer
- Return type: static void
- Signature: esdhc_mcf_copy_to_bounce_buffer(struct sdhci_host * host,struct mmc_data * data,unsigned int length)
- Line: 327

### esdhc_mcf_get_max_timeout_count
- Return type: static unsigned int
- Signature: esdhc_mcf_get_max_timeout_count(struct sdhci_host * host)
- Line: 178

### esdhc_mcf_plat_init
- Return type: static int
- Signature: esdhc_mcf_plat_init(struct sdhci_host * host,struct pltfm_mcf_data * mcf_data)
- Line: 368

### esdhc_mcf_pltfm_get_max_clock
- Return type: static unsigned int
- Signature: esdhc_mcf_pltfm_get_max_clock(struct sdhci_host * host)
- Line: 205

### esdhc_mcf_pltfm_get_min_clock
- Return type: static unsigned int
- Signature: esdhc_mcf_pltfm_get_min_clock(struct sdhci_host * host)
- Line: 212

### esdhc_mcf_pltfm_set_bus_width
- Return type: static void
- Signature: esdhc_mcf_pltfm_set_bus_width(struct sdhci_host * host,int width)
- Line: 281

### esdhc_mcf_pltfm_set_clock
- Return type: static void
- Signature: esdhc_mcf_pltfm_set_clock(struct sdhci_host * host,unsigned int clock)
- Line: 219

### esdhc_mcf_readb_be
- Return type: static u8
- Signature: esdhc_mcf_readb_be(struct sdhci_host * host,int reg)
- Line: 126

### esdhc_mcf_readl_be
- Return type: static u32
- Signature: esdhc_mcf_readl_be(struct sdhci_host * host,int reg)
- Line: 155

### esdhc_mcf_readw_be
- Return type: static u16
- Signature: esdhc_mcf_readw_be(struct sdhci_host * host,int reg)
- Line: 143

### esdhc_mcf_request_done
- Return type: static void
- Signature: esdhc_mcf_request_done(struct sdhci_host * host,struct mmc_request * mrq)
- Line: 299

### esdhc_mcf_reset
- Return type: static void
- Signature: esdhc_mcf_reset(struct sdhci_host * host,u8 mask)
- Line: 191

### esdhc_mcf_set_timeout
- Return type: static void
- Signature: esdhc_mcf_set_timeout(struct sdhci_host * host,struct mmc_command * cmd)
- Line: 183

### esdhc_mcf_writeb_be
- Return type: static void
- Signature: esdhc_mcf_writeb_be(struct sdhci_host * host,u8 val,int reg)
- Line: 65

### esdhc_mcf_writel_be
- Return type: static void
- Signature: esdhc_mcf_writel_be(struct sdhci_host * host,u32 val,int reg)
- Line: 121

### esdhc_mcf_writew_be
- Return type: static void
- Signature: esdhc_mcf_writew_be(struct sdhci_host * host,u16 val,int reg)
- Line: 93

### sdhci_esdhc_mcf_probe
- Return type: static int
- Signature: sdhci_esdhc_mcf_probe(struct platform_device * pdev)
- Line: 408

### sdhci_esdhc_mcf_remove
- Return type: static void
- Signature: sdhci_esdhc_mcf_remove(struct platform_device * pdev)
- Line: 485

## Structs (1)

### pltfm_mcf_data
- Line: 25
- Members:
  - clk_ipg: clk *
  - clk_ahb: clk *
  - clk_per: clk *
  - aside: int
  - current_bus_width: int

## Variables (3)

- static **sdhci_esdhc_mcf_driver** : platform_driver (line 498)
- static **sdhci_esdhc_mcf_pdata** : const struct sdhci_pltfm_data (line 356)
- static **sdhci_esdhc_ops** : const struct sdhci_ops (line 338)

## Macros (4)

- **ESDHC_DEFAULT_HOST_CONTROL** (line 18)
- **ESDHC_INT_VENDOR_SPEC_DMA_ERR** (line 23)
- **ESDHC_PROCTL_D3CD** (line 16)
- **ESDHC_SYS_CTRL_DTOCV_MASK** (line 17)
