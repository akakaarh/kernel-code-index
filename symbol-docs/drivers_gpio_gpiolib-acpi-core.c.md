# drivers/gpio/gpiolib-acpi-core.c

Subsystem: drivers/gpio

## Functions (42)

### __acpi_find_gpio
- Return type: static gpio_desc *
- Signature: __acpi_find_gpio(struct fwnode_handle * fwnode,const char * con_id,unsigned int idx,bool can_fallback,struct acpi_gpio_info * info)
- Line: 902
- Calls: acpi_get_gpiod_by_index, acpi_get_gpiod_from_data
- Called by: acpi_dev_gpio_irq_wake_get_by, acpi_find_gpio

### __acpi_gpio_update_gpiod_flags
- Return type: static int
- Signature: __acpi_gpio_update_gpiod_flags(enum gpiod_flags * flags,enum gpiod_flags update)
- Line: 606
- Called by: acpi_gpio_update_gpiod_flags

### acpi_can_fallback_to_crs
- Return type: static bool
- Signature: acpi_can_fallback_to_crs(struct acpi_device * adev,const char * con_id)
- Line: 887
- Called by: acpi_find_gpio, acpi_gpio_count

### acpi_dev_add_driver_gpios
- Return type: int
- Signature: acpi_dev_add_driver_gpios(struct acpi_device * adev,const struct acpi_gpio_mapping * gpios)
- Line: 541
- Called by: devm_acpi_dev_add_driver_gpios

### acpi_dev_gpio_irq_wake_get_by
- Return type: int
- Signature: acpi_dev_gpio_irq_wake_get_by(struct acpi_device * adev,const char * con_id,int index,bool * wake_capable)
- Line: 996
- Calls: __acpi_find_gpio, acpi_gpio_update_gpiod_flags, acpi_gpio_update_gpiod_lookup_flags, gpio_set_debounce_timeout, gpiod_configure_flags, gpiod_set_consumer_name, gpiod_to_irq

### acpi_dev_release_driver_gpios
- Return type: static void
- Signature: acpi_dev_release_driver_gpios(void * adev)
- Line: 559
- Calls: acpi_dev_remove_driver_gpios

### acpi_dev_remove_driver_gpios
- Return type: void
- Signature: acpi_dev_remove_driver_gpios(struct acpi_device * adev)
- Line: 552
- Called by: acpi_dev_release_driver_gpios

### acpi_find_gpio
- Return type: gpio_desc *
- Signature: acpi_find_gpio(struct fwnode_handle * fwnode,const char * con_id,unsigned int idx,enum gpiod_flags * dflags,unsigned long * lookupflags)
- Line: 944
- Calls: __acpi_find_gpio, acpi_can_fallback_to_crs, acpi_gpio_set_debounce_timeout, acpi_gpio_update_gpiod_flags, acpi_gpio_update_gpiod_lookup_flags
- Called by: gpiod_find_by_fwnode

### acpi_find_gpio_count
- Return type: static int
- Signature: acpi_find_gpio_count(struct acpi_resource * ares,void * data)
- Line: 1308

### acpi_get_driver_gpio_data
- Return type: static bool
- Signature: acpi_get_driver_gpio_data(struct acpi_device * adev,const char * name,int index,struct fwnode_reference_args * args,unsigned int * quirks)
- Line: 578
- Called by: acpi_gpio_property_lookup

### acpi_get_gpiod
- Return type: static gpio_desc *
- Signature: acpi_get_gpiod(char * path,unsigned int pin)
- Line: 131
- Calls: gpio_device_find, gpio_device_get_desc
- Called by: acpi_populate_gpio_lookup

### acpi_get_gpiod_by_index
- Return type: static int
- Signature: acpi_get_gpiod_by_index(struct acpi_device * adev,const char * propname,struct acpi_gpio_lookup * lookup)
- Line: 828
- Calls: acpi_gpio_property_lookup, acpi_gpio_resource_lookup
- Called by: __acpi_find_gpio

### acpi_get_gpiod_from_data
- Return type: static int
- Signature: acpi_get_gpiod_from_data(struct fwnode_handle * fwnode,const char * propname,struct acpi_gpio_lookup * lookup)
- Line: 869
- Calls: acpi_gpio_property_lookup, acpi_gpio_resource_lookup
- Called by: __acpi_find_gpio

