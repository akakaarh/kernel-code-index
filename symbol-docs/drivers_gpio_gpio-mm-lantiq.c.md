# drivers/gpio/gpio-mm-lantiq.c

Subsystem: drivers/gpio

## Functions (7)

### ltq_mm_apply
- Return type: static void
- Signature: ltq_mm_apply(struct ltq_mm * chip)
- Line: 41
- Called by: ltq_mm_save_regs, ltq_mm_set

### ltq_mm_dir_out
- Return type: static int
- Signature: ltq_mm_dir_out(struct gpio_chip * gc,unsigned offset,int value)
- Line: 81
- Calls: ltq_mm_set

### ltq_mm_exit
- Return type: static void __exit
- Signature: ltq_mm_exit(void)
- Line: 156

### ltq_mm_init
- Return type: static int __init
- Signature: ltq_mm_init(void)
- Line: 149

### ltq_mm_probe
- Return type: static int
- Signature: ltq_mm_probe(struct platform_device * pdev)
- Line: 98
- Calls: ltq_mm_save_regs

### ltq_mm_save_regs
- Return type: static void
- Signature: ltq_mm_save_regs(struct ltq_mm * chip)
- Line: 90
- Calls: ltq_mm_apply
- Called by: ltq_mm_probe

### ltq_mm_set
- Return type: static int
- Signature: ltq_mm_set(struct gpio_chip * gc,unsigned int offset,int value)
- Line: 60
- Calls: gpiochip_get_data, ltq_mm_apply
- Called by: ltq_mm_dir_out

## Structs (1)

### ltq_mm
- Line: 28
- Members:
  - gc: gpio_chip
  - regs: void __iomem *
  - shadow: u16

## Variables (2)

- static **ltq_mm_driver** : platform_driver (line 141)
- static **ltq_mm_match** : const struct of_device_id[] (line 135)

## Macros (2)

- **LTQ_EBU_BUSCON** (line 25)
- **LTQ_EBU_WP** (line 26)
