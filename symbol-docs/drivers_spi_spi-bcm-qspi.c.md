# drivers/spi/spi-bcm-qspi.c

Subsystem: drivers/spi

## Functions (56)

### bcm_qspi_bspi_busy_poll
- Return type: static int
- Signature: bcm_qspi_bspi_busy_poll(struct bcm_qspi * qspi)
- Line: 317

### bcm_qspi_bspi_exec_mem_op
- Return type: static int
- Signature: bcm_qspi_bspi_exec_mem_op(struct spi_device * spi,const struct spi_mem_op * op)
- Line: 1035

### bcm_qspi_bspi_flush_prefetch_buffers
- Return type: static void
- Signature: bcm_qspi_bspi_flush_prefetch_buffers(struct bcm_qspi * qspi)
- Line: 338

### bcm_qspi_bspi_init
- Return type: static void
- Signature: bcm_qspi_bspi_init(struct bcm_qspi * qspi)
- Line: 1387

### bcm_qspi_bspi_lr_clear
- Return type: static void
- Signature: bcm_qspi_bspi_lr_clear(struct bcm_qspi * qspi)
- Line: 372

### bcm_qspi_bspi_lr_data_read
- Return type: static void
- Signature: bcm_qspi_bspi_lr_data_read(struct bcm_qspi * qspi)
- Line: 379

### bcm_qspi_bspi_lr_err_l2_isr
- Return type: static irqreturn_t
- Signature: bcm_qspi_bspi_lr_err_l2_isr(int irq,void * dev_id)
- Line: 1302

### bcm_qspi_bspi_lr_is_fifo_empty
- Return type: static int
- Signature: bcm_qspi_bspi_lr_is_fifo_empty(struct bcm_qspi * qspi)
- Line: 348

### bcm_qspi_bspi_lr_l2_isr
- Return type: static irqreturn_t
- Signature: bcm_qspi_bspi_lr_l2_isr(int irq,void * dev_id)
- Line: 1265

### bcm_qspi_bspi_lr_read_fifo
- Return type: static u32
- Signature: bcm_qspi_bspi_lr_read_fifo(struct bcm_qspi * qspi)
- Line: 354

### bcm_qspi_bspi_lr_start
- Return type: static void
- Signature: bcm_qspi_bspi_lr_start(struct bcm_qspi * qspi)
- Line: 365

### bcm_qspi_bspi_set_flex_mode
- Return type: static int
- Signature: bcm_qspi_bspi_set_flex_mode(struct bcm_qspi * qspi,const struct spi_mem_op * op,int hp)
- Line: 416

### bcm_qspi_bspi_set_mode
- Return type: static int
- Signature: bcm_qspi_bspi_set_mode(struct bcm_qspi * qspi,const struct spi_mem_op * op,int hp)
- Line: 508

### bcm_qspi_bspi_set_override
- Return type: static int
- Signature: bcm_qspi_bspi_set_override(struct bcm_qspi * qspi,const struct spi_mem_op * op,int hp)
- Line: 463

### bcm_qspi_bspi_set_xfer_params
- Return type: static void
- Signature: bcm_qspi_bspi_set_xfer_params(struct bcm_qspi * qspi,u8 cmd_byte,int bpp,int bpc,int flex_mode)
- Line: 406

### bcm_qspi_bspi_ver_three
- Return type: static bool
- Signature: bcm_qspi_bspi_ver_three(struct bcm_qspi * qspi)
- Line: 331

### bcm_qspi_calc_spbr
- Return type: static u32
- Signature: bcm_qspi_calc_spbr(u32 clk_speed_hz,const struct bcm_qspi_parms * xp)
- Line: 290

### bcm_qspi_chip_select
- Return type: static void
- Signature: bcm_qspi_chip_select(struct bcm_qspi * qspi,int cs)
- Line: 583

### bcm_qspi_cleanup
- Return type: static void
- Signature: bcm_qspi_cleanup(struct spi_device * spi)
- Line: 1238

### bcm_qspi_disable_bspi
- Return type: static void
- Signature: bcm_qspi_disable_bspi(struct bcm_qspi * qspi)
- Line: 569

