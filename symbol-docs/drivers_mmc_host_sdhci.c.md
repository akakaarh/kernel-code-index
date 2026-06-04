# drivers/mmc/host/sdhci.c

Subsystem: drivers/mmc

## Functions (157)

### __sdhci_add_host
- Return type: int
- Signature: __sdhci_add_host(struct sdhci_host * host)
- Line: 4864

### __sdhci_adma_write_desc
- Return type: static void
- Signature: __sdhci_adma_write_desc(struct sdhci_host * host,void ** desc,dma_addr_t addr,int len,unsigned int cmd)
- Line: 735

### __sdhci_execute_tuning
- Return type: int
- Signature: __sdhci_execute_tuning(struct sdhci_host * host,u32 opcode)
- Line: 2871

### __sdhci_external_dma_prepare_data
- Return type: static void
- Signature: __sdhci_external_dma_prepare_data(struct sdhci_host * host,struct mmc_command * cmd)
- Line: 1326

### __sdhci_finish_data
- Return type: static void
- Signature: __sdhci_finish_data(struct sdhci_host * host,bool sw_data_timeout)
- Line: 1605

### __sdhci_finish_data_common
- Return type: void
- Signature: __sdhci_finish_data_common(struct sdhci_host * host,bool defer_reset)
- Line: 1566

### __sdhci_finish_mrq
- Return type: void
- Signature: __sdhci_finish_mrq(struct sdhci_host * host,struct mmc_request * mrq)
- Line: 1532

### __sdhci_led_activate
- Return type: static void
- Signature: __sdhci_led_activate(struct sdhci_host * host)
- Line: 406

### __sdhci_led_deactivate
- Return type: static void
- Signature: __sdhci_led_deactivate(struct sdhci_host * host)
- Line: 418

### __sdhci_read_caps
- Return type: void
- Signature: __sdhci_read_caps(struct sdhci_host * host,const u16 * ver,const u32 * caps,const u32 * caps1)
- Line: 4137

### __sdhci_set_timeout
- Return type: void
- Signature: __sdhci_set_timeout(struct sdhci_host * host,struct mmc_command * cmd)
- Line: 1057

### sdhci_abort_tuning
- Return type: void
- Signature: sdhci_abort_tuning(struct sdhci_host * host,u32 opcode)
- Line: 2797

### sdhci_ack_sdio_irq
- Return type: static void
- Signature: sdhci_ack_sdio_irq(struct mmc_host * mmc)
- Line: 2626

### sdhci_add_host
- Return type: int
- Signature: sdhci_add_host(struct sdhci_host * host)
- Line: 4933

### sdhci_adma_mark_end
- Return type: static void
- Signature: sdhci_adma_mark_end(void * desc)
- Line: 745

### sdhci_adma_show_error
- Return type: static void
- Signature: sdhci_adma_show_error(struct sdhci_host * host)
- Line: 3374

### sdhci_adma_table_post
- Return type: static void
- Signature: sdhci_adma_table_post(struct sdhci_host * host,struct mmc_data * data)
- Line: 844

### sdhci_adma_table_pre
- Return type: static void
- Signature: sdhci_adma_table_pre(struct sdhci_host * host,struct mmc_data * data,int sg_count)
- Line: 753

### sdhci_adma_write_desc
- Return type: void
- Signature: sdhci_adma_write_desc(struct sdhci_host * host,void ** desc,dma_addr_t addr,int len,unsigned int cmd)
- Line: 718

### sdhci_alloc_host
- Return type: sdhci_host *
- Signature: sdhci_alloc_host(struct device * dev,size_t priv_size)
- Line: 4062

### sdhci_allocate_bounce_buffer
- Return type: static void
- Signature: sdhci_allocate_bounce_buffer(struct sdhci_host * host)
- Line: 4189

### sdhci_auto_cmd12
- Return type: static bool
- Signature: sdhci_auto_cmd12(struct sdhci_host * host,struct mmc_request * mrq)
- Line: 1402

### sdhci_auto_cmd23
- Return type: static bool
- Signature: sdhci_auto_cmd23(struct sdhci_host * host,struct mmc_request * mrq)
- Line: 1409

### sdhci_auto_cmd_select
- Return type: static void
- Signature: sdhci_auto_cmd_select(struct sdhci_host * host,struct mmc_command * cmd,u16 * mode)
- Line: 1421

