# drivers/mmc/host/sdhci-uhs2.c

Subsystem: drivers/mmc

## Functions (40)

### __sdhci_uhs2_add_host_v4
- Return type: static void
- Signature: __sdhci_uhs2_add_host_v4(struct sdhci_host * host,u32 caps1)
- Line: 1147

### __sdhci_uhs2_finish_command
- Return type: static void
- Signature: __sdhci_uhs2_finish_command(struct sdhci_host * host)
- Line: 773

### __sdhci_uhs2_irq
- Return type: static void
- Signature: __sdhci_uhs2_irq(struct sdhci_host * host,u32 uhs2mask)
- Line: 996

### __sdhci_uhs2_remove_host
- Return type: static void
- Signature: __sdhci_uhs2_remove_host(struct sdhci_host * host,int dead)
- Line: 1179

### __sdhci_uhs2_send_command
- Return type: static void
- Signature: __sdhci_uhs2_send_command(struct sdhci_host * host,struct mmc_command * cmd)
- Line: 635

### __sdhci_uhs2_set_ios
- Return type: static void
- Signature: __sdhci_uhs2_set_ios(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 256

### __sdhci_uhs2_set_timeout
- Return type: static void
- Signature: __sdhci_uhs2_set_timeout(struct sdhci_host * host)
- Line: 218

### mmc_opt_regulator_set_ocr
- Return type: static int
- Signature: mmc_opt_regulator_set_ocr(struct mmc_host * mmc,struct regulator * supply,unsigned short vdd_bit)
- Line: 76

### sdhci_calc_timeout_uhs2
- Return type: static u8
- Signature: sdhci_calc_timeout_uhs2(struct sdhci_host * host,u8 * cmd_res,u8 * dead_lock)
- Line: 165

### sdhci_uhs2_add_host
- Return type: int
- Signature: sdhci_uhs2_add_host(struct sdhci_host * host)
- Line: 1188

### sdhci_uhs2_check_dormant
- Return type: static int
- Signature: sdhci_uhs2_check_dormant(struct sdhci_host * host)
- Line: 501

### sdhci_uhs2_clear_set_irqs
- Return type: void
- Signature: sdhci_uhs2_clear_set_irqs(struct sdhci_host * host,u32 clear,u32 set)
- Line: 244

### sdhci_uhs2_complete_work
- Return type: static void
- Signature: sdhci_uhs2_complete_work(struct work_struct * work)
- Line: 976

### sdhci_uhs2_control
- Return type: static int
- Signature: sdhci_uhs2_control(struct mmc_host * mmc,enum sd_uhs2_operation op)
- Line: 515

### sdhci_uhs2_disable_clk
- Return type: static int
- Signature: sdhci_uhs2_disable_clk(struct mmc_host * mmc)
- Line: 443

### sdhci_uhs2_do_detect_init
- Return type: static int
- Signature: sdhci_uhs2_do_detect_init(struct mmc_host * mmc)
- Line: 411

### sdhci_uhs2_dump_regs
- Return type: void
- Signature: sdhci_uhs2_dump_regs(struct sdhci_host * host)
- Line: 37

### sdhci_uhs2_enable_clk
- Return type: static int
- Signature: sdhci_uhs2_enable_clk(struct mmc_host * mmc)
- Line: 454

### sdhci_uhs2_finish_command
- Return type: static void
- Signature: sdhci_uhs2_finish_command(struct sdhci_host * host)
- Line: 824

### sdhci_uhs2_finish_data
- Return type: static void
- Signature: sdhci_uhs2_finish_data(struct sdhci_host * host)
- Line: 576

### sdhci_uhs2_host_ops_init
- Return type: static int
- Signature: sdhci_uhs2_host_ops_init(struct sdhci_host * host)
- Line: 1133

### sdhci_uhs2_init
- Return type: static int
- Signature: sdhci_uhs2_init(struct sdhci_host * host)
- Line: 359

### sdhci_uhs2_interface_detect
- Return type: static int
- Signature: sdhci_uhs2_interface_detect(struct sdhci_host * host)
- Line: 332

### sdhci_uhs2_irq
- Return type: u32
- Signature: sdhci_uhs2_irq(struct sdhci_host * host,u32 intmask)
- Line: 1047

### sdhci_uhs2_needs_reset
- Return type: static bool
- Signature: sdhci_uhs2_needs_reset(struct sdhci_host * host,struct mmc_request * mrq)
- Line: 908

### sdhci_uhs2_prepare_data
- Return type: static void
- Signature: sdhci_uhs2_prepare_data(struct sdhci_host * host,struct mmc_command * cmd)
- Line: 564

### sdhci_uhs2_remove_host
- Return type: void
- Signature: sdhci_uhs2_remove_host(struct sdhci_host * host,int dead)
- Line: 1230

### sdhci_uhs2_request
- Return type: static void
- Signature: sdhci_uhs2_request(struct mmc_host * mmc,struct mmc_request * mrq)
- Line: 863

### sdhci_uhs2_request_done
- Return type: static bool
- Signature: sdhci_uhs2_request_done(struct sdhci_host * host)
- Line: 914

### sdhci_uhs2_reset
- Return type: void
- Signature: sdhci_uhs2_reset(struct sdhci_host * host,u16 mask)
- Line: 90

### sdhci_uhs2_reset_cmd_data
- Return type: static void
- Signature: sdhci_uhs2_reset_cmd_data(struct sdhci_host * host)
- Line: 110

### sdhci_uhs2_send_command
- Return type: static bool
- Signature: sdhci_uhs2_send_command(struct sdhci_host * host,struct mmc_command * cmd)
- Line: 687

### sdhci_uhs2_send_command_retry
- Return type: static bool
- Signature: sdhci_uhs2_send_command_retry(struct sdhci_host * host,struct mmc_command * cmd,unsigned long flags)
- Line: 732

### sdhci_uhs2_set_config
- Return type: static void
- Signature: sdhci_uhs2_set_config(struct sdhci_host * host)
- Line: 473

### sdhci_uhs2_set_ios
- Return type: static int
- Signature: sdhci_uhs2_set_ios(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 302

### sdhci_uhs2_set_power
- Return type: void
- Signature: sdhci_uhs2_set_power(struct sdhci_host * host,unsigned char mode,unsigned short vdd)
- Line: 123

### sdhci_uhs2_set_timeout
- Return type: void
- Signature: sdhci_uhs2_set_timeout(struct sdhci_host * host,struct mmc_command * cmd)
- Line: 227

### sdhci_uhs2_set_transfer_mode
- Return type: static void
- Signature: sdhci_uhs2_set_transfer_mode(struct sdhci_host * host,struct mmc_command * cmd)
- Line: 585

### sdhci_uhs2_thread_irq
- Return type: static irqreturn_t
- Signature: sdhci_uhs2_thread_irq(int irq,void * dev_id)
- Line: 1093

### uhs2_dev_cmd
- Return type: static u16
- Signature: uhs2_dev_cmd(struct mmc_command * cmd)
- Line: 71

## Macros (8)

- **DBG**(f,x...) (line 25)
- **DRIVER_NAME** (line 24)
- **SDHCI_UHS2_DUMP**(f,x...) (line 27)
- **UHS2_ARG_IOADR_MASK** (line 35)
- **UHS2_CHECK_DORMANT_TIMEOUT_100MS** (line 31)
- **UHS2_INTERFACE_DETECT_TIMEOUT_100MS** (line 32)
- **UHS2_LANE_SYNC_TIMEOUT_150MS** (line 33)
- **UHS2_RESET_TIMEOUT_100MS** (line 30)
