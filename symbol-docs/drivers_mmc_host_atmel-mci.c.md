# drivers/mmc/host/atmel-mci.c

Subsystem: drivers/mmc

## Functions (52)

### atmci_cleanup_slot
- Return type: static void
- Signature: atmci_cleanup_slot(struct atmel_mci_slot * slot,unsigned int id)
- Line: 2341

### atmci_command_complete
- Return type: static void
- Signature: atmci_command_complete(struct atmel_mci * host,struct mmc_command * cmd)
- Line: 1621

### atmci_configure_dma
- Return type: static int
- Signature: atmci_configure_dma(struct atmel_mci * host)
- Line: 2359

### atmci_convert_chksize
- Return type: static unsigned int
- Signature: atmci_convert_chksize(struct atmel_mci * host,unsigned int maxburst)
- Line: 694

### atmci_detect_change
- Return type: static void
- Signature: atmci_detect_change(struct timer_list * t)
- Line: 1647

### atmci_detect_interrupt
- Return type: static irqreturn_t
- Signature: atmci_detect_interrupt(int irq,void * dev_id)
- Line: 2221

### atmci_dma_cleanup
- Return type: static void
- Signature: atmci_dma_cleanup(struct atmel_mci * host)
- Line: 959

### atmci_dma_complete
- Return type: static void
- Signature: atmci_dma_complete(void * arg)
- Line: 972

### atmci_enable_sdio_irq
- Return type: static void
- Signature: atmci_enable_sdio_irq(struct mmc_host * mmc,int enable)
- Line: 1559

### atmci_get_cap
- Return type: static void
- Signature: atmci_get_cap(struct atmel_mci * host)
- Line: 2385

### atmci_get_cd
- Return type: static int
- Signature: atmci_get_cd(struct mmc_host * mmc)
- Line: 1545

### atmci_get_ro
- Return type: static int
- Signature: atmci_get_ro(struct mmc_host * mmc)
- Line: 1531

### atmci_get_version
- Return type: static unsigned int
- Signature: atmci_get_version(struct atmel_mci * host)
- Line: 681

### atmci_init_debugfs
- Return type: static void
- Signature: atmci_init_debugfs(struct atmel_mci_slot * slot)
- Line: 602

### atmci_init_slot
- Return type: static int
- Signature: atmci_init_slot(struct atmel_mci * host,struct mci_slot_pdata * slot_data,unsigned int id,u32 sdc_reg,u32 sdio_irq)
- Line: 2236

### atmci_interrupt
- Return type: static irqreturn_t
- Signature: atmci_interrupt(int irq,void * dev_id)
- Line: 2092

### atmci_ns_to_clocks
- Return type: static unsigned int
- Signature: atmci_ns_to_clocks(struct atmel_mci * host,unsigned int ns)
- Line: 736

### atmci_of_init
- Return type: static int
- Signature: atmci_of_init(struct atmel_mci * host)
- Line: 628

### atmci_pdc_cleanup
- Return type: static void
- Signature: atmci_pdc_cleanup(struct atmel_mci * host)
- Line: 921

### atmci_pdc_complete
- Return type: static void
- Signature: atmci_pdc_complete(struct atmel_mci * host)
- Line: 935

### atmci_pdc_set_both_buf
- Return type: static void
- Signature: atmci_pdc_set_both_buf(struct atmel_mci * host,int dir)
- Line: 911

### atmci_pdc_set_single_buf
- Return type: static void
- Signature: atmci_pdc_set_single_buf(struct atmel_mci * host,enum atmci_xfer_dir dir,enum atmci_pdc_buf buf_nb)
- Line: 860

### atmci_prepare_command
- Return type: static u32
- Signature: atmci_prepare_command(struct mmc_host * mmc,struct mmc_command * cmd)
- Line: 782

### atmci_prepare_data
- Return type: static u32
- Signature: atmci_prepare_data(struct atmel_mci * host,struct mmc_data * data)
- Line: 1023

### atmci_prepare_data_dma
- Return type: static u32
- Signature: atmci_prepare_data_dma(struct atmel_mci * host,struct mmc_data * data)
- Line: 1109

