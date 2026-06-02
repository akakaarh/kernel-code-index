# drivers/i2c/busses/i2c-gxp.c

Subsystem: drivers/i2c

## Functions (15)

### gxp_i2c_ack_data
- Return type: static void
- Signature: gxp_i2c_ack_data(struct gxp_i2c_drvdata * drvdata)
- Line: 277

### gxp_i2c_chk_addr_ack
- Return type: static void
- Signature: gxp_i2c_chk_addr_ack(struct gxp_i2c_drvdata * drvdata)
- Line: 225

### gxp_i2c_chk_data_ack
- Return type: static void
- Signature: gxp_i2c_chk_data_ack(struct gxp_i2c_drvdata * drvdata)
- Line: 316

### gxp_i2c_func
- Return type: static u32
- Signature: gxp_i2c_func(struct i2c_adapter * adap)
- Line: 142

### gxp_i2c_init
- Return type: static void
- Signature: gxp_i2c_init(struct gxp_i2c_drvdata * drvdata)
- Line: 490

### gxp_i2c_irq_handler
- Return type: static irqreturn_t
- Signature: gxp_i2c_irq_handler(int irq,void * _drvdata)
- Line: 441

### gxp_i2c_master_xfer
- Return type: static int
- Signature: gxp_i2c_master_xfer(struct i2c_adapter * adapter,struct i2c_msg * msgs,int num)
- Line: 113

### gxp_i2c_probe
- Return type: static int
- Signature: gxp_i2c_probe(struct platform_device * pdev)
- Line: 508

### gxp_i2c_reg_slave
- Return type: static int
- Signature: gxp_i2c_reg_slave(struct i2c_client * slave)
- Line: 151

### gxp_i2c_remove
- Return type: static void
- Signature: gxp_i2c_remove(struct platform_device * pdev)
- Line: 581

### gxp_i2c_restart
- Return type: static void
- Signature: gxp_i2c_restart(struct gxp_i2c_drvdata * drvdata)
- Line: 203

### gxp_i2c_slave_irq_handler
- Return type: static bool
- Signature: gxp_i2c_slave_irq_handler(struct gxp_i2c_drvdata * drvdata)
- Line: 357

### gxp_i2c_start
- Return type: static void
- Signature: gxp_i2c_start(struct gxp_i2c_drvdata * drvdata)
- Line: 96

### gxp_i2c_stop
- Return type: static void
- Signature: gxp_i2c_stop(struct gxp_i2c_drvdata * drvdata)
- Line: 195

### gxp_i2c_unreg_slave
- Return type: static int
- Signature: gxp_i2c_unreg_slave(struct i2c_client * slave)
- Line: 170

## Structs (1)

### gxp_i2c_drvdata
- Line: 76
- Members:
  - dev: device *
  - base: void __iomem *
  - t: i2c_timings
  - engine: u32
  - irq: int
  - completion: completion
  - adapter: i2c_adapter
  - curr_msg: i2c_msg *
  - msgs_remaining: int
  - msgs_num: int
  - buf: u8 *
  - buf_remaining: size_t
  - state: unsigned char
  - slave: i2c_client *
  - stopped: unsigned char

## Enums (1)

### __anon23bced590103
- Line: 65

## Variables (5)

- static **gxp_i2c_algo** : const struct i2c_algorithm (line 186)
- static **gxp_i2c_driver** : platform_driver (line 596)
- static **gxp_i2c_name** : const char * const[] (line 14)
- static **gxp_i2c_of_match** : const struct of_device_id[] (line 590)
- static **i2cg_map** : regmap * (line 94)

## Macros (35)

- **FAIRNESS_CNT** (line 63)
- **FILTER_CNT** (line 62)
- **GXP_DATA_EDGE_RST_CTRL** (line 59)
- **GXP_I2CADVFEAT** (line 36)
- **GXP_I2CCYCTIM** (line 41)
- **GXP_I2CEVTERR** (line 28)
- **GXP_I2CFLTFAIR** (line 39)
- **GXP_I2CFREQDIV** (line 38)
- **GXP_I2CINTEN** (line 21)
- **GXP_I2CINTSTAT** (line 20)
- **GXP_I2CMCMD** (line 33)
- **GXP_I2COWNADR** (line 37)
- **GXP_I2CSCMD** (line 34)
- **GXP_I2CSNPAA** (line 35)
- **GXP_I2CSNPDAT** (line 32)
- **GXP_I2CSTAT** (line 24)
- **GXP_I2CTMOEDG** (line 40)
- **GXP_MAX_I2C_ENGINE** (line 13)
- **MASK_ACK** (line 26)
- **MASK_MASTER_EVENT** (line 31)
- **MASK_RW** (line 27)
- **MASK_SLAVE_CMD_EVENT** (line 29)
- **MASK_SLAVE_DATA_EVENT** (line 30)
- **MASK_STOP_EVENT** (line 25)
- **MASTER_ACK_ENAB** (line 53)
- **MASTER_EVT_CLR** (line 52)
- **RW_CMD** (line 54)
- **SLAVE_ACK_ENAB** (line 48)
- **SLAVE_EVT_CLR** (line 45)
- **SLAVE_EVT_MASK** (line 47)
- **SLAVE_EVT_STALL** (line 49)
- **SNOOP_EVT_CLR** (line 44)
- **SNOOP_EVT_MASK** (line 46)
- **START_CMD** (line 56)
- **STOP_CMD** (line 55)
