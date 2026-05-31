# drivers/gpio/gpio-max77759.c

Subsystem: drivers/gpio

## Functions (20)

### max77759_gpio_bus_lock
- Return type: static void
- Signature: max77759_gpio_bus_lock(struct irq_data * d)
- Line: 273
- Calls: gpiochip_get_data

### max77759_gpio_bus_sync_unlock
- Return type: static void
- Signature: max77759_gpio_bus_sync_unlock(struct irq_data * d)
- Line: 334
- Calls: gpiochip_get_data, max77759_gpio_bus_sync_unlock_helper

### max77759_gpio_bus_sync_unlock_helper
- Return type: static int
- Signature: max77759_gpio_bus_sync_unlock_helper(struct gpio_chip * gc,struct max77759_gpio_chip * chip)
- Line: 281
- Calls: max77759_gpio_maxq_gpio_control_read, max77759_gpio_maxq_gpio_control_write, max77759_gpio_maxq_gpio_trigger_read, max77759_gpio_maxq_gpio_trigger_write
- Called by: max77759_gpio_bus_sync_unlock

### max77759_gpio_direction_from_control
- Return type: static int
- Signature: max77759_gpio_direction_from_control(int ctrl,unsigned int offset)
- Line: 112
- Called by: max77759_gpio_get_direction, max77759_gpio_get_value

### max77759_gpio_direction_helper
- Return type: static int
- Signature: max77759_gpio_direction_helper(struct gpio_chip * gc,unsigned int offset,enum max77759_control_gpio_dir dir,int value)
- Line: 135
- Calls: gpiochip_get_data, max77759_gpio_maxq_gpio_control_read, max77759_gpio_maxq_gpio_control_write
- Called by: max77759_gpio_direction_input, max77759_gpio_direction_output

### max77759_gpio_direction_input
- Return type: static int
- Signature: max77759_gpio_direction_input(struct gpio_chip * gc,unsigned int offset)
- Line: 163
- Calls: max77759_gpio_direction_helper

### max77759_gpio_direction_output
- Return type: static int
- Signature: max77759_gpio_direction_output(struct gpio_chip * gc,unsigned int offset,int value)
- Line: 170
- Calls: max77759_gpio_direction_helper

### max77759_gpio_get_direction
- Return type: static int
- Signature: max77759_gpio_get_direction(struct gpio_chip * gc,unsigned int offset)
- Line: 122
- Calls: gpiochip_get_data, max77759_gpio_direction_from_control, max77759_gpio_maxq_gpio_control_read

### max77759_gpio_get_value
- Return type: static int
- Signature: max77759_gpio_get_value(struct gpio_chip * gc,unsigned int offset)
- Line: 177
- Calls: gpiochip_get_data, max77759_gpio_direction_from_control, max77759_gpio_maxq_gpio_control_read

### max77759_gpio_irq_mask
- Return type: static void
- Signature: max77759_gpio_irq_mask(struct irq_data * d)
- Line: 220
- Calls: gpiochip_disable_irq, gpiochip_get_data

### max77759_gpio_irq_print_chip
- Return type: static void
- Signature: max77759_gpio_irq_print_chip(struct irq_data * d,struct seq_file * p)
- Line: 361

### max77759_gpio_irq_unmask
- Return type: static void
- Signature: max77759_gpio_irq_unmask(struct irq_data * d)
- Line: 233
- Calls: gpiochip_enable_irq, gpiochip_get_data

### max77759_gpio_irqhandler
- Return type: static irqreturn_t
- Signature: max77759_gpio_irqhandler(int irq,void * data)
- Line: 379

### max77759_gpio_maxq_gpio_control_read
- Return type: static int
- Signature: max77759_gpio_maxq_gpio_control_read(struct max77759_gpio_chip * chip)
- Line: 85
- Called by: max77759_gpio_bus_sync_unlock_helper, max77759_gpio_direction_helper, max77759_gpio_get_direction, max77759_gpio_get_value, max77759_gpio_set_value

### max77759_gpio_maxq_gpio_control_write
- Return type: static int
- Signature: max77759_gpio_maxq_gpio_control_write(struct max77759_gpio_chip * chip,u8 ctrl)
- Line: 100
- Called by: max77759_gpio_bus_sync_unlock_helper, max77759_gpio_direction_helper, max77759_gpio_set_value

### max77759_gpio_maxq_gpio_trigger_read
- Return type: static int
- Signature: max77759_gpio_maxq_gpio_trigger_read(struct max77759_gpio_chip * chip)
- Line: 59
- Called by: max77759_gpio_bus_sync_unlock_helper

### max77759_gpio_maxq_gpio_trigger_write
- Return type: static int
- Signature: max77759_gpio_maxq_gpio_trigger_write(struct max77759_gpio_chip * chip,u8 trigger)
- Line: 74
- Called by: max77759_gpio_bus_sync_unlock_helper

### max77759_gpio_probe
- Return type: static int
- Signature: max77759_gpio_probe(struct platform_device * pdev)
- Line: 432

### max77759_gpio_set_irq_type
- Return type: static int
- Signature: max77759_gpio_set_irq_type(struct irq_data * d,unsigned int type)
- Line: 246
- Calls: gpiochip_get_data

### max77759_gpio_set_value
- Return type: static int
- Signature: max77759_gpio_set_value(struct gpio_chip * gc,unsigned int offset,int value)
- Line: 199
- Calls: gpiochip_get_data, max77759_gpio_maxq_gpio_control_read, max77759_gpio_maxq_gpio_control_write

## Structs (1)

### max77759_gpio_chip
- Line: 27
- Members:
  - map: regmap *
  - max77759: max77759 *
  - gc: gpio_chip
  - maxq_lock: mutex
  - irq_lock: mutex
  - irq_mask: int
  - irq_mask_changed: int
  - irq_trig: int
  - irq_trig_changed: int

## Enums (2)

### max77759_control_gpio_dir
- Line: 49

### max77759_trigger_gpio_type
- Line: 42

## Variables (5)

- static **max77759_gpio_driver** : platform_driver (line 510)
- static **max77759_gpio_irq_chip** : const struct irq_chip (line 368)
- static **max77759_gpio_line_names** : const char * const[] (line 25)
- static **max77759_gpio_of_id** : const struct of_device_id[] (line 498)
- static **max77759_gpio_platform_id** : const struct platform_device_id[] (line 504)

## Macros (8)

- **MAX77759_GPIOx_DIR**(offs,dir) (line 47)
- **MAX77759_GPIOx_DIR_MASK**(offs) (line 48)
- **MAX77759_GPIOx_INVAL_MASK**(offs) (line 57)
- **MAX77759_GPIOx_OUTVAL**(offs,val) (line 54)
- **MAX77759_GPIOx_OUTVAL_MASK**(offs) (line 55)
- **MAX77759_GPIOx_TRIGGER**(offs,val) (line 40)
- **MAX77759_GPIOx_TRIGGER_MASK**(offs) (line 41)
- **MAX77759_N_GPIOS** (line 24)
