# drivers/gpio/gpio-thunderx.c

Subsystem: drivers/gpio

## Functions (23)

### bit_cfg_reg
- Return type: static unsigned int
- Signature: bit_cfg_reg(unsigned int line)
- Line: 64
- Called by: octeon_gpio_dir_in, octeon_gpio_dir_out, thunderx_gpio_dir_in, thunderx_gpio_dir_out, thunderx_gpio_get_direction, thunderx_gpio_irq_set_type, thunderx_gpio_is_gpio_nowarn, thunderx_gpio_probe, thunderx_gpio_set_config

### intr_reg
- Return type: static unsigned int
- Signature: intr_reg(unsigned int line)
- Line: 69
- Called by: thunderx_gpio_irq_ack, thunderx_gpio_irq_mask, thunderx_gpio_irq_mask_ack, thunderx_gpio_irq_unmask

### thunderx_gpio_child_to_parent_hwirq
- Return type: static int
- Signature: thunderx_gpio_child_to_parent_hwirq(struct gpio_chip * gc,unsigned int child,unsigned int child_type,unsigned int * parent,unsigned int * parent_type)
- Line: 401
- Calls: gpiochip_get_data

### thunderx_gpio_dir_in
- Return type: static int
- Signature: thunderx_gpio_dir_in(struct gpio_chip * chip,unsigned int line)
- Line: 103
- Calls: bit_cfg_reg, gpiochip_get_data, thunderx_gpio_is_gpio

### thunderx_gpio_dir_out
- Return type: static int
- Signature: thunderx_gpio_dir_out(struct gpio_chip * chip,unsigned int line,int value)
- Line: 134
- Calls: bit_cfg_reg, gpiochip_get_data, thunderx_gpio_is_gpio, thunderx_gpio_set
- Called by: thunderx_gpio_set_config

### thunderx_gpio_get
- Return type: static int
- Signature: thunderx_gpio_get(struct gpio_chip * chip,unsigned int line)
- Line: 260
- Calls: gpiochip_get_data

### thunderx_gpio_get_direction
- Return type: static int
- Signature: thunderx_gpio_get_direction(struct gpio_chip * chip,unsigned int line)
- Line: 159
- Calls: bit_cfg_reg, gpiochip_get_data, thunderx_gpio_is_gpio_nowarn

### thunderx_gpio_irq_ack
- Return type: static void
- Signature: thunderx_gpio_irq_ack(struct irq_data * d)
- Line: 292
- Calls: gpiochip_get_data, intr_reg

### thunderx_gpio_irq_disable
- Return type: static void
- Signature: thunderx_gpio_irq_disable(struct irq_data * d)
- Line: 371
- Calls: gpiochip_disable_irq, thunderx_gpio_irq_mask

### thunderx_gpio_irq_enable
- Return type: static void
- Signature: thunderx_gpio_irq_enable(struct irq_data * d)
- Line: 362
- Calls: gpiochip_enable_irq, thunderx_gpio_irq_unmask

### thunderx_gpio_irq_mask
- Return type: static void
- Signature: thunderx_gpio_irq_mask(struct irq_data * d)
- Line: 301
- Calls: gpiochip_get_data, intr_reg
- Called by: thunderx_gpio_irq_disable

### thunderx_gpio_irq_mask_ack
- Return type: static void
- Signature: thunderx_gpio_irq_mask_ack(struct irq_data * d)
- Line: 310
- Calls: gpiochip_get_data, intr_reg

### thunderx_gpio_irq_set_type
- Return type: static int
- Signature: thunderx_gpio_irq_set_type(struct irq_data * d,unsigned int flow_type)
- Line: 328
- Calls: bit_cfg_reg, gpiochip_get_data

### thunderx_gpio_irq_unmask
- Return type: static void
- Signature: thunderx_gpio_irq_unmask(struct irq_data * d)
- Line: 319
- Calls: gpiochip_get_data, intr_reg
- Called by: thunderx_gpio_irq_enable

### thunderx_gpio_is_gpio
- Return type: static bool
- Signature: thunderx_gpio_is_gpio(struct thunderx_gpio * txgpio,unsigned int line)
- Line: 86
- Calls: thunderx_gpio_is_gpio_nowarn
- Called by: thunderx_gpio_dir_in, thunderx_gpio_dir_out, thunderx_gpio_request, thunderx_gpio_set_config

