# drivers/gpio/gpio-stmpe.c

Subsystem: drivers/gpio

## Functions (19)

### stmpe_dbg_show
- Return type: static void
- Signature: stmpe_dbg_show(struct seq_file * s,struct gpio_chip * gc)
- Line: 365
- Calls: stmpe_dbg_show_one

### stmpe_dbg_show_one
- Return type: static void
- Signature: stmpe_dbg_show_one(struct seq_file * s,struct gpio_chip * gc,unsigned int offset)
- Line: 265
- Calls: gpiochip_dup_line_label, gpiochip_get_data, stmpe_gpio_get
- Called by: stmpe_dbg_show

### stmpe_gpio_direction_input
- Return type: static int
- Signature: stmpe_gpio_direction_input(struct gpio_chip * chip,unsigned offset)
- Line: 110
- Calls: gpiochip_get_data

### stmpe_gpio_direction_output
- Return type: static int
- Signature: stmpe_gpio_direction_output(struct gpio_chip * chip,unsigned offset,int val)
- Line: 94
- Calls: gpiochip_get_data, stmpe_gpio_set

### stmpe_gpio_disable
- Return type: static void
- Signature: stmpe_gpio_disable(void * stmpe)
- Line: 469

### stmpe_gpio_exit
- Return type: static void __exit
- Signature: stmpe_gpio_exit(void)
- Line: 555

### stmpe_gpio_get
- Return type: static int
- Signature: stmpe_gpio_get(struct gpio_chip * chip,unsigned offset)
- Line: 42
- Calls: gpiochip_get_data
- Called by: stmpe_dbg_show_one

### stmpe_gpio_get_direction
- Return type: static int
- Signature: stmpe_gpio_get_direction(struct gpio_chip * chip,unsigned offset)
- Line: 75
- Calls: gpiochip_get_data

### stmpe_gpio_init
- Return type: static int __init
- Signature: stmpe_gpio_init(void)
- Line: 549

### stmpe_gpio_irq
- Return type: static irqreturn_t
- Signature: stmpe_gpio_irq(int irq,void * dev)
- Line: 388

### stmpe_gpio_irq_lock
- Return type: static void
- Signature: stmpe_gpio_irq_lock(struct irq_data * d)
- Line: 173
- Calls: gpiochip_get_data

### stmpe_gpio_irq_mask
- Return type: static void
- Signature: stmpe_gpio_irq_mask(struct irq_data * d)
- Line: 241
- Calls: gpiochip_disable_irq, gpiochip_get_data

### stmpe_gpio_irq_set_type
- Return type: static int
- Signature: stmpe_gpio_irq_set_type(struct irq_data * d,unsigned int type)
- Line: 144
- Calls: gpiochip_get_data

### stmpe_gpio_irq_sync_unlock
- Return type: static void
- Signature: stmpe_gpio_irq_sync_unlock(struct irq_data * d)
- Line: 181
- Calls: gpiochip_get_data

### stmpe_gpio_irq_unmask
- Return type: static void
- Signature: stmpe_gpio_irq_unmask(struct irq_data * d)
- Line: 253
- Calls: gpiochip_enable_irq, gpiochip_get_data

### stmpe_gpio_probe
- Return type: static int
- Signature: stmpe_gpio_probe(struct platform_device * pdev)
- Line: 474

### stmpe_gpio_request
- Return type: static int
- Signature: stmpe_gpio_request(struct gpio_chip * chip,unsigned offset)
- Line: 121
- Calls: gpiochip_get_data

### stmpe_gpio_set
- Return type: static int
- Signature: stmpe_gpio_set(struct gpio_chip * chip,unsigned int offset,int val)
- Line: 57
- Calls: gpiochip_get_data
- Called by: stmpe_gpio_direction_output

### stmpe_init_irq_valid_mask
- Return type: static void
- Signature: stmpe_init_irq_valid_mask(struct gpio_chip * gc,unsigned long * valid_mask,unsigned int ngpios)
- Line: 452
- Calls: gpiochip_get_data

## Structs (1)

### stmpe_gpio
- Line: 32
- Members:
  - chip: gpio_chip
  - stmpe: stmpe *
  - irq_lock: mutex
  - norequest_mask: u32
  - regs: u8[][]
  - oldregs: u8[][]

## Enums (2)

### __anond076adf10103
- Line: 24

### __anond076adf10203
- Line: 26

## Variables (4)

- static **stmpe_gpio_driver** : platform_driver (line 541)
- static **stmpe_gpio_irq_chip** : const struct irq_chip (line 375)
- static **stmpe_gpio_of_matches** : const struct of_device_id[] (line 535)
- static **template_chip** : const struct gpio_chip (line 132)

## Macros (4)

- **CACHE_NR_BANKS** (line 30)
- **CACHE_NR_REGS** (line 28)
- **MAX_GPIOS** (line 386)
- **NOT_SUPPORTED_IDX** (line 310)
