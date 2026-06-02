# drivers/spi/spi-ep93xx.c

Subsystem: drivers/spi

## Functions (19)

### ep93xx_dma_data_to_trans_dir
- Return type: static dma_transfer_direction
- Signature: ep93xx_dma_data_to_trans_dir(enum dma_data_direction dir)
- Line: 246

### ep93xx_do_read
- Return type: static void
- Signature: ep93xx_do_read(struct spi_controller * host)
- Line: 193

### ep93xx_do_write
- Return type: static void
- Signature: ep93xx_do_write(struct spi_controller * host)
- Line: 175

### ep93xx_spi_calc_divisors
- Return type: static int
- Signature: ep93xx_spi_calc_divisors(struct spi_controller * host,u32 rate,u8 * div_cpsr,u8 * div_scr)
- Line: 108

### ep93xx_spi_chip_setup
- Return type: static int
- Signature: ep93xx_spi_chip_setup(struct spi_controller * host,struct spi_device * spi,struct spi_transfer * xfer)
- Line: 142

### ep93xx_spi_dma_callback
- Return type: static void
- Signature: ep93xx_spi_dma_callback(void * callback_param)
- Line: 390

### ep93xx_spi_dma_finish
- Return type: static void
- Signature: ep93xx_spi_dma_finish(struct spi_controller * host,enum dma_data_direction dir)
- Line: 372

### ep93xx_spi_dma_prepare
- Return type: static dma_async_tx_descriptor *
- Signature: ep93xx_spi_dma_prepare(struct spi_controller * host,enum dma_data_direction dir)
- Line: 268

### ep93xx_spi_dma_transfer
- Return type: static int
- Signature: ep93xx_spi_dma_transfer(struct spi_controller * host)
- Line: 400

### ep93xx_spi_interrupt
- Return type: static irqreturn_t
- Signature: ep93xx_spi_interrupt(int irq,void * dev_id)
- Line: 433

### ep93xx_spi_prepare_hardware
- Return type: static int
- Signature: ep93xx_spi_prepare_hardware(struct spi_controller * host)
- Line: 543

### ep93xx_spi_prepare_message
- Return type: static int
- Signature: ep93xx_spi_prepare_message(struct spi_controller * host,struct spi_message * msg)
- Line: 515

### ep93xx_spi_probe
- Return type: static int
- Signature: ep93xx_spi_probe(struct platform_device * pdev)
- Line: 622

### ep93xx_spi_read_write
- Return type: static int
- Signature: ep93xx_spi_read_write(struct spi_controller * host)
- Line: 222

### ep93xx_spi_release_dma
- Return type: static void
- Signature: ep93xx_spi_release_dma(struct ep93xx_spi * espi)
- Line: 607

### ep93xx_spi_remove
- Return type: static void
- Signature: ep93xx_spi_remove(struct platform_device * pdev)
- Line: 713

### ep93xx_spi_setup_dma
- Return type: static int
- Signature: ep93xx_spi_setup_dma(struct device * dev,struct ep93xx_spi * espi)
- Line: 574

### ep93xx_spi_transfer_one
- Return type: static int
- Signature: ep93xx_spi_transfer_one(struct spi_controller * host,struct spi_device * spi,struct spi_transfer * xfer)
- Line: 478

### ep93xx_spi_unprepare_hardware
- Return type: static int
- Signature: ep93xx_spi_unprepare_hardware(struct spi_controller * host)
- Line: 560

## Structs (1)

### ep93xx_spi
- Line: 84
- Members:
  - clk: clk *
  - mmio: void __iomem *
  - sspdr_phys: unsigned long
  - tx: size_t
  - rx: size_t
  - fifo_level: size_t
  - dma_rx: dma_chan *
  - dma_tx: dma_chan *
  - rx_sgt: sg_table
  - tx_sgt: sg_table
  - zeropage: void *

## Variables (2)

- static **ep93xx_spi_driver** : platform_driver (line 733)
- static **ep93xx_spi_of_ids** : const struct of_device_id[] (line 727)

## Macros (28)

- **SPI_FIFO_SIZE** (line 66)
- **SPI_TIMEOUT** (line 64)
- **SSPCPSR** (line 55)
- **SSPCR0** (line 33)
- **SSPCR0_SCR_SHIFT** (line 36)
- **SSPCR0_SPH** (line 35)
- **SSPCR0_SPO** (line 34)
- **SSPCR1** (line 38)
- **SSPCR1_LBM** (line 42)
- **SSPCR1_MS** (line 44)
- **SSPCR1_RIE** (line 39)
- **SSPCR1_RORIE** (line 41)
- **SSPCR1_SOD** (line 45)
- **SSPCR1_SSE** (line 43)
- **SSPCR1_TIE** (line 40)
- **SSPDR** (line 47)
- **SSPICR** (line 61)
- **SSPIIR** (line 57)
- **SSPIIR_RIS** (line 58)
- **SSPIIR_RORIS** (line 60)
- **SSPIIR_TIS** (line 59)
- **SSPSR** (line 49)
- **SSPSR_BSY** (line 54)
- **SSPSR_RFF** (line 53)
- **SSPSR_RNE** (line 52)
- **SSPSR_TFE** (line 50)
- **SSPSR_TNF** (line 51)
- **bits_per_word_to_dss**(bpw) (line 99)
