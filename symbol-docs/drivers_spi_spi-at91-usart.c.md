# drivers/spi/spi-at91-usart.c

Subsystem: drivers/spi

## Functions (28)

### at91_usart_gpio_setup
- Return type: static int
- Signature: at91_usart_gpio_setup(struct platform_device * pdev)
- Line: 468

### at91_usart_spi_can_dma
- Return type: static bool
- Signature: at91_usart_spi_can_dma(struct spi_controller * ctrl,struct spi_device * spi,struct spi_transfer * xfer)
- Line: 113

### at91_usart_spi_check_overrun
- Return type: static u32
- Signature: at91_usart_spi_check_overrun(struct at91_usart_spi * aus)
- Line: 272

### at91_usart_spi_cleanup
- Return type: static void
- Signature: at91_usart_spi_cleanup(struct spi_device * spi)
- Line: 454

### at91_usart_spi_configure_dma
- Return type: static int
- Signature: at91_usart_spi_configure_dma(struct spi_controller * ctlr,struct at91_usart_spi * aus)
- Line: 122

### at91_usart_spi_dma_timeout
- Return type: static unsigned long
- Signature: at91_usart_spi_dma_timeout(struct at91_usart_spi * aus)
- Line: 256

### at91_usart_spi_dma_transfer
- Return type: static int
- Signature: at91_usart_spi_dma_transfer(struct spi_controller * ctlr,struct spi_transfer * xfer)
- Line: 201

### at91_usart_spi_init
- Return type: static void
- Signature: at91_usart_spi_init(struct at91_usart_spi * aus)
- Line: 462

### at91_usart_spi_interrupt
- Return type: static irqreturn_t
- Signature: at91_usart_spi_interrupt(int irq,void * dev_id)
- Line: 319

### at91_usart_spi_prepare_message
- Return type: static int
- Signature: at91_usart_spi_prepare_message(struct spi_controller * ctlr,struct spi_message * message)
- Line: 429

### at91_usart_spi_probe
- Return type: static int
- Signature: at91_usart_spi_probe(struct platform_device * pdev)
- Line: 477

### at91_usart_spi_read_status
- Return type: static u32
- Signature: at91_usart_spi_read_status(struct at91_usart_spi * aus)
- Line: 277

### at91_usart_spi_release_dma
- Return type: static void
- Signature: at91_usart_spi_release_dma(struct spi_controller * ctlr)
- Line: 185

### at91_usart_spi_remove
- Return type: static void
- Signature: at91_usart_spi_remove(struct platform_device * pdev)
- Line: 632

### at91_usart_spi_resume
- Return type: static __maybe_unused int
- Signature: at91_usart_spi_resume(struct device * dev)
- Line: 615

### at91_usart_spi_runtime_resume
- Return type: static __maybe_unused int
- Signature: at91_usart_spi_runtime_resume(struct device * dev)
- Line: 590

### at91_usart_spi_runtime_suspend
- Return type: static __maybe_unused int
- Signature: at91_usart_spi_runtime_suspend(struct device * dev)
- Line: 579

### at91_usart_spi_rx
- Return type: static void
- Signature: at91_usart_spi_rx(struct at91_usart_spi * aus)
- Line: 298

### at91_usart_spi_rx_ready
- Return type: static u32
- Signature: at91_usart_spi_rx_ready(struct at91_usart_spi * aus)
- Line: 267

### at91_usart_spi_set_xfer_speed
- Return type: static void
- Signature: at91_usart_spi_set_xfer_speed(struct at91_usart_spi * aus,struct spi_transfer * xfer)
- Line: 312

### at91_usart_spi_setup
- Return type: static int
- Signature: at91_usart_spi_setup(struct spi_device * spi)
- Line: 345

### at91_usart_spi_stop_dma
- Return type: static void
- Signature: at91_usart_spi_stop_dma(struct spi_controller * ctlr)
- Line: 193

### at91_usart_spi_suspend
- Return type: static __maybe_unused int
- Signature: at91_usart_spi_suspend(struct device * dev)
- Line: 600

### at91_usart_spi_transfer_one
- Return type: static int
- Signature: at91_usart_spi_transfer_one(struct spi_controller * ctlr,struct spi_device * spi,struct spi_transfer * xfer)
- Line: 383

### at91_usart_spi_tx
- Return type: static void
- Signature: at91_usart_spi_tx(struct at91_usart_spi * aus)
- Line: 283

### at91_usart_spi_tx_ready
- Return type: static u32
- Signature: at91_usart_spi_tx_ready(struct at91_usart_spi * aus)
- Line: 262

### at91_usart_spi_unprepare_message
- Return type: static int
- Signature: at91_usart_spi_unprepare_message(struct spi_controller * ctlr,struct spi_message * message)
- Line: 443

### dma_callback
- Return type: static void
- Signature: dma_callback(void * data)
- Line: 103

## Structs (1)

### at91_usart_spi
- Line: 78
- Members:
  - mpdev: platform_device *
  - current_transfer: spi_transfer *
  - regs: void __iomem *
  - dev: device *
  - clk: clk *
  - xfer_completion: completion
  - lock: spinlock_t
  - phybase: phys_addr_t
  - irq: int
  - current_tx_remaining_bytes: unsigned int
  - current_rx_remaining_bytes: unsigned int
  - spi_clk: u32
  - status: u32
  - xfer_failed: bool
  - use_dma: bool

## Variables (2)

- static **at91_usart_spi_driver** : platform_driver (line 653)
- static **at91_usart_spi_pm_ops** : const struct dev_pm_ops (line 647)

## Macros (39)

- **US_BRGR** (line 30)
- **US_BRGR_SIZE** (line 52)
- **US_CR** (line 23)
- **US_CR_RSTRX** (line 33)
- **US_CR_RSTTX** (line 34)
- **US_CR_RXDIS** (line 36)
- **US_CR_RXEN** (line 35)
- **US_CR_TXDIS** (line 38)
- **US_CR_TXEN** (line 37)
- **US_CSR** (line 27)
- **US_DISABLE** (line 58)
- **US_DMA_MIN_BYTES** (line 64)
- **US_DMA_TIMEOUT** (line 65)
- **US_ENABLE** (line 59)
- **US_IDR** (line 26)
- **US_IER** (line 25)
- **US_INIT** (line 62)
- **US_IR_OVRE** (line 50)
- **US_IR_RXRDY** (line 48)
- **US_IR_TXRDY** (line 49)
- **US_MAX_CLK_DIV** (line 55)
- **US_MIN_CLK_DIV** (line 54)
- **US_MR** (line 24)
- **US_MR_CHRL** (line 41)
- **US_MR_CLKO** (line 44)
- **US_MR_CPHA** (line 42)
- **US_MR_CPOL** (line 43)
- **US_MR_LOOP** (line 46)
- **US_MR_SPI_HOST** (line 40)
- **US_MR_WRDBT** (line 45)
- **US_OVRE_RXRDY_IRQS** (line 60)
- **US_RESET** (line 57)
- **US_RHR** (line 28)
- **US_THR** (line 29)
- **US_VERSION** (line 31)
- **at91_usart_spi_readb**(port,reg) (line 73)
- **at91_usart_spi_readl**(port,reg) (line 68)
- **at91_usart_spi_writeb**(port,reg,value) (line 75)
- **at91_usart_spi_writel**(port,reg,value) (line 70)
