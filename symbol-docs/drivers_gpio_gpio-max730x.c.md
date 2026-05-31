# drivers/gpio/gpio-max730x.c

Subsystem: drivers/gpio

## Functions (7)

### __max7301_set
- Return type: static int
- Signature: __max7301_set(struct max7301 * ts,unsigned offset,int value)
- Line: 78
- Called by: max7301_direction_output, max7301_set

### __max730x_probe
- Return type: int
- Signature: __max730x_probe(struct max7301 * ts)
- Line: 163
- Calls: max7301_direction_input
- Called by: max7300_probe, max7301_probe

### __max730x_remove
- Return type: void
- Signature: __max730x_remove(struct device * dev)
- Line: 223
- Called by: max7300_remove, max7301_remove

### max7301_direction_input
- Return type: static int
- Signature: max7301_direction_input(struct gpio_chip * chip,unsigned offset)
- Line: 48
- Called by: __max730x_probe

### max7301_direction_output
- Return type: static int
- Signature: max7301_direction_output(struct gpio_chip * chip,unsigned offset,int value)
- Line: 89
- Calls: __max7301_set

### max7301_get
- Return type: static int
- Signature: max7301_get(struct gpio_chip * chip,unsigned offset)
- Line: 118
- Calls: gpiochip_get_data

### max7301_set
- Return type: static int
- Signature: max7301_set(struct gpio_chip * chip,unsigned int offset,int value)
- Line: 146
- Calls: __max7301_set, gpiochip_get_data

## Macros (5)

- **PIN_CONFIG_IN_PULLUP** (line 42)
- **PIN_CONFIG_IN_WO_PULLUP** (line 43)
- **PIN_CONFIG_MASK** (line 41)
- **PIN_CONFIG_OUT** (line 44)
- **PIN_NUMBER** (line 46)
