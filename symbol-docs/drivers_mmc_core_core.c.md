# drivers/mmc/core/core.c

Subsystem: drivers/mmc

## Functions (87)

### __mmc_claim_host
- Return type: int
- Signature: __mmc_claim_host(struct mmc_host * host,struct mmc_ctx * ctx,atomic_t * abort)
- Line: 791

### __mmc_start_req
- Return type: static int
- Signature: __mmc_start_req(struct mmc_host * host,struct mmc_request * mrq)
- Line: 384

### __mmc_start_request
- Return type: static void
- Signature: __mmc_start_request(struct mmc_host * host,struct mmc_request * mrq)
- Line: 216

### __mmc_stop_host
- Return type: void
- Signature: __mmc_stop_host(struct mmc_host * host)
- Line: 2357

### _mmc_detect_card_removed
- Return type: int
- Signature: _mmc_detect_card_removed(struct mmc_host * host)
- Line: 2150

### _mmc_detect_change
- Return type: void
- Signature: _mmc_detect_change(struct mmc_host * host,unsigned long delay,bool cd_irq)
- Line: 1442

### is_trim_arg
- Return type: static bool
- Signature: is_trim_arg(unsigned int arg)
- Line: 1520

### mmc_align_erase_size
- Return type: static unsigned int
- Signature: mmc_align_erase_size(struct mmc_card * card,sector_t * from,sector_t * to,unsigned int nr)
- Line: 1743

### mmc_attach_bus
- Return type: void
- Signature: mmc_attach_bus(struct mmc_host * host,const struct mmc_bus_ops * ops)
- Line: 1429

### mmc_calc_max_discard
- Return type: unsigned int
- Signature: mmc_calc_max_discard(struct mmc_card * card)
- Line: 2000

### mmc_card_alternative_gpt_sector
- Return type: int
- Signature: mmc_card_alternative_gpt_sector(struct mmc_card * card,sector_t * gpt_sector)
- Line: 2217

### mmc_card_can_cmd23
- Return type: bool
- Signature: mmc_card_can_cmd23(struct mmc_card * card)
- Line: 1902

### mmc_card_can_discard
- Return type: bool
- Signature: mmc_card_can_discard(struct mmc_card * card)
- Line: 1876

### mmc_card_can_erase
- Return type: bool
- Signature: mmc_card_can_erase(struct mmc_card * card)
- Line: 1863

### mmc_card_can_sanitize
- Return type: bool
- Signature: mmc_card_can_sanitize(struct mmc_card * card)
- Line: 1886

### mmc_card_can_secure_erase_trim
- Return type: bool
- Signature: mmc_card_can_secure_erase_trim(struct mmc_card * card)
- Line: 1895

### mmc_card_can_trim
- Return type: bool
- Signature: mmc_card_can_trim(struct mmc_card * card)
- Line: 1869

### mmc_card_is_blockaddr
- Return type: bool
- Signature: mmc_card_is_blockaddr(struct mmc_card * card)
- Line: 2028

### mmc_command_done
- Return type: void
- Signature: mmc_command_done(struct mmc_host * host,struct mmc_request * mrq)
- Line: 119

### mmc_complete_cmd
- Return type: static void
- Signature: mmc_complete_cmd(struct mmc_request * mrq)
- Line: 113

### mmc_cqe_post_req
- Return type: void
- Signature: mmc_cqe_post_req(struct mmc_host * host,struct mmc_request * mrq)
- Line: 524

### mmc_cqe_recovery
- Return type: int
- Signature: mmc_cqe_recovery(struct mmc_host * host)
- Line: 543

### mmc_cqe_request_done
- Return type: void
- Signature: mmc_cqe_request_done(struct mmc_host * host,struct mmc_request * mrq)
- Line: 490

### mmc_cqe_start_req
- Return type: int
- Signature: mmc_cqe_start_req(struct mmc_host * host,struct mmc_request * mrq)
- Line: 437

### mmc_ctx_matches
- Return type: static bool
- Signature: mmc_ctx_matches(struct mmc_host * host,struct mmc_ctx * ctx,struct task_struct * task)
- Line: 758

### mmc_ctx_set_claimer
- Return type: static void
- Signature: mmc_ctx_set_claimer(struct mmc_host * host,struct mmc_ctx * ctx,struct task_struct * task)
- Line: 765

### mmc_detach_bus
- Return type: void
- Signature: mmc_detach_bus(struct mmc_host * host)
- Line: 1437

### mmc_detect_card_removed
- Return type: int
- Signature: mmc_detect_card_removed(struct mmc_host * host)
- Line: 2179

### mmc_detect_change
- Return type: void
- Signature: mmc_detect_change(struct mmc_host * host,unsigned long delay)
- Line: 1466

