# drivers/gpio/gpio-virtuser.c

Subsystem: drivers/gpio

## Functions (82)

### gpio_virtuser_config_make_device_group
- Return type: static config_group *
- Signature: gpio_virtuser_config_make_device_group(struct config_group * group,const char * name)
- Line: 1725

### gpio_virtuser_consumer_read
- Return type: static ssize_t
- Signature: gpio_virtuser_consumer_read(struct file * file,char __user * user_buf,size_t size,loff_t * ppos)
- Line: 601

### gpio_virtuser_consumer_write
- Return type: static ssize_t
- Signature: gpio_virtuser_consumer_write(struct file * file,const char __user * user_buf,size_t count,loff_t * ppos)
- Line: 617
- Calls: gpiod_set_consumer_name

### gpio_virtuser_count_ids
- Return type: static int
- Signature: gpio_virtuser_count_ids(struct device * dev)
- Line: 853
- Calls: gpio_virtuser_prop_is_gpio
- Called by: gpio_virtuser_probe

### gpio_virtuser_create_debugfs_attrs
- Return type: static int
- Signature: gpio_virtuser_create_debugfs_attrs(const struct gpio_virtuser_dbgfs_attr_descr * attr,size_t num_attrs,struct dentry * parent,void * data)
- Line: 751
- Called by: gpio_virtuser_dbgfs_init_line_array_attrs, gpio_virtuser_dbgfs_init_line_attrs

### gpio_virtuser_dbgfs_emit_value_array
- Return type: static void
- Signature: gpio_virtuser_dbgfs_emit_value_array(char * buf,unsigned long * values,size_t num_values)
- Line: 107
- Called by: gpio_virtuser_value_array_do_read

### gpio_virtuser_dbgfs_init_line_array_attrs
- Return type: static int
- Signature: gpio_virtuser_dbgfs_init_line_array_attrs(struct device * dev,struct gpio_descs * descs,const char * id,struct dentry * dbgfs_entry)
- Line: 768
- Calls: gpio_virtuser_create_debugfs_attrs
- Called by: gpio_virtuser_probe

### gpio_virtuser_dbgfs_init_line_attrs
- Return type: static int
- Signature: gpio_virtuser_dbgfs_init_line_attrs(struct device * dev,struct gpio_desc * desc,const char * id,unsigned int index,struct dentry * dbgfs_entry)
- Line: 796
- Calls: gpio_virtuser_create_debugfs_attrs
- Called by: gpio_virtuser_probe

### gpio_virtuser_dbgfs_parse_value_array
- Return type: static int
- Signature: gpio_virtuser_dbgfs_parse_value_array(const char * buf,size_t len,unsigned long * values)
- Line: 181
- Called by: gpio_virtuser_value_array_do_write

### gpio_virtuser_debounce_get
- Return type: static int
- Signature: gpio_virtuser_debounce_get(void * data,u64 * val)
- Line: 569

### gpio_virtuser_debounce_set
- Return type: static int
- Signature: gpio_virtuser_debounce_set(void * data,u64 val)
- Line: 578
- Calls: gpiod_set_debounce

### gpio_virtuser_debugfs_remove
- Return type: static void
- Signature: gpio_virtuser_debugfs_remove(void * data)
- Line: 833

### gpio_virtuser_device_activate
- Return type: static int
- Signature: gpio_virtuser_device_activate(struct gpio_virtuser_device * dev)
- Line: 1448
- Calls: gpio_virtuser_make_device_swnode, gpio_virtuser_make_lookup_table, gpio_virtuser_remove_lookup_table
- Called by: gpio_virtuser_device_config_live_store

### gpio_virtuser_device_config_dev_name_show
- Return type: static ssize_t
- Signature: gpio_virtuser_device_config_dev_name_show(struct config_item * item,char * page)
- Line: 1335
- Calls: to_gpio_virtuser_device

### gpio_virtuser_device_config_group_release
- Return type: static void
- Signature: gpio_virtuser_device_config_group_release(struct config_item * item)
- Line: 1695
- Calls: gpio_virtuser_device_deactivate, gpio_virtuser_device_is_live, to_gpio_virtuser_device

### gpio_virtuser_device_config_live_show
- Return type: static ssize_t
- Signature: gpio_virtuser_device_config_live_show(struct config_item * item,char * page)
- Line: 1352
- Calls: gpio_virtuser_device_is_live, to_gpio_virtuser_device

### gpio_virtuser_device_config_live_store
- Return type: static ssize_t
- Signature: gpio_virtuser_device_config_live_store(struct config_item * item,const char * page,size_t count)
- Line: 1540
- Calls: gpio_virtuser_device_activate, gpio_virtuser_device_deactivate, gpio_virtuser_device_is_live, gpio_virtuser_device_lockup_configfs, to_gpio_virtuser_device

### gpio_virtuser_device_deactivate
- Return type: static void
- Signature: gpio_virtuser_device_deactivate(struct gpio_virtuser_device * dev)
- Line: 1502
- Calls: gpio_virtuser_remove_lookup_table
- Called by: gpio_virtuser_device_config_group_release, gpio_virtuser_device_config_live_store

