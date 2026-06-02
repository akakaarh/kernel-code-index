# drivers/spi/spi-orion.c

Subsystem: drivers/spi

## Functions (19)

### orion_spi_50mhz_ac_timing_erratum
- Return type: static void
- Signature: orion_spi_50mhz_ac_timing_erratum(struct spi_device * spi,unsigned int speed)
- Line: 255

### orion_spi_baudrate_set
- Return type: static int
- Signature: orion_spi_baudrate_set(struct spi_device * spi,unsigned int speed)
- Line: 135

### orion_spi_clrbits
- Return type: static void
- Signature: orion_spi_clrbits(struct orion_spi * orion_spi,u32 reg,u32 mask)
- Line: 125

### orion_spi_mode_set
- Return type: static void
- Signature: orion_spi_mode_set(struct spi_device * spi)
- Line: 233

### orion_spi_probe
- Return type: static int
- Signature: orion_spi_probe(struct platform_device * pdev)
- Line: 644

### orion_spi_remove
- Return type: static void
- Signature: orion_spi_remove(struct platform_device * pdev)
- Line: 805

### orion_spi_reset
- Return type: static int
- Signature: orion_spi_reset(struct orion_spi * orion_spi)
- Line: 566

### orion_spi_runtime_resume
- Return type: static int
- Signature: orion_spi_runtime_resume(struct device * dev)
- Line: 838

### orion_spi_runtime_suspend
- Return type: static int
- Signature: orion_spi_runtime_suspend(struct device * dev)
- Line: 828

### orion_spi_set_cs
- Return type: static void
- Signature: orion_spi_set_cs(struct spi_device * spi,bool enable)
- Line: 327

### orion_spi_setbits
- Return type: static void
- Signature: orion_spi_setbits(struct orion_spi * orion_spi,u32 reg,u32 mask)
- Line: 114

### orion_spi_setup
- Return type: static int
- Signature: orion_spi_setup(struct spi_device * spi)
- Line: 547

### orion_spi_setup_transfer
- Return type: static int
- Signature: orion_spi_setup_transfer(struct spi_device * spi,struct spi_transfer * t)
- Line: 293

### orion_spi_transfer_one
- Return type: static int
- Signature: orion_spi_transfer_one(struct spi_controller * host,struct spi_device * spi,struct spi_transfer * t)
- Line: 531

### orion_spi_wait_till_ready
- Return type: static int
- Signature: orion_spi_wait_till_ready(struct orion_spi * orion_spi)
- Line: 367

### orion_spi_write_read
- Return type: static unsigned int
- Signature: orion_spi_write_read(struct spi_device * spi,struct spi_transfer * xfer)
- Line: 467

### orion_spi_write_read_16bit
- Return type: static int
- Signature: orion_spi_write_read_16bit(struct spi_device * spi,const u16 ** tx_buf,u16 ** rx_buf)
- Line: 431

### orion_spi_write_read_8bit
- Return type: static int
- Signature: orion_spi_write_read_8bit(struct spi_device * spi,const u8 ** tx_buf,u8 ** rx_buf)
- Line: 382

### spi_reg
- Return type: static void __iomem *
- Signature: spi_reg(struct orion_spi * orion_spi,u32 reg)
- Line: 108

## Structs (4)

### orion_child_options
- Line: 88
- Members:
  - typ: orion_spi_type
  - max_hz: unsigned long
  - min_divisor: unsigned int
  - max_divisor: unsigned int
  - prescale_mask: u32
  - is_errata_50mhz_ac: bool
  - vaddr: void __iomem *
  - size: u32
  - direct_access: orion_direct_acc
  - host: spi_controller *
  - base: void __iomem *
  - clk: clk *
  - axi_clk: clk *
  - devdata: const struct orion_spi_dev *
  - dev: device *
  - child: orion_child_options[]

