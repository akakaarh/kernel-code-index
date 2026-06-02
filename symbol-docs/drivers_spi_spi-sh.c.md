# drivers/spi/spi-sh.c

Subsystem: drivers/spi

## Functions (15)

### clear_fifo
- Return type: static void
- Signature: clear_fifo(struct spi_sh_data * ss)
- Line: 120

### spi_sh_cleanup
- Return type: static void
- Signature: spi_sh_cleanup(struct spi_device * spi)
- Line: 347

### spi_sh_clear_bit
- Return type: static void
- Signature: spi_sh_clear_bit(struct spi_sh_data * ss,unsigned long val,unsigned long offset)
- Line: 110

### spi_sh_irq
- Return type: static irqreturn_t
- Signature: spi_sh_irq(int irq,void * _ss)
- Line: 357

### spi_sh_probe
- Return type: static int
- Signature: spi_sh_probe(struct platform_device * pdev)
- Line: 388

### spi_sh_read
- Return type: static unsigned long
- Signature: spi_sh_read(struct spi_sh_data * ss,unsigned long offset)
- Line: 90

### spi_sh_receive
- Return type: static int
- Signature: spi_sh_receive(struct spi_sh_data * ss,struct spi_message * mesg,struct spi_transfer * t)
- Line: 215

### spi_sh_remove
- Return type: static void
- Signature: spi_sh_remove(struct platform_device * pdev)
- Line: 380

### spi_sh_send
- Return type: static int
- Signature: spi_sh_send(struct spi_sh_data * ss,struct spi_message * mesg,struct spi_transfer * t)
- Line: 150

### spi_sh_set_bit
- Return type: static void
- Signature: spi_sh_set_bit(struct spi_sh_data * ss,unsigned long val,unsigned long offset)
- Line: 100

### spi_sh_setup
- Return type: static int
- Signature: spi_sh_setup(struct spi_device * spi)
- Line: 328

### spi_sh_transfer_one_message
- Return type: static int
- Signature: spi_sh_transfer_one_message(struct spi_controller * ctlr,struct spi_message * mesg)
- Line: 271

### spi_sh_wait_receive_buffer
- Return type: static int
- Signature: spi_sh_wait_receive_buffer(struct spi_sh_data * ss)
- Line: 126

### spi_sh_wait_write_buffer_empty
- Return type: static int
- Signature: spi_sh_wait_write_buffer_empty(struct spi_sh_data * ss)
- Line: 138

### spi_sh_write
- Return type: static void
- Signature: spi_sh_write(struct spi_sh_data * ss,unsigned long data,unsigned long offset)
- Line: 81

## Structs (1)

### spi_sh_data
- Line: 72
- Members:
  - addr: void __iomem *
  - irq: int
  - host: spi_controller *
  - cr1: unsigned long
  - wait: wait_queue_head_t
  - width: int

## Variables (1)

- static **spi_sh_driver** : platform_driver (line 460)

## Macros (34)

- **SPI_SH_CPHA** (line 46)
- **SPI_SH_CPOL** (line 45)
- **SPI_SH_CR1** (line 26)
- **SPI_SH_CR2** (line 27)
- **SPI_SH_CR3** (line 28)
- **SPI_SH_CR4** (line 29)
- **SPI_SH_CR5** (line 30)
- **SPI_SH_FIFO_SIZE** (line 66)
- **SPI_SH_L1M0** (line 47)
- **SPI_SH_LOOPBK** (line 44)
- **SPI_SH_MAX_BYTE** (line 50)
- **SPI_SH_MUXI** (line 63)
- **SPI_SH_MUXIRQ** (line 64)
- **SPI_SH_P1L0** (line 61)
- **SPI_SH_PFONRD** (line 37)
- **SPI_SH_PP1L0** (line 62)
- **SPI_SH_RBE** (line 35)
- **SPI_SH_RBEI** (line 55)
- **SPI_SH_RBF** (line 36)
- **SPI_SH_RBFI** (line 56)
- **SPI_SH_RBR** (line 25)
- **SPI_SH_RECEIVE_TIMEOUT** (line 68)
- **SPI_SH_RSTF** (line 43)
- **SPI_SH_SEND_TIMEOUT** (line 67)
- **SPI_SH_SSA** (line 40)
- **SPI_SH_SSD** (line 39)
- **SPI_SH_SSDB** (line 38)
- **SPI_SH_SSS** (line 58)
- **SPI_SH_TBE** (line 33)
- **SPI_SH_TBEI** (line 53)
- **SPI_SH_TBF** (line 34)
- **SPI_SH_TBFI** (line 54)
- **SPI_SH_TBR** (line 24)
- **SPI_SH_WPABRT** (line 57)
