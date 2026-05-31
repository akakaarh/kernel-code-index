# drivers/gpio/gpio-ljca.c

Subsystem: drivers/gpio

## Functions (21)

### ljca_enable_irq
- Return type: static int
- Signature: ljca_enable_irq(struct ljca_gpio_dev * ljca_gpio,int gpio_id,bool enable)
- Line: 249
- Called by: ljca_gpio_async, ljca_irq_bus_unlock

### ljca_gpio_async
- Return type: static void
- Signature: ljca_gpio_async(struct work_struct * work)
- Line: 270
- Calls: ljca_enable_irq

### ljca_gpio_config
- Return type: static int
- Signature: ljca_gpio_config(struct ljca_gpio_dev * ljca_gpio,u8 gpio_id,u8 config)
- Line: 77
- Called by: ljca_gpio_direction_input, ljca_gpio_direction_output, ljca_irq_bus_unlock

### ljca_gpio_direction_input
- Return type: static int
- Signature: ljca_gpio_direction_input(struct gpio_chip * chip,unsigned int offset)
- Line: 162
- Calls: gpiochip_get_data, ljca_gpio_config

### ljca_gpio_direction_output
- Return type: static int
- Signature: ljca_gpio_direction_output(struct gpio_chip * chip,unsigned int offset,int val)
- Line: 177
- Calls: gpiochip_get_data, ljca_gpio_config, ljca_gpio_set_value

### ljca_gpio_event_cb
- Return type: static void
- Signature: ljca_gpio_event_cb(void * context,u8 cmd,const void * evt_data,int len)
- Line: 284

### ljca_gpio_get_direction
- Return type: static int
- Signature: ljca_gpio_get_direction(struct gpio_chip * chip,unsigned int offset)
- Line: 197
- Calls: gpiochip_get_data

### ljca_gpio_get_value
- Return type: static int
- Signature: ljca_gpio_get_value(struct gpio_chip * chip,unsigned int offset)
- Line: 140
- Calls: gpiochip_get_data, ljca_gpio_read

### ljca_gpio_init_valid_mask
- Return type: static int
- Signature: ljca_gpio_init_valid_mask(struct gpio_chip * chip,unsigned long * valid_mask,unsigned int ngpios)
- Line: 230
- Calls: gpiochip_get_data
- Called by: ljca_gpio_irq_init_valid_mask

### ljca_gpio_irq_init_valid_mask
- Return type: static void
- Signature: ljca_gpio_irq_init_valid_mask(struct gpio_chip * chip,unsigned long * valid_mask,unsigned int ngpios)
- Line: 242
- Calls: ljca_gpio_init_valid_mask

### ljca_gpio_probe
- Return type: static int
- Signature: ljca_gpio_probe(struct auxiliary_device * auxdev,const struct auxiliary_device_id * aux_dev_id)
- Line: 399

### ljca_gpio_read
- Return type: static int
- Signature: ljca_gpio_read(struct ljca_gpio_dev * ljca_gpio,u8 gpio_id)
- Line: 96
- Called by: ljca_gpio_get_value

### ljca_gpio_remove
- Return type: static void
- Signature: ljca_gpio_remove(struct auxiliary_device * auxdev)
- Line: 465
- Calls: gpiochip_remove

### ljca_gpio_set_config
- Return type: static int
- Signature: ljca_gpio_set_config(struct gpio_chip * chip,unsigned int offset,unsigned long config)
- Line: 207
- Calls: gpiochip_get_data

### ljca_gpio_set_value
- Return type: static int
- Signature: ljca_gpio_set_value(struct gpio_chip * chip,unsigned int offset,int val)
- Line: 147
- Calls: gpiochip_get_data, ljca_gpio_write
- Called by: ljca_gpio_direction_output

### ljca_gpio_write
- Return type: static int
- Signature: ljca_gpio_write(struct ljca_gpio_dev * ljca_gpio,u8 gpio_id,int value)
- Line: 122
- Called by: ljca_gpio_set_value

