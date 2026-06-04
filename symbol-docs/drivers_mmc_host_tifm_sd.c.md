# drivers/mmc/host/tifm_sd.c

Subsystem: drivers/mmc

## Functions (25)

### tifm_sd_abort
- Return type: static void
- Signature: tifm_sd_abort(struct timer_list * t)
- Line: 776

### tifm_sd_bounce_block
- Return type: static void
- Signature: tifm_sd_bounce_block(struct tifm_sd * host,struct mmc_data * r_data)
- Line: 221

### tifm_sd_card_event
- Return type: static void
- Signature: tifm_sd_card_event(struct tifm_dev * sock)
- Line: 497

### tifm_sd_check_status
- Return type: static void
- Signature: tifm_sd_check_status(struct tifm_sd * host)
- Line: 396

### tifm_sd_copy_page
- Return type: static void
- Signature: tifm_sd_copy_page(struct page * dst,unsigned int dst_off,struct page * src,unsigned int src_off,unsigned int count)
- Line: 208

### tifm_sd_data_event
- Return type: static void
- Signature: tifm_sd_data_event(struct tifm_dev * sock)
- Line: 469

### tifm_sd_end_cmd
- Return type: static void
- Signature: tifm_sd_end_cmd(struct work_struct * t)
- Line: 725

### tifm_sd_exec
- Return type: static void
- Signature: tifm_sd_exec(struct tifm_sd * host,struct mmc_command * cmd)
- Line: 365

### tifm_sd_exit
- Return type: static void __exit
- Signature: tifm_sd_exit(void)
- Line: 1065

### tifm_sd_fetch_resp
- Return type: static void
- Signature: tifm_sd_fetch_resp(struct mmc_command * cmd,struct tifm_dev * sock)
- Line: 384

### tifm_sd_init
- Return type: static int __init
- Signature: tifm_sd_init(void)
- Line: 1060

### tifm_sd_initialize_host
- Return type: static int
- Signature: tifm_sd_initialize_host(struct tifm_sd * host)
- Line: 874

