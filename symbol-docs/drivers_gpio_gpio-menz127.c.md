# drivers/gpio/gpio-menz127.c

Subsystem: drivers/gpio

## Functions (5)

### men_z127_debounce
- Return type: static int
- Signature: men_z127_debounce(struct gpio_chip * gc,unsigned gpio,unsigned debounce)
- Line: 44
- Calls: gpiochip_get_data
- Called by: men_z127_set_config

### men_z127_probe
- Return type: static int
- Signature: men_z127_probe(struct mcb_device * mdev,const struct mcb_device_id * id)
- Line: 141
- Calls: gpio_generic_chip_init

### men_z127_release_mem
- Return type: static void
- Signature: men_z127_release_mem(void * data)
- Line: 134

### men_z127_set_config
- Return type: static int
- Signature: men_z127_set_config(struct gpio_chip * gc,unsigned offset,unsigned long config)
- Line: 113
- Calls: men_z127_debounce, men_z127_set_single_ended

### men_z127_set_single_ended
- Return type: static int
- Signature: men_z127_set_single_ended(struct gpio_chip * gc,unsigned offset,enum pin_config_param param)
- Line: 91
- Calls: gpiochip_get_data
- Called by: men_z127_set_config

## Structs (1)

### men_z127_gpio
- Line: 38
- Members:
  - chip: gpio_generic_chip
  - reg_base: void __iomem *
  - mem: resource *

## Variables (2)

- static **men_z127_driver** : mcb_driver (line 214)
- static **men_z127_ids** : const struct mcb_device_id[] (line 206)

## Macros (15)

- **GPIO_TO_DBCNT_REG**(gpio) (line 25)
- **MEN_Z034_ID** (line 29)
- **MEN_Z037_ID** (line 30)
- **MEN_Z127_CTRL** (line 17)
- **MEN_Z127_DBER** (line 23)
- **MEN_Z127_DB_IN_RANGE**(db) (line 35)
- **MEN_Z127_DB_MAX_US** (line 34)
- **MEN_Z127_DB_MIN_US** (line 32)
- **MEN_Z127_GPIODR** (line 20)
- **MEN_Z127_ID** (line 28)
- **MEN_Z127_IER1** (line 21)
- **MEN_Z127_IER2** (line 22)
- **MEN_Z127_IRQR** (line 19)
- **MEN_Z127_ODER** (line 24)
- **MEN_Z127_PSR** (line 18)
