# drivers/gpio/gpio-104-dio-48e.c

Subsystem: drivers/gpio

## Functions (7)

### dio48e_handle_mask_sync
- Return type: static int
- Signature: dio48e_handle_mask_sync(const int index,const unsigned int mask_buf_def,const unsigned int mask_buf,void * const irq_drv_data)
- Line: 161

### dio48e_irq_init_hw
- Return type: static int
- Signature: dio48e_irq_init_hw(struct regmap * const map)
- Line: 213
- Called by: dio48e_probe

### dio48e_probe
- Return type: static int
- Signature: dio48e_probe(struct device * dev,unsigned int id)
- Line: 221
- Calls: devm_i8255_regmap_register, dio48e_irq_init_hw

### dio48e_regmap_lock
- Return type: static void
- Signature: dio48e_regmap_lock(void * lock_arg)
- Line: 125

### dio48e_regmap_unlock
- Return type: static void
- Signature: dio48e_regmap_unlock(void * lock_arg)
- Line: 134

### pit_regmap_lock
- Return type: static void
- Signature: pit_regmap_lock(void * lock_arg)
- Line: 141

### pit_regmap_unlock
- Return type: static void
- Signature: pit_regmap_unlock(void * lock_arg)
- Line: 152

## Structs (1)

### dio48e_gpio
- Line: 117
- Members:
  - lock: raw_spinlock_t
  - map: regmap *
  - regs: void __iomem *
  - flags: unsigned long
  - irq_mask: unsigned int

## Variables (19)

- static **base** : unsigned int[] (line 30)
- static **dio48e_driver** : isa_driver (line 331)
- static **dio48e_names** : const char * [] (line 194)
- static **dio48e_precious_ranges** : const struct regmap_range[] (line 62)
- static **dio48e_precious_table** : const struct regmap_access_table (line 78)
- static **dio48e_rd_ranges** : const struct regmap_range[] (line 52)
- static **dio48e_rd_table** : const struct regmap_access_table (line 70)
- static **dio48e_regmap_irqs** : const struct regmap_irq[] (line 105)
- static **dio48e_volatile_ranges** : const struct regmap_range[] (line 57)
- static **dio48e_volatile_table** : const struct regmap_access_table (line 74)
- static **dio48e_wr_ranges** : const struct regmap_range[] (line 48)
- static **dio48e_wr_table** : const struct regmap_access_table (line 66)
- static **irq** : unsigned int[] (line 35)
- static **num_dio48e** : unsigned int (line 31)
- static **num_irq** : unsigned int (line 36)
- static **pit_rd_ranges** : const struct regmap_range[] (line 86)
- static **pit_rd_table** : const struct regmap_access_table (line 93)
- static **pit_wr_ranges** : const struct regmap_range[] (line 83)
- static **pit_wr_table** : const struct regmap_access_table (line 89)

## Macros (10)

- **DIO48E_CLEAR_INTERRUPT** (line 44)
- **DIO48E_DISABLE_COUNTER_TIMER_ADDRESSING** (line 43)
- **DIO48E_DISABLE_INTERRUPT** (line 41)
- **DIO48E_ENABLE_COUNTER_TIMER_ADDRESSING** (line 42)
- **DIO48E_ENABLE_INTERRUPT** (line 40)
- **DIO48E_EXTENT** (line 27)
- **DIO48E_NGPIO** (line 193)
- **DIO48E_NUM_PPI** (line 46)
- **DIO48E_REGMAP_IRQ**(_ppi) (line 99)
- **MAX_NUM_DIO48E** (line 28)
