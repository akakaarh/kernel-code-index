# drivers/mmc/host/mtk-sd.c

Subsystem: drivers/mmc

## Functions (77)

### __msdc_enable_sdio_irq
- Return type: static void
- Signature: __msdc_enable_sdio_irq(struct msdc_host * host,int enb)
- Line: 1725

### get_best_delay
- Return type: static msdc_delay_phase
- Signature: get_best_delay(struct msdc_host * host,u64 delay)
- Line: 2204

### get_delay_len
- Return type: static int
- Signature: get_delay_len(u64 delay,u32 start_bit)
- Line: 2193

### hs400_tune_response
- Return type: static int
- Signature: hs400_tune_response(struct mmc_host * mmc,u32 opcode)
- Line: 2410

### msdc_ack_sdio_irq
- Return type: static void
- Signature: msdc_ack_sdio_irq(struct mmc_host * mmc)
- Line: 2707

### msdc_auto_cmd_done
- Return type: static int
- Signature: msdc_auto_cmd_done(struct msdc_host * host,int events,struct mmc_command * cmd)
- Line: 1248

### msdc_card_busy
- Return type: static int
- Signature: msdc_card_busy(struct mmc_host * mmc)
- Line: 1691

### msdc_cmd_done
- Return type: static bool
- Signature: msdc_cmd_done(struct msdc_host * host,int events,struct mmc_request * mrq,struct mmc_command * cmd)
- Line: 1356

### msdc_cmd_find_resp
- Return type: static u32
- Signature: msdc_cmd_find_resp(struct msdc_host * host,struct mmc_command * cmd)
- Line: 1146

### msdc_cmd_is_ready
- Return type: static bool
- Signature: msdc_cmd_is_ready(struct msdc_host * host,struct mmc_request * mrq,struct mmc_command * cmd)
- Line: 1430

### msdc_cmd_next
- Return type: static void
- Signature: msdc_cmd_next(struct msdc_host * host,struct mmc_request * mrq,struct mmc_command * cmd)
- Line: 1490

### msdc_cmd_prepare_raw_cmd
- Return type: static u32
- Signature: msdc_cmd_prepare_raw_cmd(struct msdc_host * host,struct mmc_request * mrq,struct mmc_command * cmd)
- Line: 1175

### msdc_cmdq_irq
- Return type: static irqreturn_t
- Signature: msdc_cmdq_irq(struct msdc_host * host,u32 intsts)
- Line: 1782

### msdc_cqe_cit_cal
- Return type: static void
- Signature: msdc_cqe_cit_cal(struct msdc_host * host,u64 timer_ns)
- Line: 2760

### msdc_cqe_disable
- Return type: static void
- Signature: msdc_cqe_disable(struct mmc_host * mmc,bool recovery)
- Line: 2817

### msdc_cqe_enable
- Return type: static void
- Signature: msdc_cqe_enable(struct mmc_host * mmc)
- Line: 2799

### msdc_cqe_post_disable
- Return type: static void
- Signature: msdc_cqe_post_disable(struct mmc_host * mmc)
- Line: 2853

### msdc_cqe_pre_enable
- Return type: static void
- Signature: msdc_cqe_pre_enable(struct mmc_host * mmc)
- Line: 2843

### msdc_data_prepared
- Return type: static bool
- Signature: msdc_data_prepared(struct mmc_data * data)
- Line: 878

### msdc_data_xfer_done
- Return type: static void
- Signature: msdc_data_xfer_done(struct msdc_host * host,u32 events,struct mmc_request * mrq,struct mmc_data * data)
- Line: 1575

### msdc_data_xfer_next
- Return type: static void
- Signature: msdc_data_xfer_next(struct msdc_host * host,struct mmc_request * mrq)
- Line: 1566

### msdc_deinit_hw
- Return type: static void
- Signature: msdc_deinit_hw(struct msdc_host * host)
- Line: 2091

### msdc_dma_calcs
- Return type: static u8
- Signature: msdc_dma_calcs(u8 * buf,u32 len)
- Line: 793

### msdc_dma_setup
- Return type: static void
- Signature: msdc_dma_setup(struct msdc_host * host,struct msdc_dma * dma,struct mmc_data * data)
- Line: 802

### msdc_drv_probe
- Return type: static int
- Signature: msdc_drv_probe(struct platform_device * pdev)
- Line: 2982

### msdc_drv_remove
- Return type: static void
- Signature: msdc_drv_remove(struct platform_device * pdev)
- Line: 3207

### msdc_enable_sdio_irq
- Return type: static void
- Signature: msdc_enable_sdio_irq(struct mmc_host * mmc,int enb)
- Line: 1738

### msdc_execute_hs400_tuning
- Return type: static int
- Signature: msdc_execute_hs400_tuning(struct mmc_host * mmc,struct mmc_card * card)
- Line: 2638

### msdc_execute_tuning
- Return type: static int
- Signature: msdc_execute_tuning(struct mmc_host * mmc,u32 opcode)
- Line: 2568

### msdc_gate_clock
- Return type: static void
- Signature: msdc_gate_clock(struct msdc_host * host)
- Line: 945

### msdc_get_cd
- Return type: static int
- Signature: msdc_get_cd(struct mmc_host * mmc)
- Line: 2717

