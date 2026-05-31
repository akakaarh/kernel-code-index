# drivers/gpio/gpio-lp3943.c

Subsystem: drivers/gpio

## Functions (10)

### lp3943_get_gpio_in_status
- Return type: static int
- Signature: lp3943_get_gpio_in_status(struct lp3943_gpio * lp3943_gpio,struct gpio_chip * chip,unsigned int offset)
- Line: 84
- Called by: lp3943_gpio_get

### lp3943_get_gpio_out_status
- Return type: static int
- Signature: lp3943_get_gpio_out_status(struct lp3943_gpio * lp3943_gpio,struct gpio_chip * chip,unsigned int offset)
- Line: 109
- Called by: lp3943_gpio_get

### lp3943_gpio_direction_input
- Return type: static int
- Signature: lp3943_gpio_direction_input(struct gpio_chip * chip,unsigned int offset)
- Line: 75
- Calls: gpiochip_get_data, lp3943_gpio_set_mode

### lp3943_gpio_direction_output
- Return type: static int
- Signature: lp3943_gpio_direction_output(struct gpio_chip * chip,unsigned int offset,int value)
- Line: 164
- Calls: gpiochip_get_data, lp3943_gpio_set

### lp3943_gpio_free
- Return type: static void
- Signature: lp3943_gpio_free(struct gpio_chip * chip,unsigned int offset)
- Line: 57
- Calls: gpiochip_get_data

### lp3943_gpio_get
- Return type: static int
- Signature: lp3943_gpio_get(struct gpio_chip * chip,unsigned int offset)
- Line: 131
- Calls: gpiochip_get_data, lp3943_get_gpio_in_status, lp3943_get_gpio_out_status

### lp3943_gpio_probe
- Return type: static int
- Signature: lp3943_gpio_probe(struct platform_device * pdev)
- Line: 193

### lp3943_gpio_request
- Return type: static int
- Signature: lp3943_gpio_request(struct gpio_chip * chip,unsigned int offset)
- Line: 45
- Calls: gpiochip_get_data

### lp3943_gpio_set
- Return type: static int
- Signature: lp3943_gpio_set(struct gpio_chip * chip,unsigned int offset,int value)
- Line: 150
- Calls: gpiochip_get_data, lp3943_gpio_set_mode
- Called by: lp3943_gpio_direction_output

### lp3943_gpio_set_mode
- Return type: static int
- Signature: lp3943_gpio_set_mode(struct lp3943_gpio * lp3943_gpio,u8 offset,u8 val)
- Line: 65
- Called by: lp3943_gpio_direction_input, lp3943_gpio_set

## Structs (1)

### lp3943_gpio
- Line: 39
- Members:
  - chip: gpio_chip
  - lp3943: lp3943 *
  - input_mask: u16

## Enums (1)

### lp3943_gpios
- Line: 19

## Variables (3)

- static **lp3943_gpio_chip** : const struct gpio_chip (line 179)
- static **lp3943_gpio_driver** : platform_driver (line 217)
- static **lp3943_gpio_of_match** : const struct of_device_id[] (line 211)
