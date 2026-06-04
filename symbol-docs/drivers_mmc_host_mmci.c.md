# drivers/mmc/host/mmci.c

Subsystem: drivers/mmc

## Functions (69)

### _mmci_dmae_prep_data
- Return type: static int
- Signature: _mmci_dmae_prep_data(struct mmci_host * host,struct mmc_data * data,struct dma_chan ** dma_chan,struct dma_async_tx_descriptor ** dma_desc)
- Line: 1010

### mmci_ack_sdio_irq
- Return type: static void
- Signature: mmci_ack_sdio_irq(struct mmc_host * mmc)
- Line: 2089

### mmci_card_busy
- Return type: static int
- Signature: mmci_card_busy(struct mmc_host * mmc)
- Line: 371

### mmci_cmd_irq
- Return type: static void
- Signature: mmci_cmd_irq(struct mmci_host * host,struct mmc_command * cmd,unsigned int status)
- Line: 1470

### mmci_data_irq
- Return type: static void
- Signature: mmci_data_irq(struct mmci_host * host,struct mmc_data * data,unsigned int status)
- Line: 1388

### mmci_dma_error
- Return type: static void
- Signature: mmci_dma_error(struct mmci_host * host)
- Line: 622

### mmci_dma_finalize
- Return type: static void
- Signature: mmci_dma_finalize(struct mmci_host * host,struct mmc_data * data)
- Line: 613

### mmci_dma_release
- Return type: static void
- Signature: mmci_dma_release(struct mmci_host * host)
- Line: 499

### mmci_dma_setup
- Return type: static void
- Signature: mmci_dma_setup(struct mmci_host * host)
- Line: 507

### mmci_dma_start
- Return type: static int
- Signature: mmci_dma_start(struct mmci_host * host,unsigned int datactrl)
- Line: 576

### mmci_dma_unmap
- Return type: static void
- Signature: mmci_dma_unmap(struct mmci_host * host,struct mmc_data * data)
- Line: 933

### mmci_dmae_error
- Return type: void
- Signature: mmci_dmae_error(struct mmci_host * host)
- Line: 947

### mmci_dmae_finalize
- Return type: void
- Signature: mmci_dmae_finalize(struct mmci_host * host,struct mmc_data * data)
- Line: 964

### mmci_dmae_get_next_data
- Return type: void
- Signature: mmci_dmae_get_next_data(struct mmci_host * host,struct mmc_data * data)
- Line: 1124

### mmci_dmae_prep_data
- Return type: int
- Signature: mmci_dmae_prep_data(struct mmci_host * host,struct mmc_data * data,bool next)
- Line: 1085

### mmci_dmae_release
- Return type: void
- Signature: mmci_dmae_release(struct mmci_host * host)
- Line: 922

### mmci_dmae_setup
- Return type: int
- Signature: mmci_dmae_setup(struct mmci_host * host)
- Line: 844

### mmci_dmae_start
- Return type: int
- Signature: mmci_dmae_start(struct mmci_host * host,unsigned int * datactrl)
- Line: 1106

### mmci_dmae_unprep_data
- Return type: void
- Signature: mmci_dmae_unprep_data(struct mmci_host * host,struct mmc_data * data,int err)
- Line: 1140

### mmci_enable_sdio_irq
- Return type: static void
- Signature: mmci_enable_sdio_irq(struct mmc_host * mmc,int enable)
- Line: 2071

### mmci_get_cd
- Return type: static int
- Signature: mmci_get_cd(struct mmc_host * mmc)
- Line: 2038

### mmci_get_dctrl_cfg
- Return type: static u32
- Signature: mmci_get_dctrl_cfg(struct mmci_host * host)
- Line: 683

### mmci_get_next_data
- Return type: static void
- Signature: mmci_get_next_data(struct mmci_host * host,struct mmc_data * data)
- Line: 568

### mmci_get_rx_fifocnt
- Return type: static int
- Signature: mmci_get_rx_fifocnt(struct mmci_host * host,u32 status,int remain)
- Line: 1592

### mmci_init_sg
- Return type: static void
- Signature: mmci_init_sg(struct mmci_host * host,struct mmc_data * data)
- Line: 671

