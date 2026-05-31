# drivers/gpio/gpio-eic-sprd.c

Subsystem: drivers/gpio

## Functions (21)

### sprd_eic_direction_input
- Return type: static int
- Signature: sprd_eic_direction_input(struct gpio_chip * chip,unsigned int offset)
- Line: 200

### sprd_eic_free
- Return type: static void
- Signature: sprd_eic_free(struct gpio_chip * chip,unsigned int offset)
- Line: 179
- Calls: sprd_eic_update

### sprd_eic_get
- Return type: static int
- Signature: sprd_eic_get(struct gpio_chip * chip,unsigned int offset)
- Line: 184
- Calls: gpiochip_get_data, sprd_eic_read
- Called by: sprd_eic_irq_set_type, sprd_eic_toggle_trigger

### sprd_eic_handle_one_type
- Return type: static void
- Signature: sprd_eic_handle_one_type(struct gpio_chip * chip)
- Line: 526
- Calls: gpiochip_get_data, sprd_eic_offset_base, sprd_eic_toggle_trigger
- Called by: sprd_eic_irq_notify

### sprd_eic_irq_ack
- Return type: static void
- Signature: sprd_eic_irq_ack(struct irq_data * data)
- Line: 293
- Calls: gpiochip_get_data, sprd_eic_update

### sprd_eic_irq_handler
- Return type: static void
- Signature: sprd_eic_irq_handler(struct irq_desc * desc)
- Line: 568

### sprd_eic_irq_mask
- Return type: static void
- Signature: sprd_eic_irq_mask(struct irq_data * data)
- Line: 239
- Calls: gpiochip_disable_irq, gpiochip_get_data, sprd_eic_update
- Called by: sprd_eic_toggle_trigger

### sprd_eic_irq_notify
- Return type: static int
- Signature: sprd_eic_irq_notify(struct notifier_block * nb,unsigned long action,void * data)
- Line: 584
- Calls: sprd_eic_handle_one_type, to_sprd_eic

### sprd_eic_irq_set_type
- Return type: static int
- Signature: sprd_eic_irq_set_type(struct irq_data * data,unsigned int flow_type)
- Line: 317
- Calls: gpiochip_get_data, sprd_eic_get, sprd_eic_update

### sprd_eic_irq_unmask
- Return type: static void
- Signature: sprd_eic_irq_unmask(struct irq_data * data)
- Line: 266
- Calls: gpiochip_enable_irq, gpiochip_get_data, sprd_eic_update
- Called by: sprd_eic_toggle_trigger

### sprd_eic_offset_base
- Return type: static void __iomem *
- Signature: sprd_eic_offset_base(struct sprd_eic * sprd_eic,unsigned int bank)
- Line: 134
- Called by: sprd_eic_handle_one_type, sprd_eic_read, sprd_eic_set_debounce, sprd_eic_update

### sprd_eic_probe
- Return type: static int
- Signature: sprd_eic_probe(struct platform_device * pdev)
- Line: 611

### sprd_eic_read
- Return type: static int
- Signature: sprd_eic_read(struct gpio_chip * chip,unsigned int offset,u16 reg)
- Line: 164
- Calls: gpiochip_get_data, sprd_eic_offset_base
- Called by: sprd_eic_get

### sprd_eic_request
- Return type: static int
- Signature: sprd_eic_request(struct gpio_chip * chip,unsigned int offset)
- Line: 173
- Calls: sprd_eic_update

### sprd_eic_set
- Return type: static int
- Signature: sprd_eic_set(struct gpio_chip * chip,unsigned int offset,int value)
- Line: 206

### sprd_eic_set_config
- Return type: static int
- Signature: sprd_eic_set_config(struct gpio_chip * chip,unsigned int offset,unsigned long config)
- Line: 227
- Calls: sprd_eic_set_debounce

### sprd_eic_set_debounce
- Return type: static int
- Signature: sprd_eic_set_debounce(struct gpio_chip * chip,unsigned int offset,unsigned int debounce)
- Line: 212
- Calls: gpiochip_get_data, sprd_eic_offset_base
- Called by: sprd_eic_set_config

### sprd_eic_toggle_trigger
- Return type: static void
- Signature: sprd_eic_toggle_trigger(struct gpio_chip * chip,unsigned int irq,unsigned int offset)
- Line: 477
- Calls: gpiochip_get_data, sprd_eic_get, sprd_eic_irq_mask, sprd_eic_irq_unmask, sprd_eic_update
- Called by: sprd_eic_handle_one_type