### orion_direct_acc
- Line: 83
- Members:
  - typ: orion_spi_type
  - max_hz: unsigned long
  - min_divisor: unsigned int
  - max_divisor: unsigned int
  - prescale_mask: u32
  - is_errata_50mhz_ac: bool
  - vaddr: void __iomem *
  - size: u32
  - direct_access: orion_direct_acc
  - host: spi_controller *
  - base: void __iomem *
  - clk: clk *
  - axi_clk: clk *
  - devdata: const struct orion_spi_dev *
  - dev: device *
  - child: orion_child_options[]

### orion_spi
- Line: 92
- Members:
  - typ: orion_spi_type
  - max_hz: unsigned long
  - min_divisor: unsigned int
  - max_divisor: unsigned int
  - prescale_mask: u32
  - is_errata_50mhz_ac: bool
  - vaddr: void __iomem *
  - size: u32
  - direct_access: orion_direct_acc
  - host: spi_controller *
  - base: void __iomem *
  - clk: clk *
  - axi_clk: clk *
  - devdata: const struct orion_spi_dev *
  - dev: device *
  - child: orion_child_options[]

### orion_spi_dev
- Line: 69
- Members:
  - typ: orion_spi_type
  - max_hz: unsigned long
  - min_divisor: unsigned int
  - max_divisor: unsigned int
  - prescale_mask: u32
  - is_errata_50mhz_ac: bool
  - vaddr: void __iomem *
  - size: u32
  - direct_access: orion_direct_acc
  - host: spi_controller *
  - base: void __iomem *
  - clk: clk *
  - axi_clk: clk *
  - devdata: const struct orion_spi_dev *
  - dev: device *
  - child: orion_child_options[]

## Enums (1)

### orion_spi_type
- Line: 64

## Variables (8)

- static **armada_370_spi_dev_data** : const struct orion_spi_dev (line 584)
- static **armada_375_spi_dev_data** : const struct orion_spi_dev (line 599)
- static **armada_380_spi_dev_data** : const struct orion_spi_dev (line 606)
- static **armada_xp_spi_dev_data** : const struct orion_spi_dev (line 592)
- static **orion_spi_dev_data** : const struct orion_spi_dev (line 577)
- static **orion_spi_driver** : platform_driver (line 855)
- static **orion_spi_of_match_table** : const struct of_device_id[] (line 614)
- static **orion_spi_pm_ops** : const struct dev_pm_ops (line 849)

## Macros (25)

- **ARMADA_SPI_CLK_PRESCALE_MASK** (line 56)
- **DRIVER_NAME** (line 23)
- **ORION_NUM_CHIPSELECTS** (line 32)
- **ORION_SPI_CLK_PRESCALE_MASK** (line 55)
- **ORION_SPI_CS**(cs) (line 61)
- **ORION_SPI_CS_MASK** (line 59)
- **ORION_SPI_CS_SHIFT** (line 60)
- **ORION_SPI_DATA_IN_REG** (line 41)
- **ORION_SPI_DATA_OUT_REG** (line 40)
- **ORION_SPI_IF_8_16_BIT_MODE** (line 54)
- **ORION_SPI_IF_CONFIG_REG** (line 37)
- **ORION_SPI_IF_CTRL_REG** (line 36)
- **ORION_SPI_IF_RXLSBF** (line 38)
- **ORION_SPI_IF_TXLSBF** (line 39)
- **ORION_SPI_INT_CAUSE_REG** (line 42)
- **ORION_SPI_MODE_CPHA** (line 53)
- **ORION_SPI_MODE_CPOL** (line 52)
- **ORION_SPI_MODE_MASK** (line 57)
- **ORION_SPI_TIMING_PARAMS_REG** (line 43)
- **ORION_SPI_TMISO_SAMPLE_1** (line 49)
- **ORION_SPI_TMISO_SAMPLE_2** (line 50)
- **ORION_SPI_TMISO_SAMPLE_MASK** (line 48)
- **ORION_SPI_WAIT_RDY_MAX_LOOP** (line 34)
- **SPI_AUTOSUSPEND_TIMEOUT** (line 26)
- **SPI_DIRECT_WRITE_CONFIG_REG** (line 46)
