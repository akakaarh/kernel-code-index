# drivers/spi/spi-armada-3700.c

Subsystem: drivers/spi

## Functions (30)

### a3700_is_rfifo_empty
- Return type: static int
- Signature: a3700_is_rfifo_empty(struct a3700_spi * a3700_spi)
- Line: 507

### a3700_is_wfifo_full
- Return type: static int
- Signature: a3700_is_wfifo_full(struct a3700_spi * a3700_spi)
- Line: 485

### a3700_spi_activate_cs
- Return type: static void
- Signature: a3700_spi_activate_cs(struct a3700_spi * a3700_spi,unsigned int cs)
- Line: 135

### a3700_spi_auto_cs_unset
- Return type: static void
- Signature: a3700_spi_auto_cs_unset(struct a3700_spi * a3700_spi)
- Line: 126

### a3700_spi_bytelen_set
- Return type: static void
- Signature: a3700_spi_bytelen_set(struct a3700_spi * a3700_spi,unsigned int len)
- Line: 245

### a3700_spi_clock_set
- Return type: static void
- Signature: a3700_spi_clock_set(struct a3700_spi * a3700_spi,unsigned int speed_hz)
- Line: 217

### a3700_spi_deactivate_cs
- Return type: static void
- Signature: a3700_spi_deactivate_cs(struct a3700_spi * a3700_spi,unsigned int cs)
- Line: 144

### a3700_spi_fifo_flush
- Return type: static int
- Signature: a3700_spi_fifo_flush(struct a3700_spi * a3700_spi)
- Line: 259

### a3700_spi_fifo_mode_set
- Return type: static void
- Signature: a3700_spi_fifo_mode_set(struct a3700_spi * a3700_spi,bool enable)
- Line: 185

### a3700_spi_fifo_read
- Return type: static int
- Signature: a3700_spi_fifo_read(struct a3700_spi * a3700_spi)
- Line: 514

### a3700_spi_fifo_thres_set
- Return type: static void
- Signature: a3700_spi_fifo_thres_set(struct a3700_spi * a3700_spi,unsigned int bytes)
- Line: 401

### a3700_spi_fifo_write
- Return type: static int
- Signature: a3700_spi_fifo_write(struct a3700_spi * a3700_spi)
- Line: 493

### a3700_spi_header_set
- Return type: static void
- Signature: a3700_spi_header_set(struct a3700_spi * a3700_spi)
- Line: 444

### a3700_spi_init
- Return type: static void
- Signature: a3700_spi_init(struct a3700_spi * a3700_spi)
- Line: 278

### a3700_spi_interrupt
- Return type: static irqreturn_t
- Signature: a3700_spi_interrupt(int irq,void * dev_id)
- Line: 315

### a3700_spi_mode_set
- Return type: static void
- Signature: a3700_spi_mode_set(struct a3700_spi * a3700_spi,unsigned int mode_bits)
- Line: 197

### a3700_spi_pin_mode_set
- Return type: static int
- Signature: a3700_spi_pin_mode_set(struct a3700_spi * a3700_spi,unsigned int pin_mode,bool receiving)
- Line: 154

### a3700_spi_prepare_message
- Return type: static int
- Signature: a3700_spi_prepare_message(struct spi_controller * host,struct spi_message * message)
- Line: 567

### a3700_spi_probe
- Return type: static int
- Signature: a3700_spi_probe(struct platform_device * pdev)
- Line: 813

### a3700_spi_set_cs
- Return type: static void
- Signature: a3700_spi_set_cs(struct spi_device * spi,bool enable)
- Line: 434

### a3700_spi_transfer_abort_fifo
- Return type: static void
- Signature: a3700_spi_transfer_abort_fifo(struct a3700_spi * a3700_spi)
- Line: 545

### a3700_spi_transfer_one
- Return type: static int
- Signature: a3700_spi_transfer_one(struct spi_controller * host,struct spi_device * spi,struct spi_transfer * xfer)
- Line: 784

### a3700_spi_transfer_one_fifo
- Return type: static int
- Signature: a3700_spi_transfer_one_fifo(struct spi_controller * host,struct spi_device * spi,struct spi_transfer * xfer)
- Line: 590

### a3700_spi_transfer_one_full_duplex
- Return type: static int
- Signature: a3700_spi_transfer_one_full_duplex(struct spi_controller * host,struct spi_device * spi,struct spi_transfer * xfer)
- Line: 739

### a3700_spi_transfer_setup
- Return type: static void
- Signature: a3700_spi_transfer_setup(struct spi_device * spi,struct spi_transfer * xfer)
- Line: 414

### a3700_spi_transfer_wait
- Return type: static bool
- Signature: a3700_spi_transfer_wait(struct spi_device * spi,unsigned int bit_mask)
- Line: 390

### a3700_spi_unprepare_message
- Return type: static int
- Signature: a3700_spi_unprepare_message(struct spi_controller * host,struct spi_message * message)
- Line: 796

### a3700_spi_wait_completion
- Return type: static bool
- Signature: a3700_spi_wait_completion(struct spi_device * spi)
- Line: 339

