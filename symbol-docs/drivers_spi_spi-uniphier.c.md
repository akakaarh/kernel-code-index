# drivers/spi/spi-uniphier.c

Subsystem: drivers/spi

## Functions (25)

### bytes_per_word
- Return type: static unsigned int
- Signature: bytes_per_word(unsigned int bits)
- Line: 103

### uniphier_spi_can_dma
- Return type: static bool
- Signature: uniphier_spi_can_dma(struct spi_controller * host,struct spi_device * spi,struct spi_transfer * t)
- Line: 349

### uniphier_spi_dma_rxcb
- Return type: static void
- Signature: uniphier_spi_dma_rxcb(void * data)
- Line: 364

### uniphier_spi_dma_txcb
- Return type: static void
- Signature: uniphier_spi_dma_txcb(void * data)
- Line: 376

### uniphier_spi_fill_tx_fifo
- Return type: static void
- Signature: uniphier_spi_fill_tx_fifo(struct uniphier_spi_priv * priv)
- Line: 317

### uniphier_spi_handle_err
- Return type: static void
- Signature: uniphier_spi_handle_err(struct spi_controller * host,struct spi_message * msg)
- Line: 574

### uniphier_spi_handler
- Return type: static irqreturn_t
- Signature: uniphier_spi_handler(int irq,void * dev_id)
- Line: 600

### uniphier_spi_irq_disable
- Return type: static void
- Signature: uniphier_spi_irq_disable(struct uniphier_spi_priv * priv,u32 mask)
- Line: 118

### uniphier_spi_irq_enable
- Return type: static void
- Signature: uniphier_spi_irq_enable(struct uniphier_spi_priv * priv,u32 mask)
- Line: 108

### uniphier_spi_prepare_transfer_hardware
- Return type: static int
- Signature: uniphier_spi_prepare_transfer_hardware(struct spi_controller * host)
- Line: 556

### uniphier_spi_probe
- Return type: static int
- Signature: uniphier_spi_probe(struct platform_device * pdev)
- Line: 641

### uniphier_spi_recv
- Return type: static void
- Signature: uniphier_spi_recv(struct uniphier_spi_priv * priv)
- Line: 278

### uniphier_spi_remove
- Return type: static void
- Signature: uniphier_spi_remove(struct platform_device * pdev)
- Line: 770

### uniphier_spi_send
- Return type: static void
- Signature: uniphier_spi_send(struct uniphier_spi_priv * priv)
- Line: 251

### uniphier_spi_set_baudrate
- Return type: static void
- Signature: uniphier_spi_set_baudrate(struct spi_device * spi,unsigned int speed)
- Line: 198

### uniphier_spi_set_cs
- Return type: static void
- Signature: uniphier_spi_set_cs(struct spi_device * spi,bool enable)
- Line: 334

### uniphier_spi_set_fifo_threshold
- Return type: static void
- Signature: uniphier_spi_set_fifo_threshold(struct uniphier_spi_priv * priv,unsigned int threshold)
- Line: 305

### uniphier_spi_set_mode
- Return type: static void
- Signature: uniphier_spi_set_mode(struct spi_device * spi)
- Line: 128

### uniphier_spi_set_transfer_size
- Return type: static void
- Signature: uniphier_spi_set_transfer_size(struct spi_device * spi,int size)
- Line: 181

### uniphier_spi_setup_transfer
- Return type: static void
- Signature: uniphier_spi_setup_transfer(struct spi_device * spi,struct spi_transfer * t)
- Line: 217

### uniphier_spi_transfer_one
- Return type: static int
- Signature: uniphier_spi_transfer_one(struct spi_controller * host,struct spi_device * spi,struct spi_transfer * t)
- Line: 526

### uniphier_spi_transfer_one_dma
- Return type: static int
- Signature: uniphier_spi_transfer_one_dma(struct spi_controller * host,struct spi_device * spi,struct spi_transfer * t)
- Line: 388

