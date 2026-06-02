# drivers/i2c/busses/i2c-au1550.c

Subsystem: drivers/i2c

## Functions (17)

### RD
- Return type: static unsigned long
- Signature: RD(struct i2c_au1550_data * a,int r)
- Line: 50

### WR
- Return type: static void
- Signature: WR(struct i2c_au1550_data * a,int r,unsigned long v)
- Line: 44

### au1550_func
- Return type: static u32
- Signature: au1550_func(struct i2c_adapter * adap)
- Line: 242

### au1550_xfer
- Return type: static int
- Signature: au1550_xfer(struct i2c_adapter * i2c_adap,struct i2c_msg * msgs,int num)
- Line: 212

### do_address
- Return type: static int
- Signature: do_address(struct i2c_au1550_data * adap,unsigned int addr,int rd,int q)
- Line: 98

### i2c_au1550_disable
- Return type: static void
- Signature: i2c_au1550_disable(struct i2c_au1550_data * priv)
- Line: 289

### i2c_au1550_probe
- Return type: static int
- Signature: i2c_au1550_probe(struct platform_device * pdev)
- Line: 301

### i2c_au1550_remove
- Return type: static void
- Signature: i2c_au1550_remove(struct platform_device * pdev)
- Line: 336

### i2c_au1550_resume
- Return type: static int
- Signature: i2c_au1550_resume(struct device * dev)
- Line: 353

### i2c_au1550_setup
- Return type: static void
- Signature: i2c_au1550_setup(struct i2c_au1550_data * priv)
- Line: 252

### i2c_au1550_suspend
- Return type: static int
- Signature: i2c_au1550_suspend(struct device * dev)
- Line: 344

### i2c_read
- Return type: static int
- Signature: i2c_read(struct i2c_au1550_data * adap,unsigned char * buf,unsigned int len)
- Line: 154

### i2c_write
- Return type: static int
- Signature: i2c_write(struct i2c_au1550_data * adap,unsigned char * buf,unsigned int len)
- Line: 184

### wait_ack
- Return type: static int
- Signature: wait_ack(struct i2c_au1550_data * adap)
- Line: 70

### wait_controller_done
- Return type: static int
- Signature: wait_controller_done(struct i2c_au1550_data * adap)
- Line: 84

### wait_for_rx_byte
- Return type: static int
- Signature: wait_for_rx_byte(struct i2c_au1550_data * adap,unsigned char * out)
- Line: 130

### wait_xfer_done
- Return type: static int
- Signature: wait_xfer_done(struct i2c_au1550_data * adap)
- Line: 55

## Structs (1)

### i2c_au1550_data
- Line: 38
- Members:
  - psc_base: void __iomem *
  - xfer_timeout: int
  - adap: i2c_adapter

## Variables (2)

- static **au1550_algo** : const struct i2c_algorithm (line 247)
- static **au1xpsc_smbus_driver** : platform_driver (line 365)

## Macros (9)

- **PSC_CTRL** (line 29)
- **PSC_SEL** (line 28)
- **PSC_SMBCFG** (line 30)
- **PSC_SMBEVNT** (line 34)
- **PSC_SMBMSK** (line 31)
- **PSC_SMBPCR** (line 32)
- **PSC_SMBSTAT** (line 33)
- **PSC_SMBTMR** (line 36)
- **PSC_SMBTXRX** (line 35)
