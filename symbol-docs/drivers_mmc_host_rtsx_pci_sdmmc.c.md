# drivers/mmc/host/rtsx_pci_sdmmc.c

Subsystem: drivers/mmc

## Functions (50)

### dump_reg_range
- Return type: static void
- Signature: dump_reg_range(struct realtek_pci_sdmmc * host,u16 start,u16 end)
- Line: 63

### init_extra_caps
- Return type: static void
- Signature: init_extra_caps(struct realtek_pci_sdmmc * host)
- Line: 1390

### realtek_init_host
- Return type: static void
- Signature: realtek_init_host(struct realtek_pci_sdmmc * host)
- Line: 1413

### rtsx_pci_sdmmc_card_event
- Return type: static void
- Signature: rtsx_pci_sdmmc_card_event(struct platform_device * pdev)
- Line: 1441

### rtsx_pci_sdmmc_drv_probe
- Return type: static int
- Signature: rtsx_pci_sdmmc_drv_probe(struct platform_device * pdev)
- Line: 1449

### rtsx_pci_sdmmc_drv_remove
- Return type: static void
- Signature: rtsx_pci_sdmmc_drv_remove(struct platform_device * pdev)
- Line: 1503

### sd_change_phase
- Return type: static int
- Signature: sd_change_phase(struct realtek_pci_sdmmc * host,u8 sample_point,bool rx)
- Line: 614

### sd_clear_error
- Return type: static void
- Signature: sd_clear_error(struct realtek_pci_sdmmc * host)
- Line: 56

### sd_cmd_set_data_len
- Return type: static void
- Signature: sd_cmd_set_data_len(struct rtsx_pcr * pcr,u16 blocks,u16 blksz)
- Line: 103

### sd_cmd_set_sd_cmd
- Return type: static void
- Signature: sd_cmd_set_sd_cmd(struct rtsx_pcr * pcr,struct mmc_command * cmd)
- Line: 96

### sd_disable_initial_mode
- Return type: static void
- Signature: sd_disable_initial_mode(struct realtek_pci_sdmmc * host)
- Line: 547

### sd_enable_initial_mode
- Return type: static void
- Signature: sd_enable_initial_mode(struct realtek_pci_sdmmc * host)
- Line: 541

### sd_get_cd_int
- Return type: static int
- Signature: sd_get_cd_int(struct realtek_pci_sdmmc * host)
- Line: 91

### sd_get_phase_len
- Return type: static int
- Signature: sd_get_phase_len(u32 phase_map,unsigned int start_bit)
- Line: 647

### sd_normal_rw
- Return type: static void
- Signature: sd_normal_rw(struct realtek_pci_sdmmc * host,struct mmc_request * mrq)
- Line: 580

### sd_power_off
- Return type: static int
- Signature: sd_power_off(struct realtek_pci_sdmmc * host)
- Line: 978

### sd_power_on
- Return type: static int
- Signature: sd_power_on(struct realtek_pci_sdmmc * host,unsigned char power_mode)
- Line: 904

### sd_pre_dma_transfer
- Return type: static int
- Signature: sd_pre_dma_transfer(struct realtek_pci_sdmmc * host,struct mmc_data * data,bool pre)
- Line: 146

### sd_print_debug_regs
- Return type: static void
- Signature: sd_print_debug_regs(struct realtek_pci_sdmmc * host)
- Line: 82

### sd_read_data
- Return type: static int
- Signature: sd_read_data(struct realtek_pci_sdmmc * host,struct mmc_command * cmd,u16 byte_cnt,u8 * buf,int buf_len,int timeout)
- Line: 326

### sd_read_long_data
- Return type: static int
- Signature: sd_read_long_data(struct realtek_pci_sdmmc * host,struct mmc_request * mrq)
- Line: 426

### sd_request
- Return type: static void
- Signature: sd_request(struct work_struct * work)
- Line: 795

### sd_response_type
- Return type: static int
- Signature: sd_response_type(struct mmc_command * cmd)
- Line: 111

### sd_rw_cmd
- Return type: static int
- Signature: sd_rw_cmd(struct mmc_command * cmd)
- Line: 788

### sd_rw_multi
- Return type: static int
- Signature: sd_rw_multi(struct realtek_pci_sdmmc * host,struct mmc_request * mrq)
- Line: 553

### sd_search_final_phase
- Return type: static u8
- Signature: sd_search_final_phase(struct realtek_pci_sdmmc * host,u32 phase_map)
- Line: 658

### sd_send_cmd_get_rsp
- Return type: static void
- Signature: sd_send_cmd_get_rsp(struct realtek_pci_sdmmc * host,struct mmc_command * cmd)
- Line: 208

