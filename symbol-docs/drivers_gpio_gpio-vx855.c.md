# drivers/gpio/gpio-vx855.c

Subsystem: drivers/gpio

## Functions (11)

### gpi_i_bit
- Return type: static u_int32_t
- Signature: gpi_i_bit(int i)
- Line: 42
- Called by: vx855gpio_get

### gpio_i_bit
- Return type: static u_int32_t
- Signature: gpio_i_bit(int i)
- Line: 58
- Called by: vx855gpio_get

### gpio_o_bit
- Return type: static u_int32_t
- Signature: gpio_o_bit(int i)
- Line: 66
- Called by: vx855gpio_direction_input, vx855gpio_set

### gpo_o_bit
- Return type: static u_int32_t
- Signature: gpo_o_bit(int i)
- Line: 50
- Called by: vx855gpio_get, vx855gpio_set

### vx855gpio_direction_input
- Return type: static int
- Signature: vx855gpio_direction_input(struct gpio_chip * gpio,unsigned int nr)
- Line: 80
- Calls: gpio_o_bit, gpiochip_get_data

### vx855gpio_direction_output
- Return type: static int
- Signature: vx855gpio_direction_output(struct gpio_chip * gpio,unsigned int nr,int val)
- Line: 159
- Calls: vx855gpio_set

### vx855gpio_get
- Return type: static int
- Signature: vx855gpio_get(struct gpio_chip * gpio,unsigned int nr)
- Line: 105
- Calls: gpi_i_bit, gpio_i_bit, gpiochip_get_data, gpo_o_bit

### vx855gpio_gpio_setup
- Return type: static void
- Signature: vx855gpio_gpio_setup(struct vx855_gpio * vg)
- Line: 210
- Called by: vx855gpio_probe

### vx855gpio_probe
- Return type: static int
- Signature: vx855gpio_probe(struct platform_device * pdev)
- Line: 229
- Calls: vx855gpio_gpio_setup

### vx855gpio_set
- Return type: static int
- Signature: vx855gpio_set(struct gpio_chip * gpio,unsigned int nr,int val)
- Line: 130
- Calls: gpio_o_bit, gpiochip_get_data, gpo_o_bit
- Called by: vx855gpio_direction_output

### vx855gpio_set_config
- Return type: static int
- Signature: vx855gpio_set_config(struct gpio_chip * gpio,unsigned int nr,unsigned long config)
- Line: 174

## Structs (1)

### vx855_gpio
- Line: 34
- Members:
  - gpio: gpio_chip
  - lock: spinlock_t
  - io_gpi: u32
  - io_gpo: u32

## Variables (2)

- static **vx855gpio_driver** : platform_driver (line 272)
- static **vx855gpio_names** : const char * [] (line 197)

## Macros (6)

- **MODULE_NAME** (line 19)
- **NR_VX855_GP** (line 32)
- **NR_VX855_GPI** (line 27)
- **NR_VX855_GPIO** (line 29)
- **NR_VX855_GPInO** (line 31)
- **NR_VX855_GPO** (line 28)