### gpio_virtuser_device_is_live
- Return type: static bool
- Signature: gpio_virtuser_device_is_live(struct gpio_virtuser_device * dev)
- Line: 999
- Called by: gpio_virtuser_device_config_group_release, gpio_virtuser_device_config_live_show, gpio_virtuser_device_config_live_store, gpio_virtuser_lookup_entry_config_active_low_store, gpio_virtuser_lookup_entry_config_drive_store, gpio_virtuser_lookup_entry_config_key_store, gpio_virtuser_lookup_entry_config_offset_store, gpio_virtuser_lookup_entry_config_pull_store, gpio_virtuser_lookup_entry_config_transitory_store, gpio_virtuser_make_lookup_entry_group, gpio_virtuser_make_lookup_group

### gpio_virtuser_device_lockup_configfs
- Return type: static void
- Signature: gpio_virtuser_device_lockup_configfs(struct gpio_virtuser_device * dev,bool lock)
- Line: 1516
- Called by: gpio_virtuser_device_config_live_store

### gpio_virtuser_direction_atomic_read
- Return type: static ssize_t
- Signature: gpio_virtuser_direction_atomic_read(struct file * file,char __user * user_buf,size_t size,loff_t * ppos)
- Line: 456
- Calls: gpio_virtuser_direction_do_read

### gpio_virtuser_direction_atomic_write
- Return type: static ssize_t
- Signature: gpio_virtuser_direction_atomic_write(struct file * file,const char __user * user_buf,size_t count,loff_t * ppos)
- Line: 464
- Calls: gpio_virtuser_direction_do_write

### gpio_virtuser_direction_do_read
- Return type: static ssize_t
- Signature: gpio_virtuser_direction_do_read(struct file * file,char __user * user_buf,size_t size,loff_t * ppos,bool atomic)
- Line: 335
- Calls: gpio_virtuser_get_direction_atomic, gpiod_get_direction
- Called by: gpio_virtuser_direction_atomic_read, gpio_virtuser_direction_read

### gpio_virtuser_direction_do_write
- Return type: static ssize_t
- Signature: gpio_virtuser_direction_do_write(struct file * file,const char __user * user_buf,size_t count,loff_t * ppos,bool atomic)
- Line: 390
- Calls: gpio_virtuser_set_direction, gpio_virtuser_set_direction_atomic
- Called by: gpio_virtuser_direction_atomic_write, gpio_virtuser_direction_write

### gpio_virtuser_direction_read
- Return type: static ssize_t
- Signature: gpio_virtuser_direction_read(struct file * file,char __user * user_buf,size_t size,loff_t * ppos)
- Line: 432
- Calls: gpio_virtuser_direction_do_read

### gpio_virtuser_direction_write
- Return type: static ssize_t
- Signature: gpio_virtuser_direction_write(struct file * file,const char __user * user_buf,size_t count,loff_t * ppos)
- Line: 440
- Calls: gpio_virtuser_direction_do_write

### gpio_virtuser_do_get_direction_atomic
- Return type: static void
- Signature: gpio_virtuser_do_get_direction_atomic(struct irq_work * work)
- Line: 313
- Calls: gpiod_get_direction, to_gpio_virtuser_irq_work_context

### gpio_virtuser_do_set_direction_atomic
- Return type: static void
- Signature: gpio_virtuser_do_set_direction_atomic(struct irq_work * work)
- Line: 365
- Calls: gpio_virtuser_set_direction, to_gpio_virtuser_irq_work_context

### gpio_virtuser_exit
- Return type: static void __exit
- Signature: gpio_virtuser_exit(void)
- Line: 1801

### gpio_virtuser_get_array_value
- Return type: static int
- Signature: gpio_virtuser_get_array_value(struct gpio_descs * descs,unsigned long * values,bool atomic)
- Line: 130
- Calls: gpio_virtuser_init_irq_work_context, gpio_virtuser_irq_work_queue_sync, gpiod_get_array_value_cansleep
- Called by: gpio_virtuser_value_array_do_read

### gpio_virtuser_get_direction_atomic
- Return type: static int
- Signature: gpio_virtuser_get_direction_atomic(struct gpio_desc * desc)
- Line: 322
- Calls: gpio_virtuser_init_irq_work_context, gpio_virtuser_irq_work_queue_sync
- Called by: gpio_virtuser_direction_do_read

### gpio_virtuser_get_ids
- Return type: static int
- Signature: gpio_virtuser_get_ids(struct device * dev,const char ** ids,int num_ids)
- Line: 871
- Calls: gpio_virtuser_prop_is_gpio
- Called by: gpio_virtuser_probe

### gpio_virtuser_get_lookup_count
- Return type: static size_t
- Signature: gpio_virtuser_get_lookup_count(struct gpio_virtuser_device * dev)
- Line: 1365
- Called by: gpio_virtuser_make_lookup_table

### gpio_virtuser_get_value_array_atomic
- Return type: static void
- Signature: gpio_virtuser_get_value_array_atomic(struct irq_work * work)
- Line: 119
- Calls: gpiod_get_array_value, to_gpio_virtuser_irq_work_context

