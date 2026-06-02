# drivers/i2c/busses/i2c-sh7760.c

Subsystem: drivers/i2c

## Functions (11)

### IN32
- Return type: static unsigned long
- Signature: IN32(struct cami2c * cam,int reg)
- Line: 107

### OUT32
- Return type: static void
- Signature: OUT32(struct cami2c * cam,int reg,unsigned long val)
- Line: 102

### calc_CCR
- Return type: static int
- Signature: calc_CCR(unsigned long scl_hz)
- Line: 392

### sh7760_i2c_busy_check
- Return type: static int
- Signature: sh7760_i2c_busy_check(struct cami2c * id)
- Line: 298

### sh7760_i2c_func
- Return type: static u32
- Signature: sh7760_i2c_func(struct i2c_adapter * adap)
- Line: 376

### sh7760_i2c_irq
- Return type: static irqreturn_t
- Signature: sh7760_i2c_irq(int irq,void * ptr)
- Line: 112

### sh7760_i2c_master_xfer
- Return type: static int
- Signature: sh7760_i2c_master_xfer(struct i2c_adapter * adap,struct i2c_msg * msgs,int num)
- Line: 303

### sh7760_i2c_mrecv
- Return type: static void
- Signature: sh7760_i2c_mrecv(struct cami2c * id)
- Line: 240

### sh7760_i2c_msend
- Return type: static void
- Signature: sh7760_i2c_msend(struct cami2c * id)
- Line: 266

### sh7760_i2c_probe
- Return type: static int
- Signature: sh7760_i2c_probe(struct platform_device * pdev)
- Line: 432

### sh7760_i2c_remove
- Return type: static void
- Signature: sh7760_i2c_remove(struct platform_device * pdev)
- Line: 538

## Structs (1)

### cami2c
- Line: 81
- Members:
  - iobase: void __iomem *
  - adap: i2c_adapter
  - msg: i2c_msg *
  - flags: int
  - status: int
  - xfer_done: completion
  - irq: int
  - ioarea: resource *

## Variables (2)

- static **sh7760_i2c_algo** : const struct i2c_algorithm (line 381)
- static **sh7760_i2c_drv** : platform_driver (line 550)

## Macros (53)

- **FCR_RFRST** (line 68)
- **FCR_TFRST** (line 69)
- **FIER_RXIE** (line 76)
- **FIER_TEIE** (line 75)
- **FIER_TXIE** (line 77)
- **FIFO_SIZE** (line 79)
- **FSR_RDF** (line 72)
- **FSR_TDFE** (line 73)
- **FSR_TEND** (line 71)
- **I2CCCR** (line 31)
- **I2CFCR** (line 35)
- **I2CFIER** (line 37)
- **I2CFSR** (line 36)
- **I2CMAR** (line 33)
- **I2CMCR** (line 26)
- **I2CMIER** (line 30)
- **I2CMSR** (line 28)
- **I2CRFDR** (line 38)
- **I2CRXTX** (line 34)
- **I2CSAR** (line 32)
- **I2CSCR** (line 25)
- **I2CSIER** (line 29)
- **I2CSSR** (line 27)
- **I2CTFDR** (line 39)
- **IDF_RECV** (line 88)
- **IDF_SEND** (line 87)
- **IDF_STOP** (line 89)
- **IDS_ARBLOST** (line 93)
- **IDS_DONE** (line 92)
- **IDS_NACK** (line 94)
- **MCR_ESG** (line 50)
- **MCR_FSB** (line 49)
- **MCR_FSCL** (line 44)
- **MCR_FSDA** (line 45)
- **MCR_MDBS** (line 43)
- **MCR_MIE** (line 47)
- **MCR_OBPC** (line 46)
- **MCR_TSBE** (line 48)
- **MIE_MALE** (line 61)
- **MIE_MATE** (line 66)
- **MIE_MDEE** (line 63)
- **MIE_MDRE** (line 65)
- **MIE_MDTE** (line 64)
- **MIE_MNRE** (line 60)
- **MIE_MSTE** (line 62)
- **MSR_MAL** (line 53)
- **MSR_MAT** (line 58)
- **MSR_MDE** (line 55)
- **MSR_MDR** (line 57)
- **MSR_MDT** (line 56)
- **MSR_MNR** (line 52)
- **MSR_MST** (line 54)
- **REGSIZE** (line 41)