### atmci_prepare_data_pdc
- Return type: static u32
- Signature: atmci_prepare_data_pdc(struct atmel_mci * host,struct mmc_data * data)
- Line: 1063

### atmci_probe
- Return type: static int
- Signature: atmci_probe(struct platform_device * pdev)
- Line: 2437

### atmci_queue_request
- Return type: static void
- Signature: atmci_queue_request(struct atmel_mci * host,struct atmel_mci_slot * slot,struct mmc_request * mrq)
- Line: 1347

### atmci_read_data_pio
- Return type: static void
- Signature: atmci_read_data_pio(struct atmel_mci * host)
- Line: 1944

### atmci_regs_show
- Return type: static int
- Signature: atmci_regs_show(struct seq_file * s,void * v)
- Line: 522

### atmci_remove
- Return type: static void
- Signature: atmci_remove(struct platform_device * pdev)
- Line: 2587

### atmci_req_show
- Return type: static int
- Signature: atmci_req_show(struct seq_file * s,void * v)
- Line: 434

### atmci_request
- Return type: static void
- Signature: atmci_request(struct mmc_host * mmc,struct mmc_request * mrq)
- Line: 1367

### atmci_request_end
- Return type: static void
- Signature: atmci_request_end(struct atmel_mci * host,struct mmc_request * mrq)
- Line: 1579

### atmci_runtime_resume
- Return type: static int
- Signature: atmci_runtime_resume(struct device * dev)
- Line: 2630

### atmci_runtime_suspend
- Return type: static int
- Signature: atmci_runtime_suspend(struct device * dev)
- Line: 2619

### atmci_sdio_interrupt
- Return type: static void
- Signature: atmci_sdio_interrupt(struct atmel_mci * host,u32 status)
- Line: 2079

### atmci_send_command
- Return type: static void
- Signature: atmci_send_command(struct atmel_mci * host,struct mmc_command * cmd,u32 cmd_flags)
- Line: 829

### atmci_send_stop_cmd
- Return type: static void
- Signature: atmci_send_stop_cmd(struct atmel_mci * host,struct mmc_data * data)
- Line: 847