### gpio_virtuser_get_value_atomic
- Return type: static void
- Signature: gpio_virtuser_get_value_atomic(struct irq_work * work)
- Line: 509
- Calls: gpiod_get_value, to_gpio_virtuser_irq_work_context

### gpio_virtuser_init
- Return type: static int __init
- Signature: gpio_virtuser_init(void)
- Line: 1762

### gpio_virtuser_init_irq_work_context
- Return type: static void
- Signature: gpio_virtuser_init_irq_work_context(struct gpio_virtuser_irq_work_context * ctx)
- Line: 94
- Called by: gpio_virtuser_get_array_value, gpio_virtuser_get_direction_atomic, gpio_virtuser_set_array_value, gpio_virtuser_set_direction_atomic, gpio_virtuser_value_atomic_get, gpio_virtuser_value_atomic_set

### gpio_virtuser_interrupts_get
- Return type: static int
- Signature: gpio_virtuser_interrupts_get(void * data,u64 * val)
- Line: 653

### gpio_virtuser_interrupts_set
- Return type: static int
- Signature: gpio_virtuser_interrupts_set(void * data,u64 val)
- Line: 671
- Calls: gpiod_to_irq

### gpio_virtuser_irq_handler
- Return type: static irqreturn_t
- Signature: gpio_virtuser_irq_handler(int irq,void * data)
- Line: 662

### gpio_virtuser_irq_work_queue_sync
- Return type: static void
- Signature: gpio_virtuser_irq_work_queue_sync(struct gpio_virtuser_irq_work_context * ctx)
- Line: 101
- Called by: gpio_virtuser_get_array_value, gpio_virtuser_get_direction_atomic, gpio_virtuser_set_array_value, gpio_virtuser_set_direction_atomic, gpio_virtuser_value_atomic_get, gpio_virtuser_value_atomic_set

### gpio_virtuser_lookup_config_group_release
- Return type: static void
- Signature: gpio_virtuser_lookup_config_group_release(struct config_item * item)
- Line: 1635
- Calls: to_gpio_virtuser_lookup

### gpio_virtuser_lookup_entry_config_active_low_show
- Return type: static ssize_t
- Signature: gpio_virtuser_lookup_entry_config_active_low_show(struct config_item * item,char * page)
- Line: 1247
- Calls: gpio_virtuser_lookup_get_flags

### gpio_virtuser_lookup_entry_config_active_low_store
- Return type: static ssize_t
- Signature: gpio_virtuser_lookup_entry_config_active_low_store(struct config_item * item,const char * page,size_t count)
- Line: 1256
- Calls: gpio_virtuser_device_is_live, to_gpio_virtuser_lookup_entry

### gpio_virtuser_lookup_entry_config_drive_show
- Return type: static ssize_t
- Signature: gpio_virtuser_lookup_entry_config_drive_show(struct config_item * item,char * page)
- Line: 1149
- Calls: gpio_virtuser_lookup_get_flags

### gpio_virtuser_lookup_entry_config_drive_store
- Return type: static ssize_t
- Signature: gpio_virtuser_lookup_entry_config_drive_store(struct config_item * item,const char * page,size_t count)
- Line: 1165
- Calls: gpio_virtuser_device_is_live, to_gpio_virtuser_lookup_entry

### gpio_virtuser_lookup_entry_config_group_release
- Return type: static void
- Signature: gpio_virtuser_lookup_entry_config_group_release(struct config_item * item)
- Line: 1582
- Calls: to_gpio_virtuser_lookup_entry

### gpio_virtuser_lookup_entry_config_key_show
- Return type: static ssize_t
- Signature: gpio_virtuser_lookup_entry_config_key_show(struct config_item * item,char * page)
- Line: 1046
- Calls: to_gpio_virtuser_lookup_entry

### gpio_virtuser_lookup_entry_config_key_store
- Return type: static ssize_t
- Signature: gpio_virtuser_lookup_entry_config_key_store(struct config_item * item,const char * page,size_t count)
- Line: 1058
- Calls: gpio_virtuser_device_is_live, to_gpio_virtuser_lookup_entry

### gpio_virtuser_lookup_entry_config_offset_show
- Return type: static ssize_t
- Signature: gpio_virtuser_lookup_entry_config_offset_show(struct config_item * item,char * page)
- Line: 1086
- Calls: to_gpio_virtuser_lookup_entry

### gpio_virtuser_lookup_entry_config_offset_store
- Return type: static ssize_t
- Signature: gpio_virtuser_lookup_entry_config_offset_store(struct config_item * item,const char * page,size_t count)
- Line: 1101
- Calls: gpio_virtuser_device_is_live, to_gpio_virtuser_lookup_entry

### gpio_virtuser_lookup_entry_config_pull_show
- Return type: static ssize_t
- Signature: gpio_virtuser_lookup_entry_config_pull_show(struct config_item * item,char * page)
- Line: 1195
- Calls: gpio_virtuser_lookup_get_flags

### gpio_virtuser_lookup_entry_config_pull_store
- Return type: static ssize_t
- Signature: gpio_virtuser_lookup_entry_config_pull_store(struct config_item * item,const char * page,size_t count)
- Line: 1213
- Calls: gpio_virtuser_device_is_live, to_gpio_virtuser_lookup_entry