### tifm_sd_ios
- Return type: static void
- Signature: tifm_sd_ios(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 787

### tifm_sd_op_flags
- Return type: static unsigned int
- Signature: tifm_sd_op_flags(struct mmc_command * cmd)
- Line: 322

### tifm_sd_probe
- Return type: static int
- Signature: tifm_sd_probe(struct tifm_dev * sock)
- Line: 935

### tifm_sd_read_fifo
- Return type: static void
- Signature: tifm_sd_read_fifo(struct tifm_sd * host,struct page * pg,unsigned int off,unsigned int cnt)
- Line: 113

### tifm_sd_remove
- Return type: static void
- Signature: tifm_sd_remove(struct tifm_dev * sock)
- Line: 987

### tifm_sd_request
- Return type: static void
- Signature: tifm_sd_request(struct mmc_host * mmc,struct mmc_request * mrq)
- Line: 611

### tifm_sd_resume
- Return type: static int
- Signature: tifm_sd_resume(struct tifm_dev * sock)
- Line: 1022

### tifm_sd_ro
- Return type: static int
- Signature: tifm_sd_ro(struct mmc_host * mmc)
- Line: 854

### tifm_sd_set_data_timeout
- Return type: static void
- Signature: tifm_sd_set_data_timeout(struct tifm_sd * host,struct mmc_data * data)
- Line: 583

### tifm_sd_set_dma_data
- Return type: static int
- Signature: tifm_sd_set_dma_data(struct tifm_sd * host,struct mmc_data * r_data)
- Line: 260

### tifm_sd_suspend
- Return type: static int
- Signature: tifm_sd_suspend(struct tifm_dev * sock,pm_message_t state)
- Line: 1017

### tifm_sd_transfer_data
- Return type: static void
- Signature: tifm_sd_transfer_data(struct tifm_sd * host)
- Line: 166

### tifm_sd_write_fifo
- Return type: static void
- Signature: tifm_sd_write_fifo(struct tifm_sd * host,struct page * pg,unsigned int off,unsigned int cnt)
- Line: 139

## Structs (1)

### tifm_sd
- Line: 89
- Members:
  - dev: tifm_dev *
  - eject: unsigned short:1
  - open_drain: unsigned short:1
  - no_dma: unsigned short:1
  - cmd_flags: unsigned short
  - clk_freq: unsigned int
  - clk_div: unsigned int
  - timeout_jiffies: unsigned long
  - finish_bh_work: work_struct
  - timer: timer_list
  - req: mmc_request *
  - sg_len: int
  - sg_pos: int
  - block_pos: unsigned int
  - bounce_buf: scatterlist
  - bounce_buf_data: unsigned char[]

## Enums (1)

### __anon74b699cd0103
- Line: 79

## Variables (5)

- static **fixed_timeout** : bool (line 23)
- static **no_dma** : bool (line 22)
- static **tifm_sd_driver** : tifm_driver (line 1048)
- static **tifm_sd_id_tbl** : tifm_device_id[] (line 1044)
- static **tifm_sd_ops** : const struct mmc_host_ops (line 868)

## Macros (46)

- **DRIVER_NAME** (line 19)
- **DRIVER_VERSION** (line 20)
- **TIFM_MMCSD_4BBUS** (line 31)
- **TIFM_MMCSD_AE** (line 50)
- **TIFM_MMCSD_AF** (line 49)
- **TIFM_MMCSD_BRS** (line 43)
- **TIFM_MMCSD_BUFINT** (line 34)
- **TIFM_MMCSD_CARD_RO** (line 56)
- **TIFM_MMCSD_CB** (line 42)
- **TIFM_MMCSD_CCRC** (line 48)
- **TIFM_MMCSD_CD** (line 41)
- **TIFM_MMCSD_CERR** (line 53)
- **TIFM_MMCSD_CIRQ** (line 52)
- **TIFM_MMCSD_CLKMASK** (line 29)
- **TIFM_MMCSD_CMD_AC** (line 72)
- **TIFM_MMCSD_CMD_ADTC** (line 73)
- **TIFM_MMCSD_CMD_BC** (line 70)
- **TIFM_MMCSD_CMD_BCR** (line 71)
- **TIFM_MMCSD_CTO** (line 47)
- **TIFM_MMCSD_DCRC** (line 46)
- **TIFM_MMCSD_DPE** (line 35)
- **TIFM_MMCSD_DTO** (line 45)
- **TIFM_MMCSD_EOC** (line 40)
- **TIFM_MMCSD_EOFB** (line 44)
- **TIFM_MMCSD_ERRMASK** (line 39)
- **TIFM_MMCSD_FIFO_SIZE** (line 58)
- **TIFM_MMCSD_INAB** (line 36)
- **TIFM_MMCSD_MAX_BLOCK_SIZE** (line 75)
- **TIFM_MMCSD_OCRB** (line 51)
- **TIFM_MMCSD_ODTO** (line 55)
- **TIFM_MMCSD_POWER** (line 30)
- **TIFM_MMCSD_READ** (line 37)
- **TIFM_MMCSD_REQ_TIMEOUT_MS** (line 77)
- **TIFM_MMCSD_RESET** (line 28)
- **TIFM_MMCSD_RSP_BUSY** (line 68)
- **TIFM_MMCSD_RSP_R0** (line 60)
- **TIFM_MMCSD_RSP_R1** (line 61)
- **TIFM_MMCSD_RSP_R2** (line 62)
- **TIFM_MMCSD_RSP_R3** (line 63)
- **TIFM_MMCSD_RSP_R4** (line 64)
- **TIFM_MMCSD_RSP_R5** (line 65)
- **TIFM_MMCSD_RSP_R6** (line 66)
- **TIFM_MMCSD_RXDE** (line 32)
- **TIFM_MMCSD_TXDE** (line 33)
- **tifm_sd_resume** (line 1040)
- **tifm_sd_suspend** (line 1039)
