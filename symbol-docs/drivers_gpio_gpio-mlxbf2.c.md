# drivers/gpio/gpio-mlxbf2.c

Subsystem: drivers/gpio

## Functions (13)

### mlxbf2_gpio_direction_input
- Return type: static int
- Signature: mlxbf2_gpio_direction_input(struct gpio_chip * chip,unsigned int offset)
- Line: 185
- Calls: gpiochip_get_data, mlxbf2_gpio_lock_acquire, mlxbf2_gpio_lock_release

### mlxbf2_gpio_direction_output
- Return type: static int
- Signature: mlxbf2_gpio_direction_output(struct gpio_chip * chip,unsigned int offset,int value)
- Line: 211
- Calls: gpiochip_get_data, mlxbf2_gpio_lock_acquire, mlxbf2_gpio_lock_release

### mlxbf2_gpio_get_lock_res
- Return type: static int
- Signature: mlxbf2_gpio_get_lock_res(struct platform_device * pdev)
- Line: 97
- Called by: mlxbf2_gpio_probe

### mlxbf2_gpio_irq_disable
- Return type: static void
- Signature: mlxbf2_gpio_irq_disable(struct irq_data * irqd)
- Line: 253
- Calls: gpiochip_disable_irq, gpiochip_get_data

### mlxbf2_gpio_irq_enable
- Return type: static void
- Signature: mlxbf2_gpio_irq_enable(struct irq_data * irqd)
- Line: 235
- Calls: gpiochip_enable_irq, gpiochip_get_data

### mlxbf2_gpio_irq_handler
- Return type: static irqreturn_t
- Signature: mlxbf2_gpio_irq_handler(int irq,void * ptr)
- Line: 269

### mlxbf2_gpio_irq_print_chip
- Return type: static void
- Signature: mlxbf2_gpio_irq_print_chip(struct irq_data * irqd,struct seq_file * p)
- Line: 327
- Calls: gpiochip_get_data

### mlxbf2_gpio_irq_set_type
- Return type: static int
- Signature: mlxbf2_gpio_irq_set_type(struct irq_data * irqd,unsigned int type)
- Line: 286
- Calls: gpiochip_get_data

### mlxbf2_gpio_lock_acquire
- Return type: static int
- Signature: mlxbf2_gpio_lock_acquire(struct mlxbf2_gpio_context * gs)
- Line: 132
- Called by: mlxbf2_gpio_direction_input, mlxbf2_gpio_direction_output

### mlxbf2_gpio_lock_release
- Return type: static void
- Signature: mlxbf2_gpio_lock_release(struct mlxbf2_gpio_context * gs)
- Line: 158
- Called by: mlxbf2_gpio_direction_input, mlxbf2_gpio_direction_output

### mlxbf2_gpio_probe
- Return type: static int
- Signature: mlxbf2_gpio_probe(struct platform_device * pdev)
- Line: 347
- Calls: gpio_generic_chip_init, mlxbf2_gpio_get_lock_res

### mlxbf2_gpio_resume
- Return type: static int
- Signature: mlxbf2_gpio_resume(struct device * dev)
- Line: 439

### mlxbf2_gpio_suspend
- Return type: static int
- Signature: mlxbf2_gpio_suspend(struct device * dev)
- Line: 427

## Structs (3)

### mlxbf2_gpio_context
- Line: 69
- Members:
  - gpio_mode0: u32
  - gpio_mode1: u32
  - chip: gpio_generic_chip
  - gpio_io: void __iomem *
  - dev: device *
  - csave_regs: mlxbf2_gpio_context_save_regs *
  - io: void __iomem *
  - res: resource *
  - lock: mutex *

### mlxbf2_gpio_context_save_regs
- Line: 63
- Members:
  - gpio_mode0: u32
  - gpio_mode1: u32
  - chip: gpio_generic_chip
  - gpio_io: void __iomem *
  - dev: device *
  - csave_regs: mlxbf2_gpio_context_save_regs *
  - io: void __iomem *
  - res: resource *
  - lock: mutex *

### mlxbf2_gpio_param
- Line: 80
- Members:
  - gpio_mode0: u32
  - gpio_mode1: u32
  - chip: gpio_generic_chip
  - gpio_io: void __iomem *
  - dev: device *
  - csave_regs: mlxbf2_gpio_context_save_regs *
  - io: void __iomem *
  - res: resource *
  - lock: mutex *

## Variables (5)

- static **mlxbf2_gpio_acpi_match** : const struct acpi_device_id __maybe_unused[] (line 452)
- static **mlxbf2_gpio_driver** : platform_driver (line 458)
- static **mlxbf2_gpio_irq_chip** : const struct irq_chip (line 336)
- static **yu_arm_gpio_lock_param** : mlxbf2_gpio_param (line 91)
- static **yu_arm_gpio_lock_res** : resource (line 86)

## Macros (19)

- **MLXBF2_GPIO_MAX_PINS_PER_BLOCK** (line 32)
- **YU_ARM_GPIO_LOCK_ACQUIRE** (line 43)
- **YU_ARM_GPIO_LOCK_ADDR** (line 40)
- **YU_ARM_GPIO_LOCK_RELEASE** (line 44)
- **YU_ARM_GPIO_LOCK_SIZE** (line 41)
- **YU_GPIO_CAUSE_FALL_EN** (line 55)
- **YU_GPIO_CAUSE_OR_CAUSE_EVTEN0** (line 59)
- **YU_GPIO_CAUSE_OR_CLRCAUSE** (line 61)
- **YU_GPIO_CAUSE_OR_EVTEN0** (line 60)
- **YU_GPIO_CAUSE_RISE_EN** (line 54)
- **YU_GPIO_DATACLEAR** (line 53)
- **YU_GPIO_DATAIN** (line 49)
- **YU_GPIO_DATASET** (line 52)
- **YU_GPIO_MODE0** (line 51)
- **YU_GPIO_MODE0_CLEAR** (line 58)
- **YU_GPIO_MODE0_SET** (line 57)
- **YU_GPIO_MODE1** (line 50)
- **YU_GPIO_MODE1_CLEAR** (line 56)
- **YU_LOCK_ACTIVE_BIT**(val) (line 42)