### gpio_virtuser_lookup_entry_config_transitory_show
- Return type: static ssize_t
- Signature: gpio_virtuser_lookup_entry_config_transitory_show(struct config_item * item,char * page)
- Line: 1286
- Calls: gpio_virtuser_lookup_get_flags

### gpio_virtuser_lookup_entry_config_transitory_store
- Return type: static ssize_t
- Signature: gpio_virtuser_lookup_entry_config_transitory_store(struct config_item * item,const char * page,size_t count)
- Line: 1295
- Calls: gpio_virtuser_device_is_live, to_gpio_virtuser_lookup_entry

### gpio_virtuser_lookup_get_flags
- Return type: static gpio_lookup_flags
- Signature: gpio_virtuser_lookup_get_flags(struct config_item * item)
- Line: 1137
- Calls: to_gpio_virtuser_lookup_entry
- Called by: gpio_virtuser_lookup_entry_config_active_low_show, gpio_virtuser_lookup_entry_config_drive_show, gpio_virtuser_lookup_entry_config_pull_show, gpio_virtuser_lookup_entry_config_transitory_show

### gpio_virtuser_make_device_swnode
- Return type: static fwnode_handle *
- Signature: gpio_virtuser_make_device_swnode(struct gpio_virtuser_device * dev)
- Line: 1423
- Called by: gpio_virtuser_device_activate

### gpio_virtuser_make_lookup_entry_group
- Return type: static config_group *
- Signature: gpio_virtuser_make_lookup_entry_group(struct config_group * group,const char * name)
- Line: 1609
- Calls: gpio_virtuser_device_is_live, to_gpio_virtuser_lookup

### gpio_virtuser_make_lookup_group
- Return type: static config_group *
- Signature: gpio_virtuser_make_lookup_group(struct config_group * group,const char * name)
- Line: 1664
- Calls: gpio_virtuser_device_is_live, to_gpio_virtuser_device

### gpio_virtuser_make_lookup_table
- Return type: static int
- Signature: gpio_virtuser_make_lookup_table(struct gpio_virtuser_device * dev)
- Line: 1379
- Calls: gpio_virtuser_get_lookup_count, gpiod_add_lookup_table
- Called by: gpio_virtuser_device_activate

### gpio_virtuser_probe
- Return type: static int
- Signature: gpio_virtuser_probe(struct platform_device * pdev)
- Line: 903
- Calls: devm_gpiod_get_array, gpio_virtuser_count_ids, gpio_virtuser_dbgfs_init_line_array_attrs, gpio_virtuser_dbgfs_init_line_attrs, gpio_virtuser_get_ids

### gpio_virtuser_prop_is_gpio
- Return type: static int
- Signature: gpio_virtuser_prop_is_gpio(struct property * prop)
- Line: 840
- Called by: gpio_virtuser_count_ids, gpio_virtuser_get_ids

### gpio_virtuser_remove_lookup_table
- Return type: static void
- Signature: gpio_virtuser_remove_lookup_table(struct gpio_virtuser_device * dev)
- Line: 1414
- Calls: gpiod_remove_lookup_table
- Called by: gpio_virtuser_device_activate, gpio_virtuser_device_deactivate

### gpio_virtuser_set_array_value
- Return type: static int
- Signature: gpio_virtuser_set_array_value(struct gpio_descs * descs,unsigned long * values,bool atomic)
- Line: 210
- Calls: gpio_virtuser_init_irq_work_context, gpio_virtuser_irq_work_queue_sync
- Called by: gpio_virtuser_value_array_do_write

### gpio_virtuser_set_direction
- Return type: static int
- Signature: gpio_virtuser_set_direction(struct gpio_desc * desc,int dir,int val)
- Line: 357
- Calls: gpiod_direction_input, gpiod_direction_output
- Called by: gpio_virtuser_direction_do_write, gpio_virtuser_do_set_direction_atomic

### gpio_virtuser_set_direction_atomic
- Return type: static int
- Signature: gpio_virtuser_set_direction_atomic(struct gpio_desc * desc,int dir,int val)
- Line: 374
- Calls: gpio_virtuser_init_irq_work_context, gpio_virtuser_irq_work_queue_sync
- Called by: gpio_virtuser_direction_do_write

### gpio_virtuser_set_value_array_atomic
- Return type: static void
- Signature: gpio_virtuser_set_value_array_atomic(struct irq_work * work)
- Line: 199
- Calls: gpiod_set_array_value, to_gpio_virtuser_irq_work_context

### gpio_virtuser_set_value_atomic
- Return type: static void
- Signature: gpio_virtuser_set_value_atomic(struct irq_work * work)
- Line: 537
- Calls: gpiod_set_value, to_gpio_virtuser_irq_work_context

### gpio_virtuser_value_array_atomic_read
- Return type: static ssize_t
- Signature: gpio_virtuser_value_array_atomic_read(struct file * file,char __user * user_buf,size_t count,loff_t * ppos)
- Line: 289
- Calls: gpio_virtuser_value_array_do_read

