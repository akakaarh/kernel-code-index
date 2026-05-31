# drivers/gpio/gpio-dln2.c

Subsystem: drivers/gpio

## Functions (24)

### dln2_gpio_direction_input
- Return type: static int
- Signature: dln2_gpio_direction_input(struct gpio_chip * chip,unsigned offset)
- Line: 254
- Calls: dln2_gpio_set_direction

### dln2_gpio_direction_output
- Return type: static int
- Signature: dln2_gpio_direction_output(struct gpio_chip * chip,unsigned offset,int value)
- Line: 259
- Calls: dln2_gpio_pin_set_out_val, dln2_gpio_set_direction, gpiochip_get_data

### dln2_gpio_event
- Return type: static void
- Signature: dln2_gpio_event(struct platform_device * pdev,u16 echo,const void * data,int len)
- Line: 400

### dln2_gpio_free
- Return type: static void
- Signature: dln2_gpio_free(struct gpio_chip * chip,unsigned offset)
- Line: 191
- Calls: dln2_gpio_pin_cmd, gpiochip_get_data

### dln2_gpio_get
- Return type: static int
- Signature: dln2_gpio_get(struct gpio_chip * chip,unsigned int offset)
- Line: 208
- Calls: dln2_gpio_get_direction, dln2_gpio_pin_get_in_val, dln2_gpio_pin_get_out_val, gpiochip_get_data

### dln2_gpio_get_direction
- Return type: static int
- Signature: dln2_gpio_get_direction(struct gpio_chip * chip,unsigned offset)
- Line: 198
- Calls: gpiochip_get_data
- Called by: dln2_gpio_get

### dln2_gpio_get_pin_count
- Return type: static int
- Signature: dln2_gpio_get_pin_count(struct platform_device * pdev)
- Line: 73
- Called by: dln2_gpio_probe

### dln2_gpio_pin_cmd
- Return type: static int
- Signature: dln2_gpio_pin_cmd(struct dln2_gpio * dln2,int cmd,unsigned pin)
- Line: 88
- Called by: dln2_gpio_free, dln2_gpio_request

### dln2_gpio_pin_get_in_val
- Return type: static int
- Signature: dln2_gpio_pin_get_in_val(struct dln2_gpio * dln2,unsigned int pin)
- Line: 115
- Calls: dln2_gpio_pin_val
- Called by: dln2_gpio_get

### dln2_gpio_pin_get_out_val
- Return type: static int
- Signature: dln2_gpio_pin_get_out_val(struct dln2_gpio * dln2,unsigned int pin)
- Line: 125
- Calls: dln2_gpio_pin_val
- Called by: dln2_gpio_get

### dln2_gpio_pin_set_out_val
- Return type: static int
- Signature: dln2_gpio_pin_set_out_val(struct dln2_gpio * dln2,unsigned int pin,int value)
- Line: 135
- Called by: dln2_gpio_direction_output, dln2_gpio_set

### dln2_gpio_pin_val
- Return type: static int
- Signature: dln2_gpio_pin_val(struct dln2_gpio * dln2,int cmd,unsigned int pin)
- Line: 97
- Called by: dln2_gpio_pin_get_in_val, dln2_gpio_pin_get_out_val

### dln2_gpio_probe
- Return type: static int
- Signature: dln2_gpio_probe(struct platform_device * pdev)
- Line: 440
- Calls: dln2_gpio_get_pin_count

### dln2_gpio_remove
- Return type: static void
- Signature: dln2_gpio_remove(struct platform_device * pdev)
- Line: 508

### dln2_gpio_request
- Return type: static int
- Signature: dln2_gpio_request(struct gpio_chip * chip,unsigned offset)
- Line: 150
- Calls: dln2_gpio_pin_cmd, gpiochip_get_data

### dln2_gpio_set
- Return type: static int
- Signature: dln2_gpio_set(struct gpio_chip * chip,unsigned int offset,int value)
- Line: 223
- Calls: dln2_gpio_pin_set_out_val, gpiochip_get_data

### dln2_gpio_set_config
- Return type: static int
- Signature: dln2_gpio_set_config(struct gpio_chip * chip,unsigned offset,unsigned long config)
- Line: 272
- Calls: gpiochip_get_data

### dln2_gpio_set_direction
- Return type: static int
- Signature: dln2_gpio_set_direction(struct gpio_chip * chip,unsigned offset,unsigned dir)
- Line: 231
- Calls: gpiochip_get_data
- Called by: dln2_gpio_direction_input, dln2_gpio_direction_output

### dln2_gpio_set_event_cfg
- Return type: static int
- Signature: dln2_gpio_set_event_cfg(struct dln2_gpio * dln2,unsigned pin,unsigned type,unsigned period)
- Line: 286
- Called by: dln2_irq_bus_unlock

### dln2_irq_bus_lock
- Return type: static void
- Signature: dln2_irq_bus_lock(struct irq_data * irqd)
- Line: 352
- Calls: gpiochip_get_data

