# drivers/gpio/gpio-sim.c

Subsystem: drivers/gpio

## Functions (76)

### gpio_sim_add_bank
- Return type: static int
- Signature: gpio_sim_add_bank(struct fwnode_handle * swnode,struct device * dev)
- Line: 419
- Calls: gpio_sim_setup_sysfs
- Called by: gpio_sim_probe

### gpio_sim_apply_pull
- Return type: static int
- Signature: gpio_sim_apply_pull(struct gpio_sim_chip * chip,unsigned int offset,int value)
- Line: 69
- Called by: gpio_sim_set_config, gpio_sim_sysfs_pull_store

### gpio_sim_bank_add_hogs
- Return type: static int
- Signature: gpio_sim_bank_add_hogs(struct gpio_sim_bank * bank)
- Line: 822
- Called by: gpio_sim_device_activate

### gpio_sim_bank_config_chip_name_show
- Return type: static ssize_t
- Signature: gpio_sim_bank_config_chip_name_show(struct config_item * item,char * page)
- Line: 1067
- Calls: gpio_sim_bank_get_device, gpio_sim_device_is_live, to_gpio_sim_bank

### gpio_sim_bank_config_group_release
- Return type: static void
- Signature: gpio_sim_bank_config_group_release(struct config_item * item)
- Line: 1487
- Calls: gpio_sim_bank_get_device, to_gpio_sim_bank

### gpio_sim_bank_config_label_show
- Return type: static ssize_t
- Signature: gpio_sim_bank_config_label_show(struct config_item * item,char * page)
- Line: 1086
- Calls: gpio_sim_bank_get_device, to_gpio_sim_bank

### gpio_sim_bank_config_label_store
- Return type: static ssize_t
- Signature: gpio_sim_bank_config_label_store(struct config_item * item,const char * page,size_t count)
- Line: 1096
- Calls: gpio_sim_bank_get_device, gpio_sim_device_is_live, gpio_sim_strdup_trimmed, to_gpio_sim_bank

### gpio_sim_bank_config_make_line_group
- Return type: static config_group *
- Signature: gpio_sim_bank_config_make_line_group(struct config_group * group,const char * name)
- Line: 1454
- Calls: gpio_sim_bank_get_device, gpio_sim_device_is_live, to_gpio_sim_bank

### gpio_sim_bank_config_num_lines_show
- Return type: static ssize_t
- Signature: gpio_sim_bank_config_num_lines_show(struct config_item * item,char * page)
- Line: 1121
- Calls: gpio_sim_bank_get_device, to_gpio_sim_bank

### gpio_sim_bank_config_num_lines_store
- Return type: static ssize_t
- Signature: gpio_sim_bank_config_num_lines_store(struct config_item * item,const char * page,size_t count)
- Line: 1132
- Calls: gpio_sim_bank_get_device, gpio_sim_device_is_live, to_gpio_sim_bank

### gpio_sim_bank_get_device
- Return type: static gpio_sim_device *
- Signature: gpio_sim_bank_get_device(struct gpio_sim_bank * bank)
- Line: 613
- Called by: gpio_sim_bank_config_chip_name_show, gpio_sim_bank_config_group_release, gpio_sim_bank_config_label_show, gpio_sim_bank_config_label_store, gpio_sim_bank_config_make_line_group, gpio_sim_bank_config_num_lines_show, gpio_sim_bank_config_num_lines_store, gpio_sim_line_get_device

### gpio_sim_bank_has_label
- Return type: static bool
- Signature: gpio_sim_bank_has_label(struct gpio_sim_bank * bank)
- Line: 607
- Called by: gpio_sim_make_bank_swnode

### gpio_sim_bank_labels_non_unique
- Return type: static bool
- Signature: gpio_sim_bank_labels_non_unique(struct gpio_sim_device * dev)
- Line: 881
- Called by: gpio_sim_device_activate

### gpio_sim_config_make_device_group
- Return type: static config_group *
- Signature: gpio_sim_config_make_device_group(struct config_group * group,const char * name)
- Line: 1570

### gpio_sim_dbg_show
- Return type: static void
- Signature: gpio_sim_dbg_show(struct seq_file * seq,struct gpio_chip * gc)
- Line: 255
- Calls: gpiochip_get_data

