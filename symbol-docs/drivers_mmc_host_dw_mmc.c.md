# drivers/mmc/host/dw_mmc.c

Subsystem: drivers/mmc

## Functions (93)

### __dw_mci_enable_sdio_irq
- Return type: static void
- Signature: __dw_mci_enable_sdio_irq(struct dw_mci * host,int enb)
- Line: 1542

### dw_mci_ack_sdio_irq
- Return type: static void
- Signature: dw_mci_ack_sdio_irq(struct mmc_host * mmc)
- Line: 1574

### dw_mci_adjust_fifoth
- Return type: static void
- Signature: dw_mci_adjust_fifoth(struct dw_mci * host,struct mmc_data * data)
- Line: 901

### dw_mci_alloc_host
- Return type: dw_mci *
- Signature: dw_mci_alloc_host(struct device * dev)
- Line: 3176

### dw_mci_card_busy
- Return type: static int
- Signature: dw_mci_card_busy(struct mmc_host * mmc)
- Line: 1412

### dw_mci_cleanup_host
- Return type: static void
- Signature: dw_mci_cleanup_host(struct dw_mci * host)
- Line: 2901

### dw_mci_clear_pending_cmd_complete
- Return type: static bool
- Signature: dw_mci_clear_pending_cmd_complete(struct dw_mci * host)
- Line: 1880

### dw_mci_clear_pending_data_complete
- Return type: static bool
- Signature: dw_mci_clear_pending_data_complete(struct dw_mci * host)
- Line: 1898

### dw_mci_cmd11_timer
- Return type: static void
- Signature: dw_mci_cmd11_timer(struct timer_list * t)
- Line: 2997

### dw_mci_cmd_interrupt
- Return type: static void
- Signature: dw_mci_cmd_interrupt(struct dw_mci * host,u32 status)
- Line: 2634

### dw_mci_command_complete
- Return type: static int
- Signature: dw_mci_command_complete(struct dw_mci * host,struct mmc_command * cmd)
- Line: 1773

### dw_mci_cto_timer
- Return type: static void
- Signature: dw_mci_cto_timer(struct timer_list * t)
- Line: 3011

### dw_mci_ctrl_reset
- Return type: static bool
- Signature: dw_mci_ctrl_reset(struct dw_mci * host,u32 reset)
- Line: 181

### dw_mci_ctrl_thld
- Return type: static void
- Signature: dw_mci_ctrl_thld(struct dw_mci * host,struct mmc_data * data)
- Line: 941

### dw_mci_data_complete
- Return type: static int
- Signature: dw_mci_data_complete(struct dw_mci * host,struct mmc_data * data)
- Line: 1806

### dw_mci_dma_cleanup
- Return type: static void
- Signature: dw_mci_dma_cleanup(struct dw_mci * host)
- Line: 423

### dw_mci_dmac_complete_dma
- Return type: static void
- Signature: dw_mci_dmac_complete_dma(void * arg)
- Line: 461

### dw_mci_dto_timer
- Return type: static void
- Signature: dw_mci_dto_timer(struct timer_list * t)
- Line: 3066

### dw_mci_edmac_exit
- Return type: static void
- Signature: dw_mci_edmac_exit(struct dw_mci * host)
- Line: 788

### dw_mci_edmac_init
- Return type: static int
- Signature: dw_mci_edmac_init(struct dw_mci * host)
- Line: 768

### dw_mci_edmac_start_dma
- Return type: static int
- Signature: dw_mci_edmac_start_dma(struct dw_mci * host,unsigned int sg_len)
- Line: 710

### dw_mci_edmac_stop_dma
- Return type: static void
- Signature: dw_mci_edmac_stop_dma(struct dw_mci * host)
- Line: 705

### dw_mci_enable_cd
- Return type: static void
- Signature: dw_mci_enable_cd(struct dw_mci * host)
- Line: 3155

### dw_mci_enable_sdio_irq
- Return type: static void
- Signature: dw_mci_enable_sdio_irq(struct mmc_host * mmc,int enb)
- Line: 1560

### dw_mci_execute_tuning
- Return type: static int
- Signature: dw_mci_execute_tuning(struct mmc_host * mmc,u32 opcode)
- Line: 1581

