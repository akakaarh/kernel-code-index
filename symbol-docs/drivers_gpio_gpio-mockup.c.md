# drivers/gpio/gpio-mockup.c

Subsystem: drivers/gpio

## Functions (27)

### __gpio_mockup_get
- Return type: static int
- Signature: __gpio_mockup_get(struct gpio_mockup_chip * chip,unsigned int offset)
- Line: 86
- Called by: gpio_mockup_apply_pull, gpio_mockup_get, gpio_mockup_get_multiple

### __gpio_mockup_set
- Return type: static void
- Signature: __gpio_mockup_set(struct gpio_mockup_chip * chip,unsigned int offset,int value)
- Line: 119
- Called by: gpio_mockup_apply_pull, gpio_mockup_dirout, gpio_mockup_free, gpio_mockup_set, gpio_mockup_set_multiple

### gpio_mockup_apply_pull
- Return type: static int
- Signature: gpio_mockup_apply_pull(struct gpio_mockup_chip * chip,unsigned int offset,int value)
- Line: 151
- Calls: __gpio_mockup_get, __gpio_mockup_set
- Called by: gpio_mockup_debugfs_write, gpio_mockup_set_config

### gpio_mockup_debugfs_cleanup
- Return type: static void
- Signature: gpio_mockup_debugfs_cleanup(void * data)
- Line: 396

### gpio_mockup_debugfs_open
- Return type: static int
- Signature: gpio_mockup_debugfs_open(struct inode * inode,struct file * file)
- Line: 323

### gpio_mockup_debugfs_read
- Return type: static ssize_t
- Signature: gpio_mockup_debugfs_read(struct file * file,char __user * usr_buf,size_t size,loff_t * ppos)
- Line: 272
- Calls: gpio_mockup_get

### gpio_mockup_debugfs_setup
- Return type: static void
- Signature: gpio_mockup_debugfs_setup(struct device * dev,struct gpio_mockup_chip * chip)
- Line: 357
- Called by: gpio_mockup_probe

### gpio_mockup_debugfs_write
- Return type: static ssize_t
- Signature: gpio_mockup_debugfs_write(struct file * file,const char __user * usr_buf,size_t size,loff_t * ppos)
- Line: 297
- Calls: gpio_mockup_apply_pull

### gpio_mockup_dirin
- Return type: static int
- Signature: gpio_mockup_dirin(struct gpio_chip * gc,unsigned int offset)
- Line: 224
- Calls: gpiochip_get_data

### gpio_mockup_dirout
- Return type: static int
- Signature: gpio_mockup_dirout(struct gpio_chip * gc,unsigned int offset,int value)
- Line: 211
- Calls: __gpio_mockup_set, gpiochip_get_data

### gpio_mockup_dispose_mappings
- Return type: static void
- Signature: gpio_mockup_dispose_mappings(void * data)
- Line: 403

### gpio_mockup_exit
- Return type: static void __exit
- Signature: gpio_mockup_exit(void)
- Line: 621
- Calls: gpio_mockup_unregister_pdevs

### gpio_mockup_free
- Return type: static void
- Signature: gpio_mockup_free(struct gpio_chip * gc,unsigned int offset)
- Line: 262
- Calls: __gpio_mockup_set, gpiochip_get_data

### gpio_mockup_get
- Return type: static int
- Signature: gpio_mockup_get(struct gpio_chip * gc,unsigned int offset)
- Line: 92
- Calls: __gpio_mockup_get, gpiochip_get_data
- Called by: gpio_mockup_debugfs_read

### gpio_mockup_get_direction
- Return type: static int
- Signature: gpio_mockup_get_direction(struct gpio_chip * gc,unsigned int offset)
- Line: 234
- Calls: gpiochip_get_data

### gpio_mockup_get_multiple
- Return type: static int
- Signature: gpio_mockup_get_multiple(struct gpio_chip * gc,unsigned long * mask,unsigned long * bits)
- Line: 103
- Calls: __gpio_mockup_get, gpiochip_get_data

### gpio_mockup_init
- Return type: static int __init
- Signature: gpio_mockup_init(void)
- Line: 579
- Calls: gpio_mockup_range_ngpio, gpio_mockup_register_chip, gpio_mockup_unregister_pdevs

