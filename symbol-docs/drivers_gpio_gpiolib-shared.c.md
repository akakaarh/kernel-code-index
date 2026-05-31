# drivers/gpio/gpiolib-shared.c

Subsystem: drivers/gpio

## Functions (25)

### devm_gpiod_shared_get
- Return type: gpio_shared_desc *
- Signature: devm_gpiod_shared_get(struct device * dev)
- Line: 674
- Calls: gpio_device_get_label, gpiod_hwgpio, gpiod_shared_desc_create
- Called by: gpio_shared_proxy_probe

### gpio_device_teardown_shared
- Return type: void
- Signature: gpio_device_teardown_shared(struct gpio_device * gdev)
- Line: 595
- Calls: gpio_shared_remove_adev, gpiod_free_commit, gpiod_remove_lookup_table
- Called by: gpiochip_add_data_with_key, gpiochip_remove

### gpio_shared_add_proxy_lookup
- Return type: int
- Signature: gpio_shared_add_proxy_lookup(struct device * consumer,struct fwnode_handle * fwnode,const char * con_id,unsigned long lflags)
- Line: 446
- Calls: gpio_shared_dev_is_reset_gpio, gpiod_add_lookup_table
- Called by: gpiod_find_and_request

### gpio_shared_adev_release
- Return type: static void
- Signature: gpio_shared_adev_release(struct device * dev)
- Line: 306

### gpio_shared_dev_is_reset_gpio
- Return type: static bool
- Signature: gpio_shared_dev_is_reset_gpio(struct device * consumer,struct gpio_shared_entry * entry,struct gpio_shared_ref * ref)
- Line: 356
- Called by: gpio_shared_add_proxy_lookup

### gpio_shared_dev_is_reset_gpio
- Return type: static bool
- Signature: gpio_shared_dev_is_reset_gpio(struct device * consumer,struct gpio_shared_entry * entry,struct gpio_shared_ref * ref)
- Line: 438
- Called by: gpio_shared_add_proxy_lookup

### gpio_shared_drop_entry
- Return type: static void
- Signature: gpio_shared_drop_entry(struct gpio_shared_entry * entry)
- Line: 722
- Called by: gpio_shared_free_exclusive, gpio_shared_teardown

### gpio_shared_drop_ref
- Return type: static void
- Signature: gpio_shared_drop_ref(struct gpio_shared_ref * ref)
- Line: 711
- Called by: gpio_shared_free_exclusive, gpio_shared_teardown

### gpio_shared_entry_is_really_shared
- Return type: static bool
- Signature: gpio_shared_entry_is_really_shared(struct gpio_shared_entry * entry)
- Line: 747
- Called by: gpio_shared_free_exclusive

### gpio_shared_find_entry
- Return type: static gpio_shared_entry *
- Signature: gpio_shared_find_entry(struct fwnode_handle * controller_node,unsigned int offset)
- Line: 68
- Called by: gpio_shared_of_traverse

### gpio_shared_free_exclusive
- Return type: static void
- Signature: gpio_shared_free_exclusive(void)
- Line: 773
- Calls: gpio_shared_drop_entry, gpio_shared_drop_ref, gpio_shared_entry_is_really_shared
- Called by: gpio_shared_init

### gpio_shared_init
- Return type: static int __init
- Signature: gpio_shared_init(void)
- Line: 788
- Calls: gpio_shared_free_exclusive, gpio_shared_of_scan, gpio_shared_teardown

### gpio_shared_make_adev
- Return type: static int
- Signature: gpio_shared_make_adev(struct gpio_device * gdev,struct gpio_shared_entry * entry,struct gpio_shared_ref * ref)
- Line: 311
- Calls: gpio_device_get_label
- Called by: gpiochip_setup_shared

### gpio_shared_make_ref
- Return type: static gpio_shared_ref *
- Signature: gpio_shared_make_ref(struct fwnode_handle * fwnode,const char * con_id,enum gpiod_flags flags)
- Line: 81
- Called by: gpio_shared_of_traverse, gpio_shared_setup_reset_proxy

