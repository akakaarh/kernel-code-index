# drivers/gpio/gpiolib-cdev.c

Subsystem: drivers/gpio

## Functions (75)

### chipinfo_get
- Return type: static int
- Signature: chipinfo_get(struct gpio_chardev_data * cdev,void __user * ip)
- Line: 2276
- Called by: gpio_ioctl

### debounce_irq_handler
- Return type: static irqreturn_t
- Signature: debounce_irq_handler(int irq,void * p)
- Line: 816

### debounce_setup
- Return type: static int
- Signature: debounce_setup(struct line * line,unsigned int debounce_period_us)
- Line: 895
- Calls: free_irq_label, gpio_do_set_config, gpiod_get_raw_value_cansleep, gpiod_to_irq, hte_edge_setup, make_irq_label
- Called by: edge_detector_setup

### debounce_work_func
- Return type: static void
- Signature: debounce_work_func(struct work_struct * work)
- Line: 826
- Calls: gpiod_get_raw_value_cansleep, gpiod_hwgpio, line_event_id, line_event_timestamp, linereq_put_event

### debounced_value
- Return type: static bool
- Signature: debounced_value(struct line * line)
- Line: 799
- Called by: linereq_get_values

### edge_detector_fifo_init
- Return type: static int
- Signature: edge_detector_fifo_init(struct linereq * req)
- Line: 995
- Called by: edge_detector_setup, edge_detector_update

### edge_detector_setup
- Return type: static int
- Signature: edge_detector_setup(struct line * line,struct gpio_v2_line_config * lc,unsigned int line_idx,u64 edflags)
- Line: 1003
- Calls: debounce_setup, edge_detector_fifo_init, free_irq_label, gpio_v2_line_config_debounce_period, gpio_v2_line_config_debounced, gpiod_to_irq, hte_edge_setup, make_irq_label
- Called by: edge_detector_update, linereq_create

### edge_detector_stop
- Return type: static void
- Signature: edge_detector_stop(struct line * line)
- Line: 975
- Calls: free_irq_label
- Called by: edge_detector_update, linereq_free, linereq_set_config

### edge_detector_update
- Return type: static int
- Signature: edge_detector_update(struct line * line,struct gpio_v2_line_config * lc,unsigned int line_idx,u64 edflags)
- Line: 1063
- Calls: edge_detector_fifo_init, edge_detector_setup, edge_detector_stop, gpio_v2_line_config_debounce_period
- Called by: linereq_set_config

### edge_irq_handler
- Return type: static irqreturn_t
- Signature: edge_irq_handler(int irq,void * p)
- Line: 779
- Calls: line_event_timestamp

### edge_irq_thread
- Return type: static irqreturn_t
- Signature: edge_irq_thread(int irq,void * p)
- Line: 733
- Calls: gpiod_get_value_cansleep, gpiod_hwgpio, line_event_id, line_event_timestamp, linereq_put_event

### free_irq_label
- Return type: static void
- Signature: free_irq_label(const char * label)
- Line: 607
- Called by: debounce_setup, edge_detector_setup, edge_detector_stop, lineevent_create, lineevent_free

### gpio_chrdev_open
- Return type: static int
- Signature: gpio_chrdev_open(struct inode * inode,struct file * file)
- Line: 2649
- Calls: gpio_device_get, gpio_device_put

### gpio_chrdev_release
- Return type: static int
- Signature: gpio_chrdev_release(struct inode * inode,struct file * file)
- Line: 2714
- Calls: gpio_device_put

### gpio_desc_to_lineinfo
- Return type: static void
- Signature: gpio_desc_to_lineinfo(struct gpio_desc * desc,struct gpio_v2_line_info * info,bool atomic)
- Line: 2175
- Calls: gpiochip_line_is_valid, gpiod_get_label, gpiod_hwgpio
- Called by: lineinfo_changed_notify, lineinfo_get, lineinfo_get_v1

### gpio_device_unregistered_notify
- Return type: static int
- Signature: gpio_device_unregistered_notify(struct notifier_block * nb,unsigned long action,void * data)
- Line: 2533

### gpio_ioctl
- Return type: static long
- Signature: gpio_ioctl(struct file * file,unsigned int cmd,unsigned long arg)
- Line: 2396
- Calls: chipinfo_get, lineevent_create, linehandle_create, lineinfo_get, lineinfo_get_v1, lineinfo_unwatch, linereq_create
- Called by: gpio_ioctl_compat