### gpio_mockup_probe
- Return type: static int
- Signature: gpio_mockup_probe(struct platform_device * pdev)
- Line: 416
- Calls: gpio_mockup_debugfs_setup

### gpio_mockup_range_base
- Return type: static int
- Signature: gpio_mockup_range_base(unsigned int index)
- Line: 76
- Called by: gpio_mockup_register_chip

### gpio_mockup_range_ngpio
- Return type: static int
- Signature: gpio_mockup_range_ngpio(unsigned int index)
- Line: 81
- Called by: gpio_mockup_init, gpio_mockup_register_chip

### gpio_mockup_register_chip
- Return type: static int __init
- Signature: gpio_mockup_register_chip(int idx)
- Line: 522
- Calls: gpio_mockup_range_base, gpio_mockup_range_ngpio
- Called by: gpio_mockup_init

### gpio_mockup_request
- Return type: static int
- Signature: gpio_mockup_request(struct gpio_chip * gc,unsigned int offset)
- Line: 252
- Calls: gpiochip_get_data

### gpio_mockup_set
- Return type: static int
- Signature: gpio_mockup_set(struct gpio_chip * gc,unsigned int offset,int value)
- Line: 125
- Calls: __gpio_mockup_set, gpiochip_get_data

### gpio_mockup_set_config
- Return type: static int
- Signature: gpio_mockup_set_config(struct gpio_chip * gc,unsigned int offset,unsigned long config)
- Line: 195
- Calls: gpio_mockup_apply_pull, gpiochip_get_data

### gpio_mockup_set_multiple
- Return type: static int
- Signature: gpio_mockup_set_multiple(struct gpio_chip * gc,unsigned long * mask,unsigned long * bits)
- Line: 137
- Calls: __gpio_mockup_set, gpiochip_get_data

### gpio_mockup_to_irq
- Return type: static int
- Signature: gpio_mockup_to_irq(struct gpio_chip * gc,unsigned int offset)
- Line: 245
- Calls: gpiochip_get_data

### gpio_mockup_unregister_pdevs
- Return type: static void
- Signature: gpio_mockup_unregister_pdevs(void)
- Line: 505
- Called by: gpio_mockup_exit, gpio_mockup_init

## Structs (3)

### gpio_mockup_chip
- Line: 53
- Members:
  - dir: int
  - value: int
  - pull: int
  - requested: bool
  - gc: gpio_chip
  - lines: gpio_mockup_line_status *
  - irq_sim_domain: irq_domain *
  - dbg_dir: dentry *
  - lock: mutex
  - chip: gpio_mockup_chip *
  - offset: unsigned int

### gpio_mockup_dbgfs_private
- Line: 61
- Members:
  - dir: int
  - value: int
  - pull: int
  - requested: bool
  - gc: gpio_chip
  - lines: gpio_mockup_line_status *
  - irq_sim_domain: irq_domain *
  - dbg_dir: dentry *
  - lock: mutex
  - chip: gpio_mockup_chip *
  - offset: unsigned int

### gpio_mockup_line_status
- Line: 46
- Members:
  - dir: int
  - value: int
  - pull: int
  - requested: bool
  - gc: gpio_chip
  - lines: gpio_mockup_line_status *
  - irq_sim_domain: irq_domain *
  - dbg_dir: dentry *
  - lock: mutex
  - chip: gpio_mockup_chip *
  - offset: unsigned int

## Variables (8)

- static **gpio_mockup_dbg_dir** : dentry * (line 74)
- static **gpio_mockup_debugfs_ops** : const struct file_operations (line 349)
- static **gpio_mockup_driver** : platform_driver (line 495)
- static **gpio_mockup_named_lines** : bool (line 70)
- static **gpio_mockup_num_ranges** : int (line 67)
- static **gpio_mockup_of_match** : const struct of_device_id[] (line 489)
- static **gpio_mockup_pdevs** : platform_device * [] (line 503)
- static **gpio_mockup_ranges** : int[] (line 66)

## Macros (4)

- **GPIO_MOCKUP_MAX_GC** (line 29)
- **GPIO_MOCKUP_MAX_PROP** (line 36)
- **GPIO_MOCKUP_MAX_RANGES** (line 34)
- **pr_fmt**(fmt) (line 10)
