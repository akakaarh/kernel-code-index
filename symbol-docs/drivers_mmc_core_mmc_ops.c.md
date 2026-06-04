# drivers/mmc/core/mmc_ops.c

Subsystem: drivers/mmc

## Functions (41)

### __mmc_go_idle
- Return type: int
- Signature: __mmc_go_idle(struct mmc_host * host)
- Line: 147

### __mmc_poll_for_busy
- Return type: int
- Signature: __mmc_poll_for_busy(struct mmc_host * host,unsigned int period_us,unsigned int timeout_ms,int (* busy_cb)(void * cb_data,bool * busy),void * cb_data)
- Line: 510

### __mmc_send_op_cond_cb
- Return type: static int
- Signature: __mmc_send_op_cond_cb(void * cb_data,bool * busy)
- Line: 192

### __mmc_send_status
- Return type: int
- Signature: __mmc_send_status(struct mmc_card * card,u32 * status,unsigned int retries)
- Line: 69

### __mmc_switch
- Return type: int
- Signature: __mmc_switch(struct mmc_card * card,u8 set,u8 index,u8 value,unsigned int timeout_ms,unsigned char timing,bool send_status,bool retry_crc_err,unsigned int retries)
- Line: 603

### _mmc_select_card
- Return type: static int
- Signature: _mmc_select_card(struct mmc_host * host,struct mmc_card * card)
- Line: 99

### mmc_bus_test
- Return type: int
- Signature: mmc_bus_test(struct mmc_card * card,u8 bus_width)
- Line: 847

### mmc_busy_cb
- Return type: static int
- Signature: mmc_busy_cb(void * cb_data,bool * busy)
- Line: 468

### mmc_card_can_ext_csd
- Return type: bool
- Signature: mmc_card_can_ext_csd(struct mmc_card * card)
- Line: 947

### mmc_cmdq_disable
- Return type: int
- Signature: mmc_cmdq_disable(struct mmc_card * card)
- Line: 1038

### mmc_cmdq_enable
- Return type: int
- Signature: mmc_cmdq_enable(struct mmc_card * card)
- Line: 1032

### mmc_cmdq_switch
- Return type: static int
- Signature: mmc_cmdq_switch(struct mmc_card * card,bool enable)
- Line: 1016

### mmc_deselect_cards
- Return type: int
- Signature: mmc_deselect_cards(struct mmc_host * host)
- Line: 122

### mmc_get_ext_csd
- Return type: int
- Signature: mmc_get_ext_csd(struct mmc_card * card,u8 ** new_ext_csd)
- Line: 378

### mmc_go_idle
- Return type: int
- Signature: mmc_go_idle(struct mmc_host * host)
- Line: 162

### mmc_interrupt_hpi
- Return type: static int
- Signature: mmc_interrupt_hpi(struct mmc_card * card)
- Line: 906

### mmc_poll_for_busy
- Return type: int
- Signature: mmc_poll_for_busy(struct mmc_card * card,unsigned int timeout_ms,bool retry_crc_err,enum mmc_busy_cmd busy_cmd)
- Line: 552

### mmc_prepare_busy_cmd
- Return type: bool
- Signature: mmc_prepare_busy_cmd(struct mmc_host * host,struct mmc_command * cmd,unsigned int timeout_ms)
- Line: 566

### mmc_read_bkops_status
- Return type: static int
- Signature: mmc_read_bkops_status(struct mmc_card * card)
- Line: 952

### mmc_read_tuning
- Return type: int
- Signature: mmc_read_tuning(struct mmc_host * host,unsigned int blksz,unsigned int blocks)
- Line: 1097

### mmc_run_bkops
- Return type: void
- Signature: mmc_run_bkops(struct mmc_card * card)
- Line: 974

### mmc_sanitize
- Return type: int
- Signature: mmc_sanitize(struct mmc_card * card,unsigned int timeout_ms)
- Line: 1044

### mmc_select_card
- Return type: int
- Signature: mmc_select_card(struct mmc_card * card)
- Line: 116

