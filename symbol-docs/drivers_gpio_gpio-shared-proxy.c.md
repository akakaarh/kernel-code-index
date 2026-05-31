# drivers/gpio/gpio-shared-proxy.c

Subsystem: drivers/gpio

## Functions (14)

### gpio_shared_proxy_direction_input
- Return type: static int
- Signature: gpio_shared_proxy_direction_input(struct gpio_chip * gc,unsigned int offset)
- Line: 143
- Calls: gpiochip_get_data, gpiod_direction_input, gpiod_get_direction

### gpio_shared_proxy_direction_output
- Return type: static int
- Signature: gpio_shared_proxy_direction_output(struct gpio_chip * gc,unsigned int offset,int value)
- Line: 173
- Calls: gpio_shared_proxy_set_unlocked, gpiochip_get_data, gpiod_direction_output, gpiod_get_direction

### gpio_shared_proxy_do_set
- Return type: static int
- Signature: gpio_shared_proxy_do_set(struct gpio_shared_proxy_data * proxy,int (* set_func)(struct gpio_desc * desc,int value),int value)
- Line: 231
- Calls: gpio_shared_proxy_set_unlocked
- Called by: gpio_shared_proxy_set, gpio_shared_proxy_set_cansleep

### gpio_shared_proxy_free
- Return type: static void
- Signature: gpio_shared_proxy_free(struct gpio_chip * gc,unsigned int offset)
- Line: 102
- Calls: gpiochip_get_data

### gpio_shared_proxy_get
- Return type: static int
- Signature: gpio_shared_proxy_get(struct gpio_chip * gc,unsigned int offset)
- Line: 216
- Calls: gpiochip_get_data, gpiod_get_value

### gpio_shared_proxy_get_cansleep
- Return type: static int
- Signature: gpio_shared_proxy_get_cansleep(struct gpio_chip * gc,unsigned int offset)
- Line: 223
- Calls: gpiochip_get_data, gpiod_get_value_cansleep

### gpio_shared_proxy_get_direction
- Return type: static int
- Signature: gpio_shared_proxy_get_direction(struct gpio_chip * gc,unsigned int offset)
- Line: 256
- Calls: gpiochip_get_data, gpiod_get_direction

### gpio_shared_proxy_probe
- Return type: static int
- Signature: gpio_shared_proxy_probe(struct auxiliary_device * adev,const struct auxiliary_device_id * id)
- Line: 271
- Calls: devm_gpiod_shared_get

### gpio_shared_proxy_request
- Return type: static int
- Signature: gpio_shared_proxy_request(struct gpio_chip * gc,unsigned int offset)
- Line: 87
- Calls: gpiochip_get_data

### gpio_shared_proxy_set
- Return type: static int
- Signature: gpio_shared_proxy_set(struct gpio_chip * gc,unsigned int offset,int value)
- Line: 240
- Calls: gpio_shared_proxy_do_set, gpiochip_get_data

### gpio_shared_proxy_set_cansleep
- Return type: static int
- Signature: gpio_shared_proxy_set_cansleep(struct gpio_chip * gc,unsigned int offset,int value)
- Line: 248
- Calls: gpio_shared_proxy_do_set, gpiochip_get_data

### gpio_shared_proxy_set_config
- Return type: static int
- Signature: gpio_shared_proxy_set_config(struct gpio_chip * gc,unsigned int offset,unsigned long cfg)
- Line: 115
- Calls: gpiochip_get_data, gpiod_set_config

### gpio_shared_proxy_set_unlocked
- Return type: static int
- Signature: gpio_shared_proxy_set_unlocked(struct gpio_shared_proxy_data * proxy,int (* set_func)(struct gpio_desc * desc,int value),int value)
- Line: 27
- Called by: gpio_shared_proxy_direction_output, gpio_shared_proxy_do_set

### gpio_shared_proxy_to_irq
- Return type: static int
- Signature: gpio_shared_proxy_to_irq(struct gpio_chip * gc,unsigned int offset)
- Line: 264
- Calls: gpiochip_get_data, gpiod_to_irq

## Structs (1)

### gpio_shared_proxy_data
- Line: 19
- Members:
  - gc: gpio_chip
  - shared_desc: gpio_shared_desc *
  - dev: device *
  - voted_high: bool

## Variables (2)

- static **gpio_shared_proxy_driver** : auxiliary_driver (line 322)
- static **gpio_shared_proxy_id_table** : const struct auxiliary_device_id[] (line 316)