### acpi_gpio_adr_space_handler
- Return type: static acpi_status
- Signature: acpi_gpio_adr_space_handler(u32 function,acpi_physical_address address,u32 bits,u64 * value,void * handler_context,void * region_context)
- Line: 1071
- Calls: acpi_request_own_gpiod, gpiochip_free_own_desc, gpiod_get_raw_value_cansleep, gpiod_set_raw_value_cansleep

### acpi_gpio_chip_dh
- Return type: static void
- Signature: acpi_gpio_chip_dh(acpi_handle handle,void * data)
- Line: 170

### acpi_gpio_count
- Return type: int
- Signature: acpi_gpio_count(const struct fwnode_handle * fwnode,const char * con_id)
- Line: 1327
- Calls: acpi_can_fallback_to_crs, acpi_gpio_package_count
- Called by: gpiod_count

### acpi_gpio_get_io_resource
- Return type: bool
- Signature: acpi_gpio_get_io_resource(struct acpi_resource * ares,struct acpi_resource_gpio ** agpio)
- Line: 201

### acpi_gpio_get_irq_resource
- Return type: bool
- Signature: acpi_gpio_get_irq_resource(struct acpi_resource * ares,struct acpi_resource_gpio ** agpio)
- Line: 175
- Called by: acpi_gpiochip_alloc_event

### acpi_gpio_irq_handler
- Return type: static irqreturn_t
- Signature: acpi_gpio_irq_handler(int irq,void * data)
- Line: 152

### acpi_gpio_irq_handler_evt
- Return type: static irqreturn_t
- Signature: acpi_gpio_irq_handler_evt(int irq,void * data)
- Line: 161

### acpi_gpio_irq_is_wake
- Return type: static bool
- Signature: acpi_gpio_irq_is_wake(struct device * parent,const struct acpi_resource_gpio * agpio)
- Line: 326
- Calls: acpi_gpio_in_ignore_list
- Called by: acpi_gpiochip_alloc_event, acpi_populate_gpio_lookup

### acpi_gpio_package_count
- Return type: static int
- Signature: acpi_gpio_package_count(const union acpi_object * obj)
- Line: 1283
- Called by: acpi_gpio_count

### acpi_gpio_process_deferred_list
- Return type: void __init
- Signature: acpi_gpio_process_deferred_list(struct list_head * list)
- Line: 533
- Calls: acpi_gpiochip_request_irqs
- Called by: acpi_gpio_handle_deferred_request_irqs

### acpi_gpio_property_lookup
- Return type: static int
- Signature: acpi_gpio_property_lookup(struct fwnode_handle * fwnode,const char * propname,struct acpi_gpio_lookup * lookup)
- Line: 765
- Calls: acpi_get_driver_gpio_data
- Called by: acpi_get_gpiod_by_index, acpi_get_gpiod_from_data

### acpi_gpio_resource_lookup
- Return type: static int
- Signature: acpi_gpio_resource_lookup(struct acpi_gpio_lookup * lookup)
- Line: 742
- Called by: acpi_get_gpiod_by_index, acpi_get_gpiod_from_data

### acpi_gpio_set_debounce_timeout
- Return type: static void
- Signature: acpi_gpio_set_debounce_timeout(struct gpio_desc * desc,unsigned int acpi_debounce)
- Line: 294
- Calls: gpio_set_debounce_timeout
- Called by: acpi_find_gpio, acpi_request_own_gpiod

### acpi_gpio_to_gpiod_flags
- Return type: static gpiod_flags
- Signature: acpi_gpio_to_gpiod_flags(const struct acpi_resource_gpio * agpio,int polarity)
- Line: 255
- Called by: acpi_populate_gpio_lookup, acpi_request_own_gpiod

### acpi_gpio_update_gpiod_flags
- Return type: static int
- Signature: acpi_gpio_update_gpiod_flags(enum gpiod_flags * flags,struct acpi_gpio_info * info)
- Line: 636
- Calls: __acpi_gpio_update_gpiod_flags
- Called by: acpi_dev_gpio_irq_wake_get_by, acpi_find_gpio

### acpi_gpio_update_gpiod_lookup_flags
- Return type: static int
- Signature: acpi_gpio_update_gpiod_lookup_flags(unsigned long * lookupflags,struct acpi_gpio_info * info)
- Line: 656
- Called by: acpi_dev_gpio_irq_wake_get_by, acpi_find_gpio

### acpi_gpiochip_add
- Return type: void
- Signature: acpi_gpiochip_add(struct gpio_chip * chip)
- Line: 1223
- Calls: acpi_gpiochip_request_regions
- Called by: gpiochip_add_data_with_key