### ljca_irq_bus_lock
- Return type: static void
- Signature: ljca_irq_bus_lock(struct irq_data * irqd)
- Line: 356
- Calls: gpiochip_get_data

### ljca_irq_bus_unlock
- Return type: static void
- Signature: ljca_irq_bus_unlock(struct irq_data * irqd)
- Line: 364
- Calls: gpiochip_get_data, ljca_enable_irq, ljca_gpio_config

### ljca_irq_mask
- Return type: static void
- Signature: ljca_irq_mask(struct irq_data * irqd)
- Line: 313
- Calls: gpiochip_disable_irq, gpiochip_get_data

### ljca_irq_set_type
- Return type: static int
- Signature: ljca_irq_set_type(struct irq_data * irqd,unsigned int type)
- Line: 323
- Calls: gpiochip_get_data

### ljca_irq_unmask
- Return type: static void
- Signature: ljca_irq_unmask(struct irq_data * irqd)
- Line: 303
- Calls: gpiochip_enable_irq, gpiochip_get_data

## Structs (3)

### ljca_gpio_dev
- Line: 58
- Members:
  - index: u8
  - value: u8
  - num: u8
  - ljca: ljca_client *
  - gc: gpio_chip
  - gpio_info: ljca_gpio_info *
  - connect_mode: u8 *
  - irq_lock: mutex
  - work: work_struct
  - trans_lock: mutex
  - obuf: u8[]
  - ibuf: u8[]

### ljca_gpio_op
- Line: 48
- Members:
  - index: u8
  - value: u8
  - num: u8
  - ljca: ljca_client *
  - gc: gpio_chip
  - gpio_info: ljca_gpio_info *
  - connect_mode: u8 *
  - irq_lock: mutex
  - work: work_struct
  - trans_lock: mutex
  - obuf: u8[]
  - ibuf: u8[]

### ljca_gpio_packet
- Line: 53
- Members:
  - index: u8
  - value: u8
  - num: u8
  - ljca: ljca_client *
  - gc: gpio_chip
  - gpio_info: ljca_gpio_info *
  - connect_mode: u8 *
  - irq_lock: mutex
  - work: work_struct
  - trans_lock: mutex
  - obuf: u8[]
  - ibuf: u8[]

## Variables (5)

- **__packed** : ljca_gpio_op (line 51)
- **__packed** : ljca_gpio_packet (line 56)
- static **ljca_gpio_driver** : auxiliary_driver (line 480)
- static **ljca_gpio_id_table** : const struct auxiliary_device_id[] (line 474)
- static **ljca_gpio_irqchip** : const struct irq_chip (line 388)

## Macros (19)

- **LJCA_GPIO_BUF_SIZE** (line 46)
- **LJCA_GPIO_CONFIG** (line 23)
- **LJCA_GPIO_CONF_CLR** (line 44)
- **LJCA_GPIO_CONF_DEFAULT** (line 35)
- **LJCA_GPIO_CONF_DISABLE** (line 30)
- **LJCA_GPIO_CONF_EDGE** (line 39)
- **LJCA_GPIO_CONF_INPUT** (line 31)
- **LJCA_GPIO_CONF_INTERRUPT** (line 36)
- **LJCA_GPIO_CONF_LEVEL** (line 40)
- **LJCA_GPIO_CONF_OUTPUT** (line 32)
- **LJCA_GPIO_CONF_PULLDOWN** (line 34)
- **LJCA_GPIO_CONF_PULLUP** (line 33)
- **LJCA_GPIO_CONF_SET** (line 43)
- **LJCA_GPIO_INT_EVENT** (line 26)
- **LJCA_GPIO_INT_MASK** (line 27)
- **LJCA_GPIO_INT_TYPE** (line 37)
- **LJCA_GPIO_INT_UNMASK** (line 28)
- **LJCA_GPIO_READ** (line 24)
- **LJCA_GPIO_WRITE** (line 25)
