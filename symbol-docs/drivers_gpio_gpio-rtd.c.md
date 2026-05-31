# drivers/gpio/gpio-rtd.c

Subsystem: drivers/gpio

## Functions (24)

### rtd1295_iso_gpio_get_deb_setval
- Return type: static u8
- Signature: rtd1295_iso_gpio_get_deb_setval(const struct rtd_gpio_info * info,unsigned int offset,u8 deb_index,u8 * reg_offset,u8 * shift)
- Line: 88

### rtd1295_misc_gpio_get_deb_setval
- Return type: static u8
- Signature: rtd1295_misc_gpio_get_deb_setval(const struct rtd_gpio_info * info,unsigned int offset,u8 deb_index,u8 * reg_offset,u8 * shift)
- Line: 80

### rtd_gpio_check_ie
- Return type: static bool
- Signature: rtd_gpio_check_ie(struct rtd_gpio * data,int irq)
- Line: 364
- Calls: rtd_gpio_ie_offset
- Called by: rtd_gpio_irq_handle

### rtd_gpio_dati_offset
- Return type: static int
- Signature: rtd_gpio_dati_offset(struct rtd_gpio * data,unsigned int offset)
- Line: 188
- Called by: rtd_gpio_get

### rtd_gpio_dato_offset
- Return type: static int
- Signature: rtd_gpio_dato_offset(struct rtd_gpio * data,unsigned int offset)
- Line: 183
- Called by: rtd_gpio_get, rtd_gpio_set

### rtd_gpio_dir_offset
- Return type: static int
- Signature: rtd_gpio_dir_offset(struct rtd_gpio * data,unsigned int offset)
- Line: 178
- Called by: rtd_gpio_get, rtd_gpio_get_direction, rtd_gpio_set_direction

### rtd_gpio_direction_input
- Return type: static int
- Signature: rtd_gpio_direction_input(struct gpio_chip * chip,unsigned int offset)
- Line: 352
- Calls: rtd_gpio_set_direction

### rtd_gpio_direction_output
- Return type: static int
- Signature: rtd_gpio_direction_output(struct gpio_chip * chip,unsigned int offset,int value)
- Line: 357
- Calls: rtd_gpio_set, rtd_gpio_set_direction

### rtd_gpio_disable_irq
- Return type: static void
- Signature: rtd_gpio_disable_irq(struct irq_data * d)
- Line: 454
- Calls: gpiochip_disable_irq, gpiochip_get_data, rtd_gpio_ie_offset

### rtd_gpio_dp_offset
- Return type: static int
- Signature: rtd_gpio_dp_offset(struct rtd_gpio * data,unsigned int offset)
- Line: 198
- Called by: rtd_gpio_irq_set_type

### rtd_gpio_enable_irq
- Return type: static void
- Signature: rtd_gpio_enable_irq(struct irq_data * d)
- Line: 423
- Calls: gpiochip_enable_irq, gpiochip_get_data, rtd_gpio_gpa_offset, rtd_gpio_gpda_offset, rtd_gpio_ie_offset

### rtd_gpio_get
- Return type: static int
- Signature: rtd_gpio_get(struct gpio_chip * chip,unsigned int offset)
- Line: 299
- Calls: gpiochip_get_data, rtd_gpio_dati_offset, rtd_gpio_dato_offset, rtd_gpio_dir_offset

### rtd_gpio_get_deb_setval
- Return type: static u8
- Signature: rtd_gpio_get_deb_setval(const struct rtd_gpio_info * info,unsigned int offset,u8 deb_index,u8 * reg_offset,u8 * shift)
- Line: 72

### rtd_gpio_get_direction
- Return type: static int
- Signature: rtd_gpio_get_direction(struct gpio_chip * chip,unsigned int offset)
- Line: 317
- Calls: gpiochip_get_data, rtd_gpio_dir_offset

### rtd_gpio_gpa_offset
- Return type: static int
- Signature: rtd_gpio_gpa_offset(struct rtd_gpio * data,unsigned int offset)
- Line: 204
- Called by: rtd_gpio_enable_irq

### rtd_gpio_gpda_offset
- Return type: static int
- Signature: rtd_gpio_gpda_offset(struct rtd_gpio * data,unsigned int offset)
- Line: 210
- Called by: rtd_gpio_enable_irq

### rtd_gpio_ie_offset
- Return type: static int
- Signature: rtd_gpio_ie_offset(struct rtd_gpio * data,unsigned int offset)
- Line: 193
- Called by: rtd_gpio_check_ie, rtd_gpio_disable_irq, rtd_gpio_enable_irq

