# drivers/mmc/host/meson-mx-sdhc-mmc.c

Subsystem: drivers/mmc

## Functions (25)

### meson_mx_sdhc_card_busy
- Return type: static int
- Signature: meson_mx_sdhc_card_busy(struct mmc_host * mmc)
- Line: 400

### meson_mx_sdhc_clear_fifo
- Return type: static void
- Signature: meson_mx_sdhc_clear_fifo(struct mmc_host * mmc)
- Line: 80

### meson_mx_sdhc_disable_clks
- Return type: static void
- Signature: meson_mx_sdhc_disable_clks(struct mmc_host * mmc)
- Line: 237

### meson_mx_sdhc_enable_clks
- Return type: static int
- Signature: meson_mx_sdhc_enable_clks(struct mmc_host * mmc)
- Line: 249

### meson_mx_sdhc_execute_tuning
- Return type: static int
- Signature: meson_mx_sdhc_execute_tuning(struct mmc_host * mmc,u32 opcode)
- Line: 424

### meson_mx_sdhc_init_hw
- Return type: static void
- Signature: meson_mx_sdhc_init_hw(struct mmc_host * mmc)
- Line: 724

### meson_mx_sdhc_init_hw_meson8
- Return type: static void
- Signature: meson_mx_sdhc_init_hw_meson8(struct mmc_host * mmc)
- Line: 633

### meson_mx_sdhc_init_hw_meson8m2
- Return type: static void
- Signature: meson_mx_sdhc_init_hw_meson8m2(struct mmc_host * mmc)
- Line: 700

### meson_mx_sdhc_irq
- Return type: static irqreturn_t
- Signature: meson_mx_sdhc_irq(int irq,void * data)
- Line: 537

### meson_mx_sdhc_irq_thread
- Return type: static irqreturn_t
- Signature: meson_mx_sdhc_irq_thread(int irq,void * irq_data)
- Line: 571

### meson_mx_sdhc_map_dma
- Return type: static int
- Signature: meson_mx_sdhc_map_dma(struct mmc_host * mmc,struct mmc_request * mrq)
- Line: 363

### meson_mx_sdhc_probe
- Return type: static int
- Signature: meson_mx_sdhc_probe(struct platform_device * pdev)
- Line: 760

### meson_mx_sdhc_read_response
- Return type: static u32
- Signature: meson_mx_sdhc_read_response(struct meson_mx_sdhc_host * host,u8 idx)
- Line: 521

### meson_mx_sdhc_remove
- Return type: static void
- Signature: meson_mx_sdhc_remove(struct platform_device * pdev)
- Line: 853

### meson_mx_sdhc_request
- Return type: static void
- Signature: meson_mx_sdhc_request(struct mmc_host * mmc,struct mmc_request * mrq)
- Line: 381

### meson_mx_sdhc_request_done
- Return type: static void
- Signature: meson_mx_sdhc_request_done(struct meson_mx_sdhc_host * host)
- Line: 504

### meson_mx_sdhc_reset
- Return type: static void
- Signature: meson_mx_sdhc_reset(struct meson_mx_sdhc_host * host)
- Line: 68

### meson_mx_sdhc_set_clk
- Return type: static int
- Signature: meson_mx_sdhc_set_clk(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 267

### meson_mx_sdhc_set_ios
- Return type: static void
- Signature: meson_mx_sdhc_set_ios(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 307

### meson_mx_sdhc_set_pdma_meson8
- Return type: static void
- Signature: meson_mx_sdhc_set_pdma_meson8(struct mmc_host * mmc)
- Line: 649

### meson_mx_sdhc_set_pdma_meson8m2
- Return type: static void
- Signature: meson_mx_sdhc_set_pdma_meson8m2(struct mmc_host * mmc)
- Line: 716

### meson_mx_sdhc_start_cmd
- Return type: static void
- Signature: meson_mx_sdhc_start_cmd(struct mmc_host * mmc,struct mmc_command * cmd)
- Line: 132

### meson_mx_sdhc_tuning_point_matches
- Return type: static bool
- Signature: meson_mx_sdhc_tuning_point_matches(struct mmc_host * mmc,u32 opcode)
- Line: 409

### meson_mx_sdhc_wait_before_send_meson8
- Return type: static void
- Signature: meson_mx_sdhc_wait_before_send_meson8(struct mmc_host * mmc)
- Line: 675

### meson_mx_sdhc_wait_cmd_ready
- Return type: static void
- Signature: meson_mx_sdhc_wait_cmd_ready(struct mmc_host * mmc)
- Line: 103

## Structs (2)

### meson_mx_sdhc_data
- Line: 37
- Members:
  - init_hw: void (*)(struct mmc_host * mmc)
  - set_pdma: void (*)(struct mmc_host * mmc)
  - wait_before_send: void (*)(struct mmc_host * mmc)
  - hardware_flush_all_cmds: bool
  - mmc: mmc_host *
  - mrq: mmc_request *
  - cmd: mmc_command *
  - error: int
  - regmap: regmap *
  - pclk: clk *
  - sd_clk: clk *
  - bulk_clks: clk_bulk_data[]
  - bulk_clks_enabled: bool
  - platform: const struct meson_mx_sdhc_data *

### meson_mx_sdhc_host
- Line: 44
- Members:
  - init_hw: void (*)(struct mmc_host * mmc)
  - set_pdma: void (*)(struct mmc_host * mmc)
  - wait_before_send: void (*)(struct mmc_host * mmc)
  - hardware_flush_all_cmds: bool
  - mmc: mmc_host *
  - mrq: mmc_request *
  - cmd: mmc_command *
  - error: int
  - regmap: regmap *
  - pclk: clk *
  - sd_clk: clk *
  - bulk_clks: clk_bulk_data[]
  - bulk_clks_enabled: bool
  - platform: const struct meson_mx_sdhc_data *

## Variables (6)

- static **meson_mx_sdhc_data_meson8** : const struct meson_mx_sdhc_data (line 864)
- static **meson_mx_sdhc_data_meson8m2** : const struct meson_mx_sdhc_data (line 871)
- static **meson_mx_sdhc_driver** : platform_driver (line 894)
- static **meson_mx_sdhc_of_match** : const struct of_device_id[] (line 877)
- static **meson_mx_sdhc_ops** : const struct mmc_host_ops (line 495)
- static **meson_mx_sdhc_regmap_config** : const struct regmap_config (line 61)

## Macros (7)

- **MESON_SDHC_MAX_BLK_SIZE** (line 29)
- **MESON_SDHC_NUM_BULK_CLKS** (line 28)
- **MESON_SDHC_NUM_TUNING_TRIES** (line 30)
- **MESON_SDHC_WAIT_BEFORE_SEND_SLEEP_US** (line 34)
- **MESON_SDHC_WAIT_BEFORE_SEND_TIMEOUT_US** (line 35)
- **MESON_SDHC_WAIT_CMD_READY_SLEEP_US** (line 32)
- **MESON_SDHC_WAIT_CMD_READY_TIMEOUT_US** (line 33)
