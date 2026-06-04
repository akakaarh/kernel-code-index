# drivers/mmc/host/cb710-mmc.c

Subsystem: drivers/mmc

## Functions (30)

### __cb710_mmc_enable_irq
- Return type: static void
- Signature: __cb710_mmc_enable_irq(struct cb710_slot * slot,unsigned short enable,unsigned short mask)
- Line: 63

### cb710_check_event
- Return type: static int
- Signature: cb710_check_event(struct cb710_slot * slot,u8 what)
- Line: 113

### cb710_encode_cmd_flags
- Return type: static u16
- Signature: cb710_encode_cmd_flags(struct cb710_mmc_reader * reader,struct mmc_command * cmd)
- Line: 345

### cb710_is_transfer_size_supported
- Return type: static bool
- Signature: cb710_is_transfer_size_supported(struct mmc_data * data)
- Line: 261

### cb710_mmc_command
- Return type: static int
- Signature: cb710_mmc_command(struct mmc_host * mmc,struct mmc_command * cmd)
- Line: 444

### cb710_mmc_enable_4bit_data
- Return type: static void
- Signature: cb710_mmc_enable_4bit_data(struct cb710_slot * slot,int enable)
- Line: 103

### cb710_mmc_enable_irq
- Return type: static void
- Signature: cb710_mmc_enable_irq(struct cb710_slot * slot,unsigned short enable,unsigned short mask)
- Line: 84

### cb710_mmc_exit
- Return type: static void
- Signature: cb710_mmc_exit(struct platform_device * pdev)
- Line: 748

### cb710_mmc_fifo_hack
- Return type: static void
- Signature: cb710_mmc_fifo_hack(struct cb710_slot * slot)
- Line: 222

### cb710_mmc_finish_request_bh_work
- Return type: static void
- Signature: cb710_mmc_finish_request_bh_work(struct work_struct * t)
- Line: 650

### cb710_mmc_get_cd
- Return type: static int
- Signature: cb710_mmc_get_cd(struct mmc_host * mmc)
- Line: 610

### cb710_mmc_get_ro
- Return type: static int
- Signature: cb710_mmc_get_ro(struct mmc_host * mmc)
- Line: 602

### cb710_mmc_init
- Return type: static int
- Signature: cb710_mmc_init(struct platform_device * pdev)
- Line: 687

### cb710_mmc_irq_handler
- Return type: static int
- Signature: cb710_mmc_irq_handler(struct cb710_slot * slot)
- Line: 618

### cb710_mmc_powerdown
- Return type: static void
- Signature: cb710_mmc_powerdown(struct cb710_slot * slot)
- Line: 555

### cb710_mmc_powerup
- Return type: static int
- Signature: cb710_mmc_powerup(struct cb710_slot * slot)
- Line: 500

### cb710_mmc_receive
- Return type: static int
- Signature: cb710_mmc_receive(struct cb710_slot * slot,struct mmc_data * data)
- Line: 266

### cb710_mmc_receive_pio
- Return type: static int
- Signature: cb710_mmc_receive_pio(struct cb710_slot * slot,struct sg_mapping_iter * miter,size_t dw_count)
- Line: 245

### cb710_mmc_request
- Return type: static void
- Signature: cb710_mmc_request(struct mmc_host * mmc,struct mmc_request * mrq)
- Line: 484

### cb710_mmc_reset_events
- Return type: static void
- Signature: cb710_mmc_reset_events(struct cb710_slot * slot)
- Line: 96

### cb710_mmc_resume
- Return type: static int
- Signature: cb710_mmc_resume(struct device * dev)
- Line: 676

### cb710_mmc_select_clock_divider
- Return type: static void
- Signature: cb710_mmc_select_clock_divider(struct mmc_host * mmc,int hz)
- Line: 28

### cb710_mmc_send
- Return type: static int
- Signature: cb710_mmc_send(struct cb710_slot * slot,struct mmc_data * data)
- Line: 310

### cb710_mmc_set_ios
- Return type: static void
- Signature: cb710_mmc_set_ios(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 561

### cb710_mmc_set_transfer_size
- Return type: static void
- Signature: cb710_mmc_set_transfer_size(struct cb710_slot * slot,size_t count,size_t blocksize)
- Line: 211

### cb710_mmc_suspend
- Return type: static int
- Signature: cb710_mmc_suspend(struct device * dev)
- Line: 667

### cb710_mmc_transfer_data
- Return type: static int
- Signature: cb710_mmc_transfer_data(struct cb710_slot * slot,struct mmc_data * data)
- Line: 425

### cb710_receive_response
- Return type: static void
- Signature: cb710_receive_response(struct cb710_slot * slot,struct mmc_command * cmd)
- Line: 396

### cb710_wait_for_event
- Return type: static int
- Signature: cb710_wait_for_event(struct cb710_slot * slot,u8 what)
- Line: 146

### cb710_wait_while_busy
- Return type: static int
- Signature: cb710_wait_while_busy(struct cb710_slot * slot,uint8_t mask)
- Line: 179

## Variables (4)

- static **cb710_clock_divider_log2** : const u8[8] (line 16)
- static **cb710_mmc_driver** : platform_driver (line 769)
- static **cb710_mmc_host** : const struct mmc_host_ops (line 660)
- static **cb710_src_freq_mhz** : const u8[16] (line 23)

## Macros (2)

- **CB710_MAX_DIVIDER_IDX** (line 20)
- **CB710_MMC_REQ_TIMEOUT_MS** (line 14)
