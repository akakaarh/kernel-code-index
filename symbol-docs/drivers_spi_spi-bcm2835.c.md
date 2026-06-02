# drivers/spi/spi-bcm2835.c

Subsystem: drivers/spi

## Functions (35)

### bcm2835_debugfs_create
- Return type: static void
- Signature: bcm2835_debugfs_create(struct bcm2835_spi * bs,const char * dname)
- Line: 167

### bcm2835_debugfs_create
- Return type: static void
- Signature: bcm2835_debugfs_create(struct bcm2835_spi * bs,const char * dname)
- Line: 197

### bcm2835_debugfs_remove
- Return type: static void
- Signature: bcm2835_debugfs_remove(struct bcm2835_spi * bs)
- Line: 191

### bcm2835_debugfs_remove
- Return type: static void
- Signature: bcm2835_debugfs_remove(struct bcm2835_spi * bs)
- Line: 202

### bcm2835_dma_init
- Return type: static int
- Signature: bcm2835_dma_init(struct spi_controller * ctlr,struct device * dev,struct bcm2835_spi * bs)
- Line: 890

### bcm2835_dma_release
- Return type: static void
- Signature: bcm2835_dma_release(struct spi_controller * ctlr,struct bcm2835_spi * bs)
- Line: 864

### bcm2835_rd
- Return type: static u32
- Signature: bcm2835_rd(struct bcm2835_spi * bs,unsigned int reg)
- Line: 207

### bcm2835_rd_fifo
- Return type: static void
- Signature: bcm2835_rd_fifo(struct bcm2835_spi * bs)
- Line: 217

### bcm2835_rd_fifo_blind
- Return type: static void
- Signature: bcm2835_rd_fifo_blind(struct bcm2835_spi * bs,int count)
- Line: 317

### bcm2835_rd_fifo_count
- Return type: static void
- Signature: bcm2835_rd_fifo_count(struct bcm2835_spi * bs,int count)
- Line: 252

### bcm2835_spi_can_dma
- Return type: static bool
- Signature: bcm2835_spi_can_dma(struct spi_controller * ctlr,struct spi_device * spi,struct spi_transfer * tfr)
- Line: 852

### bcm2835_spi_cleanup
- Return type: static void
- Signature: bcm2835_spi_cleanup(struct spi_device * spi)
- Line: 1150

### bcm2835_spi_dma_rx_done
- Return type: static void
- Signature: bcm2835_spi_dma_rx_done(void * data)
- Line: 607

### bcm2835_spi_dma_tx_done
- Return type: static void
- Signature: bcm2835_spi_dma_tx_done(void * data)
- Line: 635

### bcm2835_spi_handle_err
- Return type: static void
- Signature: bcm2835_spi_handle_err(struct spi_controller * ctlr,struct spi_message * msg)
- Line: 1130

### bcm2835_spi_interrupt
- Return type: static irqreturn_t
- Signature: bcm2835_spi_interrupt(int irq,void * dev_id)
- Line: 374

### bcm2835_spi_max_transfer_size
- Return type: static size_t
- Signature: bcm2835_spi_max_transfer_size(struct spi_device * spi)
- Line: 1210

### bcm2835_spi_prepare_message
- Return type: static int
- Signature: bcm2835_spi_prepare_message(struct spi_controller * ctlr,struct spi_message * msg)
- Line: 1114

### bcm2835_spi_prepare_sg
- Return type: static int
- Signature: bcm2835_spi_prepare_sg(struct spi_controller * ctlr,struct spi_transfer * tfr,struct bcm2835_spi * bs,struct bcm2835_spidev * target,bool is_tx)
- Line: 671

### bcm2835_spi_probe
- Return type: static int
- Signature: bcm2835_spi_probe(struct platform_device * pdev)
- Line: 1349

### bcm2835_spi_remove
- Return type: static void
- Signature: bcm2835_spi_remove(struct platform_device * pdev)
- Line: 1423

### bcm2835_spi_reset_hw
- Return type: static void
- Signature: bcm2835_spi_reset_hw(struct bcm2835_spi * bs)
- Line: 349

### bcm2835_spi_setup
- Return type: static int
- Signature: bcm2835_spi_setup(struct spi_device * spi)
- Line: 1223

### bcm2835_spi_setup_dma
- Return type: static int
- Signature: bcm2835_spi_setup_dma(struct spi_controller * ctlr,struct spi_device * spi,struct bcm2835_spi * bs,struct bcm2835_spidev * target)
- Line: 1172

### bcm2835_spi_transfer_one
- Return type: static int
- Signature: bcm2835_spi_transfer_one(struct spi_controller * ctlr,struct spi_device * spi,struct spi_transfer * tfr)
- Line: 1052

### bcm2835_spi_transfer_one_dma
- Return type: static int
- Signature: bcm2835_spi_transfer_one_dma(struct spi_controller * ctlr,struct spi_transfer * tfr,struct bcm2835_spidev * target,u32 cs)
- Line: 770

### bcm2835_spi_transfer_one_irq
- Return type: static int
- Signature: bcm2835_spi_transfer_one_irq(struct spi_controller * ctlr,struct spi_device * spi,struct spi_transfer * tfr,u32 cs,bool fifo_empty)
- Line: 410

### bcm2835_spi_transfer_one_poll
- Return type: static int
- Signature: bcm2835_spi_transfer_one_poll(struct spi_controller * ctlr,struct spi_device * spi,struct spi_transfer * tfr,u32 cs)
- Line: 997

### bcm2835_spi_transfer_prologue
- Return type: static void
- Signature: bcm2835_spi_transfer_prologue(struct spi_controller * ctlr,struct spi_transfer * tfr,struct bcm2835_spi * bs,u32 cs)
- Line: 485

