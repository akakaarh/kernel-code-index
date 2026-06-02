# drivers/spi/spi-ljca.c

Subsystem: drivers/spi

## Functions (9)

### ljca_spi_deinit
- Return type: static int
- Signature: ljca_spi_deinit(struct ljca_spi_dev * ljca_spi)
- Line: 145

### ljca_spi_dev_remove
- Return type: static void
- Signature: ljca_spi_dev_remove(struct auxiliary_device * auxdev)
- Line: 250

### ljca_spi_dev_resume
- Return type: static int
- Signature: ljca_spi_dev_resume(struct device * dev)
- Line: 266

### ljca_spi_dev_suspend
- Return type: static int
- Signature: ljca_spi_dev_suspend(struct device * dev)
- Line: 259

### ljca_spi_init
- Return type: static int
- Signature: ljca_spi_init(struct ljca_spi_dev * ljca_spi,u8 div,u8 mode)
- Line: 117

### ljca_spi_probe
- Return type: static int
- Signature: ljca_spi_probe(struct auxiliary_device * auxdev,const struct auxiliary_device_id * aux_dev_id)
- Line: 218

### ljca_spi_read_write
- Return type: static int
- Signature: ljca_spi_read_write(struct ljca_spi_dev * ljca_spi,const u8 * w_data,u8 * r_data,int len,int id,int complete,int cmd)
- Line: 80

### ljca_spi_transfer
- Return type: static int
- Signature: ljca_spi_transfer(struct ljca_spi_dev * ljca_spi,const u8 * tx_data,u8 * rx_data,u16 len)
- Line: 158

### ljca_spi_transfer_one
- Return type: static int
- Signature: ljca_spi_transfer_one(struct spi_controller * controller,struct spi_device * spi,struct spi_transfer * xfer)
- Line: 193

## Structs (3)

### ljca_spi_dev
- Line: 69
- Members:
  - index: u8
  - speed: u8
  - mode: u8
  - indicator: u8
  - len: u8
  - ljca: ljca_client *
  - controller: spi_controller *
  - spi_info: ljca_spi_info *
  - speed: u8
  - mode: u8
  - obuf: u8[]
  - ibuf: u8[]

### ljca_spi_init_packet
- Line: 57
- Members:
  - index: u8
  - speed: u8
  - mode: u8
  - indicator: u8
  - len: u8
  - ljca: ljca_client *
  - controller: spi_controller *
  - spi_info: ljca_spi_info *
  - speed: u8
  - mode: u8
  - obuf: u8[]
  - ibuf: u8[]

### ljca_spi_xfer_packet
- Line: 63
- Members:
  - index: u8
  - speed: u8
  - mode: u8
  - indicator: u8
  - len: u8
  - ljca: ljca_client *
  - controller: spi_controller *
  - spi_info: ljca_spi_info *
  - speed: u8
  - mode: u8
  - obuf: u8[]
  - ibuf: u8[]

## Enums (4)

### __anonff47db5c0103
- Line: 38

### __anonff47db5c0203
- Line: 47

### __anonff47db5c0303
- Line: 52

### ljca_spi_cmd
- Line: 30

## Variables (5)

- **__packed** : ljca_spi_init_packet (line 61)
- **__packed** : ljca_spi_xfer_packet (line 67)
- static **ljca_spi_driver** : auxiliary_driver (line 283)
- static **ljca_spi_id_table** : const struct auxiliary_device_id[] (line 277)
- static **ljca_spi_pm** : const struct dev_pm_ops (line 273)

## Macros (8)

- **LJCA_SPI_BUF_SIZE** (line 18)
- **LJCA_SPI_BUS_MAX_HZ** (line 16)
- **LJCA_SPI_CLK_MODE_PHASE** (line 23)
- **LJCA_SPI_CLK_MODE_POLARITY** (line 22)
- **LJCA_SPI_MAX_XFER_SIZE** (line 19)
- **LJCA_SPI_XFER_INDICATOR_CMPL** (line 26)
- **LJCA_SPI_XFER_INDICATOR_ID** (line 25)
- **LJCA_SPI_XFER_INDICATOR_INDEX** (line 27)
