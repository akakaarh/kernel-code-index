# drivers/spi/spi-apple.c

Subsystem: drivers/spi

## Functions (13)

### apple_spi_init
- Return type: static void
- Signature: apple_spi_init(struct apple_spi * spi)
- Line: 148

### apple_spi_irq
- Return type: static irqreturn_t
- Signature: apple_spi_irq(int irq,void * dev_id)
- Line: 218

### apple_spi_prep_transfer
- Return type: static bool
- Signature: apple_spi_prep_transfer(struct apple_spi * spi,struct spi_transfer * t)
- Line: 196

### apple_spi_prepare_message
- Return type: static int
- Signature: apple_spi_prepare_message(struct spi_controller * ctlr,struct spi_message * msg)
- Line: 173

### apple_spi_probe
- Return type: static int
- Signature: apple_spi_probe(struct platform_device * pdev)
- Line: 457

### apple_spi_rx
- Return type: static void
- Signature: apple_spi_rx(struct apple_spi * spi,void ** rx_ptr,u32 * left,unsigned int bytes_per_word)
- Line: 312

### apple_spi_set_cs
- Return type: static void
- Signature: apple_spi_set_cs(struct spi_device * device,bool is_high)
- Line: 189

### apple_spi_transfer_one
- Return type: static int
- Signature: apple_spi_transfer_one(struct spi_controller * ctlr,struct spi_device * device,struct spi_transfer * t)
- Line: 357

### apple_spi_tx
- Return type: static void
- Signature: apple_spi_tx(struct apple_spi * spi,const void ** tx_ptr,u32 * left,unsigned int bytes_per_word)
- Line: 267

### apple_spi_wait
- Return type: static int
- Signature: apple_spi_wait(struct apple_spi * spi,u32 fifo_bit,u32 xfer_bit,int poll)
- Line: 235

### reg_mask
- Return type: static void
- Signature: reg_mask(struct apple_spi * spi,int offset,u32 clear,u32 set)
- Line: 139

### reg_read
- Return type: static u32
- Signature: reg_read(struct apple_spi * spi,int offset)
- Line: 134

### reg_write
- Return type: static void
- Signature: reg_write(struct apple_spi * spi,int offset,u32 value)
- Line: 129

## Structs (1)

### apple_spi
- Line: 123
- Members:
  - regs: void __iomem *
  - clk: clk *
  - done: completion

## Variables (2)

- static **apple_spi_driver** : platform_driver (line 519)
- static **apple_spi_of_match** : const struct of_device_id[] (line 512)

## Macros (80)

