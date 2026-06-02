# drivers/spi/spi-fsl-cpm.c

Subsystem: drivers/spi

## Functions (10)

### fsl_spi_alloc_dummy_rx
- Return type: static void *
- Signature: fsl_spi_alloc_dummy_rx(void)
- Line: 221

### fsl_spi_cpm_bufs
- Return type: int
- Signature: fsl_spi_cpm_bufs(struct mpc8xxx_spi * mspi,struct spi_transfer * t)
- Line: 101

### fsl_spi_cpm_bufs_complete
- Return type: void
- Signature: fsl_spi_cpm_bufs_complete(struct mpc8xxx_spi * mspi)
- Line: 176

### fsl_spi_cpm_bufs_start
- Return type: static void
- Signature: fsl_spi_cpm_bufs_start(struct mpc8xxx_spi * mspi)
- Line: 72

### fsl_spi_cpm_free
- Return type: void
- Signature: fsl_spi_cpm_free(struct mpc8xxx_spi * mspi)
- Line: 402

### fsl_spi_cpm_get_pram
- Return type: static unsigned long
- Signature: fsl_spi_cpm_get_pram(struct mpc8xxx_spi * mspi)
- Line: 255

### fsl_spi_cpm_init
- Return type: int
- Signature: fsl_spi_cpm_init(struct mpc8xxx_spi * mspi)
- Line: 292

### fsl_spi_cpm_irq
- Return type: void
- Signature: fsl_spi_cpm_irq(struct mpc8xxx_spi * mspi,u32 events)
- Line: 196

### fsl_spi_cpm_reinit_txrx
- Return type: void
- Signature: fsl_spi_cpm_reinit_txrx(struct mpc8xxx_spi * mspi)
- Line: 52

### fsl_spi_free_dummy_rx
- Return type: static void
- Signature: fsl_spi_free_dummy_rx(void)
- Line: 235

## Variables (2)

- static **fsl_dummy_rx** : void * (line 48)
- static **fsl_dummy_rx_refcnt** : int (line 50)

## Macros (7)

- **CPM_SPI_CMD** (line 33)
- **CPM_SPI_CMD** (line 36)
- **SPCOM_STR** (line 43)
- **SPIE_RXB** (line 40)
- **SPIE_TXB** (line 39)
- **SPI_MRBLR** (line 46)
- **SPI_PRAM_SIZE** (line 45)
