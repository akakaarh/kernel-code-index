# drivers/gpio/gpiolib-of.c

Subsystem: drivers/gpio

## Functions (28)

### of_convert_gpio_flags
- Return type: static unsigned long
- Signature: of_convert_gpio_flags(enum of_gpio_flags flags)
- Line: 450
- Called by: of_find_gpio, of_gpiochip_get_lflags

### of_find_gpio
- Return type: gpio_desc *
- Signature: of_find_gpio(struct device_node * np,const char * con_id,unsigned int idx,unsigned long * flags)
- Line: 689
- Calls: of_convert_gpio_flags, of_get_named_gpiod_flags
- Called by: gpiod_find_by_fwnode

### of_find_gpio_device_by_node
- Return type: static gpio_device *
- Signature: of_find_gpio_device_by_node(struct device_node * np)
- Line: 760
- Calls: gpio_device_find
- Called by: of_gpio_notify

### of_find_gpio_device_by_xlate
- Return type: static gpio_device *
- Signature: of_find_gpio_device_by_xlate(const struct of_phandle_args * gpiospec)
- Line: 132
- Calls: gpio_device_find
- Called by: of_get_named_gpiod_flags

### of_find_gpio_rename
- Return type: static gpio_desc *
- Signature: of_find_gpio_rename(struct device_node * np,const char * con_id,unsigned int idx,enum of_gpio_flags * of_flags)
- Line: 479
- Calls: of_get_named_gpiod_flags

### of_find_mt2701_gpio
- Return type: static gpio_desc *
- Signature: of_find_mt2701_gpio(struct device_node * np,const char * con_id,unsigned int idx,enum of_gpio_flags * of_flags)
- Line: 616
- Calls: of_get_named_gpiod_flags

### of_find_trigger_gpio
- Return type: static gpio_desc *
- Signature: of_find_trigger_gpio(struct device_node * np,const char * con_id,unsigned int idx,enum of_gpio_flags * of_flags)
- Line: 655
- Calls: of_get_named_gpiod_flags

### of_get_named_gpiod_flags
- Return type: static gpio_desc *
- Signature: of_get_named_gpiod_flags(const struct device_node * np,const char * propname,int index,enum of_gpio_flags * flags)
- Line: 409
- Calls: gpio_device_get_chip, of_find_gpio_device_by_xlate, of_gpio_flags_quirks, of_xlate_and_get_gpiod_flags
- Called by: of_find_gpio, of_find_gpio_rename, of_find_mt2701_gpio, of_find_trigger_gpio

### of_gpio_count
- Return type: int
- Signature: of_gpio_count(const struct fwnode_handle * fwnode,const char * con_id)
- Line: 103
- Calls: of_gpio_named_count, of_gpio_spi_cs_get_count
- Called by: gpiod_count

### of_gpio_flags_quirks
- Return type: static void
- Signature: of_gpio_flags_quirks(const struct device_node * np,const char * propname,enum of_gpio_flags * flags,int index)
- Line: 335
- Calls: of_gpio_quirk_polarity, of_gpio_set_polarity_by_property, of_gpio_try_fixup_polarity
- Called by: of_get_named_gpiod_flags

### of_gpio_named_count
- Return type: static int
- Signature: of_gpio_named_count(const struct device_node * np,const char * propname)
- Line: 66
- Called by: of_gpio_count, of_gpio_spi_cs_get_count

### of_gpio_notify
- Return type: static int
- Signature: of_gpio_notify(struct notifier_block * nb,unsigned long action,void * arg)
- Line: 765
- Calls: gpio_device_get_chip, gpiochip_add_hog, of_find_gpio_device_by_node, of_gpiochip_remove_hog

### of_gpio_quirk_polarity
- Return type: static void
- Signature: of_gpio_quirk_polarity(const struct device_node * np,bool active_high,enum of_gpio_flags * flags)
- Line: 157
- Called by: of_gpio_flags_quirks, of_gpio_set_polarity_by_property, of_gpio_try_fixup_polarity

### of_gpio_set_polarity_by_property
- Return type: static void
- Signature: of_gpio_set_polarity_by_property(const struct device_node * np,const char * propname,enum of_gpio_flags * flags)
- Line: 256
- Calls: of_gpio_quirk_polarity
- Called by: of_gpio_flags_quirks

### of_gpio_spi_cs_get_count
- Return type: static int
- Signature: of_gpio_spi_cs_get_count(const struct device_node * np,const char * con_id)
- Line: 89
- Calls: of_gpio_named_count
- Called by: of_gpio_count

