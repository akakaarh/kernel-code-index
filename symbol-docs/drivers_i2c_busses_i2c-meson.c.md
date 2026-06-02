# drivers/i2c/busses/i2c-meson.c

Subsystem: drivers/i2c

## Functions (18)

### meson6_i2c_set_clk_div
- Return type: static void
- Signature: meson6_i2c_set_clk_div(struct meson_i2c * i2c,unsigned int freq)
- Line: 187

### meson_gxbb_axg_i2c_set_clk_div
- Return type: static void
- Signature: meson_gxbb_axg_i2c_set_clk_div(struct meson_i2c * i2c,unsigned int freq)
- Line: 139

### meson_i2c_add_token
- Return type: static void
- Signature: meson_i2c_add_token(struct meson_i2c * i2c,int token)
- Line: 129

### meson_i2c_do_start
- Return type: static void
- Signature: meson_i2c_do_start(struct meson_i2c * i2c,struct i2c_msg * msg)
- Line: 337

### meson_i2c_func
- Return type: static u32
- Signature: meson_i2c_func(struct i2c_adapter * adap)
- Line: 445

### meson_i2c_get_data
- Return type: static void
- Signature: meson_i2c_get_data(struct meson_i2c * i2c,char * buf,int len)
- Line: 215

### meson_i2c_irq
- Return type: static irqreturn_t
- Signature: meson_i2c_irq(int irqno,void * dev_id)
- Line: 302

### meson_i2c_prepare_xfer
- Return type: static void
- Signature: meson_i2c_prepare_xfer(struct meson_i2c * i2c)
- Line: 251

### meson_i2c_probe
- Return type: static int
- Signature: meson_i2c_probe(struct platform_device * pdev)
- Line: 456

### meson_i2c_put_data
- Return type: static void
- Signature: meson_i2c_put_data(struct meson_i2c * i2c,char * buf,int len)
- Line: 233

### meson_i2c_remove
- Return type: static void
- Signature: meson_i2c_remove(struct platform_device * pdev)
- Line: 537

### meson_i2c_reset_tokens
- Return type: static void
- Signature: meson_i2c_reset_tokens(struct meson_i2c * i2c)
- Line: 122

### meson_i2c_set_mask
- Return type: static void
- Signature: meson_i2c_set_mask(struct meson_i2c * i2c,int reg,u32 mask,u32 val)
- Line: 111

### meson_i2c_transfer_complete
- Return type: static void
- Signature: meson_i2c_transfer_complete(struct meson_i2c * i2c,u32 ctrl)
- Line: 278

### meson_i2c_xfer
- Return type: static int
- Signature: meson_i2c_xfer(struct i2c_adapter * adap,struct i2c_msg * msgs,int num)
- Line: 433

### meson_i2c_xfer_atomic
- Return type: static int
- Signature: meson_i2c_xfer_atomic(struct i2c_adapter * adap,struct i2c_msg * msgs,int num)
- Line: 439

### meson_i2c_xfer_messages
- Return type: static int
- Signature: meson_i2c_xfer_messages(struct i2c_adapter * adap,struct i2c_msg * msgs,int num,bool atomic)
- Line: 418

### meson_i2c_xfer_msg
- Return type: static int
- Signature: meson_i2c_xfer_msg(struct meson_i2c * i2c,struct i2c_msg * msg,int last,bool atomic)
- Line: 352

## Structs (2)

### meson_i2c
- Line: 86
- Members:
  - adap: i2c_adapter
  - dev: device *
  - regs: void __iomem *
  - clk: clk *
  - msg: i2c_msg *
  - state: int
  - last: bool
  - count: int
  - pos: int
  - error: int
  - lock: spinlock_t
  - done: completion
  - tokens: u32[2]
  - num_tokens: int
  - data: const struct meson_i2c_data *
  - set_clk_div: void (*)(struct meson_i2c * i2c,unsigned int freq)

### meson_i2c_data
- Line: 107
- Members:
  - adap: i2c_adapter
  - dev: device *
  - regs: void __iomem *
  - clk: clk *
  - msg: i2c_msg *
  - state: int
  - last: bool
  - count: int
  - pos: int
  - error: int
  - lock: spinlock_t
  - done: completion
  - tokens: u32[2]
  - num_tokens: int
  - data: const struct meson_i2c_data *
  - set_clk_div: void (*)(struct meson_i2c * i2c,unsigned int freq)

## Enums (2)

### __anona893336c0103
- Line: 51

### __anona893336c0203
- Line: 61

## Variables (6)

- static **i2c_axg_data** : const struct meson_i2c_data (line 553)
- static **i2c_gxbb_data** : const struct meson_i2c_data (line 549)
- static **i2c_meson6_data** : const struct meson_i2c_data (line 545)
- static **meson_i2c_algorithm** : const struct i2c_algorithm (line 450)
- static **meson_i2c_driver** : platform_driver (line 566)
- static **meson_i2c_match** : const struct of_device_id[] (line 557)

## Macros (24)

- **FILTER_DELAY** (line 49)
- **I2C_TIMEOUT_MS** (line 48)
- **REG_CTRL** (line 22)
- **REG_CTRL_ACK_IGNORE** (line 33)
- **REG_CTRL_CLKDIVEXT_MASK** (line 39)
- **REG_CTRL_CLKDIVEXT_SHIFT** (line 38)
- **REG_CTRL_CLKDIV_MASK** (line 37)
- **REG_CTRL_CLKDIV_SHIFT** (line 36)
- **REG_CTRL_ERROR** (line 35)
- **REG_CTRL_START** (line 32)
- **REG_CTRL_STATUS** (line 34)
- **REG_SLAVE_ADDR** (line 23)
- **REG_SLV_ADDR_MASK** (line 41)
- **REG_SLV_SCL_FILTER_MASK** (line 43)
- **REG_SLV_SCL_LOW_EN** (line 46)
- **REG_SLV_SCL_LOW_MASK** (line 45)
- **REG_SLV_SCL_LOW_SHIFT** (line 44)
- **REG_SLV_SDA_FILTER_MASK** (line 42)
- **REG_TOK_LIST0** (line 24)
- **REG_TOK_LIST1** (line 25)
- **REG_TOK_RDATA0** (line 28)
- **REG_TOK_RDATA1** (line 29)
- **REG_TOK_WDATA0** (line 26)
- **REG_TOK_WDATA1** (line 27)