### mmc_send_abort_tuning
- Return type: int
- Signature: mmc_send_abort_tuning(struct mmc_host * host,u32 opcode)
- Line: 745

### mmc_send_adtc_data
- Return type: int
- Signature: mmc_send_adtc_data(struct mmc_card * card,struct mmc_host * host,u32 opcode,u32 args,void * buf,unsigned len)
- Line: 291

### mmc_send_bus_test
- Return type: static int
- Signature: mmc_send_bus_test(struct mmc_card * card,struct mmc_host * host,u8 opcode,u8 len)
- Line: 771

### mmc_send_cid
- Return type: int
- Signature: mmc_send_cid(struct mmc_host * host,u32 * cid)
- Line: 370

### mmc_send_csd
- Return type: int
- Signature: mmc_send_csd(struct mmc_card * card,u32 * csd)
- Line: 361

### mmc_send_cxd_native
- Return type: static int
- Signature: mmc_send_cxd_native(struct mmc_host * host,u32 arg,u32 * cxd,int opcode)
- Line: 269

### mmc_send_hpi_cmd
- Return type: static int
- Signature: mmc_send_hpi_cmd(struct mmc_card * card)
- Line: 868

### mmc_send_op_cond
- Return type: int
- Signature: mmc_send_op_cond(struct mmc_host * host,u32 ocr,u32 * rocr)
- Line: 231

### mmc_send_status
- Return type: int
- Signature: mmc_send_status(struct mmc_card * card,u32 * status)
- Line: 93

### mmc_send_tuning
- Return type: int
- Signature: mmc_send_tuning(struct mmc_host * host,u32 opcode,int * cmd_error)
- Line: 676

### mmc_set_dsr
- Return type: int
- Signature: mmc_set_dsr(struct mmc_host * host)
- Line: 135

### mmc_set_relative_addr
- Return type: int
- Signature: mmc_set_relative_addr(struct mmc_card * card)
- Line: 257

### mmc_spi_read_ocr
- Return type: int
- Signature: mmc_spi_read_ocr(struct mmc_host * host,int highcap,u32 * ocrp)
- Line: 408

### mmc_spi_send_cxd
- Return type: static int
- Signature: mmc_spi_send_cxd(struct mmc_host * host,u32 * cxd,u32 opcode)
- Line: 340

### mmc_spi_set_crc
- Return type: int
- Signature: mmc_spi_set_crc(struct mmc_host * host,int use_crc)
- Line: 423

### mmc_switch
- Return type: int
- Signature: mmc_switch(struct mmc_card * card,u8 set,u8 index,u8 value,unsigned int timeout_ms)
- Line: 668

### mmc_switch_status
- Return type: int
- Signature: mmc_switch_status(struct mmc_card * card,bool crc_err_fatal)
- Line: 454

### mmc_switch_status_error
- Return type: static int
- Signature: mmc_switch_status_error(struct mmc_host * host,u32 status)
- Line: 438

## Structs (2)

### mmc_busy_data
- Line: 57
- Members:
  - card: mmc_card *
  - retry_crc_err: bool
  - busy_cmd: mmc_busy_cmd
  - host: mmc_host *
  - ocr: u32
  - cmd: mmc_command *

### mmc_op_cond_busy_data
- Line: 63
- Members:
  - card: mmc_card *
  - retry_crc_err: bool
  - busy_cmd: mmc_busy_cmd
  - host: mmc_host *
  - ocr: u32
  - cmd: mmc_command *

## Variables (2)

- static **tuning_blk_pattern_4bit** : const u8[] (line 27)
- static **tuning_blk_pattern_8bit** : const u8[] (line 38)

## Macros (4)

- **MMC_BKOPS_TIMEOUT_MS** (line 22)
- **MMC_OP_COND_PERIOD_US** (line 24)
- **MMC_OP_COND_TIMEOUT_MS** (line 25)
- **MMC_SANITIZE_TIMEOUT_MS** (line 23)
