# drivers/gpio/gpio-spacemit-k1.c

Subsystem: drivers/gpio

## Functions (12)

### spacemit_gpio_add_bank
- Return type: static int
- Signature: spacemit_gpio_add_bank(struct spacemit_gpio * sg,void __iomem * regs,int index,int irq)
- Line: 193
- Calls: gpio_generic_chip_init, spacemit_gpio_write
- Called by: spacemit_gpio_probe

### spacemit_gpio_bank_index
- Return type: static u32
- Signature: spacemit_gpio_bank_index(struct spacemit_gpio_bank * gb)
- Line: 76
- Called by: spacemit_gpio_irq_print_chip

### spacemit_gpio_irq_ack
- Return type: static void
- Signature: spacemit_gpio_irq_ack(struct irq_data * d)
- Line: 102
- Calls: spacemit_gpio_write

### spacemit_gpio_irq_handler
- Return type: static irqreturn_t
- Signature: spacemit_gpio_irq_handler(int irq,void * dev_id)
- Line: 81
- Calls: spacemit_gpio_read, spacemit_gpio_write

### spacemit_gpio_irq_mask
- Return type: static void
- Signature: spacemit_gpio_irq_mask(struct irq_data * d)
- Line: 109
- Calls: spacemit_gpio_write

### spacemit_gpio_irq_print_chip
- Return type: static void
- Signature: spacemit_gpio_irq_print_chip(struct irq_data * data,struct seq_file * p)
- Line: 164
- Calls: spacemit_gpio_bank_index

### spacemit_gpio_irq_set_type
- Return type: static int
- Signature: spacemit_gpio_irq_set_type(struct irq_data * d,unsigned int type)
- Line: 140
- Calls: spacemit_gpio_write

### spacemit_gpio_irq_unmask
- Return type: static void
- Signature: spacemit_gpio_irq_unmask(struct irq_data * d)
- Line: 124
- Calls: spacemit_gpio_write

### spacemit_gpio_probe
- Return type: static int
- Signature: spacemit_gpio_probe(struct platform_device * pdev)
- Line: 269
- Calls: spacemit_gpio_add_bank

### spacemit_gpio_read
- Return type: static u32
- Signature: spacemit_gpio_read(struct spacemit_gpio_bank * gb,enum spacemit_gpio_registers reg)
- Line: 64
- Called by: spacemit_gpio_irq_handler

### spacemit_gpio_write
- Return type: static void
- Signature: spacemit_gpio_write(struct spacemit_gpio_bank * gb,enum spacemit_gpio_registers reg,u32 val)
- Line: 70
- Called by: spacemit_gpio_add_bank, spacemit_gpio_irq_ack, spacemit_gpio_irq_handler, spacemit_gpio_irq_mask, spacemit_gpio_irq_set_type, spacemit_gpio_irq_unmask

### spacemit_of_node_instance_match
- Return type: static bool
- Signature: spacemit_of_node_instance_match(struct gpio_chip * gc,unsigned int i)
- Line: 182
- Calls: gpiochip_get_data

## Structs (3)

### spacemit_gpio
- Line: 58
- Members:
  - offsets: const unsigned int *
  - bank_offsets: u32[]
  - chip: gpio_generic_chip
  - sg: spacemit_gpio *
  - base: void __iomem *
  - irq_mask: u32
  - irq_rising_edge: u32
  - irq_falling_edge: u32
  - dev: device *
  - data: const struct spacemit_gpio_data *
  - sgb: spacemit_gpio_bank[]

### spacemit_gpio_bank
- Line: 49
- Members:
  - offsets: const unsigned int *
  - bank_offsets: u32[]
  - chip: gpio_generic_chip
  - sg: spacemit_gpio *
  - base: void __iomem *
  - irq_mask: u32
  - irq_rising_edge: u32
  - irq_falling_edge: u32
  - dev: device *
  - data: const struct spacemit_gpio_data *
  - sgb: spacemit_gpio_bank[]

### spacemit_gpio_data
- Line: 44
- Members:
  - offsets: const unsigned int *
  - bank_offsets: u32[]
  - chip: gpio_generic_chip
  - sg: spacemit_gpio *
  - base: void __iomem *
  - irq_mask: u32
  - irq_rising_edge: u32
  - irq_falling_edge: u32
  - dev: device *
  - data: const struct spacemit_gpio_data *
  - sgb: spacemit_gpio_bank[]

## Enums (1)

### spacemit_gpio_registers
- Line: 24

## Variables (7)

- static **k1_gpio_data** : const struct spacemit_gpio_data (line 348)
- static **k3_gpio_data** : const struct spacemit_gpio_data (line 353)
- static **spacemit_gpio_chip** : irq_chip (line 171)
- static **spacemit_gpio_driver** : platform_driver (line 365)
- static **spacemit_gpio_dt_ids** : const struct of_device_id[] (line 358)
- static **spacemit_gpio_k1_offsets** : const unsigned int[] (line 312)
- static **spacemit_gpio_k3_offsets** : const unsigned int[] (line 330)

## Macros (4)

- **SPACEMIT_NR_BANKS** (line 18)
- **SPACEMIT_NR_GPIOS_PER_BANK** (line 19)
- **to_spacemit_gpio_bank**(x) (line 21)
- **to_spacemit_gpio_regs**(gb) (line 22)
