# drivers/i2c/muxes/i2c-mux-ltc4306.c

Subsystem: drivers/i2c

## Functions (12)

### ltc4306_deselect_mux
- Return type: static int
- Signature: ltc4306_deselect_mux(struct i2c_mux_core * muxc,u32 chan)
- Line: 185

### ltc4306_gpio_direction_input
- Return type: static int
- Signature: ltc4306_gpio_direction_input(struct gpio_chip * chip,unsigned int offset)
- Line: 111

### ltc4306_gpio_direction_output
- Return type: static int
- Signature: ltc4306_gpio_direction_output(struct gpio_chip * chip,unsigned int offset,int value)
- Line: 120

### ltc4306_gpio_get
- Return type: static int
- Signature: ltc4306_gpio_get(struct gpio_chip * chip,unsigned int offset)
- Line: 75

### ltc4306_gpio_get_direction
- Return type: static int
- Signature: ltc4306_gpio_get_direction(struct gpio_chip * chip,unsigned int offset)
- Line: 97

### ltc4306_gpio_init
- Return type: static int
- Signature: ltc4306_gpio_init(struct ltc4306 * data)
- Line: 151

### ltc4306_gpio_set
- Return type: static int
- Signature: ltc4306_gpio_set(struct gpio_chip * chip,unsigned int offset,int value)
- Line: 88

### ltc4306_gpio_set_config
- Return type: static int
- Signature: ltc4306_gpio_set_config(struct gpio_chip * chip,unsigned int offset,unsigned long config)
- Line: 130

### ltc4306_is_volatile_reg
- Return type: static bool
- Signature: ltc4306_is_volatile_reg(struct device * dev,unsigned int reg)
- Line: 62

### ltc4306_probe
- Return type: static int
- Signature: ltc4306_probe(struct i2c_client * client)
- Line: 207

### ltc4306_remove
- Return type: static void
- Signature: ltc4306_remove(struct i2c_client * client)
- Line: 296

### ltc4306_select_mux
- Return type: static int
- Signature: ltc4306_select_mux(struct i2c_mux_core * muxc,u32 chan)
- Line: 177

## Structs (2)

### chip_desc
- Line: 41
- Members:
  - nchans: u8
  - num_gpios: u8
  - regmap: regmap *
  - gpiochip: gpio_chip
  - chip: const struct chip_desc *
  - nchans: u8
  - enable: u8
  - has_irq: u8
  - muxtype: chip_desc::muxtype
  - id: i2c_device_identity
  - chip: const struct chip_desc *
  - last_chan: u8
  - idle_state: s32
  - client: i2c_client *
  - irq: irq_domain *
  - irq_mask: unsigned int
  - lock: raw_spinlock_t
  - supply: regulator *
  - reset_gpio: gpio_desc *
  - reset_cont: reset_control *

### ltc4306
- Line: 46
- Members:
  - nchans: u8
  - num_gpios: u8
  - regmap: regmap *
  - gpiochip: gpio_chip
  - chip: const struct chip_desc *

## Enums (1)

### ltc_type
- Line: 36

## Variables (5)

- static **chips** : const struct chip_desc[] (line 52)
- static **ltc4306_driver** : i2c_driver (line 303)
- static **ltc4306_id** : const struct i2c_device_id[] (line 193)
- static **ltc4306_of_match** : const struct of_device_id[] (line 200)
- static **ltc4306_regmap_config** : const struct regmap_config (line 67)

## Macros (10)

- **LTC4305_MAX_NCHANS** (line 22)
- **LTC4306_MAX_NCHANS** (line 23)
- **LTC_DOWNSTREAM_ACCL_EN** (line 30)
- **LTC_GPIO_ALL_INPUT** (line 33)
- **LTC_REG_CONFIG** (line 26)
- **LTC_REG_MODE** (line 27)
- **LTC_REG_STATUS** (line 25)
- **LTC_REG_SWITCH** (line 28)
- **LTC_SWITCH_MASK** (line 34)
- **LTC_UPSTREAM_ACCL_EN** (line 31)
