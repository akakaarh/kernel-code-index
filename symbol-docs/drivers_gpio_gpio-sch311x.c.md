# drivers/gpio/gpio-sch311x.c

Subsystem: drivers/gpio

## Functions (18)

### __sch311x_gpio_set
- Return type: static void
- Signature: __sch311x_gpio_set(struct sch311x_gpio_block * block,unsigned offset,int value)
- Line: 170
- Called by: sch311x_gpio_direction_out, sch311x_gpio_set

### sch311x_detect
- Return type: static int __init
- Signature: sch311x_detect(int sio_config_port,unsigned short * addr)
- Line: 331
- Calls: sch311x_sio_enter, sch311x_sio_exit, sch311x_sio_inb, sch311x_sio_outb
- Called by: sch311x_gpio_init

### sch311x_gpio_direction_in
- Return type: static int
- Signature: sch311x_gpio_direction_in(struct gpio_chip * chip,unsigned offset)
- Line: 193
- Calls: gpiochip_get_data

### sch311x_gpio_direction_out
- Return type: static int
- Signature: sch311x_gpio_direction_out(struct gpio_chip * chip,unsigned offset,int value)
- Line: 207
- Calls: __sch311x_gpio_set, gpiochip_get_data

### sch311x_gpio_exit
- Return type: static void __exit
- Signature: sch311x_gpio_exit(void)
- Line: 439

### sch311x_gpio_free
- Return type: static void
- Signature: sch311x_gpio_free(struct gpio_chip * chip,unsigned offset)
- Line: 148
- Calls: gpiochip_get_data

### sch311x_gpio_get
- Return type: static int
- Signature: sch311x_gpio_get(struct gpio_chip * chip,unsigned offset)
- Line: 158
- Calls: gpiochip_get_data

### sch311x_gpio_get_direction
- Return type: static int
- Signature: sch311x_gpio_get_direction(struct gpio_chip * chip,unsigned offset)
- Line: 224
- Calls: gpiochip_get_data

### sch311x_gpio_init
- Return type: static int __init
- Signature: sch311x_gpio_init(void)
- Line: 412
- Calls: sch311x_detect, sch311x_gpio_pdev_add

### sch311x_gpio_pdev_add
- Return type: static int __init
- Signature: sch311x_gpio_pdev_add(const unsigned short addr)
- Line: 382
- Called by: sch311x_gpio_init

### sch311x_gpio_probe
- Return type: static int
- Signature: sch311x_gpio_probe(struct platform_device * pdev)
- Line: 267

### sch311x_gpio_request
- Return type: static int
- Signature: sch311x_gpio_request(struct gpio_chip * chip,unsigned offset)
- Line: 132
- Calls: gpiochip_get_data

### sch311x_gpio_set
- Return type: static int
- Signature: sch311x_gpio_set(struct gpio_chip * chip,unsigned int offset,int value)
- Line: 181
- Calls: __sch311x_gpio_set, gpiochip_get_data

### sch311x_gpio_set_config
- Return type: static int
- Signature: sch311x_gpio_set_config(struct gpio_chip * chip,unsigned offset,unsigned long config)
- Line: 239
- Calls: gpiochip_get_data

### sch311x_sio_enter
- Return type: static int
- Signature: sch311x_sio_enter(int sio_config_port)
- Line: 96
- Called by: sch311x_detect

### sch311x_sio_exit
- Return type: static void
- Signature: sch311x_sio_exit(int sio_config_port)
- Line: 109
- Called by: sch311x_detect

### sch311x_sio_inb
- Return type: static int
- Signature: sch311x_sio_inb(int sio_config_port,int reg)
- Line: 115
- Called by: sch311x_detect

### sch311x_sio_outb
- Return type: static void
- Signature: sch311x_sio_outb(int sio_config_port,int reg,int val)
- Line: 121
- Called by: sch311x_detect

## Structs (4)

### sch311x_gpio_block
- Line: 39
- Members:
  - runtime_reg: unsigned short
  - chip: gpio_chip
  - data_reg: unsigned short
  - config_regs: unsigned short *
  - runtime_reg: unsigned short
  - lock: spinlock_t
  - blocks: sch311x_gpio_block[6]
  - data_reg: unsigned short
  - config_regs: unsigned short[8]
  - base: unsigned short

### sch311x_gpio_block_def
- Line: 51
- Members:
  - runtime_reg: unsigned short
  - chip: gpio_chip
  - data_reg: unsigned short
  - config_regs: unsigned short *
  - runtime_reg: unsigned short
  - lock: spinlock_t
  - blocks: sch311x_gpio_block[6]
  - data_reg: unsigned short
  - config_regs: unsigned short[8]
  - base: unsigned short

### sch311x_gpio_priv
- Line: 47
- Members:
  - runtime_reg: unsigned short
  - chip: gpio_chip
  - data_reg: unsigned short
  - config_regs: unsigned short *
  - runtime_reg: unsigned short
  - lock: spinlock_t
  - blocks: sch311x_gpio_block[6]
  - data_reg: unsigned short
  - config_regs: unsigned short[8]
  - base: unsigned short

### sch311x_pdev_data
- Line: 35
- Members:
  - runtime_reg: unsigned short
  - chip: gpio_chip
  - data_reg: unsigned short
  - config_regs: unsigned short *
  - runtime_reg: unsigned short
  - lock: spinlock_t
  - blocks: sch311x_gpio_block[6]
  - data_reg: unsigned short
  - config_regs: unsigned short[8]
  - base: unsigned short

## Variables (4)

- static **sch311x_gpio_blocks** : sch311x_gpio_block_def[] (line 59)
- static **sch311x_gpio_driver** : platform_driver (line 321)
- static **sch311x_gpio_pdev** : platform_device * (line 33)
- static **sch311x_ioports** : int[] (line 31)

## Macros (7)

- **DRV_NAME** (line 20)
- **GP1** (line 29)
- **SCH311X_GPIO_CONF_DIR** (line 22)
- **SCH311X_GPIO_CONF_INVERT** (line 23)
- **SCH311X_GPIO_CONF_OPEN_DRAIN** (line 24)
- **SIO_CONFIG_KEY_ENTER** (line 26)
- **SIO_CONFIG_KEY_EXIT** (line 27)
