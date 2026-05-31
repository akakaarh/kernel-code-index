# drivers/gpio/gpio-aggregator.c

Subsystem: drivers/gpio

## Functions (71)

### devm_gpiochip_fwd_alloc
- Return type: gpiochip_fwd *
- Signature: devm_gpiochip_fwd_alloc(struct device * dev,unsigned int ngpios)
- Line: 693
- Called by: gpiochip_fwd_create

### gpio_aggregator_activate
- Return type: static int
- Signature: gpio_aggregator_activate(struct gpio_aggregator * aggr)
- Line: 906
- Calls: gpio_aggregator_add_gpio, gpio_aggregator_count_lines, gpio_aggregator_make_device_sw_node, gpiod_add_lookup_table, gpiod_remove_lookup_table
- Called by: gpio_aggregator_device_live_store

### gpio_aggregator_add_gpio
- Return type: static int
- Signature: gpio_aggregator_add_gpio(struct gpio_aggregator * aggr,const char * key,int hwnum,unsigned int * n)
- Line: 113
- Called by: gpio_aggregator_activate, gpio_aggregator_parse

### gpio_aggregator_alloc
- Return type: static int
- Signature: gpio_aggregator_alloc(struct gpio_aggregator ** aggr,size_t arg_size)
- Line: 82
- Called by: gpio_aggregator_make_group, gpio_aggregator_new_device_store

### gpio_aggregator_count_lines
- Return type: static size_t
- Signature: gpio_aggregator_count_lines(struct gpio_aggregator * aggr)
- Line: 147
- Called by: gpio_aggregator_activate, gpio_aggregator_make_device_sw_node

### gpio_aggregator_deactivate
- Return type: static void
- Signature: gpio_aggregator_deactivate(struct gpio_aggregator * aggr)
- Line: 995
- Calls: gpiod_remove_lookup_table
- Called by: gpio_aggregator_destroy, gpio_aggregator_device_live_store

### gpio_aggregator_delete_device_store
- Return type: static ssize_t
- Signature: gpio_aggregator_delete_device_store(struct device_driver * driver,const char * buf,size_t count)
- Line: 1543
- Calls: gpio_aggregator_destroy

### gpio_aggregator_destroy
- Return type: static void
- Signature: gpio_aggregator_destroy(struct gpio_aggregator * aggr)
- Line: 1531
- Calls: gpio_aggregator_deactivate, gpio_aggregator_free_lines, gpio_aggregator_is_activating, gpio_aggregator_is_active
- Called by: gpio_aggregator_delete_device_store, gpio_aggregator_idr_remove

### gpio_aggregator_device_dev_name_show
- Return type: static ssize_t
- Signature: gpio_aggregator_device_dev_name_show(struct config_item * item,char * page)
- Line: 1159
- Calls: to_gpio_aggregator

### gpio_aggregator_device_live_show
- Return type: static ssize_t
- Signature: gpio_aggregator_device_live_show(struct config_item * item,char * page)
- Line: 1175
- Calls: gpio_aggregator_is_active, to_gpio_aggregator

### gpio_aggregator_device_live_store
- Return type: static ssize_t
- Signature: gpio_aggregator_device_live_store(struct config_item * item,const char * page,size_t count)
- Line: 1186
- Calls: gpio_aggregator_activate, gpio_aggregator_deactivate, gpio_aggregator_is_activating, gpio_aggregator_is_active, gpio_aggregator_lockup_configfs, to_gpio_aggregator

### gpio_aggregator_device_make_group
- Return type: static config_group *
- Signature: gpio_aggregator_device_make_group(struct config_group * group,const char * name)
- Line: 1272
- Calls: gpio_aggregator_is_active, gpio_aggregator_line_add, gpio_aggregator_line_alloc, to_gpio_aggregator

### gpio_aggregator_device_release
- Return type: static void
- Signature: gpio_aggregator_device_release(struct config_item * item)
- Line: 1256
- Calls: gpio_aggregator_free, to_gpio_aggregator