### gpio_ioctl_compat
- Return type: static long
- Signature: gpio_ioctl_compat(struct file * file,unsigned int cmd,unsigned long arg)
- Line: 2436
- Calls: gpio_ioctl

### gpio_v2_line_config_debounce_period
- Return type: static u32
- Signature: gpio_v2_line_config_debounce_period(struct gpio_v2_line_config * lc,unsigned int line_idx)
- Line: 961
- Called by: edge_detector_setup, edge_detector_update

### gpio_v2_line_config_debounced
- Return type: static bool
- Signature: gpio_v2_line_config_debounced(struct gpio_v2_line_config * lc,unsigned int line_idx)
- Line: 947
- Called by: edge_detector_setup, gpio_v2_line_config_validate

### gpio_v2_line_config_flags
- Return type: static u64
- Signature: gpio_v2_line_config_flags(struct gpio_v2_line_config * lc,unsigned int line_idx)
- Line: 1097
- Called by: gpio_v2_line_config_validate, linereq_create, linereq_set_config

### gpio_v2_line_config_flags_to_desc_flags
- Return type: static void
- Signature: gpio_v2_line_config_flags_to_desc_flags(u64 lflags,unsigned long * flagsp)
- Line: 1224
- Called by: linereq_create, linereq_set_config

### gpio_v2_line_config_output_value
- Return type: static int
- Signature: gpio_v2_line_config_output_value(struct gpio_v2_line_config * lc,unsigned int line_idx)
- Line: 1111
- Called by: linereq_create, linereq_set_config

### gpio_v2_line_config_validate
- Return type: static int
- Signature: gpio_v2_line_config_validate(struct gpio_v2_line_config * lc,unsigned int num_lines)
- Line: 1184
- Calls: gpio_v2_line_config_debounced, gpio_v2_line_config_flags, gpio_v2_line_flags_validate
- Called by: linereq_create, linereq_set_config

### gpio_v2_line_flags_validate
- Return type: static int
- Signature: gpio_v2_line_flags_validate(u64 flags)
- Line: 1125
- Called by: gpio_v2_line_config_validate

### gpio_v2_line_info_changed_to_v1
- Return type: static void
- Signature: gpio_v2_line_info_changed_to_v1(struct gpio_v2_line_info_changed * lic_v2,struct gpioline_info_changed * lic_v1)
- Line: 2163
- Calls: gpio_v2_line_info_to_v1
- Called by: lineinfo_watch_read

### gpio_v2_line_info_to_v1
- Return type: static void
- Signature: gpio_v2_line_info_to_v1(struct gpio_v2_line_info * info_v2,struct gpioline_info * info_v1)
- Line: 2131
- Called by: gpio_v2_line_info_changed_to_v1, lineinfo_get_v1

### gpiolib_cdev_register
- Return type: int
- Signature: gpiolib_cdev_register(struct gpio_chip * gc,dev_t devt)
- Line: 2743

### gpiolib_cdev_unregister
- Return type: void
- Signature: gpiolib_cdev_unregister(struct gpio_device * gdev)
- Line: 2768

### hte_edge_setup
- Return type: static int
- Signature: hte_edge_setup(struct line * line,u64 eflags)
- Line: 697
- Calls: desc_to_gpio
- Called by: debounce_setup, edge_detector_setup

### hte_edge_setup
- Return type: static int
- Signature: hte_edge_setup(struct line * line,u64 eflags)
- Line: 727
- Calls: desc_to_gpio
- Called by: debounce_setup, edge_detector_setup

### line_event_id
- Return type: static u32
- Signature: line_event_id(int level)
- Line: 587
- Called by: debounce_work_func, edge_irq_thread, process_hw_ts_thread

### line_event_timestamp
- Return type: static u64
- Signature: line_event_timestamp(struct line * line)
- Line: 576
- Called by: debounce_work_func, edge_irq_handler, edge_irq_thread

### lineevent_create
- Return type: static DEFINE_FREE (lineevent_free,struct lineevent_state *,if (!IS_ERR_OR_NULL (_T))lineevent_free (_T))int
- Signature: lineevent_create(struct gpio_device * gdev,void __user * ip)
- Line: 2006
- Calls: free_irq_label, gpio_device_get, gpio_device_get_desc, gpiod_direction_input, gpiod_line_state_notify, gpiod_to_irq, linehandle_flags_to_desc_flags, make_irq_label
- Called by: gpio_ioctl

