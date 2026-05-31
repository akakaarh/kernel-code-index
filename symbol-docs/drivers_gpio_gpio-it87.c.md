# drivers/gpio/gpio-it87.c

Subsystem: drivers/gpio

## Functions (15)

### it87_gpio_direction_in
- Return type: static int
- Signature: it87_gpio_direction_in(struct gpio_chip * chip,unsigned gpio_num)
- Line: 192
- Calls: gpiochip_get_data, superio_clear_mask, superio_enter, superio_exit

### it87_gpio_direction_out
- Return type: static int
- Signature: it87_gpio_direction_out(struct gpio_chip * chip,unsigned gpio_num,int val)
- Line: 235
- Calls: gpiochip_get_data, it87_gpio_set, superio_enter, superio_exit, superio_set_mask

### it87_gpio_exit
- Return type: static void __exit
- Signature: it87_gpio_exit(void)
- Line: 395
- Calls: gpiochip_remove

### it87_gpio_get
- Return type: static int
- Signature: it87_gpio_get(struct gpio_chip * chip,unsigned gpio_num)
- Line: 180
- Calls: gpiochip_get_data

### it87_gpio_init
- Return type: static int __init
- Signature: it87_gpio_init(void)
- Line: 270
- Calls: superio_enter, superio_exit, superio_inb, superio_inw, superio_select

### it87_gpio_request
- Return type: static int
- Signature: it87_gpio_request(struct gpio_chip * chip,unsigned gpio_num)
- Line: 147
- Calls: gpiochip_get_data, superio_clear_mask, superio_enter, superio_exit, superio_set_mask

### it87_gpio_set
- Return type: static int
- Signature: it87_gpio_set(struct gpio_chip * chip,unsigned int gpio_num,int val)
- Line: 217
- Calls: gpiochip_get_data
- Called by: it87_gpio_direction_out

### superio_clear_mask
- Return type: static void
- Signature: superio_clear_mask(int mask,int reg)
- Line: 138
- Calls: superio_inb, superio_outb
- Called by: it87_gpio_direction_in, it87_gpio_request

### superio_enter
- Return type: static int
- Signature: superio_enter(void)
- Line: 78
- Called by: f7188x_find, f7188x_gpio_direction_in, f7188x_gpio_direction_out, f7188x_gpio_get, f7188x_gpio_get_direction, f7188x_gpio_set, f7188x_gpio_set_config, it87_gpio_direction_in, it87_gpio_direction_out, it87_gpio_init, it87_gpio_request

### superio_exit
- Return type: static void
- Signature: superio_exit(void)
- Line: 93
- Called by: f7188x_find, f7188x_gpio_direction_in, f7188x_gpio_direction_out, f7188x_gpio_get, f7188x_gpio_get_direction, f7188x_gpio_set, f7188x_gpio_set_config, it87_gpio_direction_in, it87_gpio_direction_out, it87_gpio_init, it87_gpio_request

### superio_inb
- Return type: static int
- Signature: superio_inb(int reg)
- Line: 106
- Called by: f7188x_find, f7188x_gpio_direction_in, f7188x_gpio_direction_out, f7188x_gpio_get, f7188x_gpio_get_direction, f7188x_gpio_set, f7188x_gpio_set_config, it87_gpio_init, superio_clear_mask, superio_set_mask

### superio_inw
- Return type: static int
- Signature: superio_inw(int reg)
- Line: 118
- Called by: f7188x_find, it87_gpio_init

### superio_outb
- Return type: static void
- Signature: superio_outb(int val,int reg)
- Line: 112
- Called by: f7188x_gpio_direction_in, f7188x_gpio_direction_out, f7188x_gpio_set, f7188x_gpio_set_config, superio_clear_mask, superio_set_mask

### superio_select
- Return type: static void
- Signature: superio_select(int ldn)
- Line: 100
- Called by: f7188x_gpio_direction_in, f7188x_gpio_direction_out, f7188x_gpio_get, f7188x_gpio_get_direction, f7188x_gpio_set, f7188x_gpio_set_config, it87_gpio_init

### superio_set_mask
- Return type: static void
- Signature: superio_set_mask(int mask,int reg)
- Line: 129
- Calls: superio_inb, superio_outb
- Called by: it87_gpio_direction_out, it87_gpio_request

## Structs (1)

### it87_gpio
- Line: 62
- Members:
  - chip: gpio_chip
  - lock: spinlock_t
  - io_base: u16
  - io_size: u16
  - output_base: u8
  - simple_base: u8
  - simple_size: u8

## Variables (2)

- static **it87_gpio_chip** : it87_gpio (line 72)
- static **it87_template_chip** : const struct gpio_chip (line 259)

## Macros (17)

- **CHIPID** (line 46)
- **CHIPREV** (line 47)
- **GPIO** (line 42)
- **IT8613_ID** (line 27)
- **IT8620_ID** (line 28)
- **IT8628_ID** (line 29)
- **IT8718_ID** (line 30)
- **IT8728_ID** (line 31)
- **IT8732_ID** (line 32)
- **IT8761_ID** (line 33)
- **IT8772_ID** (line 34)
- **IT8786_ID** (line 35)
- **LDNREG** (line 45)
- **NO_DEV_ID** (line 26)
- **REG** (line 38)
- **VAL** (line 39)
- **pr_fmt**(fmt) (line 13)