### sdhci_calc_clk
- Return type: u16
- Signature: sdhci_calc_clk(struct sdhci_host * host,unsigned int clock,unsigned int * actual_clock)
- Line: 1916

### sdhci_calc_sw_timeout
- Return type: static void
- Signature: sdhci_calc_sw_timeout(struct sdhci_host * host,struct mmc_command * cmd)
- Line: 936

### sdhci_calc_timeout
- Return type: static u8
- Signature: sdhci_calc_timeout(struct sdhci_host * host,struct mmc_command * cmd,bool * too_big)
- Line: 969

### sdhci_can_64bit_dma
- Return type: static bool
- Signature: sdhci_can_64bit_dma(struct sdhci_host * host)
- Line: 4260

### sdhci_card_busy
- Return type: static int
- Signature: sdhci_card_busy(struct mmc_host * mmc)
- Line: 2731

### sdhci_card_event
- Return type: static void
- Signature: sdhci_card_event(struct mmc_host * mmc)
- Line: 3050

### sdhci_cd_irq_can_wakeup
- Return type: static bool
- Signature: sdhci_cd_irq_can_wakeup(struct sdhci_host * host)
- Line: 3738

### sdhci_cleanup_host
- Return type: void
- Signature: sdhci_cleanup_host(struct sdhci_host * host)
- Line: 4844

### sdhci_cmd_irq
- Return type: static void
- Signature: sdhci_cmd_irq(struct sdhci_host * host,u32 intmask,u32 * intmask_p)
- Line: 3298

### sdhci_complete_work
- Return type: void
- Signature: sdhci_complete_work(struct work_struct * work)
- Line: 3228

### sdhci_config_dma
- Return type: static void
- Signature: sdhci_config_dma(struct sdhci_host * host)
- Line: 316

### sdhci_cqe_disable
- Return type: void
- Signature: sdhci_cqe_disable(struct mmc_host * mmc,bool recovery)
- Line: 3982

### sdhci_cqe_enable
- Return type: void
- Signature: sdhci_cqe_enable(struct mmc_host * mmc)
- Line: 3938

### sdhci_cqe_irq
- Return type: bool
- Signature: sdhci_cqe_irq(struct sdhci_host * host,u32 intmask,int * cmd_error,int * data_error)
- Line: 4004

### sdhci_data_irq
- Return type: static void
- Signature: sdhci_data_irq(struct sdhci_host * host,u32 intmask)
- Line: 3406

### sdhci_data_line_cmd
- Return type: bool
- Signature: sdhci_data_line_cmd(struct mmc_command * cmd)
- Line: 150

### sdhci_defer_done
- Return type: static bool
- Signature: sdhci_defer_done(struct sdhci_host * host,struct mmc_request * mrq)
- Line: 3546

### sdhci_del_timer
- Return type: static void
- Signature: sdhci_del_timer(struct sdhci_host * host,struct mmc_request * mrq)
- Line: 517

### sdhci_disable_card_detection
- Return type: static void
- Signature: sdhci_disable_card_detection(struct sdhci_host * host)
- Line: 183

### sdhci_disable_irq_wakeups
- Return type: void
- Signature: sdhci_disable_irq_wakeups(struct sdhci_host * host)
- Line: 3787

### sdhci_do_enable_v4_mode
- Return type: static void
- Signature: sdhci_do_enable_v4_mode(struct sdhci_host * host)
- Line: 127

### sdhci_do_reset
- Return type: bool
- Signature: sdhci_do_reset(struct sdhci_host * host,u8 mask)
- Line: 238

### sdhci_dumpregs
- Return type: void
- Signature: sdhci_dumpregs(struct sdhci_host * host)
- Line: 52

### sdhci_enable_card_detection
- Return type: static void
- Signature: sdhci_enable_card_detection(struct sdhci_host * host)
- Line: 178

### sdhci_enable_clk
- Return type: void
- Signature: sdhci_enable_clk(struct sdhci_host * host,u16 clk)
- Line: 2008

### sdhci_enable_irq_wakeups
- Return type: bool
- Signature: sdhci_enable_irq_wakeups(struct sdhci_host * host)
- Line: 3753

### sdhci_enable_preset_value
- Return type: void
- Signature: sdhci_enable_preset_value(struct sdhci_host * host,bool enable)
- Line: 2980