### gpio_sim_device_activate
- Return type: static int
- Signature: gpio_sim_device_activate(struct gpio_sim_device * dev)
- Line: 898
- Calls: gpio_sim_bank_add_hogs, gpio_sim_bank_labels_non_unique, gpio_sim_make_bank_swnode, gpio_sim_remove_swnode_recursive
- Called by: gpio_sim_device_config_live_store

### gpio_sim_device_config_dev_name_show
- Return type: static ssize_t
- Signature: gpio_sim_device_config_dev_name_show(struct config_item * item,char * page)
- Line: 688
- Calls: to_gpio_sim_device

### gpio_sim_device_config_group_release
- Return type: static void
- Signature: gpio_sim_device_config_group_release(struct config_item * item)
- Line: 1540
- Calls: gpio_sim_device_deactivate, gpio_sim_device_is_live, to_gpio_sim_device

### gpio_sim_device_config_live_show
- Return type: static ssize_t
- Signature: gpio_sim_device_config_live_show(struct config_item * item,char * page)
- Line: 706
- Calls: gpio_sim_device_is_live, to_gpio_sim_device

### gpio_sim_device_config_live_store
- Return type: static ssize_t
- Signature: gpio_sim_device_config_live_store(struct config_item * item,const char * page,size_t count)
- Line: 1007
- Calls: gpio_sim_device_activate, gpio_sim_device_deactivate, gpio_sim_device_is_live, gpio_sim_device_lockup_configfs, to_gpio_sim_device

### gpio_sim_device_config_make_bank_group
- Return type: static config_group *
- Signature: gpio_sim_device_config_make_bank_group(struct config_group * group,const char * name)
- Line: 1515
- Calls: gpio_sim_device_is_live, to_gpio_sim_device

### gpio_sim_device_deactivate
- Return type: static void
- Signature: gpio_sim_device_deactivate(struct gpio_sim_device * dev)
- Line: 967
- Calls: gpio_sim_remove_swnode_recursive
- Called by: gpio_sim_device_config_group_release, gpio_sim_device_config_live_store

### gpio_sim_device_is_live
- Return type: static bool
- Signature: gpio_sim_device_is_live(struct gpio_sim_device * dev)
- Line: 670
- Called by: gpio_sim_bank_config_chip_name_show, gpio_sim_bank_config_label_store, gpio_sim_bank_config_make_line_group, gpio_sim_bank_config_num_lines_store, gpio_sim_device_config_group_release, gpio_sim_device_config_live_show, gpio_sim_device_config_live_store, gpio_sim_device_config_make_bank_group, gpio_sim_hog_config_active_low_store, gpio_sim_hog_config_direction_store, gpio_sim_hog_config_name_store, gpio_sim_line_config_name_store

### gpio_sim_device_lockup_configfs
- Return type: static void
- Signature: gpio_sim_device_lockup_configfs(struct gpio_sim_device * dev,bool lock)
- Line: 980
- Called by: gpio_sim_device_config_live_store

### gpio_sim_direction_input
- Return type: static int
- Signature: gpio_sim_direction_input(struct gpio_chip * gc,unsigned int offset)
- Line: 168
- Calls: gpiochip_get_data

### gpio_sim_direction_output
- Return type: static int
- Signature: gpio_sim_direction_output(struct gpio_chip * gc,unsigned int offset,int value)
- Line: 155
- Calls: gpiochip_get_data

### gpio_sim_dispose_mappings
- Return type: static void
- Signature: gpio_sim_dispose_mappings(void * data)
- Line: 342

### gpio_sim_emit_chip_name
- Return type: static int
- Signature: gpio_sim_emit_chip_name(struct device * dev,void * data)
- Line: 1053

### gpio_sim_exit
- Return type: static void __exit
- Signature: gpio_sim_exit(void)
- Line: 1634

### gpio_sim_free
- Return type: static void
- Signature: gpio_sim_free(struct gpio_chip * gc,unsigned int offset)
- Line: 223
- Calls: gpiochip_get_data

### gpio_sim_get
- Return type: static int
- Signature: gpio_sim_get(struct gpio_chip * gc,unsigned int offset)
- Line: 113
- Calls: gpiochip_get_data

### gpio_sim_get_direction
- Return type: static int
- Signature: gpio_sim_get_direction(struct gpio_chip * gc,unsigned int offset)
- Line: 178
- Calls: gpiochip_get_data

### gpio_sim_get_line_names_size
- Return type: static unsigned int
- Signature: gpio_sim_get_line_names_size(struct gpio_sim_bank * bank)
- Line: 717
- Called by: gpio_sim_make_bank_swnode