### gpio_virtuser_value_array_atomic_write
- Return type: static ssize_t
- Signature: gpio_virtuser_value_array_atomic_write(struct file * file,const char __user * user_buf,size_t count,loff_t * ppos)
- Line: 297
- Calls: gpio_virtuser_value_array_do_write

### gpio_virtuser_value_array_do_read
- Return type: static ssize_t
- Signature: gpio_virtuser_value_array_do_read(struct file * file,char __user * user_buf,size_t size,loff_t * ppos,bool atomic)
- Line: 150
- Calls: gpio_virtuser_dbgfs_emit_value_array, gpio_virtuser_get_array_value
- Called by: gpio_virtuser_value_array_atomic_read, gpio_virtuser_value_array_read

### gpio_virtuser_value_array_do_write
- Return type: static ssize_t
- Signature: gpio_virtuser_value_array_do_write(struct file * file,const char __user * user_buf,size_t count,loff_t * ppos,bool atomic)
- Line: 228
- Calls: gpio_virtuser_dbgfs_parse_value_array, gpio_virtuser_set_array_value
- Called by: gpio_virtuser_value_array_atomic_write, gpio_virtuser_value_array_write

### gpio_virtuser_value_array_read
- Return type: static ssize_t
- Signature: gpio_virtuser_value_array_read(struct file * file,char __user * user_buf,size_t count,loff_t * ppos)
- Line: 264
- Calls: gpio_virtuser_value_array_do_read

### gpio_virtuser_value_array_write
- Return type: static ssize_t
- Signature: gpio_virtuser_value_array_write(struct file * file,const char __user * user_buf,size_t count,loff_t * ppos)
- Line: 272
- Calls: gpio_virtuser_value_array_do_write

### gpio_virtuser_value_atomic_get
- Return type: static int
- Signature: gpio_virtuser_value_atomic_get(void * data,u64 * val)
- Line: 518
- Calls: gpio_virtuser_init_irq_work_context, gpio_virtuser_irq_work_queue_sync

### gpio_virtuser_value_atomic_set
- Return type: static int
- Signature: gpio_virtuser_value_atomic_set(void * data,u64 val)
- Line: 546
- Calls: gpio_virtuser_init_irq_work_context, gpio_virtuser_irq_work_queue_sync

### gpio_virtuser_value_get
- Return type: static int
- Signature: gpio_virtuser_value_get(void * data,u64 * val)
- Line: 480
- Calls: gpiod_get_value_cansleep

### gpio_virtuser_value_set
- Return type: static int
- Signature: gpio_virtuser_value_set(void * data,u64 val)
- Line: 494
- Calls: gpiod_set_value_cansleep

### to_gpio_virtuser_device
- Return type: static gpio_virtuser_device *
- Signature: to_gpio_virtuser_device(struct config_item * item)
- Line: 991
- Called by: gpio_virtuser_device_config_dev_name_show, gpio_virtuser_device_config_group_release, gpio_virtuser_device_config_live_show, gpio_virtuser_device_config_live_store, gpio_virtuser_make_lookup_group

### to_gpio_virtuser_irq_work_context
- Return type: static gpio_virtuser_irq_work_context *
- Signature: to_gpio_virtuser_irq_work_context(struct irq_work * work)
- Line: 88
- Called by: gpio_virtuser_do_get_direction_atomic, gpio_virtuser_do_set_direction_atomic, gpio_virtuser_get_value_array_atomic, gpio_virtuser_get_value_atomic, gpio_virtuser_set_value_array_atomic, gpio_virtuser_set_value_atomic

### to_gpio_virtuser_lookup
- Return type: static gpio_virtuser_lookup *
- Signature: to_gpio_virtuser_lookup(struct config_item * item)
- Line: 1018
- Called by: gpio_virtuser_lookup_config_group_release, gpio_virtuser_make_lookup_entry_group

### to_gpio_virtuser_lookup_entry
- Return type: static gpio_virtuser_lookup_entry *
- Signature: to_gpio_virtuser_lookup_entry(struct config_item * item)
- Line: 1038
- Called by: gpio_virtuser_lookup_entry_config_active_low_store, gpio_virtuser_lookup_entry_config_drive_store, gpio_virtuser_lookup_entry_config_group_release, gpio_virtuser_lookup_entry_config_key_show, gpio_virtuser_lookup_entry_config_key_store, gpio_virtuser_lookup_entry_config_offset_show, gpio_virtuser_lookup_entry_config_offset_store, gpio_virtuser_lookup_entry_config_pull_store, gpio_virtuser_lookup_entry_config_transitory_store, gpio_virtuser_lookup_get_flags

## Structs (10)

### __anonea46d0ec0308
- Line: 74
- Members:
  - desc: gpio_desc *
  - descs: gpio_descs *
  - dbgfs_dir: dentry *
  - ad: gpio_virtuser_attr_data
  - ad: gpio_virtuser_attr_data
  - consumer: char[]
  - consumer_lock: mutex
  - debounce: unsigned int
  - irq: atomic_t
  - irq_count: atomic_t
  - name: const char *
  - fops: const struct file_operations *
  - work: irq_work
  - work_completion: completion
  - desc: gpio_desc *
  - dir: int
  - val: int
  - ret: int
  - descs: gpio_descs *
  - values: unsigned long *
  - pdev: platform_device *
  - group: config_group
  - id: int
  - lock: mutex
  - lookup_table: gpiod_lookup_table *
  - lookup_list: list_head
  - group: config_group
  - parent: gpio_virtuser_device *
  - siblings: list_head
  - con_id: char *
  - entry_list: list_head
  - group: config_group
  - parent: gpio_virtuser_lookup *
  - siblings: list_head
  - key: char *
  - offset: int
  - flags: gpio_lookup_flags