### bcm_qspi_enable_bspi
- Return type: static void
- Signature: bcm_qspi_enable_bspi(struct bcm_qspi * qspi)
- Line: 554

### bcm_qspi_exec_mem_op
- Return type: static int
- Signature: bcm_qspi_exec_mem_op(struct spi_mem * mem,const struct spi_mem_op * op)
- Line: 1190

### bcm_qspi_has_fastbr
- Return type: static bool
- Signature: bcm_qspi_has_fastbr(struct bcm_qspi * qspi)
- Line: 261

### bcm_qspi_has_sysclk_108
- Return type: static bool
- Signature: bcm_qspi_has_sysclk_108(struct bcm_qspi * qspi)
- Line: 272

### bcm_qspi_hw_init
- Return type: static void
- Signature: bcm_qspi_hw_init(struct bcm_qspi * qspi)
- Line: 1405

### bcm_qspi_hw_set_parms
- Return type: static void
- Signature: bcm_qspi_hw_set_parms(struct bcm_qspi * qspi,const struct bcm_qspi_parms * xp)
- Line: 611

### bcm_qspi_hw_uninit
- Return type: static void
- Signature: bcm_qspi_hw_uninit(struct bcm_qspi * qspi)
- Line: 1424

### bcm_qspi_l1_isr
- Return type: static irqreturn_t
- Signature: bcm_qspi_l1_isr(int irq,void * dev_id)
- Line: 1318

### bcm_qspi_mspi_exec_mem_op
- Return type: static int
- Signature: bcm_qspi_mspi_exec_mem_op(struct spi_device * spi,const struct spi_mem_op * op)
- Line: 1150

### bcm_qspi_mspi_l2_isr
- Return type: static irqreturn_t
- Signature: bcm_qspi_mspi_l2_isr(int irq,void * dev_id)
- Line: 1245

### bcm_qspi_mspi_transfer_is_last
- Return type: static bool
- Signature: bcm_qspi_mspi_transfer_is_last(struct bcm_qspi * qspi,struct qspi_trans * qt)
- Line: 731

### bcm_qspi_probe
- Return type: int
- Signature: bcm_qspi_probe(struct platform_device * pdev,struct bcm_qspi_soc_intc * soc_intc)
- Line: 1482

### bcm_qspi_read
- Return type: static u32
- Signature: bcm_qspi_read(struct bcm_qspi * qspi,enum base_type type,unsigned int offset)
- Line: 303

### bcm_qspi_remove
- Return type: void
- Signature: bcm_qspi_remove(struct platform_device * pdev)
- Line: 1679

### bcm_qspi_resume
- Return type: static int __maybe_unused
- Signature: bcm_qspi_resume(struct device * dev)
- Line: 1708

### bcm_qspi_setup
- Return type: static int
- Signature: bcm_qspi_setup(struct spi_device * spi)
- Line: 706

### bcm_qspi_spbr_min
- Return type: static int
- Signature: bcm_qspi_spbr_min(struct bcm_qspi * qspi)
- Line: 282

### bcm_qspi_suspend
- Return type: static int __maybe_unused
- Signature: bcm_qspi_suspend(struct device * dev)
- Line: 1692

### bcm_qspi_transfer_one
- Return type: static int
- Signature: bcm_qspi_transfer_one(struct spi_controller * host,struct spi_device * spi,struct spi_transfer * trans)
- Line: 1121

### bcm_qspi_update_parms
- Return type: static void
- Signature: bcm_qspi_update_parms(struct bcm_qspi * qspi,struct spi_device * spi,struct spi_transfer * trans)
- Line: 693

### bcm_qspi_write
- Return type: static void
- Signature: bcm_qspi_write(struct bcm_qspi * qspi,enum base_type type,unsigned int offset,unsigned int data)
- Line: 310

### bcmspi_parms_did_change
- Return type: static bool
- Signature: bcmspi_parms_did_change(const struct bcm_qspi_parms * const cur,const struct bcm_qspi_parms * const prev)
- Line: 601

### has_bspi
- Return type: static bool
- Signature: has_bspi(struct bcm_qspi * qspi)
- Line: 255

### read_cdram_slot
- Return type: static u32
- Signature: read_cdram_slot(struct bcm_qspi * qspi,int slot)
- Line: 925