### gpio_aggregator_exit
- Return type: static void __exit
- Signature: gpio_aggregator_exit(void)
- Line: 1728
- Calls: gpio_aggregator_remove_all

### gpio_aggregator_free
- Return type: static void
- Signature: gpio_aggregator_free(struct gpio_aggregator * aggr)
- Line: 104
- Called by: gpio_aggregator_device_release, gpio_aggregator_new_device_store

### gpio_aggregator_free_lines
- Return type: static void
- Signature: gpio_aggregator_free_lines(struct gpio_aggregator * aggr)
- Line: 205
- Calls: gpio_aggregator_line_del
- Called by: gpio_aggregator_destroy, gpio_aggregator_parse

### gpio_aggregator_idr_remove
- Return type: static int __exit
- Signature: gpio_aggregator_idr_remove(int id,void * p,void * data)
- Line: 1668
- Calls: gpio_aggregator_destroy

### gpio_aggregator_init
- Return type: static int __init
- Signature: gpio_aggregator_init(void)
- Line: 1696

### gpio_aggregator_is_activating
- Return type: static bool
- Signature: gpio_aggregator_is_activating(struct gpio_aggregator * aggr)
- Line: 140
- Called by: gpio_aggregator_destroy, gpio_aggregator_device_live_store, gpio_aggregator_line_key_store, gpio_aggregator_line_name_store, gpio_aggregator_line_offset_store

### gpio_aggregator_is_active
- Return type: static bool
- Signature: gpio_aggregator_is_active(struct gpio_aggregator * aggr)
- Line: 132
- Called by: gpio_aggregator_destroy, gpio_aggregator_device_live_show, gpio_aggregator_device_live_store, gpio_aggregator_device_make_group, gpio_aggregator_line_key_store, gpio_aggregator_line_name_store, gpio_aggregator_line_offset_store

### gpio_aggregator_line_add
- Return type: static void
- Signature: gpio_aggregator_line_add(struct gpio_aggregator * aggr,struct gpio_aggregator_line * line)
- Line: 181
- Called by: gpio_aggregator_device_make_group, gpio_aggregator_parse

### gpio_aggregator_line_alloc
- Return type: static gpio_aggregator_line *
- Signature: gpio_aggregator_line_alloc(struct gpio_aggregator * parent,unsigned int idx,char * key,int offset)
- Line: 155
- Called by: gpio_aggregator_device_make_group, gpio_aggregator_parse

### gpio_aggregator_line_del
- Return type: static void
- Signature: gpio_aggregator_line_del(struct gpio_aggregator * aggr,struct gpio_aggregator_line * line)
- Line: 197
- Called by: gpio_aggregator_free_lines, gpio_aggregator_line_release

### gpio_aggregator_line_key_show
- Return type: static ssize_t
- Signature: gpio_aggregator_line_key_show(struct config_item * item,char * page)
- Line: 1030
- Calls: to_gpio_aggregator_line

### gpio_aggregator_line_key_store
- Return type: static ssize_t
- Signature: gpio_aggregator_line_key_store(struct config_item * item,const char * page,size_t count)
- Line: 1041
- Calls: gpio_aggregator_is_activating, gpio_aggregator_is_active, to_gpio_aggregator_line

### gpio_aggregator_line_name_show
- Return type: static ssize_t
- Signature: gpio_aggregator_line_name_show(struct config_item * item,char * page)
- Line: 1068
- Calls: to_gpio_aggregator_line

### gpio_aggregator_line_name_store
- Return type: static ssize_t
- Signature: gpio_aggregator_line_name_store(struct config_item * item,const char * page,size_t count)
- Line: 1079
- Calls: gpio_aggregator_is_activating, gpio_aggregator_is_active, to_gpio_aggregator_line

### gpio_aggregator_line_offset_show
- Return type: static ssize_t
- Signature: gpio_aggregator_line_offset_show(struct config_item * item,char * page)
- Line: 1106
- Calls: to_gpio_aggregator_line

