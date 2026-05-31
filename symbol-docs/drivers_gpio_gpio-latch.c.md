# drivers/gpio/gpio-latch.c

Subsystem: drivers/gpio

## Functions (6)

### gpio_latch_can_sleep
- Return type: static bool
- Signature: gpio_latch_can_sleep(struct gpio_latch_priv * priv,unsigned int n_latches)
- Line: 116
- Calls: gpiod_cansleep
- Called by: gpio_latch_probe

### gpio_latch_get_direction
- Return type: static int
- Signature: gpio_latch_get_direction(struct gpio_chip * gc,unsigned int offset)
- Line: 69

### gpio_latch_probe
- Return type: static int
- Signature: gpio_latch_probe(struct platform_device * pdev)
- Line: 139
- Calls: devm_gpiod_get_array, gpio_latch_can_sleep

### gpio_latch_set
- Return type: static int
- Signature: gpio_latch_set(struct gpio_chip * gc,unsigned int offset,int val)
- Line: 98
- Calls: gpio_latch_set_unlocked, gpiochip_get_data

### gpio_latch_set_can_sleep
- Return type: static int
- Signature: gpio_latch_set_can_sleep(struct gpio_chip * gc,unsigned int offset,int val)
- Line: 107
- Calls: gpio_latch_set_unlocked, gpiochip_get_data

### gpio_latch_set_unlocked
- Return type: static int
- Signature: gpio_latch_set_unlocked(struct gpio_latch_priv * priv,int (* set)(struct gpio_desc * desc,int value),unsigned int offset,bool val)
- Line: 74
- Called by: gpio_latch_set, gpio_latch_set_can_sleep

## Structs (1)

### gpio_latch_priv
- Line: 51
- Members:
  - gc: gpio_chip
  - clk_gpios: gpio_descs *
  - latched_gpios: gpio_descs *
  - n_latched_gpios: int
  - setup_duration_ns: unsigned int
  - clock_duration_ns: unsigned int
  - shadow: unsigned long *
  - mutex: mutex
  - spinlock: spinlock_t

## Unions (1)

### __anon89c49814010a
- Line: 63
- Members:
  - gc: gpio_chip
  - clk_gpios: gpio_descs *
  - latched_gpios: gpio_descs *
  - n_latched_gpios: int
  - setup_duration_ns: unsigned int
  - clock_duration_ns: unsigned int
  - shadow: unsigned long *
  - mutex: mutex
  - spinlock: spinlock_t

## Variables (2)

- static **gpio_latch_driver** : platform_driver (line 210)
- static **gpio_latch_ids** : const struct of_device_id[] (line 202)

## Macros (1)

- **DURATION_NS_MAX** (line 137)
