# drivers/gpio/gpio-i8255.c

Subsystem: drivers/gpio

## Functions (4)

### devm_i8255_regmap_register
- Return type: int
- Signature: devm_i8255_regmap_register(struct device * const dev,const struct i8255_regmap_config * const config)
- Line: 102
- Calls: devm_gpio_regmap_register, i8255_ppi_init
- Called by: dio48e_probe, gpiomm_probe

### i8255_direction_mask
- Return type: static int
- Signature: i8255_direction_mask(const unsigned int offset)
- Line: 30
- Called by: i8255_reg_mask_xlate

### i8255_ppi_init
- Return type: static int
- Signature: i8255_ppi_init(struct regmap * const map,const unsigned int base)
- Line: 51
- Called by: devm_i8255_regmap_register

### i8255_reg_mask_xlate
- Return type: static int
- Signature: i8255_reg_mask_xlate(struct gpio_regmap * gpio,unsigned int base,unsigned int offset,unsigned int * reg,unsigned int * mask)
- Line: 70
- Calls: i8255_direction_mask

## Macros (13)

- **I8255_CONTROL** (line 26)
- **I8255_CONTROL_MODE_SET** (line 22)
- **I8255_CONTROL_PORTA_DIRECTION** (line 21)
- **I8255_CONTROL_PORTB_DIRECTION** (line 19)
- **I8255_CONTROL_PORTC_LOWER_DIRECTION** (line 18)
- **I8255_CONTROL_PORTC_UPPER_DIRECTION** (line 20)
- **I8255_NGPIO** (line 16)
- **I8255_NGPIO_PER_REG** (line 17)
- **I8255_PORTA** (line 23)
- **I8255_PORTB** (line 24)
- **I8255_PORTC** (line 25)
- **I8255_REG_DAT_BASE** (line 27)
- **I8255_REG_DIR_IN_BASE** (line 28)