### lineevent_free
- Return type: static void
- Signature: lineevent_free(struct lineevent_state * le)
- Line: 1869
- Calls: free_irq_label, gpio_device_put, gpiod_free
- Called by: lineevent_release

### lineevent_ioctl
- Return type: static long
- Signature: lineevent_ioctl(struct file * file,unsigned int cmd,unsigned long arg)
- Line: 1889
- Calls: gpiod_get_value_cansleep
- Called by: lineevent_ioctl_compat

### lineevent_ioctl_compat
- Return type: static long
- Signature: lineevent_ioctl_compat(struct file * file,unsigned int cmd,unsigned long arg)
- Line: 1924
- Calls: lineevent_ioctl

### lineevent_irq_handler
- Return type: static irqreturn_t
- Signature: lineevent_irq_handler(int irq,void * p)
- Line: 1991

### lineevent_irq_thread
- Return type: static irqreturn_t
- Signature: lineevent_irq_thread(int irq,void * p)
- Line: 1943
- Calls: gpiod_get_value_cansleep

### lineevent_poll
- Return type: static __poll_t
- Signature: lineevent_poll(struct file * file,struct poll_table_struct * wait)
- Line: 1770

### lineevent_read
- Return type: static ssize_t
- Signature: lineevent_read(struct file * file,char __user * buf,size_t count,loff_t * f_ps)
- Line: 1805

### lineevent_release
- Return type: static int
- Signature: lineevent_release(struct inode * inode,struct file * file)
- Line: 1883
- Calls: lineevent_free

### lineevent_unregistered_notify
- Return type: static int
- Signature: lineevent_unregistered_notify(struct notifier_block * nb,unsigned long action,void * data)
- Line: 1789

### linehandle_create
- Return type: static DEFINE_FREE (linehandle_free,struct linehandle_state *,if (!IS_ERR_OR_NULL (_T))linehandle_free (_T))int
- Signature: linehandle_create(struct gpio_device * gdev,void __user * ip)
- Line: 303
- Calls: gpio_device_get, gpio_device_get_desc, gpiod_direction_input_nonotify, gpiod_direction_output_nonotify, gpiod_line_state_notify, gpiod_set_transitory, linehandle_flags_to_desc_flags, linehandle_validate_flags
- Called by: gpio_ioctl

### linehandle_flags_to_desc_flags
- Return type: static void
- Signature: linehandle_flags_to_desc_flags(u32 lflags,unsigned long * flagsp)
- Line: 143
- Called by: lineevent_create, linehandle_create, linehandle_set_config

### linehandle_free
- Return type: static void
- Signature: linehandle_free(struct linehandle_state * lh)
- Line: 273
- Calls: gpio_device_put, gpiod_free
- Called by: linehandle_release

### linehandle_ioctl
- Return type: static long
- Signature: linehandle_ioctl(struct file * file,unsigned int cmd,unsigned long arg)
- Line: 204
- Calls: gpiod_get_array_value_complex, gpiod_set_array_value_complex, linehandle_set_config
- Called by: linehandle_ioctl_compat

### linehandle_ioctl_compat
- Return type: static long
- Signature: linehandle_ioctl_compat(struct file * file,unsigned int cmd,unsigned long arg)
- Line: 266
- Calls: linehandle_ioctl

### linehandle_release
- Return type: static int
- Signature: linehandle_release(struct inode * inode,struct file * file)
- Line: 285
- Calls: linehandle_free

### linehandle_set_config
- Return type: static long
- Signature: linehandle_set_config(struct linehandle_state * lh,void __user * ip)
- Line: 163
- Calls: gpiod_direction_input_nonotify, gpiod_direction_output_nonotify, gpiod_line_state_notify, linehandle_flags_to_desc_flags, linehandle_validate_flags
- Called by: linehandle_ioctl

### linehandle_validate_flags
- Return type: static int
- Signature: linehandle_validate_flags(u32 flags)
- Line: 95
- Called by: linehandle_create, linehandle_set_config

### lineinfo_changed_func
- Return type: static void
- Signature: lineinfo_changed_func(struct work_struct * work)
- Line: 2450
- Calls: gpio_device_put

