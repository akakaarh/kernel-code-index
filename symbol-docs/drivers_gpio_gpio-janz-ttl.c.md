# drivers/gpio/gpio-janz-ttl.c

Subsystem: drivers/gpio

## Functions (5)

### ttl_get_value
- Return type: static int
- Signature: ttl_get_value(struct gpio_chip * gpio,unsigned offset)
- Line: 57

### ttl_probe
- Return type: static int
- Signature: ttl_probe(struct platform_device * pdev)
- Line: 142
- Calls: ttl_setup_device

### ttl_set_value
- Return type: static int
- Signature: ttl_set_value(struct gpio_chip * gpio,unsigned int offset,int value)
- Line: 79

### ttl_setup_device
- Return type: static void
- Signature: ttl_setup_device(struct ttl_module * mod)
- Line: 116
- Calls: ttl_write_reg
- Called by: ttl_probe

### ttl_write_reg
- Return type: static void
- Signature: ttl_write_reg(struct ttl_module * mod,u8 reg,u16 val)
- Line: 110
- Called by: ttl_setup_device

## Structs (2)

### ttl_control_regs
- Line: 37
- Members:
  - portc: __be16
  - portb: __be16
  - porta: __be16
  - control: __be16
  - gpio: gpio_chip
  - regs: ttl_control_regs __iomem *
  - portc_shadow: u8
  - portb_shadow: u8
  - porta_shadow: u8
  - lock: spinlock_t

### ttl_module
- Line: 44
- Members:
  - portc: __be16
  - portb: __be16
  - porta: __be16
  - control: __be16
  - gpio: gpio_chip
  - regs: ttl_control_regs __iomem *
  - portc_shadow: u8
  - portb_shadow: u8
  - porta_shadow: u8
  - lock: spinlock_t

## Variables (1)

- static **ttl_driver** : platform_driver (line 190)

## Macros (12)

- **CONF_PAE** (line 33)
- **CONF_PBE** (line 34)
- **CONF_PCE** (line 35)
- **DRV_NAME** (line 21)
- **MASTER_CONF_CTL** (line 31)
- **MASTER_INT_CTL** (line 30)
- **PORTA_DIRECTION** (line 23)
- **PORTA_IOCTL** (line 26)
- **PORTB_DIRECTION** (line 24)
- **PORTB_IOCTL** (line 27)
- **PORTC_DIRECTION** (line 25)
- **PORTC_IOCTL** (line 28)
