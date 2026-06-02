# drivers/spi/spi-microchip-core-spi.c

Subsystem: drivers/spi

## Functions (13)

### mchp_corespi_disable
- Return type: static void
- Signature: mchp_corespi_disable(struct mchp_corespi * spi)
- Line: 82

### mchp_corespi_disable_ints
- Return type: static void
- Signature: mchp_corespi_disable_ints(struct mchp_corespi * spi)
- Line: 117

### mchp_corespi_enable_ints
- Return type: static void
- Signature: mchp_corespi_enable_ints(struct mchp_corespi * spi)
- Line: 109

### mchp_corespi_init
- Return type: static void
- Signature: mchp_corespi_init(struct spi_controller * host,struct mchp_corespi * spi)
- Line: 172

### mchp_corespi_interrupt
- Return type: static irqreturn_t
- Signature: mchp_corespi_interrupt(int irq,void * dev_id)
- Line: 189

### mchp_corespi_probe
- Return type: static int
- Signature: mchp_corespi_probe(struct platform_device * pdev)
- Line: 287

### mchp_corespi_read_fifo
- Return type: static void
- Signature: mchp_corespi_read_fifo(struct mchp_corespi * spi,u32 fifo_max)
- Line: 91

### mchp_corespi_remove
- Return type: static void
- Signature: mchp_corespi_remove(struct platform_device * pdev)
- Line: 397

### mchp_corespi_set_clk_div
- Return type: static int
- Signature: mchp_corespi_set_clk_div(struct mchp_corespi * spi,unsigned long target_hz)
- Line: 227

### mchp_corespi_set_cs
- Return type: static void
- Signature: mchp_corespi_set_cs(struct spi_device * spi,bool disable)
- Line: 142

### mchp_corespi_setup
- Return type: static int
- Signature: mchp_corespi_setup(struct spi_device * spi)
- Line: 154

### mchp_corespi_transfer_one
- Return type: static int
- Signature: mchp_corespi_transfer_one(struct spi_controller * host,struct spi_device * spi_dev,struct spi_transfer * xfer)
- Line: 257

### mchp_corespi_write_fifo
- Return type: static void
- Signature: mchp_corespi_write_fifo(struct mchp_corespi * spi,u32 fifo_max)
- Line: 125

## Structs (1)

### mchp_corespi
- Line: 70
- Members:
  - regs: void __iomem *
  - clk: clk *
  - tx_buf: const u8 *
  - rx_buf: u8 *
  - clk_gen: u32
  - irq: int
  - tx_len: unsigned int
  - rx_len: unsigned int
  - fifo_depth: u32

## Variables (2)

- static **mchp_corespi_driver** : platform_driver (line 420)
- static **mchp_corespi_dt_ids** : const struct of_device_id[] (line 413)

## Macros (42)

- **INT_ENABLE_MASK** (line 54)
- **MCHP_CORESPI_CONTROL2_INTEN_CMD** (line 52)
- **MCHP_CORESPI_CONTROL2_INTEN_DATA_RX** (line 50)
- **MCHP_CORESPI_CONTROL2_INTEN_SSEND** (line 51)
- **MCHP_CORESPI_CONTROL2_INTEN_TXRFMT** (line 49)
- **MCHP_CORESPI_CONTROL_ENABLE** (line 24)
- **MCHP_CORESPI_CONTROL_FRAMEURUN** (line 29)
- **MCHP_CORESPI_CONTROL_MASTER** (line 25)
- **MCHP_CORESPI_CONTROL_OENOFF** (line 30)
- **MCHP_CORESPI_CONTROL_RX_OVER_INT** (line 27)
- **MCHP_CORESPI_CONTROL_TX_DATA_INT** (line 26)
- **MCHP_CORESPI_CONTROL_TX_UNDER_INT** (line 28)
- **MCHP_CORESPI_DEFAULT_FIFO_DEPTH** (line 21)
- **MCHP_CORESPI_DEFAULT_MOTOROLA_MODE** (line 22)
- **MCHP_CORESPI_INT_CMDINT** (line 44)
- **MCHP_CORESPI_INT_DATA_RX** (line 46)
- **MCHP_CORESPI_INT_RX_CHANNEL_OVERFLOW** (line 42)
- **MCHP_CORESPI_INT_SSEND** (line 45)
- **MCHP_CORESPI_INT_TXDONE** (line 41)
- **MCHP_CORESPI_INT_TXRFM** (line 47)
- **MCHP_CORESPI_INT_TX_CHANNEL_UNDERRUN** (line 43)
- **MCHP_CORESPI_MAX_CS** (line 20)
- **MCHP_CORESPI_REG_CLK_DIV** (line 68)
- **MCHP_CORESPI_REG_COMMAND** (line 64)
- **MCHP_CORESPI_REG_CONTROL** (line 57)
- **MCHP_CORESPI_REG_CONTROL2** (line 63)
- **MCHP_CORESPI_REG_INTCLEAR** (line 58)
- **MCHP_CORESPI_REG_INTMASK** (line 61)
- **MCHP_CORESPI_REG_INTRAW** (line 62)
- **MCHP_CORESPI_REG_RXDATA** (line 59)
- **MCHP_CORESPI_REG_SSEL** (line 66)
- **MCHP_CORESPI_REG_STAT** (line 65)
- **MCHP_CORESPI_REG_TXDATA** (line 60)
- **MCHP_CORESPI_REG_TXDATA_LAST** (line 67)
- **MCHP_CORESPI_STATUS_ACTIVE** (line 32)
- **MCHP_CORESPI_STATUS_DONE** (line 38)
- **MCHP_CORESPI_STATUS_FIRSTFRAME** (line 39)
- **MCHP_CORESPI_STATUS_RXFIFO_EMPTY** (line 37)
- **MCHP_CORESPI_STATUS_RXFIFO_FULL** (line 35)
- **MCHP_CORESPI_STATUS_SSEL** (line 33)
- **MCHP_CORESPI_STATUS_TXFIFO_FULL** (line 36)
- **MCHP_CORESPI_STATUS_TXFIFO_UNDERFLOW** (line 34)
