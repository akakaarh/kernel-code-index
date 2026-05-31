# drivers/gpio/gpio-twl4030.c

Subsystem: drivers/gpio

## Functions (22)

### gpio_twl4030_debounce
- Return type: static int
- Signature: gpio_twl4030_debounce(u32 debounce,u8 mmc_cd)
- Line: 454
- Called by: gpio_twl4030_probe

### gpio_twl4030_exit
- Return type: static void __exit
- Signature: gpio_twl4030_exit(void)
- Line: 629

### gpio_twl4030_init
- Return type: static int __init
- Signature: gpio_twl4030_init(void)
- Line: 623

### gpio_twl4030_power_off_action
- Return type: static void
- Signature: gpio_twl4030_power_off_action(void * data)
- Line: 495
- Calls: gpiochip_free_own_desc, gpiod_unexport

### gpio_twl4030_probe
- Return type: static int
- Signature: gpio_twl4030_probe(struct platform_device * pdev)
- Line: 503
- Calls: gpio_twl4030_debounce, gpio_twl4030_pulls, gpiochip_request_own_desc, gpiod_export, of_gpio_twl4030

### gpio_twl4030_pulls
- Return type: static int
- Signature: gpio_twl4030_pulls(u32 ups,u32 downs)
- Line: 429
- Called by: gpio_twl4030_probe

### gpio_twl4030_read
- Return type: static int
- Signature: gpio_twl4030_read(u8 address)
- Line: 106
- Called by: twl4030_get_gpio_datain, twl4030_get_gpio_direction, twl4030_set_gpio_direction

### gpio_twl4030_write
- Return type: static int
- Signature: gpio_twl4030_write(u8 address,u8 data)
- Line: 71
- Called by: twl4030_set_gpio_dataout, twl4030_set_gpio_direction, twl_free, twl_request

### of_gpio_twl4030
- Return type: static twl4030_gpio_platform_data *
- Signature: of_gpio_twl4030(struct device * dev)
- Line: 471
- Called by: gpio_twl4030_probe

### twl4030_get_gpio_datain
- Return type: static int
- Signature: twl4030_get_gpio_datain(int gpio)
- Line: 190
- Calls: gpio_twl4030_read
- Called by: twl_get

### twl4030_get_gpio_direction
- Return type: static int
- Signature: twl4030_get_gpio_direction(int gpio)
- Line: 159
- Calls: gpio_twl4030_read
- Called by: twl_get_direction

### twl4030_led_set_value
- Return type: static int
- Signature: twl4030_led_set_value(int led,int value)
- Line: 123
- Called by: twl_free, twl_set

### twl4030_set_gpio_dataout
- Return type: static int
- Signature: twl4030_set_gpio_dataout(int gpio,int enable)
- Line: 176
- Calls: gpio_twl4030_write
- Called by: twl_set

### twl4030_set_gpio_direction
- Return type: static int
- Signature: twl4030_set_gpio_direction(int gpio,int is_input)
- Line: 139
- Calls: gpio_twl4030_read, gpio_twl4030_write
- Called by: twl_direction_in, twl_direction_out

### twl_direction_in
- Return type: static int
- Signature: twl_direction_in(struct gpio_chip * chip,unsigned offset)
- Line: 295
- Calls: gpiochip_get_data, twl4030_set_gpio_direction

### twl_direction_out
- Return type: static int
- Signature: twl_direction_out(struct gpio_chip * chip,unsigned offset,int value)
- Line: 358
- Calls: gpiochip_get_data, twl4030_set_gpio_direction, twl_set

### twl_free
- Return type: static void
- Signature: twl_free(struct gpio_chip * chip,unsigned offset)
- Line: 275
- Calls: gpio_twl4030_write, gpiochip_get_data, twl4030_led_set_value

### twl_get
- Return type: static int
- Signature: twl_get(struct gpio_chip * chip,unsigned offset)
- Line: 314
- Calls: gpiochip_get_data, twl4030_get_gpio_datain

### twl_get_direction
- Return type: static int
- Signature: twl_get_direction(struct gpio_chip * chip,unsigned offset)
- Line: 382
- Calls: gpiochip_get_data, twl4030_get_gpio_direction

### twl_request
- Return type: static int
- Signature: twl_request(struct gpio_chip * chip,unsigned offset)
- Line: 207
- Calls: gpio_twl4030_write, gpiochip_get_data

### twl_set
- Return type: static int
- Signature: twl_set(struct gpio_chip * chip,unsigned int offset,int value)
- Line: 337
- Calls: gpiochip_get_data, twl4030_led_set_value, twl4030_set_gpio_dataout
- Called by: twl_direction_out

### twl_to_irq
- Return type: static int
- Signature: twl_to_irq(struct gpio_chip * chip,unsigned offset)
- Line: 404
- Calls: gpiochip_get_data

## Structs (1)

### gpio_twl4030_priv
- Line: 55
- Members:
  - gpio_chip: gpio_chip
  - mutex: mutex
  - irq_base: int
  - usage_count: unsigned int
  - direction: unsigned int
  - out_state: unsigned int

## Variables (4)

- static **cached_leden** : u8 (line 117)
- static **gpio_twl4030_driver** : platform_driver (line 615)
- static **template_chip** : const struct gpio_chip (line 413)
- static **twl_gpio_match** : const struct of_device_id[] (line 606)

## Macros (20)

- **GPIO_32_MASK** (line 53)
- **LEDEN_LEDAEXT** (line 92)
- **LEDEN_LEDAON** (line 90)
- **LEDEN_LEDAPWM** (line 94)
- **LEDEN_LEDBEXT** (line 93)
- **LEDEN_LEDBON** (line 91)
- **LEDEN_LEDBPWM** (line 95)
- **LEDEN_PWM_LENGTHA** (line 96)
- **LEDEN_PWM_LENGTHB** (line 97)
- **MASK_GPIO_CTRL_GPIO0CD1** (line 48)
- **MASK_GPIO_CTRL_GPIO1CD2** (line 49)
- **MASK_GPIO_CTRL_GPIO_ON** (line 50)
- **PWMxON_LENGTH** (line 99)
- **TWL4030_LED_LEDEN_REG** (line 83)
- **TWL4030_PWMAOFF_REG** (line 85)
- **TWL4030_PWMAON_REG** (line 84)
- **TWL4030_PWMBOFF_REG** (line 87)
- **TWL4030_PWMBON_REG** (line 86)
- **is_module**() (line 42)
- **is_module**() (line 44)