### gpio_sim_get_multiple
- Return type: static int
- Signature: gpio_sim_get_multiple(struct gpio_chip * gc,unsigned long * mask,unsigned long * bits)
- Line: 132
- Calls: gpiochip_get_data

### gpio_sim_get_reserved_ranges_size
- Return type: static unsigned int
- Signature: gpio_sim_get_reserved_ranges_size(struct gpio_sim_bank * bank)
- Line: 745
- Called by: gpio_sim_make_bank_swnode

### gpio_sim_hog_config_active_low_show
- Return type: static ssize_t
- Signature: gpio_sim_hog_config_active_low_show(struct config_item * item,char * page)
- Line: 1333
- Calls: gpio_sim_hog_get_device, to_gpio_sim_hog

### gpio_sim_hog_config_active_low_store
- Return type: static ssize_t
- Signature: gpio_sim_hog_config_active_low_store(struct config_item * item,const char * page,size_t count)
- Line: 1345
- Calls: gpio_sim_device_is_live, gpio_sim_hog_get_device, to_gpio_sim_hog

### gpio_sim_hog_config_direction_show
- Return type: static ssize_t
- Signature: gpio_sim_hog_config_direction_show(struct config_item * item,char * page)
- Line: 1274
- Calls: gpio_sim_hog_get_device, to_gpio_sim_hog

### gpio_sim_hog_config_direction_store
- Return type: static ssize_t
- Signature: gpio_sim_hog_config_direction_store(struct config_item * item,const char * page,size_t count)
- Line: 1305
- Calls: gpio_sim_device_is_live, gpio_sim_hog_get_device, to_gpio_sim_hog

### gpio_sim_hog_config_item_release
- Return type: static void
- Signature: gpio_sim_hog_config_item_release(struct config_item * item)
- Line: 1376
- Calls: gpio_sim_hog_get_device, to_gpio_sim_hog

### gpio_sim_hog_config_name_show
- Return type: static ssize_t
- Signature: gpio_sim_hog_config_name_show(struct config_item * item,char * page)
- Line: 1239
- Calls: gpio_sim_hog_get_device, to_gpio_sim_hog

### gpio_sim_hog_config_name_store
- Return type: static ssize_t
- Signature: gpio_sim_hog_config_name_store(struct config_item * item,const char * page,size_t count)
- Line: 1250
- Calls: gpio_sim_device_is_live, gpio_sim_hog_get_device, gpio_sim_strdup_trimmed, to_gpio_sim_hog

### gpio_sim_hog_get_device
- Return type: static gpio_sim_device *
- Signature: gpio_sim_hog_get_device(struct gpio_sim_hog * hog)
- Line: 663
- Calls: gpio_sim_line_get_device
- Called by: gpio_sim_hog_config_active_low_show, gpio_sim_hog_config_active_low_store, gpio_sim_hog_config_direction_show, gpio_sim_hog_config_direction_store, gpio_sim_hog_config_item_release, gpio_sim_hog_config_name_show, gpio_sim_hog_config_name_store

### gpio_sim_init
- Return type: static int __init
- Signature: gpio_sim_init(void)
- Line: 1609

### gpio_sim_irq_released
- Return type: static void
- Signature: gpio_sim_irq_released(struct irq_domain * domain,irq_hw_number_t hwirq,void * data)
- Line: 242
- Calls: gpiochip_unlock_as_irq

### gpio_sim_irq_requested
- Return type: static int
- Signature: gpio_sim_irq_requested(struct irq_domain * domain,irq_hw_number_t hwirq,void * data)
- Line: 234
- Calls: gpiochip_lock_as_irq

### gpio_sim_line_config_group_release
- Return type: static void
- Signature: gpio_sim_line_config_group_release(struct config_item * item)
- Line: 1426
- Calls: gpio_sim_line_get_device, to_gpio_sim_line

### gpio_sim_line_config_make_hog_item
- Return type: static config_item *
- Signature: gpio_sim_line_config_make_hog_item(struct config_group * group,const char * name)
- Line: 1400
- Calls: gpio_sim_line_get_device, to_gpio_sim_line

### gpio_sim_line_config_name_show
- Return type: static ssize_t
- Signature: gpio_sim_line_config_name_show(struct config_item * item,char * page)
- Line: 1167
- Calls: gpio_sim_line_get_device, to_gpio_sim_line

