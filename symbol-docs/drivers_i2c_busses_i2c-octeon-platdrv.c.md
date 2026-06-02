# drivers/i2c/busses/i2c-octeon-platdrv.c

Subsystem: drivers/i2c

## Functions (12)

### __octeon_i2c_irq_disable
- Return type: static void
- Signature: __octeon_i2c_irq_disable(atomic_t * cnt,int irq)
- Line: 63

### octeon_i2c_functionality
- Return type: static u32
- Signature: octeon_i2c_functionality(struct i2c_adapter * adap)
- Line: 118

### octeon_i2c_hlc_int_disable78
- Return type: static void
- Signature: octeon_i2c_hlc_int_disable78(struct octeon_i2c * i2c)
- Line: 97

### octeon_i2c_hlc_int_enable
- Return type: static void
- Signature: octeon_i2c_hlc_int_enable(struct octeon_i2c * i2c)
- Line: 113

### octeon_i2c_hlc_int_enable78
- Return type: static void
- Signature: octeon_i2c_hlc_int_enable78(struct octeon_i2c * i2c)
- Line: 90

### octeon_i2c_hlc_isr78
- Return type: static irqreturn_t
- Signature: octeon_i2c_hlc_isr78(int irq,void * dev_id)
- Line: 103

### octeon_i2c_int_disable
- Return type: static void
- Signature: octeon_i2c_int_disable(struct octeon_i2c * i2c)
- Line: 44

### octeon_i2c_int_disable78
- Return type: static void
- Signature: octeon_i2c_int_disable78(struct octeon_i2c * i2c)
- Line: 78

### octeon_i2c_int_enable
- Return type: static void
- Signature: octeon_i2c_int_enable(struct octeon_i2c * i2c)
- Line: 38

### octeon_i2c_int_enable78
- Return type: static void
- Signature: octeon_i2c_int_enable78(struct octeon_i2c * i2c)
- Line: 57

### octeon_i2c_probe
- Return type: static int
- Signature: octeon_i2c_probe(struct platform_device * pdev)
- Line: 135

### octeon_i2c_remove
- Return type: static void
- Signature: octeon_i2c_remove(struct platform_device * pdev)
- Line: 256

## Variables (4)

- static **octeon_i2c_algo** : const struct i2c_algorithm (line 124)
- static **octeon_i2c_driver** : platform_driver (line 270)
- static **octeon_i2c_match** : const struct of_device_id[] (line 263)
- static **octeon_i2c_ops** : const struct i2c_adapter (line 129)

## Macros (1)

- **DRV_NAME** (line 29)
