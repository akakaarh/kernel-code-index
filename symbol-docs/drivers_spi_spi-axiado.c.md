# drivers/spi/spi-axiado.c

Subsystem: drivers/spi

## Functions (26)

### ax_prepare_message
- Return type: static int
- Signature: ax_prepare_message(struct spi_controller * ctlr,struct spi_message * msg)
- Line: 380

### ax_prepare_transfer_hardware
- Return type: static int
- Signature: ax_prepare_transfer_hardware(struct spi_controller * ctlr)
- Line: 463

### ax_spi_chipselect
- Return type: static void
- Signature: ax_spi_chipselect(struct spi_device * spi,bool is_high)
- Line: 107

### ax_spi_config_clock_freq
- Return type: static void
- Signature: ax_spi_config_clock_freq(struct spi_device * spi,struct spi_transfer * transfer)
- Line: 160

### ax_spi_config_clock_mode
- Return type: static void
- Signature: ax_spi_config_clock_mode(struct spi_device * spi)
- Line: 126

### ax_spi_detect_fifo_depth
- Return type: static void
- Signature: ax_spi_detect_fifo_depth(struct ax_spi * xspi)
- Line: 509

### ax_spi_fill_tx_fifo
- Return type: static void
- Signature: ax_spi_fill_tx_fifo(struct ax_spi * xspi)
- Line: 194

### ax_spi_get_rx_byte
- Return type: static u8
- Signature: ax_spi_get_rx_byte(struct ax_spi * xspi)
- Line: 532

### ax_spi_get_rx_byte_for_irq
- Return type: static u8
- Signature: ax_spi_get_rx_byte_for_irq(struct ax_spi * xspi)
- Line: 226

### ax_spi_init_hw
- Return type: static void
- Signature: ax_spi_init_hw(struct ax_spi * xspi)
- Line: 70

### ax_spi_irq
- Return type: static irqreturn_t
- Signature: ax_spi_irq(int irq,void * dev_id)
- Line: 327

### ax_spi_mem_adjust_op_size
- Return type: static int
- Signature: ax_spi_mem_adjust_op_size(struct spi_mem * mem,struct spi_mem_op * op)
- Line: 699

### ax_spi_mem_exec_op
- Return type: static int
- Signature: ax_spi_mem_exec_op(struct spi_mem * mem,const struct spi_mem_op * op)
- Line: 554

### ax_spi_probe
- Return type: static int
- Signature: ax_spi_probe(struct platform_device * pdev)
- Line: 752

### ax_spi_process_rx_and_finalize
- Return type: static bool
- Signature: ax_spi_process_rx_and_finalize(struct spi_controller * ctlr)
- Line: 253

### ax_spi_read
- Return type: static u32
- Signature: ax_spi_read(struct ax_spi * xspi,u32 offset)
- Line: 31

### ax_spi_remove
- Return type: static void
- Signature: ax_spi_remove(struct platform_device * pdev)
- Line: 878

### ax_spi_resume
- Return type: static int __maybe_unused
- Signature: ax_spi_resume(struct device * dev)
- Line: 920

### ax_spi_runtime_resume
- Return type: static int __maybe_unused
- Signature: ax_spi_runtime_resume(struct device * dev)
- Line: 937

### ax_spi_runtime_suspend
- Return type: static int __maybe_unused
- Signature: ax_spi_runtime_suspend(struct device * dev)
- Line: 966

### ax_spi_setup_transfer
- Return type: static void
- Signature: ax_spi_setup_transfer(struct spi_device * spi,struct spi_transfer * transfer)
- Line: 178

### ax_spi_suspend
- Return type: static int __maybe_unused
- Signature: ax_spi_suspend(struct device * dev)
- Line: 905

### ax_spi_write
- Return type: static void
- Signature: ax_spi_write(struct ax_spi * xspi,u32 offset,u32 val)
- Line: 42

### ax_spi_write_b
- Return type: static void
- Signature: ax_spi_write_b(struct ax_spi * xspi,u32 offset,u8 val)
- Line: 53

### ax_transfer_one
- Return type: static int
- Signature: ax_transfer_one(struct spi_controller * ctlr,struct spi_device * spi,struct spi_transfer * transfer)
- Line: 399

### ax_unprepare_transfer_hardware
- Return type: static int
- Signature: ax_unprepare_transfer_hardware(struct spi_controller * ctlr)
- Line: 486

## Variables (4)

- static **ax_spi_dev_pm_ops** : const struct dev_pm_ops (line 977)
- static **ax_spi_driver** : platform_driver (line 990)
- static **ax_spi_mem_ops** : const struct spi_controller_mem_ops (line 739)
- static **ax_spi_of_match** : const struct of_device_id[] (line 983)
