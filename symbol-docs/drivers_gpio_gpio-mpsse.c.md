# drivers/gpio/gpio-mpsse.c

Subsystem: drivers/gpio

## Functions (23)

### gpio_mpsse_direction_input
- Return type: static int
- Signature: gpio_mpsse_direction_input(struct gpio_chip * chip,unsigned int offset)
- Line: 327
- Calls: gpio_mpsse_set_bank, gpiochip_get_data, mpsse_ensure_supported

### gpio_mpsse_direction_output
- Return type: static int
- Signature: gpio_mpsse_direction_output(struct gpio_chip * chip,unsigned int offset,int value)
- Line: 309
- Calls: gpio_mpsse_gpio_set, gpiochip_get_data, mpsse_ensure_supported

### gpio_mpsse_disconnect
- Return type: static void
- Signature: gpio_mpsse_disconnect(struct usb_interface * intf)
- Line: 703
- Calls: gpio_mpsse_stop_all_except

### gpio_mpsse_get_bank
- Return type: static int
- Signature: gpio_mpsse_get_bank(struct mpsse_priv * priv,u8 bank)
- Line: 180
- Calls: mpsse_read, mpsse_write
- Called by: gpio_mpsse_get_multiple

### gpio_mpsse_get_direction
- Return type: static int
- Signature: gpio_mpsse_get_direction(struct gpio_chip * chip,unsigned int offset)
- Line: 345
- Calls: gpiochip_get_data

### gpio_mpsse_get_multiple
- Return type: static int
- Signature: gpio_mpsse_get_multiple(struct gpio_chip * chip,unsigned long * mask,unsigned long * bits)
- Line: 253
- Calls: gpio_mpsse_get_bank, gpiochip_get_data, mpsse_ensure_supported
- Called by: gpio_mpsse_gpio_get, gpio_mpsse_poll

### gpio_mpsse_gpio_get
- Return type: static int
- Signature: gpio_mpsse_gpio_get(struct gpio_chip * chip,unsigned int offset)
- Line: 280
- Calls: gpio_mpsse_get_multiple

### gpio_mpsse_gpio_set
- Return type: static int
- Signature: gpio_mpsse_gpio_set(struct gpio_chip * chip,unsigned int offset,int value)
- Line: 297
- Calls: gpio_mpsse_set_multiple
- Called by: gpio_mpsse_direction_output

### gpio_mpsse_ida_remove
- Return type: static void
- Signature: gpio_mpsse_ida_remove(void * data)
- Line: 544

### gpio_mpsse_irq_disable
- Return type: static void
- Signature: gpio_mpsse_irq_disable(struct irq_data * irqd)
- Line: 491
- Calls: gpiochip_disable_irq

### gpio_mpsse_irq_enable
- Return type: static void
- Signature: gpio_mpsse_irq_enable(struct irq_data * irqd)
- Line: 509
- Calls: gpiochip_enable_irq

### gpio_mpsse_poll
- Return type: static void
- Signature: gpio_mpsse_poll(struct work_struct * my_work)
- Line: 398
- Calls: gpio_mpsse_get_multiple, gpio_mpsse_stop_all_except

### gpio_mpsse_probe
- Return type: static int
- Signature: gpio_mpsse_probe(struct usb_interface * interface,const struct usb_device_id * id)
- Line: 578

### gpio_mpsse_set_bank
- Return type: static int
- Signature: gpio_mpsse_set_bank(struct mpsse_priv * priv,u8 bank)
- Line: 166
- Calls: mpsse_write
- Called by: gpio_mpsse_direction_input, gpio_mpsse_set_multiple

### gpio_mpsse_set_irq_type
- Return type: static int
- Signature: gpio_mpsse_set_irq_type(struct irq_data * irqd,unsigned int type)
- Line: 480

### gpio_mpsse_set_multiple
- Return type: static int
- Signature: gpio_mpsse_set_multiple(struct gpio_chip * chip,unsigned long * mask,unsigned long * bits)
- Line: 222
- Calls: gpio_mpsse_set_bank, gpiochip_get_data, mpsse_ensure_supported
- Called by: gpio_mpsse_gpio_set

### gpio_mpsse_stop_all_except
- Return type: static void
- Signature: gpio_mpsse_stop_all_except(struct mpsse_priv * priv,struct mpsse_worker * my_worker)
- Line: 367
- Called by: gpio_mpsse_disconnect, gpio_mpsse_poll

### mpsse_bulk_xfer
- Return type: static int
- Signature: mpsse_bulk_xfer(struct usb_interface * intf,struct bulk_desc * desc)
- Line: 103
- Called by: mpsse_read, mpsse_write

### mpsse_ensure_supported
- Return type: static int
- Signature: mpsse_ensure_supported(struct gpio_chip * chip,unsigned long mask,int direction)
- Line: 196
- Calls: gpiochip_get_data
- Called by: gpio_mpsse_direction_input, gpio_mpsse_direction_output, gpio_mpsse_get_multiple, gpio_mpsse_set_multiple

### mpsse_init_valid_mask
- Return type: static int
- Signature: mpsse_init_valid_mask(struct gpio_chip * chip,unsigned long * valid_mask,unsigned int ngpios)
- Line: 551
- Calls: gpiochip_get_data

### mpsse_irq_init_valid_mask
- Return type: static void
- Signature: mpsse_irq_init_valid_mask(struct gpio_chip * chip,unsigned long * valid_mask,unsigned int ngpios)
- Line: 565
- Calls: gpiochip_get_data

