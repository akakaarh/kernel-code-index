# drivers/spi/spi-sifive.c

Subsystem: drivers/spi

## Functions (15)

### sifive_spi_init
- Return type: static void
- Signature: sifive_spi_init(struct sifive_spi * spi)
- Line: 109

### sifive_spi_irq
- Return type: static irqreturn_t
- Signature: sifive_spi_irq(int irq,void * dev_id)
- Line: 208

### sifive_spi_prep_transfer
- Return type: static int
- Signature: sifive_spi_prep_transfer(struct sifive_spi * spi,struct spi_device * device,struct spi_transfer * t)
- Line: 167

### sifive_spi_prepare_message
- Return type: static int
- Signature: sifive_spi_prepare_message(struct spi_controller * host,struct spi_message * msg)
- Line: 131

### sifive_spi_probe
- Return type: static int
- Signature: sifive_spi_probe(struct platform_device * pdev)
- Line: 292

### sifive_spi_read
- Return type: static u32
- Signature: sifive_spi_read(struct sifive_spi * spi,int offset)
- Line: 104

### sifive_spi_remove
- Return type: static void
- Signature: sifive_spi_remove(struct platform_device * pdev)
- Line: 409

### sifive_spi_resume
- Return type: static int
- Signature: sifive_spi_resume(struct device * dev)
- Line: 442

### sifive_spi_rx
- Return type: static void
- Signature: sifive_spi_rx(struct sifive_spi * spi,u8 * rx_ptr)
- Line: 246

### sifive_spi_set_cs
- Return type: static void
- Signature: sifive_spi_set_cs(struct spi_device * device,bool is_high)
- Line: 153

### sifive_spi_suspend
- Return type: static int
- Signature: sifive_spi_suspend(struct device * dev)
- Line: 424

### sifive_spi_transfer_one
- Return type: static int
- Signature: sifive_spi_transfer_one(struct spi_controller * host,struct spi_device * device,struct spi_transfer * t)
- Line: 255

### sifive_spi_tx
- Return type: static void
- Signature: sifive_spi_tx(struct sifive_spi * spi,const u8 * tx_ptr)
- Line: 238

### sifive_spi_wait
- Return type: static void
- Signature: sifive_spi_wait(struct sifive_spi * spi,u32 bit,int poll)
- Line: 223

### sifive_spi_write
- Return type: static void
- Signature: sifive_spi_write(struct sifive_spi * spi,int offset,u32 value)
- Line: 99

## Structs (1)

### sifive_spi
- Line: 91
- Members:
  - regs: void __iomem *
  - clk: clk *
  - fifo_depth: unsigned int
  - cs_inactive: u32
  - done: completion

## Variables (2)

- static **sifive_spi_driver** : platform_driver (line 468)
- static **sifive_spi_of_match** : const struct of_device_id[] (line 462)

## Macros (49)

- **SIFIVE_SPI_CSMODE_MODE_AUTO** (line 53)
- **SIFIVE_SPI_CSMODE_MODE_HOLD** (line 54)
- **SIFIVE_SPI_CSMODE_MODE_OFF** (line 55)
- **SIFIVE_SPI_DEFAULT_DEPTH** (line 22)
- **SIFIVE_SPI_DEFAULT_MAX_BITS** (line 23)
- **SIFIVE_SPI_DELAY0_CSSCK**(x) (line 58)
- **SIFIVE_SPI_DELAY0_CSSCK_MASK** (line 59)
- **SIFIVE_SPI_DELAY0_SCKCS**(x) (line 60)
- **SIFIVE_SPI_DELAY0_SCKCS_MASK** (line 61)
- **SIFIVE_SPI_DELAY1_INTERCS**(x) (line 64)
- **SIFIVE_SPI_DELAY1_INTERCS_MASK** (line 65)
- **SIFIVE_SPI_DELAY1_INTERXFR**(x) (line 66)
- **SIFIVE_SPI_DELAY1_INTERXFR_MASK** (line 67)
- **SIFIVE_SPI_DRIVER_NAME** (line 19)
- **SIFIVE_SPI_FMT_DIR** (line 75)
- **SIFIVE_SPI_FMT_ENDIAN** (line 74)
- **SIFIVE_SPI_FMT_LEN**(x) (line 76)
- **SIFIVE_SPI_FMT_LEN_MASK** (line 77)
- **SIFIVE_SPI_FMT_PROTO_DUAL** (line 71)
- **SIFIVE_SPI_FMT_PROTO_MASK** (line 73)
- **SIFIVE_SPI_FMT_PROTO_QUAD** (line 72)
- **SIFIVE_SPI_FMT_PROTO_SINGLE** (line 70)
- **SIFIVE_SPI_IP_RXWM** (line 89)
- **SIFIVE_SPI_IP_TXWM** (line 88)
- **SIFIVE_SPI_MAX_CS** (line 21)
- **SIFIVE_SPI_REG_CSDEF** (line 29)
- **SIFIVE_SPI_REG_CSID** (line 28)
- **SIFIVE_SPI_REG_CSMODE** (line 30)
- **SIFIVE_SPI_REG_DELAY0** (line 31)
- **SIFIVE_SPI_REG_DELAY1** (line 32)
- **SIFIVE_SPI_REG_FCTRL** (line 38)
- **SIFIVE_SPI_REG_FFMT** (line 39)
- **SIFIVE_SPI_REG_FMT** (line 33)
- **SIFIVE_SPI_REG_IE** (line 40)
- **SIFIVE_SPI_REG_IP** (line 41)
- **SIFIVE_SPI_REG_RXDATA** (line 35)
- **SIFIVE_SPI_REG_RXMARK** (line 37)
- **SIFIVE_SPI_REG_SCKDIV** (line 26)
- **SIFIVE_SPI_REG_SCKMODE** (line 27)
- **SIFIVE_SPI_REG_TXDATA** (line 34)
- **SIFIVE_SPI_REG_TXMARK** (line 36)
- **SIFIVE_SPI_RXDATA_DATA_MASK** (line 84)
- **SIFIVE_SPI_RXDATA_EMPTY** (line 85)
- **SIFIVE_SPI_SCKDIV_DIV_MASK** (line 44)
- **SIFIVE_SPI_SCKMODE_MODE_MASK** (line 49)
- **SIFIVE_SPI_SCKMODE_PHA** (line 47)
- **SIFIVE_SPI_SCKMODE_POL** (line 48)
- **SIFIVE_SPI_TXDATA_DATA_MASK** (line 80)
- **SIFIVE_SPI_TXDATA_FULL** (line 81)
