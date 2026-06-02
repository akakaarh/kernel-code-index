# drivers/spi/spi-cavium.c

Subsystem: drivers/spi

## Functions (3)

### octeon_spi_do_transfer
- Return type: static int
- Signature: octeon_spi_do_transfer(struct octeon_spi * p,struct spi_message * msg,struct spi_transfer * xfer,bool last_xfer)
- Line: 28

### octeon_spi_transfer_one_message
- Return type: int
- Signature: octeon_spi_transfer_one_message(struct spi_controller * ctlr,struct spi_message * msg)
- Line: 127

### octeon_spi_wait_ready
- Return type: static void
- Signature: octeon_spi_wait_ready(struct octeon_spi * p)
- Line: 16
