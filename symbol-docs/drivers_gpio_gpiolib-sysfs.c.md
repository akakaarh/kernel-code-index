# drivers/gpio/gpiolib-sysfs.c

Subsystem: drivers/gpio

## Functions (35)

### active_low_show
- Return type: static ssize_t
- Signature: active_low_show(struct device * dev,struct device_attribute * attr,char * buf)
- Line: 367

### active_low_store
- Return type: static ssize_t
- Signature: active_low_store(struct device * dev,struct device_attribute * attr,const char * buf,size_t size)
- Line: 381
- Calls: gpio_sysfs_set_active_low

### base_show
- Return type: static ssize_t
- Signature: base_show(struct device * dev,struct device_attribute * attr,char * buf)
- Line: 445

### chip_export_store
- Return type: static ssize_t
- Signature: chip_export_store(struct device * dev,struct device_attribute * attr,const char * buf,size_t size)
- Line: 557
- Calls: do_chip_export_store

### chip_unexport_store
- Return type: static ssize_t
- Signature: chip_unexport_store(struct device * dev,struct device_attribute * attr,const char * buf,size_t size)
- Line: 567
- Calls: do_chip_export_store

### direction_show
- Return type: static ssize_t
- Signature: direction_show(struct device * dev,struct device_attribute * attr,char * buf)
- Line: 124
- Calls: gpiod_get_direction

### direction_store
- Return type: static ssize_t
- Signature: direction_store(struct device * dev,struct device_attribute * attr,const char * buf,size_t size)
- Line: 140
- Calls: gpiod_direction_input, gpiod_direction_output_raw

### do_chip_export_store
- Return type: static ssize_t
- Signature: do_chip_export_store(struct device * dev,struct device_attribute * attr,const char * buf,ssize_t size,int (* handler)(struct gpio_desc * desc))
- Line: 531
- Calls: gpio_device_get_desc
- Called by: chip_export_store, chip_unexport_store

### edge_show
- Return type: static ssize_t
- Signature: edge_show(struct device * dev,struct device_attribute * attr,char * buf)
- Line: 295

### edge_store
- Return type: static ssize_t
- Signature: edge_store(struct device * dev,struct device_attribute * attr,const char * buf,size_t size)
- Line: 311
- Calls: gpio_sysfs_free_irq, gpio_sysfs_request_irq, gpiod_line_state_notify

### export_gpio_desc
- Return type: static int
- Signature: export_gpio_desc(struct gpio_desc * desc)
- Line: 473
- Calls: gpiochip_line_is_valid, gpiod_export, gpiod_free, gpiod_hwgpio, gpiod_line_state_notify, gpiod_set_transitory
- Called by: export_store

### export_store
- Return type: static ssize_t
- Signature: export_store(const struct class * class,const struct class_attribute * attr,const char * buf,size_t len)
- Line: 604
- Calls: export_gpio_desc, gpio_to_desc

### gdev_get_data
- Return type: static gpiodev_data *
- Signature: gdev_get_data(struct gpio_device * gdev)
- Line: 680
- Called by: gpiochip_sysfs_unregister, gpiod_export, gpiod_unexport_unlocked

### gpio_is_visible
- Return type: static umode_t
- Signature: gpio_is_visible(struct kobject * kobj,struct attribute * attr,int n)
- Line: 400
- Calls: gpiod_to_irq

### gpio_sysfs_free_irq
- Return type: static void
- Signature: gpio_sysfs_free_irq(struct gpiod_data * data)
- Line: 273
- Calls: gpiochip_unlock_as_irq, gpiod_hwgpio
- Called by: edge_store, gpio_sysfs_set_active_low, gpiod_unexport_unlocked

### gpio_sysfs_irq
- Return type: static irqreturn_t
- Signature: gpio_sysfs_irq(int irq,void * priv)
- Line: 203

### gpio_sysfs_request_irq
- Return type: static int
- Signature: gpio_sysfs_request_irq(struct gpiod_data * data,unsigned char flags)
- Line: 213
- Calls: gpiochip_lock_as_irq, gpiochip_unlock_as_irq, gpiod_hwgpio, gpiod_to_irq
- Called by: edge_store, gpio_sysfs_set_active_low

### gpio_sysfs_set_active_low
- Return type: static int
- Signature: gpio_sysfs_set_active_low(struct gpiod_data * data,int value)
- Line: 344
- Calls: gpio_sysfs_free_irq, gpio_sysfs_request_irq, gpiod_line_state_notify
- Called by: active_low_store

### gpiochip_sysfs_register
- Return type: int
- Signature: gpiochip_sysfs_register(struct gpio_chip * gc)
- Line: 986
- Called by: gpiochip_setup_dev, gpiofind_sysfs_register

### gpiochip_sysfs_unregister
- Return type: void
- Signature: gpiochip_sysfs_unregister(struct gpio_chip * gc)
- Line: 1050
- Calls: gdev_get_data, gpiod_free, gpiod_unexport_unlocked
- Called by: gpiochip_remove

### gpiod_attr_init
- Return type: static void
- Signature: gpiod_attr_init(struct device_attribute * dev_attr,const char * name,ssize_t (* show)(struct device * dev,struct device_attribute * attr,char * buf),ssize_t (* store)(struct device * dev,struct device_attribute * attr,const char * buf,size_t count))
- Line: 696
- Called by: gpiod_export

