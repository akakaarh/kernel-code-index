# drivers/spi/spi-ch341.c

Subsystem: drivers/spi

## Functions (7)

### ch341_config_stream
- Return type: static int
- Signature: ch341_config_stream(struct ch341_spi_dev * ch341)
- Line: 114

### ch341_disconnect
- Return type: static void
- Signature: ch341_disconnect(struct usb_interface * intf)
- Line: 227

### ch341_enable_pins
- Return type: static int
- Signature: ch341_enable_pins(struct ch341_spi_dev * ch341,bool enable)
- Line: 125

### ch341_probe
- Return type: static int
- Signature: ch341_probe(struct usb_interface * intf,const struct usb_device_id * id)
- Line: 141

### ch341_recv
- Return type: static void
- Signature: ch341_recv(struct urb * urb)
- Line: 92

### ch341_set_cs
- Return type: static void
- Signature: ch341_set_cs(struct spi_device * spi,bool is_high)
- Line: 42

### ch341_transfer_one
- Return type: static int
- Signature: ch341_transfer_one(struct spi_controller * host,struct spi_device * spi,struct spi_transfer * trans)
- Line: 66

## Structs (1)

### ch341_spi_dev
- Line: 30
- Members:
  - ctrl: spi_controller *
  - udev: usb_device *
  - write_pipe: unsigned int
  - read_pipe: unsigned int
  - rx_len: int
  - rx_buf: void *
  - tx_buf: u8 *
  - rx_urb: urb *
  - spidev: spi_device *

## Variables (3)

- static **ch341_id_table** : const struct usb_device_id[] (line 238)
- static **ch341a_usb_driver** : usb_driver (line 244)
- static **chip** : spi_board_info (line 137)

## Macros (11)

- **CH341A_CMD_I2C_STM_END** (line 24)
- **CH341A_CMD_I2C_STM_SET** (line 23)
- **CH341A_CMD_I2C_STREAM** (line 22)
- **CH341A_CMD_SPI_STREAM** (line 26)
- **CH341A_CMD_UIO_STM_DIR** (line 19)
- **CH341A_CMD_UIO_STM_END** (line 18)
- **CH341A_CMD_UIO_STM_OUT** (line 20)
- **CH341A_CMD_UIO_STREAM** (line 16)
- **CH341A_STM_I2C_100K** (line 28)
- **CH341_DEFAULT_TIMEOUT** (line 14)
- **CH341_PACKET_LENGTH** (line 13)
