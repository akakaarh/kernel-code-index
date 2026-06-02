# drivers/i2c/busses/i2c-synquacer.c

Subsystem: drivers/i2c

## Functions (14)

### calc_timeout_ms
- Return type: static unsigned long
- Signature: calc_timeout_ms(struct synquacer_i2c * i2c,struct i2c_msg * msgs,int num)
- Line: 164

### is_lastmsg
- Return type: static int
- Signature: is_lastmsg(struct synquacer_i2c * i2c)
- Line: 149

### is_msgend
- Return type: static int
- Signature: is_msgend(struct synquacer_i2c * i2c)
- Line: 159

### is_msglast
- Return type: static int
- Signature: is_msglast(struct synquacer_i2c * i2c)
- Line: 154

### synquacer_i2c_doxfer
- Return type: static int
- Signature: synquacer_i2c_doxfer(struct synquacer_i2c * i2c,struct i2c_msg * msgs,int num)
- Line: 310

### synquacer_i2c_functionality
- Return type: static u32
- Signature: synquacer_i2c_functionality(struct i2c_adapter * adap)
- Line: 518

### synquacer_i2c_hw_init
- Return type: static void
- Signature: synquacer_i2c_hw_init(struct synquacer_i2c * i2c)
- Line: 198

### synquacer_i2c_hw_reset
- Return type: static void
- Signature: synquacer_i2c_hw_reset(struct synquacer_i2c * i2c)
- Line: 249

### synquacer_i2c_isr
- Return type: static irqreturn_t
- Signature: synquacer_i2c_isr(int irq,void * dev_id)
- Line: 357

### synquacer_i2c_master_start
- Return type: static int
- Signature: synquacer_i2c_master_start(struct synquacer_i2c * i2c,struct i2c_msg * pmsg)
- Line: 258

### synquacer_i2c_probe
- Return type: static int
- Signature: synquacer_i2c_probe(struct platform_device * pdev)
- Line: 535

### synquacer_i2c_remove
- Return type: static void
- Signature: synquacer_i2c_remove(struct platform_device * pdev)
- Line: 610

### synquacer_i2c_stop
- Return type: static void
- Signature: synquacer_i2c_stop(struct synquacer_i2c * i2c,int ret)
- Line: 177

### synquacer_i2c_xfer
- Return type: static int
- Signature: synquacer_i2c_xfer(struct i2c_adapter * adap,struct i2c_msg * msgs,int num)
- Line: 494

## Structs (1)

### synquacer_i2c
- Line: 131
- Members:
  - completion: completion
  - msg: i2c_msg *
  - msg_num: u32
  - msg_idx: u32
  - msg_ptr: u32
  - irq: int
  - dev: device *
  - base: void __iomem *
  - pclkrate: u32
  - speed_khz: u32
  - timeout_ms: u32
  - state: i2c_state
  - adapter: i2c_adapter

## Enums (1)

### i2c_state
- Line: 124

## Variables (5)

- static **synquacer_i2c_acpi_ids** : const struct acpi_device_id[] (line 624)
- static **synquacer_i2c_algo** : const struct i2c_algorithm (line 523)
- static **synquacer_i2c_driver** : platform_driver (line 631)
- static **synquacer_i2c_dt_ids** : const struct of_device_id[]__maybe_unused (line 617)
- static **synquacer_i2c_ops** : const struct i2c_adapter (line 528)

## Macros (49)

- **SYNQUACER_I2C_BC2R_SCLL** (line 61)
- **SYNQUACER_I2C_BC2R_SCLS** (line 63)
- **SYNQUACER_I2C_BC2R_SDAL** (line 62)
- **SYNQUACER_I2C_BC2R_SDAS** (line 64)
- **SYNQUACER_I2C_BCR_ACK** (line 49)
- **SYNQUACER_I2C_BCR_BEIE** (line 52)
- **SYNQUACER_I2C_BCR_BER** (line 53)
- **SYNQUACER_I2C_BCR_GCAA** (line 48)
- **SYNQUACER_I2C_BCR_INT** (line 46)
- **SYNQUACER_I2C_BCR_INTE** (line 47)
- **SYNQUACER_I2C_BCR_MSS** (line 50)
- **SYNQUACER_I2C_BCR_SCC** (line 51)
- **SYNQUACER_I2C_BSR_AAS** (line 39)
- **SYNQUACER_I2C_BSR_AL** (line 42)
- **SYNQUACER_I2C_BSR_BB** (line 44)
- **SYNQUACER_I2C_BSR_FBT** (line 37)
- **SYNQUACER_I2C_BSR_GCA** (line 38)
- **SYNQUACER_I2C_BSR_LRB** (line 41)
- **SYNQUACER_I2C_BSR_RSC** (line 43)
- **SYNQUACER_I2C_BSR_TRX** (line 40)
- **SYNQUACER_I2C_BUS_CLK_FR**(rate) (line 67)
- **SYNQUACER_I2C_CCR_CS_FAST_MAX_18M**(rate) (line 86)
- **SYNQUACER_I2C_CCR_CS_FAST_MIN_18M**(rate) (line 105)
- **SYNQUACER_I2C_CCR_CS_MASK** (line 55)
- **SYNQUACER_I2C_CCR_CS_STD_MAX_18M**(rate) (line 78)
- **SYNQUACER_I2C_CCR_CS_STD_MIN_18M**(rate) (line 95)
- **SYNQUACER_I2C_CCR_EN** (line 56)
- **SYNQUACER_I2C_CCR_FM** (line 57)
- **SYNQUACER_I2C_CLK_MASTER_FAST**(rate) (line 73)
- **SYNQUACER_I2C_CLK_MASTER_STD**(rate) (line 70)
- **SYNQUACER_I2C_CLK_RATE_18M** (line 119)
- **SYNQUACER_I2C_CSR_CS_FAST_MAX_18M**(rate) (line 91)
- **SYNQUACER_I2C_CSR_CS_FAST_MIN_18M**(rate) (line 110)
- **SYNQUACER_I2C_CSR_CS_MASK** (line 59)
- **SYNQUACER_I2C_CSR_CS_STD_MAX_18M**(rate) (line 83)
- **SYNQUACER_I2C_CSR_CS_STD_MIN_18M**(rate) (line 100)
- **SYNQUACER_I2C_MAX_CLK_RATE** (line 117)
- **SYNQUACER_I2C_MIN_CLK_RATE** (line 115)
- **SYNQUACER_I2C_REG_ADR** (line 30)
- **SYNQUACER_I2C_REG_BC2R** (line 34)
- **SYNQUACER_I2C_REG_BCR** (line 28)
- **SYNQUACER_I2C_REG_BSR** (line 27)
- **SYNQUACER_I2C_REG_CCR** (line 29)
- **SYNQUACER_I2C_REG_CSR** (line 32)
- **SYNQUACER_I2C_REG_DAR** (line 31)
- **SYNQUACER_I2C_REG_FSR** (line 33)
- **SYNQUACER_I2C_SPEED_FM** (line 121)
- **SYNQUACER_I2C_SPEED_SM** (line 122)
- **WAIT_PCLK**(n,rate) (line 23)
