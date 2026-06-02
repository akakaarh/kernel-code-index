# drivers/spi/spi-altera-core.c

Subsystem: drivers/spi

## Functions (9)

### altera_spi_init_host
- Return type: void
- Signature: altera_spi_init_host(struct spi_controller * host)
- Line: 204

### altera_spi_irq
- Return type: irqreturn_t
- Signature: altera_spi_irq(int irq,void * dev)
- Line: 183

### altera_spi_rx_word
- Return type: static void
- Signature: altera_spi_rx_word(struct altera_spi * hw)
- Line: 115

### altera_spi_set_cs
- Return type: static void
- Signature: altera_spi_set_cs(struct spi_device * spi,bool is_high)
- Line: 73

### altera_spi_to_hw
- Return type: static altera_spi *
- Signature: altera_spi_to_hw(struct spi_device * sdev)
- Line: 68

### altera_spi_tx_word
- Return type: static void
- Signature: altera_spi_tx_word(struct altera_spi * hw)
- Line: 89

### altera_spi_txrx
- Return type: static int
- Signature: altera_spi_txrx(struct spi_controller * host,struct spi_device * spi,struct spi_transfer * t)
- Line: 142

### altr_spi_readl
- Return type: static int
- Signature: altr_spi_readl(struct altera_spi * hw,unsigned int reg,unsigned int * val)
- Line: 56

### altr_spi_writel
- Return type: static int
- Signature: altr_spi_writel(struct altera_spi * hw,unsigned int reg,unsigned int val)
- Line: 43

## Macros (18)

- **ALTERA_SPI_CONTROL** (line 26)
- **ALTERA_SPI_CONTROL_IE_MSK** (line 40)
- **ALTERA_SPI_CONTROL_IROE_MSK** (line 36)
- **ALTERA_SPI_CONTROL_IRRDY_MSK** (line 39)
- **ALTERA_SPI_CONTROL_ITOE_MSK** (line 37)
- **ALTERA_SPI_CONTROL_ITRDY_MSK** (line 38)
- **ALTERA_SPI_CONTROL_SSO_MSK** (line 41)
- **ALTERA_SPI_RXDATA** (line 23)
- **ALTERA_SPI_STATUS** (line 25)
- **ALTERA_SPI_STATUS_E_MSK** (line 34)
- **ALTERA_SPI_STATUS_ROE_MSK** (line 29)
- **ALTERA_SPI_STATUS_RRDY_MSK** (line 33)
- **ALTERA_SPI_STATUS_TMT_MSK** (line 31)
- **ALTERA_SPI_STATUS_TOE_MSK** (line 30)
- **ALTERA_SPI_STATUS_TRDY_MSK** (line 32)
- **ALTERA_SPI_TARGET_SEL** (line 27)
- **ALTERA_SPI_TXDATA** (line 24)
- **DRV_NAME** (line 21)