### uniphier_spi_transfer_one_irq
- Return type: static int
- Signature: uniphier_spi_transfer_one_irq(struct spi_controller * host,struct spi_device * spi,struct spi_transfer * t)
- Line: 471

### uniphier_spi_transfer_one_poll
- Return type: static int
- Signature: uniphier_spi_transfer_one_poll(struct spi_controller * host,struct spi_device * spi,struct spi_transfer * t)
- Line: 498

### uniphier_spi_unprepare_transfer_hardware
- Return type: static int
- Signature: uniphier_spi_unprepare_transfer_hardware(struct spi_controller * host)
- Line: 565

## Structs (1)

### uniphier_spi_priv
- Line: 25
- Members:
  - base: void __iomem *
  - base_dma_addr: dma_addr_t
  - clk: clk *
  - host: spi_controller *
  - xfer_done: completion
  - error: int
  - tx_bytes: unsigned int
  - rx_bytes: unsigned int
  - tx_buf: const u8 *
  - rx_buf: u8 *
  - dma_busy: atomic_t
  - is_save_param: bool
  - bits_per_word: u8
  - mode: u16
  - speed_hz: u32

## Variables (2)

- static **uniphier_spi_driver** : platform_driver (line 792)
- static **uniphier_spi_match** : const struct of_device_id[] (line 786)

## Macros (49)

- **SSI_CKS** (line 48)
- **SSI_CKS_CKDLY** (line 52)
- **SSI_CKS_CKINIT** (line 51)
- **SSI_CKS_CKPHS** (line 50)
- **SSI_CKS_CKRAT_MASK** (line 49)
- **SSI_CTL** (line 45)
- **SSI_CTL_EN** (line 46)
- **SSI_DMA_RX_BUSY** (line 100)
- **SSI_DMA_TX_BUSY** (line 101)
- **SSI_FC** (line 88)
- **SSI_FC_RXFFL** (line 91)
- **SSI_FC_RXFTH_MASK** (line 92)
- **SSI_FC_TXFFL** (line 89)
- **SSI_FC_TXFTH_MASK** (line 90)
- **SSI_FIFO_BURST_NUM** (line 98)
- **SSI_FIFO_DEPTH** (line 97)
- **SSI_FPS** (line 62)
- **SSI_FPS_FSPOL** (line 63)
- **SSI_FPS_FSTRT** (line 64)
- **SSI_IC** (line 83)
- **SSI_IC_RCIC** (line 85)
- **SSI_IC_RORIC** (line 86)
- **SSI_IC_TCIC** (line 84)
- **SSI_IE** (line 70)
- **SSI_IE_ALL_MASK** (line 76)
- **SSI_IE_RCIE** (line 72)
- **SSI_IE_RORIE** (line 75)
- **SSI_IE_RXRE** (line 74)
- **SSI_IE_TCIE** (line 71)
- **SSI_IE_TXRE** (line 73)
- **SSI_IS** (line 78)
- **SSI_IS_RCID** (line 80)
- **SSI_IS_RORID** (line 81)
- **SSI_IS_RXRS** (line 79)
- **SSI_MAX_CLK_DIVIDER** (line 22)
- **SSI_MIN_CLK_DIVIDER** (line 23)
- **SSI_POLL_TIMEOUT_US** (line 21)
- **SSI_RXDR** (line 95)
- **SSI_RXWDS** (line 59)
- **SSI_RXWDS_DTLEN_MASK** (line 60)
- **SSI_SR** (line 66)
- **SSI_SR_BUSY** (line 67)
- **SSI_SR_RNE** (line 68)
- **SSI_TIMEOUT_MS** (line 20)
- **SSI_TXDR** (line 94)
- **SSI_TXWDS** (line 54)
- **SSI_TXWDS_DTLEN_MASK** (line 57)
- **SSI_TXWDS_TDTF_MASK** (line 56)
- **SSI_TXWDS_WDLEN_MASK** (line 55)