### gpiod_export
- Return type: int
- Signature: gpiod_export(struct gpio_desc * desc,bool direction_may_change)
- Line: 727
- Calls: desc_to_gpio, gdev_get_data, gpiod_attr_init, gpiod_hwgpio
- Called by: export_gpio_desc, gpio_twl4030_probe

### gpiod_export_link
- Return type: int
- Signature: gpiod_export_link(struct device * dev,const char * name,struct gpio_desc * desc)
- Line: 896

### gpiod_unexport
- Return type: void
- Signature: gpiod_unexport(struct gpio_desc * desc)
- Line: 973
- Calls: gpiod_unexport_unlocked
- Called by: gpio_twl4030_power_off_action, unexport_gpio_desc

### gpiod_unexport_unlocked
- Return type: static void
- Signature: gpiod_unexport_unlocked(struct gpio_desc * desc)
- Line: 922
- Calls: gdev_get_data, gpio_sysfs_free_irq, gpiod_is_equal, gpiod_to_gpio_device
- Called by: gpiochip_sysfs_unregister, gpiod_unexport

### gpiofind_sysfs_register
- Return type: static int
- Signature: gpiofind_sysfs_register(struct gpio_chip * gc,const void * data)
- Line: 1080
- Calls: gpiochip_sysfs_register

### gpiolib_sysfs_init
- Return type: static int __init
- Signature: gpiolib_sysfs_init(void)
- Line: 1091
- Calls: gpio_device_find

### label_show
- Return type: static ssize_t
- Signature: label_show(struct device * dev,struct device_attribute * attr,char * buf)
- Line: 455

### match_export
- Return type: static int
- Signature: match_export(struct device * dev,const void * desc)
- Line: 876
- Calls: gpiod_is_equal

### match_gdev
- Return type: static int
- Signature: match_gdev(struct device * dev,const void * desc)
- Line: 671

### ngpio_show
- Return type: static ssize_t
- Signature: ngpio_show(struct device * dev,struct device_attribute * attr,char * buf)
- Line: 464

### unexport_gpio_desc
- Return type: static int
- Signature: unexport_gpio_desc(struct gpio_desc * desc)
- Line: 515
- Calls: gpiod_free, gpiod_unexport
- Called by: unexport_store

### unexport_store
- Return type: static ssize_t
- Signature: unexport_store(const struct class * class,const struct class_attribute * attr,const char * buf,size_t len)
- Line: 630
- Calls: gpio_to_desc, unexport_gpio_desc

### value_show
- Return type: static ssize_t
- Signature: value_show(struct device * dev,struct device_attribute * attr,char * buf)
- Line: 163
- Calls: gpiod_get_value_cansleep

### value_store
- Return type: static ssize_t
- Signature: value_store(struct device * dev,struct device_attribute * attr,const char * buf,size_t size)
- Line: 180
- Calls: gpiod_set_value_cansleep

## Structs (2)

### gpiod_data
- Line: 55
- Members:
  - list: list_head
  - desc: gpio_desc *
  - dev: device *
  - mutex: mutex
  - value_kn: kernfs_node *
  - irq: int
  - irq_flags: unsigned char
  - direction_can_change: bool
  - parent: kobject *
  - dir_attr: device_attribute
  - val_attr: device_attribute
  - edge_attr: device_attribute
  - active_low_attr: device_attribute
  - class_attrs: attribute * []
  - class_attr_group: attribute_group
  - class_attr_groups: const struct attribute_group * [2]
  - chip_attrs: attribute * []
  - chip_attr_group: attribute_group
  - chip_attr_groups: const struct attribute_group * [2]
  - exported_lines: list_head
  - gdev: gpio_device *
  - cdev_id: device *
  - cdev_base: device *

### gpiodev_data
- Line: 88
- Members:
  - list: list_head
  - desc: gpio_desc *
  - dev: device *
  - mutex: mutex
  - value_kn: kernfs_node *
  - irq: int
  - irq_flags: unsigned char
  - direction_can_change: bool
  - parent: kobject *
  - dir_attr: device_attribute
  - val_attr: device_attribute
  - edge_attr: device_attribute
  - active_low_attr: device_attribute
  - class_attrs: attribute * []
  - class_attr_group: attribute_group
  - class_attr_groups: const struct attribute_group * [2]
  - chip_attrs: attribute * []
  - chip_attr_group: attribute_group
  - chip_attr_groups: const struct attribute_group * [2]
  - exported_lines: list_head
  - gdev: gpio_device *
  - cdev_id: device *
  - cdev_base: device *

## Enums (2)

### __anon66c38bf70103
- Line: 37

### __anon66c38bf70203
- Line: 48

## Variables (7)

- static **dev_attr_export** : device_attribute (line 564)
- static **dev_attr_unexport** : device_attribute (line 574)
- static **gpio_class** : const struct class (line 664)
- static **gpio_class_attrs** : attribute * [] (line 656)
- static **gpiochip_attrs** : attribute * [] (line 579)
- static **gpiochip_ext_attrs** : attribute * [] (line 588)
- static **trigger_names** : const char * const[] (line 288)

## Macros (4)

- **GPIO_IRQF_TRIGGER_BOTH** (line 34)
- **GPIO_IRQF_TRIGGER_FALLING** (line 32)
- **GPIO_IRQF_TRIGGER_NONE** (line 31)
- **GPIO_IRQF_TRIGGER_RISING** (line 33)
