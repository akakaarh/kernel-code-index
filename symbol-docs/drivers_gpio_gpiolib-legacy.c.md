# drivers/gpio/gpiolib-legacy.c

Subsystem: drivers/gpio

## Functions (5)

### devm_gpio_release
- Return type: static void
- Signature: devm_gpio_release(void * gpio)
- Line: 71
- Calls: gpio_free

### devm_gpio_request_one
- Return type: int
- Signature: devm_gpio_request_one(struct device * dev,unsigned gpio,unsigned long flags,const char * label)
- Line: 88
- Calls: gpio_free, gpio_request

### gpio_free
- Return type: void
- Signature: gpio_free(unsigned gpio)
- Line: 18
- Calls: gpio_to_desc, gpiod_free
- Called by: devm_gpio_release, devm_gpio_request_one, gpio_request_one

### gpio_request
- Return type: int
- Signature: gpio_request(unsigned gpio,const char * label)
- Line: 58
- Calls: gpio_to_desc, gpiod_request
- Called by: devm_gpio_request_one, gpio_request_one

### gpio_request_one
- Return type: int
- Signature: gpio_request_one(unsigned gpio,unsigned long flags,const char * label)
- Line: 35
- Calls: gpio_free, gpio_request
