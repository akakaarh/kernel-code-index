# drivers/spi/spi-gpio.c

Subsystem: drivers/spi

## Functions (20)

### getmiso
- Return type: static int
- Signature: getmiso(const struct spi_device * spi)
- Line: 72

### setmosi
- Return type: static void
- Signature: setmosi(const struct spi_device * spi,int is_on)
- Line: 65

### setsck
- Return type: static void
- Signature: setsck(const struct spi_device * spi,int is_on)
- Line: 58

### spi_gpio_chipselect
- Return type: static void
- Signature: spi_gpio_chipselect(struct spi_device * spi,int is_active)
- Line: 194

### spi_gpio_cleanup
- Return type: static void
- Signature: spi_gpio_cleanup(struct spi_device * spi)
- Line: 279

### spi_gpio_probe
- Return type: static int
- Signature: spi_gpio_probe(struct platform_device * pdev)
- Line: 340

### spi_gpio_probe_pdata
- Return type: static int
- Signature: spi_gpio_probe_pdata(struct platform_device * pdev,struct spi_controller * host)
- Line: 308

### spi_gpio_request
- Return type: static int
- Signature: spi_gpio_request(struct device * dev,struct spi_gpio * spi_gpio)
- Line: 294

### spi_gpio_set_direction
- Return type: static int
- Signature: spi_gpio_set_direction(struct spi_device * spi,bool output)
- Line: 241

### spi_gpio_set_mosi_idle
- Return type: static void
- Signature: spi_gpio_set_mosi_idle(struct spi_device * spi)
- Line: 211

### spi_gpio_setup
- Return type: static int
- Signature: spi_gpio_setup(struct spi_device * spi)
- Line: 219

### spi_gpio_spec_txrx_word_mode0
- Return type: static u32
- Signature: spi_gpio_spec_txrx_word_mode0(struct spi_device * spi,unsigned int nsecs,u32 word,u8 bits,unsigned int flags)
- Line: 152

### spi_gpio_spec_txrx_word_mode1
- Return type: static u32
- Signature: spi_gpio_spec_txrx_word_mode1(struct spi_device * spi,unsigned int nsecs,u32 word,u8 bits,unsigned int flags)
- Line: 162

### spi_gpio_spec_txrx_word_mode2
- Return type: static u32
- Signature: spi_gpio_spec_txrx_word_mode2(struct spi_device * spi,unsigned int nsecs,u32 word,u8 bits,unsigned int flags)
- Line: 172

### spi_gpio_spec_txrx_word_mode3
- Return type: static u32
- Signature: spi_gpio_spec_txrx_word_mode3(struct spi_device * spi,unsigned int nsecs,u32 word,u8 bits,unsigned int flags)
- Line: 182

### spi_gpio_txrx_word_mode0
- Return type: static u32
- Signature: spi_gpio_txrx_word_mode0(struct spi_device * spi,unsigned int nsecs,u32 word,u8 bits,unsigned int flags)
- Line: 106

### spi_gpio_txrx_word_mode1
- Return type: static u32
- Signature: spi_gpio_txrx_word_mode1(struct spi_device * spi,unsigned int nsecs,u32 word,u8 bits,unsigned int flags)
- Line: 115

### spi_gpio_txrx_word_mode2
- Return type: static u32
- Signature: spi_gpio_txrx_word_mode2(struct spi_device * spi,unsigned int nsecs,u32 word,u8 bits,unsigned int flags)
- Line: 124

### spi_gpio_txrx_word_mode3
- Return type: static u32
- Signature: spi_gpio_txrx_word_mode3(struct spi_device * spi,unsigned int nsecs,u32 word,u8 bits,unsigned int flags)
- Line: 133

### spi_to_spi_gpio
- Return type: static spi_gpio * __pure
- Signature: spi_to_spi_gpio(const struct spi_device * spi)
- Line: 47

## Structs (1)

### spi_gpio
- Line: 32
- Members:
  - bitbang: spi_bitbang
  - sck: gpio_desc *
  - miso: gpio_desc *
  - mosi: gpio_desc *
  - cs_gpios: gpio_desc **

## Variables (2)

- static **spi_gpio_driver** : platform_driver (line 423)
- static **spi_gpio_dt_ids** : const struct of_device_id[] (line 417)

## Macros (2)

- **DRIVER_NAME** (line 42)
- **spidelay**(nsecs) (line 88)