### gpio_sim_line_config_name_store
- Return type: static ssize_t
- Signature: gpio_sim_line_config_name_store(struct config_item * item,const char * page,size_t count)
- Line: 1177
- Calls: gpio_sim_device_is_live, gpio_sim_line_get_device, gpio_sim_strdup_trimmed, to_gpio_sim_line

### gpio_sim_line_config_valid_show
- Return type: static ssize_t
- Signature: gpio_sim_line_config_valid_show(struct config_item * item,char * page)
- Line: 1202
- Calls: gpio_sim_line_get_device, to_gpio_sim_line

### gpio_sim_line_config_valid_store
- Return type: static ssize_t
- Signature: gpio_sim_line_config_valid_store(struct config_item * item,const char * page,size_t count)
- Line: 1212
- Calls: gpio_sim_line_get_device, to_gpio_sim_line

### gpio_sim_line_get_device
- Return type: static gpio_sim_device *
- Signature: gpio_sim_line_get_device(struct gpio_sim_line * line)
- Line: 642
- Calls: gpio_sim_bank_get_device
- Called by: gpio_sim_hog_get_device, gpio_sim_line_config_group_release, gpio_sim_line_config_make_hog_item, gpio_sim_line_config_name_show, gpio_sim_line_config_name_store, gpio_sim_line_config_valid_show, gpio_sim_line_config_valid_store

### gpio_sim_make_bank_swnode
- Return type: static fwnode_handle *
- Signature: gpio_sim_make_bank_swnode(struct gpio_sim_bank * bank,struct fwnode_handle * parent)
- Line: 776
- Calls: gpio_sim_bank_has_label, gpio_sim_get_line_names_size, gpio_sim_get_reserved_ranges_size, gpio_sim_set_line_names, gpio_sim_set_reserved_ranges
- Called by: gpio_sim_device_activate

### gpio_sim_probe
- Return type: static int
- Signature: gpio_sim_probe(struct platform_device * pdev)
- Line: 518
- Calls: gpio_sim_add_bank

### gpio_sim_put_device
- Return type: static void
- Signature: gpio_sim_put_device(void * data)
- Line: 335

### gpio_sim_remove_swnode_recursive
- Return type: static void
- Signature: gpio_sim_remove_swnode_recursive(struct fwnode_handle * swnode)
- Line: 871
- Calls: gpio_sim_remove_swnode_recursive
- Called by: gpio_sim_device_activate, gpio_sim_device_deactivate, gpio_sim_remove_swnode_recursive

### gpio_sim_request
- Return type: static int
- Signature: gpio_sim_request(struct gpio_chip * gc,unsigned int offset)
- Line: 213
- Calls: gpiochip_get_data

### gpio_sim_set
- Return type: static int
- Signature: gpio_sim_set(struct gpio_chip * gc,unsigned int offset,int value)
- Line: 122
- Calls: gpiochip_get_data

### gpio_sim_set_config
- Return type: static int
- Signature: gpio_sim_set_config(struct gpio_chip * gc,unsigned int offset,unsigned long config)
- Line: 189
- Calls: gpio_sim_apply_pull, gpiochip_get_data

### gpio_sim_set_line_names
- Return type: static void
- Signature: gpio_sim_set_line_names(struct gpio_sim_bank * bank,char ** line_names)
- Line: 733
- Called by: gpio_sim_make_bank_swnode

### gpio_sim_set_multiple
- Return type: static int
- Signature: gpio_sim_set_multiple(struct gpio_chip * gc,unsigned long * mask,unsigned long * bits)
- Line: 143
- Calls: gpiochip_get_data

### gpio_sim_set_reserved_ranges
- Return type: static void
- Signature: gpio_sim_set_reserved_ranges(struct gpio_sim_bank * bank,u32 * ranges)
- Line: 760
- Called by: gpio_sim_make_bank_swnode

### gpio_sim_setup_sysfs
- Return type: static int
- Signature: gpio_sim_setup_sysfs(struct gpio_sim_chip * chip)
- Line: 358
- Called by: gpio_sim_add_bank

### gpio_sim_strdup_trimmed
- Return type: static char *
- Signature: gpio_sim_strdup_trimmed(const char * str,size_t count)
- Line: 677
- Called by: gpio_sim_bank_config_label_store, gpio_sim_hog_config_name_store, gpio_sim_line_config_name_store

