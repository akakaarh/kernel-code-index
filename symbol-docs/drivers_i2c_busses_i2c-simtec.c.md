# drivers/i2c/busses/i2c-simtec.c

Subsystem: drivers/i2c

## Functions (6)

### simtec_i2c_getscl
- Return type: static int
- Signature: simtec_i2c_getscl(void * pw)
- Line: 52

### simtec_i2c_getsda
- Return type: static int
- Signature: simtec_i2c_getsda(void * pw)
- Line: 46

### simtec_i2c_probe
- Return type: static int
- Signature: simtec_i2c_probe(struct platform_device * dev)
- Line: 60

### simtec_i2c_remove
- Return type: static void
- Signature: simtec_i2c_remove(struct platform_device * dev)
- Line: 129

### simtec_i2c_setscl
- Return type: static void
- Signature: simtec_i2c_setscl(void * pw,int state)
- Line: 40

### simtec_i2c_setsda
- Return type: static void
- Signature: simtec_i2c_setsda(void * pw,int state)
- Line: 34

## Structs (1)

### simtec_i2c_data
- Line: 19
- Members:
  - ioarea: resource *
  - reg: void __iomem *
  - adap: i2c_adapter
  - bit: i2c_algo_bit_data

## Variables (1)

- static **simtec_i2c_driver** : platform_driver (line 142)

## Macros (4)

- **CMD_SET_SCL** (line 27)
- **CMD_SET_SDA** (line 26)
- **STATE_SCL** (line 30)
- **STATE_SDA** (line 29)