### rtd_gpio_irq_handle
- Return type: static void
- Signature: rtd_gpio_irq_handle(struct irq_desc * desc)
- Line: 376
- Calls: rtd_gpio_check_ie

### rtd_gpio_irq_set_type
- Return type: static int
- Signature: rtd_gpio_irq_set_type(struct irq_data * d,unsigned int type)
- Line: 474
- Calls: gpiochip_get_data, rtd_gpio_dp_offset

### rtd_gpio_probe
- Return type: static int
- Signature: rtd_gpio_probe(struct platform_device * pdev)
- Line: 525

### rtd_gpio_set
- Return type: static int
- Signature: rtd_gpio_set(struct gpio_chip * chip,unsigned int offset,int value)
- Line: 278
- Calls: gpiochip_get_data, rtd_gpio_dato_offset
- Called by: rtd_gpio_direction_output

### rtd_gpio_set_config
- Return type: static int
- Signature: rtd_gpio_set_config(struct gpio_chip * chip,unsigned int offset,unsigned long config)
- Line: 260
- Calls: gpiochip_generic_config, rtd_gpio_set_debounce

### rtd_gpio_set_debounce
- Return type: static int
- Signature: rtd_gpio_set_debounce(struct gpio_chip * chip,unsigned int offset,unsigned int debounce)
- Line: 216
- Calls: gpiochip_get_data
- Called by: rtd_gpio_set_config

### rtd_gpio_set_direction
- Return type: static int
- Signature: rtd_gpio_set_direction(struct gpio_chip * chip,unsigned int offset,bool out)
- Line: 331
- Calls: gpiochip_get_data, rtd_gpio_dir_offset
- Called by: rtd_gpio_direction_input, rtd_gpio_direction_output

## Structs (2)

### rtd_gpio
- Line: 63
- Members:
  - name: const char *
  - gpio_base: unsigned int
  - num_gpios: unsigned int
  - dir_offset: u8 *
  - dato_offset: u8 *
  - dati_offset: u8 *
  - ie_offset: u8 *
  - dp_offset: u8 *
  - gpa_offset: u8 *
  - gpda_offset: u8 *
  - deb_offset: u8 *
  - deb_val: u8 *
  - get_deb_setval: u8 (*)(const struct rtd_gpio_info * info,unsigned int offset,u8 deb_index,u8 * reg_offset,u8 * shift)
  - gpio_chip: gpio_chip
  - info: const struct rtd_gpio_info *
  - base: void __iomem *
  - irq_base: void __iomem *
  - irqs: unsigned int[2]
  - lock: raw_spinlock_t

### rtd_gpio_info
- Line: 45
- Members:
  - name: const char *
  - gpio_base: unsigned int
  - num_gpios: unsigned int
  - dir_offset: u8 *
  - dato_offset: u8 *
  - dati_offset: u8 *
  - ie_offset: u8 *
  - dp_offset: u8 *
  - gpa_offset: u8 *
  - gpda_offset: u8 *
  - deb_offset: u8 *
  - deb_val: u8 *
  - get_deb_setval: u8 (*)(const struct rtd_gpio_info * info,unsigned int offset,u8 deb_index,u8 * reg_offset,u8 * shift)
  - gpio_chip: gpio_chip
  - info: const struct rtd_gpio_info *
  - base: void __iomem *
  - irq_base: void __iomem *
  - irqs: unsigned int[2]
  - lock: raw_spinlock_t

## Variables (8)

- static **rtd1295_iso_gpio_info** : const struct rtd_gpio_info (line 162)
- static **rtd1295_misc_gpio_info** : const struct rtd_gpio_info (line 146)
- static **rtd1395_iso_gpio_info** : const struct rtd_gpio_info (line 130)
- static **rtd1619_iso_gpio_info** : const struct rtd_gpio_info (line 113)
- static **rtd_gpio_irq_chip** : const struct irq_chip (line 517)
- static **rtd_gpio_of_matches** : const struct of_device_id[] (line 586)
- static **rtd_gpio_platform_driver** : platform_driver (line 599)
- static **rtd_iso_gpio_info** : const struct rtd_gpio_info (line 96)

## Macros (7)

- **RTD_GPIO_DEBOUNCE_100US** (line 23)
- **RTD_GPIO_DEBOUNCE_10MS** (line 25)
- **RTD_GPIO_DEBOUNCE_10US** (line 22)
- **RTD_GPIO_DEBOUNCE_1MS** (line 24)
- **RTD_GPIO_DEBOUNCE_1US** (line 21)
- **RTD_GPIO_DEBOUNCE_20MS** (line 26)
- **RTD_GPIO_DEBOUNCE_30MS** (line 27)
