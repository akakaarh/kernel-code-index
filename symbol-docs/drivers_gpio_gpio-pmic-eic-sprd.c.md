# drivers/gpio/gpio-pmic-eic-sprd.c

Subsystem: drivers/gpio

## Functions (16)

### sprd_pmic_eic_bus_lock
- Return type: static void
- Signature: sprd_pmic_eic_bus_lock(struct irq_data * data)
- Line: 195
- Calls: gpiochip_get_data

### sprd_pmic_eic_bus_sync_unlock
- Return type: static void
- Signature: sprd_pmic_eic_bus_sync_unlock(struct irq_data * data)
- Line: 203
- Calls: gpiochip_get_data, sprd_pmic_eic_get, sprd_pmic_eic_update

### sprd_pmic_eic_direction_input
- Return type: static int
- Signature: sprd_pmic_eic_direction_input(struct gpio_chip * chip,unsigned int offset)
- Line: 105

### sprd_pmic_eic_free
- Return type: static void
- Signature: sprd_pmic_eic_free(struct gpio_chip * chip,unsigned int offset)
- Line: 95
- Calls: sprd_pmic_eic_update

### sprd_pmic_eic_get
- Return type: static int
- Signature: sprd_pmic_eic_get(struct gpio_chip * chip,unsigned int offset)
- Line: 100
- Calls: sprd_pmic_eic_read
- Called by: sprd_pmic_eic_bus_sync_unlock, sprd_pmic_eic_toggle_trigger

### sprd_pmic_eic_irq_handler
- Return type: static irqreturn_t
- Signature: sprd_pmic_eic_irq_handler(int irq,void * data)
- Line: 262
- Calls: sprd_pmic_eic_toggle_trigger, sprd_pmic_eic_update

### sprd_pmic_eic_irq_mask
- Return type: static void
- Signature: sprd_pmic_eic_irq_mask(struct irq_data * data)
- Line: 142
- Calls: gpiochip_disable_irq, gpiochip_get_data

### sprd_pmic_eic_irq_set_type
- Return type: static int
- Signature: sprd_pmic_eic_irq_set_type(struct irq_data * data,unsigned int flow_type)
- Line: 166
- Calls: gpiochip_get_data

### sprd_pmic_eic_irq_unmask
- Return type: static void
- Signature: sprd_pmic_eic_irq_unmask(struct irq_data * data)
- Line: 154
- Calls: gpiochip_enable_irq, gpiochip_get_data

### sprd_pmic_eic_probe
- Return type: static int
- Signature: sprd_pmic_eic_probe(struct platform_device * pdev)
- Line: 305

### sprd_pmic_eic_read
- Return type: static int
- Signature: sprd_pmic_eic_read(struct gpio_chip * chip,unsigned int offset,u16 reg)
- Line: 75
- Calls: gpiochip_get_data
- Called by: sprd_pmic_eic_get

### sprd_pmic_eic_request
- Return type: static int
- Signature: sprd_pmic_eic_request(struct gpio_chip * chip,unsigned int offset)
- Line: 89
- Calls: sprd_pmic_eic_update

### sprd_pmic_eic_set_config
- Return type: static int
- Signature: sprd_pmic_eic_set_config(struct gpio_chip * chip,unsigned int offset,unsigned long config)
- Line: 130
- Calls: sprd_pmic_eic_set_debounce

### sprd_pmic_eic_set_debounce
- Return type: static int
- Signature: sprd_pmic_eic_set_debounce(struct gpio_chip * chip,unsigned int offset,unsigned int debounce)
- Line: 112
- Calls: gpiochip_get_data
- Called by: sprd_pmic_eic_set_config

### sprd_pmic_eic_toggle_trigger
- Return type: static void
- Signature: sprd_pmic_eic_toggle_trigger(struct gpio_chip * chip,unsigned int irq,unsigned int offset)
- Line: 233
- Calls: sprd_pmic_eic_get, sprd_pmic_eic_update
- Called by: sprd_pmic_eic_irq_handler

### sprd_pmic_eic_update
- Return type: static void
- Signature: sprd_pmic_eic_update(struct gpio_chip * chip,unsigned int offset,u16 reg,unsigned int val)
- Line: 65
- Calls: gpiochip_get_data
- Called by: sprd_pmic_eic_bus_sync_unlock, sprd_pmic_eic_free, sprd_pmic_eic_irq_handler, sprd_pmic_eic_request, sprd_pmic_eic_toggle_trigger

## Structs (1)

### sprd_pmic_eic
- Line: 56
- Members:
  - chip: gpio_chip
  - map: regmap *
  - offset: u32
  - reg: u8[]
  - buslock: mutex
  - irq: int

## Enums (1)

### __anoncc50a8d50103
- Line: 40

## Variables (3)

- static **pmic_eic_irq_chip** : const struct irq_chip (line 294)
- static **sprd_pmic_eic_driver** : platform_driver (line 370)
- static **sprd_pmic_eic_of_match** : const struct of_device_id[] (line 364)

## Macros (14)

- **SPRD_PMIC_EIC_BIT**(x) (line 33)
- **SPRD_PMIC_EIC_CTRL0** (line 24)
- **SPRD_PMIC_EIC_DATA** (line 16)
- **SPRD_PMIC_EIC_DATA_MASK** (line 32)
- **SPRD_PMIC_EIC_DBNC_MASK** (line 34)
- **SPRD_PMIC_EIC_DMSK** (line 17)
- **SPRD_PMIC_EIC_IC** (line 22)
- **SPRD_PMIC_EIC_IE** (line 19)
- **SPRD_PMIC_EIC_IEV** (line 18)
- **SPRD_PMIC_EIC_MIS** (line 21)
- **SPRD_PMIC_EIC_NR** (line 31)
- **SPRD_PMIC_EIC_PER_BANK_NR** (line 30)
- **SPRD_PMIC_EIC_RIS** (line 20)
- **SPRD_PMIC_EIC_TRIG** (line 23)
