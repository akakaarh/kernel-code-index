# drivers/gpio/gpio-nct6694.c

Subsystem: drivers/gpio

## Functions (17)

### nct6694_direction_input
- Return type: static int
- Signature: nct6694_direction_input(struct gpio_chip * gpio,unsigned int offset)
- Line: 72
- Calls: gpiochip_get_data

### nct6694_direction_output
- Return type: static int
- Signature: nct6694_direction_output(struct gpio_chip * gpio,unsigned int offset,int val)
- Line: 93
- Calls: gpiochip_get_data

### nct6694_get_direction
- Return type: static int
- Signature: nct6694_get_direction(struct gpio_chip * gpio,unsigned int offset)
- Line: 53
- Calls: gpiochip_get_data

### nct6694_get_irq_trig
- Return type: static int
- Signature: nct6694_get_irq_trig(struct nct6694_gpio_data * data)
- Line: 274
- Called by: nct6694_gpio_probe

### nct6694_get_value
- Return type: static int
- Signature: nct6694_get_value(struct gpio_chip * gpio,unsigned int offset)
- Line: 130
- Calls: gpiochip_get_data

### nct6694_gpio_ida_free
- Return type: static void
- Signature: nct6694_gpio_ida_free(void * d)
- Line: 384

### nct6694_gpio_probe
- Return type: static int
- Signature: nct6694_gpio_probe(struct platform_device * pdev)
- Line: 392
- Calls: nct6694_get_irq_trig

### nct6694_init_valid_mask
- Return type: static int
- Signature: nct6694_init_valid_mask(struct gpio_chip * gpio,unsigned long * valid_mask,unsigned int ngpios)
- Line: 219
- Calls: gpiochip_get_data

### nct6694_irq_bus_lock
- Return type: static void
- Signature: nct6694_irq_bus_lock(struct irq_data * d)
- Line: 338
- Calls: gpiochip_get_data

### nct6694_irq_bus_sync_unlock
- Return type: static void
- Signature: nct6694_irq_bus_sync_unlock(struct irq_data * d)
- Line: 346
- Calls: gpiochip_get_data

### nct6694_irq_dispose_mapping
- Return type: static void
- Signature: nct6694_irq_dispose_mapping(void * d)
- Line: 377

### nct6694_irq_handler
- Return type: static irqreturn_t
- Signature: nct6694_irq_handler(int irq,void * priv)
- Line: 242

### nct6694_irq_mask
- Return type: static void
- Signature: nct6694_irq_mask(struct irq_data * d)
- Line: 293
- Calls: gpiochip_disable_irq

### nct6694_irq_set_type
- Return type: static int
- Signature: nct6694_irq_set_type(struct irq_data * d,unsigned int type)
- Line: 309
- Calls: gpiochip_get_data

### nct6694_irq_unmask
- Return type: static void
- Signature: nct6694_irq_unmask(struct irq_data * d)
- Line: 301
- Calls: gpiochip_enable_irq

### nct6694_set_config
- Return type: static int
- Signature: nct6694_set_config(struct gpio_chip * gpio,unsigned int offset,unsigned long config)
- Line: 188
- Calls: gpiochip_get_data

### nct6694_set_value
- Return type: static int
- Signature: nct6694_set_value(struct gpio_chip * gpio,unsigned int offset,int val)
- Line: 163
- Calls: gpiochip_get_data

## Structs (1)

### nct6694_gpio_data
- Line: 37
- Members:
  - nct6694: nct6694 *
  - gpio: gpio_chip
  - lock: mutex
  - irq_lock: mutex
  - reg_val: unsigned char
  - irq_trig_falling: unsigned char
  - irq_trig_rising: unsigned char
  - group: unsigned char
  - irq: int

## Variables (2)

- static **nct6694_gpio_driver** : platform_driver (line 487)
- static **nct6694_irq_chip** : const struct irq_chip (line 366)

## Macros (12)

- **NCT6694_GPIO_MOD** (line 21)
- **NCT6694_GPIO_VALID** (line 24)
- **NCT6694_GPIO_VER** (line 23)
- **NCT6694_GPI_CLR** (line 31)
- **NCT6694_GPI_DATA** (line 25)
- **NCT6694_GPI_FALLING** (line 32)
- **NCT6694_GPI_RISING** (line 33)
- **NCT6694_GPI_STS** (line 30)
- **NCT6694_GPO_DATA** (line 28)
- **NCT6694_GPO_DIR** (line 26)
- **NCT6694_GPO_TYPE** (line 27)
- **NCT6694_NR_GPIO** (line 35)
