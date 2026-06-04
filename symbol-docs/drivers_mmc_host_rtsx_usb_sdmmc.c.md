# drivers/mmc/host/rtsx_usb_sdmmc.c

Subsystem: drivers/mmc

## Functions (41)

### get_phase_len
- Return type: static int
- Signature: get_phase_len(u32 phase_map,unsigned int idx)
- Line: 609

### get_phase_point
- Return type: static u32
- Signature: get_phase_point(u32 phase_map,unsigned int idx)
- Line: 603

### rtsx_usb_init_host
- Return type: static void
- Signature: rtsx_usb_init_host(struct rtsx_usb_sdmmc * host)
- Line: 1337

### rtsx_usb_led_control
- Return type: static void
- Signature: rtsx_usb_led_control(struct led_classdev * led,enum led_brightness brightness)
- Line: 1301

### rtsx_usb_sdmmc_drv_probe
- Return type: static int
- Signature: rtsx_usb_sdmmc_drv_probe(struct platform_device * pdev)
- Line: 1364

### rtsx_usb_sdmmc_drv_remove
- Return type: static void
- Signature: rtsx_usb_sdmmc_drv_remove(struct platform_device * pdev)
- Line: 1421

### rtsx_usb_sdmmc_runtime_resume
- Return type: static int
- Signature: rtsx_usb_sdmmc_runtime_resume(struct device * dev)
- Line: 1466

### rtsx_usb_sdmmc_runtime_suspend
- Return type: static int
- Signature: rtsx_usb_sdmmc_runtime_suspend(struct device * dev)
- Line: 1458

### rtsx_usb_update_led
- Return type: static void
- Signature: rtsx_usb_update_led(struct work_struct * work)
- Line: 1314

### sd_change_phase
- Return type: static int
- Signature: sd_change_phase(struct rtsx_usb_sdmmc * host,u8 sample_point,int tx)
- Line: 576

### sd_clear_error
- Return type: static void
- Signature: sd_clear_error(struct rtsx_usb_sdmmc * host)
- Line: 64

### sd_disable_initial_mode
- Return type: static void
- Signature: sd_disable_initial_mode(struct rtsx_usb_sdmmc * host)
- Line: 536

### sd_enable_initial_mode
- Return type: static void
- Signature: sd_enable_initial_mode(struct rtsx_usb_sdmmc * host)
- Line: 530

### sd_normal_rw
- Return type: static void
- Signature: sd_normal_rw(struct rtsx_usb_sdmmc * host,struct mmc_request * mrq)
- Line: 542

### sd_power_off
- Return type: static int
- Signature: sd_power_off(struct rtsx_usb_sdmmc * host)
- Line: 1015

### sd_power_on
- Return type: static int
- Signature: sd_power_on(struct rtsx_usb_sdmmc * host)
- Line: 962

### sd_print_debug_regs
- Return type: static void
- Signature: sd_print_debug_regs(struct rtsx_usb_sdmmc * host)
- Line: 76

### sd_pull_ctl_disable_lqfp48
- Return type: static int
- Signature: sd_pull_ctl_disable_lqfp48(struct rtsx_ucr * ucr)
- Line: 906

### sd_pull_ctl_disable_qfn24
- Return type: static int
- Signature: sd_pull_ctl_disable_qfn24(struct rtsx_ucr * ucr)
- Line: 920

### sd_pull_ctl_enable_lqfp48
- Return type: static int
- Signature: sd_pull_ctl_enable_lqfp48(struct rtsx_ucr * ucr)
- Line: 934

### sd_pull_ctl_enable_qfn24
- Return type: static int
- Signature: sd_pull_ctl_enable_qfn24(struct rtsx_ucr * ucr)
- Line: 948

### sd_read_data
- Return type: static int
- Signature: sd_read_data(struct rtsx_usb_sdmmc * host,struct mmc_command * cmd,u16 byte_cnt,u8 * buf,int buf_len,int timeout)
- Line: 92

### sd_rw_multi
- Return type: static int
- Signature: sd_rw_multi(struct rtsx_usb_sdmmc * host,struct mmc_request * mrq)
- Line: 446