### sdhci_enable_sdio_irq
- Return type: void
- Signature: sdhci_enable_sdio_irq(struct mmc_host * mmc,int enable)
- Line: 2609

### sdhci_enable_sdio_irq_nolock
- Return type: static void
- Signature: sdhci_enable_sdio_irq_nolock(struct sdhci_host * host,int enable)
- Line: 2596

### sdhci_enable_v4_mode
- Return type: void
- Signature: sdhci_enable_v4_mode(struct sdhci_host * host)
- Line: 143

### sdhci_end_tuning
- Return type: void
- Signature: sdhci_end_tuning(struct sdhci_host * host)
- Line: 2779

### sdhci_error_out_mrqs
- Return type: static void
- Signature: sdhci_error_out_mrqs(struct sdhci_host * host,int err)
- Line: 3037

### sdhci_execute_tuning
- Return type: int
- Signature: sdhci_execute_tuning(struct mmc_host * mmc,u32 opcode)
- Line: 2911

### sdhci_external_dma_channel
- Return type: static dma_chan *
- Signature: sdhci_external_dma_channel(struct sdhci_host * host,struct mmc_data * data)
- Line: 1388

### sdhci_external_dma_channel
- Return type: static dma_chan *
- Signature: sdhci_external_dma_channel(struct sdhci_host * host,struct mmc_data * data)
- Line: 1250

### sdhci_external_dma_init
- Return type: static int
- Signature: sdhci_external_dma_init(struct sdhci_host * host)
- Line: 1367

### sdhci_external_dma_init
- Return type: static int
- Signature: sdhci_external_dma_init(struct sdhci_host * host)
- Line: 1220

### sdhci_external_dma_pre_transfer
- Return type: static void
- Signature: sdhci_external_dma_pre_transfer(struct sdhci_host * host,struct mmc_command * cmd)
- Line: 1383

### sdhci_external_dma_pre_transfer
- Return type: static void
- Signature: sdhci_external_dma_pre_transfer(struct sdhci_host * host,struct mmc_command * cmd)
- Line: 1352

### sdhci_external_dma_prepare_data
- Return type: static void
- Signature: sdhci_external_dma_prepare_data(struct sdhci_host * host,struct mmc_command * cmd)
- Line: 1376

### sdhci_external_dma_prepare_data
- Return type: static void
- Signature: sdhci_external_dma_prepare_data(struct sdhci_host * host,struct mmc_command * cmd)
- Line: 1339

### sdhci_external_dma_release
- Return type: static void
- Signature: sdhci_external_dma_release(struct sdhci_host * host)
- Line: 1372

### sdhci_external_dma_release
- Return type: static void
- Signature: sdhci_external_dma_release(struct sdhci_host * host)
- Line: 1311

### sdhci_external_dma_setup
- Return type: static int
- Signature: sdhci_external_dma_setup(struct sdhci_host * host,struct mmc_command * cmd)
- Line: 1256

### sdhci_finish_command
- Return type: static void
- Signature: sdhci_finish_command(struct sdhci_host * host)
- Line: 1818

### sdhci_finish_data
- Return type: static void
- Signature: sdhci_finish_data(struct sdhci_host * host)
- Line: 1648

### sdhci_finish_mrq
- Return type: void
- Signature: sdhci_finish_mrq(struct sdhci_host * host,struct mmc_request * mrq)
- Line: 1558

### sdhci_get_cd
- Return type: static int
- Signature: sdhci_get_cd(struct mmc_host * mmc)
- Line: 2513

### sdhci_get_cd_nogpio
- Return type: int
- Signature: sdhci_get_cd_nogpio(struct mmc_host * mmc)
- Line: 2540

### sdhci_get_preset_value
- Return type: static u16
- Signature: sdhci_get_preset_value(struct sdhci_host * host)
- Line: 1872

### sdhci_get_ro
- Return type: int
- Signature: sdhci_get_ro(struct mmc_host * mmc)
- Line: 2559

### sdhci_get_vdd_value
- Return type: unsigned short
- Signature: sdhci_get_vdd_value(unsigned short vdd)
- Line: 2091

### sdhci_has_requests
- Return type: static bool
- Signature: sdhci_has_requests(struct sdhci_host * host)
- Line: 525

### sdhci_hw_reset
- Return type: static void
- Signature: sdhci_hw_reset(struct mmc_host * mmc)
- Line: 2588