### read_from_hw
- Return type: static void
- Signature: read_from_hw(struct bcm_qspi * qspi,int slots)
- Line: 824

### read_rxram_slot_u16
- Return type: static u16
- Signature: read_rxram_slot_u16(struct bcm_qspi * qspi,int slot)
- Line: 787

### read_rxram_slot_u32
- Return type: static u32
- Signature: read_rxram_slot_u32(struct bcm_qspi * qspi,int slot)
- Line: 797

### read_rxram_slot_u64
- Return type: static u64
- Signature: read_rxram_slot_u64(struct bcm_qspi * qspi,int slot)
- Line: 809

### read_rxram_slot_u8
- Return type: static u8
- Signature: read_rxram_slot_u8(struct bcm_qspi * qspi,int slot)
- Line: 779

### update_qspi_trans_byte_count
- Return type: static int
- Signature: update_qspi_trans_byte_count(struct bcm_qspi * qspi,struct qspi_trans * qt,int flags)
- Line: 741

### write_cdram_slot
- Return type: static void
- Signature: write_cdram_slot(struct bcm_qspi * qspi,int slot,u32 val)
- Line: 930

### write_to_hw
- Return type: static int
- Signature: write_to_hw(struct bcm_qspi * qspi,struct spi_device * spi)
- Line: 936

### write_txram_slot_u16
- Return type: static void
- Signature: write_txram_slot_u16(struct bcm_qspi * qspi,int slot,u16 val)
- Line: 892

### write_txram_slot_u32
- Return type: static void
- Signature: write_txram_slot_u32(struct bcm_qspi * qspi,int slot,u32 val)
- Line: 903

### write_txram_slot_u64
- Return type: static void
- Signature: write_txram_slot_u64(struct bcm_qspi * qspi,int slot,u64 val)
- Line: 912

### write_txram_slot_u8
- Return type: static void
- Signature: write_txram_slot_u8(struct bcm_qspi * qspi,int slot,u8 val)
- Line: 883

## Structs (7)

### bcm_qspi
- Line: 221
- Members:
  - speed_hz: u32
  - mode: u8
  - bits_per_word: u8
  - flex_mode: bool
  - width: unsigned int
  - addrlen: unsigned int
  - hp: unsigned int
  - irq_name: const char *
  - irq_handler: const irq_handler_t
  - irq_source: int
  - mask: u32
  - irqp: const struct bcm_qspi_irq *
  - dev: void *
  - trans: spi_transfer *
  - byte: int
  - mspi_last_trans: bool
  - pdev: platform_device *
  - host: spi_controller *
  - clk: clk *
  - base_clk: u32
  - max_speed_hz: u32
  - base: void __iomem * []
  - soc_intc: bcm_qspi_soc_intc *
  - last_parms: bcm_qspi_parms
  - trans_pos: qspi_trans
  - curr_cs: int
  - bspi_maj_rev: int
  - bspi_min_rev: int
  - bspi_enabled: int
  - bspi_rf_op: const struct spi_mem_op *
  - bspi_rf_op_idx: u32
  - bspi_rf_op_len: u32
  - bspi_rf_op_status: u32
  - xfer_mode: bcm_xfer_mode
  - s3_strap_override_ctrl: u32
  - bspi_mode: bool
  - big_endian: bool
  - num_irqs: int
  - dev_ids: bcm_qspi_dev_id *
  - mspi_done: completion
  - bspi_done: completion
  - mspi_maj_rev: u8
  - mspi_min_rev: u8
  - mspi_spcr3_sysclk: bool
  - has_mspi_rev: bool
  - has_spcr3_sysclk: bool