### lineinfo_changed_notify
- Return type: static int
- Signature: lineinfo_changed_notify(struct notifier_block * nb,unsigned long action,void * data)
- Line: 2484
- Calls: gpio_desc_to_lineinfo, gpio_device_get, gpiod_hwgpio

### lineinfo_ensure_abi_version
- Return type: static int
- Signature: lineinfo_ensure_abi_version(struct gpio_chardev_data * cdata,unsigned int version)
- Line: 2295
- Called by: lineinfo_get, lineinfo_get_v1

### lineinfo_get
- Return type: static int
- Signature: lineinfo_get(struct gpio_chardev_data * cdev,void __user * ip,bool watch)
- Line: 2342
- Calls: gpio_desc_to_lineinfo, gpio_device_get_desc, lineinfo_ensure_abi_version
- Called by: gpio_ioctl

### lineinfo_get_v1
- Return type: static int
- Signature: lineinfo_get_v1(struct gpio_chardev_data * cdev,void __user * ip,bool watch)
- Line: 2306
- Calls: gpio_desc_to_lineinfo, gpio_device_get_desc, gpio_v2_line_info_to_v1, lineinfo_ensure_abi_version
- Called by: gpio_ioctl

### lineinfo_unwatch
- Return type: static int
- Signature: lineinfo_unwatch(struct gpio_chardev_data * cdev,void __user * ip)
- Line: 2377
- Called by: gpio_ioctl

### lineinfo_watch_poll
- Return type: static __poll_t
- Signature: lineinfo_watch_poll(struct file * file,struct poll_table_struct * pollt)
- Line: 2545

### lineinfo_watch_read
- Return type: static ssize_t
- Signature: lineinfo_watch_read(struct file * file,char __user * buf,size_t count,loff_t * off)
- Line: 2565
- Calls: gpio_v2_line_info_changed_to_v1

### linereq_create
- Return type: static DEFINE_FREE (linereq_free,struct linereq *,if (!IS_ERR_OR_NULL (_T))linereq_free (_T))int
- Signature: linereq_create(struct gpio_device * gdev,void __user * ip)
- Line: 1604
- Calls: edge_detector_setup, gpio_device_get, gpio_device_get_desc, gpio_v2_line_config_flags, gpio_v2_line_config_flags_to_desc_flags, gpio_v2_line_config_output_value, gpio_v2_line_config_validate, gpiod_direction_input_nonotify, gpiod_direction_output_nonotify, gpiod_line_state_notify, gpiod_set_transitory
- Called by: gpio_ioctl

### linereq_free
- Return type: static void
- Signature: linereq_free(struct linereq * lr)
- Line: 1544
- Calls: edge_detector_stop, gpio_device_put, gpiod_free
- Called by: linereq_release

### linereq_get_values
- Return type: static long
- Signature: linereq_get_values(struct linereq * lr,void __user * ip)
- Line: 1262
- Calls: debounced_value, gpiod_get_array_value_complex
- Called by: linereq_ioctl

### linereq_ioctl
- Return type: static long
- Signature: linereq_ioctl(struct file * file,unsigned int cmd,unsigned long arg)
- Line: 1443
- Calls: linereq_get_values, linereq_set_config, linereq_set_values
- Called by: linereq_ioctl_compat

### linereq_ioctl_compat
- Return type: static long
- Signature: linereq_ioctl_compat(struct file * file,unsigned int cmd,unsigned long arg)
- Line: 1467
- Calls: linereq_ioctl

### linereq_poll
- Return type: static __poll_t
- Signature: linereq_poll(struct file * file,struct poll_table_struct * wait)
- Line: 1474

### linereq_put_event
- Return type: static void
- Signature: linereq_put_event(struct linereq * lr,struct gpio_v2_line_event * le)
- Line: 558
- Called by: debounce_work_func, edge_irq_thread, process_hw_ts_thread

### linereq_read
- Return type: static ssize_t
- Signature: linereq_read(struct file * file,char __user * buf,size_t count,loff_t * f_ps)
- Line: 1494

### linereq_release
- Return type: static int
- Signature: linereq_release(struct inode * inode,struct file * file)
- Line: 1564
- Calls: linereq_free

### linereq_set_config
- Return type: static long
- Signature: linereq_set_config(struct linereq * lr,void __user * ip)
- Line: 1389
- Calls: edge_detector_stop, edge_detector_update, gpio_v2_line_config_flags, gpio_v2_line_config_flags_to_desc_flags, gpio_v2_line_config_output_value, gpio_v2_line_config_validate, gpiod_direction_input_nonotify, gpiod_direction_output_nonotify, gpiod_line_state_notify
- Called by: linereq_ioctl

