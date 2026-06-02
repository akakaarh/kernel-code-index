# drivers/i2c/busses/i2c-pasemi-core.c

Subsystem: drivers/i2c

## Functions (11)

### pasemi_i2c_common_probe
- Return type: int
- Signature: pasemi_i2c_common_probe(struct pasemi_smbus * smbus)
- Line: 423

### pasemi_i2c_xfer
- Return type: static int
- Signature: pasemi_i2c_xfer(struct i2c_adapter * adapter,struct i2c_msg * msgs,int num)
- Line: 241

### pasemi_i2c_xfer_msg
- Return type: static int
- Signature: pasemi_i2c_xfer_msg(struct i2c_adapter * adapter,struct i2c_msg * msg,int stop)
- Line: 193

### pasemi_irq_handler
- Return type: irqreturn_t
- Signature: pasemi_irq_handler(int irq,void * dev_id)
- Line: 453

### pasemi_reset
- Return type: static void
- Signature: pasemi_reset(struct pasemi_smbus * smbus)
- Line: 80

### pasemi_smb_clear
- Return type: static int
- Signature: pasemi_smb_clear(struct pasemi_smbus * smbus)
- Line: 91

### pasemi_smb_func
- Return type: static u32
- Signature: pasemi_smb_func(struct i2c_adapter * adapter)
- Line: 409

### pasemi_smb_waitready
- Return type: static int
- Signature: pasemi_smb_waitready(struct pasemi_smbus * smbus)
- Line: 122

### pasemi_smb_xfer
- Return type: static int
- Signature: pasemi_smb_xfer(struct i2c_adapter * adapter,u16 addr,unsigned short flags,char read_write,u8 command,int size,union i2c_smbus_data * data)
- Line: 257

### reg_read
- Return type: static int
- Signature: reg_read(struct pasemi_smbus * smbus,int reg)
- Line: 69

### reg_write
- Return type: static void
- Signature: reg_write(struct pasemi_smbus * smbus,int reg,int val)
- Line: 63

## Variables (1)

- static **smbus_algorithm** : const struct i2c_algorithm (line 417)

## Macros (31)

- **CTL_CLK_M** (line 55)
- **CTL_EN** (line 51)
- **CTL_MRR** (line 52)
- **CTL_MTR** (line 53)
- **CTL_UJM** (line 54)
- **MRXFIFO_DATA_M** (line 38)
- **MRXFIFO_EMPTY** (line 37)
- **MTXFIFO_DATA_M** (line 35)
- **MTXFIFO_READ** (line 32)
- **MTXFIFO_START** (line 34)
- **MTXFIFO_STOP** (line 33)
- **PASEMI_TRANSFER_TIMEOUT_MS** (line 61)
- **REG_CTL** (line 28)
- **REG_IMASK** (line 27)
- **REG_MRXFIFO** (line 24)
- **REG_MTXFIFO** (line 23)
- **REG_REV** (line 29)
- **REG_SMSTA** (line 26)
- **REG_XFSTA** (line 25)
- **RXFIFO_RD**(smbus) (line 78)
- **SMSTA_JAM** (line 43)
- **SMSTA_JMD** (line 42)
- **SMSTA_MRNE** (line 47)
- **SMSTA_MTA** (line 45)
- **SMSTA_MTE** (line 48)
- **SMSTA_MTN** (line 46)
- **SMSTA_MTO** (line 44)
- **SMSTA_TOM** (line 49)
- **SMSTA_XEN** (line 41)
- **SMSTA_XIP** (line 40)
- **TXFIFO_WR**(smbus,reg) (line 77)