### dw_mci_fault_timer
- Return type: static hrtimer_restart
- Signature: dw_mci_fault_timer(struct hrtimer * t)
- Line: 1688

### dw_mci_get_cd
- Return type: static int
- Signature: dw_mci_get_cd(struct mmc_host * mmc)
- Line: 882

### dw_mci_get_ro
- Return type: static int
- Signature: dw_mci_get_ro(struct mmc_host * mmc)
- Line: 1462

### dw_mci_handle_cd
- Return type: static void
- Signature: dw_mci_handle_cd(struct dw_mci * host)
- Line: 2649

### dw_mci_hw_reset
- Return type: static void
- Signature: dw_mci_hw_reset(struct mmc_host * mmc)
- Line: 1481

### dw_mci_idmac_init
- Return type: static int
- Signature: dw_mci_idmac_init(struct dw_mci * host)
- Line: 488

### dw_mci_idmac_reset
- Return type: static void
- Signature: dw_mci_idmac_reset(struct dw_mci * host)
- Line: 436

### dw_mci_idmac_start_dma
- Return type: static int
- Signature: dw_mci_idmac_start_dma(struct dw_mci * host,unsigned int sg_len)
- Line: 661

### dw_mci_idmac_stop_dma
- Return type: static void
- Signature: dw_mci_idmac_stop_dma(struct dw_mci * host)
- Line: 444

### dw_mci_init_debugfs
- Return type: static void
- Signature: dw_mci_init_debugfs(struct dw_mci * host)
- Line: 159

### dw_mci_init_dma
- Return type: static void
- Signature: dw_mci_init_dma(struct dw_mci * host)
- Line: 2907

### dw_mci_init_fault
- Return type: static void
- Signature: dw_mci_init_fault(struct dw_mci * host)
- Line: 1733

### dw_mci_init_fault
- Return type: static void
- Signature: dw_mci_init_fault(struct dw_mci * host)
- Line: 1740

### dw_mci_init_host
- Return type: static int
- Signature: dw_mci_init_host(struct dw_mci * host)
- Line: 2834

### dw_mci_init_host_caps
- Return type: static int
- Signature: dw_mci_init_host_caps(struct dw_mci * host)
- Line: 2795

### dw_mci_interrupt
- Return type: static irqreturn_t
- Signature: dw_mci_interrupt(int irq,void * dev_id)
- Line: 2655

### dw_mci_parse_dt
- Return type: static int
- Signature: dw_mci_parse_dt(struct dw_mci * host)
- Line: 3117

### dw_mci_post_req
- Return type: static void
- Signature: dw_mci_post_req(struct mmc_host * mmc,struct mmc_request * mrq,int err)
- Line: 864

### dw_mci_pre_dma_transfer
- Return type: static int
- Signature: dw_mci_pre_dma_transfer(struct dw_mci * host,struct mmc_data * data,int cookie)
- Line: 809

### dw_mci_pre_req
- Return type: static void
- Signature: dw_mci_pre_req(struct mmc_host * mmc,struct mmc_request * mrq)
- Line: 847

### dw_mci_prep_stop_abort
- Return type: static u32
- Signature: dw_mci_prep_stop_abort(struct dw_mci * host,struct mmc_command * cmd)
- Line: 308

### dw_mci_prepare_command
- Return type: static u32
- Signature: dw_mci_prepare_command(struct mmc_host * mmc,struct mmc_command * cmd)
- Line: 241

### dw_mci_prepare_desc
- Return type: static int
- Signature: dw_mci_prepare_desc(struct dw_mci * host,struct mmc_data * data,unsigned int sg_len,bool is_64bit)
- Line: 566

