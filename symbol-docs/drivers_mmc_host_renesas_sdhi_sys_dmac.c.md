# drivers/mmc/host/renesas_sdhi_sys_dmac.c

Subsystem: drivers/mmc

## Functions (11)

### renesas_sdhi_sys_dmac_abort_dma
- Return type: static void
- Signature: renesas_sdhi_sys_dmac_abort_dma(struct tmio_mmc_host * host)
- Line: 109

### renesas_sdhi_sys_dmac_dataend_dma
- Return type: static void
- Signature: renesas_sdhi_sys_dmac_dataend_dma(struct tmio_mmc_host * host)
- Line: 121

### renesas_sdhi_sys_dmac_dma_callback
- Return type: static void
- Signature: renesas_sdhi_sys_dmac_dma_callback(void * arg)
- Line: 128

### renesas_sdhi_sys_dmac_enable_dma
- Return type: static void
- Signature: renesas_sdhi_sys_dmac_enable_dma(struct tmio_mmc_host * host,bool enable)
- Line: 97

### renesas_sdhi_sys_dmac_issue_work_fn
- Return type: static void
- Signature: renesas_sdhi_sys_dmac_issue_work_fn(struct work_struct * work)
- Line: 317

### renesas_sdhi_sys_dmac_probe
- Return type: static int
- Signature: renesas_sdhi_sys_dmac_probe(struct platform_device * pdev)
- Line: 453

### renesas_sdhi_sys_dmac_release_dma
- Return type: static void
- Signature: renesas_sdhi_sys_dmac_release_dma(struct tmio_mmc_host * host)
- Line: 424

### renesas_sdhi_sys_dmac_request_dma
- Return type: static void
- Signature: renesas_sdhi_sys_dmac_request_dma(struct tmio_mmc_host * host,struct tmio_mmc_data * pdata)
- Line: 339

### renesas_sdhi_sys_dmac_start_dma
- Return type: static void
- Signature: renesas_sdhi_sys_dmac_start_dma(struct tmio_mmc_host * host,struct mmc_data * data)
- Line: 305

### renesas_sdhi_sys_dmac_start_dma_rx
- Return type: static void
- Signature: renesas_sdhi_sys_dmac_start_dma_rx(struct tmio_mmc_host * host)
- Line: 157

### renesas_sdhi_sys_dmac_start_dma_tx
- Return type: static void
- Signature: renesas_sdhi_sys_dmac_start_dma_tx(struct tmio_mmc_host * host)
- Line: 229

## Variables (8)

- static **of_default_cfg** : const struct renesas_sdhi_of_data (line 30)
- static **of_rcar_gen1_compatible** : const struct renesas_sdhi_of_data (line 42)
- static **of_rcar_gen2_compatible** : const struct renesas_sdhi_of_data (line 61)
- static **of_rz_compatible** : const struct renesas_sdhi_of_data (line 34)
- static **rcar_gen2_scc_taps** : renesas_sdhi_scc[] (line 50)
- static **renesas_sdhi_sys_dmac_dma_ops** : const struct tmio_mmc_dma_ops (line 444)
- static **renesas_sdhi_sys_dmac_of_match** : const struct of_device_id[] (line 76)
- static **renesas_sys_dmac_sdhi_driver** : platform_driver (line 463)

## Macros (1)

- **TMIO_MMC_MIN_DMA_LEN** (line 28)
