# drivers/gpio/gpio-bcm-kona.c

Subsystem: drivers/gpio

## Functions (24)

### bcm_kona_gpio_direction_input
- Return type: static int
- Signature: bcm_kona_gpio_direction_input(struct gpio_chip * chip,unsigned gpio)
- Line: 219
- Calls: gpiochip_get_data

### bcm_kona_gpio_direction_output
- Return type: static int
- Signature: bcm_kona_gpio_direction_output(struct gpio_chip * chip,unsigned gpio,int value)
- Line: 238
- Calls: gpiochip_get_data

### bcm_kona_gpio_free
- Return type: static void
- Signature: bcm_kona_gpio_free(struct gpio_chip * chip,unsigned gpio)
- Line: 212
- Calls: bcm_kona_gpio_lock_gpio, gpiochip_get_data

### bcm_kona_gpio_get
- Return type: static int
- Signature: bcm_kona_gpio_get(struct gpio_chip * chip,unsigned gpio)
- Line: 179
- Calls: bcm_kona_gpio_get_dir, gpiochip_get_data

### bcm_kona_gpio_get_dir
- Return type: static int
- Signature: bcm_kona_gpio_get_dir(struct gpio_chip * chip,unsigned gpio)
- Line: 142
- Calls: gpiochip_get_data
- Called by: bcm_kona_gpio_get, bcm_kona_gpio_set

### bcm_kona_gpio_irq_ack
- Return type: static void
- Signature: bcm_kona_gpio_irq_ack(struct irq_data * d)
- Line: 348

### bcm_kona_gpio_irq_handler
- Return type: static void
- Signature: bcm_kona_gpio_irq_handler(struct irq_desc * desc)
- Line: 449

### bcm_kona_gpio_irq_map
- Return type: static int
- Signature: bcm_kona_gpio_irq_map(struct irq_domain * d,unsigned int irq,irq_hw_number_t hwirq)
- Line: 534

### bcm_kona_gpio_irq_mask
- Return type: static void
- Signature: bcm_kona_gpio_irq_mask(struct irq_data * d)
- Line: 367
- Calls: gpiochip_disable_irq

### bcm_kona_gpio_irq_relres
- Return type: static void
- Signature: bcm_kona_gpio_irq_relres(struct irq_data * d)
- Line: 500
- Calls: bcm_kona_gpio_lock_gpio, gpiochip_relres_irq

### bcm_kona_gpio_irq_reqres
- Return type: static int
- Signature: bcm_kona_gpio_irq_reqres(struct irq_data * d)
- Line: 486
- Calls: bcm_kona_gpio_unlock_gpio, gpiochip_reqres_irq

### bcm_kona_gpio_irq_set_type
- Return type: static int
- Signature: bcm_kona_gpio_irq_set_type(struct irq_data * d,unsigned int type)
- Line: 407

### bcm_kona_gpio_irq_unmap
- Return type: static void
- Signature: bcm_kona_gpio_irq_unmap(struct irq_domain * d,unsigned int irq)
- Line: 549

### bcm_kona_gpio_irq_unmask
- Return type: static void
- Signature: bcm_kona_gpio_irq_unmask(struct irq_data * d)
- Line: 387
- Calls: gpiochip_enable_irq

### bcm_kona_gpio_lock_gpio
- Return type: static void
- Signature: bcm_kona_gpio_lock_gpio(struct bcm_kona_gpio * kona_gpio,unsigned gpio)
- Line: 100
- Calls: bcm_kona_gpio_write_lock_regs
- Called by: bcm_kona_gpio_free, bcm_kona_gpio_irq_relres

### bcm_kona_gpio_probe
- Return type: static int
- Signature: bcm_kona_gpio_probe(struct platform_device * pdev)
- Line: 578
- Calls: bcm_kona_gpio_reset

### bcm_kona_gpio_request
- Return type: static int
- Signature: bcm_kona_gpio_request(struct gpio_chip * chip,unsigned gpio)
- Line: 204
- Calls: bcm_kona_gpio_unlock_gpio, gpiochip_get_data

### bcm_kona_gpio_reset
- Return type: static void
- Signature: bcm_kona_gpio_reset(struct bcm_kona_gpio * kona_gpio)
- Line: 561
- Calls: bcm_kona_gpio_write_lock_regs
- Called by: bcm_kona_gpio_probe

### bcm_kona_gpio_set
- Return type: static int
- Signature: bcm_kona_gpio_set(struct gpio_chip * chip,unsigned int gpio,int value)
- Line: 152
- Calls: bcm_kona_gpio_get_dir, gpiochip_get_data

