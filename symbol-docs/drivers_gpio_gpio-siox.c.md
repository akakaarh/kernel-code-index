# drivers/gpio/gpio-siox.c

Subsystem: drivers/gpio

## Functions (12)

### gpio_siox_direction_input
- Return type: static int
- Signature: gpio_siox_direction_input(struct gpio_chip * chip,unsigned int offset)
- Line: 181

### gpio_siox_direction_output
- Return type: static int
- Signature: gpio_siox_direction_output(struct gpio_chip * chip,unsigned int offset,int value)
- Line: 190
- Calls: gpio_siox_set

### gpio_siox_get
- Return type: static int
- Signature: gpio_siox_get(struct gpio_chip * chip,unsigned int offset)
- Line: 141
- Calls: gpiochip_get_data

### gpio_siox_get_data
- Return type: static int
- Signature: gpio_siox_get_data(struct siox_device * sdevice,const u8 buf[])
- Line: 38

### gpio_siox_get_direction
- Return type: static int
- Signature: gpio_siox_get_direction(struct gpio_chip * chip,unsigned int offset)
- Line: 199

### gpio_siox_irq_ack
- Return type: static void
- Signature: gpio_siox_irq_ack(struct irq_data * d)
- Line: 97
- Calls: gpiochip_get_data

### gpio_siox_irq_mask
- Return type: static void
- Signature: gpio_siox_irq_mask(struct irq_data * d)
- Line: 107
- Calls: gpiochip_disable_irq, gpiochip_get_data

### gpio_siox_irq_set_type
- Return type: static int
- Signature: gpio_siox_irq_set_type(struct irq_data * d,u32 type)
- Line: 129
- Calls: gpiochip_get_data

### gpio_siox_irq_unmask
- Return type: static void
- Signature: gpio_siox_irq_unmask(struct irq_data * d)
- Line: 118
- Calls: gpiochip_enable_irq, gpiochip_get_data

### gpio_siox_probe
- Return type: static int
- Signature: gpio_siox_probe(struct siox_device * sdevice)
- Line: 217

### gpio_siox_set
- Return type: static int
- Signature: gpio_siox_set(struct gpio_chip * chip,unsigned int offset,int value)
- Line: 163
- Calls: gpiochip_get_data
- Called by: gpio_siox_direction_output

### gpio_siox_set_data
- Return type: static int
- Signature: gpio_siox_set_data(struct siox_device * sdevice,u8 status,u8 buf[])
- Line: 27

## Structs (1)

### gpio_siox_ddata
- Line: 11
- Members:
  - gchip: gpio_chip
  - lock: mutex
  - setdata: u8[1]
  - getdata: u8[3]
  - irqlock: raw_spinlock_t
  - irq_enable: u32
  - irq_status: u32
  - irq_type: u32[20]

## Variables (2)

- static **gpio_siox_driver** : siox_driver (line 259)
- static **gpio_siox_irq_chip** : const struct irq_chip (line 207)
