# drivers/spi/spi-cs42l43.c

Subsystem: drivers/spi

## Functions (13)

### cs42l43_create_bridge_amp
- Return type: static spi_board_info *
- Signature: cs42l43_create_bridge_amp(struct cs42l43_spi * priv,const char * const name,int cs,int spkid)
- Line: 275

### cs42l43_find_xu_node
- Return type: static fwnode_handle *
- Signature: cs42l43_find_xu_node(struct fwnode_handle * fwnode)
- Line: 248

### cs42l43_get_speaker_id_gpios
- Return type: static int
- Signature: cs42l43_get_speaker_id_gpios(struct cs42l43_spi * priv,int * result)
- Line: 219

### cs42l43_prepare_message
- Return type: static int
- Signature: cs42l43_prepare_message(struct spi_controller * ctlr,struct spi_message * msg)
- Line: 169

### cs42l43_prepare_transfer_hardware
- Return type: static int
- Signature: cs42l43_prepare_transfer_hardware(struct spi_controller * ctlr)
- Line: 190

### cs42l43_release_of_node
- Return type: static void
- Signature: cs42l43_release_of_node(void * data)
- Line: 308

### cs42l43_set_cs
- Return type: static void
- Signature: cs42l43_set_cs(struct spi_device * spi,bool is_high)
- Line: 162

### cs42l43_spi_max_length
- Return type: static size_t
- Signature: cs42l43_spi_max_length(struct spi_device * spi)
- Line: 214

### cs42l43_spi_probe
- Return type: static int
- Signature: cs42l43_spi_probe(struct platform_device * pdev)
- Line: 313

### cs42l43_spi_rx
- Return type: static int
- Signature: cs42l43_spi_rx(struct regmap * regmap,u8 * buf,unsigned int len)
- Line: 92

### cs42l43_spi_tx
- Return type: static int
- Signature: cs42l43_spi_tx(struct regmap * regmap,const u8 * buf,unsigned int len)
- Line: 55

### cs42l43_transfer_one
- Return type: static int
- Signature: cs42l43_transfer_one(struct spi_controller * ctlr,struct spi_device * spi,struct spi_transfer * tfr)
- Line: 128

### cs42l43_unprepare_transfer_hardware
- Return type: static int
- Signature: cs42l43_unprepare_transfer_hardware(struct spi_controller * ctlr)
- Line: 202

## Structs (1)

### cs42l43_spi
- Line: 39
- Members:
  - dev: device *
  - regmap: regmap *
  - ctlr: spi_controller *

## Enums (1)

### cs42l43_spi_cmd
- Line: 34

## Variables (4)

- static **amp_info_template** : spi_board_info (line 49)
- static **cs42l43_clock_divs** : const unsigned int[] (line 45)
- static **cs42l43_spi_driver** : platform_driver (line 446)
- static **cs42l43_spi_id_table** : const struct platform_device_id[] (line 440)

## Macros (3)

- **CS42L43_FIFO_SIZE** (line 30)
- **CS42L43_SPI_MAX_LENGTH** (line 32)
- **CS42L43_SPI_ROOT_HZ** (line 31)
