# drivers/gpio/gpio-sch.c

Subsystem: drivers/gpio

## Functions (18)

### sch_gpio_bit
- Return type: static unsigned int
- Signature: sch_gpio_bit(struct sch_gpio * sch,unsigned int gpio)
- Line: 63
- Called by: sch_gpio_reg_get, sch_gpio_reg_set

### sch_gpio_direction_in
- Return type: static int
- Signature: sch_gpio_direction_in(struct gpio_chip * gc,unsigned int gpio_num)
- Line: 102
- Calls: gpiochip_get_data, sch_gpio_reg_set

### sch_gpio_direction_out
- Return type: static int
- Signature: sch_gpio_direction_out(struct gpio_chip * gc,unsigned int gpio_num,int val)
- Line: 132
- Calls: gpiochip_get_data, sch_gpio_reg_set, sch_gpio_set

### sch_gpio_get
- Return type: static int
- Signature: sch_gpio_get(struct gpio_chip * gc,unsigned int gpio_num)
- Line: 113
- Calls: gpiochip_get_data, sch_gpio_reg_get

### sch_gpio_get_direction
- Return type: static int
- Signature: sch_gpio_get_direction(struct gpio_chip * gc,unsigned int gpio_num)
- Line: 154
- Calls: gpiochip_get_data, sch_gpio_reg_get

### sch_gpio_gpe_handler
- Return type: static u32
- Signature: sch_gpio_gpe_handler(acpi_handle gpe_device,u32 gpe,void * context)
- Line: 261

### sch_gpio_install_gpe_handler
- Return type: static int
- Signature: sch_gpio_install_gpe_handler(struct sch_gpio * sch)
- Line: 299
- Called by: sch_gpio_probe

### sch_gpio_offset
- Return type: static unsigned int
- Signature: sch_gpio_offset(struct sch_gpio * sch,unsigned int gpio,unsigned int reg)
- Line: 50
- Called by: sch_gpio_reg_get, sch_gpio_reg_set

### sch_gpio_probe
- Return type: static int
- Signature: sch_gpio_probe(struct platform_device * pdev)
- Line: 323
- Calls: sch_gpio_install_gpe_handler, sch_gpio_reg_set

### sch_gpio_reg_get
- Return type: static int
- Signature: sch_gpio_reg_get(struct sch_gpio * sch,unsigned int gpio,unsigned int reg)
- Line: 70
- Calls: sch_gpio_bit, sch_gpio_offset
- Called by: sch_gpio_get, sch_gpio_get_direction

### sch_gpio_reg_set
- Return type: static void
- Signature: sch_gpio_reg_set(struct sch_gpio * sch,unsigned int gpio,unsigned int reg,int val)
- Line: 83
- Calls: sch_gpio_bit, sch_gpio_offset
- Called by: sch_gpio_direction_in, sch_gpio_direction_out, sch_gpio_probe, sch_gpio_set, sch_irq_ack, sch_irq_mask_unmask, sch_irq_type

### sch_gpio_remove_gpe_handler
- Return type: static void
- Signature: sch_gpio_remove_gpe_handler(void * data)
- Line: 291

### sch_gpio_set
- Return type: static int
- Signature: sch_gpio_set(struct gpio_chip * gc,unsigned int gpio_num,int val)
- Line: 120
- Calls: gpiochip_get_data, sch_gpio_reg_set
- Called by: sch_gpio_direction_out

### sch_irq_ack
- Return type: static void
- Signature: sch_irq_ack(struct irq_data * d)
- Line: 211
- Calls: gpiochip_get_data, sch_gpio_reg_set

### sch_irq_mask
- Return type: static void
- Signature: sch_irq_mask(struct irq_data * d)
- Line: 233
- Calls: gpiochip_disable_irq, sch_irq_mask_unmask

### sch_irq_mask_unmask
- Return type: static void
- Signature: sch_irq_mask_unmask(struct gpio_chip * gc,irq_hw_number_t gpio_num,int val)
- Line: 223
- Calls: gpiochip_get_data, sch_gpio_reg_set
- Called by: sch_irq_mask, sch_irq_unmask

### sch_irq_type
- Return type: static int
- Signature: sch_irq_type(struct irq_data * d,unsigned int type)
- Line: 174
- Calls: gpiochip_get_data, sch_gpio_reg_set

### sch_irq_unmask
- Return type: static void
- Signature: sch_irq_unmask(struct irq_data * d)
- Line: 242
- Calls: gpiochip_enable_irq, sch_irq_mask_unmask

## Structs (1)

### sch_gpio
- Line: 39
- Members:
  - chip: gpio_chip
  - regs: void __iomem *
  - lock: spinlock_t
  - resume_base: unsigned short
  - gpe: u32
  - gpe_handler: acpi_gpe_handler

## Variables (3)

- static **sch_gpio_chip** : const struct gpio_chip (line 164)
- static **sch_gpio_driver** : platform_driver (line 408)
- static **sch_irqchip** : const struct irq_chip (line 251)

## Macros (11)

- **CORE_BANK_OFFSET** (line 30)
- **GEN** (line 21)
- **GGPE** (line 26)
- **GIO** (line 22)
- **GLV** (line 23)
- **GPE0E_GPIO** (line 37)
- **GSMI** (line 27)
- **GTNE** (line 25)
- **GTPE** (line 24)
- **GTS** (line 28)
- **RESUME_BANK_OFFSET** (line 31)
