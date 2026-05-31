# drivers/gpio/gpio-ws16c48.c

Subsystem: drivers/gpio

## Functions (6)

### ws16c48_handle_mask_sync
- Return type: static int
- Signature: ws16c48_handle_mask_sync(const int index,const unsigned int mask_buf_def,const unsigned int mask_buf,void * const irq_drv_data)
- Line: 133

### ws16c48_handle_post_irq
- Return type: static int
- Signature: ws16c48_handle_post_irq(void * const irq_drv_data)
- Line: 124

### ws16c48_handle_pre_irq
- Return type: static int
- Signature: ws16c48_handle_pre_irq(void * const irq_drv_data)
- Line: 114

### ws16c48_irq_init_hw
- Return type: static int
- Signature: ws16c48_irq_init_hw(struct regmap * const map)
- Line: 223
- Called by: ws16c48_probe

### ws16c48_probe
- Return type: static int
- Signature: ws16c48_probe(struct device * dev,unsigned int id)
- Line: 245
- Calls: devm_gpio_regmap_register, ws16c48_irq_init_hw

### ws16c48_set_type_config
- Return type: static int
- Signature: ws16c48_set_type_config(unsigned int ** const buf,const unsigned int type,const struct regmap_irq * const irq_data,const int idx,void * const irq_drv_data)
- Line: 166

## Structs (1)

### ws16c48_gpio
- Line: 108
- Members:
  - map: regmap *
  - lock: raw_spinlock_t
  - irq_mask: u8[]

## Variables (14)

- static **base** : unsigned int[] (line 23)
- static **irq** : unsigned int[] (line 28)
- static **num_irq** : unsigned int (line 29)
- static **num_ws16c48** : unsigned int (line 24)
- static **ws16c48_driver** : isa_driver (line 316)
- static **ws16c48_names** : const char * [] (line 208)
- static **ws16c48_rd_ranges** : const struct regmap_range[] (line 48)
- static **ws16c48_rd_table** : const struct regmap_access_table (line 58)
- static **ws16c48_regmap_config** : const struct regmap_config (line 66)
- static **ws16c48_regmap_irqs** : const struct regmap_irq[] (line 91)
- static **ws16c48_volatile_ranges** : const struct regmap_range[] (line 51)
- static **ws16c48_volatile_table** : const struct regmap_access_table (line 62)
- static **ws16c48_wr_ranges** : const struct regmap_range[] (line 45)
- static **ws16c48_wr_table** : const struct regmap_access_table (line 54)

## Macros (16)

- **ENAB_PAGE** (line 42)
- **INT_ID_PAGE** (line 43)
- **MAX_NUM_WS16C48** (line 21)
- **PAGE_LOCK_PAGE_FIELD** (line 40)
- **POL_PAGE** (line 41)
- **WS16C48_DAT_BASE** (line 33)
- **WS16C48_ENAB** (line 37)
- **WS16C48_EXTENT** (line 20)
- **WS16C48_INT_ID** (line 38)
- **WS16C48_NGPIO** (line 207)
- **WS16C48_NGPIO_PER_REG** (line 78)
- **WS16C48_NUM_IRQS** (line 90)
- **WS16C48_PAGE_BASE** (line 35)
- **WS16C48_PAGE_LOCK** (line 34)
- **WS16C48_POL** (line 36)
- **WS16C48_REGMAP_IRQ**(_id) (line 79)
