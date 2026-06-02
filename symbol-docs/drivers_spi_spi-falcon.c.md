# drivers/spi/spi-falcon.c

Subsystem: drivers/spi

## Functions (4)

### falcon_sflash_probe
- Return type: static int
- Signature: falcon_sflash_probe(struct platform_device * pdev)
- Line: 391

### falcon_sflash_setup
- Return type: static int
- Signature: falcon_sflash_setup(struct spi_device * spi)
- Line: 308

### falcon_sflash_xfer
- Return type: static int
- Signature: falcon_sflash_xfer(struct spi_device * spi,struct spi_transfer * t,unsigned long flags)
- Line: 98

### falcon_sflash_xfer_one
- Return type: static int
- Signature: falcon_sflash_xfer_one(struct spi_controller * host,struct spi_message * m)
- Line: 355

## Structs (1)

### falcon_sflash
- Line: 92
- Members:
  - sfcmd: u32
  - host: spi_controller *

## Enums (1)

### __anonc79b7ab50103
- Line: 108

## Variables (2)

- static **falcon_sflash_driver** : platform_driver (line 421)
- static **falcon_sflash_match** : const struct of_device_id[] (line 415)

## Macros (41)

- **BUSRCON0** (line 23)
- **BUSRCON0_AGEN_SERIAL_FLASH** (line 81)
- **BUSRCON0_PORTW_8_BIT_MUX** (line 83)
- **BUSWCON0** (line 25)
- **BUSWCON0_AGEN_SERIAL_FLASH** (line 85)
- **CLOCK_100M** (line 89)
- **CLOCK_50M** (line 90)
- **DRV_NAME** (line 17)
- **EBUCC** (line 41)
- **EBUCC_EBUDIV_SELF100** (line 79)
- **FALCON_SPI_XFER_BEGIN** (line 19)
- **FALCON_SPI_XFER_END** (line 20)
- **SFADDR** (line 35)
- **SFCMD** (line 33)
- **SFCMD_ALEN_MASK** (line 51)
- **SFCMD_ALEN_OFFSET** (line 50)
- **SFCMD_CS_MASK** (line 48)
- **SFCMD_CS_OFFSET** (line 47)
- **SFCMD_DIR_WRITE** (line 71)
- **SFCMD_DLEN_OFFSET** (line 73)
- **SFCMD_DUMLEN_MASK** (line 45)
- **SFCMD_DUMLEN_OFFSET** (line 44)
- **SFCMD_KEEP_CS_KEEP_SELECTED** (line 87)
- **SFCMD_OPC_MASK** (line 69)
- **SFCON** (line 27)
- **SFCON_DEV_SIZE_A23_0** (line 62)
- **SFCON_DEV_SIZE_MASK** (line 63)
- **SFDATA** (line 37)
- **SFIO** (line 39)
- **SFIO_UNUSED_WD_MASK** (line 67)
- **SFSTAT** (line 31)
- **SFSTAT_CMD_ERR** (line 75)
- **SFSTAT_CMD_PEND** (line 77)
- **SFTIME** (line 29)
- **SFTIME_RD_POS_MASK** (line 65)
- **SFTIME_SCKF_POS_MASK** (line 60)
- **SFTIME_SCKF_POS_OFFSET** (line 59)
- **SFTIME_SCKR_POS_MASK** (line 54)
- **SFTIME_SCKR_POS_OFFSET** (line 53)
- **SFTIME_SCK_PER_MASK** (line 57)
- **SFTIME_SCK_PER_OFFSET** (line 56)