### __anonea46d0ec0408
- Line: 80
- Members:
  - desc: gpio_desc *
  - descs: gpio_descs *
  - dbgfs_dir: dentry *
  - ad: gpio_virtuser_attr_data
  - ad: gpio_virtuser_attr_data
  - consumer: char[]
  - consumer_lock: mutex
  - debounce: unsigned int
  - irq: atomic_t
  - irq_count: atomic_t
  - name: const char *
  - fops: const struct file_operations *
  - work: irq_work
  - work_completion: completion
  - desc: gpio_desc *
  - dir: int
  - val: int
  - ret: int
  - descs: gpio_descs *
  - values: unsigned long *
  - pdev: platform_device *
  - group: config_group
  - id: int
  - lock: mutex
  - lookup_table: gpiod_lookup_table *
  - lookup_list: list_head
  - group: config_group
  - parent: gpio_virtuser_device *
  - siblings: list_head
  - con_id: char *
  - entry_list: list_head
  - group: config_group
  - parent: gpio_virtuser_lookup *
  - siblings: list_head
  - key: char *
  - offset: int
  - flags: gpio_lookup_flags

### gpio_virtuser_attr_data
- Line: 44
- Members:
  - desc: gpio_desc *
  - descs: gpio_descs *
  - dbgfs_dir: dentry *
  - ad: gpio_virtuser_attr_data
  - ad: gpio_virtuser_attr_data
  - consumer: char[]
  - consumer_lock: mutex
  - debounce: unsigned int
  - irq: atomic_t
  - irq_count: atomic_t
  - name: const char *
  - fops: const struct file_operations *
  - work: irq_work
  - work_completion: completion
  - desc: gpio_desc *
  - dir: int
  - val: int
  - ret: int
  - descs: gpio_descs *
  - values: unsigned long *
  - pdev: platform_device *
  - group: config_group
  - id: int
  - lock: mutex
  - lookup_table: gpiod_lookup_table *
  - lookup_list: list_head
  - group: config_group
  - parent: gpio_virtuser_device *
  - siblings: list_head
  - con_id: char *
  - entry_list: list_head
  - group: config_group
  - parent: gpio_virtuser_lookup *
  - siblings: list_head
  - key: char *
  - offset: int
  - flags: gpio_lookup_flags

### gpio_virtuser_dbgfs_attr_descr
- Line: 65
- Members:
  - desc: gpio_desc *
  - descs: gpio_descs *
  - dbgfs_dir: dentry *
  - ad: gpio_virtuser_attr_data
  - ad: gpio_virtuser_attr_data
  - consumer: char[]
  - consumer_lock: mutex
  - debounce: unsigned int
  - irq: atomic_t
  - irq_count: atomic_t
  - name: const char *
  - fops: const struct file_operations *
  - work: irq_work
  - work_completion: completion
  - desc: gpio_desc *
  - dir: int
  - val: int
  - ret: int
  - descs: gpio_descs *
  - values: unsigned long *
  - pdev: platform_device *
  - group: config_group
  - id: int
  - lock: mutex
  - lookup_table: gpiod_lookup_table *
  - lookup_list: list_head
  - group: config_group
  - parent: gpio_virtuser_device *
  - siblings: list_head
  - con_id: char *
  - entry_list: list_head
  - group: config_group
  - parent: gpio_virtuser_lookup *
  - siblings: list_head
  - key: char *
  - offset: int
  - flags: gpio_lookup_flags

### gpio_virtuser_device
- Line: 978
- Members:
  - desc: gpio_desc *
  - descs: gpio_descs *
  - dbgfs_dir: dentry *
  - ad: gpio_virtuser_attr_data
  - ad: gpio_virtuser_attr_data
  - consumer: char[]
  - consumer_lock: mutex
  - debounce: unsigned int
  - irq: atomic_t
  - irq_count: atomic_t
  - name: const char *
  - fops: const struct file_operations *
  - work: irq_work
  - work_completion: completion
  - desc: gpio_desc *
  - dir: int
  - val: int
  - ret: int
  - descs: gpio_descs *
  - values: unsigned long *
  - pdev: platform_device *
  - group: config_group
  - id: int
  - lock: mutex
  - lookup_table: gpiod_lookup_table *
  - lookup_list: list_head
  - group: config_group
  - parent: gpio_virtuser_device *
  - siblings: list_head
  - con_id: char *
  - entry_list: list_head
  - group: config_group
  - parent: gpio_virtuser_lookup *
  - siblings: list_head
  - key: char *
  - offset: int
  - flags: gpio_lookup_flags