### bcm_qspi_data
- Line: 1440
- Members:
  - speed_hz: u32
  - mode: u8
  - bits_per_word: u8
  - flex_mode: bool
  - width: unsigned int
  - addrlen: unsigned int
  - hp: unsigned int
  - irq_name: const char *
  - irq_handler: const irq_handler_t
  - irq_source: int
  - mask: u32
  - irqp: const struct bcm_qspi_irq *
  - dev: void *
  - trans: spi_transfer *
  - byte: int
  - mspi_last_trans: bool
  - pdev: platform_device *
  - host: spi_controller *
  - clk: clk *
  - base_clk: u32
  - max_speed_hz: u32
  - base: void __iomem * []
  - soc_intc: bcm_qspi_soc_intc *
  - last_parms: bcm_qspi_parms
  - trans_pos: qspi_trans
  - curr_cs: int
  - bspi_maj_rev: int
  - bspi_min_rev: int
  - bspi_enabled: int
  - bspi_rf_op: const struct spi_mem_op *
  - bspi_rf_op_idx: u32
  - bspi_rf_op_len: u32
  - bspi_rf_op_status: u32
  - xfer_mode: bcm_xfer_mode
  - s3_strap_override_ctrl: u32
  - bspi_mode: bool
  - big_endian: bool
  - num_irqs: int
  - dev_ids: bcm_qspi_dev_id *
  - mspi_done: completion
  - bspi_done: completion
  - mspi_maj_rev: u8
  - mspi_min_rev: u8
  - mspi_spcr3_sysclk: bool
  - has_mspi_rev: bool
  - has_spcr3_sysclk: bool

### bcm_qspi_dev_id
- Line: 209
- Members:
  - speed_hz: u32
  - mode: u8
  - bits_per_word: u8
  - flex_mode: bool
  - width: unsigned int
  - addrlen: unsigned int
  - hp: unsigned int
  - irq_name: const char *
  - irq_handler: const irq_handler_t
  - irq_source: int
  - mask: u32
  - irqp: const struct bcm_qspi_irq *
  - dev: void *
  - trans: spi_transfer *
  - byte: int
  - mspi_last_trans: bool
  - pdev: platform_device *
  - host: spi_controller *
  - clk: clk *
  - base_clk: u32
  - max_speed_hz: u32
  - base: void __iomem * []
  - soc_intc: bcm_qspi_soc_intc *
  - last_parms: bcm_qspi_parms
  - trans_pos: qspi_trans
  - curr_cs: int
  - bspi_maj_rev: int
  - bspi_min_rev: int
  - bspi_enabled: int
  - bspi_rf_op: const struct spi_mem_op *
  - bspi_rf_op_idx: u32
  - bspi_rf_op_len: u32
  - bspi_rf_op_status: u32
  - xfer_mode: bcm_xfer_mode
  - s3_strap_override_ctrl: u32
  - bspi_mode: bool
  - big_endian: bool
  - num_irqs: int
  - dev_ids: bcm_qspi_dev_id *
  - mspi_done: completion
  - bspi_done: completion
  - mspi_maj_rev: u8
  - mspi_min_rev: u8
  - mspi_spcr3_sysclk: bool
  - has_mspi_rev: bool
  - has_spcr3_sysclk: bool

### bcm_qspi_irq
- Line: 202
- Members:
  - speed_hz: u32
  - mode: u8
  - bits_per_word: u8
  - flex_mode: bool
  - width: unsigned int
  - addrlen: unsigned int
  - hp: unsigned int
  - irq_name: const char *
  - irq_handler: const irq_handler_t
  - irq_source: int
  - mask: u32
  - irqp: const struct bcm_qspi_irq *
  - dev: void *
  - trans: spi_transfer *
  - byte: int
  - mspi_last_trans: bool
  - pdev: platform_device *
  - host: spi_controller *
  - clk: clk *
  - base_clk: u32
  - max_speed_hz: u32
  - base: void __iomem * []
  - soc_intc: bcm_qspi_soc_intc *
  - last_parms: bcm_qspi_parms
  - trans_pos: qspi_trans
  - curr_cs: int
  - bspi_maj_rev: int
  - bspi_min_rev: int
  - bspi_enabled: int
  - bspi_rf_op: const struct spi_mem_op *
  - bspi_rf_op_idx: u32
  - bspi_rf_op_len: u32
  - bspi_rf_op_status: u32
  - xfer_mode: bcm_xfer_mode
  - s3_strap_override_ctrl: u32
  - bspi_mode: bool
  - big_endian: bool
  - num_irqs: int
  - dev_ids: bcm_qspi_dev_id *
  - mspi_done: completion
  - bspi_done: completion
  - mspi_maj_rev: u8
  - mspi_min_rev: u8
  - mspi_spcr3_sysclk: bool
  - has_mspi_rev: bool
  - has_spcr3_sysclk: bool

