# drivers/spi/spi-xilinx.c

Subsystem: drivers/spi

## Functions (14)

### xilinx_spi_chipselect
- Return type: static void
- Signature: xilinx_spi_chipselect(struct spi_device * spi,int is_on)
- Line: 186

### xilinx_spi_find_buffer_size
- Return type: static int
- Signature: xilinx_spi_find_buffer_size(struct xilinx_spi * xspi)
- Line: 361

### xilinx_spi_irq
- Return type: static irqreturn_t
- Signature: xilinx_spi_irq(int irq,void * dev_id)
- Line: 344

### xilinx_spi_probe
- Return type: static int
- Signature: xilinx_spi_probe(struct platform_device * pdev)
- Line: 391

### xilinx_spi_remove
- Return type: static void
- Signature: xilinx_spi_remove(struct platform_device * pdev)
- Line: 506

### xilinx_spi_rx
- Return type: static void
- Signature: xilinx_spi_rx(struct xilinx_spi * xspi)
- Line: 141

### xilinx_spi_setup_transfer
- Return type: static int
- Signature: xilinx_spi_setup_transfer(struct spi_device * spi,struct spi_transfer * t)
- Line: 225

### xilinx_spi_tx
- Return type: static void
- Signature: xilinx_spi_tx(struct xilinx_spi * xspi)
- Line: 116

### xilinx_spi_txrx_bufs
- Return type: static int
- Signature: xilinx_spi_txrx_bufs(struct spi_device * spi,struct spi_transfer * t)
- Line: 238

### xspi_init_hw
- Return type: static void
- Signature: xspi_init_hw(struct xilinx_spi * xspi)
- Line: 163

### xspi_read32
- Return type: static unsigned int
- Signature: xspi_read32(void __iomem * addr)
- Line: 101

### xspi_read32_be
- Return type: static unsigned int
- Signature: xspi_read32_be(void __iomem * addr)
- Line: 111

### xspi_write32
- Return type: static void
- Signature: xspi_write32(u32 val,void __iomem * addr)
- Line: 96

### xspi_write32_be
- Return type: static void
- Signature: xspi_write32_be(u32 val,void __iomem * addr)
- Line: 106

## Structs (1)

### xilinx_spi
- Line: 79
- Members:
  - bitbang: spi_bitbang
  - done: completion
  - regs: void __iomem *
  - irq: int
  - force_irq: bool
  - rx_ptr: u8 *
  - tx_ptr: const u8 *
  - bytes_per_word: u8
  - buffer_size: int
  - cs_inactive: u32
  - read_fn: unsigned int (*)(void __iomem * addr)
  - write_fn: void (*)(u32 val,void __iomem * addr)

## Variables (2)

- static **xilinx_spi_driver** : platform_driver (line 525)
- static **xilinx_spi_of_match** : const struct of_device_id[] (line 383)

## Macros (36)

- **XILINX_SPI_MAX_CS** (line 23)
- **XILINX_SPI_NAME** (line 25)
- **XIPIF_V123B_DGIER_OFFSET** (line 61)
- **XIPIF_V123B_GINTR_ENABLE** (line 62)
- **XIPIF_V123B_IIER_OFFSET** (line 65)
- **XIPIF_V123B_IISR_OFFSET** (line 64)
- **XIPIF_V123B_RESETR_OFFSET** (line 76)
- **XIPIF_V123B_RESET_MASK** (line 77)
- **XSPI_CR_CPHA** (line 36)
- **XSPI_CR_CPOL** (line 35)
- **XSPI_CR_ENABLE** (line 33)
- **XSPI_CR_LOOP** (line 32)
- **XSPI_CR_LSB_FIRST** (line 43)
- **XSPI_CR_MANUAL_SSELECT** (line 41)
- **XSPI_CR_MASTER_MODE** (line 34)
- **XSPI_CR_MODE_MASK** (line 37)
- **XSPI_CR_OFFSET** (line 30)
- **XSPI_CR_RXFIFO_RESET** (line 40)
- **XSPI_CR_TRANS_INHIBIT** (line 42)
- **XSPI_CR_TXFIFO_RESET** (line 39)
- **XSPI_INTR_MODE_FAULT** (line 67)
- **XSPI_INTR_RX_FULL** (line 72)
- **XSPI_INTR_RX_OVERRUN** (line 73)
- **XSPI_INTR_SLAVE_MODE_FAULT** (line 68)
- **XSPI_INTR_TX_EMPTY** (line 70)
- **XSPI_INTR_TX_HALF_EMPTY** (line 74)
- **XSPI_INTR_TX_UNDERRUN** (line 71)
- **XSPI_RXD_OFFSET** (line 54)
- **XSPI_SR_MODE_FAULT_MASK** (line 51)
- **XSPI_SR_OFFSET** (line 45)
- **XSPI_SR_RX_EMPTY_MASK** (line 47)
- **XSPI_SR_RX_FULL_MASK** (line 48)
- **XSPI_SR_TX_EMPTY_MASK** (line 49)
- **XSPI_SR_TX_FULL_MASK** (line 50)
- **XSPI_SSR_OFFSET** (line 56)
- **XSPI_TXD_OFFSET** (line 53)
