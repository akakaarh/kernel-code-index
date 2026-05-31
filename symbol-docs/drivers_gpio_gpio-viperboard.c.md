# drivers/gpio/gpio-viperboard.c

Subsystem: drivers/gpio

## Functions (12)

### vprbrd_gpio_exit
- Return type: static void __exit
- Signature: vprbrd_gpio_exit(void)
- Line: 470

### vprbrd_gpio_init
- Return type: static int __init
- Signature: vprbrd_gpio_init(void)
- Line: 440

### vprbrd_gpio_probe
- Return type: static int
- Signature: vprbrd_gpio_probe(struct platform_device * pdev)
- Line: 393

### vprbrd_gpioa_direction_input
- Return type: static int
- Signature: vprbrd_gpioa_direction_input(struct gpio_chip * chip,unsigned int offset)
- Line: 177
- Calls: gpiochip_get_data

### vprbrd_gpioa_direction_output
- Return type: static int
- Signature: vprbrd_gpioa_direction_output(struct gpio_chip * chip,unsigned int offset,int value)
- Line: 214
- Calls: gpiochip_get_data

### vprbrd_gpioa_get
- Return type: static int
- Signature: vprbrd_gpioa_get(struct gpio_chip * chip,unsigned int offset)
- Line: 81
- Calls: gpiochip_get_data

### vprbrd_gpioa_set
- Return type: static int
- Signature: vprbrd_gpioa_set(struct gpio_chip * chip,unsigned int offset,int value)
- Line: 131
- Calls: gpiochip_get_data

### vprbrd_gpiob_direction_input
- Return type: static int
- Signature: vprbrd_gpiob_direction_input(struct gpio_chip * chip,unsigned int offset)
- Line: 350
- Calls: gpiochip_get_data, vprbrd_gpiob_setdir

### vprbrd_gpiob_direction_output
- Return type: static int
- Signature: vprbrd_gpiob_direction_output(struct gpio_chip * chip,unsigned int offset,int value)
- Line: 371
- Calls: gpiochip_get_data, vprbrd_gpiob_set, vprbrd_gpiob_setdir

### vprbrd_gpiob_get
- Return type: static int
- Signature: vprbrd_gpiob_get(struct gpio_chip * chip,unsigned int offset)
- Line: 280
- Calls: gpiochip_get_data

### vprbrd_gpiob_set
- Return type: static int
- Signature: vprbrd_gpiob_set(struct gpio_chip * chip,unsigned int offset,int value)
- Line: 312
- Calls: gpiochip_get_data
- Called by: vprbrd_gpiob_direction_output

### vprbrd_gpiob_setdir
- Return type: static int
- Signature: vprbrd_gpiob_setdir(struct vprbrd * vb,unsigned int offset,unsigned int dir)
- Line: 259
- Called by: vprbrd_gpiob_direction_input, vprbrd_gpiob_direction_output

## Structs (3)

### vprbrd_gpio
- Line: 62
- Members:
  - cmd: u8
  - clk: u8
  - offset: u8
  - t1: u8
  - t2: u8
  - invert: u8
  - pwmlevel: u8
  - outval: u8
  - risefall: u8
  - answer: u8
  - __fill: u8
  - cmd: u8
  - val: u16
  - mask: u16
  - gpioa: gpio_chip
  - gpioa_out: u32
  - gpioa_val: u32
  - gpiob: gpio_chip
  - gpiob_out: u32
  - gpiob_val: u32
  - vb: vprbrd *

### vprbrd_gpioa_msg
- Line: 42
- Members:
  - cmd: u8
  - clk: u8
  - offset: u8
  - t1: u8
  - t2: u8
  - invert: u8
  - pwmlevel: u8
  - outval: u8
  - risefall: u8
  - answer: u8
  - __fill: u8
  - cmd: u8
  - val: u16
  - mask: u16
  - gpioa: gpio_chip
  - gpioa_out: u32
  - gpioa_val: u32
  - gpiob: gpio_chip
  - gpiob_out: u32
  - gpiob_val: u32
  - vb: vprbrd *

### vprbrd_gpiob_msg
- Line: 56
- Members:
  - cmd: u8
  - clk: u8
  - offset: u8
  - t1: u8
  - t2: u8
  - invert: u8
  - pwmlevel: u8
  - outval: u8
  - risefall: u8
  - answer: u8
  - __fill: u8
  - cmd: u8
  - val: u16
  - mask: u16
  - gpioa: gpio_chip
  - gpioa_out: u32
  - gpioa_val: u32
  - gpiob: gpio_chip
  - gpiob_out: u32
  - gpiob_val: u32
  - vb: vprbrd *

## Variables (5)

- **__packed** : vprbrd_gpioa_msg (line 54)
- **__packed** : vprbrd_gpiob_msg (line 60)
- static **gpioa_clk** : unsigned char (line 73)
- static **gpioa_freq** : unsigned int (line 74)
- static **vprbrd_gpio_driver** : platform_driver (line 435)

## Macros (16)

- **VPRBRD_GPIOA_CLK_100HZ** (line 26)
- **VPRBRD_GPIOA_CLK_100KHZ** (line 23)
- **VPRBRD_GPIOA_CLK_10HZ** (line 27)
- **VPRBRD_GPIOA_CLK_10KHZ** (line 24)
- **VPRBRD_GPIOA_CLK_1KHZ** (line 25)
- **VPRBRD_GPIOA_CLK_1MHZ** (line 22)
- **VPRBRD_GPIOA_CMD_CONT** (line 31)
- **VPRBRD_GPIOA_CMD_GETIN** (line 37)
- **VPRBRD_GPIOA_CMD_PULSE** (line 32)
- **VPRBRD_GPIOA_CMD_PWM** (line 33)
- **VPRBRD_GPIOA_CMD_SETIN** (line 35)
- **VPRBRD_GPIOA_CMD_SETINT** (line 36)
- **VPRBRD_GPIOA_CMD_SETOUT** (line 34)
- **VPRBRD_GPIOA_FREQ_DEFAULT** (line 29)
- **VPRBRD_GPIOB_CMD_SETDIR** (line 39)
- **VPRBRD_GPIOB_CMD_SETVAL** (line 40)
