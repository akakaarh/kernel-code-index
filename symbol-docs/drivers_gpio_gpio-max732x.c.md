# drivers/gpio/gpio-max732x.c

Subsystem: drivers/gpio

## Functions (27)

### is_group_a
- Return type: static int
- Signature: is_group_a(struct max732x_chip * chip,unsigned off)
- Line: 189
- Called by: max732x_gpio_get_value, max732x_gpio_set_mask, max732x_probe

### max732x_exit
- Return type: static void __exit
- Signature: max732x_exit(void)
- Line: 728

### max732x_gpio_direction_input
- Return type: static int
- Signature: max732x_gpio_direction_input(struct gpio_chip * gc,unsigned off)
- Line: 255
- Calls: gpiochip_get_data, max732x_gpio_set_value
- Called by: max732x_irq_bus_sync_unlock

### max732x_gpio_direction_output
- Return type: static int
- Signature: max732x_gpio_direction_output(struct gpio_chip * gc,unsigned off,int val)
- Line: 276
- Calls: gpiochip_get_data, max732x_gpio_set_value

### max732x_gpio_get_value
- Return type: static int
- Signature: max732x_gpio_get_value(struct gpio_chip * gc,unsigned off)
- Line: 194
- Calls: gpiochip_get_data, is_group_a, max732x_readb

### max732x_gpio_set_mask
- Return type: static void
- Signature: max732x_gpio_set_mask(struct gpio_chip * gc,unsigned off,int mask,int val)
- Line: 207
- Calls: gpiochip_get_data, is_group_a, max732x_writeb
- Called by: max732x_gpio_set_multiple, max732x_gpio_set_value

### max732x_gpio_set_multiple
- Return type: static int
- Signature: max732x_gpio_set_multiple(struct gpio_chip * gc,unsigned long * mask,unsigned long * bits)
- Line: 241
- Calls: max732x_gpio_set_mask

### max732x_gpio_set_value
- Return type: static int
- Signature: max732x_gpio_set_value(struct gpio_chip * gc,unsigned int off,int val)
- Line: 230
- Calls: max732x_gpio_set_mask
- Called by: max732x_gpio_direction_input, max732x_gpio_direction_output

### max732x_init
- Return type: static int __init
- Signature: max732x_init(void)
- Line: 719

### max732x_irq_bus_lock
- Return type: static void
- Signature: max732x_irq_bus_lock(struct irq_data * d)
- Line: 367
- Calls: gpiochip_get_data

### max732x_irq_bus_sync_unlock
- Return type: static void
- Signature: max732x_irq_bus_sync_unlock(struct irq_data * d)
- Line: 376
- Calls: gpiochip_get_data, max732x_gpio_direction_input, max732x_irq_update_mask

### max732x_irq_handler
- Return type: static irqreturn_t
- Signature: max732x_irq_handler(int irq,void * devid)
- Line: 478
- Calls: max732x_irq_pending

### max732x_irq_mask
- Return type: static void
- Signature: max732x_irq_mask(struct irq_data * d)
- Line: 349
- Calls: gpiochip_disable_irq, gpiochip_get_data

### max732x_irq_pending
- Return type: static uint8_t
- Signature: max732x_irq_pending(struct max732x_chip * chip)
- Line: 447
- Calls: max732x_readw
- Called by: max732x_irq_handler

### max732x_irq_set_type
- Return type: static int
- Signature: max732x_irq_set_type(struct irq_data * d,unsigned int type)
- Line: 395
- Calls: gpiochip_get_data

### max732x_irq_set_wake
- Return type: static int
- Signature: max732x_irq_set_wake(struct irq_data * data,unsigned int on)
- Line: 427

### max732x_irq_setup
- Return type: static int
- Signature: max732x_irq_setup(struct max732x_chip * chip,const struct i2c_device_id * id)
- Line: 500
- Called by: max732x_probe

