# drivers/gpio/gpio-xra1403.c

Subsystem: drivers/gpio

## Functions (8)

### to_reg
- Return type: static unsigned int
- Signature: to_reg(unsigned int reg,unsigned int offset)
- Line: 46
- Called by: crystalcove_gpio_dbg_show, crystalcove_gpio_dir_in, crystalcove_gpio_dir_out, crystalcove_gpio_get, crystalcove_gpio_set, crystalcove_update_irq_ctrl, wcove_gpio_dbg_show, wcove_gpio_dir_in, wcove_gpio_dir_out, wcove_gpio_get, wcove_gpio_get_direction, wcove_gpio_set, wcove_gpio_set_config, wcove_update_irq_ctrl, xra1403_direction_input, xra1403_direction_output, xra1403_get, xra1403_get_direction, xra1403_set

### xra1403_dbg_show
- Return type: static void
- Signature: xra1403_dbg_show(struct seq_file * s,struct gpio_chip * chip)
- Line: 115
- Calls: gpiochip_get_data

### xra1403_direction_input
- Return type: static int
- Signature: xra1403_direction_input(struct gpio_chip * chip,unsigned int offset)
- Line: 51
- Calls: gpiochip_get_data, to_reg

### xra1403_direction_output
- Return type: static int
- Signature: xra1403_direction_output(struct gpio_chip * chip,unsigned int offset,int value)
- Line: 59
- Calls: gpiochip_get_data, to_reg

### xra1403_get
- Return type: static int
- Signature: xra1403_get(struct gpio_chip * chip,unsigned int offset)
- Line: 92
- Calls: gpiochip_get_data, to_reg

### xra1403_get_direction
- Return type: static int
- Signature: xra1403_get_direction(struct gpio_chip * chip,unsigned int offset)
- Line: 76
- Calls: gpiochip_get_data, to_reg

### xra1403_probe
- Return type: static int
- Signature: xra1403_probe(struct spi_device * spi)
- Line: 147
- Calls: devm_gpiod_get_optional

### xra1403_set
- Return type: static int
- Signature: xra1403_set(struct gpio_chip * chip,unsigned int offset,int value)
- Line: 105
- Calls: gpiochip_get_data, to_reg

## Structs (1)

### xra1403
- Line: 33
- Members:
  - chip: gpio_chip
  - regmap: regmap *

## Variables (4)

- static **xra1403_driver** : spi_driver (line 200)
- static **xra1403_ids** : const struct spi_device_id[] (line 188)
- static **xra1403_regmap_cfg** : const struct regmap_config (line 38)
- static **xra1403_spi_of_match** : const struct of_device_id[] (line 194)

## Macros (13)

- **XRA_FEIR** (line 29)
- **XRA_GCR** (line 23)
- **XRA_GSR** (line 20)
- **XRA_IER** (line 25)
- **XRA_IFR** (line 30)
- **XRA_ISR** (line 27)
- **XRA_LAST** (line 31)
- **XRA_OCR** (line 21)
- **XRA_PIR** (line 22)
- **XRA_PUR** (line 24)
- **XRA_REIR** (line 28)
- **XRA_TSCR** (line 26)
- **xra1403_dbg_show** (line 144)