### mmc_do_calc_max_discard
- Return type: static unsigned int
- Signature: mmc_do_calc_max_discard(struct mmc_card * card,unsigned int arg)
- Line: 1922

### mmc_do_erase
- Return type: static int
- Signature: mmc_do_erase(struct mmc_card * card,sector_t from,sector_t to,unsigned int arg)
- Line: 1630

### mmc_erase
- Return type: int
- Signature: mmc_erase(struct mmc_card * card,sector_t from,unsigned int nr,unsigned int arg)
- Line: 1801

### mmc_erase_group_aligned
- Return type: int
- Signature: mmc_erase_group_aligned(struct mmc_card * card,sector_t from,unsigned int nr)
- Line: 1911

### mmc_erase_timeout
- Return type: static unsigned int
- Signature: mmc_erase_timeout(struct mmc_card * card,unsigned int arg,unsigned int qty)
- Line: 1620

### mmc_execute_tuning
- Return type: int
- Signature: mmc_execute_tuning(struct mmc_card * card)
- Line: 931

### mmc_exit
- Return type: static void __exit
- Signature: mmc_exit(void)
- Line: 2418

### mmc_get_card
- Return type: void
- Signature: mmc_get_card(struct mmc_card * card,struct mmc_ctx * ctx)
- Line: 868

### mmc_handle_undervoltage
- Return type: int
- Signature: mmc_handle_undervoltage(struct mmc_host * host)
- Line: 1411

### mmc_host_set_uhs_voltage
- Return type: int
- Signature: mmc_host_set_uhs_voltage(struct mmc_host * host)
- Line: 1188

### mmc_hw_reset
- Return type: int
- Signature: mmc_hw_reset(struct mmc_card * card)
- Line: 2068

### mmc_hw_reset_for_init
- Return type: static void
- Signature: mmc_hw_reset_for_init(struct mmc_host * host)
- Line: 2049

### mmc_init
- Return type: static int __init
- Signature: mmc_init(void)
- Line: 2393

### mmc_init_erase
- Return type: void
- Signature: mmc_init_erase(struct mmc_card * card)
- Line: 1472

### mmc_is_req_done
- Return type: bool
- Signature: mmc_is_req_done(struct mmc_host * host,struct mmc_request * mrq)
- Line: 596

### mmc_mmc_erase_timeout
- Return type: static unsigned int
- Signature: mmc_mmc_erase_timeout(struct mmc_card * card,unsigned int arg,unsigned int qty)
- Line: 1525

### mmc_mrq_pr_debug
- Return type: static void
- Signature: mmc_mrq_pr_debug(struct mmc_host * host,struct mmc_request * mrq,bool cqe)
- Line: 264

### mmc_mrq_prep
- Return type: static int
- Signature: mmc_mrq_prep(struct mmc_host * host,struct mmc_request * mrq)
- Line: 298

### mmc_of_find_child_device
- Return type: device_node *
- Signature: mmc_of_find_child_device(struct mmc_host * host,unsigned func_num)
- Line: 1101

### mmc_of_get_func_num
- Return type: static int
- Signature: mmc_of_get_func_num(struct device_node * node)
- Line: 1089

### mmc_power_cycle
- Return type: void
- Signature: mmc_power_cycle(struct mmc_host * host,u32 ocr)
- Line: 1394

### mmc_power_off
- Return type: void
- Signature: mmc_power_off(struct mmc_host * host)
- Line: 1372

### mmc_power_up
- Return type: void
- Signature: mmc_power_up(struct mmc_host * host,u32 ocr)
- Line: 1338

### mmc_put_card
- Return type: void
- Signature: mmc_put_card(struct mmc_card * card,struct mmc_ctx * ctx)
- Line: 879

### mmc_release_host
- Return type: void
- Signature: mmc_release_host(struct mmc_host * host)
- Line: 839

### mmc_request_done
- Return type: void
- Signature: mmc_request_done(struct mmc_host * host,struct mmc_request * mrq)
- Line: 139

### mmc_rescan
- Return type: void
- Signature: mmc_rescan(struct work_struct * work)
- Line: 2252

### mmc_rescan_try_freq
- Return type: static int
- Signature: mmc_rescan_try_freq(struct mmc_host * host,unsigned freq)
- Line: 2099

### mmc_schedule_delayed_work
- Return type: static int
- Signature: mmc_schedule_delayed_work(struct delayed_work * work,unsigned long delay)
- Line: 63

### mmc_sd_erase_timeout
- Return type: static unsigned int
- Signature: mmc_sd_erase_timeout(struct mmc_card * card,unsigned int arg,unsigned int qty)
- Line: 1589

