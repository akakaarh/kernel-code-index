# drivers/i2c/busses/i2c-ibm_iic.c

Subsystem: drivers/i2c

## Functions (20)

### dump_iic_regs
- Return type: static void
- Signature: dump_iic_regs(const char * header,struct ibm_iic_private * dev)
- Line: 81

### iic_abort_xfer
- Return type: static void
- Signature: iic_abort_xfer(struct ibm_iic_private * dev)
- Line: 376

### iic_address
- Return type: static void
- Signature: iic_address(struct ibm_iic_private * dev,struct i2c_msg * msg)
- Line: 512

### iic_address_neq
- Return type: static int
- Signature: iic_address_neq(const struct i2c_msg * p1,const struct i2c_msg * p2)
- Line: 534

### iic_clckdiv
- Return type: static u8
- Signature: iic_clckdiv(unsigned int opb)
- Line: 627

### iic_dc_wait
- Return type: static int
- Signature: iic_dc_wait(volatile struct iic_regs __iomem * iic,u8 mask)
- Line: 228

### iic_dev_init
- Return type: static void
- Signature: iic_dev_init(struct ibm_iic_private * dev)
- Line: 133

### iic_dev_reset
- Return type: static void
- Signature: iic_dev_reset(struct ibm_iic_private * dev)
- Line: 178

### iic_func
- Return type: static u32
- Signature: iic_func(struct i2c_adapter * adap)
- Line: 614

### iic_handler
- Return type: static irqreturn_t
- Signature: iic_handler(int irq,void * dev_id)
- Line: 324

### iic_interrupt_mode
- Return type: static void
- Signature: iic_interrupt_mode(struct ibm_iic_private * dev,int enable)
- Line: 125

### iic_invalid_address
- Return type: static int
- Signature: iic_invalid_address(const struct i2c_msg * p)
- Line: 529

### iic_probe
- Return type: static int
- Signature: iic_probe(struct platform_device * ofdev)
- Line: 682

### iic_remove
- Return type: static void
- Signature: iic_remove(struct platform_device * ofdev)
- Line: 764

### iic_request_irq
- Return type: static int
- Signature: iic_request_irq(struct platform_device * ofdev,struct ibm_iic_private * dev)
- Line: 651

### iic_smbus_quick
- Return type: static int
- Signature: iic_smbus_quick(struct ibm_iic_private * dev,const struct i2c_msg * p)
- Line: 239

### iic_wait_for_tc
- Return type: static int
- Signature: iic_wait_for_tc(struct ibm_iic_private * dev)
- Line: 408

### iic_xfer
- Return type: static int
- Signature: iic_xfer(struct i2c_adapter * adap,struct i2c_msg * msgs,int num)
- Line: 545

### iic_xfer_bytes
- Return type: static int
- Signature: iic_xfer_bytes(struct ibm_iic_private * dev,struct i2c_msg * pm,int combined_xfer)
- Line: 455

### iic_xfer_result
- Return type: static int
- Signature: iic_xfer_result(struct ibm_iic_private * dev)
- Line: 343

## Structs (1)

### ibm_iic_timings
- Line: 100
- Members:
  - hd_sta: unsigned int
  - su_sto: unsigned int
  - low: unsigned int
  - high: unsigned int
  - buf: unsigned int

## Variables (6)

- static **ibm_iic_driver** : platform_driver (line 785)
- static **ibm_iic_match** : const struct of_device_id[] (line 779)
- static **iic_algo** : const struct i2c_algorithm (line 619)
- static **iic_force_fast** : bool (line 56)
- static **iic_force_poll** : bool (line 52)
- **timings** : ibm_iic_timings[] (line 106)

## Macros (8)

- **DBG**(f,x...) (line 71)
- **DBG**(f,x...) (line 73)
- **DBG2**(f,x...) (line 76)
- **DBG2**(f,x...) (line 78)
- **DBG_LEVEL** (line 60)
- **DRIVER_VERSION** (line 47)
- **DUMP_REGS**(h,dev) (line 94)
- **DUMP_REGS**(h,dev) (line 96)