### acpi_gpiochip_alloc_event
- Return type: static acpi_status
- Signature: acpi_gpiochip_alloc_event(struct acpi_resource * ares,void * context)
- Line: 343
- Calls: acpi_gpio_get_irq_resource, acpi_gpio_in_ignore_list, acpi_gpio_irq_is_wake, acpi_request_own_gpiod, gpiochip_free_own_desc, gpiochip_lock_as_irq, gpiochip_unlock_as_irq, gpiod_to_irq

### acpi_gpiochip_find
- Return type: static int
- Signature: acpi_gpiochip_find(struct gpio_chip * gc,const void * data)
- Line: 95

### acpi_gpiochip_free_interrupts
- Return type: void
- Signature: acpi_gpiochip_free_interrupts(struct gpio_chip * chip)
- Line: 497
- Calls: acpi_gpio_remove_from_deferred_list, gpiochip_free_own_desc, gpiochip_unlock_as_irq
- Called by: gpiochip_irqchip_remove, mb86s70_gpio_remove, xgene_gpio_sb_remove

### acpi_gpiochip_free_regions
- Return type: static void
- Signature: acpi_gpiochip_free_regions(struct acpi_gpio_chip * achip)
- Line: 1201
- Calls: gpiochip_free_own_desc
- Called by: acpi_gpiochip_remove

### acpi_gpiochip_remove
- Return type: void
- Signature: acpi_gpiochip_remove(struct gpio_chip * chip)
- Line: 1258
- Calls: acpi_gpiochip_free_regions
- Called by: gpiochip_add_data_with_key, gpiochip_remove

### acpi_gpiochip_request_interrupts
- Return type: void
- Signature: acpi_gpiochip_request_interrupts(struct gpio_chip * chip)
- Line: 460
- Calls: acpi_gpio_add_to_deferred_list, acpi_gpiochip_request_irqs
- Called by: gpiochip_add_irqchip, mb86s70_gpio_probe, xgene_gpio_sb_probe

### acpi_gpiochip_request_irq
- Return type: static void
- Signature: acpi_gpiochip_request_irq(struct acpi_gpio_chip * acpi_gpio,struct acpi_gpio_event * event)
- Line: 218
- Calls: acpi_gpio_need_run_edge_events_on_boot, gpiod_get_raw_value_cansleep
- Called by: acpi_gpiochip_request_irqs

### acpi_gpiochip_request_irqs
- Return type: static void
- Signature: acpi_gpiochip_request_irqs(struct acpi_gpio_chip * acpi_gpio)
- Line: 246
- Calls: acpi_gpiochip_request_irq
- Called by: acpi_gpio_process_deferred_list, acpi_gpiochip_request_interrupts

### acpi_gpiochip_request_regions
- Return type: static void
- Signature: acpi_gpiochip_request_regions(struct acpi_gpio_chip * achip)
- Line: 1185
- Called by: acpi_gpiochip_add

### acpi_populate_gpio_lookup
- Return type: static int
- Signature: acpi_populate_gpio_lookup(struct acpi_resource * ares,void * data)
- Line: 686
- Calls: acpi_get_gpiod, acpi_gpio_irq_is_wake, acpi_gpio_to_gpiod_flags, gpio_to_desc

### acpi_request_own_gpiod
- Return type: static gpio_desc *
- Signature: acpi_request_own_gpiod(struct gpio_chip * chip,struct acpi_resource_gpio * agpio,unsigned int index,const char * label)
- Line: 307
- Calls: acpi_gpio_set_debounce_timeout, acpi_gpio_to_gpiod_flags, gpiochip_request_own_desc
- Called by: acpi_gpio_adr_space_handler, acpi_gpiochip_alloc_event

### devm_acpi_dev_add_driver_gpios
- Return type: int
- Signature: devm_acpi_dev_add_driver_gpios(struct device * dev,const struct acpi_gpio_mapping * gpios)
- Line: 564
- Calls: acpi_dev_add_driver_gpios
- Called by: pca953x_acpi_get_irq

## Structs (5)

