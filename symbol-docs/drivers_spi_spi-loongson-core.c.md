# drivers/spi/spi-loongson-core.c

Subsystem: drivers/spi

## Functions (16)

### loongson_spi_init_controller
- Return type: int
- Signature: loongson_spi_init_controller(struct device * dev,void __iomem * regs)
- Line: 196

### loongson_spi_prepare_message
- Return type: static int
- Signature: loongson_spi_prepare_message(struct spi_controller * ctlr,struct spi_message * m)
- Line: 148

### loongson_spi_read_reg
- Return type: static char
- Signature: loongson_spi_read_reg(struct loongson_spi * spi,unsigned char reg)
- Line: 25

### loongson_spi_reginit
- Return type: static void
- Signature: loongson_spi_reginit(struct loongson_spi * loongson_spi_dev)
- Line: 180

### loongson_spi_resume
- Return type: static int __maybe_unused
- Signature: loongson_spi_resume(struct device * dev)
- Line: 252

### loongson_spi_set_clk
- Return type: static void
- Signature: loongson_spi_set_clk(struct loongson_spi * loongson_spi,unsigned int hz)
- Line: 41

### loongson_spi_set_cs
- Return type: static void
- Signature: loongson_spi_set_cs(struct spi_device * spi,bool en)
- Line: 30

### loongson_spi_set_mode
- Return type: static void
- Signature: loongson_spi_set_mode(struct loongson_spi * loongson_spi,struct spi_device * spi)
- Line: 62

### loongson_spi_setup
- Return type: static int
- Signature: loongson_spi_setup(struct spi_device * spi)
- Line: 90

### loongson_spi_suspend
- Return type: static int __maybe_unused
- Signature: loongson_spi_suspend(struct device * dev)
- Line: 232

### loongson_spi_transfer_one
- Return type: static int
- Signature: loongson_spi_transfer_one(struct spi_controller * ctrl,struct spi_device * spi,struct spi_transfer * xfer)
- Line: 159

### loongson_spi_unprepare_message
- Return type: static int
- Signature: loongson_spi_unprepare_message(struct spi_controller * ctrl,struct spi_message * m)
- Line: 171

### loongson_spi_update_state
- Return type: static int
- Signature: loongson_spi_update_state(struct loongson_spi * loongson_spi,struct spi_device * spi,struct spi_transfer * t)
- Line: 78

### loongson_spi_write_read
- Return type: static int
- Signature: loongson_spi_write_read(struct spi_device * spi,struct spi_transfer * xfer)
- Line: 131

### loongson_spi_write_read_8bit
- Return type: static int
- Signature: loongson_spi_write_read_8bit(struct spi_device * spi,const u8 ** tx_buf,u8 ** rx_buf,unsigned int num)
- Line: 107

### loongson_spi_write_reg
- Return type: static void
- Signature: loongson_spi_write_reg(struct loongson_spi * spi,unsigned char reg,unsigned char data)
- Line: 19

## Variables (1)

- **loongson_spi_dev_pm_ops** : const struct dev_pm_ops (line 272)
