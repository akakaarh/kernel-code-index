# drivers/mmc/host/of_mmc_spi.c

Subsystem: drivers/mmc

## Functions (5)

### mmc_spi_get_pdata
- Return type: mmc_spi_platform_data *
- Signature: mmc_spi_get_pdata(struct spi_device * spi)
- Line: 51

### mmc_spi_put_pdata
- Return type: void
- Signature: mmc_spi_put_pdata(struct spi_device * spi)
- Line: 87

### of_mmc_spi_exit
- Return type: static void
- Signature: of_mmc_spi_exit(struct device * dev,void * mmc)
- Line: 44

### of_mmc_spi_init
- Return type: static int
- Signature: of_mmc_spi_init(struct device * dev,irqreturn_t (* irqhandler)(int,void *),void * mmc)
- Line: 35

### to_of_mmc_spi
- Return type: static of_mmc_spi *
- Signature: to_of_mmc_spi(struct device * dev)
- Line: 30

## Structs (1)

### of_mmc_spi
- Line: 25
- Members:
  - pdata: mmc_spi_platform_data
  - detect_irq: int
