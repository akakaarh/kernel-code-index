# drivers/gpio/gpio-xtensa.c

Subsystem: drivers/gpio

## Functions (11)

### disable_cp
- Return type: static void
- Signature: disable_cp(unsigned long flags,unsigned long cpenable)
- Line: 52
- Called by: xtensa_expstate_get_value, xtensa_expstate_set_value, xtensa_impwire_get_value

### disable_cp
- Return type: static void
- Signature: disable_cp(unsigned long flags,unsigned long cpenable)
- Line: 66
- Called by: xtensa_expstate_get_value, xtensa_expstate_set_value, xtensa_impwire_get_value

### enable_cp
- Return type: static unsigned long
- Signature: enable_cp(unsigned long * cpenable)
- Line: 42
- Called by: xtensa_expstate_get_value, xtensa_expstate_set_value, xtensa_impwire_get_value

### enable_cp
- Return type: static unsigned long
- Signature: enable_cp(unsigned long * cpenable)
- Line: 60
- Called by: xtensa_expstate_get_value, xtensa_expstate_set_value, xtensa_impwire_get_value

### xtensa_expstate_get_direction
- Return type: static int
- Signature: xtensa_expstate_get_direction(struct gpio_chip * gc,unsigned offset)
- Line: 89

### xtensa_expstate_get_value
- Return type: static int
- Signature: xtensa_expstate_get_value(struct gpio_chip * gc,unsigned offset)
- Line: 94
- Calls: disable_cp, enable_cp

### xtensa_expstate_set_value
- Return type: static int
- Signature: xtensa_expstate_set_value(struct gpio_chip * gc,unsigned int offset,int value)
- Line: 106
- Calls: disable_cp, enable_cp

### xtensa_gpio_init
- Return type: static int __init
- Signature: xtensa_gpio_init(void)
- Line: 155

### xtensa_gpio_probe
- Return type: static int
- Signature: xtensa_gpio_probe(struct platform_device * pdev)
- Line: 138

### xtensa_impwire_get_direction
- Return type: static int
- Signature: xtensa_impwire_get_direction(struct gpio_chip * gc,unsigned offset)
- Line: 72

### xtensa_impwire_get_value
- Return type: static int
- Signature: xtensa_impwire_get_value(struct gpio_chip * gc,unsigned offset)
- Line: 77
- Calls: disable_cp, enable_cp

## Variables (3)

- static **expstate_chip** : gpio_chip (line 129)
- static **impwire_chip** : gpio_chip (line 121)
- static **xtensa_gpio_driver** : platform_driver (line 148)
