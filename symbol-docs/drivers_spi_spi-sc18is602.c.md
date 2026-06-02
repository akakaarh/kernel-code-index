# drivers/spi/spi-sc18is602.c

Subsystem: drivers/spi

## Functions (8)

### sc18is602_check_transfer
- Return type: static int
- Signature: sc18is602_check_transfer(struct spi_device * spi,struct spi_transfer * t,int tlen)
- Line: 175

### sc18is602_max_transfer_size
- Return type: static size_t
- Signature: sc18is602_max_transfer_size(struct spi_device * spi)
- Line: 223

### sc18is602_probe
- Return type: static int
- Signature: sc18is602_probe(struct i2c_client * client)
- Line: 239

### sc18is602_setup
- Return type: static int
- Signature: sc18is602_setup(struct spi_device * spi)
- Line: 228

### sc18is602_setup_transfer
- Return type: static int
- Signature: sc18is602_setup_transfer(struct sc18is602 * hw,u32 hz,u8 mode)
- Line: 131

### sc18is602_transfer_one
- Return type: static int
- Signature: sc18is602_transfer_one(struct spi_controller * host,struct spi_message * m)
- Line: 184

### sc18is602_txrx
- Return type: static int
- Signature: sc18is602_txrx(struct sc18is602 * hw,struct spi_message * msg,struct spi_transfer * t,bool do_transfer)
- Line: 66

### sc18is602_wait_ready
- Return type: static int
- Signature: sc18is602_wait_ready(struct sc18is602 * hw,int len)
- Line: 51

## Structs (1)

### sc18is602
- Line: 34
- Members:
  - host: spi_controller *
  - dev: device *
  - ctrl: u8
  - freq: u32
  - speed: u32
  - client: i2c_client *
  - id: chips
  - buffer: u8[]
  - tlen: int
  - rindex: int
  - reset: gpio_desc *

## Enums (1)

### chips
- Line: 21

## Variables (3)

- static **sc18is602_driver** : i2c_driver (line 322)
- static **sc18is602_id** : const struct i2c_device_id[] (line 297)
- static **sc18is602_of_match** : const struct of_device_id[] (line 305)

## Macros (9)

- **SC18IS602_BUFSIZ** (line 23)
- **SC18IS602_CLOCK** (line 24)
- **SC18IS602_MODE_CLOCK_DIV_128** (line 32)
- **SC18IS602_MODE_CLOCK_DIV_16** (line 30)
- **SC18IS602_MODE_CLOCK_DIV_4** (line 29)
- **SC18IS602_MODE_CLOCK_DIV_64** (line 31)
- **SC18IS602_MODE_CPHA** (line 26)
- **SC18IS602_MODE_CPOL** (line 27)
- **SC18IS602_MODE_LSB_FIRST** (line 28)
