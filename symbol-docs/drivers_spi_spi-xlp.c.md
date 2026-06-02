# drivers/spi/spi-xlp.c

Subsystem: drivers/spi

## Functions (13)

### xlp_spi_fill_txfifo
- Return type: static void
- Signature: xlp_spi_fill_txfifo(struct xlp_spi_priv * xspi)
- Line: 200

### xlp_spi_interrupt
- Return type: static irqreturn_t
- Signature: xlp_spi_interrupt(int irq,void * dev_id)
- Line: 222

### xlp_spi_probe
- Return type: static int
- Signature: xlp_spi_probe(struct platform_device * pdev)
- Line: 368

### xlp_spi_read_rxfifo
- Return type: static void
- Signature: xlp_spi_read_rxfifo(struct xlp_spi_priv * xspi)
- Line: 180

### xlp_spi_reg_read
- Return type: static u32
- Signature: xlp_spi_reg_read(struct xlp_spi_priv * priv,int cs,int regoff)
- Line: 104

### xlp_spi_reg_write
- Return type: static void
- Signature: xlp_spi_reg_write(struct xlp_spi_priv * priv,int cs,int regoff,u32 val)
- Line: 110

### xlp_spi_send_cmd
- Return type: static void
- Signature: xlp_spi_send_cmd(struct xlp_spi_priv * xspi,int xfer_len,int cmd_cont)
- Line: 254

### xlp_spi_setup
- Return type: static int
- Signature: xlp_spi_setup(struct spi_device * spi)
- Line: 135

### xlp_spi_sysctl_setup
- Return type: static void
- Signature: xlp_spi_sysctl_setup(struct xlp_spi_priv * xspi)
- Line: 125

### xlp_spi_sysctl_write
- Return type: static void
- Signature: xlp_spi_sysctl_write(struct xlp_spi_priv * priv,int regoff,u32 val)
- Line: 116

### xlp_spi_transfer_one
- Return type: static int
- Signature: xlp_spi_transfer_one(struct spi_controller * host,struct spi_device * spi,struct spi_transfer * t)
- Line: 346

### xlp_spi_txrx_bufs
- Return type: static int
- Signature: xlp_spi_txrx_bufs(struct xlp_spi_priv * xs,struct spi_transfer * t)
- Line: 319

### xlp_spi_xfer_block
- Return type: static int
- Signature: xlp_spi_xfer_block(struct xlp_spi_priv * xs,const unsigned char * tx_buf,unsigned char * rx_buf,int xfer_len,int cmd_cont)
- Line: 269

## Structs (1)

### xlp_spi_priv
- Line: 89
- Members:
  - dev: device
  - base: void __iomem *
  - tx_buf: const u8 *
  - rx_buf: u8 *
  - tx_len: int
  - rx_len: int
  - txerrors: int
  - rxerrors: int
  - cs: int
  - spi_clk: u32
  - cmd_cont: bool
  - done: completion

## Variables (2)

- static **xlp_spi_acpi_match** : const struct acpi_device_id[] (line 429)
- static **xlp_spi_driver** : platform_driver (line 437)

## Macros (50)

- **SPI_CS_OFFSET** (line 76)
- **XLP_SPI_CMD** (line 29)
- **XLP_SPI_CMD_CONT** (line 34)
- **XLP_SPI_CMD_IDLE_MASK** (line 30)
- **XLP_SPI_CMD_RX_MASK** (line 32)
- **XLP_SPI_CMD_TXRX_MASK** (line 33)
- **XLP_SPI_CMD_TX_MASK** (line 31)
- **XLP_SPI_CONFIG** (line 15)
- **XLP_SPI_CPHA** (line 16)
- **XLP_SPI_CPOL** (line 17)
- **XLP_SPI_CS_LSBFE** (line 22)
- **XLP_SPI_CS_POL** (line 18)
- **XLP_SPI_DEFAULT_FREQ** (line 80)
- **XLP_SPI_FDIV** (line 26)
- **XLP_SPI_FDIV_MAX** (line 82)
- **XLP_SPI_FDIV_MIN** (line 81)
- **XLP_SPI_FIFO_SIZE** (line 78)
- **XLP_SPI_FIFO_THRESH** (line 56)
- **XLP_SPI_FIFO_WCNT** (line 59)
- **XLP_SPI_INTR_DONE** (line 49)
- **XLP_SPI_INTR_EN** (line 48)
- **XLP_SPI_INTR_RXOF** (line 53)
- **XLP_SPI_INTR_RXTH** (line 51)
- **XLP_SPI_INTR_TXTH** (line 50)
- **XLP_SPI_INTR_TXUF** (line 52)
- **XLP_SPI_MAX_CS** (line 79)
- **XLP_SPI_RXCAP_EN** (line 23)
- **XLP_SPI_RXDATA_FIFO** (line 68)
- **XLP_SPI_RXFIFO_WCNT_MASK** (line 60)
- **XLP_SPI_RXMISO_EN** (line 21)
- **XLP_SPI_RX_INT** (line 42)
- **XLP_SPI_RX_OF** (line 44)
- **XLP_SPI_STATUS** (line 38)
- **XLP_SPI_STAT_MASK** (line 45)
- **XLP_SPI_SYSCTRL** (line 71)
- **XLP_SPI_SYS_CLKDIS** (line 73)
- **XLP_SPI_SYS_PMEN** (line 74)
- **XLP_SPI_SYS_RESET** (line 72)
- **XLP_SPI_TXDATA_FIFO** (line 65)
- **XLP_SPI_TXFIFO_WCNT_MASK** (line 61)
- **XLP_SPI_TXFIFO_WCNT_SHIFT** (line 62)
- **XLP_SPI_TXMISO_EN** (line 19)
- **XLP_SPI_TXMOSI_EN** (line 20)
- **XLP_SPI_TXRXTH** (line 77)
- **XLP_SPI_TX_INT** (line 41)
- **XLP_SPI_TX_UF** (line 43)
- **XLP_SPI_XFER_SIZE** (line 87)
- **XLP_SPI_XFR_BITCNT_SHIFT** (line 35)
- **XLP_SPI_XFR_DONE** (line 40)
- **XLP_SPI_XFR_PENDING** (line 39)