### linereq_set_values
- Return type: static long
- Signature: linereq_set_values(struct linereq * lr,void __user * ip)
- Line: 1334
- Calls: gpiod_set_array_value_complex
- Called by: linereq_ioctl

### linereq_show_fdinfo
- Return type: static void
- Signature: linereq_show_fdinfo(struct seq_file * out,struct file * file)
- Line: 1573
- Calls: gpiod_hwgpio

### linereq_unregistered_notify
- Return type: static int
- Signature: linereq_unregistered_notify(struct notifier_block * nb,unsigned long action,void * data)
- Line: 547

### make_irq_label
- Return type: static char *
- Signature: make_irq_label(const char * orig)
- Line: 593
- Called by: debounce_setup, edge_detector_setup, lineevent_create

### process_hw_ts
- Return type: static hte_return
- Signature: process_hw_ts(struct hte_ts_data * ts,void * p)
- Line: 662

### process_hw_ts_thread
- Return type: static hte_return
- Signature: process_hw_ts_thread(void * p)
- Line: 614
- Calls: gpiod_get_raw_value_cansleep, gpiod_hwgpio, line_event_id, linereq_put_event

## Structs (7)

### compat_gpioeevent_data
- Line: 1800
- Members:
  - gdev: gpio_device *
  - label: const char *
  - descs: gpio_desc * []
  - num_descs: u32
  - desc: gpio_desc *
  - req: linereq *
  - irq: unsigned int
  - edflags: u64
  - timestamp_ns: u64
  - req_seqno: u32
  - line_seqno: u32
  - work: delayed_work
  - sw_debounced: unsigned int
  - level: unsigned int
  - hdesc: hte_ts_desc
  - raw_level: int
  - total_discard_seq: u32
  - last_seqno: u32
  - gdev: gpio_device *
  - label: const char *
  - num_lines: u32
  - wait: wait_queue_head_t
  - device_unregistered_nb: notifier_block
  - event_buffer_size: u32
  - seqno: atomic_t
  - config_mutex: mutex
  - gdev: gpio_device *
  - label: const char *
  - desc: gpio_desc *
  - eflags: u32
  - irq: int
  - wait: wait_queue_head_t
  - device_unregistered_nb: notifier_block
  - timestamp: u64
  - timestamp: compat_u64
  - id: u32
  - gdev: gpio_device *
  - wait: wait_queue_head_t
  - lineinfo_changed_nb: notifier_block
  - device_unregistered_nb: notifier_block
  - watched_lines: unsigned long *
  - watch_abi_version: atomic_t
  - fp: file *
  - work: work_struct
  - chg: gpio_v2_line_info_changed
  - gdev: gpio_device *
  - cdev: gpio_chardev_data *

### gpio_chardev_data
- Line: 2263
- Members:
  - gdev: gpio_device *
  - label: const char *
  - descs: gpio_desc * []
  - num_descs: u32
  - desc: gpio_desc *
  - req: linereq *
  - irq: unsigned int
  - edflags: u64
  - timestamp_ns: u64
  - req_seqno: u32
  - line_seqno: u32
  - work: delayed_work
  - sw_debounced: unsigned int
  - level: unsigned int
  - hdesc: hte_ts_desc
  - raw_level: int
  - total_discard_seq: u32
  - last_seqno: u32
  - gdev: gpio_device *
  - label: const char *
  - num_lines: u32
  - wait: wait_queue_head_t
  - device_unregistered_nb: notifier_block
  - event_buffer_size: u32
  - seqno: atomic_t
  - config_mutex: mutex
  - gdev: gpio_device *
  - label: const char *
  - desc: gpio_desc *
  - eflags: u32
  - irq: int
  - wait: wait_queue_head_t
  - device_unregistered_nb: notifier_block
  - timestamp: u64
  - timestamp: compat_u64
  - id: u32
  - gdev: gpio_device *
  - wait: wait_queue_head_t
  - lineinfo_changed_nb: notifier_block
  - device_unregistered_nb: notifier_block
  - watched_lines: unsigned long *
  - watch_abi_version: atomic_t
  - fp: file *
  - work: work_struct
  - chg: gpio_v2_line_info_changed
  - gdev: gpio_device *
  - cdev: gpio_chardev_data *