### max732x_irq_setup
- Return type: static int
- Signature: max732x_irq_setup(struct max732x_chip * chip,const struct i2c_device_id * id)
- Line: 540
- Called by: max732x_probe

### max732x_irq_unmask
- Return type: static void
- Signature: max732x_irq_unmask(struct irq_data * d)
- Line: 358
- Calls: gpiochip_enable_irq, gpiochip_get_data

### max732x_irq_update_mask
- Return type: static void
- Signature: max732x_irq_update_mask(struct max732x_chip * chip)
- Line: 322
- Calls: max732x_writeb, max732x_writew
- Called by: max732x_irq_bus_sync_unlock

### max732x_probe
- Return type: static int
- Signature: max732x_probe(struct i2c_client * client)
- Line: 616
- Calls: is_group_a, max732x_irq_setup, max732x_readb, max732x_setup_gpio, of_gpio_max732x

### max732x_readb
- Return type: static int
- Signature: max732x_readb(struct max732x_chip * chip,int group_a,uint8_t * val)
- Line: 173
- Called by: max732x_gpio_get_value, max732x_probe

### max732x_readw
- Return type: static int
- Signature: max732x_readw(struct max732x_chip * chip,uint16_t * val)
- Line: 308
- Called by: max732x_irq_pending

### max732x_setup_gpio
- Return type: static int
- Signature: max732x_setup_gpio(struct max732x_chip * chip,const struct i2c_device_id * id,unsigned gpio_start)
- Line: 553
- Called by: max732x_probe

### max732x_writeb
- Return type: static int
- Signature: max732x_writeb(struct max732x_chip * chip,int group_a,uint8_t val)
- Line: 158
- Called by: max732x_gpio_set_mask, max732x_irq_update_mask

### max732x_writew
- Return type: static int
- Signature: max732x_writew(struct max732x_chip * chip,uint16_t val)
- Line: 293
- Called by: max732x_irq_update_mask

### of_gpio_max732x
- Return type: static max732x_platform_data *
- Signature: of_gpio_max732x(struct device * dev)
- Line: 603
- Called by: max732x_probe

## Structs (1)

### max732x_chip
- Line: 133
- Members:
  - gpio_chip: gpio_chip
  - client: i2c_client *
  - client_dummy: i2c_client *
  - client_group_a: i2c_client *
  - client_group_b: i2c_client *
  - mask_group_a: unsigned int
  - dir_input: unsigned int
  - dir_output: unsigned int
  - lock: mutex
  - reg_out: uint8_t[2]
  - irq_lock: mutex
  - irq_mask: uint8_t
  - irq_mask_cur: uint8_t
  - irq_trig_raise: uint8_t
  - irq_trig_fall: uint8_t
  - irq_features: uint8_t

## Enums (1)

### __anon4b50d3e20103
- Line: 81

## Variables (5)

- static **max732x_driver** : i2c_driver (line 710)
- static **max732x_features** : uint64_t[] (line 93)
- static **max732x_id** : const struct i2c_device_id[] (line 105)
- static **max732x_irq_chip** : const struct irq_chip (line 435)
- static **max732x_of_table** : const struct of_device_id[] (line 119)

## Macros (16)

- **GROUP_A**(x) (line 71)
- **GROUP_B**(x) (line 72)
- **INT_CAPS**(x) (line 79)
- **INT_INDEP_MASK** (line 76)
- **INT_MERGED_MASK** (line 77)
- **INT_NONE** (line 74)
- **INT_NO_MASK** (line 75)
- **IO_4I4O** (line 65)
- **IO_4P4O** (line 66)
- **IO_8I** (line 67)
- **IO_8O** (line 69)
- **IO_8P** (line 68)
- **PORT_INPUT** (line 62)
- **PORT_NONE** (line 60)
- **PORT_OPENDRAIN** (line 63)
- **PORT_OUTPUT** (line 61)
