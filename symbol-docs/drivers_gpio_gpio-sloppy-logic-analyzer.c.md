# drivers/gpio/gpio-sloppy-logic-analyzer.c

Subsystem: drivers/gpio

## Functions (10)

### fops_buf_size_get
- Return type: static int
- Signature: fops_buf_size_get(void * data,u64 * val)
- Line: 155

### fops_buf_size_set
- Return type: static int
- Signature: fops_buf_size_set(void * data,u64 val)
- Line: 164
- Called by: gpio_la_poll_probe

### fops_capture_set
- Return type: static int
- Signature: fops_capture_set(void * data,u64 val)
- Line: 68
- Calls: gpio_la_get_array

### gpio_la_get_array
- Return type: static __always_inline int
- Signature: gpio_la_get_array(struct gpio_descs * d,unsigned long * sptr)
- Line: 57
- Calls: gpiod_get_array_value
- Called by: fops_capture_set

### gpio_la_poll_exit
- Return type: static void __exit
- Signature: gpio_la_poll_exit(void)
- Line: 336

### gpio_la_poll_init
- Return type: static int __init
- Signature: gpio_la_poll_init(void)
- Line: 323

### gpio_la_poll_probe
- Return type: static int
- Signature: gpio_la_poll_probe(struct platform_device * pdev)
- Line: 223
- Calls: devm_gpiod_get_array, fops_buf_size_set, gpiod_cansleep, gpiod_set_consumer_name

### gpio_la_poll_remove
- Return type: static void
- Signature: gpio_la_poll_remove(struct platform_device * pdev)
- Line: 299

### trigger_open
- Return type: static int
- Signature: trigger_open(struct inode * inode,struct file * file)
- Line: 190

### trigger_write
- Return type: static ssize_t
- Signature: trigger_write(struct file * file,const char __user * ubuf,size_t count,loff_t * offset)
- Line: 195

## Structs (1)

### gpio_la_poll_priv
- Line: 40
- Members:
  - blob_lock: mutex
  - buf_idx: u32
  - descs: gpio_descs *
  - delay_ns: unsigned long
  - acq_delay: unsigned long
  - blob: debugfs_blob_wrapper
  - debug_dir: dentry *
  - blob_dent: dentry *
  - meta: debugfs_blob_wrapper
  - dev: device *
  - trig_len: unsigned int
  - trig_data: u8 *

## Variables (4)

- static **fops_trigger** : const struct file_operations (line 216)
- static **gpio_la_poll_debug_dir** : dentry * (line 55)
- static **gpio_la_poll_device_driver** : platform_driver (line 314)
- static **gpio_la_poll_of_match** : const struct of_device_id[] (line 308)

## Macros (4)

- **GPIO_LA_DEFAULT_BUF_SIZE** (line 35)
- **GPIO_LA_MAX_PROBES** (line 37)
- **GPIO_LA_NAME** (line 34)
- **GPIO_LA_NUM_TESTS** (line 38)