### dln2_irq_bus_unlock
- Return type: static void
- Signature: dln2_irq_bus_unlock(struct irq_data * irqd)
- Line: 360
- Calls: dln2_gpio_set_event_cfg, gpiochip_get_data

### dln2_irq_mask
- Return type: static void
- Signature: dln2_irq_mask(struct irq_data * irqd)
- Line: 313
- Calls: gpiochip_disable_irq, gpiochip_get_data

### dln2_irq_set_type
- Return type: static int
- Signature: dln2_irq_set_type(struct irq_data * irqd,unsigned type)
- Line: 323
- Calls: gpiochip_get_data

### dln2_irq_unmask
- Return type: static void
- Signature: dln2_irq_unmask(struct irq_data * irqd)
- Line: 303
- Calls: gpiochip_enable_irq, gpiochip_get_data

## Structs (5)

### __anon5ee18c180108
- Line: 289
- Members:
  - pdev: platform_device *
  - gpio: gpio_chip
  - irq_type: int[]
  - irq_lock: mutex
  - pin: __le16
  - __packed: __le16 pin
  - value: u8
  - pin: __le16
  - type: u8
  - period: __le16
  - count: __le16
  - type: __u8
  - pin: __le16
  - value: __u8

### __anon5ee18c180208
- Line: 405
- Members:
  - pdev: platform_device *
  - gpio: gpio_chip
  - irq_type: int[]
  - irq_lock: mutex
  - pin: __le16
  - __packed: __le16 pin
  - value: u8
  - pin: __le16
  - type: u8
  - period: __le16
  - count: __le16
  - type: __u8
  - pin: __le16
  - value: __u8

### dln2_gpio
- Line: 46
- Members:
  - pdev: platform_device *
  - gpio: gpio_chip
  - irq_type: int[]
  - irq_lock: mutex
  - pin: __le16
  - __packed: __le16 pin
  - value: u8
  - pin: __le16
  - type: u8
  - period: __le16
  - count: __le16
  - type: __u8
  - pin: __le16
  - value: __u8

### dln2_gpio_pin
- Line: 64
- Members:
  - pdev: platform_device *
  - gpio: gpio_chip
  - irq_type: int[]
  - irq_lock: mutex
  - pin: __le16
  - __packed: __le16 pin
  - value: u8
  - pin: __le16
  - type: u8
  - period: __le16
  - count: __le16
  - type: __u8
  - pin: __le16
  - value: __u8

### dln2_gpio_pin_val
- Line: 68
- Members:
  - pdev: platform_device *
  - gpio: gpio_chip
  - irq_type: int[]
  - irq_lock: mutex
  - pin: __le16
  - __packed: __le16 pin
  - value: u8
  - pin: __le16
  - type: u8
  - period: __le16
  - count: __le16
  - type: __u8
  - pin: __le16
  - value: __u8

## Variables (2)

- static **dln2_gpio_driver** : platform_driver (line 513)
- static **dln2_irqchip** : const struct irq_chip (line 389)

## Macros (25)

- **DLN2_GPIO_CONDITION_MET_EV** (line 28)
- **DLN2_GPIO_DIRECTION_IN** (line 147)
- **DLN2_GPIO_DIRECTION_OUT** (line 148)
- **DLN2_GPIO_EVENT_CHANGE** (line 37)
- **DLN2_GPIO_EVENT_CHANGE_FALLING** (line 41)
- **DLN2_GPIO_EVENT_CHANGE_RISING** (line 40)
- **DLN2_GPIO_EVENT_LVL_HIGH** (line 38)
- **DLN2_GPIO_EVENT_LVL_LOW** (line 39)
- **DLN2_GPIO_EVENT_MASK** (line 42)
- **DLN2_GPIO_EVENT_NONE** (line 36)
- **DLN2_GPIO_GET_DEBOUNCE** (line 23)
- **DLN2_GPIO_GET_PIN_COUNT** (line 21)
- **DLN2_GPIO_ID** (line 19)
- **DLN2_GPIO_MAX_PINS** (line 44)
- **DLN2_GPIO_PIN_DISABLE** (line 30)
- **DLN2_GPIO_PIN_ENABLE** (line 29)
- **DLN2_GPIO_PIN_GET_DIRECTION** (line 32)
- **DLN2_GPIO_PIN_GET_EVENT_CFG** (line 34)
- **DLN2_GPIO_PIN_GET_OUT_VAL** (line 27)
- **DLN2_GPIO_PIN_GET_VAL** (line 25)
- **DLN2_GPIO_PIN_SET_DIRECTION** (line 31)
- **DLN2_GPIO_PIN_SET_EVENT_CFG** (line 33)
- **DLN2_GPIO_PIN_SET_OUT_VAL** (line 26)
- **DLN2_GPIO_PORT_GET_VAL** (line 24)
- **DLN2_GPIO_SET_DEBOUNCE** (line 22)