### bcm_qspi_parms
- Line: 177
- Members:
  - speed_hz: u32
  - mode: u8
  - bits_per_word: u8
  - flex_mode: bool
  - width: unsigned int
  - addrlen: unsigned int
  - hp: unsigned int
  - irq_name: const char *
  - irq_handler: const irq_handler_t
  - irq_source: int
  - mask: u32
  - irqp: const struct bcm_qspi_irq *
  - dev: void *
  - trans: spi_transfer *
  - byte: int
  - mspi_last_trans: bool
  - pdev: platform_device *
  - host: spi_controller *
  - clk: clk *
  - base_clk: u32
  - max_speed_hz: u32
  - base: void __iomem * []
  - soc_intc: bcm_qspi_soc_intc *
  - last_parms: bcm_qspi_parms
  - trans_pos: qspi_trans
  - curr_cs: int
  - bspi_maj_rev: int
  - bspi_min_rev: int
  - bspi_enabled: int
  - bspi_rf_op: const struct spi_mem_op *
  - bspi_rf_op_idx: u32
  - bspi_rf_op_len: u32
  - bspi_rf_op_status: u32
  - xfer_mode: bcm_xfer_mode
  - s3_strap_override_ctrl: u32
  - bspi_mode: bool
  - big_endian: bool
  - num_irqs: int
  - dev_ids: bcm_qspi_dev_id *
  - mspi_done: completion
  - bspi_done: completion
  - mspi_maj_rev: u8
  - mspi_min_rev: u8
  - mspi_spcr3_sysclk: bool
  - has_mspi_rev: bool
  - has_spcr3_sysclk: bool

### bcm_xfer_mode
- Line: 183
- Members:
  - speed_hz: u32
  - mode: u8
  - bits_per_word: u8
  - flex_mode: bool
  - width: unsigned int
  - addrlen: unsigned int
  - hp: unsigned int
  - irq_name: const char *
  - irq_handler: const irq_handler_t
  - irq_source: int
  - mask: u32
  - irqp: const struct bcm_qspi_irq *
  - dev: void *
  - trans: spi_transfer *
  - byte: int
  - mspi_last_trans: bool
  - pdev: platform_device *
  - host: spi_controller *
  - clk: clk *
  - base_clk: u32
  - max_speed_hz: u32
  - base: void __iomem * []
  - soc_intc: bcm_qspi_soc_intc *
  - last_parms: bcm_qspi_parms
  - trans_pos: qspi_trans
  - curr_cs: int
  - bspi_maj_rev: int
  - bspi_min_rev: int
  - bspi_enabled: int
  - bspi_rf_op: const struct spi_mem_op *
  - bspi_rf_op_idx: u32
  - bspi_rf_op_len: u32
  - bspi_rf_op_status: u32
  - xfer_mode: bcm_xfer_mode
  - s3_strap_override_ctrl: u32
  - bspi_mode: bool
  - big_endian: bool
  - num_irqs: int
  - dev_ids: bcm_qspi_dev_id *
  - mspi_done: completion
  - bspi_done: completion
  - mspi_maj_rev: u8
  - mspi_min_rev: u8
  - mspi_spcr3_sysclk: bool
  - has_mspi_rev: bool
  - has_spcr3_sysclk: bool