### gpio_aggregator_line_offset_store
- Return type: static ssize_t
- Signature: gpio_aggregator_line_offset_store(struct config_item * item,const char * page,size_t count)
- Line: 1117
- Calls: gpio_aggregator_is_activating, gpio_aggregator_is_active, to_gpio_aggregator_line

### gpio_aggregator_line_release
- Return type: static void
- Signature: gpio_aggregator_line_release(struct config_item * item)
- Line: 1233
- Calls: gpio_aggregator_line_del, to_gpio_aggregator_line

### gpio_aggregator_lockup_configfs
- Return type: static void
- Signature: gpio_aggregator_lockup_configfs(struct gpio_aggregator * aggr,bool lock)
- Line: 1008
- Called by: gpio_aggregator_device_live_store

### gpio_aggregator_make_device_sw_node
- Return type: static fwnode_handle *
- Signature: gpio_aggregator_make_device_sw_node(struct gpio_aggregator * aggr)
- Line: 877
- Calls: gpio_aggregator_count_lines
- Called by: gpio_aggregator_activate

### gpio_aggregator_make_group
- Return type: static config_group *
- Signature: gpio_aggregator_make_group(struct config_group * group,const char * name)
- Line: 1324
- Calls: gpio_aggregator_alloc

### gpio_aggregator_new_device_store
- Return type: static ssize_t
- Signature: gpio_aggregator_new_device_store(struct device_driver * driver,const char * buf,size_t count)
- Line: 1456
- Calls: gpio_aggregator_alloc, gpio_aggregator_free, gpio_aggregator_parse, gpiod_add_lookup_table, gpiod_remove_lookup_table

### gpio_aggregator_parse
- Return type: static int
- Signature: gpio_aggregator_parse(struct gpio_aggregator * aggr)
- Line: 1368
- Calls: gpio_aggregator_add_gpio, gpio_aggregator_free_lines, gpio_aggregator_line_add, gpio_aggregator_line_alloc
- Called by: gpio_aggregator_new_device_store

### gpio_aggregator_probe
- Return type: static int
- Signature: gpio_aggregator_probe(struct platform_device * pdev)
- Line: 1594
- Calls: devm_gpiod_get_index, gpiochip_fwd_create, gpiod_count

### gpio_aggregator_remove_all
- Return type: static void __exit
- Signature: gpio_aggregator_remove_all(void)
- Line: 1678
- Called by: gpio_aggregator_exit

### gpio_fwd_delay
- Return type: static void
- Signature: gpio_fwd_delay(struct gpio_chip * chip,unsigned int offset,int value)
- Line: 347
- Calls: gpiochip_get_data, gpiod_is_active_low
- Called by: gpio_fwd_set

### gpio_fwd_direction_input
- Return type: static int
- Signature: gpio_fwd_direction_input(struct gpio_chip * chip,unsigned int offset)
- Line: 278
- Calls: gpiochip_get_data, gpiod_direction_input
- Called by: gpiochip_fwd_gpio_direction_input

### gpio_fwd_direction_output
- Return type: static int
- Signature: gpio_fwd_direction_output(struct gpio_chip * chip,unsigned int offset,int value)
- Line: 285
- Calls: gpiochip_get_data, gpiod_direction_output
- Called by: gpiochip_fwd_gpio_direction_output

### gpio_fwd_get
- Return type: static int
- Signature: gpio_fwd_get(struct gpio_chip * chip,unsigned int offset)
- Line: 293
- Calls: gpiochip_get_data, gpiod_get_value, gpiod_get_value_cansleep
- Called by: gpiochip_fwd_gpio_get

### gpio_fwd_get_direction
- Return type: static int
- Signature: gpio_fwd_get_direction(struct gpio_chip * chip,unsigned int offset)
- Line: 264
- Calls: gpiochip_get_data, gpiod_get_direction
- Called by: gpiochip_fwd_gpio_get_direction