### gpio_virtuser_irq_work_context
- Line: 70
- Members:
  - desc: gpio_desc *
  - descs: gpio_descs *
  - dbgfs_dir: dentry *
  - ad: gpio_virtuser_attr_data
  - ad: gpio_virtuser_attr_data
  - consumer: char[]
  - consumer_lock: mutex
  - debounce: unsigned int
  - irq: atomic_t
  - irq_count: atomic_t
  - name: const char *
  - fops: const struct file_operations *
  - work: irq_work
  - work_completion: completion
  - desc: gpio_desc *
  - dir: int
  - val: int
  - ret: int
  - descs: gpio_descs *
  - values: unsigned long *
  - pdev: platform_device *
  - group: config_group
  - id: int
  - lock: mutex
  - lookup_table: gpiod_lookup_table *
  - lookup_list: list_head
  - group: config_group
  - parent: gpio_virtuser_device *
  - siblings: list_head
  - con_id: char *
  - entry_list: list_head
  - group: config_group
  - parent: gpio_virtuser_lookup *
  - siblings: list_head
  - key: char *
  - offset: int
  - flags: gpio_lookup_flags

### gpio_virtuser_line_array_data
- Line: 52
- Members:
  - desc: gpio_desc *
  - descs: gpio_descs *
  - dbgfs_dir: dentry *
  - ad: gpio_virtuser_attr_data
  - ad: gpio_virtuser_attr_data
  - consumer: char[]
  - consumer_lock: mutex
  - debounce: unsigned int
  - irq: atomic_t
  - irq_count: atomic_t
  - name: const char *
  - fops: const struct file_operations *
  - work: irq_work
  - work_completion: completion
  - desc: gpio_desc *
  - dir: int
  - val: int
  - ret: int
  - descs: gpio_descs *
  - values: unsigned long *
  - pdev: platform_device *
  - group: config_group
  - id: int
  - lock: mutex
  - lookup_table: gpiod_lookup_table *
  - lookup_list: list_head
  - group: config_group
  - parent: gpio_virtuser_device *
  - siblings: list_head
  - con_id: char *
  - entry_list: list_head
  - group: config_group
  - parent: gpio_virtuser_lookup *
  - siblings: list_head
  - key: char *
  - offset: int
  - flags: gpio_lookup_flags

### gpio_virtuser_line_data
- Line: 56
- Members:
  - desc: gpio_desc *
  - descs: gpio_descs *
  - dbgfs_dir: dentry *
  - ad: gpio_virtuser_attr_data
  - ad: gpio_virtuser_attr_data
  - consumer: char[]
  - consumer_lock: mutex
  - debounce: unsigned int
  - irq: atomic_t
  - irq_count: atomic_t
  - name: const char *
  - fops: const struct file_operations *
  - work: irq_work
  - work_completion: completion
  - desc: gpio_desc *
  - dir: int
  - val: int
  - ret: int
  - descs: gpio_descs *
  - values: unsigned long *
  - pdev: platform_device *
  - group: config_group
  - id: int
  - lock: mutex
  - lookup_table: gpiod_lookup_table *
  - lookup_list: list_head
  - group: config_group
  - parent: gpio_virtuser_device *
  - siblings: list_head
  - con_id: char *
  - entry_list: list_head
  - group: config_group
  - parent: gpio_virtuser_lookup *
  - siblings: list_head
  - key: char *
  - offset: int
  - flags: gpio_lookup_flags

### gpio_virtuser_lookup
- Line: 1006
- Members:
  - desc: gpio_desc *
  - descs: gpio_descs *
  - dbgfs_dir: dentry *
  - ad: gpio_virtuser_attr_data
  - ad: gpio_virtuser_attr_data
  - consumer: char[]
  - consumer_lock: mutex
  - debounce: unsigned int
  - irq: atomic_t
  - irq_count: atomic_t
  - name: const char *
  - fops: const struct file_operations *
  - work: irq_work
  - work_completion: completion
  - desc: gpio_desc *
  - dir: int
  - val: int
  - ret: int
  - descs: gpio_descs *
  - values: unsigned long *
  - pdev: platform_device *
  - group: config_group
  - id: int
  - lock: mutex
  - lookup_table: gpiod_lookup_table *
  - lookup_list: list_head
  - group: config_group
  - parent: gpio_virtuser_device *
  - siblings: list_head
  - con_id: char *
  - entry_list: list_head
  - group: config_group
  - parent: gpio_virtuser_lookup *
  - siblings: list_head
  - key: char *
  - offset: int
  - flags: gpio_lookup_flags

### gpio_virtuser_lookup_entry
- Line: 1025
- Members:
  - desc: gpio_desc *
  - descs: gpio_descs *
  - dbgfs_dir: dentry *
  - ad: gpio_virtuser_attr_data
  - ad: gpio_virtuser_attr_data
  - consumer: char[]
  - consumer_lock: mutex
  - debounce: unsigned int
  - irq: atomic_t
  - irq_count: atomic_t
  - name: const char *
  - fops: const struct file_operations *
  - work: irq_work
  - work_completion: completion
  - desc: gpio_desc *
  - dir: int
  - val: int
  - ret: int
  - descs: gpio_descs *
  - values: unsigned long *
  - pdev: platform_device *
  - group: config_group
  - id: int
  - lock: mutex
  - lookup_table: gpiod_lookup_table *
  - lookup_list: list_head
  - group: config_group
  - parent: gpio_virtuser_device *
  - siblings: list_head
  - con_id: char *
  - entry_list: list_head
  - group: config_group
  - parent: gpio_virtuser_lookup *
  - siblings: list_head
  - key: char *
  - offset: int
  - flags: gpio_lookup_flags

