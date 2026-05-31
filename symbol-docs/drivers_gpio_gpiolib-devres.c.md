# drivers/gpio/gpiolib-devres.c

Subsystem: drivers/gpio

## Functions (14)

### devm_fwnode_gpiod_get_index
- Return type: gpio_desc *
- Signature: devm_fwnode_gpiod_get_index(struct device * dev,struct fwnode_handle * fwnode,const char * con_id,int index,enum gpiod_flags flags,const char * label)
- Line: 143
- Calls: gpiod_find_and_request

### devm_gpio_chip_release
- Return type: static void
- Signature: devm_gpio_chip_release(void * data)
- Line: 326
- Calls: gpiochip_remove

### devm_gpiochip_add_data_with_key
- Return type: int
- Signature: devm_gpiochip_add_data_with_key(struct device * dev,struct gpio_chip * gc,void * data,struct lock_class_key * lock_key,struct lock_class_key * request_key)
- Line: 350
- Calls: gpiochip_add_data_with_key

### devm_gpiod_get
- Return type: gpio_desc * __must_check
- Signature: devm_gpiod_get(struct device * dev,const char * con_id,enum gpiod_flags flags)
- Line: 47
- Calls: devm_gpiod_get_index
- Called by: gpio_lmux_probe

### devm_gpiod_get_array
- Return type: gpio_descs * __must_check
- Signature: devm_gpiod_get_array(struct device * dev,const char * con_id,enum gpiod_flags flags)
- Line: 212
- Calls: gpiod_get_array
- Called by: devm_gpiod_get_array_optional, gpio_la_poll_probe, gpio_latch_probe, gpio_virtuser_probe

### devm_gpiod_get_array_optional
- Return type: gpio_descs * __must_check
- Signature: devm_gpiod_get_array_optional(struct device * dev,const char * con_id,enum gpiod_flags flags)
- Line: 249
- Calls: devm_gpiod_get_array
- Called by: devm_gpiod_get_array_optional_count

### devm_gpiod_get_index
- Return type: gpio_desc * __must_check
- Signature: devm_gpiod_get_index(struct device * dev,const char * con_id,unsigned int idx,enum gpiod_flags flags)
- Line: 94
- Calls: gpiod_get_index
- Called by: devm_gpiod_get, devm_gpiod_get_index_optional, gpio_aggregator_probe

### devm_gpiod_get_index_optional
- Return type: gpio_desc * __must_check
- Signature: devm_gpiod_get_index_optional(struct device * dev,const char * con_id,unsigned int index,enum gpiod_flags flags)
- Line: 181
- Calls: devm_gpiod_get_index
- Called by: devm_gpiod_get_optional

### devm_gpiod_get_optional
- Return type: gpio_desc * __must_check
- Signature: devm_gpiod_get_optional(struct device * dev,const char * con_id,enum gpiod_flags flags)
- Line: 70
- Calls: devm_gpiod_get_index_optional
- Called by: gen_74x164_probe, pca953x_probe, pcf857x_probe, pisosr_gpio_probe, xra1403_probe

### devm_gpiod_put
- Return type: void
- Signature: devm_gpiod_put(struct device * dev,struct gpio_desc * desc)
- Line: 271

### devm_gpiod_put_array
- Return type: void
- Signature: devm_gpiod_put_array(struct device * dev,struct gpio_descs * descs)
- Line: 320
- Called by: max3191x_probe

### devm_gpiod_release
- Return type: static void
- Signature: devm_gpiod_release(void * desc)
- Line: 22
- Calls: gpiod_put

### devm_gpiod_release_array
- Return type: static void
- Signature: devm_gpiod_release_array(void * descs)
- Line: 27
- Calls: gpiod_put_array

### devm_gpiod_unhinge
- Return type: void
- Signature: devm_gpiod_unhinge(struct device * dev,struct gpio_desc * desc)
- Line: 291