### gpio_fwd_get_multiple
- Return type: static int
- Signature: gpio_fwd_get_multiple(struct gpiochip_fwd * fwd,unsigned long * mask,unsigned long * bits)
- Line: 301
- Calls: gpiod_get_array_value, gpiod_get_array_value_cansleep
- Called by: gpio_fwd_get_multiple_locked

### gpio_fwd_get_multiple_locked
- Return type: static int
- Signature: gpio_fwd_get_multiple_locked(struct gpio_chip * chip,unsigned long * mask,unsigned long * bits)
- Line: 327
- Calls: gpio_fwd_get_multiple, gpiochip_get_data
- Called by: gpiochip_fwd_gpio_get_multiple

### gpio_fwd_request
- Return type: static int
- Signature: gpio_fwd_request(struct gpio_chip * chip,unsigned int offset)
- Line: 257
- Calls: gpiochip_get_data
- Called by: gpiochip_fwd_gpio_request

### gpio_fwd_set
- Return type: static int
- Signature: gpio_fwd_set(struct gpio_chip * chip,unsigned int offset,int value)
- Line: 368
- Calls: gpio_fwd_delay, gpiochip_get_data, gpiod_set_value, gpiod_set_value_cansleep
- Called by: gpiochip_fwd_gpio_set

### gpio_fwd_set_config
- Return type: static int
- Signature: gpio_fwd_set_config(struct gpio_chip * chip,unsigned int offset,unsigned long config)
- Line: 426
- Calls: gpiochip_get_data, gpiod_set_config
- Called by: gpiochip_fwd_gpio_set_config

### gpio_fwd_set_multiple
- Return type: static int
- Signature: gpio_fwd_set_multiple(struct gpiochip_fwd * fwd,unsigned long * mask,unsigned long * bits)
- Line: 386
- Calls: gpiod_set_array_value, gpiod_set_array_value_cansleep
- Called by: gpio_fwd_set_multiple_locked

### gpio_fwd_set_multiple_locked
- Return type: static int
- Signature: gpio_fwd_set_multiple_locked(struct gpio_chip * chip,unsigned long * mask,unsigned long * bits)
- Line: 406
- Calls: gpio_fwd_set_multiple, gpiochip_get_data
- Called by: gpiochip_fwd_gpio_set_multiple

### gpio_fwd_to_irq
- Return type: static int
- Signature: gpio_fwd_to_irq(struct gpio_chip * chip,unsigned int offset)
- Line: 434
- Calls: gpiochip_get_data, gpiod_to_irq
- Called by: gpiochip_fwd_gpio_to_irq

### gpiochip_fwd_create
- Return type: static gpiochip_fwd *
- Signature: gpiochip_fwd_create(struct device * dev,unsigned int ngpios,struct gpio_desc * descs[],unsigned long features)
- Line: 824
- Calls: devm_gpiochip_fwd_alloc, gpiochip_fwd_desc_add, gpiochip_fwd_register, gpiochip_fwd_setup_delay_line
- Called by: gpio_aggregator_probe

### gpiochip_fwd_delay_of_xlate
- Return type: static int
- Signature: gpiochip_fwd_delay_of_xlate(struct gpio_chip * chip,const struct of_phandle_args * gpiospec,u32 * flags)
- Line: 450
- Calls: gpiochip_get_data

### gpiochip_fwd_desc_add
- Return type: int
- Signature: gpiochip_fwd_desc_add(struct gpiochip_fwd * fwd,struct gpio_desc * desc,unsigned int offset)
- Line: 741
- Calls: desc_to_gpio, gpiod_cansleep, gpiod_to_irq
- Called by: gpiochip_fwd_create

### gpiochip_fwd_desc_free
- Return type: void
- Signature: gpiochip_fwd_desc_free(struct gpiochip_fwd * fwd,unsigned int offset)
- Line: 773
- Calls: gpiod_put

### gpiochip_fwd_get_data
- Return type: void *
- Signature: gpiochip_fwd_get_data(struct gpiochip_fwd * fwd)
- Line: 512

