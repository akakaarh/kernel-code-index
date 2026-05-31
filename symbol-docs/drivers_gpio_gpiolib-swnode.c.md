# drivers/gpio/gpiolib-swnode.c

Subsystem: drivers/gpio

## Functions (6)

### swnode_find_gpio
- Return type: gpio_desc *
- Signature: swnode_find_gpio(struct fwnode_handle * fwnode,const char * con_id,unsigned int idx,unsigned long * flags)
- Line: 78
- Calls: gpio_device_get_desc, swnode_get_gpio_device, swnode_gpio_get_reference
- Called by: gpiod_find_by_fwnode

### swnode_get_gpio_device
- Return type: static gpio_device *
- Signature: swnode_get_gpio_device(struct fwnode_handle * fwnode)
- Line: 26
- Calls: gpio_device_find_by_fwnode, gpio_device_find_by_label
- Called by: swnode_find_gpio

### swnode_gpio_cleanup
- Return type: static void __exit
- Signature: swnode_gpio_cleanup(void)
- Line: 185

### swnode_gpio_count
- Return type: int
- Signature: swnode_gpio_count(const struct fwnode_handle * fwnode,const char * con_id)
- Line: 140
- Calls: swnode_gpio_get_reference
- Called by: gpiod_count

### swnode_gpio_get_reference
- Return type: static int
- Signature: swnode_gpio_get_reference(const struct fwnode_handle * fwnode,const char * propname,unsigned int idx,struct fwnode_reference_args * args)
- Line: 67
- Called by: swnode_find_gpio, swnode_gpio_count

### swnode_gpio_init
- Return type: static int __init
- Signature: swnode_gpio_init(void)
- Line: 173

## Variables (1)

- **swnode_gpio_undefined** : const struct software_node (line 168)

## Macros (1)

- **pr_fmt**(fmt) (line 8)
