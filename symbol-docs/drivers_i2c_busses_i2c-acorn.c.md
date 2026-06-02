# drivers/i2c/busses/i2c-acorn.c

Subsystem: drivers/i2c

## Functions (5)

### i2c_ioc_init
- Return type: static int __init
- Signature: i2c_ioc_init(void)
- Line: 85

### ioc_getscl
- Return type: static int
- Signature: ioc_getscl(void * data)
- Line: 60

### ioc_getsda
- Return type: static int
- Signature: ioc_getsda(void * data)
- Line: 65

### ioc_setscl
- Return type: static void
- Signature: ioc_setscl(void * data,int state)
- Line: 30

### ioc_setsda
- Return type: static void
- Signature: ioc_setsda(void * data,int state)
- Line: 45

## Variables (3)

- static **force_ones** : u_int (line 28)
- static **ioc_data** : i2c_algo_bit_data (line 70)
- static **ioc_ops** : i2c_adapter (line 79)

## Macros (3)

- **FORCE_ONES** (line 18)
- **SCL** (line 19)
- **SDA** (line 20)
