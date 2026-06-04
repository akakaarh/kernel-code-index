# drivers/mmc/host/uniphier-sd.c

Subsystem: drivers/mmc

## Functions (28)

### uniphier_sd_clk_disable
- Return type: static void
- Signature: uniphier_sd_clk_disable(struct tmio_mmc_host * host)
- Line: 410

### uniphier_sd_clk_enable
- Return type: static int
- Signature: uniphier_sd_clk_enable(struct tmio_mmc_host * host)
- Line: 363

### uniphier_sd_dma_endisable
- Return type: static void
- Signature: uniphier_sd_dma_endisable(struct tmio_mmc_host * host,int enable)
- Line: 87

### uniphier_sd_external_dma_abort
- Return type: static void
- Signature: uniphier_sd_external_dma_abort(struct tmio_mmc_host * host)
- Line: 213

### uniphier_sd_external_dma_callback
- Return type: static void
- Signature: uniphier_sd_external_dma_callback(void * param,const struct dmaengine_result * result)
- Line: 102

### uniphier_sd_external_dma_dataend
- Return type: static void
- Signature: uniphier_sd_external_dma_dataend(struct tmio_mmc_host * host)
- Line: 223

### uniphier_sd_external_dma_enable
- Return type: static void
- Signature: uniphier_sd_external_dma_enable(struct tmio_mmc_host * host,bool enable)
- Line: 179

### uniphier_sd_external_dma_issue
- Return type: static void
- Signature: uniphier_sd_external_dma_issue(struct work_struct * t)
- Line: 93

### uniphier_sd_external_dma_release
- Return type: static void
- Signature: uniphier_sd_external_dma_release(struct tmio_mmc_host * host)
- Line: 205

### uniphier_sd_external_dma_request
- Return type: static void
- Signature: uniphier_sd_external_dma_request(struct tmio_mmc_host * host,struct tmio_mmc_data * pdata)
- Line: 184

### uniphier_sd_external_dma_start
- Return type: static void
- Signature: uniphier_sd_external_dma_start(struct tmio_mmc_host * host,struct mmc_data * data)
- Line: 131

### uniphier_sd_host_init
- Return type: static void
- Signature: uniphier_sd_host_init(struct tmio_mmc_host * host)
- Line: 513

### uniphier_sd_hw_reset
- Return type: static void
- Signature: uniphier_sd_hw_reset(struct mmc_host * mmc)
- Line: 419

### uniphier_sd_internal_dma_abort
- Return type: static void
- Signature: uniphier_sd_internal_dma_abort(struct tmio_mmc_host * host)
- Line: 330

### uniphier_sd_internal_dma_dataend
- Return type: static void
- Signature: uniphier_sd_internal_dma_dataend(struct tmio_mmc_host * host)
- Line: 344

### uniphier_sd_internal_dma_enable
- Return type: static void
- Signature: uniphier_sd_internal_dma_enable(struct tmio_mmc_host * host,bool enable)
- Line: 301

### uniphier_sd_internal_dma_issue
- Return type: static void
- Signature: uniphier_sd_internal_dma_issue(struct work_struct * t)
- Line: 239

### uniphier_sd_internal_dma_release
- Return type: static void
- Signature: uniphier_sd_internal_dma_release(struct tmio_mmc_host * host)
- Line: 323

### uniphier_sd_internal_dma_request
- Return type: static void
- Signature: uniphier_sd_internal_dma_request(struct tmio_mmc_host * host,struct tmio_mmc_data * pdata)
- Line: 306

### uniphier_sd_internal_dma_start
- Return type: static void
- Signature: uniphier_sd_internal_dma_start(struct tmio_mmc_host * host,struct mmc_data * data)
- Line: 252

### uniphier_sd_priv
- Return type: static void *
- Signature: uniphier_sd_priv(struct tmio_mmc_host * host)
- Line: 82

### uniphier_sd_probe
- Return type: static int
- Signature: uniphier_sd_probe(struct platform_device * pdev)
- Line: 615

### uniphier_sd_remove
- Return type: static void
- Signature: uniphier_sd_remove(struct platform_device * pdev)
- Line: 726

### uniphier_sd_set_clock
- Return type: static void
- Signature: uniphier_sd_set_clock(struct tmio_mmc_host * host,unsigned int clock)
- Line: 468