### spireg_read
- Return type: static u32
- Signature: spireg_read(struct a3700_spi * a3700_spi,u32 offset)
- Line: 116

### spireg_write
- Return type: static void
- Signature: spireg_write(struct a3700_spi * a3700_spi,u32 offset,u32 data)
- Line: 121

## Structs (1)

### a3700_spi
- Line: 101
- Members:
  - host: spi_controller *
  - base: void __iomem *
  - clk: clk *
  - irq: unsigned int
  - flags: unsigned int
  - xmit_data: bool
  - tx_buf: const u8 *
  - rx_buf: u8 *
  - buf_len: size_t
  - byte_len: u8
  - wait_mask: u32
  - done: completion

## Variables (2)

- static **a3700_spi_driver** : platform_driver (line 900)
- static **a3700_spi_dt_ids** : const struct of_device_id[] (line 806)

## Macros (63)

- **A3700_SPI_ADDR_CNT_BIT** (line 93)
- **A3700_SPI_ADDR_CNT_MASK** (line 94)
- **A3700_SPI_ADDR_NOT_CONFIG** (line 46)
- **A3700_SPI_ADDR_PIN** (line 70)
- **A3700_SPI_AUTO_CS** (line 63)
- **A3700_SPI_BYTE_LEN** (line 77)
- **A3700_SPI_CLK_CAPT_EDGE** (line 99)
- **A3700_SPI_CLK_EVEN_OFFS** (line 80)
- **A3700_SPI_CLK_PHA** (line 76)
- **A3700_SPI_CLK_POL** (line 75)
- **A3700_SPI_CLK_PRESCALE** (line 78)
- **A3700_SPI_CLK_PRESCALE_MASK** (line 79)
- **A3700_SPI_DATA_IN_REG** (line 34)
- **A3700_SPI_DATA_OUT_REG** (line 33)
- **A3700_SPI_DATA_PIN0** (line 72)
- **A3700_SPI_DATA_PIN1** (line 71)
- **A3700_SPI_DATA_PIN_MASK** (line 86)
- **A3700_SPI_DMA_RD_EN** (line 64)
- **A3700_SPI_DUMMY_CNT_BIT** (line 89)
- **A3700_SPI_DUMMY_CNT_MASK** (line 90)
- **A3700_SPI_EN** (line 45)
- **A3700_SPI_FIFO_FLUSH** (line 73)
- **A3700_SPI_FIFO_MODE** (line 65)
- **A3700_SPI_FIFO_THRS_MASK** (line 84)
- **A3700_SPI_IF_ADDR_REG** (line 36)
- **A3700_SPI_IF_CFG_REG** (line 32)
- **A3700_SPI_IF_CTRL_REG** (line 31)
- **A3700_SPI_IF_DIN_CNT_REG** (line 39)
- **A3700_SPI_IF_HDR_CNT_REG** (line 38)
- **A3700_SPI_IF_INST_REG** (line 35)
- **A3700_SPI_IF_RMODE_REG** (line 37)
- **A3700_SPI_IF_TIME_REG** (line 40)
- **A3700_SPI_INSTR_CNT_BIT** (line 95)
- **A3700_SPI_INSTR_CNT_MASK** (line 96)
- **A3700_SPI_INST_PIN** (line 69)
- **A3700_SPI_INT_MASK_REG** (line 42)
- **A3700_SPI_INT_STAT_REG** (line 41)
- **A3700_SPI_MAX_PRESCALE** (line 27)
- **A3700_SPI_MAX_SPEED_HZ** (line 26)
- **A3700_SPI_RFIFO_EMPTY** (line 54)
- **A3700_SPI_RFIFO_FULL** (line 53)
- **A3700_SPI_RFIFO_OVERFLOW** (line 49)
- **A3700_SPI_RFIFO_RDY** (line 56)
- **A3700_SPI_RFIFO_THRS** (line 62)
- **A3700_SPI_RFIFO_THRS_BIT** (line 83)
- **A3700_SPI_RFIFO_UNDERFLOW** (line 50)
- **A3700_SPI_RMODE_CNT_BIT** (line 91)
- **A3700_SPI_RMODE_CNT_MASK** (line 92)
- **A3700_SPI_RW_EN** (line 74)
- **A3700_SPI_SRST** (line 66)
- **A3700_SPI_TIMEOUT** (line 28)
- **A3700_SPI_WFIFO_EMPTY** (line 52)
- **A3700_SPI_WFIFO_FULL** (line 51)
- **A3700_SPI_WFIFO_OVERFLOW** (line 47)
- **A3700_SPI_WFIFO_RDY** (line 55)
- **A3700_SPI_WFIFO_THRS** (line 61)
- **A3700_SPI_WFIFO_THRS_BIT** (line 82)
- **A3700_SPI_WFIFO_UNDERFLOW** (line 48)
- **A3700_SPI_XFER_DONE** (line 58)
- **A3700_SPI_XFER_RDY** (line 57)
- **A3700_SPI_XFER_START** (line 67)
- **A3700_SPI_XFER_STOP** (line 68)
- **DRIVER_NAME** (line 24)
