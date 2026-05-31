# drivers/gpio/gpio-f7188x.c

Subsystem: drivers/gpio

## Functions (17)

### f7188x_find
- Return type: static int __init
- Signature: f7188x_find(int addr,struct f7188x_sio * sio)
- Line: 528
- Calls: superio_enter, superio_exit, superio_inb, superio_inw
- Called by: f7188x_gpio_init

### f7188x_gpio_device_add
- Return type: static int __init
- Signature: f7188x_gpio_device_add(const struct f7188x_sio * sio)
- Line: 600
- Called by: f7188x_gpio_init

### f7188x_gpio_direction_in
- Return type: static int
- Signature: f7188x_gpio_direction_in(struct gpio_chip * chip,unsigned offset)
- Line: 314
- Calls: gpiochip_get_data, superio_enter, superio_exit, superio_inb, superio_outb, superio_select

### f7188x_gpio_direction_out
- Return type: static int
- Signature: f7188x_gpio_direction_out(struct gpio_chip * chip,unsigned offset,int value)
- Line: 363
- Calls: gpiochip_get_data, superio_enter, superio_exit, superio_inb, superio_outb, superio_select

### f7188x_gpio_exit
- Return type: static void __exit
- Signature: f7188x_gpio_exit(void)
- Line: 662

### f7188x_gpio_get
- Return type: static int
- Signature: f7188x_gpio_get(struct gpio_chip * chip,unsigned offset)
- Line: 339
- Calls: gpiochip_get_data, superio_enter, superio_exit, superio_inb, superio_select

### f7188x_gpio_get_direction
- Return type: static int
- Signature: f7188x_gpio_get_direction(struct gpio_chip * chip,unsigned offset)
- Line: 289
- Calls: gpiochip_get_data, superio_enter, superio_exit, superio_inb, superio_select

### f7188x_gpio_init
- Return type: static int __init
- Signature: f7188x_gpio_init(void)
- Line: 642
- Calls: f7188x_find, f7188x_gpio_device_add

### f7188x_gpio_probe
- Return type: static int
- Signature: f7188x_gpio_probe(struct platform_device * pdev)
- Line: 454

### f7188x_gpio_set
- Return type: static int
- Signature: f7188x_gpio_set(struct gpio_chip * chip,unsigned int offset,int value)
- Line: 395
- Calls: gpiochip_get_data, superio_enter, superio_exit, superio_inb, superio_outb, superio_select

### f7188x_gpio_set_config
- Return type: static int
- Signature: f7188x_gpio_set_config(struct gpio_chip * chip,unsigned offset,unsigned long config)
- Line: 421
- Calls: gpiochip_get_data, superio_enter, superio_exit, superio_inb, superio_outb, superio_select

### superio_enter
- Return type: static int
- Signature: superio_enter(int base)
- Line: 126
- Called by: f7188x_find, f7188x_gpio_direction_in, f7188x_gpio_direction_out, f7188x_gpio_get, f7188x_gpio_get_direction, f7188x_gpio_set, f7188x_gpio_set_config, it87_gpio_direction_in, it87_gpio_direction_out, it87_gpio_init, it87_gpio_request

### superio_exit
- Return type: static void
- Signature: superio_exit(int base)
- Line: 147
- Called by: f7188x_find, f7188x_gpio_direction_in, f7188x_gpio_direction_out, f7188x_gpio_get, f7188x_gpio_get_direction, f7188x_gpio_set, f7188x_gpio_set_config, it87_gpio_direction_in, it87_gpio_direction_out, it87_gpio_init, it87_gpio_request

### superio_inb
- Return type: static int
- Signature: superio_inb(int base,int reg)
- Line: 102
- Called by: f7188x_find, f7188x_gpio_direction_in, f7188x_gpio_direction_out, f7188x_gpio_get, f7188x_gpio_get_direction, f7188x_gpio_set, f7188x_gpio_set_config, it87_gpio_init, superio_clear_mask, superio_set_mask

### superio_inw
- Return type: static int
- Signature: superio_inw(int base,int reg)
- Line: 108
- Called by: f7188x_find, it87_gpio_init

