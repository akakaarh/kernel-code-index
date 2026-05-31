# drivers/gpio/gpio-raspberrypi-exp.c

Subsystem: drivers/gpio

## Functions (7)

### rpi_exp_gpio_dir_in
- Return type: static int
- Signature: rpi_exp_gpio_dir_in(struct gpio_chip * gc,unsigned int off)
- Line: 74
- Calls: gpiochip_get_data, rpi_exp_gpio_get_polarity

### rpi_exp_gpio_dir_out
- Return type: static int
- Signature: rpi_exp_gpio_dir_out(struct gpio_chip * gc,unsigned int off,int val)
- Line: 103
- Calls: gpiochip_get_data, rpi_exp_gpio_get_polarity

### rpi_exp_gpio_get
- Return type: static int
- Signature: rpi_exp_gpio_get(struct gpio_chip * gc,unsigned int off)
- Line: 156
- Calls: gpiochip_get_data

### rpi_exp_gpio_get_direction
- Return type: static int
- Signature: rpi_exp_gpio_get_direction(struct gpio_chip * gc,unsigned int off)
- Line: 132
- Calls: gpiochip_get_data

### rpi_exp_gpio_get_polarity
- Return type: static int
- Signature: rpi_exp_gpio_get_polarity(struct gpio_chip * gc,unsigned int off)
- Line: 54
- Calls: gpiochip_get_data
- Called by: rpi_exp_gpio_dir_in, rpi_exp_gpio_dir_out

### rpi_exp_gpio_probe
- Return type: static int
- Signature: rpi_exp_gpio_probe(struct platform_device * pdev)
- Line: 201

### rpi_exp_gpio_set
- Return type: static int
- Signature: rpi_exp_gpio_set(struct gpio_chip * gc,unsigned int off,int val)
- Line: 178
- Calls: gpiochip_get_data

## Structs (4)

### gpio_get_config
- Line: 41
- Members:
  - gc: gpio_chip
  - fw: rpi_firmware *
  - gpio: u32
  - direction: u32
  - polarity: u32
  - term_en: u32
  - term_pull_up: u32
  - state: u32
  - gpio: u32
  - direction: u32
  - polarity: u32
  - term_en: u32
  - term_pull_up: u32
  - gpio: u32
  - state: u32

### gpio_get_set_state
- Line: 49
- Members:
  - gc: gpio_chip
  - fw: rpi_firmware *
  - gpio: u32
  - direction: u32
  - polarity: u32
  - term_en: u32
  - term_pull_up: u32
  - state: u32
  - gpio: u32
  - direction: u32
  - polarity: u32
  - term_en: u32
  - term_pull_up: u32
  - gpio: u32
  - state: u32

### gpio_set_config
- Line: 32
- Members:
  - gc: gpio_chip
  - fw: rpi_firmware *
  - gpio: u32
  - direction: u32
  - polarity: u32
  - term_en: u32
  - term_pull_up: u32
  - state: u32
  - gpio: u32
  - direction: u32
  - polarity: u32
  - term_en: u32
  - term_pull_up: u32
  - gpio: u32
  - state: u32

### rpi_exp_gpio
- Line: 25
- Members:
  - gc: gpio_chip
  - fw: rpi_firmware *
  - gpio: u32
  - direction: u32
  - polarity: u32
  - term_en: u32
  - term_pull_up: u32
  - state: u32
  - gpio: u32
  - direction: u32
  - polarity: u32
  - term_en: u32
  - term_pull_up: u32
  - gpio: u32
  - state: u32

## Variables (2)

- static **rpi_exp_gpio_driver** : platform_driver (line 247)
- static **rpi_exp_gpio_ids** : const struct of_device_id[] (line 241)

## Macros (5)

- **MODULE_NAME** (line 17)
- **NUM_GPIO** (line 18)
- **RPI_EXP_GPIO_BASE** (line 20)
- **RPI_EXP_GPIO_DIR_IN** (line 22)
- **RPI_EXP_GPIO_DIR_OUT** (line 23)
