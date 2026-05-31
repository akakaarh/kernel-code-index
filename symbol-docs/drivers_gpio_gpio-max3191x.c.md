# drivers/gpio/gpio-max3191x.c

Subsystem: drivers/gpio

## Functions (13)

### devm_gpiod_get_array_optional_count
- Return type: static gpio_descs *
- Signature: devm_gpiod_get_array_optional_count(struct device * dev,const char * con_id,enum gpiod_flags flags,unsigned int expected)
- Line: 317
- Calls: devm_gpiod_get_array_optional, gpiod_count
- Called by: max3191x_probe

### max3191x_chip_is_faulting
- Return type: static bool
- Signature: max3191x_chip_is_faulting(struct max3191x_chip * max3191x,unsigned int chipnum)
- Line: 178
- Called by: max3191x_get, max3191x_get_multiple

### max3191x_direction_input
- Return type: static int
- Signature: max3191x_direction_input(struct gpio_chip * gpio,unsigned int offset)
- Line: 101

### max3191x_get
- Return type: static int
- Signature: max3191x_get(struct gpio_chip * gpio,unsigned int offset)
- Line: 194
- Calls: gpiochip_get_data, max3191x_chip_is_faulting, max3191x_readout_locked, max3191x_wordlen

### max3191x_get_direction
- Return type: static int
- Signature: max3191x_get_direction(struct gpio_chip * gpio,unsigned int offset)
- Line: 96

### max3191x_get_multiple
- Return type: static int
- Signature: max3191x_get_multiple(struct gpio_chip * gpio,unsigned long * mask,unsigned long * bits)
- Line: 219
- Calls: gpiochip_get_data, max3191x_chip_is_faulting, max3191x_readout_locked, max3191x_wordlen

### max3191x_gpiod_multi_set_single_value
- Return type: static void
- Signature: max3191x_gpiod_multi_set_single_value(struct gpio_descs * descs,int value)
- Line: 299
- Called by: max3191x_probe

### max3191x_probe
- Return type: static int
- Signature: max3191x_probe(struct spi_device * spi)
- Line: 344
- Calls: devm_gpiod_get_array_optional_count, devm_gpiod_put_array, max3191x_gpiod_multi_set_single_value, max3191x_wordlen

### max3191x_readout_locked
- Return type: static int
- Signature: max3191x_readout_locked(struct max3191x_chip * max3191x)
- Line: 111
- Calls: gpiod_get_value_cansleep
- Called by: max3191x_get, max3191x_get_multiple

### max3191x_register_driver
- Return type: static int __init
- Signature: max3191x_register_driver(struct spi_driver * sdrv)
- Line: 434

### max3191x_remove
- Return type: static void
- Signature: max3191x_remove(struct spi_device * spi)
- Line: 426
- Calls: gpiochip_remove

### max3191x_set_config
- Return type: static int
- Signature: max3191x_set_config(struct gpio_chip * gpio,unsigned int offset,unsigned long config)
- Line: 253
- Calls: gpiochip_get_data, gpiod_set_value_cansleep

### max3191x_wordlen
- Return type: static unsigned int
- Signature: max3191x_wordlen(struct max3191x_chip * max3191x)
- Line: 106
- Called by: max3191x_get, max3191x_get_multiple, max3191x_probe

## Structs (1)

### max3191x_chip
- Line: 72
- Members:
  - gpio: gpio_chip
  - lock: mutex
  - nchips: u32
  - mode: max3191x_mode
  - modesel_pins: gpio_descs *
  - fault_pins: gpio_descs *
  - db0_pins: gpio_descs *
  - db1_pins: gpio_descs *
  - mesg: spi_message
  - xfer: spi_transfer
  - crc_error: unsigned long *
  - overtemp: unsigned long *
  - undervolt1: unsigned long *
  - undervolt2: unsigned long *
  - fault: unsigned long *
  - ignore_uv: bool

## Enums (1)

### max3191x_mode
- Line: 41

## Variables (3)

- static **max3191x_driver** : spi_driver (line 462)
- static **max3191x_of_id** : const struct of_device_id[] (line 440)
- static **max3191x_spi_id** : const struct spi_device_id[] (line 451)

## Macros (2)

- **MAX3191X_CRC8_POLYNOMIAL** (line 92)
- **MAX3191X_NGPIO** (line 91)