### of_gpio_threecell_xlate
- Return type: static int
- Signature: of_gpio_threecell_xlate(struct gpio_chip * gc,const struct of_phandle_args * gpiospec,u32 * flags)
- Line: 875

### of_gpio_try_fixup_polarity
- Return type: static void
- Signature: of_gpio_try_fixup_polarity(const struct device_node * np,const char * propname,enum of_gpio_flags * flags)
- Line: 179
- Calls: of_gpio_quirk_polarity
- Called by: of_gpio_flags_quirks

### of_gpio_twocell_xlate
- Return type: static int
- Signature: of_gpio_twocell_xlate(struct gpio_chip * gc,const struct of_phandle_args * gpiospec,u32 * flags)
- Line: 833

### of_gpiochip_add
- Return type: int
- Signature: of_gpiochip_add(struct gpio_chip * chip)
- Line: 1040
- Calls: of_gpiochip_add_pin_range
- Called by: gpiochip_add_data_with_key

### of_gpiochip_add_pin_range
- Return type: static int
- Signature: of_gpiochip_add_pin_range(struct gpio_chip * chip)
- Line: 1037
- Calls: gpiochip_add_pingroup_range
- Called by: of_gpiochip_add

### of_gpiochip_add_pin_range
- Return type: static int
- Signature: of_gpiochip_add_pin_range(struct gpio_chip * chip)
- Line: 904
- Calls: gpiochip_add_pingroup_range
- Called by: of_gpiochip_add

### of_gpiochip_get_lflags
- Return type: int
- Signature: of_gpiochip_get_lflags(struct gpio_chip * chip,struct fwnode_reference_args * gpiospec,unsigned long * lflags)
- Line: 716
- Calls: of_convert_gpio_flags, of_xlate_and_get_gpiod_flags
- Called by: gpiochip_add_hog

### of_gpiochip_instance_match
- Return type: bool
- Signature: of_gpiochip_instance_match(struct gpio_chip * gc,unsigned int index)
- Line: 1089
- Called by: gpiochip_irq_select

### of_gpiochip_match_node
- Return type: static int
- Signature: of_gpiochip_match_node(struct gpio_chip * chip,const void * data)
- Line: 755

### of_gpiochip_match_node_and_xlate
- Return type: static int
- Signature: of_gpiochip_match_node_and_xlate(struct gpio_chip * chip,const void * data)
- Line: 121

### of_gpiochip_remove
- Return type: void
- Signature: of_gpiochip_remove(struct gpio_chip * chip)
- Line: 1077
- Called by: gpiochip_add_data_with_key, gpiochip_remove

### of_gpiochip_remove_hog
- Return type: static void
- Signature: of_gpiochip_remove_hog(struct gpio_chip * chip,struct device_node * hog)
- Line: 745
- Calls: gpiochip_free_own_desc
- Called by: of_gpio_notify

### of_xlate_and_get_gpiod_flags
- Return type: static gpio_desc *
- Signature: of_xlate_and_get_gpiod_flags(struct gpio_chip * chip,struct of_phandle_args * gpiospec,enum of_gpio_flags * flags)
- Line: 137
- Calls: gpiochip_get_desc
- Called by: of_get_named_gpiod_flags, of_gpiochip_get_lflags

## Structs (3)

### __anonc4602e140108
- Line: 183
- Members:
  - compatible: const char *
  - propname: const char *
  - active_high: bool
  - compatible: const char *
  - gpio_propname: const char *
  - polarity_propname: const char *
  - con_id: const char *
  - legacy_id: const char *
  - compatible: const char *

### __anonc4602e140208
- Line: 262
- Members:
  - compatible: const char *
  - propname: const char *
  - active_high: bool
  - compatible: const char *
  - gpio_propname: const char *
  - polarity_propname: const char *
  - con_id: const char *
  - legacy_id: const char *
  - compatible: const char *

### of_rename_gpio
- Line: 484
- Members:
  - compatible: const char *
  - propname: const char *
  - active_high: bool
  - compatible: const char *
  - gpio_propname: const char *
  - polarity_propname: const char *
  - con_id: const char *
  - legacy_id: const char *
  - compatible: const char *

## Enums (1)

### of_gpio_flags
- Line: 33

## Typedefs (1)

- **of_find_gpio_quirk** → gpio_desc * (*)(struct device_node * np,const char * con_id,unsigned int idx,enum of_gpio_flags * of_flags) (line 676)

## Variables (2)

- **gpio_of_notifier** : notifier_block (line 815)
- static **of_find_gpio_quirks** : const of_find_gpio_quirk[] (line 680)
