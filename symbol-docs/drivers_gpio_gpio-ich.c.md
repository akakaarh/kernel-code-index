# drivers/gpio/gpio-ich.c

Subsystem: drivers/gpio

## Functions (14)

### ich6_gpio_get
- Return type: static int
- Signature: ich6_gpio_get(struct gpio_chip * chip,unsigned int nr)
- Line: 201
- Calls: ichx_gpio_get

### ich6_gpio_request
- Return type: static int
- Signature: ich6_gpio_request(struct gpio_chip * chip,unsigned int nr)
- Line: 245
- Calls: ichx_gpio_request

### ichx_gpio_check_available
- Return type: static bool
- Signature: ichx_gpio_check_available(struct gpio_chip * gpio,unsigned int nr)
- Line: 153
- Called by: ichx_gpio_request

### ichx_gpio_direction_input
- Return type: static int
- Signature: ichx_gpio_direction_input(struct gpio_chip * gpio,unsigned int nr)
- Line: 166
- Calls: ichx_write_bit

### ichx_gpio_direction_output
- Return type: static int
- Signature: ichx_gpio_direction_output(struct gpio_chip * gpio,unsigned int nr,int val)
- Line: 175
- Calls: ichx_write_bit

### ichx_gpio_get
- Return type: static int
- Signature: ichx_gpio_get(struct gpio_chip * chip,unsigned int nr)
- Line: 196
- Calls: ichx_read_bit
- Called by: ich6_gpio_get

### ichx_gpio_get_direction
- Return type: static int
- Signature: ichx_gpio_get_direction(struct gpio_chip * gpio,unsigned int nr)
- Line: 158
- Calls: ichx_read_bit

### ichx_gpio_probe
- Return type: static int
- Signature: ichx_gpio_probe(struct platform_device * pdev)
- Line: 389
- Calls: ichx_gpio_request_regions, ichx_gpiolib_setup

### ichx_gpio_request
- Return type: static int
- Signature: ichx_gpio_request(struct gpio_chip * chip,unsigned int nr)
- Line: 228
- Calls: ichx_gpio_check_available, ichx_read_bit
- Called by: ich6_gpio_request

### ichx_gpio_request_regions
- Return type: static int
- Signature: ichx_gpio_request_regions(struct device * dev,struct resource * res_base,const char * name,u8 use_gpio)
- Line: 370
- Called by: ichx_gpio_probe

### ichx_gpio_set
- Return type: static int
- Signature: ichx_gpio_set(struct gpio_chip * chip,unsigned int nr,int val)
- Line: 259
- Calls: ichx_write_bit

### ichx_gpiolib_setup
- Return type: static void
- Signature: ichx_gpiolib_setup(struct gpio_chip * chip)
- Line: 264
- Called by: ichx_gpio_probe

### ichx_read_bit
- Return type: static int
- Signature: ichx_read_bit(int reg,unsigned int nr)
- Line: 133
- Called by: ichx_gpio_get, ichx_gpio_get_direction, ichx_gpio_request

### ichx_write_bit
- Return type: static int
- Signature: ichx_write_bit(int reg,unsigned int nr,int val,int verify)
- Line: 101
- Called by: ichx_gpio_direction_input, ichx_gpio_direction_output, ichx_gpio_set

## Structs (2)

### __anond4a9da5c0108
- Line: 85
- Members:
  - ngpio: uint
  - regs: const u8 (*)[3]
  - reglen: const u8 *
  - have_blink: bool
  - uses_gpe0: bool
  - use_sel_ignore: u32[3]
  - request: int (*)(struct gpio_chip * chip,unsigned int offset)
  - get: int (*)(struct gpio_chip * chip,unsigned int offset)
  - use_outlvl_cache: bool
  - lock: spinlock_t
  - dev: device *
  - chip: gpio_chip
  - gpio_base: resource *
  - pm_base: resource *
  - desc: ichx_desc *
  - orig_gpio_ctrl: u32
  - use_gpio: u8
  - outlvl_cache: int[3]

### ichx_desc
- Line: 57
- Members:
  - ngpio: uint
  - regs: const u8 (*)[3]
  - reglen: const u8 *
  - have_blink: bool
  - uses_gpe0: bool
  - use_sel_ignore: u32[3]
  - request: int (*)(struct gpio_chip * chip,unsigned int offset)
  - get: int (*)(struct gpio_chip * chip,unsigned int offset)
  - use_outlvl_cache: bool
  - lock: spinlock_t
  - dev: device *
  - chip: gpio_chip
  - gpio_base: resource *
  - pm_base: resource *
  - desc: ichx_desc *
  - orig_gpio_ctrl: u32
  - use_gpio: u8
  - outlvl_cache: int[3]

## Enums (1)

### GPIO_REG
- Line: 26

## Variables (15)

- static **avoton_desc** : ichx_desc (line 360)
- static **avoton_reglen** : const u8[3] (line 50)
- static **avoton_regs** : const u8[4][3] (line 44)
- static **i3100_desc** : ichx_desc (line 302)
- static **ich10_cons_desc** : ichx_desc (line 339)
- static **ich10_corp_desc** : ichx_desc (line 345)
- static **ich6_desc** : ichx_desc (line 287)
- static **ich7_desc** : ichx_desc (line 323)
- static **ich9_desc** : ichx_desc (line 331)
- static **ichx_gpio_driver** : platform_driver (line 476)
- **ichx_priv** : __anond4a9da5c0108 (line 95)
- static **ichx_reglen** : const u8[3] (line 40)
- static **ichx_regs** : const u8[4][3] (line 33)
- static **intel5_desc** : ichx_desc (line 353)
- static **modparam_gpiobase** : int (line 97)

## Macros (3)

- **DRV_NAME** (line 15)
- **ICHX_READ**(reg,base_res) (line 55)
- **ICHX_WRITE**(val,reg,base_res) (line 54)