### bcm2835_spi_undo_prologue
- Return type: static void
- Signature: bcm2835_spi_undo_prologue(struct bcm2835_spi * bs)
- Line: 574

### bcm2835_wait_tx_fifo_empty
- Return type: static void
- Signature: bcm2835_wait_tx_fifo_empty(struct bcm2835_spi * bs)
- Line: 306

### bcm2835_wr
- Return type: static void
- Signature: bcm2835_wr(struct bcm2835_spi * bs,unsigned int reg,u32 val)
- Line: 212

### bcm2835_wr_fifo
- Return type: static void
- Signature: bcm2835_wr_fifo(struct bcm2835_spi * bs)
- Line: 230

### bcm2835_wr_fifo_blind
- Return type: static void
- Signature: bcm2835_wr_fifo_blind(struct bcm2835_spi * bs,int count)
- Line: 336

### bcm2835_wr_fifo_count
- Return type: static void
- Signature: bcm2835_wr_fifo_count(struct bcm2835_spi * bs,int count)
- Line: 278

## Structs (2)

### bcm2835_spi
- Line: 120
- Members:
  - regs: void __iomem *
  - clk: clk *
  - cs_gpio: gpio_desc *
  - clk_hz: unsigned long
  - irq: int
  - tfr: spi_transfer *
  - ctlr: spi_controller *
  - tx_buf: const u8 *
  - rx_buf: u8 *
  - tx_len: int
  - rx_len: int
  - tx_prologue: int
  - rx_prologue: int
  - tx_spillover: unsigned int
  - debugfs_dir: dentry *
  - count_transfer_polling: u64
  - count_transfer_irq: u64
  - count_transfer_irq_after_polling: u64
  - count_transfer_dma: u64
  - target: bcm2835_spidev *
  - tx_dma_active: unsigned int
  - rx_dma_active: unsigned int
  - fill_tx_desc: dma_async_tx_descriptor *
  - fill_tx_addr: dma_addr_t
  - prepare_cs: u32
  - clear_rx_desc: dma_async_tx_descriptor *
  - clear_rx_addr: dma_addr_t
  - ____cacheline_aligned: u32 clear_rx_cs

### bcm2835_spidev
- Line: 159
- Members:
  - regs: void __iomem *
  - clk: clk *
  - cs_gpio: gpio_desc *
  - clk_hz: unsigned long
  - irq: int
  - tfr: spi_transfer *
  - ctlr: spi_controller *
  - tx_buf: const u8 *
  - rx_buf: u8 *
  - tx_len: int
  - rx_len: int
  - tx_prologue: int
  - rx_prologue: int
  - tx_spillover: unsigned int
  - debugfs_dir: dentry *
  - count_transfer_polling: u64
  - count_transfer_irq: u64
  - count_transfer_irq_after_polling: u64
  - count_transfer_dma: u64
  - target: bcm2835_spidev *
  - tx_dma_active: unsigned int
  - rx_dma_active: unsigned int
  - fill_tx_desc: dma_async_tx_descriptor *
  - fill_tx_addr: dma_addr_t
  - prepare_cs: u32
  - clear_rx_desc: dma_async_tx_descriptor *
  - clear_rx_addr: dma_addr_t
  - ____cacheline_aligned: u32 clear_rx_cs

## Variables (3)

- static **bcm2835_spi_driver** : platform_driver (line 1445)
- static **bcm2835_spi_match** : const struct of_device_id[] (line 1439)
- static **polling_limit_us** : unsigned int (line 79)

## Macros (35)

- **BCM2835_SPI_CLK** (line 39)
- **BCM2835_SPI_CS** (line 37)
- **BCM2835_SPI_CS_ADCS** (line 57)
- **BCM2835_SPI_CS_CLEAR_RX** (line 63)
- **BCM2835_SPI_CS_CLEAR_TX** (line 64)
- **BCM2835_SPI_CS_CPHA** (line 66)
- **BCM2835_SPI_CS_CPOL** (line 65)
- **BCM2835_SPI_CS_CSPOL** (line 62)
- **BCM2835_SPI_CS_CSPOL0** (line 49)
- **BCM2835_SPI_CS_CSPOL1** (line 48)
- **BCM2835_SPI_CS_CSPOL2** (line 47)
- **BCM2835_SPI_CS_CS_01** (line 68)
- **BCM2835_SPI_CS_CS_10** (line 67)
- **BCM2835_SPI_CS_DMAEN** (line 60)
- **BCM2835_SPI_CS_DMA_LEN** (line 46)
- **BCM2835_SPI_CS_DONE** (line 54)
- **BCM2835_SPI_CS_INTD** (line 59)
- **BCM2835_SPI_CS_INTR** (line 58)
- **BCM2835_SPI_CS_LEN** (line 55)
- **BCM2835_SPI_CS_LEN_LONG** (line 45)
- **BCM2835_SPI_CS_REN** (line 56)
- **BCM2835_SPI_CS_RXD** (line 53)
- **BCM2835_SPI_CS_RXF** (line 50)
- **BCM2835_SPI_CS_RXR** (line 51)
- **BCM2835_SPI_CS_TA** (line 61)
- **BCM2835_SPI_CS_TXD** (line 52)
- **BCM2835_SPI_DC** (line 42)
- **BCM2835_SPI_DLEN** (line 40)
- **BCM2835_SPI_DMA_MIN_LENGTH** (line 72)
- **BCM2835_SPI_FIFO** (line 38)
- **BCM2835_SPI_FIFO_SIZE** (line 70)
- **BCM2835_SPI_FIFO_SIZE_3_4** (line 71)
- **BCM2835_SPI_LTOH** (line 41)
- **BCM2835_SPI_MODE_BITS** (line 73)
- **DRV_NAME** (line 76)