### acpi_gpio_chip
- Line: 57
- Members:
  - node: list_head
  - handle: acpi_handle
  - handler: irq_handler_t
  - pin: unsigned int
  - irq: unsigned int
  - irqflags: unsigned long
  - irq_is_wake: bool
  - irq_requested: bool
  - desc: gpio_desc *
  - node: list_head
  - pin: unsigned int
  - desc: gpio_desc *
  - conn_info: acpi_connection_info
  - conns: list_head
  - conn_lock: mutex
  - chip: gpio_chip *
  - events: list_head
  - deferred_req_irqs_list_entry: list_head
  - adev: acpi_device *
  - flags: gpiod_flags
  - gpioint: bool
  - wake_capable: bool
  - pin_config: int
  - polarity: int
  - triggering: int
  - debounce: unsigned int
  - quirks: unsigned int
  - params: acpi_gpio_params
  - info: acpi_gpio_info *
  - desc: gpio_desc *
  - n: int

### acpi_gpio_connection
- Line: 51
- Members:
  - node: list_head
  - handle: acpi_handle
  - handler: irq_handler_t
  - pin: unsigned int
  - irq: unsigned int
  - irqflags: unsigned long
  - irq_is_wake: bool
  - irq_requested: bool
  - desc: gpio_desc *
  - node: list_head
  - pin: unsigned int
  - desc: gpio_desc *
  - conn_info: acpi_connection_info
  - conns: list_head
  - conn_lock: mutex
  - chip: gpio_chip *
  - events: list_head
  - deferred_req_irqs_list_entry: list_head
  - adev: acpi_device *
  - flags: gpiod_flags
  - gpioint: bool
  - wake_capable: bool
  - pin_config: int
  - polarity: int
  - triggering: int
  - debounce: unsigned int
  - quirks: unsigned int
  - params: acpi_gpio_params
  - info: acpi_gpio_info *
  - desc: gpio_desc *
  - n: int

### acpi_gpio_event
- Line: 39
- Members:
  - node: list_head
  - handle: acpi_handle
  - handler: irq_handler_t
  - pin: unsigned int
  - irq: unsigned int
  - irqflags: unsigned long
  - irq_is_wake: bool
  - irq_requested: bool
  - desc: gpio_desc *
  - node: list_head
  - pin: unsigned int
  - desc: gpio_desc *
  - conn_info: acpi_connection_info
  - conns: list_head
  - conn_lock: mutex
  - chip: gpio_chip *
  - events: list_head
  - deferred_req_irqs_list_entry: list_head
  - adev: acpi_device *
  - flags: gpiod_flags
  - gpioint: bool
  - wake_capable: bool
  - pin_config: int
  - polarity: int
  - triggering: int
  - debounce: unsigned int
  - quirks: unsigned int
  - params: acpi_gpio_params
  - info: acpi_gpio_info *
  - desc: gpio_desc *
  - n: int

### acpi_gpio_info
- Line: 83
- Members:
  - node: list_head
  - handle: acpi_handle
  - handler: irq_handler_t
  - pin: unsigned int
  - irq: unsigned int
  - irqflags: unsigned long
  - irq_is_wake: bool
  - irq_requested: bool
  - desc: gpio_desc *
  - node: list_head
  - pin: unsigned int
  - desc: gpio_desc *
  - conn_info: acpi_connection_info
  - conns: list_head
  - conn_lock: mutex
  - chip: gpio_chip *
  - events: list_head
  - deferred_req_irqs_list_entry: list_head
  - adev: acpi_device *
  - flags: gpiod_flags
  - gpioint: bool
  - wake_capable: bool
  - pin_config: int
  - polarity: int
  - triggering: int
  - debounce: unsigned int
  - quirks: unsigned int
  - params: acpi_gpio_params
  - info: acpi_gpio_info *
  - desc: gpio_desc *
  - n: int

### acpi_gpio_lookup
- Line: 679
- Members:
  - node: list_head
  - handle: acpi_handle
  - handler: irq_handler_t
  - pin: unsigned int
  - irq: unsigned int
  - irqflags: unsigned long
  - irq_is_wake: bool
  - irq_requested: bool
  - desc: gpio_desc *
  - node: list_head
  - pin: unsigned int
  - desc: gpio_desc *
  - conn_info: acpi_connection_info
  - conns: list_head
  - conn_lock: mutex
  - chip: gpio_chip *
  - events: list_head
  - deferred_req_irqs_list_entry: list_head
  - adev: acpi_device *
  - flags: gpiod_flags
  - gpioint: bool
  - wake_capable: bool
  - pin_config: int
  - polarity: int
  - triggering: int
  - debounce: unsigned int
  - quirks: unsigned int
  - params: acpi_gpio_params
  - info: acpi_gpio_info *
  - desc: gpio_desc *
  - n: int