### gpio_sim_sysfs_pull_show
- Return type: static ssize_t
- Signature: gpio_sim_sysfs_pull_show(struct device * dev,struct device_attribute * attr,char * buf)
- Line: 302
- Calls: to_gpio_sim_attr

### gpio_sim_sysfs_pull_store
- Return type: static ssize_t
- Signature: gpio_sim_sysfs_pull_store(struct device * dev,struct device_attribute * attr,const char * buf,size_t len)
- Line: 316
- Calls: gpio_sim_apply_pull, to_gpio_sim_attr

### gpio_sim_sysfs_remove
- Return type: static void
- Signature: gpio_sim_sysfs_remove(void * data)
- Line: 351

### gpio_sim_sysfs_val_show
- Return type: static ssize_t
- Signature: gpio_sim_sysfs_val_show(struct device * dev,struct device_attribute * attr,char * buf)
- Line: 273
- Calls: to_gpio_sim_attr

### gpio_sim_sysfs_val_store
- Return type: static ssize_t
- Signature: gpio_sim_sysfs_val_store(struct device * dev,struct device_attribute * attr,const char * buf,size_t count)
- Line: 286

### gpio_sim_to_irq
- Return type: static int
- Signature: gpio_sim_to_irq(struct gpio_chip * gc,unsigned int offset)
- Line: 206
- Calls: gpiochip_get_data

### to_gpio_sim_attr
- Return type: static gpio_sim_attribute *
- Signature: to_gpio_sim_attr(struct device_attribute * dev_attr)
- Line: 64
- Called by: gpio_sim_sysfs_pull_show, gpio_sim_sysfs_pull_store, gpio_sim_sysfs_val_show

### to_gpio_sim_bank
- Return type: static gpio_sim_bank *
- Signature: to_gpio_sim_bank(struct config_item * item)
- Line: 600
- Called by: gpio_sim_bank_config_chip_name_show, gpio_sim_bank_config_group_release, gpio_sim_bank_config_label_show, gpio_sim_bank_config_label_store, gpio_sim_bank_config_make_line_group, gpio_sim_bank_config_num_lines_show, gpio_sim_bank_config_num_lines_store

### to_gpio_sim_device
- Return type: static gpio_sim_device *
- Signature: to_gpio_sim_device(struct config_item * item)
- Line: 566
- Called by: gpio_sim_device_config_dev_name_show, gpio_sim_device_config_group_release, gpio_sim_device_config_live_show, gpio_sim_device_config_live_store, gpio_sim_device_config_make_bank_group

### to_gpio_sim_hog
- Return type: static gpio_sim_hog *
- Signature: to_gpio_sim_hog(struct config_item * item)
- Line: 658
- Called by: gpio_sim_hog_config_active_low_show, gpio_sim_hog_config_active_low_store, gpio_sim_hog_config_direction_show, gpio_sim_hog_config_direction_store, gpio_sim_hog_config_item_release, gpio_sim_hog_config_name_show, gpio_sim_hog_config_name_store

### to_gpio_sim_line
- Return type: static gpio_sim_line *
- Signature: to_gpio_sim_line(struct config_item * item)
- Line: 634
- Called by: gpio_sim_line_config_group_release, gpio_sim_line_config_make_hog_item, gpio_sim_line_config_name_show, gpio_sim_line_config_name_store, gpio_sim_line_config_valid_show, gpio_sim_line_config_valid_store

## Structs (7)

### gpio_sim_attribute
- Line: 58
- Members:
  - gc: gpio_chip
  - dev: device *
  - request_map: unsigned long *
  - direction_map: unsigned long *
  - value_map: unsigned long *
  - pull_map: unsigned long *
  - irq_sim: irq_domain *
  - lock: mutex
  - attr_groups: const struct attribute_group **
  - dev_attr: device_attribute
  - offset: unsigned int
  - pdev: platform_device *
  - group: config_group
  - id: int
  - lock: mutex
  - bank_list: list_head
  - group: config_group
  - parent: gpio_sim_device *
  - siblings: list_head
  - label: char *
  - num_lines: unsigned int
  - line_list: list_head
  - swnode: fwnode_handle *
  - group: config_group
  - parent: gpio_sim_bank *
  - siblings: list_head
  - offset: unsigned int
  - name: char *
  - valid: bool
  - hog: gpio_sim_hog *
  - item: config_item
  - parent: gpio_sim_line *
  - name: char *
  - dir: int
  - active_low: bool
  - swnode: fwnode_handle *
  - page: char *