### sd_search_final_phase
- Return type: static u8
- Signature: sd_search_final_phase(struct rtsx_usb_sdmmc * host,u32 phase_map)
- Line: 620

### sd_send_cmd_get_rsp
- Return type: static void
- Signature: sd_send_cmd_get_rsp(struct rtsx_usb_sdmmc * host,struct mmc_command * cmd)
- Line: 285

### sd_set_bus_width
- Return type: static int
- Signature: sd_set_bus_width(struct rtsx_usb_sdmmc * host,unsigned char bus_width)
- Line: 889

### sd_set_power_mode
- Return type: static void
- Signature: sd_set_power_mode(struct rtsx_usb_sdmmc * host,unsigned char power_mode)
- Line: 1039

### sd_set_timing
- Return type: static int
- Signature: sd_set_timing(struct rtsx_usb_sdmmc * host,unsigned char timing,bool * ddr_mode)
- Line: 1080

### sd_tuning_phase
- Return type: static void
- Signature: sd_tuning_phase(struct rtsx_usb_sdmmc * host,u8 opcode,u16 * phase_map)
- Line: 683

### sd_tuning_rx
- Return type: static int
- Signature: sd_tuning_rx(struct rtsx_usb_sdmmc * host,u8 opcode)
- Line: 699

### sd_tuning_rx_cmd
- Return type: static int
- Signature: sd_tuning_rx_cmd(struct rtsx_usb_sdmmc * host,u8 opcode,u8 sample_point)
- Line: 661

### sd_wait_data_idle
- Return type: static void
- Signature: sd_wait_data_idle(struct rtsx_usb_sdmmc * host)
- Line: 647

### sd_write_data
- Return type: static int
- Signature: sd_write_data(struct rtsx_usb_sdmmc * host,struct mmc_command * cmd,u16 byte_cnt,u8 * buf,int buf_len,int timeout)
- Line: 199

### sdmmc_card_busy
- Return type: static int
- Signature: sdmmc_card_busy(struct mmc_host * mmc)
- Line: 1231

### sdmmc_dev
- Return type: static device *
- Signature: sdmmc_dev(struct rtsx_usb_sdmmc * host)
- Line: 59

### sdmmc_execute_tuning
- Return type: static int
- Signature: sdmmc_execute_tuning(struct mmc_host * mmc,u32 opcode)
- Line: 1271

### sdmmc_get_cd
- Return type: static int
- Signature: sdmmc_get_cd(struct mmc_host * mmc)
- Line: 771

### sdmmc_get_ro
- Return type: static int
- Signature: sdmmc_get_ro(struct mmc_host * mmc)
- Line: 743

### sdmmc_request
- Return type: static void
- Signature: sdmmc_request(struct mmc_host * mmc,struct mmc_request * mrq)
- Line: 810

### sdmmc_set_ios
- Return type: static void
- Signature: sdmmc_set_ios(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 1141

### sdmmc_switch_voltage
- Return type: static int
- Signature: sdmmc_switch_voltage(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 1182

## Structs (1)

### rtsx_usb_sdmmc
- Line: 33
- Members:
  - pdev: platform_device *
  - ucr: rtsx_ucr *
  - mmc: mmc_host *
  - mrq: mmc_request *
  - host_mutex: mutex
  - ssc_depth: u8
  - clock: unsigned int
  - vpclk: bool
  - double_clk: bool
  - host_removal: bool
  - card_exist: bool
  - initial_mode: bool
  - ddr_mode: bool
  - power_mode: unsigned char
  - ocp_stat: u16
  - led: led_classdev
  - led_name: char[32]
  - led_work: work_struct

## Variables (4)

- static **rtsx_usb_sdmmc_dev_pm_ops** : const struct dev_pm_ops (line 1476)
- static **rtsx_usb_sdmmc_driver** : platform_driver (line 1489)
- static **rtsx_usb_sdmmc_ids** : const struct platform_device_id[] (line 1480)
- static **rtsx_usb_sdmmc_ops** : const struct mmc_host_ops (line 1290)

## Macros (2)

- **RTSX_USB_USE_LEDS_CLASS** (line 30)
- **sd_print_debug_regs**(host) (line 89)