### line
- Line: 418
- Members:
  - gdev: gpio_device *
  - label: const char *
  - descs: gpio_desc * []
  - num_descs: u32
  - desc: gpio_desc *
  - req: linereq *
  - irq: unsigned int
  - edflags: u64
  - timestamp_ns: u64
  - req_seqno: u32
  - line_seqno: u32
  - work: delayed_work
  - sw_debounced: unsigned int
  - level: unsigned int
  - hdesc: hte_ts_desc
  - raw_level: int
  - total_discard_seq: u32
  - last_seqno: u32
  - gdev: gpio_device *
  - label: const char *
  - num_lines: u32
  - wait: wait_queue_head_t
  - device_unregistered_nb: notifier_block
  - event_buffer_size: u32
  - seqno: atomic_t
  - config_mutex: mutex
  - gdev: gpio_device *
  - label: const char *
  - desc: gpio_desc *
  - eflags: u32
  - irq: int
  - wait: wait_queue_head_t
  - device_unregistered_nb: notifier_block
  - timestamp: u64
  - timestamp: compat_u64
  - id: u32
  - gdev: gpio_device *
  - wait: wait_queue_head_t
  - lineinfo_changed_nb: notifier_block
  - device_unregistered_nb: notifier_block
  - watched_lines: unsigned long *
  - watch_abi_version: atomic_t
  - fp: file *
  - work: work_struct
  - chg: gpio_v2_line_info_changed
  - gdev: gpio_device *
  - cdev: gpio_chardev_data *

### lineevent_state
- Line: 1754
- Members:
  - gdev: gpio_device *
  - label: const char *
  - descs: gpio_desc * []
  - num_descs: u32
  - desc: gpio_desc *
  - req: linereq *
  - irq: unsigned int
  - edflags: u64
  - timestamp_ns: u64
  - req_seqno: u32
  - line_seqno: u32
  - work: delayed_work
  - sw_debounced: unsigned int
  - level: unsigned int
  - hdesc: hte_ts_desc
  - raw_level: int
  - total_discard_seq: u32
  - last_seqno: u32
  - gdev: gpio_device *
  - label: const char *
  - num_lines: u32
  - wait: wait_queue_head_t
  - device_unregistered_nb: notifier_block
  - event_buffer_size: u32
  - seqno: atomic_t
  - config_mutex: mutex
  - gdev: gpio_device *
  - label: const char *
  - desc: gpio_desc *
  - eflags: u32
  - irq: int
  - wait: wait_queue_head_t
  - device_unregistered_nb: notifier_block
  - timestamp: u64
  - timestamp: compat_u64
  - id: u32
  - gdev: gpio_device *
  - wait: wait_queue_head_t
  - lineinfo_changed_nb: notifier_block
  - device_unregistered_nb: notifier_block
  - watched_lines: unsigned long *
  - watch_abi_version: atomic_t
  - fp: file *
  - work: work_struct
  - chg: gpio_v2_line_info_changed
  - gdev: gpio_device *
  - cdev: gpio_chardev_data *

### linehandle_state
- Line: 74
- Members:
  - gdev: gpio_device *
  - label: const char *
  - descs: gpio_desc * []
  - num_descs: u32
  - desc: gpio_desc *
  - req: linereq *
  - irq: unsigned int
  - edflags: u64
  - timestamp_ns: u64
  - req_seqno: u32
  - line_seqno: u32
  - work: delayed_work
  - sw_debounced: unsigned int
  - level: unsigned int
  - hdesc: hte_ts_desc
  - raw_level: int
  - total_discard_seq: u32
  - last_seqno: u32
  - gdev: gpio_device *
  - label: const char *
  - num_lines: u32
  - wait: wait_queue_head_t
  - device_unregistered_nb: notifier_block
  - event_buffer_size: u32
  - seqno: atomic_t
  - config_mutex: mutex
  - gdev: gpio_device *
  - label: const char *
  - desc: gpio_desc *
  - eflags: u32
  - irq: int
  - wait: wait_queue_head_t
  - device_unregistered_nb: notifier_block
  - timestamp: u64
  - timestamp: compat_u64
  - id: u32
  - gdev: gpio_device *
  - wait: wait_queue_head_t
  - lineinfo_changed_nb: notifier_block
  - device_unregistered_nb: notifier_block
  - watched_lines: unsigned long *
  - watch_abi_version: atomic_t
  - fp: file *
  - work: work_struct
  - chg: gpio_v2_line_info_changed
  - gdev: gpio_device *
  - cdev: gpio_chardev_data *