### uniphier_sd_speed_switch
- Return type: static void
- Signature: uniphier_sd_speed_switch(struct tmio_mmc_host * host)
- Line: 432

### uniphier_sd_start_signal_voltage_switch
- Return type: static int
- Signature: uniphier_sd_start_signal_voltage_switch(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 543

### uniphier_sd_uhs_enable
- Return type: static void
- Signature: uniphier_sd_uhs_enable(struct tmio_mmc_host * host,bool uhs_en)
- Line: 451

### uniphier_sd_uhs_init
- Return type: static int
- Signature: uniphier_sd_uhs_init(struct tmio_mmc_host * host)
- Line: 581

## Structs (1)

### uniphier_sd_priv
- Line: 66
- Members:
  - tmio_data: tmio_mmc_data
  - pinctrl: pinctrl *
  - pinstate_uhs: pinctrl_state *
  - clk: clk *
  - rst: reset_control *
  - rst_br: reset_control *
  - rst_hw: reset_control *
  - chan: dma_chan *
  - dma_dir: dma_data_direction
  - sdctrl_regmap: regmap *
  - sdctrl_ch: u32
  - clk_rate: unsigned long
  - caps: unsigned long

## Variables (4)

- static **uniphier_sd_driver** : platform_driver (line 751)
- static **uniphier_sd_external_dma_ops** : const struct tmio_mmc_dma_ops (line 230)
- static **uniphier_sd_internal_dma_ops** : const struct tmio_mmc_dma_ops (line 354)
- static **uniphier_sd_match** : const struct of_device_id[] (line 734)

## Macros (34)

- **UNIPHIER_SDCTRL_CHOFFSET** (line 53)
- **UNIPHIER_SDCTRL_MODE** (line 54)
- **UNIPHIER_SDCTRL_MODE_SDRSEL** (line 56)
- **UNIPHIER_SDCTRL_MODE_UHS1MOD** (line 55)
- **UNIPHIER_SD_CAP_BROKEN_DMA_RX** (line 64)
- **UNIPHIER_SD_CAP_EXTENDED_IP** (line 62)
- **UNIPHIER_SD_CC_EXT_MODE** (line 26)
- **UNIPHIER_SD_CC_EXT_MODE_DMA** (line 27)
- **UNIPHIER_SD_CLKCTL_OFFEN** (line 25)
- **UNIPHIER_SD_CLK_CTL_DIV1** (line 24)
- **UNIPHIER_SD_CLK_CTL_DIV1024** (line 23)
- **UNIPHIER_SD_DMA_ADDR_H** (line 50)
- **UNIPHIER_SD_DMA_ADDR_L** (line 49)
- **UNIPHIER_SD_DMA_CTL** (line 44)
- **UNIPHIER_SD_DMA_CTL_START** (line 45)
- **UNIPHIER_SD_DMA_MODE** (line 34)
- **UNIPHIER_SD_DMA_MODE_ADDR_INC** (line 43)
- **UNIPHIER_SD_DMA_MODE_DIR_FROM_DEV** (line 37)
- **UNIPHIER_SD_DMA_MODE_DIR_MASK** (line 35)
- **UNIPHIER_SD_DMA_MODE_DIR_TO_DEV** (line 36)
- **UNIPHIER_SD_DMA_MODE_WIDTH_16** (line 40)
- **UNIPHIER_SD_DMA_MODE_WIDTH_32** (line 41)
- **UNIPHIER_SD_DMA_MODE_WIDTH_64** (line 42)
- **UNIPHIER_SD_DMA_MODE_WIDTH_8** (line 39)
- **UNIPHIER_SD_DMA_MODE_WIDTH_MASK** (line 38)
- **UNIPHIER_SD_DMA_RST** (line 46)
- **UNIPHIER_SD_DMA_RST_CH0** (line 48)
- **UNIPHIER_SD_DMA_RST_CH1** (line 47)
- **UNIPHIER_SD_HOST_MODE** (line 28)
- **UNIPHIER_SD_VOLT** (line 29)
- **UNIPHIER_SD_VOLT_180** (line 33)
- **UNIPHIER_SD_VOLT_330** (line 32)
- **UNIPHIER_SD_VOLT_MASK** (line 30)
- **UNIPHIER_SD_VOLT_OFF** (line 31)