### mpsse_read
- Return type: static int
- Signature: mpsse_read(struct usb_interface * intf,u8 * buf,size_t len)
- Line: 140
- Calls: mpsse_bulk_xfer
- Called by: gpio_mpsse_get_bank

### mpsse_write
- Return type: static int
- Signature: mpsse_write(struct usb_interface * intf,u8 * buf,size_t len)
- Line: 123
- Calls: mpsse_bulk_xfer
- Called by: gpio_mpsse_get_bank, gpio_mpsse_set_bank

## Structs (4)

### bulk_desc
- Line: 51
- Members:
  - gpio: gpio_chip
  - udev: usb_device *
  - intf: usb_interface *
  - intf_id: u8
  - workers: list_head
  - irq_mutex: mutex
  - irq_race: mutex
  - irq_spin: raw_spinlock_t
  - irq_type: atomic_t[16]
  - irq_enabled: atomic_t
  - id: int
  - gpio_outputs: u8[2]
  - gpio_dir: u8[2]
  - dir_in: unsigned long
  - dir_out: unsigned long
  - bulk_in_buf: u8 *
  - bulk_in: usb_endpoint_descriptor *
  - bulk_out: usb_endpoint_descriptor *
  - io_mutex: mutex
  - priv: mpsse_priv *
  - work: work_struct
  - cancelled: atomic_t
  - list: list_head
  - destroy: list_head
  - tx: bool
  - data: u8 *
  - len: int
  - len_actual: int
  - timeout: int
  - names: const char * []
  - dir_in: unsigned long
  - dir_out: unsigned long

### mpsse_priv
- Line: 16
- Members:
  - gpio: gpio_chip
  - udev: usb_device *
  - intf: usb_interface *
  - intf_id: u8
  - workers: list_head
  - irq_mutex: mutex
  - irq_race: mutex
  - irq_spin: raw_spinlock_t
  - irq_type: atomic_t[16]
  - irq_enabled: atomic_t
  - id: int
  - gpio_outputs: u8[2]
  - gpio_dir: u8[2]
  - dir_in: unsigned long
  - dir_out: unsigned long
  - bulk_in_buf: u8 *
  - bulk_in: usb_endpoint_descriptor *
  - bulk_out: usb_endpoint_descriptor *
  - io_mutex: mutex
  - priv: mpsse_priv *
  - work: work_struct
  - cancelled: atomic_t
  - list: list_head
  - destroy: list_head
  - tx: bool
  - data: u8 *
  - len: int
  - len_actual: int
  - timeout: int
  - names: const char * []
  - dir_in: unsigned long
  - dir_out: unsigned long

### mpsse_quirk
- Line: 62
- Members:
  - gpio: gpio_chip
  - udev: usb_device *
  - intf: usb_interface *
  - intf_id: u8
  - workers: list_head
  - irq_mutex: mutex
  - irq_race: mutex
  - irq_spin: raw_spinlock_t
  - irq_type: atomic_t[16]
  - irq_enabled: atomic_t
  - id: int
  - gpio_outputs: u8[2]
  - gpio_dir: u8[2]
  - dir_in: unsigned long
  - dir_out: unsigned long
  - bulk_in_buf: u8 *
  - bulk_in: usb_endpoint_descriptor *
  - bulk_out: usb_endpoint_descriptor *
  - io_mutex: mutex
  - priv: mpsse_priv *
  - work: work_struct
  - cancelled: atomic_t
  - list: list_head
  - destroy: list_head
  - tx: bool
  - data: u8 *
  - len: int
  - len_actual: int
  - timeout: int
  - names: const char * []
  - dir_in: unsigned long
  - dir_out: unsigned long

### mpsse_worker
- Line: 43
- Members:
  - gpio: gpio_chip
  - udev: usb_device *
  - intf: usb_interface *
  - intf_id: u8
  - workers: list_head
  - irq_mutex: mutex
  - irq_race: mutex
  - irq_spin: raw_spinlock_t
  - irq_type: atomic_t[16]
  - irq_enabled: atomic_t
  - id: int
  - gpio_outputs: u8[2]
  - gpio_dir: u8[2]
  - dir_in: unsigned long
  - dir_out: unsigned long
  - bulk_in_buf: u8 *
  - bulk_in: usb_endpoint_descriptor *
  - bulk_out: usb_endpoint_descriptor *
  - io_mutex: mutex
  - priv: mpsse_priv *
  - work: work_struct
  - cancelled: atomic_t
  - list: list_head
  - destroy: list_head
  - tx: bool
  - data: u8 *
  - len: int
  - len_actual: int
  - timeout: int
  - names: const char * []
  - dir_in: unsigned long
  - dir_out: unsigned long

## Variables (4)

- static **bryx_brik_quirk** : mpsse_quirk (line 68)
- static **gpio_mpsse_driver** : usb_driver (line 718)
- static **gpio_mpsse_irq_chip** : const struct irq_chip (line 535)
- static **gpio_mpsse_table** : const struct usb_device_id[] (line 77)

## Macros (9)

- **GET_BITS_CMD** (line 90)
- **MODE_MPSSE** (line 93)
- **MODE_RESET** (line 94)
- **MPSSE_NGPIO** (line 60)
- **MPSSE_POLL_INTERVAL** (line 101)
- **MPSSE_READ_TIMEOUT** (line 98)
- **MPSSE_WRITE_TIMEOUT** (line 97)
- **SET_BITMODE_REQUEST** (line 92)
- **SET_BITS_CMD** (line 89)