### gpiochip_fwd_get_gpiochip
- Return type: gpio_chip *
- Signature: gpiochip_fwd_get_gpiochip(struct gpiochip_fwd * fwd)
- Line: 500
- Called by: gpiochip_fwd_gpio_direction_input, gpiochip_fwd_gpio_direction_output, gpiochip_fwd_gpio_get, gpiochip_fwd_gpio_get_direction, gpiochip_fwd_gpio_get_multiple, gpiochip_fwd_gpio_request, gpiochip_fwd_gpio_set, gpiochip_fwd_gpio_set_config, gpiochip_fwd_gpio_set_multiple, gpiochip_fwd_gpio_to_irq

### gpiochip_fwd_gpio_direction_input
- Return type: int
- Signature: gpiochip_fwd_gpio_direction_input(struct gpiochip_fwd * fwd,unsigned int offset)
- Line: 573
- Calls: gpio_fwd_direction_input, gpiochip_fwd_get_gpiochip

### gpiochip_fwd_gpio_direction_output
- Return type: int
- Signature: gpiochip_fwd_gpio_direction_output(struct gpiochip_fwd * fwd,unsigned int offset,int value)
- Line: 557
- Calls: gpio_fwd_direction_output, gpiochip_fwd_get_gpiochip

### gpiochip_fwd_gpio_get
- Return type: int
- Signature: gpiochip_fwd_gpio_get(struct gpiochip_fwd * fwd,unsigned int offset)
- Line: 589
- Calls: gpio_fwd_get, gpiochip_fwd_get_gpiochip

### gpiochip_fwd_gpio_get_direction
- Return type: int
- Signature: gpiochip_fwd_gpio_get_direction(struct gpiochip_fwd * fwd,unsigned int offset)
- Line: 540
- Calls: gpio_fwd_get_direction, gpiochip_fwd_get_gpiochip

### gpiochip_fwd_gpio_get_multiple
- Return type: int
- Signature: gpiochip_fwd_gpio_get_multiple(struct gpiochip_fwd * fwd,unsigned long * mask,unsigned long * bits)
- Line: 607
- Calls: gpio_fwd_get_multiple_locked, gpiochip_fwd_get_gpiochip

### gpiochip_fwd_gpio_request
- Return type: int
- Signature: gpiochip_fwd_gpio_request(struct gpiochip_fwd * fwd,unsigned int offset)
- Line: 525
- Calls: gpio_fwd_request, gpiochip_fwd_get_gpiochip

### gpiochip_fwd_gpio_set
- Return type: int
- Signature: gpiochip_fwd_gpio_set(struct gpiochip_fwd * fwd,unsigned int offset,int value)
- Line: 624
- Calls: gpio_fwd_set, gpiochip_fwd_get_gpiochip

### gpiochip_fwd_gpio_set_config
- Return type: int
- Signature: gpiochip_fwd_gpio_set_config(struct gpiochip_fwd * fwd,unsigned int offset,unsigned long config)
- Line: 660
- Calls: gpio_fwd_set_config, gpiochip_fwd_get_gpiochip

### gpiochip_fwd_gpio_set_multiple
- Return type: int
- Signature: gpiochip_fwd_gpio_set_multiple(struct gpiochip_fwd * fwd,unsigned long * mask,unsigned long * bits)
- Line: 642
- Calls: gpio_fwd_set_multiple_locked, gpiochip_fwd_get_gpiochip

### gpiochip_fwd_gpio_to_irq
- Return type: int
- Signature: gpiochip_fwd_gpio_to_irq(struct gpiochip_fwd * fwd,unsigned int offset)
- Line: 677
- Calls: gpio_fwd_to_irq, gpiochip_fwd_get_gpiochip

### gpiochip_fwd_register
- Return type: int
- Signature: gpiochip_fwd_register(struct gpiochip_fwd * fwd,void * data)
- Line: 787
- Called by: gpiochip_fwd_create

### gpiochip_fwd_setup_delay_line
- Return type: static int
- Signature: gpiochip_fwd_setup_delay_line(struct gpiochip_fwd * fwd)
- Line: 472
- Called by: gpiochip_fwd_create