### sd_set_bus_width
- Return type: static int
- Signature: sd_set_bus_width(struct realtek_pci_sdmmc * host,unsigned char bus_width)
- Line: 887

### sd_set_power_mode
- Return type: static int
- Signature: sd_set_power_mode(struct realtek_pci_sdmmc * host,unsigned char power_mode)
- Line: 1001

### sd_set_timing
- Return type: static int
- Signature: sd_set_timing(struct realtek_pci_sdmmc * host,unsigned char timing)
- Line: 1014

### sd_status_index
- Return type: static int
- Signature: sd_status_index(int resp_type)
- Line: 129

### sd_tuning_phase
- Return type: static int
- Signature: sd_tuning_phase(struct realtek_pci_sdmmc * host,u8 opcode,u32 * phase_map)
- Line: 726

### sd_tuning_rx
- Return type: static int
- Signature: sd_tuning_rx(struct realtek_pci_sdmmc * host,u8 opcode)
- Line: 744

### sd_tuning_rx_cmd
- Return type: static int
- Signature: sd_tuning_rx_cmd(struct realtek_pci_sdmmc * host,u8 opcode,u8 sample_point)
- Line: 699

### sd_wait_data_idle
- Return type: static void
- Signature: sd_wait_data_idle(struct realtek_pci_sdmmc * host)
- Line: 685

### sd_write_data
- Return type: static int
- Signature: sd_write_data(struct realtek_pci_sdmmc * host,struct mmc_command * cmd,u16 byte_cnt,u8 * buf,int buf_len,int timeout)
- Line: 379

### sd_write_long_data
- Return type: static int
- Signature: sd_write_long_data(struct realtek_pci_sdmmc * host,struct mmc_request * mrq)
- Line: 484

### sdio_extblock_cmd
- Return type: static int
- Signature: sdio_extblock_cmd(struct mmc_command * cmd,struct mmc_data * data)
- Line: 782

### sdmmc_card_busy
- Return type: static int
- Signature: sdmmc_card_busy(struct mmc_host * mmc)
- Line: 1233

### sdmmc_dev
- Return type: static device *
- Signature: sdmmc_dev(struct realtek_pci_sdmmc * host)
- Line: 51

### sdmmc_execute_tuning
- Return type: static int
- Signature: sdmmc_execute_tuning(struct mmc_host * mmc,u32 opcode)
- Line: 1273

### sdmmc_get_cd
- Return type: static int
- Signature: sdmmc_get_cd(struct mmc_host * mmc)
- Line: 1159

### sdmmc_get_ro
- Return type: static int
- Signature: sdmmc_get_ro(struct mmc_host * mmc)
- Line: 1134

### sdmmc_init_sd_express
- Return type: static int
- Signature: sdmmc_init_sd_express(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 1324

### sdmmc_post_req
- Return type: static void
- Signature: sdmmc_post_req(struct mmc_host * mmc,struct mmc_request * mrq,int err)
- Line: 196

### sdmmc_pre_req
- Return type: static void
- Signature: sdmmc_pre_req(struct mmc_host * mmc,struct mmc_request * mrq)
- Line: 180

### sdmmc_request
- Return type: static void
- Signature: sdmmc_request(struct mmc_host * mmc,struct mmc_request * mrq)
- Line: 872

### sdmmc_set_ios
- Return type: static void
- Signature: sdmmc_set_ios(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 1086

### sdmmc_switch_voltage
- Return type: static int
- Signature: sdmmc_switch_voltage(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 1184

### test_phase_bit
- Return type: static u32
- Signature: test_phase_bit(u32 phase_map,unsigned int bit)
- Line: 641

## Structs (1)

### realtek_pci_sdmmc
- Line: 26
- Members:
  - pdev: platform_device *
  - pcr: rtsx_pcr *
  - mmc: mmc_host *
  - mrq: mmc_request *
  - work: work_struct
  - host_mutex: mutex
  - ssc_depth: u8
  - clock: unsigned int
  - vpclk: bool
  - double_clk: bool
  - eject: bool
  - initial_mode: bool
  - prev_power_state: int
  - sg_count: int
  - cookie: s32
  - cookie_sg_count: int
  - using_cookie: bool

## Variables (3)

- static **realtek_pci_sdmmc_ops** : const struct mmc_host_ops (line 1377)
- static **rtsx_pci_sdmmc_driver** : platform_driver (line 1552)
- static **rtsx_pci_sdmmc_ids** : const struct platform_device_id[] (line 1543)

## Macros (2)

- **SDMMC_WORKQ_NAME** (line 31)
- **sd_print_debug_regs**(host) (line 88)
