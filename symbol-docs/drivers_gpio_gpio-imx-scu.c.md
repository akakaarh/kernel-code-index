# drivers/gpio/gpio-imx-scu.c

Subsystem: drivers/gpio

## Functions (5)

### _imx_scu_gpio_init
- Return type: static int __init
- Signature: _imx_scu_gpio_init(void)
- Line: 126

### imx_scu_gpio_get
- Return type: static int
- Signature: imx_scu_gpio_get(struct gpio_chip * chip,unsigned int offset)
- Line: 36
- Calls: gpiochip_get_data

### imx_scu_gpio_get_direction
- Return type: static int
- Signature: imx_scu_gpio_get_direction(struct gpio_chip * chip,unsigned int offset)
- Line: 73

### imx_scu_gpio_probe
- Return type: static int
- Signature: imx_scu_gpio_probe(struct platform_device * pdev)
- Line: 78

### imx_scu_gpio_set
- Return type: static int
- Signature: imx_scu_gpio_set(struct gpio_chip * chip,unsigned int offset,int value)
- Line: 55
- Calls: gpiochip_get_data

## Structs (1)

### scu_gpio_priv
- Line: 18
- Members:
  - chip: gpio_chip
  - lock: mutex
  - dev: device *
  - handle: imx_sc_ipc *

## Variables (3)

- static **imx_scu_gpio_driver** : platform_driver (line 118)
- static **imx_scu_gpio_dt_ids** : const struct of_device_id[] (line 113)
- static **scu_rsrc_arr** : unsigned int[] (line 25)