### mmc_select_drive_strength
- Return type: int
- Signature: mmc_select_drive_strength(struct mmc_card * card,unsigned int max_dtr,int card_drv_type,int * drv_type)
- Line: 1294

### mmc_select_voltage
- Return type: u32
- Signature: mmc_select_voltage(struct mmc_host * host,u32 ocr)
- Line: 1121

### mmc_set_blocklen
- Return type: int
- Signature: mmc_set_blocklen(struct mmc_card * card,unsigned int blocklen)
- Line: 2034

### mmc_set_bus_mode
- Return type: void
- Signature: mmc_set_bus_mode(struct mmc_host * host,unsigned int mode)
- Line: 968

### mmc_set_bus_width
- Return type: void
- Signature: mmc_set_bus_width(struct mmc_host * host,unsigned int width)
- Line: 977

### mmc_set_chip_select
- Return type: void
- Signature: mmc_set_chip_select(struct mmc_host * host,int mode)
- Line: 910

### mmc_set_clock
- Return type: void
- Signature: mmc_set_clock(struct mmc_host * host,unsigned int hz)
- Line: 920

### mmc_set_data_timeout
- Return type: void
- Signature: mmc_set_data_timeout(struct mmc_data * data,const struct mmc_card * card)
- Line: 660

### mmc_set_driver_type
- Return type: void
- Signature: mmc_set_driver_type(struct mmc_host * host,unsigned int drv_type)
- Line: 1288

### mmc_set_initial_signal_voltage
- Return type: void
- Signature: mmc_set_initial_signal_voltage(struct mmc_host * host)
- Line: 1177

### mmc_set_initial_state
- Return type: void
- Signature: mmc_set_initial_state(struct mmc_host * host)
- Line: 986

### mmc_set_ios
- Return type: static void
- Signature: mmc_set_ios(struct mmc_host * host)
- Line: 894

### mmc_set_signal_voltage
- Return type: int
- Signature: mmc_set_signal_voltage(struct mmc_host * host,int signal_voltage)
- Line: 1161

### mmc_set_timing
- Return type: void
- Signature: mmc_set_timing(struct mmc_host * host,unsigned int timing)
- Line: 1279

### mmc_set_uhs_voltage
- Return type: int
- Signature: mmc_set_uhs_voltage(struct mmc_host * host,u32 ocr)
- Line: 1211

### mmc_should_fail_request
- Return type: static void
- Signature: mmc_should_fail_request(struct mmc_host * host,struct mmc_request * mrq)
- Line: 106

### mmc_should_fail_request
- Return type: static void
- Signature: mmc_should_fail_request(struct mmc_host * host,struct mmc_request * mrq)
- Line: 81

### mmc_start_host
- Return type: void
- Signature: mmc_start_host(struct mmc_host * host)
- Line: 2339

### mmc_start_request
- Return type: int
- Signature: mmc_start_request(struct mmc_host * host,struct mmc_request * mrq)
- Line: 335

### mmc_stop_host
- Return type: void
- Signature: mmc_stop_host(struct mmc_host * host)
- Line: 2371

### mmc_sw_reset
- Return type: int
- Signature: mmc_sw_reset(struct mmc_card * card)
- Line: 2082

### mmc_vdd_to_ocrbitnum
- Return type: static int
- Signature: mmc_vdd_to_ocrbitnum(int vdd,bool low_bits)
- Line: 1031

### mmc_vddrange_to_ocrmask
- Return type: u32
- Signature: mmc_vddrange_to_ocrmask(int vdd_min,int vdd_max)
- Line: 1065

### mmc_wait_done
- Return type: static void
- Signature: mmc_wait_done(struct mmc_request * mrq)
- Line: 367

### mmc_wait_for_cmd
- Return type: int
- Signature: mmc_wait_for_cmd(struct mmc_host * host,struct mmc_command * cmd,int retries)
- Line: 633

### mmc_wait_for_req
- Return type: void
- Signature: mmc_wait_for_req(struct mmc_host * host,struct mmc_request * mrq)
- Line: 614

### mmc_wait_for_req_done
- Return type: void
- Signature: mmc_wait_for_req_done(struct mmc_host * host,struct mmc_request * mrq)
- Line: 403

### mmc_wait_ongoing_tfr_cmd
- Return type: static void
- Signature: mmc_wait_ongoing_tfr_cmd(struct mmc_host * host)
- Line: 372

## Variables (2)

- static **freqs** : const unsigned[] (line 53)
- **use_spi_crc** : bool (line 60)

## Macros (4)

- **CREATE_TRACE_POINTS** (line 34)
- **MMC_CQE_RECOVERY_TIMEOUT** (line 532)
- **MMC_ERASE_TIMEOUT_MS** (line 50)
- **SD_DISCARD_TIMEOUT_MS** (line 51)
