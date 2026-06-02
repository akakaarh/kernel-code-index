# drivers/i2c/busses/i2c-icy.c

Subsystem: drivers/i2c

## Functions (7)

### icy_pcf_getclock
- Return type: static int
- Signature: icy_pcf_getclock(void * data)
- Line: 86

### icy_pcf_getown
- Return type: static int
- Signature: icy_pcf_getown(void * data)
- Line: 81

### icy_pcf_getpcf
- Return type: static int
- Signature: icy_pcf_getpcf(void * data,int ctl)
- Line: 72

### icy_pcf_setpcf
- Return type: static void
- Signature: icy_pcf_setpcf(void * data,int ctl,int val)
- Line: 63

### icy_pcf_waitforpin
- Return type: static void
- Signature: icy_pcf_waitforpin(void * data)
- Line: 91

### icy_probe
- Return type: static int
- Signature: icy_probe(struct zorro_dev * z,const struct zorro_device_id * ent)
- Line: 121

### icy_remove
- Return type: static void
- Signature: icy_remove(struct zorro_dev * z)
- Line: 187

## Structs (1)

### icy_i2c
- Line: 52
- Members:
  - adapter: i2c_adapter
  - reg_s0: void __iomem *
  - reg_s1: void __iomem *
  - ltc2990_client: i2c_client *

## Variables (6)

- static **icy_driver** : zorro_driver (line 202)
- static **icy_ltc2990_addresses** : unsigned short const[] (line 99)
- static **icy_ltc2990_meas_mode** : const u32[] (line 110)
- static **icy_ltc2990_node** : const struct software_node (line 117)
- static **icy_ltc2990_props** : const struct property_entry[] (line 112)
- static **icy_zorro_tbl** : const struct zorro_device_id[] (line 195)
