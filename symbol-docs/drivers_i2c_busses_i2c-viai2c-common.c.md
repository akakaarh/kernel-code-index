# drivers/i2c/busses/i2c-viai2c-common.c

Subsystem: drivers/i2c

## Functions (6)

### viai2c_init
- Return type: int
- Signature: viai2c_init(struct platform_device * pdev,struct viai2c ** pi2c,int plat)
- Line: 178

### viai2c_irq_xfer
- Return type: int
- Signature: viai2c_irq_xfer(struct viai2c * i2c)
- Line: 135

### viai2c_read
- Return type: static int
- Signature: viai2c_read(struct viai2c * i2c,struct i2c_msg * pmsg,bool first)
- Line: 64

### viai2c_wait_bus_not_busy
- Return type: int
- Signature: viai2c_wait_bus_not_busy(struct viai2c * i2c)
- Line: 5

### viai2c_write
- Return type: static int
- Signature: viai2c_write(struct viai2c * i2c,struct i2c_msg * pmsg,int last)
- Line: 22

### viai2c_xfer
- Return type: int
- Signature: viai2c_xfer(struct i2c_adapter * adap,struct i2c_msg msgs[],int num)
- Line: 98