### gpio_shared_of_node_ignore
- Return type: static bool
- Signature: gpio_shared_of_node_ignore(struct device_node * node)
- Line: 136
- Called by: gpio_shared_of_traverse

### gpio_shared_of_scan
- Return type: static int
- Signature: gpio_shared_of_scan(void)
- Line: 292
- Calls: gpio_shared_of_traverse
- Called by: gpio_shared_init

### gpio_shared_of_scan
- Return type: static int
- Signature: gpio_shared_of_scan(void)
- Line: 300
- Calls: gpio_shared_of_traverse
- Called by: gpio_shared_init

### gpio_shared_of_traverse
- Return type: static int
- Signature: gpio_shared_of_traverse(struct device_node * curr)
- Line: 159
- Calls: gpio_shared_find_entry, gpio_shared_make_ref, gpio_shared_of_node_ignore, gpio_shared_of_traverse, gpio_shared_setup_reset_proxy
- Called by: gpio_shared_of_scan, gpio_shared_of_traverse

### gpio_shared_release
- Return type: static void
- Signature: gpio_shared_release(struct kref * kref)
- Line: 623
- Calls: gpio_device_put

### gpio_shared_remove_adev
- Return type: static void
- Signature: gpio_shared_remove_adev(struct auxiliary_device * adev)
- Line: 503
- Called by: gpio_device_teardown_shared

### gpio_shared_setup_reset_proxy
- Return type: static int
- Signature: gpio_shared_setup_reset_proxy(struct gpio_shared_entry * entry,enum gpiod_flags flags)
- Line: 110
- Calls: gpio_shared_make_ref
- Called by: gpio_shared_of_traverse

### gpio_shared_teardown
- Return type: static void __init
- Signature: gpio_shared_teardown(void)
- Line: 734
- Calls: gpio_shared_drop_entry, gpio_shared_drop_ref
- Called by: gpio_shared_init

### gpiochip_setup_shared
- Return type: int
- Signature: gpiochip_setup_shared(struct gpio_chip * gc)
- Line: 509
- Calls: gpio_device_get_label, gpio_shared_make_adev, gpiod_free_commit, gpiod_request_commit
- Called by: gpiochip_add_data_with_key

### gpiod_shared_desc_create
- Return type: static gpio_shared_desc *
- Signature: gpiod_shared_desc_create(struct gpio_shared_entry * entry)
- Line: 647
- Calls: gpio_device_find_by_fwnode, gpiod_cansleep
- Called by: devm_gpiod_shared_get

### gpiod_shared_put
- Return type: static void
- Signature: gpiod_shared_put(void * data)
- Line: 639

## Structs (2)

### gpio_shared_entry
- Line: 48
- Members:
  - list: list_head
  - fwnode: fwnode_handle *
  - flags: gpiod_flags
  - con_id: char *
  - dev_id: int
  - lock: mutex
  - lock_key: lock_class_key
  - adev: auxiliary_device
  - lookup: gpiod_lookup_table *
  - is_reset_gpio: bool
  - list: list_head
  - fwnode: fwnode_handle *
  - offset: unsigned int
  - index: size_t
  - lock: mutex
  - shared_desc: gpio_shared_desc *
  - ref: kref
  - refs: list_head

### gpio_shared_ref
- Line: 31
- Members:
  - list: list_head
  - fwnode: fwnode_handle *
  - flags: gpiod_flags
  - con_id: char *
  - dev_id: int
  - lock: mutex
  - lock_key: lock_class_key
  - adev: auxiliary_device
  - lookup: gpiod_lookup_table *
  - is_reset_gpio: bool
  - list: list_head
  - fwnode: fwnode_handle *
  - offset: unsigned int
  - index: size_t
  - lock: mutex
  - shared_desc: gpio_shared_desc *
  - ref: kref
  - refs: list_head

## Macros (1)

- **pr_fmt**(fmt) (line 6)