### lineinfo_changed_ctx
- Line: 2443
- Members:
  - gdev: gpio_device *
  - label: const char *
  - descs: gpio_desc * []
  - num_descs: u32
  - desc: gpio_desc *
  - req: linereq *
  - irq: unsigned int
  - edflags: u64
  - timestamp_ns: u64
  - req_seqno: u32
  - line_seqno: u32
  - work: delayed_work
  - sw_debounced: unsigned int
  - level: unsigned int
  - hdesc: hte_ts_desc
  - raw_level: int
  - total_discard_seq: u32
  - last_seqno: u32
  - gdev: gpio_device *
  - label: const char *
  - num_lines: u32
  - wait: wait_queue_head_t
  - device_unregistered_nb: notifier_block
  - event_buffer_size: u32
  - seqno: atomic_t
  - config_mutex: mutex
  - gdev: gpio_device *
  - label: const char *
  - desc: gpio_desc *
  - eflags: u32
  - irq: int
  - wait: wait_queue_head_t
  - device_unregistered_nb: notifier_block
  - timestamp: u64
  - timestamp: compat_u64
  - id: u32
  - gdev: gpio_device *
  - wait: wait_queue_head_t
  - lineinfo_changed_nb: notifier_block
  - device_unregistered_nb: notifier_block
  - watched_lines: unsigned long *
  - watch_abi_version: atomic_t
  - fp: file *
  - work: work_struct
  - chg: gpio_v2_line_info_changed
  - gdev: gpio_device *
  - cdev: gpio_chardev_data *

### linereq
- Line: 500
- Members:
  - gdev: gpio_device *
  - label: const char *
  - descs: gpio_desc * []
  - num_descs: u32
  - desc: gpio_desc *
  - req: linereq *
  - irq: unsigned int
  - edflags: u64
  - timestamp_ns: u64
  - req_seqno: u32
  - line_seqno: u32
  - work: delayed_work
  - sw_debounced: unsigned int
  - level: unsigned int
  - hdesc: hte_ts_desc
  - raw_level: int
  - total_discard_seq: u32
  - last_seqno: u32
  - gdev: gpio_device *
  - label: const char *
  - num_lines: u32
  - wait: wait_queue_head_t
  - device_unregistered_nb: notifier_block
  - event_buffer_size: u32
  - seqno: atomic_t
  - config_mutex: mutex
  - gdev: gpio_device *
  - label: const char *
  - desc: gpio_desc *
  - eflags: u32
  - irq: int
  - wait: wait_queue_head_t
  - device_unregistered_nb: notifier_block
  - timestamp: u64
  - timestamp: compat_u64
  - id: u32
  - gdev: gpio_device *
  - wait: wait_queue_head_t
  - lineinfo_changed_nb: notifier_block
  - device_unregistered_nb: notifier_block
  - watched_lines: unsigned long *
  - watch_abi_version: atomic_t
  - fp: file *
  - work: work_struct
  - chg: gpio_v2_line_info_changed
  - gdev: gpio_device *
  - cdev: gpio_chardev_data *

## Variables (4)

- static **gpio_fileops** : const struct file_operations (line 2731)
- static **line_fileops** : const struct file_operations (line 1587)
- static **lineevent_fileops** : const struct file_operations (line 1931)
- static **linehandle_fileops** : const struct file_operations (line 291)

## Macros (10)

- **GPIOEVENT_REQUEST_VALID_FLAGS** (line 1766)
- **GPIOHANDLE_REQUEST_DIRECTION_FLAGS** (line 91)
- **GPIOHANDLE_REQUEST_VALID_FLAGS** (line 81)
- **GPIO_V2_LINE_BIAS_FLAGS** (line 513)
- **GPIO_V2_LINE_DIRECTION_FLAGS** (line 518)
- **GPIO_V2_LINE_DRIVE_FLAGS** (line 522)
- **GPIO_V2_LINE_EDGE_DETECTOR_FLAGS** (line 542)
- **GPIO_V2_LINE_EDGE_FLAGS** (line 526)
- **GPIO_V2_LINE_FLAG_EDGE_BOTH** (line 530)
- **GPIO_V2_LINE_VALID_FLAGS** (line 532)
