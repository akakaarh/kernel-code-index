# drivers/gpio/gpio-syscon.c

Subsystem: drivers/gpio

## Functions (7)

### keystone_gpio_set
- Return type: static int
- Signature: keystone_gpio_set(struct gpio_chip * chip,unsigned int offset,int val)
- Line: 159
- Calls: gpiochip_get_data

### rockchip_gpio_set
- Return type: static int
- Signature: rockchip_gpio_set(struct gpio_chip * chip,unsigned int offset,int val)
- Line: 128
- Calls: gpiochip_get_data, rockchip_gpio_writel_bit
- Called by: rockchip_gpio_direction_output

### syscon_gpio_dir_in
- Return type: static int
- Signature: syscon_gpio_dir_in(struct gpio_chip * chip,unsigned offset)
- Line: 84
- Calls: gpiochip_get_data

### syscon_gpio_dir_out
- Return type: static int
- Signature: syscon_gpio_dir_out(struct gpio_chip * chip,unsigned offset,int val)
- Line: 102
- Calls: gpiochip_get_data

### syscon_gpio_get
- Return type: static int
- Signature: syscon_gpio_get(struct gpio_chip * chip,unsigned offset)
- Line: 55
- Calls: gpiochip_get_data

### syscon_gpio_probe
- Return type: static int
- Signature: syscon_gpio_probe(struct platform_device * pdev)
- Line: 207

### syscon_gpio_set
- Return type: static int
- Signature: syscon_gpio_set(struct gpio_chip * chip,unsigned int offset,int val)
- Line: 71
- Calls: gpiochip_get_data

## Structs (2)

### syscon_gpio_data
- Line: 38
- Members:
  - flags: unsigned int
  - bit_count: unsigned int
  - dat_bit_offset: unsigned int
  - dir_bit_offset: unsigned int
  - set: int (*)(struct gpio_chip * chip,unsigned int offset,int value)
  - chip: gpio_chip
  - syscon: regmap *
  - data: const struct syscon_gpio_data *
  - dreg_offset: u32
  - dir_reg_offset: u32

### syscon_gpio_priv
- Line: 47
- Members:
  - flags: unsigned int
  - bit_count: unsigned int
  - dat_bit_offset: unsigned int
  - dir_bit_offset: unsigned int
  - set: int (*)(struct gpio_chip * chip,unsigned int offset,int value)
  - chip: gpio_chip
  - syscon: regmap *
  - data: const struct syscon_gpio_data *
  - dreg_offset: u32
  - dir_reg_offset: u32

## Variables (5)

- static **clps711x_mctrl_gpio** : const struct syscon_gpio_data (line 121)
- static **keystone_dsp_gpio** : const struct syscon_gpio_data (line 182)
- static **rockchip_rk3328_gpio_mute** : const struct syscon_gpio_data (line 149)
- static **syscon_gpio_driver** : platform_driver (line 261)
- static **syscon_gpio_ids** : const struct of_device_id[] (line 190)

## Macros (6)

- **GPIO_SYSCON_FEAT_DIR** (line 18)
- **GPIO_SYSCON_FEAT_IN** (line 16)
- **GPIO_SYSCON_FEAT_OUT** (line 17)
- **KEYSTONE_LOCK_BIT** (line 157)
- **SYSCON_REG_BITS** (line 22)
- **SYSCON_REG_SIZE** (line 21)
