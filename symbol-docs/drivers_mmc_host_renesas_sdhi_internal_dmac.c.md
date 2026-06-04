# drivers/mmc/host/renesas_sdhi_internal_dmac.c

Subsystem: drivers/mmc

## Functions (16)

### renesas_sdhi_internal_dmac_abort_dma
- Return type: static void
- Signature: renesas_sdhi_internal_dmac_abort_dma(struct tmio_mmc_host * host)
- Line: 315

### renesas_sdhi_internal_dmac_complete
- Return type: static bool
- Signature: renesas_sdhi_internal_dmac_complete(struct tmio_mmc_host * host)
- Line: 464

### renesas_sdhi_internal_dmac_complete_work_fn
- Return type: static void
- Signature: renesas_sdhi_internal_dmac_complete_work_fn(struct work_struct * work)
- Line: 490

### renesas_sdhi_internal_dmac_dataend_dma
- Return type: static void
- Signature: renesas_sdhi_internal_dmac_dataend_dma(struct tmio_mmc_host * host)
- Line: 350

### renesas_sdhi_internal_dmac_dma_irq
- Return type: static bool
- Signature: renesas_sdhi_internal_dmac_dma_irq(struct tmio_mmc_host * host)
- Line: 329

### renesas_sdhi_internal_dmac_enable_dma
- Return type: static void
- Signature: renesas_sdhi_internal_dmac_enable_dma(struct tmio_mmc_host * host,bool enable)
- Line: 298

### renesas_sdhi_internal_dmac_end_dma
- Return type: static void
- Signature: renesas_sdhi_internal_dmac_end_dma(struct tmio_mmc_host * host)
- Line: 505

### renesas_sdhi_internal_dmac_issue_work_fn
- Return type: static void
- Signature: renesas_sdhi_internal_dmac_issue_work_fn(struct work_struct * work)
- Line: 446

### renesas_sdhi_internal_dmac_map
- Return type: static bool
- Signature: renesas_sdhi_internal_dmac_map(struct tmio_mmc_host * host,struct mmc_data * data,enum renesas_sdhi_dma_cookie cookie)
- Line: 383

### renesas_sdhi_internal_dmac_post_req
- Return type: static void
- Signature: renesas_sdhi_internal_dmac_post_req(struct mmc_host * mmc,struct mmc_request * mrq,int err)
- Line: 511

### renesas_sdhi_internal_dmac_pre_req
- Return type: static void
- Signature: renesas_sdhi_internal_dmac_pre_req(struct mmc_host * mmc,struct mmc_request * mrq)
- Line: 524

### renesas_sdhi_internal_dmac_probe
- Return type: static int
- Signature: renesas_sdhi_internal_dmac_probe(struct platform_device * pdev)
- Line: 580

### renesas_sdhi_internal_dmac_release_dma
- Return type: static void
- Signature: renesas_sdhi_internal_dmac_release_dma(struct tmio_mmc_host * host)
- Line: 563

### renesas_sdhi_internal_dmac_request_dma
- Return type: static void
- Signature: renesas_sdhi_internal_dmac_request_dma(struct tmio_mmc_host * host,struct tmio_mmc_data * pdata)
- Line: 538

### renesas_sdhi_internal_dmac_start_dma
- Return type: static void
- Signature: renesas_sdhi_internal_dmac_start_dma(struct tmio_mmc_host * host,struct mmc_data * data)
- Line: 406

### renesas_sdhi_internal_dmac_unmap
- Return type: static void
- Signature: renesas_sdhi_internal_dmac_unmap(struct tmio_mmc_host * host,struct mmc_data * data,enum renesas_sdhi_dma_cookie cookie)
- Line: 368

## Enums (1)

### renesas_sdhi_dma_cookie
- Line: 61

## Variables (33)

