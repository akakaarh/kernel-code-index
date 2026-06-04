# drivers/mmc/host/alcor.c

Subsystem: drivers/mmc

## Functions (40)

### alcor_card_busy
- Return type: static int
- Signature: alcor_card_busy(struct mmc_host * mmc)
- Line: 721

### alcor_cd_irq
- Return type: static void
- Signature: alcor_cd_irq(struct alcor_sdmmc_host * host,u32 intmask)
- Line: 548

### alcor_cmd_irq_done
- Return type: static int
- Signature: alcor_cmd_irq_done(struct alcor_sdmmc_host * host,u32 intmask)
- Line: 408

### alcor_cmd_irq_thread
- Return type: static void
- Signature: alcor_cmd_irq_thread(struct alcor_sdmmc_host * host,u32 intmask)
- Line: 452

### alcor_data_irq_done
- Return type: static int
- Signature: alcor_data_irq_done(struct alcor_sdmmc_host * host,u32 intmask)
- Line: 472

### alcor_data_irq_thread
- Return type: static void
- Signature: alcor_data_irq_thread(struct alcor_sdmmc_host * host,u32 intmask)
- Line: 526

### alcor_data_set_dma
- Return type: static void
- Signature: alcor_data_set_dma(struct alcor_sdmmc_host * host)
- Line: 123

### alcor_err_irq
- Return type: static void
- Signature: alcor_err_irq(struct alcor_sdmmc_host * host,u32 intmask)
- Line: 384

### alcor_finish_data
- Return type: static void
- Signature: alcor_finish_data(struct alcor_sdmmc_host * host)
- Line: 340

### alcor_get_cd
- Return type: static int
- Signature: alcor_get_cd(struct mmc_host * mmc)
- Line: 733

### alcor_get_ro
- Return type: static int
- Signature: alcor_get_ro(struct mmc_host * mmc)
- Line: 745

### alcor_hw_init
- Return type: static void
- Signature: alcor_hw_init(struct alcor_sdmmc_host * host)
- Line: 989

### alcor_hw_uninit
- Return type: static void
- Signature: alcor_hw_uninit(struct alcor_sdmmc_host * host)
- Line: 1034

### alcor_init_mmc
- Return type: static void
- Signature: alcor_init_mmc(struct alcor_sdmmc_host * host)
- Line: 1049

### alcor_irq
- Return type: static irqreturn_t
- Signature: alcor_irq(int irq,void * d)
- Line: 619

### alcor_irq_thread
- Return type: static irqreturn_t
- Signature: alcor_irq_thread(int irq,void * d)
- Line: 570

### alcor_mask_sd_irqs
- Return type: static void
- Signature: alcor_mask_sd_irqs(struct alcor_sdmmc_host * host)
- Line: 88

### alcor_pci_sdmmc_drv_probe
- Return type: static int
- Signature: alcor_pci_sdmmc_drv_probe(struct platform_device * pdev)
- Line: 1080

### alcor_pci_sdmmc_drv_remove
- Return type: static void
- Signature: alcor_pci_sdmmc_drv_remove(struct platform_device * pdev)
- Line: 1120

### alcor_pci_sdmmc_resume
- Return type: static int
- Signature: alcor_pci_sdmmc_resume(struct device * dev)
- Line: 1144

### alcor_pci_sdmmc_suspend
- Return type: static int
- Signature: alcor_pci_sdmmc_suspend(struct device * dev)
- Line: 1132

### alcor_post_req
- Return type: static void
- Signature: alcor_post_req(struct mmc_host * mmc,struct mmc_request * mrq,int err)
- Line: 826

### alcor_pre_req
- Return type: static void
- Signature: alcor_pre_req(struct mmc_host * mmc,struct mmc_request * mrq)
- Line: 776

### alcor_prepare_data
- Return type: static void
- Signature: alcor_prepare_data(struct alcor_sdmmc_host * host,struct mmc_command * cmd)
- Line: 239