### gpio_sim_bank
- Line: 573
- Members:
  - gc: gpio_chip
  - dev: device *
  - request_map: unsigned long *
  - direction_map: unsigned long *
  - value_map: unsigned long *
  - pull_map: unsigned long *
  - irq_sim: irq_domain *
  - lock: mutex
  - attr_groups: const struct attribute_group **
  - dev_attr: device_attribute
  - offset: unsigned int
  - pdev: platform_device *
  - group: config_group
  - id: int
  - lock: mutex
  - bank_list: list_head
  - group: config_group
  - parent: gpio_sim_device *
  - siblings: list_head
  - label: char *
  - num_lines: unsigned int
  - line_list: list_head
  - swnode: fwnode_handle *
  - group: config_group
  - parent: gpio_sim_bank *
  - siblings: list_head
  - offset: unsigned int
  - name: char *
  - valid: bool
  - hog: gpio_sim_hog *
  - item: config_item
  - parent: gpio_sim_line *
  - name: char *
  - dir: int
  - active_low: bool
  - swnode: fwnode_handle *
  - page: char *

### gpio_sim_chip
- Line: 46
- Members:
  - gc: gpio_chip
  - dev: device *
  - request_map: unsigned long *
  - direction_map: unsigned long *
  - value_map: unsigned long *
  - pull_map: unsigned long *
  - irq_sim: irq_domain *
  - lock: mutex
  - attr_groups: const struct attribute_group **
  - dev_attr: device_attribute
  - offset: unsigned int
  - pdev: platform_device *
  - group: config_group
  - id: int
  - lock: mutex
  - bank_list: list_head
  - group: config_group
  - parent: gpio_sim_device *
  - siblings: list_head
  - label: char *
  - num_lines: unsigned int
  - line_list: list_head
  - swnode: fwnode_handle *
  - group: config_group
  - parent: gpio_sim_bank *
  - siblings: list_head
  - offset: unsigned int
  - name: char *
  - valid: bool
  - hog: gpio_sim_hog *
  - item: config_item
  - parent: gpio_sim_line *
  - name: char *
  - dir: int
  - active_low: bool
  - swnode: fwnode_handle *
  - page: char *

### gpio_sim_chip_name_ctx
- Line: 1048
- Members:
  - gc: gpio_chip
  - dev: device *
  - request_map: unsigned long *
  - direction_map: unsigned long *
  - value_map: unsigned long *
  - pull_map: unsigned long *
  - irq_sim: irq_domain *
  - lock: mutex
  - attr_groups: const struct attribute_group **
  - dev_attr: device_attribute
  - offset: unsigned int
  - pdev: platform_device *
  - group: config_group
  - id: int
  - lock: mutex
  - bank_list: list_head
  - group: config_group
  - parent: gpio_sim_device *
  - siblings: list_head
  - label: char *
  - num_lines: unsigned int
  - line_list: list_head
  - swnode: fwnode_handle *
  - group: config_group
  - parent: gpio_sim_bank *
  - siblings: list_head
  - offset: unsigned int
  - name: char *
  - valid: bool
  - hog: gpio_sim_hog *
  - item: config_item
  - parent: gpio_sim_line *
  - name: char *
  - dir: int
  - active_low: bool
  - swnode: fwnode_handle *
  - page: char *

### gpio_sim_device
- Line: 546
- Members:
  - gc: gpio_chip
  - dev: device *
  - request_map: unsigned long *
  - direction_map: unsigned long *
  - value_map: unsigned long *
  - pull_map: unsigned long *
  - irq_sim: irq_domain *
  - lock: mutex
  - attr_groups: const struct attribute_group **
  - dev_attr: device_attribute
  - offset: unsigned int
  - pdev: platform_device *
  - group: config_group
  - id: int
  - lock: mutex
  - bank_list: list_head
  - group: config_group
  - parent: gpio_sim_device *
  - siblings: list_head
  - label: char *
  - num_lines: unsigned int
  - line_list: list_head
  - swnode: fwnode_handle *
  - group: config_group
  - parent: gpio_sim_bank *
  - siblings: list_head
  - offset: unsigned int
  - name: char *
  - valid: bool
  - hog: gpio_sim_hog *
  - item: config_item
  - parent: gpio_sim_line *
  - name: char *
  - dir: int
  - active_low: bool
  - swnode: fwnode_handle *
  - page: char *