- static **global_flags** : unsigned long (line 74)
- static **of_data_rcar_gen3** : const struct renesas_sdhi_of_data (line 107)
- static **of_data_rcar_gen3_no_sdh_fallback** : const struct renesas_sdhi_of_data (line 124)
- static **of_data_rza2** : const struct renesas_sdhi_of_data (line 92)
- static **of_r8a7795_compatible** : const struct renesas_sdhi_of_data_with_quirks (line 235)
- static **of_r8a77961_compatible** : const struct renesas_sdhi_of_data_with_quirks (line 240)
- static **of_r8a77965_compatible** : const struct renesas_sdhi_of_data_with_quirks (line 245)
- static **of_r8a77970_compatible** : const struct renesas_sdhi_of_data_with_quirks (line 250)
- static **of_r8a77990_compatible** : const struct renesas_sdhi_of_data_with_quirks (line 255)
- static **of_rcar_gen3_compatible** : const struct renesas_sdhi_of_data_with_quirks (line 265)
- static **of_rcar_gen3_nohs400_compatible** : const struct renesas_sdhi_of_data_with_quirks (line 269)
- static **of_rza2_compatible** : const struct renesas_sdhi_of_data_with_quirks (line 274)
- static **of_rzg2l_compatible** : const struct renesas_sdhi_of_data_with_quirks (line 260)
- static **r8a77965_calib_table** : const u8[2][] (line 147)
- static **r8a7796_es13_calib_table** : const u8[2][] (line 140)
- static **r8a77990_calib_table** : const u8[2][] (line 154)
- static **rcar_gen3_scc_taps** : renesas_sdhi_scc[] (line 84)
- static **renesas_internal_dmac_sdhi_driver** : platform_driver (line 608)
- static **renesas_sdhi_internal_dmac_dev_pm_ops** : const struct dev_pm_ops (line 601)
- static **renesas_sdhi_internal_dmac_dma_ops** : const struct tmio_mmc_dma_ops (line 569)
- static **renesas_sdhi_internal_dmac_of_match** : const struct of_device_id[] (line 279)
- static **sdhi_quirks_4tap** : const struct renesas_sdhi_quirks (line 173)
- static **sdhi_quirks_4tap_nohs400** : const struct renesas_sdhi_quirks (line 161)
- static **sdhi_quirks_4tap_nohs400_one_rx** : const struct renesas_sdhi_quirks (line 166)
- static **sdhi_quirks_bad_taps1357** : const struct renesas_sdhi_quirks (line 187)
- static **sdhi_quirks_bad_taps2367** : const struct renesas_sdhi_quirks (line 192)
- static **sdhi_quirks_fixed_addr** : const struct renesas_sdhi_quirks (line 183)
- static **sdhi_quirks_match** : const struct soc_device_attribute[] (line 225)
- static **sdhi_quirks_nohs400** : const struct renesas_sdhi_quirks (line 179)
- static **sdhi_quirks_r8a77965** : const struct renesas_sdhi_quirks (line 204)
- static **sdhi_quirks_r8a7796_es13** : const struct renesas_sdhi_quirks (line 197)
- static **sdhi_quirks_r8a77990** : const struct renesas_sdhi_quirks (line 210)
- static **sdhi_quirks_rzg2l** : const struct renesas_sdhi_quirks (line 215)

## Macros (24)

- **DM_CM_DTRAN_CTRL** (line 28)
- **DM_CM_DTRAN_MODE** (line 27)
- **DM_CM_INFO1** (line 30)
- **DM_CM_INFO1_MASK** (line 31)
- **DM_CM_INFO2** (line 32)
- **DM_CM_INFO2_MASK** (line 33)
- **DM_CM_RST** (line 29)
- **DM_DTRAN_ADDR** (line 34)
- **DTRAN_CTRL_DM_START** (line 43)
- **DTRAN_MODE_ADDR_MODE** (line 40)
- **DTRAN_MODE_BUS_WIDTH** (line 39)
- **DTRAN_MODE_CH_NUM_CH0** (line 37)
- **DTRAN_MODE_CH_NUM_CH1** (line 38)
- **INFO1_DTRANEND0** (line 54)
- **INFO1_DTRANEND1** (line 52)
- **INFO1_DTRANEND1_OLD** (line 53)
- **INFO1_MASK_CLEAR** (line 51)
- **INFO2_DTRANERR0** (line 59)
- **INFO2_DTRANERR1** (line 58)
- **INFO2_MASK_CLEAR** (line 57)
- **RST_DTRANRST0** (line 47)
- **RST_DTRANRST1** (line 46)
- **RST_RESERVED_BITS** (line 48)
- **SDHI_INTERNAL_DMAC_RX_IN_USE** (line 81)