### gpiochip_fwd_setup_delay_line
- Return type: static int
- Signature: gpiochip_fwd_setup_delay_line(struct gpiochip_fwd * fwd)
- Line: 488
- Called by: gpiochip_fwd_create

### to_gpio_aggregator
- Return type: static gpio_aggregator *
- Signature: to_gpio_aggregator(struct config_item * item)
- Line: 861
- Called by: gpio_aggregator_device_dev_name_show, gpio_aggregator_device_live_show, gpio_aggregator_device_live_store, gpio_aggregator_device_make_group, gpio_aggregator_device_release

### to_gpio_aggregator_line
- Return type: static gpio_aggregator_line *
- Signature: to_gpio_aggregator_line(struct config_item * item)
- Line: 869
- Called by: gpio_aggregator_line_key_show, gpio_aggregator_line_key_store, gpio_aggregator_line_name_show, gpio_aggregator_line_name_store, gpio_aggregator_line_offset_show, gpio_aggregator_line_offset_store, gpio_aggregator_line_release

## Structs (5)

### gpio_aggregator
- Line: 42
- Members:
  - pdev: platform_device *
  - group: config_group
  - lookups: gpiod_lookup_table *
  - lock: mutex
  - id: int
  - list_head: list_head
  - init_via_sysfs: bool
  - args: char[]
  - group: config_group
  - parent: gpio_aggregator *
  - entry: list_head
  - idx: unsigned int
  - name: const char *
  - key: const char *
  - offset: int
  - flags: gpio_lookup_flags
  - init_via_sysfs: bool
  - ramp_up_us: u32
  - ramp_down_us: u32
  - chip: gpio_chip
  - descs: gpio_desc **
  - mlock: mutex
  - slock: spinlock_t
  - delay_timings: gpiochip_fwd_timing *
  - data: void *
  - valid_mask: unsigned long *
  - tmp: unsigned long[]

### gpio_aggregator_line
- Line: 57
- Members:
  - pdev: platform_device *
  - group: config_group
  - lookups: gpiod_lookup_table *
  - lock: mutex
  - id: int
  - list_head: list_head
  - init_via_sysfs: bool
  - args: char[]
  - group: config_group
  - parent: gpio_aggregator *
  - entry: list_head
  - idx: unsigned int
  - name: const char *
  - key: const char *
  - offset: int
  - flags: gpio_lookup_flags
  - init_via_sysfs: bool
  - ramp_up_us: u32
  - ramp_down_us: u32
  - chip: gpio_chip
  - descs: gpio_desc **
  - mlock: mutex
  - slock: spinlock_t
  - delay_timings: gpiochip_fwd_timing *
  - data: void *
  - valid_mask: unsigned long *
  - tmp: unsigned long[]

### gpio_aggregator_pdev_meta
- Line: 75
- Members:
  - pdev: platform_device *
  - group: config_group
  - lookups: gpiod_lookup_table *
  - lock: mutex
  - id: int
  - list_head: list_head
  - init_via_sysfs: bool
  - args: char[]
  - group: config_group
  - parent: gpio_aggregator *
  - entry: list_head
  - idx: unsigned int
  - name: const char *
  - key: const char *
  - offset: int
  - flags: gpio_lookup_flags
  - init_via_sysfs: bool
  - ramp_up_us: u32
  - ramp_down_us: u32
  - chip: gpio_chip
  - descs: gpio_desc **
  - mlock: mutex
  - slock: spinlock_t
  - delay_timings: gpiochip_fwd_timing *
  - data: void *
  - valid_mask: unsigned long *
  - tmp: unsigned long[]

