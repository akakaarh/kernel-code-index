# drivers/gpio/gpio-graniterapids.c

Subsystem: drivers/gpio

## Functions (19)

### gnr_gpio_configure_line
- Return type: static int
- Signature: gnr_gpio_configure_line(struct gpio_chip * gc,unsigned int gpio,u32 clear_mask,u32 set_mask)
- Line: 75
- Calls: gnr_gpio_get_padcfg_addr, gpiochip_get_data
- Called by: gnr_gpio_direction_input, gnr_gpio_direction_output, gnr_gpio_irq_set_type, gnr_gpio_set

### gnr_gpio_direction_input
- Return type: static int
- Signature: gnr_gpio_direction_input(struct gpio_chip * gc,unsigned int gpio)
- Line: 145
- Calls: gnr_gpio_configure_line

### gnr_gpio_direction_output
- Return type: static int
- Signature: gnr_gpio_direction_output(struct gpio_chip * gc,unsigned int gpio,int value)
- Line: 150
- Calls: gnr_gpio_configure_line

### gnr_gpio_get
- Return type: static int
- Signature: gnr_gpio_get(struct gpio_chip * gc,unsigned int gpio)
- Line: 109
- Calls: gnr_gpio_get_padcfg_addr, gpiochip_get_data

### gnr_gpio_get_direction
- Return type: static int
- Signature: gnr_gpio_get_direction(struct gpio_chip * gc,unsigned int gpio)
- Line: 132
- Calls: gnr_gpio_get_padcfg_addr, gpiochip_get_data

### gnr_gpio_get_padcfg_addr
- Return type: static void __iomem *
- Signature: gnr_gpio_get_padcfg_addr(const struct gnr_gpio * priv,unsigned int gpio)
- Line: 69
- Called by: gnr_gpio_configure_line, gnr_gpio_get, gnr_gpio_get_direction, gnr_gpio_irq_set_type, gnr_gpio_request, gnr_gpio_resume, gnr_gpio_suspend

### gnr_gpio_get_reg_addr
- Return type: static void __iomem *
- Signature: gnr_gpio_get_reg_addr(const struct gnr_gpio * priv,unsigned int base,unsigned int gpio)
- Line: 168
- Called by: gnr_gpio_irq_ack, gnr_gpio_irq_mask_unmask

### gnr_gpio_init_pin_ro_bits
- Return type: static void
- Signature: gnr_gpio_init_pin_ro_bits(struct device * dev,const void __iomem * cfg_lock_base,unsigned long * ro_bitmap)
- Line: 273
- Called by: gnr_gpio_probe

### gnr_gpio_irq
- Return type: static irqreturn_t
- Signature: gnr_gpio_irq(int irq,void * data)
- Line: 283

### gnr_gpio_irq_ack
- Return type: static void
- Signature: gnr_gpio_irq_ack(struct irq_data * d)
- Line: 175
- Calls: gnr_gpio_get_reg_addr, gpiochip_get_data

### gnr_gpio_irq_mask
- Return type: static void
- Signature: gnr_gpio_irq_mask(struct irq_data * d)
- Line: 210
- Calls: gnr_gpio_irq_mask_unmask, gpiochip_disable_irq

### gnr_gpio_irq_mask_unmask
- Return type: static void
- Signature: gnr_gpio_irq_mask_unmask(struct gpio_chip * gc,unsigned long gpio,bool mask)
- Line: 192
- Calls: gnr_gpio_get_reg_addr, gpiochip_get_data
- Called by: gnr_gpio_irq_mask, gnr_gpio_irq_unmask

### gnr_gpio_irq_set_type
- Return type: static int
- Signature: gnr_gpio_irq_set_type(struct irq_data * d,unsigned int type)
- Line: 228
- Calls: gnr_gpio_configure_line, gnr_gpio_get_padcfg_addr, gpiochip_get_data

### gnr_gpio_irq_unmask
- Return type: static void
- Signature: gnr_gpio_irq_unmask(struct irq_data * d)
- Line: 219
- Calls: gnr_gpio_irq_mask_unmask, gpiochip_enable_irq

### gnr_gpio_probe
- Return type: static int
- Signature: gnr_gpio_probe(struct platform_device * pdev)
- Line: 314
- Calls: gnr_gpio_init_pin_ro_bits

### gnr_gpio_request
- Return type: static int
- Signature: gnr_gpio_request(struct gpio_chip * gc,unsigned int gpio)
- Line: 95
- Calls: gnr_gpio_get_padcfg_addr, gpiochip_get_data

### gnr_gpio_resume
- Return type: static int
- Signature: gnr_gpio_resume(struct device * dev)
- Line: 382
- Calls: gnr_gpio_get_padcfg_addr

### gnr_gpio_set
- Return type: static int
- Signature: gnr_gpio_set(struct gpio_chip * gc,unsigned int gpio,int value)
- Line: 119
- Calls: gnr_gpio_configure_line

### gnr_gpio_suspend
- Return type: static int
- Signature: gnr_gpio_suspend(struct device * dev)
- Line: 369
- Calls: gnr_gpio_get_padcfg_addr

## Structs (1)

### gnr_gpio
- Line: 60
- Members:
  - gc: gpio_chip
  - reg_base: void __iomem *
  - pad_base: void __iomem *
  - lock: raw_spinlock_t
  - pad_backup: u32[]

## Variables (4)

- static **gnr_gpio_acpi_match** : const struct acpi_device_id[] (line 397)
- static **gnr_gpio_chip** : const struct gpio_chip (line 158)
- static **gnr_gpio_driver** : platform_driver (line 403)
- static **gnr_gpio_irq_chip** : const struct irq_chip (line 263)

## Macros (17)

- **GNR_CFG_DW_HOSTSW_MODE** (line 40)
- **GNR_CFG_DW_INTSEL_MASK** (line 42)
- **GNR_CFG_DW_RXDIS** (line 46)
- **GNR_CFG_DW_RXSTATE** (line 48)
- **GNR_CFG_DW_RX_DISABLE** (line 43)
- **GNR_CFG_DW_RX_EDGE** (line 44)
- **GNR_CFG_DW_RX_LEVEL** (line 45)
- **GNR_CFG_DW_RX_MASK** (line 41)
- **GNR_CFG_DW_TXDIS** (line 47)
- **GNR_CFG_DW_TXSTATE** (line 49)
- **GNR_CFG_LOCK_OFFSET** (line 36)
- **GNR_CFG_PADBAR** (line 35)
- **GNR_GPI_ENABLE_OFFSET** (line 38)
- **GNR_GPI_STATUS_OFFSET** (line 37)
- **GNR_NUM_PINS** (line 31)
- **GNR_NUM_REGS** (line 33)
- **GNR_PINS_PER_REG** (line 32)