### mmci_irq
- Return type: static irqreturn_t
- Signature: mmci_irq(int irq,void * dev_id)
- Line: 1791

### mmci_irq_thread
- Return type: static irqreturn_t
- Signature: mmci_irq_thread(int irq,void * dev_id)
- Line: 1855

### mmci_of_parse
- Return type: static int
- Signature: mmci_of_parse(struct device_node * np,struct mmc_host * mmc)
- Line: 2168

### mmci_pio_irq
- Return type: static irqreturn_t
- Signature: mmci_pio_irq(int irq,void * dev_id)
- Line: 1697

### mmci_pio_read
- Return type: static int
- Signature: mmci_pio_read(struct mmci_host * host,char * buffer,unsigned int remain)
- Line: 1611

### mmci_pio_write
- Return type: static int
- Signature: mmci_pio_write(struct mmci_host * host,char * buffer,unsigned int remain,u32 status)
- Line: 1659

### mmci_post_request
- Return type: static void
- Signature: mmci_post_request(struct mmc_host * mmc,struct mmc_request * mrq,int err)
- Line: 1224

### mmci_pre_request
- Return type: static void
- Signature: mmci_pre_request(struct mmc_host * mmc,struct mmc_request * mrq)
- Line: 1208

### mmci_prep_data
- Return type: static int
- Signature: mmci_prep_data(struct mmci_host * host,struct mmc_data * data,bool next)
- Line: 543

### mmci_probe
- Return type: static int
- Signature: mmci_probe(struct amba_device * dev,const struct amba_id * id)
- Line: 2203

### mmci_probe_level_translator
- Return type: static void
- Signature: mmci_probe_level_translator(struct mmc_host * mmc)
- Line: 2109

### mmci_qcom_get_rx_fifocnt
- Return type: static int
- Signature: mmci_qcom_get_rx_fifocnt(struct mmci_host * host,u32 status,int r)
- Line: 1597

### mmci_reg_delay
- Return type: static void
- Signature: mmci_reg_delay(struct mmci_host * host)
- Line: 385

### mmci_remove
- Return type: static void
- Signature: mmci_remove(struct amba_device * dev)
- Line: 2490

### mmci_request
- Return type: static void
- Signature: mmci_request(struct mmc_host * mmc,struct mmc_request * mrq)
- Line: 1879

### mmci_request_end
- Return type: static void
- Signature: mmci_request_end(struct mmci_host * host,struct mmc_request * mrq)
- Line: 632

### mmci_restore
- Return type: static void
- Signature: mmci_restore(struct mmci_host * host)
- Line: 2536

### mmci_runtime_resume
- Return type: static int
- Signature: mmci_runtime_resume(struct device * dev)
- Line: 2569

### mmci_runtime_suspend
- Return type: static int
- Signature: mmci_runtime_suspend(struct device * dev)
- Line: 2554

### mmci_save
- Return type: static void
- Signature: mmci_save(struct mmci_host * host)
- Line: 2519

### mmci_set_clkreg
- Return type: static void
- Signature: mmci_set_clkreg(struct mmci_host * host,unsigned int desired)
- Line: 440