### bcm_kona_gpio_set_config
- Return type: static int
- Signature: bcm_kona_gpio_set_config(struct gpio_chip * chip,unsigned gpio,unsigned long config)
- Line: 321
- Calls: bcm_kona_gpio_set_debounce

### bcm_kona_gpio_set_debounce
- Return type: static int
- Signature: bcm_kona_gpio_set_debounce(struct gpio_chip * chip,unsigned gpio,unsigned debounce)
- Line: 275
- Calls: gpiochip_get_data
- Called by: bcm_kona_gpio_set_config

### bcm_kona_gpio_to_irq
- Return type: static int
- Signature: bcm_kona_gpio_to_irq(struct gpio_chip * chip,unsigned gpio)
- Line: 265
- Calls: gpiochip_get_data

### bcm_kona_gpio_unlock_gpio
- Return type: static void
- Signature: bcm_kona_gpio_unlock_gpio(struct bcm_kona_gpio * kona_gpio,unsigned gpio)
- Line: 123
- Calls: bcm_kona_gpio_write_lock_regs
- Called by: bcm_kona_gpio_irq_reqres, bcm_kona_gpio_request

### bcm_kona_gpio_write_lock_regs
- Return type: static void
- Signature: bcm_kona_gpio_write_lock_regs(void __iomem * reg_base,int bank_id,u32 lockcode)
- Line: 93
- Called by: bcm_kona_gpio_lock_gpio, bcm_kona_gpio_reset, bcm_kona_gpio_unlock_gpio

## Structs (2)

### bcm_kona_gpio
- Line: 84
- Members:
  - id: int
  - irq: int
  - gpio_unlock_count: u8[]
  - kona_gpio: bcm_kona_gpio *
  - reg_base: void __iomem *
  - num_bank: int
  - lock: raw_spinlock_t
  - gpio_chip: gpio_chip
  - irq_domain: irq_domain *

### bcm_kona_gpio_bank
- Line: 61
- Members:
  - id: int
  - irq: int
  - gpio_unlock_count: u8[]
  - kona_gpio: bcm_kona_gpio *
  - reg_base: void __iomem *
  - num_bank: int
  - lock: raw_spinlock_t
  - gpio_chip: gpio_chip
  - irq_domain: irq_domain *

## Variables (7)

- static **bcm_gpio_irq_chip** : irq_chip (line 511)
- static **bcm_kona_gpio_driver** : platform_driver (line 665)
- static **bcm_kona_gpio_of_match** : of_device_id const[] (line 522)
- static **bcm_kona_irq_ops** : const struct irq_domain_ops (line 555)
- static **gpio_lock_class** : lock_class_key (line 531)
- static **gpio_request_class** : lock_class_key (line 532)
- static **template_chip** : const struct gpio_chip (line 333)

## Macros (28)

- **BCM_GPIO_PASSWD** (line 21)
- **GPIO_BANK**(gpio) (line 25)
- **GPIO_BIT**(gpio) (line 26)
- **GPIO_CONTROL**(gpio) (line 29)
- **GPIO_GPCTR0_DBR_MASK** (line 44)
- **GPIO_GPCTR0_DBR_SHIFT** (line 43)
- **GPIO_GPCTR0_DB_ENABLE_MASK** (line 56)
- **GPIO_GPCTR0_IOTR_CMD_0UTPUT** (line 53)
- **GPIO_GPCTR0_IOTR_CMD_INPUT** (line 54)
- **GPIO_GPCTR0_IOTR_MASK** (line 52)
- **GPIO_GPCTR0_ITR_CMD_BOTH_EDGE** (line 50)
- **GPIO_GPCTR0_ITR_CMD_FALLING_EDGE** (line 49)
- **GPIO_GPCTR0_ITR_CMD_RISING_EDGE** (line 48)
- **GPIO_GPCTR0_ITR_MASK** (line 47)
- **GPIO_GPCTR0_ITR_SHIFT** (line 46)
- **GPIO_GPPWR_OFFSET** (line 41)
- **GPIO_INT_MASK**(bank) (line 37)
- **GPIO_INT_MSKCLR**(bank) (line 38)
- **GPIO_INT_STATUS**(bank) (line 36)
- **GPIO_IN_STATUS**(bank) (line 33)
- **GPIO_MAX_BANK_NUM** (line 23)
- **GPIO_OUT_CLEAR**(bank) (line 35)
- **GPIO_OUT_SET**(bank) (line 34)
- **GPIO_OUT_STATUS**(bank) (line 32)
- **GPIO_PER_BANK** (line 22)
- **GPIO_PWD_STATUS**(bank) (line 39)
- **LOCK_CODE** (line 58)
- **UNLOCK_CODE** (line 59)
