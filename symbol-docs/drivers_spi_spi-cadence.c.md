# drivers/spi/spi-cadence.c

Subsystem: drivers/spi

## Functions (24)

### cdns_prepare_message
- Return type: static int
- Signature: cdns_prepare_message(struct spi_controller * ctlr,struct spi_message * msg)
- Line: 481

### cdns_prepare_transfer_hardware
- Return type: static int
- Signature: cdns_prepare_transfer_hardware(struct spi_controller * ctlr)
- Line: 548

### cdns_spi_chipselect
- Return type: static void
- Signature: cdns_spi_chipselect(struct spi_device * spi,bool is_high)
- Line: 192

### cdns_spi_config_clock_freq
- Return type: static void
- Signature: cdns_spi_config_clock_freq(struct spi_device * spi,struct spi_transfer * transfer)
- Line: 265

### cdns_spi_config_clock_mode
- Return type: static void
- Signature: cdns_spi_config_clock_mode(struct spi_device * spi)
- Line: 223

### cdns_spi_detect_fifo_depth
- Return type: static void
- Signature: cdns_spi_detect_fifo_depth(struct cdns_spi * xspi)
- Line: 597

### cdns_spi_init_hw
- Return type: static void
- Signature: cdns_spi_init_hw(struct cdns_spi * xspi,bool is_target)
- Line: 165

### cdns_spi_irq
- Return type: static irqreturn_t
- Signature: cdns_spi_irq(int irq,void * dev_id)
- Line: 430

### cdns_spi_n_bytes
- Return type: static u8
- Signature: cdns_spi_n_bytes(struct spi_transfer * transfer)
- Line: 317

### cdns_spi_probe
- Return type: static int
- Signature: cdns_spi_probe(struct platform_device * pdev)
- Line: 636

### cdns_spi_process_fifo
- Return type: static void
- Signature: cdns_spi_process_fifo(struct cdns_spi * xspi,int ntx,int nrx)
- Line: 395

### cdns_spi_read
- Return type: static u32
- Signature: cdns_spi_read(struct cdns_spi * xspi,u32 offset)
- Line: 143

### cdns_spi_reader
- Return type: static void
- Signature: cdns_spi_reader(struct cdns_spi * xspi)
- Line: 327

### cdns_spi_remove
- Return type: static void
- Signature: cdns_spi_remove(struct platform_device * pdev)
- Line: 779

### cdns_spi_resume
- Return type: static int __maybe_unused
- Signature: cdns_spi_resume(struct device * dev)
- Line: 829

### cdns_spi_runtime_resume
- Return type: static int __maybe_unused
- Signature: cdns_spi_runtime_resume(struct device * dev)
- Line: 846

### cdns_spi_runtime_suspend
- Return type: static int __maybe_unused
- Signature: cdns_spi_runtime_suspend(struct device * dev)
- Line: 875

### cdns_spi_setup_transfer
- Return type: static int
- Signature: cdns_spi_setup_transfer(struct spi_device * spi,struct spi_transfer * transfer)
- Line: 303

### cdns_spi_suspend
- Return type: static int __maybe_unused
- Signature: cdns_spi_suspend(struct device * dev)
- Line: 814

### cdns_spi_write
- Return type: static void
- Signature: cdns_spi_write(struct cdns_spi * xspi,u32 offset,u32 val)
- Line: 148

### cdns_spi_writer
- Return type: static void
- Signature: cdns_spi_writer(struct cdns_spi * xspi)
- Line: 358

### cdns_target_abort
- Return type: static int
- Signature: cdns_target_abort(struct spi_controller * ctlr)
- Line: 615

### cdns_transfer_one
- Return type: static int
- Signature: cdns_transfer_one(struct spi_controller * ctlr,struct spi_device * spi,struct spi_transfer * transfer)
- Line: 502

### cdns_unprepare_transfer_hardware
- Return type: static int
- Signature: cdns_unprepare_transfer_hardware(struct spi_controller * ctlr)
- Line: 567

## Structs (1)

### cdns_spi
- Line: 118
- Members:
  - regs: void __iomem *
  - ref_clk: clk *
  - pclk: clk *
  - clk_rate: unsigned int
  - speed_hz: u32
  - txbuf: const void *
  - rxbuf: void *
  - tx_bytes: int
  - rx_bytes: int
  - n_bytes: u8
  - dev_busy: u8
  - is_decoded_cs: u32
  - tx_fifo_depth: unsigned int
  - rstc: reset_control *

## Enums (1)

### cdns_spi_frame_n_bytes
- Line: 135

## Variables (3)

- static **cdns_spi_dev_pm_ops** : const struct dev_pm_ops (line 886)
- static **cdns_spi_driver** : platform_driver (line 901)
- static **cdns_spi_of_match** : const struct of_device_id[] (line 892)

## Macros (39)

- **CDNS_SPI_BAUD_DIV_MAX** (line 69)
- **CDNS_SPI_BAUD_DIV_MIN** (line 70)
- **CDNS_SPI_BAUD_DIV_SHIFT** (line 71)
- **CDNS_SPI_CR** (line 28)
- **CDNS_SPI_CR_BAUD_DIV** (line 52)
- **CDNS_SPI_CR_BAUD_DIV_4** (line 56)
- **CDNS_SPI_CR_CPHA** (line 48)
- **CDNS_SPI_CR_CPOL** (line 49)
- **CDNS_SPI_CR_DEFAULT** (line 57)
- **CDNS_SPI_CR_MANSTRT** (line 47)
- **CDNS_SPI_CR_MANSTRTEN** (line 54)
- **CDNS_SPI_CR_MSTREN** (line 53)
- **CDNS_SPI_CR_PERI_SEL** (line 51)
- **CDNS_SPI_CR_SSCTRL** (line 50)
- **CDNS_SPI_CR_SSFORCE** (line 55)
- **CDNS_SPI_DEFAULT_NUM_CS** (line 99)
- **CDNS_SPI_DR** (line 34)
- **CDNS_SPI_ER** (line 33)
- **CDNS_SPI_ER_DISABLE** (line 96)
- **CDNS_SPI_ER_ENABLE** (line 95)
- **CDNS_SPI_IDR** (line 31)
- **CDNS_SPI_IER** (line 30)
- **CDNS_SPI_IMR** (line 32)
- **CDNS_SPI_ISR** (line 29)
- **CDNS_SPI_IXR_ALL** (line 88)
- **CDNS_SPI_IXR_DEFAULT** (line 85)
- **CDNS_SPI_IXR_MODF** (line 83)
- **CDNS_SPI_IXR_RXNEMTY** (line 84)
- **CDNS_SPI_IXR_TXFULL** (line 87)
- **CDNS_SPI_IXR_TXOW** (line 82)
- **CDNS_SPI_NAME** (line 25)
- **CDNS_SPI_NOSS** (line 74)
- **CDNS_SPI_RXD** (line 36)
- **CDNS_SPI_SICR** (line 37)
- **CDNS_SPI_SS0** (line 73)
- **CDNS_SPI_SS_SHIFT** (line 72)
- **CDNS_SPI_THLD** (line 38)
- **CDNS_SPI_TXD** (line 35)
- **SPI_AUTOSUSPEND_TIMEOUT** (line 40)