### gpiochip_fwd
- Line: 239
- Members:
  - pdev: platform_device *
  - group: config_group
  - lookups: gpiod_lookup_table *
  - lock: mutex
  - id: int
  - list_head: list_head
  - init_via_sysfs: bool
  - args: char[]
  - group: config_group
  - parent: gpio_aggregator *
  - entry: list_head
  - idx: unsigned int
  - name: const char *
  - key: const char *
  - offset: int
  - flags: gpio_lookup_flags
  - init_via_sysfs: bool
  - ramp_up_us: u32
  - ramp_down_us: u32
  - chip: gpio_chip
  - descs: gpio_desc **
  - mlock: mutex
  - slock: spinlock_t
  - delay_timings: gpiochip_fwd_timing *
  - data: void *
  - valid_mask: unsigned long *
  - tmp: unsigned long[]

### gpiochip_fwd_timing
- Line: 234
- Members:
  - pdev: platform_device *
  - group: config_group
  - lookups: gpiod_lookup_table *
  - lock: mutex
  - id: int
  - list_head: list_head
  - init_via_sysfs: bool
  - args: char[]
  - group: config_group
  - parent: gpio_aggregator *
  - entry: list_head
  - idx: unsigned int
  - name: const char *
  - key: const char *
  - offset: int
  - flags: gpio_lookup_flags
  - init_via_sysfs: bool
  - ramp_up_us: u32
  - ramp_down_us: u32
  - chip: gpio_chip
  - descs: gpio_desc **
  - mlock: mutex
  - slock: spinlock_t
  - delay_timings: gpiochip_fwd_timing *
  - data: void *
  - valid_mask: unsigned long *
  - tmp: unsigned long[]

## Unions (1)

### __anon0a3cdc2b010a
- Line: 242
- Members:
  - pdev: platform_device *
  - group: config_group
  - lookups: gpiod_lookup_table *
  - lock: mutex
  - id: int
  - list_head: list_head
  - init_via_sysfs: bool
  - args: char[]
  - group: config_group
  - parent: gpio_aggregator *
  - entry: list_head
  - idx: unsigned int
  - name: const char *
  - key: const char *
  - offset: int
  - flags: gpio_lookup_flags
  - init_via_sysfs: bool
  - ramp_up_us: u32
  - ramp_down_us: u32
  - chip: gpio_chip
  - descs: gpio_desc **
  - mlock: mutex
  - slock: spinlock_t
  - delay_timings: gpiochip_fwd_timing *
  - data: void *
  - valid_mask: unsigned long *
  - tmp: unsigned long[]

## Variables (15)

- static **driver_attr_gpio_aggregator_delete_device** : driver_attribute (line 1580)
- static **driver_attr_gpio_aggregator_new_device** : driver_attribute (line 1528)
- static **gpio_aggregator_attrs** : attribute * [] (line 1583)
- static **gpio_aggregator_device_attrs** : configfs_attribute * [] (line 1226)
- static **gpio_aggregator_device_group_ops** : const struct configfs_group_operations (line 1312)
- static **gpio_aggregator_device_item_ops** : const struct configfs_item_operations (line 1267)
- static **gpio_aggregator_device_type** : const struct config_item_type (line 1316)
- static **gpio_aggregator_driver** : platform_driver (line 1659)
- static **gpio_aggregator_dt_ids** : const struct of_device_id[] (line 1646)
- static **gpio_aggregator_group_ops** : const struct configfs_group_operations (line 1347)
- static **gpio_aggregator_line_attrs** : configfs_attribute * [] (line 1151)
- static **gpio_aggregator_line_item_ops** : const struct configfs_item_operations (line 1246)
- static **gpio_aggregator_line_type** : const struct config_item_type (line 1250)
- static **gpio_aggregator_subsys** : configfs_subsystem (line 1356)
- static **gpio_aggregator_type** : const struct config_item_type (line 1351)

## Macros (8)

- **AGGREGATOR_LEGACY_PREFIX** (line 36)
- **AGGREGATOR_MAX_GPIOS** (line 35)
- **DRV_NAME** (line 7)
- **FWD_FEATURE_DELAY** (line 447)
- **fwd_tmp_descs**(fwd) (line 253)
- **fwd_tmp_size**(ngpios) (line 255)
- **fwd_tmp_values**(fwd) (line 252)
- **pr_fmt**(fmt) (line 8)