### sdhci_init
- Return type: static void
- Signature: sdhci_init(struct sdhci_host * host,int soft)
- Line: 362

### sdhci_initialize_data
- Return type: void
- Signature: sdhci_initialize_data(struct sdhci_host * host,struct mmc_data * data)
- Line: 1082

### sdhci_irq
- Return type: static irqreturn_t
- Signature: sdhci_irq(int irq,void * dev_id)
- Line: 3556

### sdhci_kmap_atomic
- Return type: static char *
- Signature: sdhci_kmap_atomic(struct scatterlist * sg)
- Line: 708

### sdhci_kunmap_atomic
- Return type: static void
- Signature: sdhci_kunmap_atomic(void * buffer)
- Line: 713

### sdhci_led_activate
- Return type: static void
- Signature: sdhci_led_activate(struct sdhci_host * host)
- Line: 476

### sdhci_led_activate
- Return type: static void
- Signature: sdhci_led_activate(struct sdhci_host * host)
- Line: 495

### sdhci_led_control
- Return type: static void
- Signature: sdhci_led_control(struct led_classdev * led,enum led_brightness brightness)
- Line: 431

### sdhci_led_deactivate
- Return type: static void
- Signature: sdhci_led_deactivate(struct sdhci_host * host)
- Line: 480

### sdhci_led_deactivate
- Return type: static void
- Signature: sdhci_led_deactivate(struct sdhci_host * host)
- Line: 500

### sdhci_led_register
- Return type: static int
- Signature: sdhci_led_register(struct sdhci_host * host)
- Line: 486

### sdhci_led_register
- Return type: static int
- Signature: sdhci_led_register(struct sdhci_host * host)
- Line: 450

### sdhci_led_unregister
- Return type: static void
- Signature: sdhci_led_unregister(struct sdhci_host * host)
- Line: 491

### sdhci_led_unregister
- Return type: static void
- Signature: sdhci_led_unregister(struct sdhci_host * host)
- Line: 468

### sdhci_manual_cmd23
- Return type: static bool
- Signature: sdhci_manual_cmd23(struct sdhci_host * host,struct mmc_request * mrq)
- Line: 1415

### sdhci_mod_timer
- Return type: void
- Signature: sdhci_mod_timer(struct sdhci_host * host,struct mmc_request * mrq,unsigned long timeout)
- Line: 507

### sdhci_needs_reset
- Return type: bool
- Signature: sdhci_needs_reset(struct sdhci_host * host,struct mmc_request * mrq)
- Line: 1501

### sdhci_post_req
- Return type: static void
- Signature: sdhci_post_req(struct mmc_host * mmc,struct mmc_request * mrq,int err)
- Line: 3010

### sdhci_pre_dma_transfer
- Return type: static int
- Signature: sdhci_pre_dma_transfer(struct sdhci_host * host,struct mmc_data * data,int cookie)
- Line: 653

### sdhci_pre_req
- Return type: static void
- Signature: sdhci_pre_req(struct mmc_host * mmc,struct mmc_request * mrq)
- Line: 3022

### sdhci_prepare_data
- Return type: static void
- Signature: sdhci_prepare_data(struct sdhci_host * host,struct mmc_command * cmd)
- Line: 1207

### sdhci_prepare_dma
- Return type: void
- Signature: sdhci_prepare_dma(struct sdhci_host * host,struct mmc_data * data)
- Line: 1118

