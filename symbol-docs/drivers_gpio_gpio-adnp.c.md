# drivers/gpio/gpio-adnp.c

Subsystem: drivers/gpio

## Functions (17)

### __adnp_gpio_set
- Return type: static int
- Signature: __adnp_gpio_set(struct adnp * adnp,unsigned int offset,int value)
- Line: 83
- Calls: adnp_read, adnp_write
- Called by: adnp_gpio_direction_output, adnp_gpio_set

### adnp_gpio_dbg_show
- Return type: static void
- Signature: adnp_gpio_dbg_show(struct seq_file * s,struct gpio_chip * chip)
- Line: 174
- Calls: adnp_read, gpiochip_get_data

### adnp_gpio_direction_input
- Return type: static int
- Signature: adnp_gpio_direction_input(struct gpio_chip * chip,unsigned offset)
- Line: 111
- Calls: adnp_read, adnp_write, gpiochip_get_data

### adnp_gpio_direction_output
- Return type: static int
- Signature: adnp_gpio_direction_output(struct gpio_chip * chip,unsigned offset,int value)
- Line: 141
- Calls: __adnp_gpio_set, adnp_read, adnp_write, gpiochip_get_data

### adnp_gpio_get
- Return type: static int
- Signature: adnp_gpio_get(struct gpio_chip * chip,unsigned offset)
- Line: 68
- Calls: adnp_read, gpiochip_get_data

### adnp_gpio_set
- Return type: static int
- Signature: adnp_gpio_set(struct gpio_chip * chip,unsigned int offset,int value)
- Line: 102
- Calls: __adnp_gpio_set, gpiochip_get_data

### adnp_gpio_setup
- Return type: static int
- Signature: adnp_gpio_setup(struct adnp * adnp,unsigned int num_gpios,bool is_irq_controller)
- Line: 422
- Calls: adnp_irq_setup
- Called by: adnp_i2c_probe

### adnp_i2c_probe
- Return type: static int
- Signature: adnp_i2c_probe(struct i2c_client * client)
- Line: 471
- Calls: adnp_gpio_setup

### adnp_irq
- Return type: static irqreturn_t
- Signature: adnp_irq(int irq,void * data)
- Line: 227
- Calls: adnp_read

### adnp_irq_bus_lock
- Return type: static void
- Signature: adnp_irq_bus_lock(struct irq_data * d)
- Line: 331
- Calls: gpiochip_get_data

### adnp_irq_bus_unlock
- Return type: static void
- Signature: adnp_irq_bus_unlock(struct irq_data * d)
- Line: 339
- Calls: adnp_write, gpiochip_get_data

### adnp_irq_mask
- Return type: static void
- Signature: adnp_irq_mask(struct irq_data * d)
- Line: 279
- Calls: gpiochip_disable_irq, gpiochip_get_data

### adnp_irq_set_type
- Return type: static int
- Signature: adnp_irq_set_type(struct irq_data * d,unsigned int type)
- Line: 301
- Calls: gpiochip_get_data

### adnp_irq_setup
- Return type: static int
- Signature: adnp_irq_setup(struct adnp * adnp)
- Line: 365
- Calls: adnp_read, adnp_write
- Called by: adnp_gpio_setup

### adnp_irq_unmask
- Return type: static void
- Signature: adnp_irq_unmask(struct irq_data * d)
- Line: 290
- Calls: gpiochip_enable_irq, gpiochip_get_data

### adnp_read
- Return type: static int
- Signature: adnp_read(struct adnp * adnp,unsigned offset,uint8_t * value)
- Line: 39
- Called by: __adnp_gpio_set, adnp_gpio_dbg_show, adnp_gpio_direction_input, adnp_gpio_direction_output, adnp_gpio_get, adnp_irq, adnp_irq_setup

### adnp_write
- Return type: static int
- Signature: adnp_write(struct adnp * adnp,unsigned offset,uint8_t value)
- Line: 54
- Called by: __adnp_gpio_set, adnp_gpio_direction_input, adnp_gpio_direction_output, adnp_irq_bus_unlock, adnp_irq_setup

## Structs (1)

### adnp
- Line: 23
- Members:
  - client: i2c_client *
  - gpio: gpio_chip
  - reg_shift: unsigned int
  - i2c_lock: mutex
  - irq_lock: mutex
  - irq_enable: u8 *
  - irq_level: u8 *
  - irq_rise: u8 *
  - irq_fall: u8 *
  - irq_high: u8 *
  - irq_low: u8 *

## Variables (4)

- static **adnp_i2c_driver** : i2c_driver (line 513)
- static **adnp_i2c_id** : const struct i2c_device_id[] (line 501)
- static **adnp_irq_chip** : const struct irq_chip (line 354)
- static **adnp_of_match** : const struct of_device_id[] (line 507)

## Macros (5)

- **GPIO_DDR**(gpio) (line 17)
- **GPIO_IER**(gpio) (line 19)
- **GPIO_ISR**(gpio) (line 20)
- **GPIO_PLR**(gpio) (line 18)
- **GPIO_PTR**(gpio) (line 21)