## Unions (2)

### __anonea46d0ec010a
- Line: 45
- Members:
  - desc: gpio_desc *
  - descs: gpio_descs *
  - dbgfs_dir: dentry *
  - ad: gpio_virtuser_attr_data
  - ad: gpio_virtuser_attr_data
  - consumer: char[]
  - consumer_lock: mutex
  - debounce: unsigned int
  - irq: atomic_t
  - irq_count: atomic_t
  - name: const char *
  - fops: const struct file_operations *
  - work: irq_work
  - work_completion: completion
  - desc: gpio_desc *
  - dir: int
  - val: int
  - ret: int
  - descs: gpio_descs *
  - values: unsigned long *
  - pdev: platform_device *
  - group: config_group
  - id: int
  - lock: mutex
  - lookup_table: gpiod_lookup_table *
  - lookup_list: list_head
  - group: config_group
  - parent: gpio_virtuser_device *
  - siblings: list_head
  - con_id: char *
  - entry_list: list_head
  - group: config_group
  - parent: gpio_virtuser_lookup *
  - siblings: list_head
  - key: char *
  - offset: int
  - flags: gpio_lookup_flags

### __anonea46d0ec020a
- Line: 73
- Members:
  - desc: gpio_desc *
  - descs: gpio_descs *
  - dbgfs_dir: dentry *
  - ad: gpio_virtuser_attr_data
  - ad: gpio_virtuser_attr_data
  - consumer: char[]
  - consumer_lock: mutex
  - debounce: unsigned int
  - irq: atomic_t
  - irq_count: atomic_t
  - name: const char *
  - fops: const struct file_operations *
  - work: irq_work
  - work_completion: completion
  - desc: gpio_desc *
  - dir: int
  - val: int
  - ret: int
  - descs: gpio_descs *
  - values: unsigned long *
  - pdev: platform_device *
  - group: config_group
  - id: int
  - lock: mutex
  - lookup_table: gpiod_lookup_table *
  - lookup_list: list_head
  - group: config_group
  - parent: gpio_virtuser_device *
  - siblings: list_head
  - con_id: char *
  - entry_list: list_head
  - group: config_group
  - parent: gpio_virtuser_lookup *
  - siblings: list_head
  - key: char *
  - offset: int
  - flags: gpio_lookup_flags

## Variables (23)

- static **gpio_virtuser_config_group_ops** : const struct configfs_group_operations (line 1744)
- static **gpio_virtuser_config_subsys** : configfs_subsystem (line 1753)
- static **gpio_virtuser_config_type** : const struct config_item_type (line 1748)
- static **gpio_virtuser_consumer_fops** : const struct file_operations (line 645)
- static **gpio_virtuser_dbg_root** : dentry * (line 42)
- static **gpio_virtuser_device_config_attrs** : configfs_attribute * [] (line 1575)
- static **gpio_virtuser_device_config_group_ops** : const struct configfs_group_operations (line 1713)
- static **gpio_virtuser_device_config_group_type** : const struct config_item_type (line 1717)
- static **gpio_virtuser_device_config_item_ops** : const struct configfs_item_operations (line 1709)
- static **gpio_virtuser_direction_atomic_fops** : const struct file_operations (line 472)
- static **gpio_virtuser_direction_fops** : const struct file_operations (line 448)
- static **gpio_virtuser_driver** : platform_driver (line 970)
- static **gpio_virtuser_line_array_dbgfs_attrs** : const struct gpio_virtuser_dbgfs_attr_descr[] (line 708)
- static **gpio_virtuser_line_dbgfs_attrs** : const struct gpio_virtuser_dbgfs_attr_descr[] (line 720)
- static **gpio_virtuser_lookup_config_group_ops** : configfs_group_operations (line 1653)
- static **gpio_virtuser_lookup_config_group_type** : const struct config_item_type (line 1657)
- static **gpio_virtuser_lookup_config_item_ops** : const struct configfs_item_operations (line 1648)
- static **gpio_virtuser_lookup_entry_config_attrs** : configfs_attribute * [] (line 1324)
- static **gpio_virtuser_lookup_entry_config_group_type** : const struct config_item_type (line 1602)
- static **gpio_virtuser_lookup_entry_config_item_ops** : configfs_item_operations (line 1597)
- static **gpio_virtuser_of_match** : const struct of_device_id[] (line 964)
- static **gpio_virtuser_value_array_atomic_fops** : const struct file_operations (line 305)
- static **gpio_virtuser_value_array_fops** : const struct file_operations (line 280)

## Macros (2)

- **GPIO_VIRTUSER_NAME_BUF_LEN** (line 39)
- **pr_fmt**(fmt) (line 8)
