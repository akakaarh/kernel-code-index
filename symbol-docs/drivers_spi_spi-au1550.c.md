# drivers/spi/spi-au1550.c

Subsystem: drivers/spi

## Functions (19)

### au1550_spi_baudcfg
- Return type: static u32
- Signature: au1550_spi_baudcfg(struct au1550_spi * hw,unsigned int speed_hz)
- Line: 101

### au1550_spi_bits_handlers_set
- Return type: static void
- Signature: au1550_spi_bits_handlers_set(struct au1550_spi * hw,int bpw)
- Line: 640

### au1550_spi_chipsel
- Return type: static void
- Signature: au1550_spi_chipsel(struct spi_device * spi,int value)
- Line: 160

### au1550_spi_dma_irq_callback
- Return type: static irqreturn_t
- Signature: au1550_spi_dma_irq_callback(struct au1550_spi * hw)
- Line: 402

### au1550_spi_dma_rxtmp_alloc
- Return type: static int
- Signature: au1550_spi_dma_rxtmp_alloc(struct au1550_spi * hw,unsigned int size)
- Line: 278

### au1550_spi_dma_rxtmp_free
- Return type: static void
- Signature: au1550_spi_dma_rxtmp_free(struct au1550_spi * hw)
- Line: 295

### au1550_spi_dma_txrxb
- Return type: static int
- Signature: au1550_spi_dma_txrxb(struct spi_device * spi,struct spi_transfer * t)
- Line: 304

### au1550_spi_exit
- Return type: static void __exit
- Signature: au1550_spi_exit(void)
- Line: 973

### au1550_spi_init
- Return type: static int __init
- Signature: au1550_spi_init(void)
- Line: 949

### au1550_spi_irq
- Return type: static irqreturn_t
- Signature: au1550_spi_irq(int irq,void * dev)
- Line: 633

### au1550_spi_mask_ack_all
- Return type: static void
- Signature: au1550_spi_mask_ack_all(struct au1550_spi * hw)
- Line: 124

### au1550_spi_pio_irq_callback
- Return type: static irqreturn_t
- Signature: au1550_spi_pio_irq_callback(struct au1550_spi * hw)
- Line: 536

### au1550_spi_pio_txrxb
- Return type: static void
- Signature: au1550_spi_pio_txrxb(struct spi_device * spi,struct spi_transfer * t)
- Line: 493

### au1550_spi_probe
- Return type: static int
- Signature: au1550_spi_probe(struct platform_device * pdev)
- Line: 714

### au1550_spi_remove
- Return type: static void
- Signature: au1550_spi_remove(struct platform_device * pdev)
- Line: 917

### au1550_spi_reset_fifos
- Return type: static void
- Signature: au1550_spi_reset_fifos(struct au1550_spi * hw)
- Line: 139

### au1550_spi_setup_psc_as_spi
- Return type: static void
- Signature: au1550_spi_setup_psc_as_spi(struct au1550_spi * hw)
- Line: 665

### au1550_spi_setupxfer
- Return type: static int
- Signature: au1550_spi_setupxfer(struct spi_device * spi,struct spi_transfer * t)
- Line: 220

### au1550_spi_txrx_bufs
- Return type: static int
- Signature: au1550_spi_txrx_bufs(struct spi_device * spi,struct spi_transfer * t)
- Line: 626

## Structs (1)

### au1550_spi
- Line: 40
- Members:
  - bitbang: spi_bitbang
  - regs: volatile psc_spi_t __iomem *
  - irq: int
  - len: unsigned int
  - tx_count: unsigned int
  - rx_count: unsigned int
  - tx: const u8 *
  - rx: u8 *
  - rx_word: void (*)(struct au1550_spi * hw)
  - tx_word: void (*)(struct au1550_spi * hw)
  - txrx_bufs: int (*)(struct spi_device * spi,struct spi_transfer * t)
  - irq_callback: irqreturn_t (*)(struct au1550_spi * hw)
  - host_done: completion
  - usedma: unsigned int
  - dma_tx_id: u32
  - dma_rx_id: u32
  - dma_tx_ch: u32
  - dma_rx_ch: u32
  - dma_rx_tmpbuf: u8 *
  - dma_rx_tmpbuf_size: unsigned int
  - dma_rx_tmpbuf_addr: u32
  - host: spi_controller *
  - dev: device *
  - pdata: au1550_spi_info *
  - ioarea: resource *

## Variables (4)

- static **au1550_spi_drv** : platform_driver (line 941)
- static **au1550_spi_mem_dbdev** : dbdev_tab_t (line 77)
- static **ddma_memid** : int (line 87)
- static **usedma** : unsigned int (line 29)

## Macros (4)

- **AU1550_SPI_DBDMA_DESCRIPTORS** (line 37)
- **AU1550_SPI_DMA_RXTMP_MINSIZE** (line 38)
- **AU1550_SPI_RX_WORD**(size,mask) (line 459)
- **AU1550_SPI_TX_WORD**(size,mask) (line 471)