### msdc_hs400_enhanced_strobe
- Return type: static void
- Signature: msdc_hs400_enhanced_strobe(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 2735

### msdc_hw_reset
- Return type: static void
- Signature: msdc_hw_reset(struct mmc_host * mmc)
- Line: 2698

### msdc_init_gpd_bd
- Return type: static void
- Signature: msdc_init_gpd_bd(struct msdc_host * host,struct msdc_dma * dma)
- Line: 2109

### msdc_init_hw
- Return type: static void
- Signature: msdc_init_hw(struct msdc_host * host)
- Line: 1874

### msdc_irq
- Return type: static irqreturn_t
- Signature: msdc_irq(int irq,void * dev_id)
- Line: 1811

### msdc_new_tx_setting
- Return type: static void
- Signature: msdc_new_tx_setting(struct msdc_host * host)
- Line: 975

### msdc_of_clock_parse
- Return type: static int
- Signature: msdc_of_clock_parse(struct platform_device * pdev,struct msdc_host * host)
- Line: 2929

### msdc_of_property_parse
- Return type: static void
- Signature: msdc_of_property_parse(struct platform_device * pdev,struct msdc_host * host)
- Line: 2888

### msdc_ops_request
- Return type: static void
- Signature: msdc_ops_request(struct mmc_host * mmc,struct mmc_request * mrq)
- Line: 1506

### msdc_ops_set_ios
- Return type: static void
- Signature: msdc_ops_set_ios(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 2141

### msdc_ops_switch_volt
- Return type: static int
- Signature: msdc_ops_switch_volt(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 1663

### msdc_post_req
- Return type: static void
- Signature: msdc_post_req(struct mmc_host * mmc,struct mmc_request * mrq,int err)
- Line: 1551

### msdc_pre_req
- Return type: static void
- Signature: msdc_pre_req(struct mmc_host * mmc,struct mmc_request * mrq)
- Line: 1539

### msdc_prepare_data
- Return type: static void
- Signature: msdc_prepare_data(struct msdc_host * host,struct mmc_data * data)
- Line: 868

### msdc_prepare_hs400_tuning
- Return type: static int
- Signature: msdc_prepare_hs400_tuning(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 2610

### msdc_recheck_sdio_irq
- Return type: static void
- Signature: msdc_recheck_sdio_irq(struct msdc_host * host)
- Line: 1280

### msdc_request_done
- Return type: static void
- Signature: msdc_request_done(struct msdc_host * host,struct mmc_request * mrq)
- Line: 1308

### msdc_request_timeout
- Return type: static void
- Signature: msdc_request_timeout(struct work_struct * work)
- Line: 1700

### msdc_reset_hw
- Return type: static void
- Signature: msdc_reset_hw(struct msdc_host * host)
- Line: 767

### msdc_restore_reg
- Return type: static void
- Signature: msdc_restore_reg(struct msdc_host * host)
- Line: 3261

### msdc_resume
- Return type: static int
- Signature: msdc_resume(struct device * dev)
- Line: 3377

### msdc_runtime_resume
- Return type: static int
- Signature: msdc_runtime_resume(struct device * dev)
- Line: 3329

### msdc_runtime_suspend
- Return type: static int
- Signature: msdc_runtime_suspend(struct device * dev)
- Line: 3303

### msdc_save_reg
- Return type: static void
- Signature: msdc_save_reg(struct msdc_host * host)
- Line: 3232

### msdc_set_buswidth
- Return type: static void
- Signature: msdc_set_buswidth(struct msdc_host * host,u32 width)
- Line: 1640

### msdc_set_busy_timeout
- Return type: static void
- Signature: msdc_set_busy_timeout(struct msdc_host * host,u64 ns,u64 clks)
- Line: 936

### msdc_set_cmd_delay
- Return type: static void
- Signature: msdc_set_cmd_delay(struct msdc_host * host,u32 value)
- Line: 2242

### msdc_set_data_delay
- Return type: static void
- Signature: msdc_set_data_delay(struct msdc_host * host,u32 value)
- Line: 2272

### msdc_set_data_sample_edge
- Return type: static void
- Signature: msdc_set_data_sample_edge(struct msdc_host * host,bool rising)
- Line: 2303

### msdc_set_mclk
- Return type: static void
- Signature: msdc_set_mclk(struct msdc_host * host,unsigned char timing,u32 hz)
- Line: 1009

### msdc_set_timeout
- Return type: static void
- Signature: msdc_set_timeout(struct msdc_host * host,u64 ns,u64 clks)
- Line: 924

### msdc_start_command
- Return type: static void
- Signature: msdc_start_command(struct msdc_host * host,struct mmc_request * mrq,struct mmc_command * cmd)
- Line: 1460

### msdc_start_data
- Return type: static void
- Signature: msdc_start_data(struct msdc_host * host,struct mmc_command * cmd,struct mmc_data * data)
- Line: 1230

### msdc_suspend
- Return type: static int
- Signature: msdc_suspend(struct device * dev)
- Line: 3352

### msdc_timeout_cal
- Return type: static u64
- Signature: msdc_timeout_cal(struct msdc_host * host,u64 ns,u64 clks)
- Line: 895

### msdc_track_cmd_data
- Return type: static void
- Signature: msdc_track_cmd_data(struct msdc_host * host,struct mmc_command * cmd)
- Line: 1299

### msdc_tune_data
- Return type: static int
- Signature: msdc_tune_data(struct mmc_host * mmc,u32 opcode)
- Line: 2461

### msdc_tune_response
- Return type: static int
- Signature: msdc_tune_response(struct mmc_host * mmc,u32 opcode)
- Line: 2316

### msdc_tune_together
- Return type: static int
- Signature: msdc_tune_together(struct mmc_host * mmc,u32 opcode)
- Line: 2512

### msdc_ungate_clock
- Return type: static int
- Signature: msdc_ungate_clock(struct msdc_host * host)
- Line: 955

### msdc_unprepare_data
- Return type: static void
- Signature: msdc_unprepare_data(struct msdc_host * host,struct mmc_data * data)
- Line: 883

### sdr_clr_bits
- Return type: static void
- Signature: sdr_clr_bits(void __iomem * reg,u32 bs)
- Line: 743

### sdr_get_field
- Return type: static void
- Signature: sdr_get_field(void __iomem * reg,u32 field,u32 * val)
- Line: 760

### sdr_set_bits
- Return type: static void
- Signature: sdr_set_bits(void __iomem * reg,u32 bs)
- Line: 735

### sdr_set_field
- Return type: static void
- Signature: sdr_set_field(void __iomem * reg,u32 field,u32 val)
- Line: 751

### test_delay_bit
- Return type: static u64
- Signature: test_delay_bit(u64 delay,u32 bit)
- Line: 2187

## Structs (8)

### msdc_delay_phase
- Line: 463
- Members:
  - gpd_info: u32
  - next: u32
  - ptr: u32
  - gpd_data_len: u32
  - arg: u32
  - blknum: u32
  - cmd: u32
  - bd_info: u32
  - next: u32
  - ptr: u32
  - bd_data_len: u32
  - sg: scatterlist *
  - gpd: mt_gpdma_desc *
  - bd: mt_bdma_desc *
  - gpd_addr: dma_addr_t
  - bd_addr: dma_addr_t
  - msdc_cfg: u32
  - iocon: u32
  - sdc_cfg: u32
  - pad_tune: u32
  - patch_bit0: u32
  - patch_bit1: u32
  - patch_bit2: u32
  - pad_ds_tune: u32
  - pad_cmd_tune: u32
  - emmc50_cfg0: u32
  - emmc50_cfg3: u32
  - sdc_fifo_cfg: u32
  - emmc_top_control: u32
  - emmc_top_cmd: u32
  - emmc50_pad_ds_tune: u32
  - loop_test_control: u32
  - clk_div_bits: u8
  - recheck_sdio_irq: bool
  - hs400_tune: bool
  - needs_top_base: bool
  - pad_tune_reg: u32
  - async_fifo: bool
  - data_tune: bool
  - busy_check: bool
  - stop_clk_fix: bool
  - stop_dly_sel: u8
  - pop_en_cnt: u8
  - enhance_rx: bool
  - support_64g: bool
  - use_internal_cd: bool
  - support_new_tx: bool
  - support_new_rx: bool
  - support_spm_res_release: bool
  - iocon: u32
  - pad_tune: u32
  - pad_cmd_tune: u32
  - emmc_top_control: u32
  - emmc_top_cmd: u32
  - maxlen: u8
  - start: u8
  - final_phase: u8
  - dev: device *
  - dev_comp: const struct mtk_mmc_compatible *
  - cmd_rsp: int
  - lock: spinlock_t
  - mrq: mmc_request *
  - cmd: mmc_command *
  - data: mmc_data *
  - error: int
  - base: void __iomem *
  - top_base: void __iomem *
  - dma: msdc_dma
  - dma_mask: u64
  - timeout_ns: u32
  - timeout_clks: u32
  - pinctrl: pinctrl *
  - pins_default: pinctrl_state *
  - pins_uhs: pinctrl_state *
  - pins_eint: pinctrl_state *
  - req_timeout: delayed_work
  - irq: int
  - eint_irq: int
  - reset: reset_control *
  - src_clk: clk *
  - h_clk: clk *
  - bus_clk: clk *
  - src_clk_cg: clk *
  - sys_clk_cg: clk *
  - crypto_clk: clk *
  - bulk_clks: clk_bulk_data[]
  - mclk: u32
  - src_clk_freq: u32
  - timing: unsigned char
  - vqmmc_enabled: bool
  - latch_ck: u32
  - hs400_ds_delay: u32
  - hs400_ds_dly3: u32
  - hs200_cmd_int_delay: u32
  - hs400_cmd_int_delay: u32
  - tuning_step: u32
  - hs400_cmd_resp_sel_rising: bool
  - hs400_mode: bool
  - hs400_tuning: bool
  - internal_cd: bool
  - cqhci: bool
  - hsq_en: bool
  - save_para: msdc_save_para
  - def_tune_para: msdc_tune_para
  - saved_tune_para: msdc_tune_para
  - cq_host: cqhci_host *
  - cq_ssc1_time: u32

### msdc_dma
- Line: 408
- Members:
  - gpd_info: u32
  - next: u32
  - ptr: u32
  - gpd_data_len: u32
  - arg: u32
  - blknum: u32
  - cmd: u32
  - bd_info: u32
  - next: u32
  - ptr: u32
  - bd_data_len: u32
  - sg: scatterlist *
  - gpd: mt_gpdma_desc *
  - bd: mt_bdma_desc *
  - gpd_addr: dma_addr_t
  - bd_addr: dma_addr_t
  - msdc_cfg: u32
  - iocon: u32
  - sdc_cfg: u32
  - pad_tune: u32
  - patch_bit0: u32
  - patch_bit1: u32
  - patch_bit2: u32
  - pad_ds_tune: u32
  - pad_cmd_tune: u32
  - emmc50_cfg0: u32
  - emmc50_cfg3: u32
  - sdc_fifo_cfg: u32
  - emmc_top_control: u32
  - emmc_top_cmd: u32
  - emmc50_pad_ds_tune: u32
  - loop_test_control: u32
  - clk_div_bits: u8
  - recheck_sdio_irq: bool
  - hs400_tune: bool
  - needs_top_base: bool
  - pad_tune_reg: u32
  - async_fifo: bool
  - data_tune: bool
  - busy_check: bool
  - stop_clk_fix: bool
  - stop_dly_sel: u8
  - pop_en_cnt: u8
  - enhance_rx: bool
  - support_64g: bool
  - use_internal_cd: bool
  - support_new_tx: bool
  - support_new_rx: bool
  - support_spm_res_release: bool
  - iocon: u32
  - pad_tune: u32
  - pad_cmd_tune: u32
  - emmc_top_control: u32
  - emmc_top_cmd: u32
  - maxlen: u8
  - start: u8
  - final_phase: u8
  - dev: device *
  - dev_comp: const struct mtk_mmc_compatible *
  - cmd_rsp: int
  - lock: spinlock_t
  - mrq: mmc_request *
  - cmd: mmc_command *
  - data: mmc_data *
  - error: int
  - base: void __iomem *
  - top_base: void __iomem *
  - dma: msdc_dma
  - dma_mask: u64
  - timeout_ns: u32
  - timeout_clks: u32
  - pinctrl: pinctrl *
  - pins_default: pinctrl_state *
  - pins_uhs: pinctrl_state *
  - pins_eint: pinctrl_state *
  - req_timeout: delayed_work
  - irq: int
  - eint_irq: int
  - reset: reset_control *
  - src_clk: clk *
  - h_clk: clk *
  - bus_clk: clk *
  - src_clk_cg: clk *
  - sys_clk_cg: clk *
  - crypto_clk: clk *
  - bulk_clks: clk_bulk_data[]
  - mclk: u32
  - src_clk_freq: u32
  - timing: unsigned char
  - vqmmc_enabled: bool
  - latch_ck: u32
  - hs400_ds_delay: u32
  - hs400_ds_dly3: u32
  - hs200_cmd_int_delay: u32
  - hs400_cmd_int_delay: u32
  - tuning_step: u32
  - hs400_cmd_resp_sel_rising: bool
  - hs400_mode: bool
  - hs400_tuning: bool
  - internal_cd: bool
  - cqhci: bool
  - hsq_en: bool
  - save_para: msdc_save_para
  - def_tune_para: msdc_tune_para
  - saved_tune_para: msdc_tune_para
  - cq_host: cqhci_host *
  - cq_ssc1_time: u32

### msdc_host
- Line: 469
- Members:
  - gpd_info: u32
  - next: u32
  - ptr: u32
  - gpd_data_len: u32
  - arg: u32
  - blknum: u32
  - cmd: u32
  - bd_info: u32
  - next: u32
  - ptr: u32
  - bd_data_len: u32
  - sg: scatterlist *
  - gpd: mt_gpdma_desc *
  - bd: mt_bdma_desc *
  - gpd_addr: dma_addr_t
  - bd_addr: dma_addr_t
  - msdc_cfg: u32
  - iocon: u32
  - sdc_cfg: u32
  - pad_tune: u32
  - patch_bit0: u32
  - patch_bit1: u32
  - patch_bit2: u32
  - pad_ds_tune: u32
  - pad_cmd_tune: u32
  - emmc50_cfg0: u32
  - emmc50_cfg3: u32
  - sdc_fifo_cfg: u32
  - emmc_top_control: u32
  - emmc_top_cmd: u32
  - emmc50_pad_ds_tune: u32
  - loop_test_control: u32
  - clk_div_bits: u8
  - recheck_sdio_irq: bool
  - hs400_tune: bool
  - needs_top_base: bool
  - pad_tune_reg: u32
  - async_fifo: bool
  - data_tune: bool
  - busy_check: bool
  - stop_clk_fix: bool
  - stop_dly_sel: u8
  - pop_en_cnt: u8
  - enhance_rx: bool
  - support_64g: bool
  - use_internal_cd: bool
  - support_new_tx: bool
  - support_new_rx: bool
  - support_spm_res_release: bool
  - iocon: u32
  - pad_tune: u32
  - pad_cmd_tune: u32
  - emmc_top_control: u32
  - emmc_top_cmd: u32
  - maxlen: u8
  - start: u8
  - final_phase: u8
  - dev: device *
  - dev_comp: const struct mtk_mmc_compatible *
  - cmd_rsp: int
  - lock: spinlock_t
  - mrq: mmc_request *
  - cmd: mmc_command *
  - data: mmc_data *
  - error: int
  - base: void __iomem *
  - top_base: void __iomem *
  - dma: msdc_dma
  - dma_mask: u64
  - timeout_ns: u32
  - timeout_clks: u32
  - pinctrl: pinctrl *
  - pins_default: pinctrl_state *
  - pins_uhs: pinctrl_state *
  - pins_eint: pinctrl_state *
  - req_timeout: delayed_work
  - irq: int
  - eint_irq: int
  - reset: reset_control *
  - src_clk: clk *
  - h_clk: clk *
  - bus_clk: clk *
  - src_clk_cg: clk *
  - sys_clk_cg: clk *
  - crypto_clk: clk *
  - bulk_clks: clk_bulk_data[]
  - mclk: u32
  - src_clk_freq: u32
  - timing: unsigned char
  - vqmmc_enabled: bool
  - latch_ck: u32
  - hs400_ds_delay: u32
  - hs400_ds_dly3: u32
  - hs200_cmd_int_delay: u32
  - hs400_cmd_int_delay: u32
  - tuning_step: u32
  - hs400_cmd_resp_sel_rising: bool
  - hs400_mode: bool
  - hs400_tuning: bool
  - internal_cd: bool
  - cqhci: bool
  - hsq_en: bool
  - save_para: msdc_save_para
  - def_tune_para: msdc_tune_para
  - saved_tune_para: msdc_tune_para
  - cq_host: cqhci_host *
  - cq_ssc1_time: u32

### msdc_save_para
- Line: 416
- Members:
  - gpd_info: u32
  - next: u32
  - ptr: u32
  - gpd_data_len: u32
  - arg: u32
  - blknum: u32
  - cmd: u32
  - bd_info: u32
  - next: u32
  - ptr: u32
  - bd_data_len: u32
  - sg: scatterlist *
  - gpd: mt_gpdma_desc *
  - bd: mt_bdma_desc *
  - gpd_addr: dma_addr_t
  - bd_addr: dma_addr_t
  - msdc_cfg: u32
  - iocon: u32
  - sdc_cfg: u32
  - pad_tune: u32
  - patch_bit0: u32
  - patch_bit1: u32
  - patch_bit2: u32
  - pad_ds_tune: u32
  - pad_cmd_tune: u32
  - emmc50_cfg0: u32
  - emmc50_cfg3: u32
  - sdc_fifo_cfg: u32
  - emmc_top_control: u32
  - emmc_top_cmd: u32
  - emmc50_pad_ds_tune: u32
  - loop_test_control: u32
  - clk_div_bits: u8
  - recheck_sdio_irq: bool
  - hs400_tune: bool
  - needs_top_base: bool
  - pad_tune_reg: u32
  - async_fifo: bool
  - data_tune: bool
  - busy_check: bool
  - stop_clk_fix: bool
  - stop_dly_sel: u8
  - pop_en_cnt: u8
  - enhance_rx: bool
  - support_64g: bool
  - use_internal_cd: bool
  - support_new_tx: bool
  - support_new_rx: bool
  - support_spm_res_release: bool
  - iocon: u32
  - pad_tune: u32
  - pad_cmd_tune: u32
  - emmc_top_control: u32
  - emmc_top_cmd: u32
  - maxlen: u8
  - start: u8
  - final_phase: u8
  - dev: device *
  - dev_comp: const struct mtk_mmc_compatible *
  - cmd_rsp: int
  - lock: spinlock_t
  - mrq: mmc_request *
  - cmd: mmc_command *
  - data: mmc_data *
  - error: int
  - base: void __iomem *
  - top_base: void __iomem *
  - dma: msdc_dma
  - dma_mask: u64
  - timeout_ns: u32
  - timeout_clks: u32
  - pinctrl: pinctrl *
  - pins_default: pinctrl_state *
  - pins_uhs: pinctrl_state *
  - pins_eint: pinctrl_state *
  - req_timeout: delayed_work
  - irq: int
  - eint_irq: int
  - reset: reset_control *
  - src_clk: clk *
  - h_clk: clk *
  - bus_clk: clk *
  - src_clk_cg: clk *
  - sys_clk_cg: clk *
  - crypto_clk: clk *
  - bulk_clks: clk_bulk_data[]
  - mclk: u32
  - src_clk_freq: u32
  - timing: unsigned char
  - vqmmc_enabled: bool
  - latch_ck: u32
  - hs400_ds_delay: u32
  - hs400_ds_dly3: u32
  - hs200_cmd_int_delay: u32
  - hs400_cmd_int_delay: u32
  - tuning_step: u32
  - hs400_cmd_resp_sel_rising: bool
  - hs400_mode: bool
  - hs400_tuning: bool
  - internal_cd: bool
  - cqhci: bool
  - hsq_en: bool
  - save_para: msdc_save_para
  - def_tune_para: msdc_tune_para
  - saved_tune_para: msdc_tune_para
  - cq_host: cqhci_host *
  - cq_ssc1_time: u32

### msdc_tune_para
- Line: 455
- Members:
  - gpd_info: u32
  - next: u32
  - ptr: u32
  - gpd_data_len: u32
  - arg: u32
  - blknum: u32
  - cmd: u32
  - bd_info: u32
  - next: u32
  - ptr: u32
  - bd_data_len: u32
  - sg: scatterlist *
  - gpd: mt_gpdma_desc *
  - bd: mt_bdma_desc *
  - gpd_addr: dma_addr_t
  - bd_addr: dma_addr_t
  - msdc_cfg: u32
  - iocon: u32
  - sdc_cfg: u32
  - pad_tune: u32
  - patch_bit0: u32
  - patch_bit1: u32
  - patch_bit2: u32
  - pad_ds_tune: u32
  - pad_cmd_tune: u32
  - emmc50_cfg0: u32
  - emmc50_cfg3: u32
  - sdc_fifo_cfg: u32
  - emmc_top_control: u32
  - emmc_top_cmd: u32
  - emmc50_pad_ds_tune: u32
  - loop_test_control: u32
  - clk_div_bits: u8
  - recheck_sdio_irq: bool
  - hs400_tune: bool
  - needs_top_base: bool
  - pad_tune_reg: u32
  - async_fifo: bool
  - data_tune: bool
  - busy_check: bool
  - stop_clk_fix: bool
  - stop_dly_sel: u8
  - pop_en_cnt: u8
  - enhance_rx: bool
  - support_64g: bool
  - use_internal_cd: bool
  - support_new_tx: bool
  - support_new_rx: bool
  - support_spm_res_release: bool
  - iocon: u32
  - pad_tune: u32
  - pad_cmd_tune: u32
  - emmc_top_control: u32
  - emmc_top_cmd: u32
  - maxlen: u8
  - start: u8
  - final_phase: u8
  - dev: device *
  - dev_comp: const struct mtk_mmc_compatible *
  - cmd_rsp: int
  - lock: spinlock_t
  - mrq: mmc_request *
  - cmd: mmc_command *
  - data: mmc_data *
  - error: int
  - base: void __iomem *
  - top_base: void __iomem *
  - dma: msdc_dma
  - dma_mask: u64
  - timeout_ns: u32
  - timeout_clks: u32
  - pinctrl: pinctrl *
  - pins_default: pinctrl_state *
  - pins_uhs: pinctrl_state *
  - pins_eint: pinctrl_state *
  - req_timeout: delayed_work
  - irq: int
  - eint_irq: int
  - reset: reset_control *
  - src_clk: clk *
  - h_clk: clk *
  - bus_clk: clk *
  - src_clk_cg: clk *
  - sys_clk_cg: clk *
  - crypto_clk: clk *
  - bulk_clks: clk_bulk_data[]
  - mclk: u32
  - src_clk_freq: u32
  - timing: unsigned char
  - vqmmc_enabled: bool
  - latch_ck: u32
  - hs400_ds_delay: u32
  - hs400_ds_dly3: u32
  - hs200_cmd_int_delay: u32
  - hs400_cmd_int_delay: u32
  - tuning_step: u32
  - hs400_cmd_resp_sel_rising: bool
  - hs400_mode: bool
  - hs400_tuning: bool
  - internal_cd: bool
  - cqhci: bool
  - hsq_en: bool
  - save_para: msdc_save_para
  - def_tune_para: msdc_tune_para
  - saved_tune_para: msdc_tune_para
  - cq_host: cqhci_host *
  - cq_ssc1_time: u32

### mt_bdma_desc
- Line: 393
- Members:
  - gpd_info: u32
  - next: u32
  - ptr: u32
  - gpd_data_len: u32
  - arg: u32
  - blknum: u32
  - cmd: u32
  - bd_info: u32
  - next: u32
  - ptr: u32
  - bd_data_len: u32
  - sg: scatterlist *
  - gpd: mt_gpdma_desc *
  - bd: mt_bdma_desc *
  - gpd_addr: dma_addr_t
  - bd_addr: dma_addr_t
  - msdc_cfg: u32
  - iocon: u32
  - sdc_cfg: u32
  - pad_tune: u32
  - patch_bit0: u32
  - patch_bit1: u32
  - patch_bit2: u32
  - pad_ds_tune: u32
  - pad_cmd_tune: u32
  - emmc50_cfg0: u32
  - emmc50_cfg3: u32
  - sdc_fifo_cfg: u32
  - emmc_top_control: u32
  - emmc_top_cmd: u32
  - emmc50_pad_ds_tune: u32
  - loop_test_control: u32
  - clk_div_bits: u8
  - recheck_sdio_irq: bool
  - hs400_tune: bool
  - needs_top_base: bool
  - pad_tune_reg: u32
  - async_fifo: bool
  - data_tune: bool
  - busy_check: bool
  - stop_clk_fix: bool
  - stop_dly_sel: u8
  - pop_en_cnt: u8
  - enhance_rx: bool
  - support_64g: bool
  - use_internal_cd: bool
  - support_new_tx: bool
  - support_new_rx: bool
  - support_spm_res_release: bool
  - iocon: u32
  - pad_tune: u32
  - pad_cmd_tune: u32
  - emmc_top_control: u32
  - emmc_top_cmd: u32
  - maxlen: u8
  - start: u8
  - final_phase: u8
  - dev: device *
  - dev_comp: const struct mtk_mmc_compatible *
  - cmd_rsp: int
  - lock: spinlock_t
  - mrq: mmc_request *
  - cmd: mmc_command *
  - data: mmc_data *
  - error: int
  - base: void __iomem *
  - top_base: void __iomem *
  - dma: msdc_dma
  - dma_mask: u64
  - timeout_ns: u32
  - timeout_clks: u32
  - pinctrl: pinctrl *
  - pins_default: pinctrl_state *
  - pins_uhs: pinctrl_state *
  - pins_eint: pinctrl_state *
  - req_timeout: delayed_work
  - irq: int
  - eint_irq: int
  - reset: reset_control *
  - src_clk: clk *
  - h_clk: clk *
  - bus_clk: clk *
  - src_clk_cg: clk *
  - sys_clk_cg: clk *
  - crypto_clk: clk *
  - bulk_clks: clk_bulk_data[]
  - mclk: u32
  - src_clk_freq: u32
  - timing: unsigned char
  - vqmmc_enabled: bool
  - latch_ck: u32
  - hs400_ds_delay: u32
  - hs400_ds_dly3: u32
  - hs200_cmd_int_delay: u32
  - hs400_cmd_int_delay: u32
  - tuning_step: u32
  - hs400_cmd_resp_sel_rising: bool
  - hs400_mode: bool
  - hs400_tuning: bool
  - internal_cd: bool
  - cqhci: bool
  - hsq_en: bool
  - save_para: msdc_save_para
  - def_tune_para: msdc_tune_para
  - saved_tune_para: msdc_tune_para
  - cq_host: cqhci_host *
  - cq_ssc1_time: u32

### mt_gpdma_desc
- Line: 375
- Members:
  - gpd_info: u32
  - next: u32
  - ptr: u32
  - gpd_data_len: u32
  - arg: u32
  - blknum: u32
  - cmd: u32
  - bd_info: u32
  - next: u32
  - ptr: u32
  - bd_data_len: u32
  - sg: scatterlist *
  - gpd: mt_gpdma_desc *
  - bd: mt_bdma_desc *
  - gpd_addr: dma_addr_t
  - bd_addr: dma_addr_t
  - msdc_cfg: u32
  - iocon: u32
  - sdc_cfg: u32
  - pad_tune: u32
  - patch_bit0: u32
  - patch_bit1: u32
  - patch_bit2: u32
  - pad_ds_tune: u32
  - pad_cmd_tune: u32
  - emmc50_cfg0: u32
  - emmc50_cfg3: u32
  - sdc_fifo_cfg: u32
  - emmc_top_control: u32
  - emmc_top_cmd: u32
  - emmc50_pad_ds_tune: u32
  - loop_test_control: u32
  - clk_div_bits: u8
  - recheck_sdio_irq: bool
  - hs400_tune: bool
  - needs_top_base: bool
  - pad_tune_reg: u32
  - async_fifo: bool
  - data_tune: bool
  - busy_check: bool
  - stop_clk_fix: bool
  - stop_dly_sel: u8
  - pop_en_cnt: u8
  - enhance_rx: bool
  - support_64g: bool
  - use_internal_cd: bool
  - support_new_tx: bool
  - support_new_rx: bool
  - support_spm_res_release: bool
  - iocon: u32
  - pad_tune: u32
  - pad_cmd_tune: u32
  - emmc_top_control: u32
  - emmc_top_cmd: u32
  - maxlen: u8
  - start: u8
  - final_phase: u8
  - dev: device *
  - dev_comp: const struct mtk_mmc_compatible *
  - cmd_rsp: int
  - lock: spinlock_t
  - mrq: mmc_request *
  - cmd: mmc_command *
  - data: mmc_data *
  - error: int
  - base: void __iomem *
  - top_base: void __iomem *
  - dma: msdc_dma
  - dma_mask: u64
  - timeout_ns: u32
  - timeout_clks: u32
  - pinctrl: pinctrl *
  - pins_default: pinctrl_state *
  - pins_uhs: pinctrl_state *
  - pins_eint: pinctrl_state *
  - req_timeout: delayed_work
  - irq: int
  - eint_irq: int
  - reset: reset_control *
  - src_clk: clk *
  - h_clk: clk *
  - bus_clk: clk *
  - src_clk_cg: clk *
  - sys_clk_cg: clk *
  - crypto_clk: clk *
  - bulk_clks: clk_bulk_data[]
  - mclk: u32
  - src_clk_freq: u32
  - timing: unsigned char
  - vqmmc_enabled: bool
  - latch_ck: u32
  - hs400_ds_delay: u32
  - hs400_ds_dly3: u32
  - hs200_cmd_int_delay: u32
  - hs400_cmd_int_delay: u32
  - tuning_step: u32
  - hs400_cmd_resp_sel_rising: bool
  - hs400_mode: bool
  - hs400_tuning: bool
  - internal_cd: bool
  - cqhci: bool
  - hsq_en: bool
  - save_para: msdc_save_para
  - def_tune_para: msdc_tune_para
  - saved_tune_para: msdc_tune_para
  - cq_host: cqhci_host *
  - cq_ssc1_time: u32

### mtk_mmc_compatible
- Line: 435
- Members:
  - gpd_info: u32
  - next: u32
  - ptr: u32
  - gpd_data_len: u32
  - arg: u32
  - blknum: u32
  - cmd: u32
  - bd_info: u32
  - next: u32
  - ptr: u32
  - bd_data_len: u32
  - sg: scatterlist *
  - gpd: mt_gpdma_desc *
  - bd: mt_bdma_desc *
  - gpd_addr: dma_addr_t
  - bd_addr: dma_addr_t
  - msdc_cfg: u32
  - iocon: u32
  - sdc_cfg: u32
  - pad_tune: u32
  - patch_bit0: u32
  - patch_bit1: u32
  - patch_bit2: u32
  - pad_ds_tune: u32
  - pad_cmd_tune: u32
  - emmc50_cfg0: u32
  - emmc50_cfg3: u32
  - sdc_fifo_cfg: u32
  - emmc_top_control: u32
  - emmc_top_cmd: u32
  - emmc50_pad_ds_tune: u32
  - loop_test_control: u32
  - clk_div_bits: u8
  - recheck_sdio_irq: bool
  - hs400_tune: bool
  - needs_top_base: bool
  - pad_tune_reg: u32
  - async_fifo: bool
  - data_tune: bool
  - busy_check: bool
  - stop_clk_fix: bool
  - stop_dly_sel: u8
  - pop_en_cnt: u8
  - enhance_rx: bool
  - support_64g: bool
  - use_internal_cd: bool
  - support_new_tx: bool
  - support_new_rx: bool
  - support_spm_res_release: bool
  - iocon: u32
  - pad_tune: u32
  - pad_cmd_tune: u32
  - emmc_top_control: u32
  - emmc_top_cmd: u32
  - maxlen: u8
  - start: u8
  - final_phase: u8
  - dev: device *
  - dev_comp: const struct mtk_mmc_compatible *
  - cmd_rsp: int
  - lock: spinlock_t
  - mrq: mmc_request *
  - cmd: mmc_command *
  - data: mmc_data *
  - error: int
  - base: void __iomem *
  - top_base: void __iomem *
  - dma: msdc_dma
  - dma_mask: u64
  - timeout_ns: u32
  - timeout_clks: u32
  - pinctrl: pinctrl *
  - pins_default: pinctrl_state *
  - pins_uhs: pinctrl_state *
  - pins_eint: pinctrl_state *
  - req_timeout: delayed_work
  - irq: int
  - eint_irq: int
  - reset: reset_control *
  - src_clk: clk *
  - h_clk: clk *
  - bus_clk: clk *
  - src_clk_cg: clk *
  - sys_clk_cg: clk *
  - crypto_clk: clk *
  - bulk_clks: clk_bulk_data[]
  - mclk: u32
  - src_clk_freq: u32
  - timing: unsigned char
  - vqmmc_enabled: bool
  - latch_ck: u32
  - hs400_ds_delay: u32
  - hs400_ds_dly3: u32
  - hs200_cmd_int_delay: u32
  - hs400_cmd_int_delay: u32
  - tuning_step: u32
  - hs400_cmd_resp_sel_rising: bool
  - hs400_mode: bool
  - hs400_tuning: bool
  - internal_cd: bool
  - cqhci: bool
  - hsq_en: bool
  - save_para: msdc_save_para
  - def_tune_para: msdc_tune_para
  - saved_tune_para: msdc_tune_para
  - cq_host: cqhci_host *
  - cq_ssc1_time: u32

## Variables (20)

- static **cmd_ints_mask** : const u32 (line 786)
- static **data_ints_mask** : const u32 (line 789)
- static **msdc_cmdq_ops** : const struct cqhci_host_ops (line 2881)
- static **msdc_dev_pm_ops** : const struct dev_pm_ops (line 3388)
- static **msdc_of_ids** : const struct of_device_id[] (line 715)
- static **mt2701_compat** : const struct mtk_mmc_compatible (line 529)
- static **mt2712_compat** : const struct mtk_mmc_compatible (line 542)
- static **mt6779_compat** : const struct mtk_mmc_compatible (line 556)
- static **mt6795_compat** : const struct mtk_mmc_compatible (line 570)
- static **mt7620_compat** : const struct mtk_mmc_compatible (line 583)
- static **mt7622_compat** : const struct mtk_mmc_compatible (line 596)
- static **mt7986_compat** : const struct mtk_mmc_compatible (line 610)
- static **mt8135_compat** : const struct mtk_mmc_compatible (line 625)
- static **mt8173_compat** : const struct mtk_mmc_compatible (line 638)
- static **mt8183_compat** : const struct mtk_mmc_compatible (line 651)
- static **mt8189_compat** : const struct mtk_mmc_compatible (line 678)
- static **mt8196_compat** : const struct mtk_mmc_compatible (line 697)
- static **mt8516_compat** : const struct mtk_mmc_compatible (line 666)
- static **mt_msdc_driver** : platform_driver (line 3393)
- static **mt_msdc_ops** : const struct mmc_host_ops (line 2863)

## Macros (273)

- **BDMA_DESC_BLKPAD** (line 397)
- **BDMA_DESC_BUFLEN** (line 404)
- **BDMA_DESC_BUFLEN_EXT** (line 405)
- **BDMA_DESC_CHECKSUM** (line 396)
- **BDMA_DESC_DWPAD** (line 398)
- **BDMA_DESC_EOL** (line 395)
- **BDMA_DESC_NEXT_H4** (line 399)
- **BDMA_DESC_PTR_H4** (line 400)
- **CMDQ_RDAT_CNT** (line 301)
- **CMD_TIMEOUT** (line 364)
- **CQHCI_RD_CMD_WND_SEL** (line 320)
- **CQHCI_SETTING** (line 90)
- **CQHCI_WR_CMD_WND_SEL** (line 321)
- **DATA_K_VALUE_SEL** (line 330)
- **DAT_TIMEOUT** (line 365)
- **DEFAULT_DEBOUNCE** (line 367)
- **DELAY_EN** (line 325)
- **DMA_ADDR_HIGH_4BIT** (line 220)
- **DMA_SA_H4BIT** (line 73)
- **EMMC50_CFG0** (line 85)
- **EMMC50_CFG1** (line 86)
- **EMMC50_CFG1_DS_CFG** (line 309)
- **EMMC50_CFG2** (line 87)
- **EMMC50_CFG2_AXI_SET_LEN** (line 312)
- **EMMC50_CFG3** (line 88)
- **EMMC50_CFG3_OUTS_WR** (line 314)
- **EMMC50_CFG_CFCSTS_SEL** (line 305)
- **EMMC50_CFG_CMD_RESP_SEL** (line 306)
- **EMMC50_CFG_CRCSTS_EDGE** (line 304)
- **EMMC50_CFG_PADCMD_LATCHCK** (line 303)
- **EMMC50_PAD_DS_TUNE** (line 97)
- **EMMC51_CFG0** (line 84)
- **EMMC_IOCON** (line 71)
- **EMMC_TOP_CMD** (line 96)
- **EMMC_TOP_CONTROL** (line 95)
- **GPDMA_DESC_BDP** (line 378)
- **GPDMA_DESC_BUFLEN** (line 386)
- **GPDMA_DESC_CHECKSUM** (line 379)
- **GPDMA_DESC_EXTLEN** (line 387)
- **GPDMA_DESC_HWO** (line 377)
- **GPDMA_DESC_INT** (line 380)
- **GPDMA_DESC_NEXT_H4** (line 381)
- **GPDMA_DESC_PTR_H4** (line 382)
- **LOOP_EN_SEL_CLK** (line 349)
- **LOOP_TEST_CONTROL** (line 98)
- **MAX_BD_NUM** (line 39)
- **MSDC_ASYNC_FLAG** (line 360)
- **MSDC_BURST_64B** (line 49)
- **MSDC_BUS_1BITS** (line 45)
- **MSDC_BUS_4BITS** (line 46)
- **MSDC_BUS_8BITS** (line 47)
- **MSDC_CFG** (line 54)
- **MSDC_CFG_BV18PSS** (line 111)
- **MSDC_CFG_BV18SDT** (line 110)
- **MSDC_CFG_CKDIV** (line 113)
- **MSDC_CFG_CKDIV_EXTRA** (line 117)
- **MSDC_CFG_CKDRVEN** (line 109)
- **MSDC_CFG_CKMOD** (line 114)
- **MSDC_CFG_CKMOD_EXTRA** (line 118)
- **MSDC_CFG_CKPDN** (line 106)
- **MSDC_CFG_CKSTB** (line 112)
- **MSDC_CFG_HS400_CK_MODE** (line 115)
- **MSDC_CFG_HS400_CK_MODE_EXTRA** (line 116)
- **MSDC_CFG_MODE** (line 105)
- **MSDC_CFG_PIO** (line 108)
- **MSDC_CFG_RST** (line 107)
- **MSDC_CKGEN_MSDC_DLY_SEL** (line 243)
- **MSDC_DMA_CFG** (line 76)
- **MSDC_DMA_CFG_ACTIVEEN** (line 234)
- **MSDC_DMA_CFG_AHBHPROT2** (line 233)
- **MSDC_DMA_CFG_CS12B16B** (line 235)
- **MSDC_DMA_CFG_DECSEN** (line 232)
- **MSDC_DMA_CFG_STS** (line 231)
- **MSDC_DMA_CTRL** (line 75)
- **MSDC_DMA_CTRL_BRUSTSZ** (line 228)
- **MSDC_DMA_CTRL_LASTBUF** (line 227)
- **MSDC_DMA_CTRL_MODE** (line 226)
- **MSDC_DMA_CTRL_RESUME** (line 225)
- **MSDC_DMA_CTRL_START** (line 223)
- **MSDC_DMA_CTRL_STOP** (line 224)
- **MSDC_DMA_SA** (line 74)
- **MSDC_FIFOCS** (line 59)
- **MSDC_FIFOCS_CLR** (line 193)
- **MSDC_FIFOCS_RXCNT** (line 191)
- **MSDC_FIFOCS_TXCNT** (line 192)
- **MSDC_INT** (line 57)
- **MSDC_INTEN** (line 58)
- **MSDC_INTEN_ACMD19_DONE** (line 185)
- **MSDC_INTEN_ACMDCRCERR** (line 174)
- **MSDC_INTEN_ACMDRDY** (line 172)
- **MSDC_INTEN_ACMDTMO** (line 173)
- **MSDC_INTEN_CDSC** (line 171)
- **MSDC_INTEN_CMDRDY** (line 177)
- **MSDC_INTEN_CMDTMO** (line 178)
- **MSDC_INTEN_CSTA** (line 180)
- **MSDC_INTEN_DATCRCERR** (line 184)
- **MSDC_INTEN_DATTMO** (line 183)
- **MSDC_INTEN_DMAQ_EMPTY** (line 175)
- **MSDC_INTEN_DMA_BDCSERR** (line 186)
- **MSDC_INTEN_DMA_GPDCSERR** (line 187)
- **MSDC_INTEN_DMA_PROTECT** (line 188)
- **MSDC_INTEN_DXFER_DONE** (line 182)
- **MSDC_INTEN_MMCIRQ** (line 170)
- **MSDC_INTEN_RSPCRCERR** (line 179)
- **MSDC_INTEN_SDIOIRQ** (line 176)
- **MSDC_INTEN_XFER_COMPL** (line 181)
- **MSDC_INT_ACMD19_DONE** (line 163)
- **MSDC_INT_ACMDCRCERR** (line 152)
- **MSDC_INT_ACMDRDY** (line 150)
- **MSDC_INT_ACMDTMO** (line 151)
- **MSDC_INT_CDSC** (line 149)
- **MSDC_INT_CMDQ** (line 167)
- **MSDC_INT_CMDRDY** (line 155)
- **MSDC_INT_CMDTMO** (line 156)
- **MSDC_INT_CSTA** (line 158)
- **MSDC_INT_DATCRCERR** (line 162)
- **MSDC_INT_DATTMO** (line 161)
- **MSDC_INT_DAT_LATCH_CK_SEL** (line 242)
- **MSDC_INT_DMAQ_EMPTY** (line 153)
- **MSDC_INT_DMA_BDCSERR** (line 164)
- **MSDC_INT_DMA_GPDCSERR** (line 165)
- **MSDC_INT_DMA_PROTECT** (line 166)
- **MSDC_INT_DXFER_DONE** (line 160)
- **MSDC_INT_MMCIRQ** (line 148)
- **MSDC_INT_RSPCRCERR** (line 157)
- **MSDC_INT_SDIOIRQ** (line 154)
- **MSDC_INT_XFER_COMPL** (line 159)
- **MSDC_IOCON** (line 55)
- **MSDC_IOCON_D0SPL** (line 128)
- **MSDC_IOCON_D1SPL** (line 129)
- **MSDC_IOCON_D2SPL** (line 130)
- **MSDC_IOCON_D3SPL** (line 131)
- **MSDC_IOCON_D4SPL** (line 132)
- **MSDC_IOCON_D5SPL** (line 133)
- **MSDC_IOCON_D6SPL** (line 134)
- **MSDC_IOCON_D7SPL** (line 135)
- **MSDC_IOCON_DDLSEL** (line 124)
- **MSDC_IOCON_DDR50CKD** (line 125)
- **MSDC_IOCON_DSPL** (line 123)
- **MSDC_IOCON_DSPLSEL** (line 126)
- **MSDC_IOCON_RISCSZ** (line 136)
- **MSDC_IOCON_RSPL** (line 122)
- **MSDC_IOCON_SDR104CKS** (line 121)
- **MSDC_IOCON_W_DSPL** (line 127)
- **MSDC_MMAP_FLAG** (line 361)
- **MSDC_NEW_RX_CFG** (line 70)
- **MSDC_NEW_RX_PATH_SEL** (line 217)
- **MSDC_NR_CLOCKS** (line 40)
- **MSDC_PAD_TUNE** (line 80)
- **MSDC_PAD_TUNE0** (line 81)
- **MSDC_PAD_TUNE_CLKTDLY** (line 285)
- **MSDC_PAD_TUNE_CMD2_SEL** (line 290)
- **MSDC_PAD_TUNE_CMDRDLY** (line 282)
- **MSDC_PAD_TUNE_CMDRDLY2** (line 283)
- **MSDC_PAD_TUNE_CMDRRDLY** (line 284)
- **MSDC_PAD_TUNE_CMD_SEL** (line 288)
- **MSDC_PAD_TUNE_DATRRDLY** (line 280)
- **MSDC_PAD_TUNE_DATRRDLY2** (line 281)
- **MSDC_PAD_TUNE_DATWRDLY** (line 279)
- **MSDC_PAD_TUNE_RD2_SEL** (line 289)
- **MSDC_PAD_TUNE_RD_SEL** (line 287)
- **MSDC_PAD_TUNE_RXDLYSEL** (line 286)
- **MSDC_PATCH_BIT** (line 77)
- **MSDC_PATCH_BIT1** (line 78)
- **MSDC_PATCH_BIT1_CMDTA** (line 256)
- **MSDC_PATCH_BIT1_STOP_DLY** (line 258)
- **MSDC_PATCH_BIT2** (line 79)
- **MSDC_PATCH_BIT2_CFGCRCSTS** (line 271)
- **MSDC_PATCH_BIT2_CFGRESP** (line 270)
- **MSDC_PATCH_BIT_BUSYDLY** (line 246)
- **MSDC_PATCH_BIT_CMDFSEL** (line 249)
- **MSDC_PATCH_BIT_DECRCTMO** (line 252)
- **MSDC_PATCH_BIT_DESCUP_SEL** (line 241)
- **MSDC_PATCH_BIT_DIS_WRMON** (line 239)
- **MSDC_PATCH_BIT_IDRTSEL** (line 248)
- **MSDC_PATCH_BIT_INTDLSEL** (line 250)
- **MSDC_PATCH_BIT_IODSSEL** (line 244)
- **MSDC_PATCH_BIT_IOINTSEL** (line 245)
- **MSDC_PATCH_BIT_ODDSUPP** (line 238)
- **MSDC_PATCH_BIT_RD_DAT_SEL** (line 240)
- **MSDC_PATCH_BIT_SPCPUSH** (line 251)
- **MSDC_PATCH_BIT_WDOD** (line 247)
- **MSDC_PB1_AHB_GDMA_HCLK** (line 266)
- **MSDC_PB1_AUTO_SYNCST_CLR** (line 262)
- **MSDC_PB1_BUSY_CHECK_SEL** (line 257)
- **MSDC_PB1_DDR_CMD_FIX_SEL** (line 259)
- **MSDC_PB1_LP_DCM_EN** (line 264)
- **MSDC_PB1_MARK_POP_WATER** (line 263)
- **MSDC_PB1_MSDC_CLK_ENFEAT** (line 267)
- **MSDC_PB1_RSVD20** (line 261)
- **MSDC_PB1_RSVD3** (line 265)
- **MSDC_PB1_SINGLE_BURST** (line 260)
- **MSDC_PB1_WRDAT_CRC_TACNTR** (line 255)
- **MSDC_PB2_CFGCRCSTSEDGE** (line 276)
- **MSDC_PB2_CRCSTSENSEL** (line 277)
- **MSDC_PB2_POP_EN_CNT** (line 275)
- **MSDC_PB2_RESPSTSENSEL** (line 274)
- **MSDC_PB2_RESPWAIT** (line 273)
- **MSDC_PB2_SUPPORT_64G** (line 272)
- **MSDC_PREPARE_FLAG** (line 359)
- **MSDC_PS** (line 56)
- **MSDC_PS_CDDEBOUNCE** (line 141)
- **MSDC_PS_CDEN** (line 139)
- **MSDC_PS_CDSTS** (line 140)
- **MSDC_PS_CMD** (line 144)
- **MSDC_PS_DAT** (line 142)
- **MSDC_PS_DATA1** (line 143)
- **MSDC_PS_WP** (line 145)
- **MTK_MMC_AUTOSUSPEND_DELAY** (line 363)
- **PAD_CMD_RD_RXDLY2_SEL** (line 336)
- **PAD_CMD_RD_RXDLY_SEL** (line 337)
- **PAD_CMD_RXDLY** (line 335)
- **PAD_CMD_RXDLY2** (line 334)
- **PAD_CMD_TUNE** (line 83)
- **PAD_CMD_TUNE_RX_DLY3** (line 298)
- **PAD_CMD_TX_DLY** (line 338)
- **PAD_DAT_RD_RXDLY** (line 327)
- **PAD_DAT_RD_RXDLY2** (line 326)
- **PAD_DAT_RD_RXDLY2_SEL** (line 328)
- **PAD_DAT_RD_RXDLY_SEL** (line 329)
- **PAD_DELAY_FULL** (line 371)
- **PAD_DELAY_HALF** (line 370)
- **PAD_DS_DLY1** (line 343)
- **PAD_DS_DLY2_SEL** (line 342)
- **PAD_DS_DLY3** (line 344)
- **PAD_DS_DLY_SEL** (line 341)
- **PAD_DS_TUNE** (line 82)
- **PAD_DS_TUNE_DLY1** (line 294)
- **PAD_DS_TUNE_DLY2** (line 295)
- **PAD_DS_TUNE_DLY2_SEL** (line 293)
- **PAD_DS_TUNE_DLY3** (line 296)
- **PAD_DS_TUNE_DLY_SEL** (line 292)
- **PAD_RXDLY_SEL** (line 324)
- **REQ_CMD_BUSY** (line 357)
- **REQ_CMD_EIO** (line 352)
- **REQ_CMD_TMO** (line 353)
- **REQ_DAT_ERR** (line 354)
- **REQ_STOP_EIO** (line 355)
- **REQ_STOP_TMO** (line 356)
- **SDC_ACMD_RESP** (line 72)
- **SDC_ADV_CFG0** (line 69)
- **SDC_ARG** (line 62)
- **SDC_BLK_NUM** (line 68)
- **SDC_CFG** (line 60)
- **SDC_CFG_BUSWIDTH** (line 199)
- **SDC_CFG_DTOC** (line 203)
- **SDC_CFG_INSWKUP** (line 197)
- **SDC_CFG_INTATGAP** (line 202)
- **SDC_CFG_SDIO** (line 200)
- **SDC_CFG_SDIOIDE** (line 201)
- **SDC_CFG_SDIOINTWKUP** (line 196)
- **SDC_CFG_WRDTOC** (line 198)
- **SDC_CMD** (line 61)
- **SDC_DAT1_IRQ_TRIGGER** (line 212)
- **SDC_FIFO_CFG** (line 89)
- **SDC_FIFO_CFG_RDVALIDSEL** (line 317)
- **SDC_FIFO_CFG_WRVALIDSEL** (line 316)
- **SDC_NEW_TX_EN** (line 214)
- **SDC_RESP0** (line 64)
- **SDC_RESP1** (line 65)
- **SDC_RESP2** (line 66)
- **SDC_RESP3** (line 67)
- **SDC_RX_ENHANCE_EN** (line 213)
- **SDC_RX_ENH_EN** (line 331)
- **SDC_STS** (line 63)
- **SDC_STS_CMDBUSY** (line 207)
- **SDC_STS_SDCBUSY** (line 206)
- **SDC_STS_SPM_RESOURCE_RELEASE** (line 208)
- **SDC_STS_SWR_COMPL** (line 209)
- **TEST_HS400_CMD_LOOP_MUX_SEL** (line 350)
- **TEST_LOOP_DSCLK_MUX_SEL** (line 347)
- **TEST_LOOP_LATCH_MUX_SEL** (line 348)
- **TUNING_REG2_FIXED_OFFEST** (line 369)
