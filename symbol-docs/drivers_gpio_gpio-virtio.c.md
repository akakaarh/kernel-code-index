# drivers/gpio/gpio-virtio.c

Subsystem: drivers/gpio

## Functions (24)

### _virtio_gpio_req
- Return type: static int
- Signature: _virtio_gpio_req(struct virtio_gpio * vgpio,u16 type,u16 gpio,u8 txvalue,u8 * rxvalue,void * response,u32 rxlen)
- Line: 65
- Called by: virtio_gpio_get_names, virtio_gpio_req

### ignore_irq
- Return type: static bool
- Signature: ignore_irq(struct virtio_gpio * vgpio,int gpio,struct vgpio_irq_line * irq_line)
- Line: 361
- Calls: virtio_gpio_irq_prepare
- Called by: virtio_gpio_event_vq

### virtio_gpio_alloc_vqs
- Return type: static int
- Signature: virtio_gpio_alloc_vqs(struct virtio_gpio * vgpio,struct virtio_device * vdev)
- Line: 452
- Calls: virtio_gpio_free_vqs
- Called by: virtio_gpio_probe

### virtio_gpio_direction_input
- Return type: static int
- Signature: virtio_gpio_direction_input(struct gpio_chip * gc,unsigned int gpio)
- Line: 172
- Calls: gpiochip_get_data, virtio_gpio_req

### virtio_gpio_direction_output
- Return type: static int
- Signature: virtio_gpio_direction_output(struct gpio_chip * gc,unsigned int gpio,int value)
- Line: 180
- Calls: gpiochip_get_data, virtio_gpio_req

### virtio_gpio_event_vq
- Return type: static void
- Signature: virtio_gpio_event_vq(struct virtqueue * vq)
- Line: 394
- Calls: ignore_irq

### virtio_gpio_free
- Return type: static void
- Signature: virtio_gpio_free(struct gpio_chip * gc,unsigned int gpio)
- Line: 143
- Calls: gpiochip_get_data, virtio_gpio_req

### virtio_gpio_free_vqs
- Return type: static void
- Signature: virtio_gpio_free_vqs(struct virtio_device * vdev)
- Line: 446
- Called by: virtio_gpio_alloc_vqs, virtio_gpio_probe, virtio_gpio_remove

### virtio_gpio_get
- Return type: static int
- Signature: virtio_gpio_get(struct gpio_chip * gc,unsigned int gpio)
- Line: 194
- Calls: gpiochip_get_data, virtio_gpio_req

### virtio_gpio_get_direction
- Return type: static int
- Signature: virtio_gpio_get_direction(struct gpio_chip * gc,unsigned int gpio)
- Line: 151
- Calls: gpiochip_get_data, virtio_gpio_req

### virtio_gpio_get_names
- Return type: static const char **
- Signature: virtio_gpio_get_names(struct virtio_gpio * vgpio,u32 gpio_names_size,u16 ngpio)
- Line: 490
- Calls: _virtio_gpio_req
- Called by: virtio_gpio_probe

### virtio_gpio_irq_bus_lock
- Return type: static void
- Signature: virtio_gpio_irq_bus_lock(struct irq_data * d)
- Line: 328
- Calls: gpiochip_get_data

### virtio_gpio_irq_bus_sync_unlock
- Return type: static void
- Signature: virtio_gpio_irq_bus_sync_unlock(struct irq_data * d)
- Line: 336
- Calls: gpiochip_get_data, virtio_gpio_irq_prepare, virtio_gpio_req

### virtio_gpio_irq_disable
- Return type: static void
- Signature: virtio_gpio_irq_disable(struct irq_data * d)
- Line: 255
- Calls: gpiochip_get_data

### virtio_gpio_irq_enable
- Return type: static void
- Signature: virtio_gpio_irq_enable(struct irq_data * d)
- Line: 240
- Calls: gpiochip_get_data

### virtio_gpio_irq_mask
- Return type: static void
- Signature: virtio_gpio_irq_mask(struct irq_data * d)
- Line: 270
- Calls: gpiochip_get_data

### virtio_gpio_irq_prepare
- Return type: static void
- Signature: virtio_gpio_irq_prepare(struct virtio_gpio * vgpio,u16 gpio)
- Line: 213
- Called by: ignore_irq, virtio_gpio_irq_bus_sync_unlock, virtio_gpio_irq_unmask