- **APPLE_SPI_CFG** (line 25)
- **APPLE_SPI_CFG_CPHA** (line 26)
- **APPLE_SPI_CFG_CPOL** (line 27)
- **APPLE_SPI_CFG_FIFO_THRESH** (line 39)
- **APPLE_SPI_CFG_FIFO_THRESH_1B** (line 42)
- **APPLE_SPI_CFG_FIFO_THRESH_4B** (line 41)
- **APPLE_SPI_CFG_FIFO_THRESH_8B** (line 40)
- **APPLE_SPI_CFG_IE_RXCOMPLETE** (line 32)
- **APPLE_SPI_CFG_IE_TXCOMPLETE** (line 43)
- **APPLE_SPI_CFG_IE_TXRXTHRESH** (line 33)
- **APPLE_SPI_CFG_LSB_FIRST** (line 34)
- **APPLE_SPI_CFG_MODE** (line 28)
- **APPLE_SPI_CFG_MODE_DMA** (line 31)
- **APPLE_SPI_CFG_MODE_IRQ** (line 30)
- **APPLE_SPI_CFG_MODE_POLLED** (line 29)
- **APPLE_SPI_CFG_WORD_SIZE** (line 35)
- **APPLE_SPI_CFG_WORD_SIZE_16B** (line 37)
- **APPLE_SPI_CFG_WORD_SIZE_32B** (line 38)
- **APPLE_SPI_CFG_WORD_SIZE_8B** (line 36)
- **APPLE_SPI_CLKDIV** (line 56)
- **APPLE_SPI_CLKDIV_MAX** (line 57)
- **APPLE_SPI_CTRL** (line 20)
- **APPLE_SPI_CTRL_RUN** (line 21)
- **APPLE_SPI_CTRL_RX_RESET** (line 23)
- **APPLE_SPI_CTRL_TX_RESET** (line 22)
- **APPLE_SPI_DELAY_ENABLE** (line 102)
- **APPLE_SPI_DELAY_MOSI_VAL** (line 107)
- **APPLE_SPI_DELAY_NO_INTERBYTE** (line 103)
- **APPLE_SPI_DELAY_POST** (line 101)
- **APPLE_SPI_DELAY_PRE** (line 100)
- **APPLE_SPI_DELAY_SCK_VAL** (line 106)
- **APPLE_SPI_DELAY_SET_MOSI** (line 105)
- **APPLE_SPI_DELAY_SET_SCK** (line 104)
- **APPLE_SPI_FIFOSTAT** (line 62)
- **APPLE_SPI_FIFOSTAT_LEVEL_RX** (line 66)
- **APPLE_SPI_FIFOSTAT_LEVEL_TX** (line 64)
- **APPLE_SPI_FIFOSTAT_RXEMPTY** (line 65)
- **APPLE_SPI_FIFOSTAT_TXFULL** (line 63)
- **APPLE_SPI_FIFO_DEPTH** (line 109)
- **APPLE_SPI_FIFO_RXFULL** (line 77)
- **APPLE_SPI_FIFO_RXTHRESH** (line 75)
- **APPLE_SPI_FIFO_RXUNDERRUN** (line 79)
- **APPLE_SPI_FIFO_TXEMPTY** (line 78)
- **APPLE_SPI_FIFO_TXOVERFLOW** (line 80)
- **APPLE_SPI_FIFO_TXTHRESH** (line 76)
- **APPLE_SPI_IE_FIFO** (line 73)
- **APPLE_SPI_IE_XFER** (line 68)
- **APPLE_SPI_IF_FIFO** (line 74)
- **APPLE_SPI_IF_XFER** (line 69)
- **APPLE_SPI_PIN** (line 50)
- **APPLE_SPI_PINCFG** (line 92)
- **APPLE_SPI_PINCFG_CLK_IDLE_VAL** (line 96)
- **APPLE_SPI_PINCFG_CS_IDLE_VAL** (line 97)
- **APPLE_SPI_PINCFG_KEEP_CLK** (line 93)
- **APPLE_SPI_PINCFG_KEEP_CS** (line 94)
- **APPLE_SPI_PINCFG_KEEP_MOSI** (line 95)
- **APPLE_SPI_PINCFG_MOSI_IDLE_VAL** (line 98)
- **APPLE_SPI_PIN_CS** (line 52)
- **APPLE_SPI_PIN_KEEP_MOSI** (line 51)
- **APPLE_SPI_RXCNT** (line 58)
- **APPLE_SPI_RXDATA** (line 55)
- **APPLE_SPI_SHIFTCFG** (line 82)
- **APPLE_SPI_SHIFTCFG_AND_CLK_DATA** (line 85)
- **APPLE_SPI_SHIFTCFG_BITS** (line 89)
- **APPLE_SPI_SHIFTCFG_CLK_ENABLE** (line 83)
- **APPLE_SPI_SHIFTCFG_CS_AS_DATA** (line 86)
- **APPLE_SPI_SHIFTCFG_CS_ENABLE** (line 84)
- **APPLE_SPI_SHIFTCFG_OVERRIDE_CS** (line 90)
- **APPLE_SPI_SHIFTCFG_RX_ENABLE** (line 88)
- **APPLE_SPI_SHIFTCFG_TX_ENABLE** (line 87)
- **APPLE_SPI_STATUS** (line 45)
- **APPLE_SPI_STATUS_RXCOMPLETE** (line 46)
- **APPLE_SPI_STATUS_TXCOMPLETE** (line 48)
- **APPLE_SPI_STATUS_TXRXTHRESH** (line 47)
- **APPLE_SPI_TIMEOUT_MS** (line 121)
- **APPLE_SPI_TXCNT** (line 60)
- **APPLE_SPI_TXDATA** (line 54)
- **APPLE_SPI_WORD_DELAY** (line 59)
- **APPLE_SPI_XFER_RXCOMPLETE** (line 70)
- **APPLE_SPI_XFER_TXCOMPLETE** (line 71)
