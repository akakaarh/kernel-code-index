# drivers/spi/spi-mpfs.c

Subsystem: drivers/spi

## Functions (20)

### mpfs_spi_calculate_clkgen
- Return type: static int
- Signature: mpfs_spi_calculate_clkgen(struct mpfs_spi * spi,unsigned long target_hz)
- Line: 441

### mpfs_spi_disable
- Return type: static void
- Signature: mpfs_spi_disable(struct mpfs_spi * spi)
- Line: 126

### mpfs_spi_disable_ints
- Return type: static void
- Signature: mpfs_spi_disable_ints(struct mpfs_spi * spi)
- Line: 169

### mpfs_spi_enable_ints
- Return type: static void
- Signature: mpfs_spi_enable_ints(struct mpfs_spi * spi)
- Line: 161

### mpfs_spi_init
- Return type: static void
- Signature: mpfs_spi_init(struct spi_controller * host,struct mpfs_spi * spi)
- Line: 309

### mpfs_spi_interrupt
- Return type: static irqreturn_t
- Signature: mpfs_spi_interrupt(int irq,void * dev_id)
- Line: 408

### mpfs_spi_prepare_message
- Return type: static int
- Signature: mpfs_spi_prepare_message(struct spi_controller * host,struct spi_message * msg)
- Line: 516

### mpfs_spi_probe
- Return type: static int
- Signature: mpfs_spi_probe(struct platform_device * pdev)
- Line: 527

### mpfs_spi_read
- Return type: static u32
- Signature: mpfs_spi_read(struct mpfs_spi * spi,unsigned int reg)
- Line: 116

### mpfs_spi_read_fifo
- Return type: static void
- Signature: mpfs_spi_read_fifo(struct mpfs_spi * spi,int fifo_max)
- Line: 135

### mpfs_spi_remove
- Return type: static void
- Signature: mpfs_spi_remove(struct platform_device * pdev)
- Line: 590

### mpfs_spi_set_clk_gen
- Return type: static void
- Signature: mpfs_spi_set_clk_gen(struct mpfs_spi * spi)
- Line: 357

### mpfs_spi_set_cs
- Return type: static void
- Signature: mpfs_spi_set_cs(struct spi_device * spi,bool disable)
- Line: 265

### mpfs_spi_set_framesize
- Return type: static void
- Signature: mpfs_spi_set_framesize(struct mpfs_spi * spi,int bt)
- Line: 243

### mpfs_spi_set_mode
- Return type: static void
- Signature: mpfs_spi_set_mode(struct mpfs_spi * spi,unsigned int mode)
- Line: 371

### mpfs_spi_set_xfer_size
- Return type: static void
- Signature: mpfs_spi_set_xfer_size(struct mpfs_spi * spi,int len)
- Line: 177

### mpfs_spi_setup
- Return type: static int
- Signature: mpfs_spi_setup(struct spi_device * spi)
- Line: 287

### mpfs_spi_transfer_one
- Return type: static int
- Signature: mpfs_spi_transfer_one(struct spi_controller * host,struct spi_device * spi_dev,struct spi_transfer * xfer)
- Line: 478

### mpfs_spi_write
- Return type: static void
- Signature: mpfs_spi_write(struct mpfs_spi * spi,unsigned int reg,u32 val)
- Line: 121

### mpfs_spi_write_fifo
- Return type: static void
- Signature: mpfs_spi_write_fifo(struct mpfs_spi * spi,int fifo_max)
- Line: 218

## Structs (1)

### mpfs_spi
- Line: 102
- Members:
  - regs: void __iomem *
  - clk: clk *
  - tx_buf: const u8 *
  - rx_buf: u8 *
  - clk_gen: u32
  - clk_mode: u32
  - pending_slave_select: u32
  - irq: int
  - tx_len: int
  - rx_len: int
  - n_bytes: int

## Variables (2)

- static **mpfs_spi_driver** : platform_driver (line 615)
- static **mpfs_spi_dt_ids** : const struct of_device_id[] (line 608)