### dw_mci_prepare_hs400_tuning
- Return type: static int
- Signature: dw_mci_prepare_hs400_tuning(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 1592

### dw_mci_prepare_sdio_irq
- Return type: static void
- Signature: dw_mci_prepare_sdio_irq(struct dw_mci * host,bool prepare)
- Line: 1514

### dw_mci_probe
- Return type: int
- Signature: dw_mci_probe(struct dw_mci * host)
- Line: 3193

### dw_mci_pull_data
- Return type: static void
- Signature: dw_mci_pull_data(struct dw_mci * host,void * buf,int cnt)
- Line: 2511

### dw_mci_pull_data16
- Return type: static void
- Signature: dw_mci_pull_data16(struct dw_mci * host,void * buf,int cnt)
- Line: 2225

### dw_mci_pull_data32
- Return type: static void
- Signature: dw_mci_pull_data32(struct dw_mci * host,void * buf,int cnt)
- Line: 2308

### dw_mci_pull_data64
- Return type: static void
- Signature: dw_mci_pull_data64(struct dw_mci * host,void * buf,int cnt)
- Line: 2392

### dw_mci_pull_data64_32
- Return type: static void
- Signature: dw_mci_pull_data64_32(struct dw_mci * host,void * buf,int cnt)
- Line: 2477

### dw_mci_pull_final_bytes
- Return type: static void
- Signature: dw_mci_pull_final_bytes(struct dw_mci * host,void * buf,int cnt)
- Line: 2168

### dw_mci_pull_part_bytes
- Return type: static int
- Signature: dw_mci_pull_part_bytes(struct dw_mci * host,void * buf,int cnt)
- Line: 2155

### dw_mci_push_data16
- Return type: static void
- Signature: dw_mci_push_data16(struct dw_mci * host,void * buf,int cnt)
- Line: 2175

### dw_mci_push_data32
- Return type: static void
- Signature: dw_mci_push_data32(struct dw_mci * host,void * buf,int cnt)
- Line: 2258

### dw_mci_push_data64
- Return type: static void
- Signature: dw_mci_push_data64(struct dw_mci * host,void * buf,int cnt)
- Line: 2341

### dw_mci_push_data64_32
- Return type: static void
- Signature: dw_mci_push_data64_32(struct dw_mci * host,void * buf,int cnt)
- Line: 2426

### dw_mci_push_part_bytes
- Return type: static int
- Signature: dw_mci_push_part_bytes(struct dw_mci * host,void * buf,int cnt)
- Line: 2146

### dw_mci_read_data_pio
- Return type: static void
- Signature: dw_mci_read_data_pio(struct dw_mci * host,bool dto)
- Line: 2526

### dw_mci_regs_show
- Return type: static int
- Signature: dw_mci_regs_show(struct seq_file * s,void * v)
- Line: 140

### dw_mci_remove
- Return type: void
- Signature: dw_mci_remove(struct dw_mci * host)
- Line: 3404

### dw_mci_req_show
- Return type: static int
- Signature: dw_mci_req_show(struct seq_file * s,void * v)
- Line: 99

### dw_mci_request
- Return type: static void
- Signature: dw_mci_request(struct mmc_host * mmc,struct mmc_request * mrq)
- Line: 1286

### dw_mci_request_end
- Return type: static void
- Signature: dw_mci_request_end(struct dw_mci * host,struct mmc_request * mrq)
- Line: 1753

### dw_mci_reset
- Return type: static bool
- Signature: dw_mci_reset(struct dw_mci * host)
- Line: 1604

### dw_mci_runtime_resume
- Return type: int
- Signature: dw_mci_runtime_resume(struct device * dev)
- Line: 3443

### dw_mci_runtime_suspend
- Return type: int
- Signature: dw_mci_runtime_suspend(struct device * dev)
- Line: 3426

### dw_mci_set_cto
- Return type: static void
- Signature: dw_mci_set_cto(struct dw_mci * host)
- Line: 347

### dw_mci_set_data_timeout
- Return type: static void
- Signature: dw_mci_set_data_timeout(struct dw_mci * host,unsigned int timeout_ns)
- Line: 1196

### dw_mci_set_drto
- Return type: static void
- Signature: dw_mci_set_drto(struct dw_mci * host)
- Line: 1849

### dw_mci_set_ios
- Return type: static void
- Signature: dw_mci_set_ios(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 1330

### dw_mci_set_part_bytes
- Return type: static void
- Signature: dw_mci_set_part_bytes(struct dw_mci * host,void * buf,int cnt)
- Line: 2139

### dw_mci_setup_bus
- Return type: static void
- Signature: dw_mci_setup_bus(struct dw_mci * host,bool force_clkinit)
- Line: 1115

### dw_mci_start_command
- Return type: static void
- Signature: dw_mci_start_command(struct dw_mci * host,struct mmc_command * cmd,u32 cmd_flags)
- Line: 385

### dw_mci_start_fault_timer
- Return type: static void
- Signature: dw_mci_start_fault_timer(struct dw_mci * host)
- Line: 1710

### dw_mci_start_fault_timer
- Return type: static void
- Signature: dw_mci_start_fault_timer(struct dw_mci * host)
- Line: 1744

### dw_mci_start_request
- Return type: static void
- Signature: dw_mci_start_request(struct dw_mci * host,struct mmc_command * cmd)
- Line: 1227

### dw_mci_stop_dma
- Return type: static void
- Signature: dw_mci_stop_dma(struct dw_mci * host)
- Line: 412

### dw_mci_stop_fault_timer
- Return type: static void
- Signature: dw_mci_stop_fault_timer(struct dw_mci * host)
- Line: 1728

### dw_mci_stop_fault_timer
- Return type: static void
- Signature: dw_mci_stop_fault_timer(struct dw_mci * host)
- Line: 1748

### dw_mci_submit_data
- Return type: static void
- Signature: dw_mci_submit_data(struct dw_mci * host,struct mmc_data * data)
- Line: 1052

### dw_mci_submit_data_dma
- Return type: static int
- Signature: dw_mci_submit_data_dma(struct dw_mci * host,struct mmc_data * data)
- Line: 993

### dw_mci_switch_voltage
- Return type: static int
- Signature: dw_mci_switch_voltage(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 1426

### dw_mci_wait_while_busy
- Return type: static void
- Signature: dw_mci_wait_while_busy(struct dw_mci * host,u32 cmd_flags)
- Line: 202

### dw_mci_work_func
- Return type: static void
- Signature: dw_mci_work_func(struct work_struct * t)
- Line: 1910

### dw_mci_write_data_pio
- Return type: static void
- Signature: dw_mci_write_data_pio(struct dw_mci * host)
- Line: 2580

### mci_send_cmd
- Return type: static void
- Signature: mci_send_cmd(struct dw_mci * host,u32 cmd,u32 arg)
- Line: 224

### send_stop_abort
- Return type: static void
- Signature: send_stop_abort(struct dw_mci * host,struct mmc_data * data)
- Line: 404

## Structs (2)

### idmac_desc
- Line: 76
- Members:
  - des0: u32
  - des1: u32
  - des2: u32
  - des3: u32
  - des4: u32
  - des5: u32
  - des6: u32
  - des7: u32
  - des0: __le32
  - des1: __le32
  - des2: __le32
  - des3: __le32

### idmac_desc_64addr
- Line: 55
- Members:
  - des0: u32
  - des1: u32
  - des2: u32
  - des3: u32
  - des4: u32
  - des5: u32
  - des6: u32
  - des7: u32
  - des0: __le32
  - des1: __le32
  - des2: __le32
  - des3: __le32

## Variables (4)

- static **dw_mci_edmac_ops** : const struct dw_mci_dma_ops (line 800)
- static **dw_mci_idmac_ops** : const struct dw_mci_dma_ops (line 697)
- static **dw_mci_ops** : const struct mmc_host_ops (line 1671)
- **dw_mci_pmops** : const struct dev_pm_ops (line 3512)

## Macros (19)

- **DESC_RING_BUF_SZ** (line 53)
- **DW_MCI_CMD_ERROR_FLAGS** (line 39)
- **DW_MCI_DATA_ERROR_FLAGS** (line 36)
- **DW_MCI_DESC_DATA_LENGTH** (line 96)
- **DW_MCI_DMA_THRESHOLD** (line 43)
- **DW_MCI_ERROR_FLAGS** (line 41)
- **DW_MCI_FREQ_MAX** (line 45)
- **DW_MCI_FREQ_MIN** (line 46)
- **IDMAC_64ADDR_SET_BUFFER1_SIZE**(d,s) (line 63)
- **IDMAC_DES0_CES** (line 83)
- **IDMAC_DES0_CH** (line 81)
- **IDMAC_DES0_DIC** (line 78)
- **IDMAC_DES0_ER** (line 82)
- **IDMAC_DES0_FD** (line 80)
- **IDMAC_DES0_LD** (line 79)
- **IDMAC_DES0_OWN** (line 84)
- **IDMAC_INT_CLR** (line 48)
- **IDMAC_OWN_CLR64**(x) (line 57)
- **IDMAC_SET_BUFFER1_SIZE**(d,s) (line 87)