### alcor_prepare_sg_miter
- Return type: static void
- Signature: alcor_prepare_sg_miter(struct alcor_sdmmc_host * host)
- Line: 227

### alcor_request
- Return type: static void
- Signature: alcor_request(struct mmc_host * mmc,struct mmc_request * mrq)
- Line: 757

### alcor_request_complete
- Return type: static void
- Signature: alcor_request_complete(struct alcor_sdmmc_host * host,bool cancel_timeout)
- Line: 315

### alcor_reset
- Return type: static void
- Signature: alcor_reset(struct alcor_sdmmc_host * host,u8 val)
- Line: 105

### alcor_rmw8
- Return type: static void
- Signature: alcor_rmw8(struct alcor_sdmmc_host * host,unsigned int addr,u8 clear,u8 set)
- Line: 73

### alcor_send_cmd
- Return type: static void
- Signature: alcor_send_cmd(struct alcor_sdmmc_host * host,struct mmc_command * cmd,bool set_timeout)
- Line: 263

### alcor_set_bus_width
- Return type: static void
- Signature: alcor_set_bus_width(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 706

### alcor_set_clock
- Return type: static void
- Signature: alcor_set_clock(struct alcor_sdmmc_host * host,unsigned int clock)
- Line: 653

### alcor_set_ios
- Return type: static void
- Signature: alcor_set_ios(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 907

### alcor_set_power_mode
- Return type: static void
- Signature: alcor_set_power_mode(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 846

### alcor_set_timing
- Return type: static void
- Signature: alcor_set_timing(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 693

### alcor_signal_voltage_switch
- Return type: static int
- Signature: alcor_signal_voltage_switch(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 928

### alcor_timeout_timer
- Return type: static void
- Signature: alcor_timeout_timer(struct work_struct * work)
- Line: 962

### alcor_trf_block_pio
- Return type: static void
- Signature: alcor_trf_block_pio(struct alcor_sdmmc_host * host,bool read)
- Line: 186

### alcor_trigger_data_transfer
- Return type: static void
- Signature: alcor_trigger_data_transfer(struct alcor_sdmmc_host * host)
- Line: 149

### alcor_unmask_sd_irqs
- Return type: static void
- Signature: alcor_unmask_sd_irqs(struct alcor_sdmmc_host * host)
- Line: 95

## Structs (2)

### alcor_pll_conf
- Line: 36
- Members:
  - clk_src_freq: unsigned int
  - clk_src_reg: unsigned int
  - min_div: unsigned int
  - max_div: unsigned int
  - dev: device *
  - alcor_pci: alcor_pci_priv *
  - mrq: mmc_request *
  - cmd: mmc_command *
  - data: mmc_data *
  - dma_on: unsigned int:1
  - cmd_mutex: mutex
  - timeout_work: delayed_work
  - sg_miter: sg_mapping_iter
  - sg: scatterlist *
  - blocks: unsigned int
  - sg_count: int
  - irq_status_sd: u32
  - cur_power_mode: unsigned char

### alcor_sdmmc_host
- Line: 43
- Members:
  - clk_src_freq: unsigned int
  - clk_src_reg: unsigned int
  - min_div: unsigned int
  - max_div: unsigned int
  - dev: device *
  - alcor_pci: alcor_pci_priv *
  - mrq: mmc_request *
  - cmd: mmc_command *
  - data: mmc_data *
  - dma_on: unsigned int:1
  - cmd_mutex: mutex
  - timeout_work: delayed_work
  - sg_miter: sg_mapping_iter
  - sg: scatterlist *
  - blocks: unsigned int
  - sg_count: int
  - irq_status_sd: u32
  - cur_power_mode: unsigned char

## Enums (1)

### alcor_cookie
- Line: 30

## Variables (4)

- static **alcor_pci_sdmmc_driver** : platform_driver (line 1165)
- static **alcor_pci_sdmmc_ids** : const struct platform_device_id[] (line 1156)
- static **alcor_pll_cfg** : const struct alcor_pll_conf[] (line 65)
- static **alcor_sdc_ops** : const struct mmc_host_ops (line 951)
