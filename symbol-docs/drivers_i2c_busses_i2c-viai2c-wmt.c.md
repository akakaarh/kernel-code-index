# drivers/i2c/busses/i2c-viai2c-wmt.c

Subsystem: drivers/i2c

## Functions (5)

### wmt_i2c_func
- Return type: static u32
- Signature: wmt_i2c_func(struct i2c_adapter * adap)
- Line: 32

### wmt_i2c_isr
- Return type: static irqreturn_t
- Signature: wmt_i2c_isr(int irq,void * data)
- Line: 72

### wmt_i2c_probe
- Return type: static int
- Signature: wmt_i2c_probe(struct platform_device * pdev)
- Line: 98

### wmt_i2c_remove
- Return type: static void
- Signature: wmt_i2c_remove(struct platform_device * pdev)
- Line: 149

### wmt_i2c_reset_hardware
- Return type: static int
- Signature: wmt_i2c_reset_hardware(struct viai2c * i2c)
- Line: 42

## Variables (3)

- static **wmt_i2c_algo** : const struct i2c_algorithm (line 37)
- static **wmt_i2c_driver** : platform_driver (line 164)
- static **wmt_i2c_dt_ids** : const struct of_device_id[] (line 159)

## Macros (11)

- **MCR_APB_166M** (line 30)
- **MCR_APB_96M** (line 29)
- **REG_SLAVE_CR** (line 16)
- **REG_SLAVE_DR** (line 20)
- **REG_SLAVE_IMR** (line 19)
- **REG_SLAVE_ISR** (line 18)
- **REG_SLAVE_SR** (line 17)
- **REG_SLAVE_TR** (line 21)
- **SCL_TIMEOUT**(x) (line 24)
- **TR_HS** (line 26)
- **TR_STD** (line 25)
