# drivers/mmc/host/mmc_spi.c

Subsystem: drivers/mmc

## Functions (19)

### maptype
- Return type: static char *
- Signature: maptype(struct mmc_command * cmd)
- Line: 202

### mmc_cs_off
- Return type: static int
- Signature: mmc_cs_off(struct mmc_spi_host * host)
- Line: 138

### mmc_powerstring
- Return type: static char *
- Signature: mmc_powerstring(u8 power_mode)
- Line: 1023

### mmc_spi_command_send
- Return type: static int
- Signature: mmc_spi_command_send(struct mmc_spi_host * host,struct mmc_request * mrq,struct mmc_command * cmd,int cs_on)
- Line: 398

### mmc_spi_data_do
- Return type: static void
- Signature: mmc_spi_data_do(struct mmc_spi_host * host,struct mmc_command * cmd,struct mmc_data * data,u32 blk_size)
- Line: 768

### mmc_spi_detect_irq
- Return type: static irqreturn_t
- Signature: mmc_spi_detect_irq(int irq,void * mmc)
- Line: 1135

### mmc_spi_initsequence
- Return type: static void
- Signature: mmc_spi_initsequence(struct mmc_spi_host * host)
- Line: 978

### mmc_spi_probe
- Return type: static int
- Signature: mmc_spi_probe(struct spi_device * spi)
- Line: 1144

### mmc_spi_readblock
- Return type: static int
- Signature: mmc_spi_readblock(struct mmc_spi_host * host,struct spi_transfer * t,unsigned long timeout)
- Line: 684

### mmc_spi_readbytes
- Return type: static int
- Signature: mmc_spi_readbytes(struct mmc_spi_host * host,unsigned int len)
- Line: 144

### mmc_spi_readtoken
- Return type: static int
- Signature: mmc_spi_readtoken(struct mmc_spi_host * host,unsigned long timeout)
- Line: 187

### mmc_spi_remove
- Return type: static void
- Signature: mmc_spi_remove(struct spi_device * spi)
- Line: 1314

### mmc_spi_request
- Return type: static void
- Signature: mmc_spi_request(struct mmc_host * mmc,struct mmc_request * mrq)
- Line: 897

### mmc_spi_response_get
- Return type: static int
- Signature: mmc_spi_response_get(struct mmc_spi_host * host,struct mmc_command * cmd,int cs_on)
- Line: 214

### mmc_spi_set_ios
- Return type: static void
- Signature: mmc_spi_set_ios(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 1033

### mmc_spi_setup_data_message
- Return type: static void
- Signature: mmc_spi_setup_data_message(struct mmc_spi_host * host,bool multiple,bool write)
- Line: 509

### mmc_spi_skip
- Return type: static int
- Signature: mmc_spi_skip(struct mmc_spi_host * host,unsigned long timeout,unsigned n,u8 byte)
- Line: 156

### mmc_spi_wait_unbusy
- Return type: static int
- Signature: mmc_spi_wait_unbusy(struct mmc_spi_host * host,unsigned long timeout)
- Line: 182

### mmc_spi_writeblock
- Return type: static int
- Signature: mmc_spi_writeblock(struct mmc_spi_host * host,struct spi_transfer * t,unsigned long timeout)
- Line: 590

## Structs (2)

### mmc_spi_host
- Line: 104
- Members:
  - status: u8[29]
  - data_token: u8
  - crc_val: __be16
  - mmc: mmc_host *
  - spi: spi_device *
  - power_mode: unsigned char
  - powerup_msecs: u16
  - pdata: mmc_spi_platform_data *
  - crc: spi_transfer
  - early_status: spi_transfer
  - t: spi_transfer
  - token: spi_transfer
  - m: spi_message
  - status: spi_transfer
  - readback: spi_message
  - data: scratch *
  - ones: void *

### scratch
- Line: 98
- Members:
  - status: u8[29]
  - data_token: u8
  - crc_val: __be16
  - mmc: mmc_host *
  - spi: spi_device *
  - power_mode: unsigned char
  - powerup_msecs: u16
  - pdata: mmc_spi_platform_data *
  - crc: spi_transfer
  - early_status: spi_transfer
  - t: spi_transfer
  - token: spi_transfer
  - m: spi_message
  - status: spi_transfer
  - readback: spi_message
  - data: scratch *
  - ones: void *

## Variables (4)

- static **mmc_spi_dev_ids** : const struct spi_device_id[] (line 1332)
- static **mmc_spi_driver** : spi_driver (line 1344)
- static **mmc_spi_of_match_table** : const struct of_device_id[] (line 1338)
- static **mmc_spi_ops** : const struct mmc_host_ops (line 1120)

## Macros (11)

- **MMC_SPI_BLOCKSATONCE** (line 89)
- **MMC_SPI_BLOCKSIZE** (line 77)
- **MMC_SPI_INIT_TIMEOUT_MS** (line 80)
- **MMC_SPI_R1B_TIMEOUT_MS** (line 79)
- **SPI_MMC_RESPONSE_CODE**(x) (line 65)
- **SPI_RESPONSE_ACCEPTED** (line 66)
- **SPI_RESPONSE_CRC_ERR** (line 67)
- **SPI_RESPONSE_WRITE_ERR** (line 68)
- **SPI_TOKEN_MULTI_WRITE** (line 74)
- **SPI_TOKEN_SINGLE** (line 73)
- **SPI_TOKEN_STOP_TRAN** (line 75)
