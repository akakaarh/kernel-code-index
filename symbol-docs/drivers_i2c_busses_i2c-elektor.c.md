# drivers/i2c/busses/i2c-elektor.c

Subsystem: drivers/i2c

## Functions (10)

### elektor_match
- Return type: static int
- Signature: elektor_match(struct device * dev,unsigned int id)
- Line: 196

### elektor_probe
- Return type: static int
- Signature: elektor_probe(struct device * dev,unsigned int id)
- Line: 255

### elektor_remove
- Return type: static void
- Signature: elektor_remove(struct device * dev,unsigned int id)
- Line: 284

### pcf_isa_getbyte
- Return type: static int
- Signature: pcf_isa_getbyte(void * data,int ctl)
- Line: 75

### pcf_isa_getclock
- Return type: static int
- Signature: pcf_isa_getclock(void * data)
- Line: 90

### pcf_isa_getown
- Return type: static int
- Signature: pcf_isa_getown(void * data)
- Line: 84

### pcf_isa_handler
- Return type: static irqreturn_t
- Signature: pcf_isa_handler(int this_irq,void * dev_id)
- Line: 124

### pcf_isa_init
- Return type: static int
- Signature: pcf_isa_init(void)
- Line: 133

### pcf_isa_setbyte
- Return type: static void
- Signature: pcf_isa_setbyte(void * data,int ctl,int val)
- Line: 58

### pcf_isa_waitforpin
- Return type: static void
- Signature: pcf_isa_waitforpin(void * data)
- Line: 95

## Variables (12)

- static **base** : int (line 37)
- static **base_iomem** : u8 __iomem * (line 38)
- static **clock** : int (line 41)
- static **i2c_elektor_driver** : isa_driver (line 302)
- static **irq** : int (line 40)
- static **mmapped** : int (line 43)
- static **own** : int (line 42)
- static **pcf_isa_data** : i2c_algo_pcf_data (line 181)
- static **pcf_isa_ops** : i2c_adapter (line 189)
- static **pcf_isa_ops** : i2c_adapter (line 54)
- static **pcf_pending** : int (line 51)
- static **pcf_wait** : wait_queue_head_t (line 50)

## Macros (1)

- **DEFAULT_BASE** (line 35)