### qspi_trans
- Line: 215
- Members:
  - speed_hz: u32
  - mode: u8
  - bits_per_word: u8
  - flex_mode: bool
  - width: unsigned int
  - addrlen: unsigned int
  - hp: unsigned int
  - irq_name: const char *
  - irq_handler: const irq_handler_t
  - irq_source: int
  - mask: u32
  - irqp: const struct bcm_qspi_irq *
  - dev: void *
  - trans: spi_transfer *
  - byte: int
  - mspi_last_trans: bool
  - pdev: platform_device *
  - host: spi_controller *
  - clk: clk *
  - base_clk: u32
  - max_speed_hz: u32
  - base: void __iomem * []
  - soc_intc: bcm_qspi_soc_intc *
  - last_parms: bcm_qspi_parms
  - trans_pos: qspi_trans
  - curr_cs: int
  - bspi_maj_rev: int
  - bspi_min_rev: int
  - bspi_enabled: int
  - bspi_rf_op: const struct spi_mem_op *
  - bspi_rf_op_idx: u32
  - bspi_rf_op_len: u32
  - bspi_rf_op_status: u32
  - xfer_mode: bcm_xfer_mode
  - s3_strap_override_ctrl: u32
  - bspi_mode: bool
  - big_endian: bool
  - num_irqs: int
  - dev_ids: bcm_qspi_dev_id *
  - mspi_done: completion
  - bspi_done: completion
  - mspi_maj_rev: u8
  - mspi_min_rev: u8
  - mspi_spcr3_sysclk: bool
  - has_mspi_rev: bool
  - has_spcr3_sysclk: bool

## Enums (2)

### base_type
- Line: 190

### irq_source
- Line: 197

## Variables (6)

- static **bcm_qspi_mem_ops** : const struct spi_controller_mem_ops (line 1436)
- static **bcm_qspi_no_rev_data** : const struct bcm_qspi_data (line 1445)
- static **bcm_qspi_of_match** : const struct of_device_id[]__maybe_unused (line 1460)
- static **bcm_qspi_rev_data** : const struct bcm_qspi_data (line 1450)
- static **bcm_qspi_spcr3_data** : const struct bcm_qspi_data (line 1455)
- static **qspi_irq_tab** : const struct bcm_qspi_irq[] (line 1339)

## Macros (103)