### virtio_gpio_irq_set_type
- Return type: static int
- Signature: virtio_gpio_irq_set_type(struct irq_data * d,unsigned int type)
- Line: 295
- Calls: gpiochip_get_data

### virtio_gpio_irq_unmask
- Return type: static void
- Signature: virtio_gpio_irq_unmask(struct irq_data * d)
- Line: 281
- Calls: gpiochip_get_data, virtio_gpio_irq_prepare

### virtio_gpio_probe
- Return type: static int
- Signature: virtio_gpio_probe(struct virtio_device * vdev)
- Line: 535
- Calls: virtio_gpio_alloc_vqs, virtio_gpio_free_vqs, virtio_gpio_get_names

### virtio_gpio_remove
- Return type: static void
- Signature: virtio_gpio_remove(struct virtio_device * vdev)
- Line: 640
- Calls: gpiochip_remove, virtio_gpio_free_vqs

### virtio_gpio_req
- Return type: static int
- Signature: virtio_gpio_req(struct virtio_gpio * vgpio,u16 type,u16 gpio,u8 txvalue,u8 * rxvalue)
- Line: 133
- Calls: _virtio_gpio_req
- Called by: virtio_gpio_direction_input, virtio_gpio_direction_output, virtio_gpio_free, virtio_gpio_get, virtio_gpio_get_direction, virtio_gpio_irq_bus_sync_unlock, virtio_gpio_set

### virtio_gpio_request_vq
- Return type: static void
- Signature: virtio_gpio_request_vq(struct virtqueue * vq)
- Line: 431

### virtio_gpio_set
- Return type: static int
- Signature: virtio_gpio_set(struct gpio_chip * gc,unsigned int gpio,int value)
- Line: 204
- Calls: gpiochip_get_data, virtio_gpio_req

## Structs (3)

### vgpio_irq_line
- Line: 37
- Members:
  - lock: mutex
  - completion: completion
  - rxlen: unsigned int
  - req: virtio_gpio_request
  - res: virtio_gpio_response
  - type: u8
  - disabled: bool
  - masked: bool
  - queued: bool
  - update_pending: bool
  - queue_pending: bool
  - ireq: virtio_gpio_irq_request
  - ires: virtio_gpio_irq_response
  - vdev: virtio_device *
  - lock: mutex
  - gc: gpio_chip
  - lines: virtio_gpio_line *
  - request_vq: virtqueue *
  - event_vq: virtqueue *
  - irq_lock: mutex
  - eventq_lock: raw_spinlock_t
  - irq_lines: vgpio_irq_line *

### virtio_gpio
- Line: 51
- Members:
  - lock: mutex
  - completion: completion
  - rxlen: unsigned int
  - req: virtio_gpio_request
  - res: virtio_gpio_response
  - type: u8
  - disabled: bool
  - masked: bool
  - queued: bool
  - update_pending: bool
  - queue_pending: bool
  - ireq: virtio_gpio_irq_request
  - ires: virtio_gpio_irq_response
  - vdev: virtio_device *
  - lock: mutex
  - gc: gpio_chip
  - lines: virtio_gpio_line *
  - request_vq: virtqueue *
  - event_vq: virtqueue *
  - irq_lock: mutex
  - eventq_lock: raw_spinlock_t
  - irq_lines: vgpio_irq_line *

### virtio_gpio_line
- Line: 25
- Members:
  - lock: mutex
  - completion: completion
  - rxlen: unsigned int
  - req: virtio_gpio_request
  - res: virtio_gpio_response
  - type: u8
  - disabled: bool
  - masked: bool
  - queued: bool
  - update_pending: bool
  - queue_pending: bool
  - ireq: virtio_gpio_irq_request
  - ires: virtio_gpio_irq_response
  - vdev: virtio_device *
  - lock: mutex
  - gc: gpio_chip
  - lines: virtio_gpio_line *
  - request_vq: virtqueue *
  - event_vq: virtqueue *
  - irq_lock: mutex
  - eventq_lock: raw_spinlock_t
  - irq_lines: vgpio_irq_line *

## Variables (3)

- static **features** : const unsigned int[] (line 654)
- static **id_table** : const struct virtio_device_id[] (line 648)
- static **virtio_gpio_driver** : virtio_driver (line 658)