### sdhci_prepare_hs400_tuning
- Return type: static int
- Signature: sdhci_prepare_hs400_tuning(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 2742

### sdhci_present_error
- Return type: bool
- Signature: sdhci_present_error(struct sdhci_host * host,struct mmc_command * cmd,bool present)
- Line: 1744

### sdhci_preset_needed
- Return type: static bool
- Signature: sdhci_preset_needed(struct sdhci_host * host,unsigned char timing)
- Line: 2336

### sdhci_presetable_values_change
- Return type: static bool
- Signature: sdhci_presetable_values_change(struct sdhci_host * host,struct mmc_ios * ios)
- Line: 2342

### sdhci_read_block_pio
- Return type: static void
- Signature: sdhci_read_block_pio(struct sdhci_host * host)
- Line: 536

### sdhci_read_rsp_136
- Return type: static void
- Signature: sdhci_read_rsp_136(struct sdhci_host * host,struct mmc_command * cmd)
- Line: 1798

### sdhci_reinit
- Return type: static void
- Signature: sdhci_reinit(struct sdhci_host * host)
- Line: 389

### sdhci_remove_host
- Return type: void
- Signature: sdhci_remove_host(struct sdhci_host * host,int dead)
- Line: 4954

### sdhci_request
- Return type: void
- Signature: sdhci_request(struct mmc_host * mmc,struct mmc_request * mrq)
- Line: 2211

### sdhci_request_atomic
- Return type: int
- Signature: sdhci_request_atomic(struct mmc_host * mmc,struct mmc_request * mrq)
- Line: 2243

### sdhci_request_done
- Return type: static bool
- Signature: sdhci_request_done(struct sdhci_host * host)
- Line: 3149

### sdhci_request_done_dma
- Return type: void
- Signature: sdhci_request_done_dma(struct sdhci_host * host,struct mmc_request * mrq)
- Line: 3102

### sdhci_reset
- Return type: void
- Signature: sdhci_reset(struct sdhci_host * host,u8 mask)
- Line: 204

### sdhci_reset_for_all
- Return type: static void
- Signature: sdhci_reset_for_all(struct sdhci_host * host)
- Line: 253

### sdhci_reset_for_reason
- Return type: static void
- Signature: sdhci_reset_for_reason(struct sdhci_host * host,enum sdhci_reset_reason reason)
- Line: 274

### sdhci_reset_tuning
- Return type: void
- Signature: sdhci_reset_tuning(struct sdhci_host * host)
- Line: 2786

### sdhci_resume_host
- Return type: int
- Signature: sdhci_resume_host(struct sdhci_host * host)
- Line: 3822

### sdhci_runtime_pm_bus_off
- Return type: static void
- Signature: sdhci_runtime_pm_bus_off(struct sdhci_host * host)
- Line: 196

### sdhci_runtime_pm_bus_on
- Return type: static void
- Signature: sdhci_runtime_pm_bus_on(struct sdhci_host * host)
- Line: 188

### sdhci_runtime_resume_host
- Return type: void
- Signature: sdhci_runtime_resume_host(struct sdhci_host * host,int soft_reset)
- Line: 3881

### sdhci_runtime_suspend_host
- Return type: void
- Signature: sdhci_runtime_suspend_host(struct sdhci_host * host)
- Line: 3861

### sdhci_sdma_address
- Return type: static dma_addr_t
- Signature: sdhci_sdma_address(struct sdhci_host * host)
- Line: 891

### sdhci_send_command
- Return type: static bool
- Signature: sdhci_send_command(struct sdhci_host * host,struct mmc_command * cmd)
- Line: 1653

### sdhci_send_command_retry
- Return type: static bool
- Signature: sdhci_send_command_retry(struct sdhci_host * host,struct mmc_command * cmd,unsigned long flags)
- Line: 1756

### sdhci_send_tuning
- Return type: void
- Signature: sdhci_send_tuning(struct sdhci_host * host,u32 opcode)
- Line: 2816

### sdhci_set_adma_addr
- Return type: static void
- Signature: sdhci_set_adma_addr(struct sdhci_host * host,dma_addr_t addr)
- Line: 884

### sdhci_set_block_info
- Return type: static void
- Signature: sdhci_set_block_info(struct sdhci_host * host,struct mmc_data * data)
- Line: 1097

### sdhci_set_bus_width
- Return type: void
- Signature: sdhci_set_bus_width(struct sdhci_host * host,int width)
- Line: 2277

### sdhci_set_card_detection
- Return type: static void
- Signature: sdhci_set_card_detection(struct sdhci_host * host,bool enable)
- Line: 156

### sdhci_set_clock
- Return type: void
- Signature: sdhci_set_clock(struct sdhci_host * host,unsigned int clock)
- Line: 2062

### sdhci_set_data_timeout_irq
- Return type: void
- Signature: sdhci_set_data_timeout_irq(struct sdhci_host * host,bool enable)
- Line: 1046

### sdhci_set_default_irqs
- Return type: static void
- Signature: sdhci_set_default_irqs(struct sdhci_host * host)
- Line: 300

### sdhci_set_dma_mask
- Return type: static int
- Signature: sdhci_set_dma_mask(struct sdhci_host * host)
- Line: 4107

### sdhci_set_ios
- Return type: void
- Signature: sdhci_set_ios(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 2373

### sdhci_set_ios_common
- Return type: void
- Signature: sdhci_set_ios_common(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 2353

### sdhci_set_mrq_done
- Return type: static void
- Signature: sdhci_set_mrq_done(struct sdhci_host * host,struct mmc_request * mrq)
- Line: 1511

### sdhci_set_power
- Return type: void
- Signature: sdhci_set_power(struct sdhci_host * host,unsigned char mode,unsigned short vdd)
- Line: 2176

### sdhci_set_power_and_bus_voltage
- Return type: void
- Signature: sdhci_set_power_and_bus_voltage(struct sdhci_host * host,unsigned char mode,unsigned short vdd)
- Line: 2192

### sdhci_set_power_noreg
- Return type: void
- Signature: sdhci_set_power_noreg(struct sdhci_host * host,unsigned char mode,unsigned short vdd)
- Line: 2121

### sdhci_set_power_reg
- Return type: static void
- Signature: sdhci_set_power_reg(struct sdhci_host * host,unsigned char mode,unsigned short vdd)
- Line: 2078

### sdhci_set_sdma_addr
- Return type: static void
- Signature: sdhci_set_sdma_addr(struct sdhci_host * host,dma_addr_t addr)
- Line: 899

### sdhci_set_timeout
- Return type: static void
- Signature: sdhci_set_timeout(struct sdhci_host * host,struct mmc_command * cmd)
- Line: 1074

### sdhci_set_transfer_irqs
- Return type: static void
- Signature: sdhci_set_transfer_irqs(struct sdhci_host * host)
- Line: 1027

### sdhci_set_transfer_mode
- Return type: static void
- Signature: sdhci_set_transfer_mode(struct sdhci_host * host,struct mmc_command * cmd)
- Line: 1460

### sdhci_set_uhs_signaling
- Return type: void
- Signature: sdhci_set_uhs_signaling(struct sdhci_host * host,unsigned timing)
- Line: 2297

### sdhci_setup_host
- Return type: int
- Signature: sdhci_setup_host(struct sdhci_host * host)
- Line: 4273

### sdhci_start_signal_voltage_switch
- Return type: int
- Signature: sdhci_start_signal_voltage_switch(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 2636

### sdhci_start_tuning
- Return type: void
- Signature: sdhci_start_tuning(struct sdhci_host * host)
- Line: 2754

### sdhci_suspend_host
- Return type: int
- Signature: sdhci_suspend_host(struct sdhci_host * host)
- Line: 3803

### sdhci_switch_external_dma
- Return type: void
- Signature: sdhci_switch_external_dma(struct sdhci_host * host,bool en)
- Line: 1396

### sdhci_target_timeout
- Return type: static unsigned int
- Signature: sdhci_target_timeout(struct sdhci_host * host,struct mmc_command * cmd,struct mmc_data * data)
- Line: 907

### sdhci_thread_irq
- Return type: irqreturn_t
- Signature: sdhci_thread_irq(int irq,void * dev_id)
- Line: 3698

### sdhci_timeout_data_timer
- Return type: static void
- Signature: sdhci_timeout_data_timer(struct timer_list * t)
- Line: 3260

### sdhci_timeout_timer
- Return type: static void
- Signature: sdhci_timeout_timer(struct timer_list * t)
- Line: 3238

### sdhci_timing_has_preset
- Return type: static bool
- Signature: sdhci_timing_has_preset(unsigned char timing)
- Line: 2322

### sdhci_transfer_pio
- Return type: static void
- Signature: sdhci_transfer_pio(struct sdhci_host * host)
- Line: 615

### sdhci_write_block_pio
- Return type: static void
- Signature: sdhci_write_block_pio(struct sdhci_host * host)
- Line: 575

## Enums (1)

### sdhci_reset_reason
- Line: 265

## Variables (3)

- static **debug_quirks** : unsigned int (line 47)
- static **debug_quirks2** : unsigned int (line 48)
- static **sdhci_ops** : const struct mmc_host_ops (line 3079)

## Macros (5)

- **DBG**(f,x...) (line 39)
- **DRIVER_NAME** (line 37)
- **MAX_TUNING_LOOP** (line 45)
- **SDHCI_DUMP**(f,x...) (line 42)
- **sdhci_reset_for**(h,r) (line 298)