### mmci_set_ios
- Return type: static void
- Signature: mmci_set_ios(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 1926

### mmci_set_mask1
- Return type: static void
- Signature: mmci_set_mask1(struct mmci_host * host,unsigned int mask)
- Line: 644

### mmci_set_max_busy_timeout
- Return type: static void
- Signature: mmci_set_max_busy_timeout(struct mmc_host * mmc)
- Line: 1911

### mmci_sig_volt_switch
- Return type: static int
- Signature: mmci_sig_volt_switch(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 2053

### mmci_signal_sdio_irq
- Return type: static void
- Signature: mmci_signal_sdio_irq(struct mmci_host * host,u32 status)
- Line: 1780

### mmci_start_command
- Return type: static void
- Signature: mmci_start_command(struct mmci_host * host,struct mmc_command * cmd,u32 c)
- Line: 1321

### mmci_start_data
- Return type: static void
- Signature: mmci_start_data(struct mmci_host * host,struct mmc_data * data)
- Line: 1236

### mmci_stop_command
- Return type: static void
- Signature: mmci_stop_command(struct mmci_host * host)
- Line: 1381

### mmci_stop_data
- Return type: static void
- Signature: mmci_stop_data(struct mmci_host * host)
- Line: 664

### mmci_unprep_data
- Return type: static void
- Signature: mmci_unprep_data(struct mmci_host * host,struct mmc_data * data,int err)
- Line: 559

### mmci_validate_data
- Return type: static int
- Signature: mmci_validate_data(struct mmci_host * host,struct mmc_data * data)
- Line: 524

### mmci_variant_init
- Return type: static void
- Signature: mmci_variant_init(struct mmci_host * host)
- Line: 1190

### mmci_write_clkreg
- Return type: void
- Signature: mmci_write_clkreg(struct mmci_host * host,u32 clk)
- Line: 403

### mmci_write_datactrlreg
- Return type: static void
- Signature: mmci_write_datactrlreg(struct mmci_host * host,u32 datactrl)
- Line: 425

### mmci_write_pwrreg
- Return type: void
- Signature: mmci_write_pwrreg(struct mmci_host * host,u32 pwr)
- Line: 414

### mmci_write_sdio_irq_bit
- Return type: static void
- Signature: mmci_write_sdio_irq_bit(struct mmci_host * host,int enable)
- Line: 1769

### ux500_busy_clear_mask_done
- Return type: static void
- Signature: ux500_busy_clear_mask_done(struct mmci_host * host)
- Line: 693

### ux500_busy_complete
- Return type: static bool
- Signature: ux500_busy_complete(struct mmci_host * host,struct mmc_command * cmd,u32 status,u32 err_msk)
- Line: 721

### ux500_busy_timeout_work
- Return type: static void
- Signature: ux500_busy_timeout_work(struct work_struct * work)
- Line: 1563

### ux500_state_str
- Return type: static char *
- Signature: ux500_state_str(struct mmci_host * host)
- Line: 1544

### ux500_variant_init
- Return type: static void
- Signature: ux500_variant_init(struct mmci_host * host)
- Line: 1195

### ux500v2_get_dctrl_cfg
- Return type: static u32
- Signature: ux500v2_get_dctrl_cfg(struct mmci_host * host)
- Line: 688

### ux500v2_variant_init
- Return type: static void
- Signature: ux500v2_variant_init(struct mmci_host * host)
- Line: 1201

## Structs (2)

### mmci_dmae_next
- Line: 831
- Members:
  - desc: dma_async_tx_descriptor *
  - chan: dma_chan *
  - cur: dma_chan *
  - rx_channel: dma_chan *
  - tx_channel: dma_chan *
  - desc_current: dma_async_tx_descriptor *
  - next_data: mmci_dmae_next

### mmci_dmae_priv
- Line: 836
- Members:
  - desc: dma_async_tx_descriptor *
  - chan: dma_chan *
  - cur: dma_chan *
  - rx_channel: dma_chan *
  - tx_channel: dma_chan *
  - desc_current: dma_async_tx_descriptor *
  - next_data: mmci_dmae_next

## Variables (19)

- static **fmax** : unsigned int (line 53)
- static **mmci_dev_pm_ops** : const struct dev_pm_ops (line 2584)
- static **mmci_driver** : amba_driver (line 2672)
- static **mmci_ids** : const struct amba_id[] (line 2589)
- static **mmci_ops** : mmc_host_ops (line 2099)
- static **mmci_variant_ops** : mmci_host_ops (line 1173)
- static **mmci_variant_ops** : mmci_host_ops (line 1185)
- static **variant_arm** : variant_data (line 55)
- static **variant_arm_extended_fifo** : variant_data (line 74)
- static **variant_arm_extended_fifo_hwfc** : variant_data (line 92)
- static **variant_nomadik** : variant_data (line 136)
- static **variant_qcom** : variant_data (line 342)
- static **variant_stm32** : variant_data (line 231)
- static **variant_stm32_sdmmc** : variant_data (line 256)
- static **variant_stm32_sdmmcv2** : variant_data (line 284)
- static **variant_stm32_sdmmcv3** : variant_data (line 313)
- static **variant_u300** : variant_data (line 111)
- static **variant_ux500** : variant_data (line 162)
- static **variant_ux500v2** : variant_data (line 196)

## Macros (1)

- **DRIVER_NAME** (line 47)
