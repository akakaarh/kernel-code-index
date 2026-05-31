# drivers/gpio/gpio-74x164.c

Subsystem: drivers/gpio

## Functions (8)

### __gen_74x164_write_config
- Return type: static int
- Signature: __gen_74x164_write_config(struct gen_74x164_chip * chip)
- Line: 36
- Called by: gen_74x164_probe, gen_74x164_set_multiple, gen_74x164_set_value

### gen_74x164_activate
- Return type: static int
- Signature: gen_74x164_activate(struct device * dev,struct gen_74x164_chip * chip)
- Line: 105
- Calls: gpiod_set_value_cansleep
- Called by: gen_74x164_probe

### gen_74x164_deactivate
- Return type: static void
- Signature: gen_74x164_deactivate(void * data)
- Line: 98
- Calls: gpiod_set_value_cansleep

### gen_74x164_direction_output
- Return type: static int
- Signature: gen_74x164_direction_output(struct gpio_chip * gc,unsigned offset,int val)
- Line: 91
- Calls: gen_74x164_set_value

### gen_74x164_get_value
- Return type: static int
- Signature: gen_74x164_get_value(struct gpio_chip * gc,unsigned offset)
- Line: 42
- Calls: gpiochip_get_data

### gen_74x164_probe
- Return type: static int
- Signature: gen_74x164_probe(struct spi_device * spi)
- Line: 111
- Calls: __gen_74x164_write_config, devm_gpiod_get_optional, gen_74x164_activate

### gen_74x164_set_multiple
- Return type: static int
- Signature: gen_74x164_set_multiple(struct gpio_chip * gc,unsigned long * mask,unsigned long * bits)
- Line: 70
- Calls: __gen_74x164_write_config, gpiochip_get_data

### gen_74x164_set_value
- Return type: static int
- Signature: gen_74x164_set_value(struct gpio_chip * gc,unsigned int offset,int val)
- Line: 53
- Calls: __gen_74x164_write_config, gpiochip_get_data
- Called by: gen_74x164_direction_output

## Structs (1)

### gen_74x164_chip
- Line: 21
- Members:
  - gpio_chip: gpio_chip
  - lock: mutex
  - gpiod_oe: gpio_desc *
  - registers: u32

## Variables (3)

- static **gen_74x164_driver** : spi_driver (line 181)
- static **gen_74x164_dt_ids** : const struct of_device_id[] (line 174)
- static **gen_74x164_spi_ids** : const struct spi_device_id[] (line 167)

## Macros (1)

- **GEN_74X164_NUMBER_GPIOS** (line 19)
