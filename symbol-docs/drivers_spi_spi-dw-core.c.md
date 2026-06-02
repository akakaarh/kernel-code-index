# drivers/spi/spi-dw-core.c

Subsystem: drivers/spi

## Functions (37)

### dw_reader
- Return type: static void
- Signature: dw_reader(struct dw_spi * dws)
- Line: 156

### dw_spi_abort
- Return type: static void
- Signature: dw_spi_abort(struct spi_controller * ctlr)
- Line: 468

### dw_spi_add_controller
- Return type: int
- Signature: dw_spi_add_controller(struct device * dev,struct dw_spi * dws)
- Line: 921

### dw_spi_adjust_mem_op_size
- Return type: static int
- Signature: dw_spi_adjust_mem_op_size(struct spi_mem * mem,struct spi_mem_op * op)
- Line: 491

### dw_spi_check_status
- Return type: int
- Signature: dw_spi_check_status(struct dw_spi * dws,bool raw)
- Line: 177

### dw_spi_cleanup
- Return type: static void
- Signature: dw_spi_cleanup(struct spi_device * spi)
- Line: 825

### dw_spi_ctlr_busy
- Return type: static bool
- Signature: dw_spi_ctlr_busy(struct dw_spi * dws)
- Line: 625

### dw_spi_debugfs_init
- Return type: static void
- Signature: dw_spi_debugfs_init(struct dw_spi * dws)
- Line: 81

### dw_spi_debugfs_init
- Return type: static void
- Signature: dw_spi_debugfs_init(struct dw_spi * dws)
- Line: 62

### dw_spi_debugfs_remove
- Return type: static void
- Signature: dw_spi_debugfs_remove(struct dw_spi * dws)
- Line: 85

### dw_spi_debugfs_remove
- Return type: static void
- Signature: dw_spi_debugfs_remove(struct dw_spi * dws)
- Line: 75

### dw_spi_exec_mem_op
- Return type: static int
- Signature: dw_spi_exec_mem_op(struct spi_mem * mem,const struct spi_mem_op * op)
- Line: 675

### dw_spi_free_mem_buf
- Return type: static void
- Signature: dw_spi_free_mem_buf(struct dw_spi * dws)
- Line: 559

### dw_spi_handle_err
- Return type: static void
- Signature: dw_spi_handle_err(struct spi_controller * ctlr,struct spi_message * msg)
- Line: 478

### dw_spi_hw_init
- Return type: static void
- Signature: dw_spi_hw_init(struct device * dev,struct dw_spi * dws)
- Line: 834

### dw_spi_init_mem_buf
- Return type: static int
- Signature: dw_spi_init_mem_buf(struct dw_spi * dws,const struct spi_mem_op * op)
- Line: 509

### dw_spi_init_mem_ops
- Return type: static void
- Signature: dw_spi_init_mem_ops(struct dw_spi * dws)
- Line: 776

### dw_spi_irq
- Return type: static irqreturn_t
- Signature: dw_spi_irq(int irq,void * dev_id)
- Line: 251

### dw_spi_irq_setup
- Return type: static void
- Signature: dw_spi_irq_setup(struct dw_spi * dws)
- Line: 359

### dw_spi_poll_transfer
- Return type: static int
- Signature: dw_spi_poll_transfer(struct dw_spi * dws,struct spi_transfer * transfer)
- Line: 390

### dw_spi_prepare_cr0
- Return type: static u32
- Signature: dw_spi_prepare_cr0(struct dw_spi * dws,struct spi_device * spi)
- Line: 268

### dw_spi_remove_controller
- Return type: void
- Signature: dw_spi_remove_controller(struct dw_spi * dws)
- Line: 1023

### dw_spi_resume_controller
- Return type: int
- Signature: dw_spi_resume_controller(struct dw_spi * dws)
- Line: 1051

### dw_spi_rx_max
- Return type: static u32
- Signature: dw_spi_rx_max(struct dw_spi * dws)
- Line: 130

### dw_spi_set_cs
- Return type: void
- Signature: dw_spi_set_cs(struct spi_device * spi,bool enable)
- Line: 90

### dw_spi_setup
- Return type: static int
- Signature: dw_spi_setup(struct spi_device * spi)
- Line: 789

### dw_spi_stop_mem_op
- Return type: static void
- Signature: dw_spi_stop_mem_op(struct dw_spi * dws,struct spi_device * spi)
- Line: 660

### dw_spi_supports_mem_op
- Return type: static bool
- Signature: dw_spi_supports_mem_op(struct spi_mem * mem,const struct spi_mem_op * op)
- Line: 499

### dw_spi_suspend_controller
- Return type: int
- Signature: dw_spi_suspend_controller(struct dw_spi * dws)
- Line: 1038

### dw_spi_target_abort
- Return type: static int
- Signature: dw_spi_target_abort(struct spi_controller * ctlr)
- Line: 484

### dw_spi_transfer_handler
- Return type: static irqreturn_t
- Signature: dw_spi_transfer_handler(struct dw_spi * dws)
- Line: 213

### dw_spi_transfer_one
- Return type: static int
- Signature: dw_spi_transfer_one(struct spi_controller * ctlr,struct spi_device * spi,struct spi_transfer * transfer)
- Line: 416

### dw_spi_tx_max
- Return type: static u32
- Signature: dw_spi_tx_max(struct dw_spi * dws)
- Line: 110

### dw_spi_update_config
- Return type: void
- Signature: dw_spi_update_config(struct dw_spi * dws,struct spi_device * spi,struct dw_spi_cfg * cfg)
- Line: 315

### dw_spi_wait_mem_op_done
- Return type: static int
- Signature: dw_spi_wait_mem_op_done(struct dw_spi * dws)
- Line: 630

### dw_spi_write_then_read
- Return type: static int
- Signature: dw_spi_write_then_read(struct dw_spi * dws,struct spi_device * spi)
- Line: 565

### dw_writer
- Return type: static void
- Signature: dw_writer(struct dw_spi * dws)
- Line: 135

## Structs (1)

### dw_spi_chip_data
- Line: 30
- Members:
  - cr0: u32
  - rx_sample_dly: u32

## Variables (2)

- static **dw_spi_dbgfs_regs** : const struct debugfs_reg32[] (line 43)
- static **dw_spi_mem_caps** : const struct spi_controller_mem_caps (line 917)

## Macros (1)

- **DW_SPI_DBGFS_REG**(_name,_off) (line 37)