- **ADDR_4MB_MASK** (line 147)
- **BSPI_ADDRLEN_3BYTES** (line 70)
- **BSPI_ADDRLEN_4BYTES** (line 71)
- **BSPI_B0_CTRL** (line 37)
- **BSPI_B0_STATUS** (line 36)
- **BSPI_B1_CTRL** (line 39)
- **BSPI_B1_STATUS** (line 38)
- **BSPI_BITS_PER_CYCLE** (line 42)
- **BSPI_BITS_PER_PHASE** (line 43)
- **BSPI_BPP_ADDR_SELECT_MASK** (line 79)
- **BSPI_BPP_MODE_SELECT_MASK** (line 78)
- **BSPI_BSPI_FLASH_UPPER_ADDR_BYTE** (line 45)
- **BSPI_BSPI_PIO_DATA** (line 50)
- **BSPI_BSPI_PIO_IODIR** (line 49)
- **BSPI_BSPI_PIO_MODE_ENABLE** (line 48)
- **BSPI_BSPI_XOR_ENABLE** (line 47)
- **BSPI_BSPI_XOR_VALUE** (line 46)
- **BSPI_BUSY_STATUS** (line 34)
- **BSPI_CMD_AND_MODE_BYTE** (line 44)
- **BSPI_FLEX_MODE_ENABLE** (line 41)
- **BSPI_INTR_STATUS** (line 35)
- **BSPI_MAST_N_BOOT_CTRL** (line 33)
- **BSPI_RAF_CTRL** (line 55)
- **BSPI_RAF_CTRL_CLEAR_MASK** (line 76)
- **BSPI_RAF_CTRL_START_MASK** (line 75)
- **BSPI_RAF_CURR_ADDR** (line 61)
- **BSPI_RAF_FULLNESS** (line 56)
- **BSPI_RAF_NUM_WORDS** (line 54)
- **BSPI_RAF_READ_DATA** (line 59)
- **BSPI_RAF_START_ADDR** (line 53)
- **BSPI_RAF_STATUS** (line 58)
- **BSPI_RAF_STATUS_FIFO_EMPTY_MASK** (line 73)
- **BSPI_RAF_WATERMARK** (line 57)
- **BSPI_RAF_WORD_CNT** (line 60)
- **BSPI_READ_LENGTH** (line 81)
- **BSPI_REVISION_ID** (line 31)
- **BSPI_SCRATCH** (line 32)
- **BSPI_STRAP_OVERRIDE_CTRL** (line 40)
- **BSPI_STRAP_OVERRIDE_CTRL_ADDR_4BYTE** (line 66)
- **BSPI_STRAP_OVERRIDE_CTRL_DATA_DUAL** (line 65)
- **BSPI_STRAP_OVERRIDE_CTRL_DATA_QUAD** (line 67)
- **BSPI_STRAP_OVERRIDE_CTRL_ENDAIN_MODE** (line 68)
- **BSPI_STRAP_OVERRIDE_CTRL_OVERRIDE** (line 64)
- **DRIVER_NAME** (line 27)
- **INTR_BASE_BIT_SHIFT** (line 133)
- **INTR_COUNT** (line 134)
- **MAX_CMD_SIZE** (line 145)
- **MSPI_BASE_FREQ** (line 138)
- **MSPI_CDRAM** (line 100)
- **MSPI_CDRAM_BITSE_BIT** (line 108)
- **MSPI_CDRAM_CONT_BIT** (line 107)
- **MSPI_CDRAM_DT_BIT** (line 109)
- **MSPI_CDRAM_OUTP** (line 106)
- **MSPI_CDRAM_PCS** (line 110)
- **MSPI_CPTQP** (line 95)
- **MSPI_ENDQP** (line 92)
- **MSPI_MASTER_BIT** (line 103)
- **MSPI_MSPI_STATUS** (line 94)
- **MSPI_MSPI_STATUS_SPIF** (line 131)
- **MSPI_NEWQP** (line 91)
- **MSPI_NUM_CDRAM** (line 105)
- **MSPI_REV** (line 97)
- **MSPI_RXRAM** (line 99)
- **MSPI_SPCR0_LSB** (line 84)
- **MSPI_SPCR0_MSB** (line 85)
- **MSPI_SPCR0_MSB_BITS_SHIFT** (line 88)
- **MSPI_SPCR0_MSB_CPHA** (line 86)
- **MSPI_SPCR0_MSB_CPOL** (line 87)
- **MSPI_SPCR1_LSB** (line 89)
- **MSPI_SPCR1_MSB** (line 90)
- **MSPI_SPCR2** (line 93)
- **MSPI_SPCR2_CONT_AFTER_CMD** (line 113)
- **MSPI_SPCR2_SPE** (line 112)
- **MSPI_SPCR3** (line 96)
- **MSPI_SPCR3_CPHARX** (line 129)
- **MSPI_SPCR3_DAM_16BYTE** (line 124)
- **MSPI_SPCR3_DAM_32BYTE** (line 125)
- **MSPI_SPCR3_DAM_8BYTE** (line 123)
- **MSPI_SPCR3_DATA_REG_SZ** (line 128)
- **MSPI_SPCR3_FASTBR** (line 115)
- **MSPI_SPCR3_FASTDT** (line 116)
- **MSPI_SPCR3_HALFDUPLEX** (line 126)
- **MSPI_SPCR3_HDOUTTYPE** (line 127)
- **MSPI_SPCR3_SYSCLKSEL_108** (line 120)
- **MSPI_SPCR3_SYSCLKSEL_27** (line 118)
- **MSPI_SPCR3_SYSCLKSEL_MASK** (line 117)
- **MSPI_SPCR3_TXRXDAM_MASK** (line 122)
- **MSPI_TXRAM** (line 98)
- **MSPI_WRITE_LOCK** (line 101)
- **NUM_CHIPSELECT** (line 136)
- **OPCODE_DIOR** (line 140)
- **OPCODE_DIOR_4B** (line 142)
- **OPCODE_QIOR** (line 141)
- **OPCODE_QIOR_4B** (line 143)
- **QSPI_SPBR_MAX** (line 137)
- **TRANS_STATUS_BREAK_CS_CHANGE** (line 156)
- **TRANS_STATUS_BREAK_DELAY** (line 154)
- **TRANS_STATUS_BREAK_DESELECT** (line 166)
- **TRANS_STATUS_BREAK_EOM** (line 152)
- **TRANS_STATUS_BREAK_NONE** (line 150)
- **TRANS_STATUS_BREAK_NO_BYTES** (line 158)
- **TRANS_STATUS_BREAK_TX** (line 161)
- **swap4bytes**(__val) (line 173)
