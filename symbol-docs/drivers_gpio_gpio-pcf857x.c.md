# drivers/gpio/gpio-pcf857x.c

Subsystem: drivers/gpio

## Functions (21)

### i2c_read_le16
- Return type: static int
- Signature: i2c_read_le16(struct i2c_client * client)
- Line: 107
- Called by: pcf857x_probe

### i2c_read_le8
- Return type: static int
- Signature: i2c_read_le8(struct i2c_client * client)
- Line: 91

### i2c_write_le16
- Return type: static int
- Signature: i2c_write_le16(struct i2c_client * client,unsigned int word)
- Line: 98

### i2c_write_le8
- Return type: static int
- Signature: i2c_write_le8(struct i2c_client * client,unsigned int data)
- Line: 86

### noop
- Return type: static void
- Signature: noop(struct irq_data * data)
- Line: 221

### pcf857x_exit
- Return type: static void __exit
- Signature: pcf857x_exit(void)
- Line: 463

### pcf857x_get
- Return type: static int
- Signature: pcf857x_get(struct gpio_chip * chip,unsigned int offset)
- Line: 133
- Calls: gpiochip_get_data

### pcf857x_get_multiple
- Return type: static int
- Signature: pcf857x_get_multiple(struct gpio_chip * chip,unsigned long * mask,unsigned long * bits)
- Line: 142
- Calls: gpiochip_get_data

### pcf857x_init
- Return type: static int __init
- Signature: pcf857x_init(void)
- Line: 454

### pcf857x_input
- Return type: static int
- Signature: pcf857x_input(struct gpio_chip * chip,unsigned int offset)
- Line: 120
- Calls: gpiochip_get_data

### pcf857x_irq
- Return type: static irqreturn_t
- Signature: pcf857x_irq(int irq,void * data)
- Line: 196

### pcf857x_irq_bus_lock
- Return type: static void
- Signature: pcf857x_irq_bus_lock(struct irq_data * data)
- Line: 248

### pcf857x_irq_bus_sync_unlock
- Return type: static void
- Signature: pcf857x_irq_bus_sync_unlock(struct irq_data * data)
- Line: 255

### pcf857x_irq_disable
- Return type: static void
- Signature: pcf857x_irq_disable(struct irq_data * data)
- Line: 239
- Calls: gpiochip_disable_irq

### pcf857x_irq_enable
- Return type: static void
- Signature: pcf857x_irq_enable(struct irq_data * data)
- Line: 230
- Calls: gpiochip_enable_irq

### pcf857x_irq_set_wake
- Return type: static int
- Signature: pcf857x_irq_set_wake(struct irq_data * data,unsigned int on)
- Line: 223

### pcf857x_output
- Return type: static int
- Signature: pcf857x_output(struct gpio_chip * chip,unsigned int offset,int value)
- Line: 157
- Calls: gpiochip_get_data
- Called by: pcf857x_set

### pcf857x_probe
- Return type: static int
- Signature: pcf857x_probe(struct i2c_client * client)
- Line: 278
- Calls: devm_gpiod_get_optional, gpiod_set_value_cansleep, i2c_read_le16

### pcf857x_set
- Return type: static int
- Signature: pcf857x_set(struct gpio_chip * chip,unsigned int offset,int value)
- Line: 174
- Calls: pcf857x_output

### pcf857x_set_multiple
- Return type: static int
- Signature: pcf857x_set_multiple(struct gpio_chip * chip,unsigned long * mask,unsigned long * bits)
- Line: 179
- Calls: gpiochip_get_data

### pcf857x_shutdown
- Return type: static void
- Signature: pcf857x_shutdown(struct i2c_client * client)
- Line: 436

## Structs (1)

### pcf857x
- Line: 70
- Members:
  - chip: gpio_chip
  - client: i2c_client *
  - lock: mutex
  - out: unsigned int
  - status: unsigned int
  - irq_enabled: unsigned int
  - write: int (*)(struct i2c_client * client,unsigned int data)
  - read: int (*)(struct i2c_client * client)

## Variables (4)

- static **pcf857x_driver** : i2c_driver (line 444)
- static **pcf857x_id** : const struct i2c_device_id[] (line 22)
- static **pcf857x_irq_chip** : const struct irq_chip (line 262)
- static **pcf857x_of_table** : const struct of_device_id[] (line 40)