## Macros (73)

- **CLK_GEN_MIN** (line 29)
- **CLK_GEN_MODE0_MAX** (line 28)
- **CLK_GEN_MODE1_MAX** (line 27)
- **COMMAND_CLRFRAMECNT** (line 92)
- **COMMAND_RXFIFORST** (line 94)
- **COMMAND_TXFIFORST** (line 93)
- **CONTROL_BIGFIFO** (line 43)
- **CONTROL_CLKMODE** (line 42)
- **CONTROL_ENABLE** (line 32)
- **CONTROL_FRAMECNT_MASK** (line 49)
- **CONTROL_FRAMECNT_SHIFT** (line 50)
- **CONTROL_FRAMEURUN** (line 41)
- **CONTROL_MASTER** (line 33)
- **CONTROL_MODE_MASK** (line 47)
- **CONTROL_OENOFF** (line 44)
- **CONTROL_RESET** (line 45)
- **CONTROL_RX_DATA_INT** (line 34)
- **CONTROL_RX_OVER_INT** (line 36)
- **CONTROL_SPH** (line 39)
- **CONTROL_SPO** (line 38)
- **CONTROL_SPS** (line 40)
- **CONTROL_TX_DATA_INT** (line 35)
- **CONTROL_TX_UNDER_INT** (line 37)
- **DEFAULT_FRAMESIZE** (line 25)
- **FIFO_DEPTH** (line 26)
- **FRAME_SIZE_MASK** (line 77)
- **INT_ENABLE_MASK** (line 73)
- **INT_RXRDY** (line 69)
- **INT_RX_CHANNEL_OVERFLOW** (line 70)
- **INT_TXDONE** (line 68)
- **INT_TX_CHANNEL_UNDERRUN** (line 71)
- **MAX_CS** (line 24)
- **MAX_LEN** (line 23)
- **MICROCHIP_SPI_PM_OPS** (line 601)
- **MODE_X_MASK_SHIFT** (line 30)
- **MOTOROLA_MODE** (line 48)
- **REG_CLK_GEN** (line 82)
- **REG_CMD_SIZE** (line 96)
- **REG_COMMAND** (line 91)
- **REG_CONTROL** (line 75)
- **REG_CONTROL2** (line 90)
- **REG_CTRL2** (line 99)
- **REG_FRAMESUP** (line 100)
- **REG_FRAME_SIZE** (line 76)
- **REG_HWSTATUS** (line 97)
- **REG_INT_CLEAR** (line 79)
- **REG_MIS** (line 88)
- **REG_PKTSIZE** (line 95)
- **REG_RIS** (line 89)
- **REG_RX_DATA** (line 80)
- **REG_SLAVE_SELECT** (line 83)
- **REG_STAT8** (line 98)
- **REG_STATUS** (line 78)
- **REG_TX_DATA** (line 81)
- **SSELOUT** (line 87)
- **SSELOUT_SHIFT** (line 86)
- **SSEL_DIRECT** (line 85)
- **SSEL_MASK** (line 84)
- **STATUS_ACTIVE** (line 52)
- **STATUS_FRAMESTART** (line 54)
- **STATUS_RXDAT_RXED** (line 65)
- **STATUS_RXFIFO_EMPTY** (line 60)
- **STATUS_RXFIFO_EMPTY_NEXT_READ** (line 59)
- **STATUS_RXFIFO_FULL** (line 62)
- **STATUS_RXFIFO_FULL_NEXT_WRITE** (line 61)
- **STATUS_RX_OVERFLOW** (line 64)
- **STATUS_SSEL** (line 53)
- **STATUS_TXDAT_SENT** (line 66)
- **STATUS_TXFIFO_EMPTY** (line 56)
- **STATUS_TXFIFO_EMPTY_NEXT_READ** (line 55)
- **STATUS_TXFIFO_FULL** (line 58)
- **STATUS_TXFIFO_FULL_NEXT_WRITE** (line 57)
- **STATUS_TX_UNDERRUN** (line 63)