### atmci_set_ios
- Return type: static void
- Signature: atmci_set_ios(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 1401

### atmci_set_timeout
- Return type: static void
- Signature: atmci_set_timeout(struct atmel_mci * host,struct atmel_mci_slot * slot,struct mmc_data * data)
- Line: 749

### atmci_show_status_reg
- Return type: static void
- Signature: atmci_show_status_reg(struct seq_file * s,const char * regname,u32 value)
- Line: 476

### atmci_start_request
- Return type: static void
- Signature: atmci_start_request(struct atmel_mci * host,struct atmel_mci_slot * slot)
- Line: 1252

### atmci_stop_transfer
- Return type: static void
- Signature: atmci_stop_transfer(struct atmel_mci * host)
- Line: 1215

### atmci_stop_transfer_dma
- Return type: static void
- Signature: atmci_stop_transfer_dma(struct atmel_mci * host)
- Line: 1232

### atmci_stop_transfer_pdc
- Return type: static void
- Signature: atmci_stop_transfer_pdc(struct atmel_mci * host)
- Line: 1227

### atmci_submit_data
- Return type: static void
- Signature: atmci_submit_data(struct atmel_mci * host,struct mmc_data * data)
- Line: 1186

### atmci_submit_data_dma
- Return type: static void
- Signature: atmci_submit_data_dma(struct atmel_mci * host,struct mmc_data * data)
- Line: 1204

### atmci_submit_data_pdc
- Return type: static void
- Signature: atmci_submit_data_pdc(struct atmel_mci * host,struct mmc_data * data)
- Line: 1195

### atmci_timeout_timer
- Return type: static void
- Signature: atmci_timeout_timer(struct timer_list * t)
- Line: 709

### atmci_work_func
- Return type: static void
- Signature: atmci_work_func(struct work_struct * t)
- Line: 1744

### atmci_write_data_pio
- Return type: static void
- Signature: atmci_write_data_pio(struct atmel_mci * host)
- Line: 2011

## Structs (5)

### atmel_mci
- Line: 332
- Members:
  - bus_width: unsigned int
  - detect_pin: gpio_desc *
  - wp_pin: gpio_desc *
  - non_removable: bool
  - has_dma_conf_reg: bool
  - has_pdc: bool
  - has_cfg_reg: bool
  - has_cstor_reg: bool
  - has_highspeed: bool
  - has_rwproof: bool
  - has_odd_clk_div: bool
  - has_bad_data_ordering: bool
  - need_reset_after_xfer: bool
  - need_blksz_mul_4: bool
  - need_notbusy_for_read_ops: bool
  - chan: dma_chan *
  - data_desc: dma_async_tx_descriptor *
  - lock: spinlock_t
  - regs: void __iomem *
  - sg: scatterlist *
  - sg_len: unsigned int
  - pio_offset: unsigned int
  - buffer: unsigned int *
  - buf_size: unsigned int
  - buf_phys_addr: dma_addr_t
  - cur_slot: atmel_mci_slot *
  - mrq: mmc_request *
  - cmd: mmc_command *
  - data: mmc_data *
  - data_size: unsigned int
  - dma: atmel_mci_dma
  - data_chan: dma_chan *
  - dma_conf: dma_slave_config
  - cmd_status: u32
  - data_status: u32
  - stop_cmdr: u32
  - bh_work: work_struct
  - pending_events: unsigned long
  - completed_events: unsigned long
  - state: atmel_mci_state
  - queue: list_head
  - need_clock_update: bool
  - need_reset: bool
  - timer: timer_list
  - mode_reg: u32
  - cfg_reg: u32
  - bus_hz: unsigned long
  - mapbase: unsigned long
  - mck: clk *
  - dev: device *
  - pdata: mci_slot_pdata[]
  - slot: atmel_mci_slot * []
  - caps: atmel_mci_caps
  - prepare_data: u32 (*)(struct atmel_mci * host,struct mmc_data * data)
  - submit_data: void (*)(struct atmel_mci * host,struct mmc_data * data)
  - stop_transfer: void (*)(struct atmel_mci * host)
  - mmc: mmc_host *
  - host: atmel_mci *
  - sdc_reg: u32
  - sdio_irq: u32
  - mrq: mmc_request *
  - queue_node: list_head
  - clock: unsigned int
  - flags: unsigned long
  - detect_pin: gpio_desc *
  - wp_pin: gpio_desc *
  - detect_timer: timer_list

### atmel_mci_caps
- Line: 229
- Members:
  - bus_width: unsigned int
  - detect_pin: gpio_desc *
  - wp_pin: gpio_desc *
  - non_removable: bool
  - has_dma_conf_reg: bool
  - has_pdc: bool
  - has_cfg_reg: bool
  - has_cstor_reg: bool
  - has_highspeed: bool
  - has_rwproof: bool
  - has_odd_clk_div: bool
  - has_bad_data_ordering: bool
  - need_reset_after_xfer: bool
  - need_blksz_mul_4: bool
  - need_notbusy_for_read_ops: bool
  - chan: dma_chan *
  - data_desc: dma_async_tx_descriptor *
  - lock: spinlock_t
  - regs: void __iomem *
  - sg: scatterlist *
  - sg_len: unsigned int
  - pio_offset: unsigned int
  - buffer: unsigned int *
  - buf_size: unsigned int
  - buf_phys_addr: dma_addr_t
  - cur_slot: atmel_mci_slot *
  - mrq: mmc_request *
  - cmd: mmc_command *
  - data: mmc_data *
  - data_size: unsigned int
  - dma: atmel_mci_dma
  - data_chan: dma_chan *
  - dma_conf: dma_slave_config
  - cmd_status: u32
  - data_status: u32
  - stop_cmdr: u32
  - bh_work: work_struct
  - pending_events: unsigned long
  - completed_events: unsigned long
  - state: atmel_mci_state
  - queue: list_head
  - need_clock_update: bool
  - need_reset: bool
  - timer: timer_list
  - mode_reg: u32
  - cfg_reg: u32
  - bus_hz: unsigned long
  - mapbase: unsigned long
  - mck: clk *
  - dev: device *
  - pdata: mci_slot_pdata[]
  - slot: atmel_mci_slot * []
  - caps: atmel_mci_caps
  - prepare_data: u32 (*)(struct atmel_mci * host,struct mmc_data * data)
  - submit_data: void (*)(struct atmel_mci * host,struct mmc_data * data)
  - stop_transfer: void (*)(struct atmel_mci * host)
  - mmc: mmc_host *
  - host: atmel_mci *
  - sdc_reg: u32
  - sdio_irq: u32
  - mrq: mmc_request *
  - queue_node: list_head
  - clock: unsigned int
  - flags: unsigned long
  - detect_pin: gpio_desc *
  - wp_pin: gpio_desc *
  - detect_timer: timer_list

### atmel_mci_dma
- Line: 243
- Members:
  - bus_width: unsigned int
  - detect_pin: gpio_desc *
  - wp_pin: gpio_desc *
  - non_removable: bool
  - has_dma_conf_reg: bool
  - has_pdc: bool
  - has_cfg_reg: bool
  - has_cstor_reg: bool
  - has_highspeed: bool
  - has_rwproof: bool
  - has_odd_clk_div: bool
  - has_bad_data_ordering: bool
  - need_reset_after_xfer: bool
  - need_blksz_mul_4: bool
  - need_notbusy_for_read_ops: bool
  - chan: dma_chan *
  - data_desc: dma_async_tx_descriptor *
  - lock: spinlock_t
  - regs: void __iomem *
  - sg: scatterlist *
  - sg_len: unsigned int
  - pio_offset: unsigned int
  - buffer: unsigned int *
  - buf_size: unsigned int
  - buf_phys_addr: dma_addr_t
  - cur_slot: atmel_mci_slot *
  - mrq: mmc_request *
  - cmd: mmc_command *
  - data: mmc_data *
  - data_size: unsigned int
  - dma: atmel_mci_dma
  - data_chan: dma_chan *
  - dma_conf: dma_slave_config
  - cmd_status: u32
  - data_status: u32
  - stop_cmdr: u32
  - bh_work: work_struct
  - pending_events: unsigned long
  - completed_events: unsigned long
  - state: atmel_mci_state
  - queue: list_head
  - need_clock_update: bool
  - need_reset: bool
  - timer: timer_list
  - mode_reg: u32
  - cfg_reg: u32
  - bus_hz: unsigned long
  - mapbase: unsigned long
  - mck: clk *
  - dev: device *
  - pdata: mci_slot_pdata[]
  - slot: atmel_mci_slot * []
  - caps: atmel_mci_caps
  - prepare_data: u32 (*)(struct atmel_mci * host,struct mmc_data * data)
  - submit_data: void (*)(struct atmel_mci * host,struct mmc_data * data)
  - stop_transfer: void (*)(struct atmel_mci * host)
  - mmc: mmc_host *
  - host: atmel_mci *
  - sdc_reg: u32
  - sdio_irq: u32
  - mrq: mmc_request *
  - queue_node: list_head
  - clock: unsigned int
  - flags: unsigned long
  - detect_pin: gpio_desc *
  - wp_pin: gpio_desc *
  - detect_timer: timer_list

### atmel_mci_slot
- Line: 401
- Members:
  - bus_width: unsigned int
  - detect_pin: gpio_desc *
  - wp_pin: gpio_desc *
  - non_removable: bool
  - has_dma_conf_reg: bool
  - has_pdc: bool
  - has_cfg_reg: bool
  - has_cstor_reg: bool
  - has_highspeed: bool
  - has_rwproof: bool
  - has_odd_clk_div: bool
  - has_bad_data_ordering: bool
  - need_reset_after_xfer: bool
  - need_blksz_mul_4: bool
  - need_notbusy_for_read_ops: bool
  - chan: dma_chan *
  - data_desc: dma_async_tx_descriptor *
  - lock: spinlock_t
  - regs: void __iomem *
  - sg: scatterlist *
  - sg_len: unsigned int
  - pio_offset: unsigned int
  - buffer: unsigned int *
  - buf_size: unsigned int
  - buf_phys_addr: dma_addr_t
  - cur_slot: atmel_mci_slot *
  - mrq: mmc_request *
  - cmd: mmc_command *
  - data: mmc_data *
  - data_size: unsigned int
  - dma: atmel_mci_dma
  - data_chan: dma_chan *
  - dma_conf: dma_slave_config
  - cmd_status: u32
  - data_status: u32
  - stop_cmdr: u32
  - bh_work: work_struct
  - pending_events: unsigned long
  - completed_events: unsigned long
  - state: atmel_mci_state
  - queue: list_head
  - need_clock_update: bool
  - need_reset: bool
  - timer: timer_list
  - mode_reg: u32
  - cfg_reg: u32
  - bus_hz: unsigned long
  - mapbase: unsigned long
  - mck: clk *
  - dev: device *
  - pdata: mci_slot_pdata[]
  - slot: atmel_mci_slot * []
  - caps: atmel_mci_caps
  - prepare_data: u32 (*)(struct atmel_mci * host,struct mmc_data * data)
  - submit_data: void (*)(struct atmel_mci * host,struct mmc_data * data)
  - stop_transfer: void (*)(struct atmel_mci * host)
  - mmc: mmc_host *
  - host: atmel_mci *
  - sdc_reg: u32
  - sdio_irq: u32
  - mrq: mmc_request *
  - queue_node: list_head
  - clock: unsigned int
  - flags: unsigned long
  - detect_pin: gpio_desc *
  - wp_pin: gpio_desc *
  - detect_timer: timer_list

### mci_slot_pdata
- Line: 222
- Members:
  - bus_width: unsigned int
  - detect_pin: gpio_desc *
  - wp_pin: gpio_desc *
  - non_removable: bool
  - has_dma_conf_reg: bool
  - has_pdc: bool
  - has_cfg_reg: bool
  - has_cstor_reg: bool
  - has_highspeed: bool
  - has_rwproof: bool
  - has_odd_clk_div: bool
  - has_bad_data_ordering: bool
  - need_reset_after_xfer: bool
  - need_blksz_mul_4: bool
  - need_notbusy_for_read_ops: bool
  - chan: dma_chan *
  - data_desc: dma_async_tx_descriptor *
  - lock: spinlock_t
  - regs: void __iomem *
  - sg: scatterlist *
  - sg_len: unsigned int
  - pio_offset: unsigned int
  - buffer: unsigned int *
  - buf_size: unsigned int
  - buf_phys_addr: dma_addr_t
  - cur_slot: atmel_mci_slot *
  - mrq: mmc_request *
  - cmd: mmc_command *
  - data: mmc_data *
  - data_size: unsigned int
  - dma: atmel_mci_dma
  - data_chan: dma_chan *
  - dma_conf: dma_slave_config
  - cmd_status: u32
  - data_status: u32
  - stop_cmdr: u32
  - bh_work: work_struct
  - pending_events: unsigned long
  - completed_events: unsigned long
  - state: atmel_mci_state
  - queue: list_head
  - need_clock_update: bool
  - need_reset: bool
  - timer: timer_list
  - mode_reg: u32
  - cfg_reg: u32
  - bus_hz: unsigned long
  - mapbase: unsigned long
  - mck: clk *
  - dev: device *
  - pdata: mci_slot_pdata[]
  - slot: atmel_mci_slot * []
  - caps: atmel_mci_caps
  - prepare_data: u32 (*)(struct atmel_mci * host,struct mmc_data * data)
  - submit_data: void (*)(struct atmel_mci * host,struct mmc_data * data)
  - stop_transfer: void (*)(struct atmel_mci * host)
  - mmc: mmc_host *
  - host: atmel_mci *
  - sdc_reg: u32
  - sdio_irq: u32
  - mrq: mmc_request *
  - queue_node: list_head
  - clock: unsigned int
  - flags: unsigned long
  - detect_pin: gpio_desc *
  - wp_pin: gpio_desc *
  - detect_timer: timer_list

## Enums (4)

### __anond6db7fe00103
- Line: 180

### atmci_pdc_buf
- Line: 201

### atmci_xfer_dir
- Line: 196

### atmel_mci_state
- Line: 187

## Variables (4)

- static **atmci_dev_pm_ops** : const struct dev_pm_ops (line 2639)
- static **atmci_driver** : platform_driver (line 2644)
- static **atmci_dt_ids** : const struct of_device_id[] (line 621)
- static **atmci_ops** : const struct mmc_host_ops (line 1570)

## Macros (127)

- **ATMCI_ACKRCV** (line 143)
- **ATMCI_ACKRCVE** (line 144)
- **ATMCI_ARGR** (line 77)
- **ATMCI_BCNT**(x) (line 102)
- **ATMCI_BLKE** (line 120)
- **ATMCI_BLKLEN**(x) (line 103)
- **ATMCI_BLKOVRE** (line 139)
- **ATMCI_BLKR** (line 101)
- **ATMCI_CARD_NEED_INIT** (line 414)
- **ATMCI_CARD_PRESENT** (line 413)
- **ATMCI_CFG** (line 151)
- **ATMCI_CFG_FERRCTRL_COR** (line 153)
- **ATMCI_CFG_FIFOMODE_1DATA** (line 152)
- **ATMCI_CFG_HSMODE** (line 154)
- **ATMCI_CFG_LSYNC** (line 155)
- **ATMCI_CMDR** (line 78)
- **ATMCI_CMDRDY** (line 117)
- **ATMCI_CMDR_BLOCK** (line 94)
- **ATMCI_CMDR_CMDNB**(x) (line 79)
- **ATMCI_CMDR_MAXLAT_5CYC** (line 88)
- **ATMCI_CMDR_MAXLAT_64CYC** (line 89)
- **ATMCI_CMDR_MULTI_BLOCK** (line 95)
- **ATMCI_CMDR_OPDCMD** (line 87)
- **ATMCI_CMDR_RSPTYP_136BIT** (line 82)
- **ATMCI_CMDR_RSPTYP_48BIT** (line 81)
- **ATMCI_CMDR_RSPTYP_NONE** (line 80)
- **ATMCI_CMDR_SDIO_BLOCK** (line 98)
- **ATMCI_CMDR_SDIO_BYTE** (line 97)
- **ATMCI_CMDR_SDIO_RESUME** (line 100)
- **ATMCI_CMDR_SDIO_SUSPEND** (line 99)
- **ATMCI_CMDR_SPCMD_INIT** (line 83)
- **ATMCI_CMDR_SPCMD_INT** (line 85)
- **ATMCI_CMDR_SPCMD_INTRESP** (line 86)
- **ATMCI_CMDR_SPCMD_SYNC** (line 84)
- **ATMCI_CMDR_START_XFER** (line 90)
- **ATMCI_CMDR_STOP_XFER** (line 91)
- **ATMCI_CMDR_STREAM** (line 96)
- **ATMCI_CMDR_TRDIR_READ** (line 93)
- **ATMCI_CMDR_TRDIR_WRITE** (line 92)
- **ATMCI_CMD_TIMEOUT_MS** (line 174)
- **ATMCI_CR** (line 51)
- **ATMCI_CR_MCIDIS** (line 53)
- **ATMCI_CR_MCIEN** (line 52)
- **ATMCI_CR_PWSDIS** (line 55)
- **ATMCI_CR_PWSEN** (line 54)
- **ATMCI_CR_SWRST** (line 56)
- **ATMCI_CSRCV** (line 128)
- **ATMCI_CSTOCYC**(x) (line 105)
- **ATMCI_CSTOE** (line 138)
- **ATMCI_CSTOMUL**(x) (line 106)
- **ATMCI_CSTOR** (line 104)
- **ATMCI_DATA_ERROR_FLAGS** (line 177)
- **ATMCI_DCRCE** (line 136)
- **ATMCI_DMA** (line 147)
- **ATMCI_DMADONE** (line 140)
- **ATMCI_DMAEN** (line 150)
- **ATMCI_DMA_CHKSIZE**(x) (line 149)
- **ATMCI_DMA_OFFSET**(x) (line 148)
- **ATMCI_DMA_THRESHOLD** (line 178)
- **ATMCI_DTIP** (line 121)
- **ATMCI_DTOCYC**(x) (line 67)
- **ATMCI_DTOE** (line 137)
- **ATMCI_DTOMUL**(x) (line 68)
- **ATMCI_DTOR** (line 66)
- **ATMCI_ENDRX** (line 123)
- **ATMCI_ENDTX** (line 124)
- **ATMCI_FIFOEMPTY** (line 141)
- **ATMCI_FIFO_APERTURE** (line 163)
- **ATMCI_GET_WP_VS**(x) (line 160)
- **ATMCI_GET_WP_VSRC**(x) (line 161)
- **ATMCI_IDR** (line 115)
- **ATMCI_IER** (line 114)
- **ATMCI_IMR** (line 116)
- **ATMCI_MAX_NR_SLOTS** (line 43)
- **ATMCI_MR** (line 57)
- **ATMCI_MR_CLKDIV**(x) (line 58)
- **ATMCI_MR_CLKODD**(x) (line 65)
- **ATMCI_MR_PDCFBYTE** (line 62)
- **ATMCI_MR_PDCMODE** (line 64)
- **ATMCI_MR_PDCPADV** (line 63)
- **ATMCI_MR_PWSDIV**(x) (line 59)
- **ATMCI_MR_RDPROOF** (line 60)
- **ATMCI_MR_WRPROOF** (line 61)
- **ATMCI_NOTBUSY** (line 122)
- **ATMCI_OVRE** (line 145)
- **ATMCI_RCRCE** (line 133)
- **ATMCI_RDIRE** (line 132)
- **ATMCI_RDR** (line 111)
- **ATMCI_REGS_SIZE** (line 166)
- **ATMCI_RENDE** (line 134)
- **ATMCI_RINDE** (line 131)
- **ATMCI_RSPR** (line 107)
- **ATMCI_RSPR1** (line 108)
- **ATMCI_RSPR2** (line 109)
- **ATMCI_RSPR3** (line 110)
- **ATMCI_RTOE** (line 135)
- **ATMCI_RXBUFF** (line 129)
- **ATMCI_RXRDY** (line 118)
- **ATMCI_SDCBUS_1BIT** (line 73)
- **ATMCI_SDCBUS_4BIT** (line 74)
- **ATMCI_SDCBUS_8BIT** (line 75)
- **ATMCI_SDCBUS_MASK** (line 76)
- **ATMCI_SDCR** (line 69)
- **ATMCI_SDCSEL_MASK** (line 72)
- **ATMCI_SDCSEL_SLOT_A** (line 70)
- **ATMCI_SDCSEL_SLOT_B** (line 71)
- **ATMCI_SDIOIRQA** (line 125)
- **ATMCI_SDIOIRQB** (line 126)
- **ATMCI_SDIOWAIT** (line 127)
- **ATMCI_SHUTDOWN** (line 415)
- **ATMCI_SR** (line 113)
- **ATMCI_TDR** (line 112)
- **ATMCI_TXBUFE** (line 130)
- **ATMCI_TXRDY** (line 119)
- **ATMCI_UNRE** (line 146)
- **ATMCI_VERSION** (line 162)
- **ATMCI_WPMR** (line 156)
- **ATMCI_WPSR** (line 159)
- **ATMCI_WP_EN** (line 157)
- **ATMCI_WP_KEY** (line 158)
- **ATMCI_XFRDONE** (line 142)
- **AUTOSUSPEND_DELAY** (line 175)
- **atmci_readl**(port,reg) (line 169)
- **atmci_set_completed**(host,event) (line 425)
- **atmci_set_pending**(host,event) (line 427)
- **atmci_test_and_clear_pending**(host,event) (line 423)
- **atmci_writel**(port,reg,value) (line 171)