### gpio_sim_hog
- Line: 649
- Members:
  - gc: gpio_chip
  - dev: device *
  - request_map: unsigned long *
  - direction_map: unsigned long *
  - value_map: unsigned long *
  - pull_map: unsigned long *
  - irq_sim: irq_domain *
  - lock: mutex
  - attr_groups: const struct attribute_group **
  - dev_attr: device_attribute
  - offset: unsigned int
  - pdev: platform_device *
  - group: config_group
  - id: int
  - lock: mutex
  - bank_list: list_head
  - group: config_group
  - parent: gpio_sim_device *
  - siblings: list_head
  - label: char *
  - num_lines: unsigned int
  - line_list: list_head
  - swnode: fwnode_handle *
  - group: config_group
  - parent: gpio_sim_bank *
  - siblings: list_head
  - offset: unsigned int
  - name: char *
  - valid: bool
  - hog: gpio_sim_hog *
  - item: config_item
  - parent: gpio_sim_line *
  - name: char *
  - dir: int
  - active_low: bool
  - swnode: fwnode_handle *
  - page: char *

### gpio_sim_line
- Line: 620
- Members:
  - gc: gpio_chip
  - dev: device *
  - request_map: unsigned long *
  - direction_map: unsigned long *
  - value_map: unsigned long *
  - pull_map: unsigned long *
  - irq_sim: irq_domain *
  - lock: mutex
  - attr_groups: const struct attribute_group **
  - dev_attr: device_attribute
  - offset: unsigned int
  - pdev: platform_device *
  - group: config_group
  - id: int
  - lock: mutex
  - bank_list: list_head
  - group: config_group
  - parent: gpio_sim_device *
  - siblings: list_head
  - label: char *
  - num_lines: unsigned int
  - line_list: list_head
  - swnode: fwnode_handle *
  - group: config_group
  - parent: gpio_sim_bank *
  - siblings: list_head
  - offset: unsigned int
  - name: char *
  - valid: bool
  - hog: gpio_sim_hog *
  - item: config_item
  - parent: gpio_sim_line *
  - name: char *
  - dir: int
  - active_low: bool
  - swnode: fwnode_handle *
  - page: char *

## Variables (22)

- static **gpio_sim_bank_config_attrs** : configfs_attribute * [] (line 1159)
- static **gpio_sim_bank_config_group_ops** : const struct configfs_group_operations (line 1503)
- static **gpio_sim_bank_config_group_type** : const struct config_item_type (line 1507)
- static **gpio_sim_bank_config_item_ops** : const struct configfs_item_operations (line 1499)
- static **gpio_sim_config_group_ops** : const struct configfs_group_operations (line 1591)
- static **gpio_sim_config_subsys** : configfs_subsystem (line 1600)
- static **gpio_sim_config_type** : const struct config_item_type (line 1595)
- static **gpio_sim_device_config_attrs** : configfs_attribute * [] (line 1042)
- static **gpio_sim_device_config_group_ops** : const struct configfs_group_operations (line 1558)
- static **gpio_sim_device_config_group_type** : const struct config_item_type (line 1562)
- static **gpio_sim_device_config_item_ops** : const struct configfs_item_operations (line 1554)
- static **gpio_sim_driver** : platform_driver (line 538)
- static **gpio_sim_hog_config_attrs** : configfs_attribute * [] (line 1369)
- static **gpio_sim_hog_config_item_ops** : const struct configfs_item_operations (line 1389)
- static **gpio_sim_hog_config_type** : const struct config_item_type (line 1393)
- static **gpio_sim_irq_sim_ops** : const struct irq_sim_ops (line 250)
- static **gpio_sim_line_config_attrs** : configfs_attribute * [] (line 1233)
- static **gpio_sim_line_config_group_ops** : const struct configfs_group_operations (line 1442)
- static **gpio_sim_line_config_item_ops** : const struct configfs_item_operations (line 1438)
- static **gpio_sim_line_config_type** : const struct config_item_type (line 1446)
- static **gpio_sim_of_match** : const struct of_device_id[] (line 532)
- static **gpio_sim_sysfs_pull_strings** : const char * const[] (line 297)

## Macros (5)

- **GPIO_SIM_HOG_PROP_MAX** (line 41)
- **GPIO_SIM_NGPIO_MAX** (line 39)
- **GPIO_SIM_NUM_ATTRS** (line 42)
- **GPIO_SIM_PROP_MAX** (line 40)
- **pr_fmt**(fmt) (line 8)
