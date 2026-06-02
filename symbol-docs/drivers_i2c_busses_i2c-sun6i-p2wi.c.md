# drivers/i2c/busses/i2c-sun6i-p2wi.c

Subsystem: drivers/i2c

## Functions (5)

### p2wi_functionality
- Return type: static u32
- Signature: p2wi_functionality(struct i2c_adapter * adap)
- Line: 112

### p2wi_interrupt
- Return type: static irqreturn_t
- Signature: p2wi_interrupt(int irq,void * dev_id)
- Line: 94

### p2wi_probe
- Return type: static int
- Signature: p2wi_probe(struct platform_device * pdev)
- Line: 183

### p2wi_remove
- Return type: static void
- Signature: p2wi_remove(struct platform_device * dev)
- Line: 312

### p2wi_smbus_xfer
- Return type: static int
- Signature: p2wi_smbus_xfer(struct i2c_adapter * adap,u16 addr,unsigned short flags,char read_write,u8 command,int size,union i2c_smbus_data * data)
- Line: 117

## Structs (1)

### p2wi
- Line: 84
- Members:
  - adapter: i2c_adapter
  - complete: completion
  - status: unsigned int
  - regs: void __iomem *
  - clk: clk *
  - rstc: reset_control *
  - target_addr: int

## Variables (3)

- static **p2wi_algo** : const struct i2c_algorithm (line 172)
- static **p2wi_driver** : platform_driver (line 320)
- static **p2wi_of_match_table** : const struct of_device_id[] (line 177)

## Macros (35)

- **P2WI_CCR** (line 36)
- **P2WI_CCR_CLK_DIV**(v) (line 56)
- **P2WI_CCR_MAX_CLK_DIV** (line 55)
- **P2WI_CCR_SDA_OUT_DELAY**(v) (line 54)
- **P2WI_CTRL** (line 35)
- **P2WI_CTRL_ABORT_TRANS** (line 49)
- **P2WI_CTRL_GLOBAL_INT_ENB** (line 50)
- **P2WI_CTRL_SOFT_RST** (line 51)
- **P2WI_CTRL_START_TRANS** (line 48)
- **P2WI_DADDR0** (line 39)
- **P2WI_DADDR1** (line 40)
- **P2WI_DATA0** (line 42)
- **P2WI_DATA1** (line 43)
- **P2WI_DLEN** (line 41)
- **P2WI_DLEN_DATA_LENGTH**(v) (line 66)
- **P2WI_DLEN_READ** (line 65)
- **P2WI_INTE** (line 37)
- **P2WI_INTS** (line 38)
- **P2WI_INTS_LOAD_BSY** (line 60)
- **P2WI_INTS_TRANS_ERR** (line 61)
- **P2WI_INTS_TRANS_ERR_ID**(v) (line 59)
- **P2WI_INTS_TRANS_OVER** (line 62)
- **P2WI_LCR** (line 44)
- **P2WI_LCR_SCL_CTL** (line 71)
- **P2WI_LCR_SCL_CTL_EN** (line 72)
- **P2WI_LCR_SCL_STATE** (line 69)
- **P2WI_LCR_SDA_CTL** (line 73)
- **P2WI_LCR_SDA_CTL_EN** (line 74)
- **P2WI_LCR_SDA_STATE** (line 70)
- **P2WI_MAX_FREQ** (line 82)
- **P2WI_PMCR** (line 45)
- **P2WI_PMCR_PMU_DEV_ADDR**(v) (line 80)
- **P2WI_PMCR_PMU_INIT_DATA**(v) (line 78)
- **P2WI_PMCR_PMU_INIT_SEND** (line 77)
- **P2WI_PMCR_PMU_MODE_REG**(v) (line 79)
