# drivers/spi/spi-xcomm.c

Subsystem: drivers/spi

## Functions (9)

### spi_xcomm_chipselect
- Return type: static void
- Signature: spi_xcomm_chipselect(struct spi_xcomm * spi_xcomm,struct spi_device * spi,int is_active)
- Line: 98

### spi_xcomm_gpio_add
- Return type: static int
- Signature: spi_xcomm_gpio_add(struct spi_xcomm * spi_xcomm)
- Line: 65

### spi_xcomm_gpio_get_direction
- Return type: static int
- Signature: spi_xcomm_gpio_get_direction(struct gpio_chip * chip,unsigned int offset)
- Line: 59

### spi_xcomm_gpio_set_value
- Return type: static int
- Signature: spi_xcomm_gpio_set_value(struct gpio_chip * chip,unsigned int offset,int val)
- Line: 47

### spi_xcomm_probe
- Return type: static int
- Signature: spi_xcomm_probe(struct i2c_client * i2c)
- Line: 245

### spi_xcomm_setup_transfer
- Return type: static int
- Signature: spi_xcomm_setup_transfer(struct spi_xcomm * spi_xcomm,struct spi_device * spi,struct spi_transfer * t,unsigned int * settings)
- Line: 112

### spi_xcomm_sync_config
- Return type: static int
- Signature: spi_xcomm_sync_config(struct spi_xcomm * spi_xcomm,unsigned int len)
- Line: 83

### spi_xcomm_transfer_one
- Return type: static int
- Signature: spi_xcomm_transfer_one(struct spi_controller * host,struct spi_message * msg)
- Line: 176

### spi_xcomm_txrx_bufs
- Return type: static int
- Signature: spi_xcomm_txrx_bufs(struct spi_xcomm * spi_xcomm,struct spi_device * spi,struct spi_transfer * t)
- Line: 151

## Structs (1)

### spi_xcomm
- Line: 34
- Members:
  - i2c: i2c_client *
  - gc: gpio_chip
  - settings: u16
  - chipselect: u16
  - current_speed: unsigned int
  - buf: u8[63]

## Variables (2)

- static **spi_xcomm_driver** : i2c_driver (line 277)
- static **spi_xcomm_ids** : const struct i2c_device_id[] (line 271)

## Macros (14)

- **SPI_XCOMM_CLOCK** (line 32)
- **SPI_XCOMM_CMD_GPIO_SET** (line 30)
- **SPI_XCOMM_CMD_UPDATE_CONFIG** (line 28)
- **SPI_XCOMM_CMD_WRITE** (line 29)
- **SPI_XCOMM_SETTINGS_3WIRE** (line 18)
- **SPI_XCOMM_SETTINGS_CLOCK_DIV_16** (line 25)
- **SPI_XCOMM_SETTINGS_CLOCK_DIV_4** (line 26)
- **SPI_XCOMM_SETTINGS_CLOCK_DIV_64** (line 24)
- **SPI_XCOMM_SETTINGS_CLOCK_DIV_MASK** (line 23)
- **SPI_XCOMM_SETTINGS_CPHA** (line 21)
- **SPI_XCOMM_SETTINGS_CPOL** (line 22)
- **SPI_XCOMM_SETTINGS_CS_HIGH** (line 19)
- **SPI_XCOMM_SETTINGS_LEN_OFFSET** (line 17)
- **SPI_XCOMM_SETTINGS_SAMPLE_END** (line 20)
