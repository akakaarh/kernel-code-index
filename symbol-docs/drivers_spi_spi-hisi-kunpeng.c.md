# drivers/spi/spi-hisi-kunpeng.c

Subsystem: drivers/spi

## Functions (20)

### __hisi_calc_div_reg
- Return type: static void
- Signature: __hisi_calc_div_reg(struct hisi_chip_data * chip)
- Line: 287

### hisi_calc_effective_speed
- Return type: static u32
- Signature: hisi_calc_effective_speed(struct spi_controller * host,struct hisi_chip_data * chip,u32 speed_hz)
- Line: 303

### hisi_spi_busy
- Return type: static u32
- Signature: hisi_spi_busy(struct hisi_spi * hs)
- Line: 179

### hisi_spi_cleanup
- Return type: static void
- Signature: hisi_spi_cleanup(struct spi_device * spi)
- Line: 453

### hisi_spi_debugfs_init
- Return type: static int
- Signature: hisi_spi_debugfs_init(struct hisi_spi * hs)
- Line: 161

### hisi_spi_disable
- Return type: static void
- Signature: hisi_spi_disable(struct hisi_spi * hs)
- Line: 218

### hisi_spi_flush_fifo
- Return type: static void
- Signature: hisi_spi_flush_fifo(struct hisi_spi * hs)
- Line: 194

### hisi_spi_handle_err
- Return type: static void
- Signature: hisi_spi_handle_err(struct spi_controller * host,struct spi_message * msg)
- Line: 421

### hisi_spi_hw_init
- Return type: static void
- Signature: hisi_spi_hw_init(struct hisi_spi * hs)
- Line: 334

### hisi_spi_irq
- Return type: static irqreturn_t
- Signature: hisi_spi_irq(int irq,void * dev_id)
- Line: 346

### hisi_spi_n_bytes
- Return type: static u8
- Signature: hisi_spi_n_bytes(struct spi_transfer * transfer)
- Line: 225

### hisi_spi_prepare_cr
- Return type: static u32
- Signature: hisi_spi_prepare_cr(struct spi_device * spi)
- Line: 323

### hisi_spi_probe
- Return type: static int
- Signature: hisi_spi_probe(struct platform_device * pdev)
- Line: 461

### hisi_spi_reader
- Return type: static void
- Signature: hisi_spi_reader(struct hisi_spi * hs)
- Line: 235

### hisi_spi_remove
- Return type: static void
- Signature: hisi_spi_remove(struct platform_device * pdev)
- Line: 538

### hisi_spi_rx_not_empty
- Return type: static u32
- Signature: hisi_spi_rx_not_empty(struct hisi_spi * hs)
- Line: 184

### hisi_spi_setup
- Return type: static int
- Signature: hisi_spi_setup(struct spi_device * spi)
- Line: 435

### hisi_spi_transfer_one
- Return type: static int
- Signature: hisi_spi_transfer_one(struct spi_controller * host,struct spi_device * spi,struct spi_transfer * transfer)
- Line: 385

### hisi_spi_tx_not_full
- Return type: static u32
- Signature: hisi_spi_tx_not_full(struct hisi_spi * hs)
- Line: 189

### hisi_spi_writer
- Return type: static void
- Signature: hisi_spi_writer(struct hisi_spi * hs)
- Line: 261

## Structs (2)

### hisi_chip_data
- Line: 114
- Members:
  - cr: u32
  - speed_hz: u32
  - clk_div: u16
  - div_post: u8
  - div_pre: u8
  - dev: device *
  - regs: void __iomem *
  - irq: int
  - fifo_len: u32
  - tx: const void *
  - tx_len: unsigned int
  - rx: void *
  - rx_len: unsigned int
  - n_bytes: u8
  - debugfs: dentry *
  - regset: debugfs_regset32

### hisi_spi
- Line: 124
- Members:
  - cr: u32
  - speed_hz: u32
  - clk_div: u16
  - div_post: u8
  - div_pre: u8
  - dev: device *
  - regs: void __iomem *
  - irq: int
  - fifo_len: u32
  - tx: const void *
  - tx_len: unsigned int
  - rx: void *
  - rx_len: unsigned int
  - n_bytes: u8
  - debugfs: dentry *
  - regset: debugfs_regset32

## Enums (3)

### hisi_spi_frame_n_bytes
- Line: 106

### hisi_spi_rx_level_trig
- Line: 86

### hisi_spi_tx_level_trig
- Line: 96

## Variables (3)

- static **hisi_spi_acpi_match** : const struct acpi_device_id[] (line 547)
- static **hisi_spi_driver** : platform_driver (line 553)
- static **hisi_spi_regs** : const struct debugfs_reg32[] (line 148)

## Macros (48)

- **CLK_DIV_MAX** (line 79)
- **CLK_DIV_MIN** (line 80)
- **CR_BPW_MASK** (line 42)
- **CR_CPHA_MASK** (line 39)
- **CR_CPOL_MASK** (line 38)
- **CR_DIV_POST_MASK** (line 41)
- **CR_DIV_PRE_MASK** (line 40)
- **CR_LOOP_MASK** (line 37)
- **CR_SPD_MODE_MASK** (line 43)
- **DEFAULT_NUM_CS** (line 82)
- **DIV_POST_MAX** (line 75)
- **DIV_POST_MIN** (line 76)
- **DIV_PRE_MAX** (line 77)
- **DIV_PRE_MIN** (line 78)
- **FIFOC_RX_MASK** (line 47)
- **FIFOC_TX_MASK** (line 46)
- **HISI_SPI_CR** (line 24)
- **HISI_SPI_CSCR** (line 23)
- **HISI_SPI_DBGFS_REG**(_name,_off) (line 142)
- **HISI_SPI_DIN** (line 28)
- **HISI_SPI_DOUT** (line 29)
- **HISI_SPI_ENR** (line 25)
- **HISI_SPI_FIFOC** (line 26)
- **HISI_SPI_ICR** (line 33)
- **HISI_SPI_IMR** (line 27)
- **HISI_SPI_ISR** (line 32)
- **HISI_SPI_RISR** (line 31)
- **HISI_SPI_SR** (line 30)
- **HISI_SPI_VERSION** (line 34)
- **HISI_SPI_WAIT_TIMEOUT_MS** (line 84)
- **ICR_MASK** (line 73)
- **ICR_RXOF** (line 71)
- **ICR_RXTO** (line 72)
- **IMR_MASK** (line 54)
- **IMR_RX** (line 52)
- **IMR_RXOF** (line 50)
- **IMR_RXTO** (line 51)
- **IMR_TX** (line 53)
- **ISR_MASK** (line 68)
- **ISR_RX** (line 66)
- **ISR_RXOF** (line 64)
- **ISR_RXTO** (line 65)
- **ISR_TX** (line 67)
- **SR_BUSY** (line 61)
- **SR_RXF** (line 60)
- **SR_RXNE** (line 59)
- **SR_TXE** (line 57)
- **SR_TXNF** (line 58)
