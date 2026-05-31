# drivers/gpio/gpio-usbio.c

Subsystem: drivers/gpio

## Functions (9)

### usbio_gpio_direction_input
- Return type: static int
- Signature: usbio_gpio_direction_input(struct gpio_chip * gc,unsigned int offset)
- Line: 136
- Calls: usbio_gpio_update_config

### usbio_gpio_direction_output
- Return type: static int
- Signature: usbio_gpio_direction_output(struct gpio_chip * gc,unsigned int offset,int value)
- Line: 142
- Calls: usbio_gpio_set, usbio_gpio_update_config

### usbio_gpio_get
- Return type: static int
- Signature: usbio_gpio_get(struct gpio_chip * gc,unsigned int offset)
- Line: 71
- Calls: gpiochip_get_data, usbio_gpio_get_bank_and_pin

### usbio_gpio_get_bank_and_pin
- Return type: static void
- Signature: usbio_gpio_get_bank_and_pin(struct gpio_chip * gc,unsigned int offset,struct usbio_gpio_bank ** bank_ret,unsigned int * pin_ret)
- Line: 37
- Calls: gpiochip_get_data
- Called by: usbio_gpio_get, usbio_gpio_get_direction, usbio_gpio_set, usbio_gpio_update_config

### usbio_gpio_get_direction
- Return type: static int
- Signature: usbio_gpio_get_direction(struct gpio_chip * gc,unsigned int offset)
- Line: 57
- Calls: usbio_gpio_get_bank_and_pin

### usbio_gpio_probe
- Return type: static int
- Signature: usbio_gpio_probe(struct auxiliary_device * adev,const struct auxiliary_device_id * adev_id)
- Line: 180

### usbio_gpio_set
- Return type: static int
- Signature: usbio_gpio_set(struct gpio_chip * gc,unsigned int offset,int value)
- Line: 94
- Calls: gpiochip_get_data, usbio_gpio_get_bank_and_pin
- Called by: usbio_gpio_direction_output

### usbio_gpio_set_config
- Return type: static int
- Signature: usbio_gpio_set_config(struct gpio_chip * gc,unsigned int offset,unsigned long config)
- Line: 155
- Calls: usbio_gpio_update_config

### usbio_gpio_update_config
- Return type: static int
- Signature: usbio_gpio_update_config(struct gpio_chip * gc,unsigned int offset,u8 mask,u8 value)
- Line: 112
- Calls: gpiochip_get_data, usbio_gpio_get_bank_and_pin
- Called by: usbio_gpio_direction_input, usbio_gpio_direction_output, usbio_gpio_set_config

## Structs (2)

### usbio_gpio
- Line: 21
- Members:
  - config: u8[]
  - bitmap: u32
  - config_mutex: mutex
  - banks: usbio_gpio_bank[]
  - gc: gpio_chip
  - adev: auxiliary_device *

### usbio_gpio_bank
- Line: 16
- Members:
  - config: u8[]
  - bitmap: u32
  - config_mutex: mutex
  - banks: usbio_gpio_bank[]
  - gc: gpio_chip
  - adev: auxiliary_device *

## Variables (3)

- static **usbio_gpio_acpi_hids** : const struct acpi_device_id[] (line 28)
- static **usbio_gpio_driver** : auxiliary_driver (line 237)
- static **usbio_gpio_id_table** : const struct auxiliary_device_id[] (line 231)