### thunderx_gpio_is_gpio_nowarn
- Return type: static bool
- Signature: thunderx_gpio_is_gpio_nowarn(struct thunderx_gpio * txgpio,unsigned int line)
- Line: 74
- Calls: bit_cfg_reg
- Called by: thunderx_gpio_get_direction, thunderx_gpio_is_gpio

### thunderx_gpio_populate_parent_alloc_info
- Return type: static int
- Signature: thunderx_gpio_populate_parent_alloc_info(struct gpio_chip * chip,union gpio_irq_fwspec * gfwspec,unsigned int parent_hwirq,unsigned int parent_type)
- Line: 420

### thunderx_gpio_probe
- Return type: static int
- Signature: thunderx_gpio_probe(struct pci_dev * pdev,const struct pci_device_id * id)
- Line: 431
- Calls: bit_cfg_reg

### thunderx_gpio_remove
- Return type: static void
- Signature: thunderx_gpio_remove(struct pci_dev * pdev)
- Line: 576

### thunderx_gpio_request
- Return type: static int
- Signature: thunderx_gpio_request(struct gpio_chip * chip,unsigned int line)
- Line: 96
- Calls: gpiochip_get_data, thunderx_gpio_is_gpio

### thunderx_gpio_set
- Return type: static int
- Signature: thunderx_gpio_set(struct gpio_chip * chip,unsigned int line,int value)
- Line: 119
- Calls: gpiochip_get_data
- Called by: thunderx_gpio_dir_out

### thunderx_gpio_set_config
- Return type: static int
- Signature: thunderx_gpio_set_config(struct gpio_chip * chip,unsigned int line,unsigned long cfg)
- Line: 180
- Calls: bit_cfg_reg, gpiochip_get_data, thunderx_gpio_dir_out, thunderx_gpio_is_gpio

### thunderx_gpio_set_multiple
- Return type: static int
- Signature: thunderx_gpio_set_multiple(struct gpio_chip * chip,unsigned long * mask,unsigned long * bits)
- Line: 274
- Calls: gpiochip_get_data

## Structs (2)

### thunderx_gpio
- Line: 53
- Members:
  - txgpio: thunderx_gpio *
  - line: unsigned int
  - fil_bits: unsigned int
  - chip: gpio_chip
  - register_base: u8 __iomem *
  - msix_entries: msix_entry *
  - line_entries: thunderx_line *
  - lock: raw_spinlock_t
  - invert_mask: unsigned long[2]
  - od_mask: unsigned long[2]
  - base_msi: int

### thunderx_line
- Line: 47
- Members:
  - txgpio: thunderx_gpio *
  - line: unsigned int
  - fil_bits: unsigned int
  - chip: gpio_chip
  - register_base: u8 __iomem *
  - msix_entries: msix_entry *
  - line_entries: thunderx_line *
  - lock: raw_spinlock_t
  - invert_mask: unsigned long[2]
  - od_mask: unsigned long[2]
  - base_msi: int

## Variables (3)

- static **thunderx_gpio_driver** : pci_driver (line 597)
- static **thunderx_gpio_id_table** : const struct pci_device_id[] (line 590)
- static **thunderx_gpio_irq_chip** : const struct irq_chip (line 386)

## Macros (22)

- **GLITCH_FILTER_400NS** (line 42)
- **GPIO_2ND_BANK** (line 40)
- **GPIO_BIT_CFG** (line 25)
- **GPIO_BIT_CFG_FIL_CNT_SHIFT** (line 31)
- **GPIO_BIT_CFG_FIL_MASK** (line 30)
- **GPIO_BIT_CFG_FIL_SEL_SHIFT** (line 32)
- **GPIO_BIT_CFG_INT_EN** (line 28)
- **GPIO_BIT_CFG_INT_TYPE** (line 29)
- **GPIO_BIT_CFG_PIN_SEL_MASK** (line 34)
- **GPIO_BIT_CFG_PIN_XOR** (line 27)
- **GPIO_BIT_CFG_TX_OD** (line 33)
- **GPIO_BIT_CFG_TX_OE** (line 26)
- **GPIO_CONST** (line 23)
- **GPIO_CONST_GPIOS_MASK** (line 24)
- **GPIO_INTR** (line 35)
- **GPIO_INTR_ENA_W1C** (line 38)
- **GPIO_INTR_ENA_W1S** (line 39)
- **GPIO_INTR_INTR** (line 36)
- **GPIO_INTR_INTR_W1S** (line 37)
- **GPIO_RX_DAT** (line 20)
- **GPIO_TX_CLR** (line 22)
- **GPIO_TX_SET** (line 21)
