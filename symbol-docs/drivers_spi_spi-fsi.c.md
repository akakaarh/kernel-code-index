# drivers/spi/spi-fsi.c

Subsystem: drivers/spi

## Functions (15)

### fsi_spi_check_mux
- Return type: static int
- Signature: fsi_spi_check_mux(struct fsi_device * fsi,struct device * dev)
- Line: 86

### fsi_spi_check_status
- Return type: static int
- Signature: fsi_spi_check_status(struct fsi_spi * ctx)
- Line: 106

### fsi_spi_data_in
- Return type: static int
- Signature: fsi_spi_data_in(u64 in,u8 * rx,int len)
- Line: 215

### fsi_spi_data_out
- Return type: static int
- Signature: fsi_spi_data_out(u64 * out,const u8 * tx,int len)
- Line: 226

### fsi_spi_max_transfer_size
- Return type: static size_t
- Signature: fsi_spi_max_transfer_size(struct spi_device * spi)
- Line: 526

### fsi_spi_probe
- Return type: static int
- Signature: fsi_spi_probe(struct fsi_device * fsi)
- Line: 531

### fsi_spi_read_reg
- Return type: static int
- Signature: fsi_spi_read_reg(struct fsi_spi * ctx,u32 offset,u64 * value)
- Line: 126

### fsi_spi_reset
- Return type: static int
- Signature: fsi_spi_reset(struct fsi_spi * ctx)
- Line: 241

### fsi_spi_sequence_add
- Return type: static void
- Signature: fsi_spi_sequence_add(struct fsi_spi_sequence * seq,u8 val)
- Line: 280

### fsi_spi_sequence_init
- Return type: static void
- Signature: fsi_spi_sequence_init(struct fsi_spi_sequence * seq)
- Line: 292

### fsi_spi_status
- Return type: static int
- Signature: fsi_spi_status(struct fsi_spi * ctx,u64 * status,const char * dir)
- Line: 260

### fsi_spi_transfer_data
- Return type: static int
- Signature: fsi_spi_transfer_data(struct fsi_spi * ctx,struct spi_transfer * transfer)
- Line: 298

### fsi_spi_transfer_init
- Return type: static int
- Signature: fsi_spi_transfer_init(struct fsi_spi * ctx)
- Line: 362

### fsi_spi_transfer_one_message
- Return type: static int
- Signature: fsi_spi_transfer_one_message(struct spi_controller * ctlr,struct spi_message * mesg)
- Line: 424

### fsi_spi_write_reg
- Return type: static int
- Signature: fsi_spi_write_reg(struct fsi_spi * ctx,u32 offset,u64 value)
- Line: 173

## Structs (3)

### fsi2spi
- Line: 70
- Members:
  - fsi: fsi_device *
  - lock: mutex
  - dev: device *
  - bridge: fsi2spi *
  - base: u32
  - bit: int
  - data: u64

### fsi_spi
- Line: 75
- Members:
  - fsi: fsi_device *
  - lock: mutex
  - dev: device *
  - bridge: fsi2spi *
  - base: u32
  - bit: int
  - data: u64

### fsi_spi_sequence
- Line: 81
- Members:
  - fsi: fsi_device *
  - lock: mutex
  - dev: device *
  - bridge: fsi2spi *
  - base: u32
  - bit: int
  - data: u64

## Variables (2)

- static **fsi_spi_driver** : fsi_driver (line 591)
- static **fsi_spi_ids** : const struct fsi_device_id[] (line 585)

## Macros (49)

- **FSI2SPI_CMD** (line 19)
- **FSI2SPI_CMD_WRITE** (line 20)
- **FSI2SPI_DATA0** (line 17)
- **FSI2SPI_DATA1** (line 18)
- **FSI2SPI_IRQ** (line 24)
- **FSI2SPI_RESET** (line 21)
- **FSI2SPI_STATUS** (line 22)
- **FSI2SPI_STATUS_ANY_ERROR** (line 23)
- **FSI_ENGID_SPI** (line 13)
- **FSI_MBOX_ROOT_CTRL_8** (line 14)
- **FSI_MBOX_ROOT_CTRL_8_SPI_MUX** (line 15)
- **SPI_FSI_BASE** (line 26)
- **SPI_FSI_CFG1** (line 33)
- **SPI_FSI_CLOCK_CFG** (line 34)
- **SPI_FSI_CLOCK_CFG_ECC_DISABLE** (line 36)
- **SPI_FSI_CLOCK_CFG_MM_ENABLE** (line 35)
- **SPI_FSI_CLOCK_CFG_MODE** (line 39)
- **SPI_FSI_CLOCK_CFG_RESET1** (line 37)
- **SPI_FSI_CLOCK_CFG_RESET2** (line 38)
- **SPI_FSI_CLOCK_CFG_SCK_DIV** (line 42)
- **SPI_FSI_CLOCK_CFG_SCK_NO_DEL** (line 41)
- **SPI_FSI_CLOCK_CFG_SCK_RECV_DEL** (line 40)
- **SPI_FSI_COUNTER_CFG** (line 32)
- **SPI_FSI_DATA_RX** (line 45)
- **SPI_FSI_DATA_TX** (line 44)
- **SPI_FSI_ERROR** (line 31)
- **SPI_FSI_MAX_RX_SIZE** (line 28)
- **SPI_FSI_MAX_TX_SIZE** (line 29)
- **SPI_FSI_MMAP** (line 43)
- **SPI_FSI_PORT_CTRL** (line 68)
- **SPI_FSI_SEQUENCE** (line 46)
- **SPI_FSI_SEQUENCE_BRANCH**(x) (line 52)
- **SPI_FSI_SEQUENCE_COPY_DATA_TX** (line 51)
- **SPI_FSI_SEQUENCE_SEL_SLAVE**(x) (line 48)
- **SPI_FSI_SEQUENCE_SHIFT_IN**(x) (line 50)
- **SPI_FSI_SEQUENCE_SHIFT_OUT**(x) (line 49)
- **SPI_FSI_SEQUENCE_STOP** (line 47)
- **SPI_FSI_STATUS** (line 53)
- **SPI_FSI_STATUS_ANY_ERROR** (line 64)
- **SPI_FSI_STATUS_ERROR** (line 54)
- **SPI_FSI_STATUS_RDR_FULL** (line 63)
- **SPI_FSI_STATUS_RDR_OVERRUN** (line 62)
- **SPI_FSI_STATUS_RDR_UNDERRUN** (line 61)
- **SPI_FSI_STATUS_SEQ_STATE** (line 56)
- **SPI_FSI_STATUS_SEQ_STATE_IDLE** (line 57)
- **SPI_FSI_STATUS_TDR_FULL** (line 60)
- **SPI_FSI_STATUS_TDR_OVERRUN** (line 59)
- **SPI_FSI_STATUS_TDR_UNDERRUN** (line 58)
- **SPI_FSI_TIMEOUT_MS** (line 27)