### superio_outb
- Return type: static void
- Signature: superio_outb(int base,int reg,int val)
- Line: 120
- Called by: f7188x_gpio_direction_in, f7188x_gpio_direction_out, f7188x_gpio_set, f7188x_gpio_set_config, superio_clear_mask, superio_set_mask

### superio_select
- Return type: static void
- Signature: superio_select(int base,int ld)
- Line: 141
- Called by: f7188x_gpio_direction_in, f7188x_gpio_direction_out, f7188x_gpio_get, f7188x_gpio_get_direction, f7188x_gpio_set, f7188x_gpio_set_config, it87_gpio_init

## Structs (3)

### f7188x_gpio_bank
- Line: 86
- Members:
  - addr: int
  - device: int
  - type: chips
  - chip: gpio_chip
  - regbase: unsigned int
  - data: f7188x_gpio_data *
  - sio: f7188x_sio *
  - nr_bank: int
  - bank: f7188x_gpio_bank *

### f7188x_gpio_data
- Line: 92
- Members:
  - addr: int
  - device: int
  - type: chips
  - chip: gpio_chip
  - regbase: unsigned int
  - data: f7188x_gpio_data *
  - sio: f7188x_sio *
  - nr_bank: int
  - bank: f7188x_gpio_bank *

### f7188x_sio
- Line: 80
- Members:
  - addr: int
  - device: int
  - type: chips
  - chip: gpio_chip
  - regbase: unsigned int
  - data: f7188x_gpio_data *
  - sio: f7188x_sio *
  - nr_bank: int
  - bank: f7188x_gpio_bank *

## Enums (1)

### chips
- Line: 56

## Variables (12)

- static **f71869_gpio_bank** : f7188x_gpio_bank[] (line 194)
- static **f71869a_gpio_bank** : f7188x_gpio_bank[] (line 204)
- static **f71882_gpio_bank** : f7188x_gpio_bank[] (line 215)
- static **f71889_gpio_bank** : f7188x_gpio_bank[] (line 234)
- static **f71889a_gpio_bank** : f7188x_gpio_bank[] (line 223)
- static **f7188x_gpio_driver** : platform_driver (line 635)
- static **f7188x_gpio_pdev** : platform_device * (line 597)
- static **f7188x_names** : const char * const[] (line 68)
- static **f81804_gpio_bank** : f7188x_gpio_bank[] (line 258)
- static **f81865_gpio_bank** : f7188x_gpio_bank[] (line 268)
- static **f81866_gpio_bank** : f7188x_gpio_bank[] (line 245)
- static **nct6126d_gpio_bank** : f7188x_gpio_bank[] (line 278)

## Macros (27)

- **DRVNAME** (line 10)
- **F7188X_GPIO_BANK**(_ngpio,_regbase,_label) (line 167)
- **SIO_DEVID** (line 24)
- **SIO_F71869A_ID** (line 38)
- **SIO_F71869_ID** (line 37)
- **SIO_F71882_ID** (line 39)
- **SIO_F71889A_ID** (line 41)
- **SIO_F71889_ID** (line 40)
- **SIO_F81804_ID** (line 43)
- **SIO_F81865_ID** (line 44)
- **SIO_F81866_ID** (line 42)
- **SIO_FINTEK_DEVREV** (line 32)
- **SIO_FINTEK_ID** (line 35)
- **SIO_FINTEK_MANID** (line 33)
- **SIO_LDSEL** (line 23)
- **SIO_LD_GPIO_FINTEK** (line 46)
- **SIO_LD_GPIO_NUVOTON** (line 53)
- **SIO_LOCK_KEY** (line 27)
- **SIO_NCT6126D_ID** (line 51)
- **SIO_UNLOCK_KEY** (line 26)
- **f7188x_gpio_data_in**(base) (line 187)
- **f7188x_gpio_data_out**(base) (line 186)
- **f7188x_gpio_data_single**(type) (line 192)
- **f7188x_gpio_dir**(base) (line 185)
- **f7188x_gpio_dir_invert**(type) (line 191)
- **f7188x_gpio_out_mode**(base) (line 189)
- **pr_fmt**(fmt) (line 11)