### sprd_eic_unregister_notifier
- Return type: static void
- Signature: sprd_eic_unregister_notifier(void * data)
- Line: 604

### sprd_eic_update
- Return type: static void
- Signature: sprd_eic_update(struct gpio_chip * chip,unsigned int offset,u16 reg,unsigned int val)
- Line: 143
- Calls: gpiochip_get_data, sprd_eic_offset_base
- Called by: sprd_eic_free, sprd_eic_irq_ack, sprd_eic_irq_mask, sprd_eic_irq_set_type, sprd_eic_irq_unmask, sprd_eic_request, sprd_eic_toggle_trigger

### to_sprd_eic
- Return type: static sprd_eic *
- Signature: to_sprd_eic(struct notifier_block * nb)
- Line: 104
- Called by: sprd_eic_irq_notify

## Structs (2)

### sprd_eic
- Line: 93
- Members:
  - chip: gpio_chip
  - irq_nb: notifier_block
  - base: void __iomem * []
  - type: sprd_eic_type
  - lock: spinlock_t
  - irq: int
  - type: sprd_eic_type

### sprd_eic_variant_data
- Line: 109
- Members:
  - chip: gpio_chip
  - irq_nb: notifier_block
  - base: void __iomem * []
  - type: sprd_eic_type
  - lock: spinlock_t
  - irq: int
  - type: sprd_eic_type

## Enums (1)

### sprd_eic_type
- Line: 85

## Variables (8)

- static **sc9860_eic_async_data** : const struct sprd_eic_variant_data (line 126)
- static **sc9860_eic_dbnc_data** : const struct sprd_eic_variant_data (line 118)
- static **sc9860_eic_latch_data** : const struct sprd_eic_variant_data (line 122)
- static **sc9860_eic_sync_data** : const struct sprd_eic_variant_data (line 130)
- static **sprd_eic_driver** : platform_driver (line 726)
- static **sprd_eic_irq** : const struct irq_chip (line 594)
- static **sprd_eic_label_name** : const char * [] (line 113)
- static **sprd_eic_of_match** : const struct of_device_id[] (line 703)

## Macros (36)

- **SPRD_EIC_ASYNC_DATA** (line 42)
- **SPRD_EIC_ASYNC_INTBOTH** (line 40)
- **SPRD_EIC_ASYNC_INTCLR** (line 38)
- **SPRD_EIC_ASYNC_INTIE** (line 35)
- **SPRD_EIC_ASYNC_INTMODE** (line 39)
- **SPRD_EIC_ASYNC_INTMSK** (line 37)
- **SPRD_EIC_ASYNC_INTPOL** (line 41)
- **SPRD_EIC_ASYNC_INTRAW** (line 36)
- **SPRD_EIC_BIT**(x) (line 60)
- **SPRD_EIC_DATA_MASK** (line 59)
- **SPRD_EIC_DBNC_CTRL0** (line 26)
- **SPRD_EIC_DBNC_DATA** (line 18)
- **SPRD_EIC_DBNC_DMSK** (line 19)
- **SPRD_EIC_DBNC_IC** (line 24)
- **SPRD_EIC_DBNC_IE** (line 21)
- **SPRD_EIC_DBNC_IEV** (line 20)
- **SPRD_EIC_DBNC_MASK** (line 61)
- **SPRD_EIC_DBNC_MIS** (line 23)
- **SPRD_EIC_DBNC_RIS** (line 22)
- **SPRD_EIC_DBNC_TRIG** (line 25)
- **SPRD_EIC_LATCH_INTCLR** (line 31)
- **SPRD_EIC_LATCH_INTEN** (line 28)
- **SPRD_EIC_LATCH_INTMODE** (line 33)
- **SPRD_EIC_LATCH_INTMSK** (line 30)
- **SPRD_EIC_LATCH_INTPOL** (line 32)
- **SPRD_EIC_LATCH_INTRAW** (line 29)
- **SPRD_EIC_MAX_BANK** (line 57)
- **SPRD_EIC_PER_BANK_NR** (line 58)
- **SPRD_EIC_SYNC_DATA** (line 51)
- **SPRD_EIC_SYNC_INTBOTH** (line 49)
- **SPRD_EIC_SYNC_INTCLR** (line 47)
- **SPRD_EIC_SYNC_INTIE** (line 44)
- **SPRD_EIC_SYNC_INTMODE** (line 48)
- **SPRD_EIC_SYNC_INTMSK** (line 46)
- **SPRD_EIC_SYNC_INTPOL** (line 50)
- **SPRD_EIC_SYNC_INTRAW** (line 45)
