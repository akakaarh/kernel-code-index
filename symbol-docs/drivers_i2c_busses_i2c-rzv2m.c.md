# drivers/i2c/busses/i2c-rzv2m.c

Subsystem: drivers/i2c

## Functions (19)

### bit_clrl
- Return type: static void
- Signature: bit_clrl(void __iomem * addr,u32 val)
- Line: 83

### bit_setl
- Return type: static void
- Signature: bit_setl(void __iomem * addr,u32 val)
- Line: 78

### rzv2m_i2c_clock_calculate
- Return type: static int
- Signature: rzv2m_i2c_clock_calculate(struct device * dev,struct rzv2m_i2c_priv * priv)
- Line: 98

### rzv2m_i2c_disable
- Return type: static int
- Signature: rzv2m_i2c_disable(struct device * dev,struct rzv2m_i2c_priv * priv)
- Line: 386

### rzv2m_i2c_func
- Return type: static u32
- Signature: rzv2m_i2c_func(struct i2c_adapter * adap)
- Line: 380

### rzv2m_i2c_init
- Return type: static void
- Signature: rzv2m_i2c_init(struct rzv2m_i2c_priv * priv)
- Line: 156

### rzv2m_i2c_probe
- Return type: static int
- Signature: rzv2m_i2c_probe(struct platform_device * pdev)
- Line: 409

### rzv2m_i2c_read_with_ack
- Return type: static int
- Signature: rzv2m_i2c_read_with_ack(struct rzv2m_i2c_priv * priv,u8 * data,bool last)
- Line: 199

### rzv2m_i2c_receive
- Return type: static int
- Signature: rzv2m_i2c_receive(struct rzv2m_i2c_priv * priv,struct i2c_msg * msg,unsigned int * count)
- Line: 266

### rzv2m_i2c_remove
- Return type: static void
- Signature: rzv2m_i2c_remove(struct platform_device * pdev)
- Line: 480

### rzv2m_i2c_resume
- Return type: static int
- Signature: rzv2m_i2c_resume(struct device * dev)
- Line: 497

### rzv2m_i2c_send
- Return type: static int
- Signature: rzv2m_i2c_send(struct rzv2m_i2c_priv * priv,struct i2c_msg * msg,unsigned int * count)
- Line: 250

### rzv2m_i2c_send_address
- Return type: static int
- Signature: rzv2m_i2c_send_address(struct rzv2m_i2c_priv * priv,struct i2c_msg * msg)
- Line: 283

### rzv2m_i2c_stop_condition
- Return type: static int
- Signature: rzv2m_i2c_stop_condition(struct rzv2m_i2c_priv * priv)
- Line: 308

### rzv2m_i2c_suspend
- Return type: static int
- Signature: rzv2m_i2c_suspend(struct device * dev)
- Line: 490

### rzv2m_i2c_tia_irq_handler
- Return type: static irqreturn_t
- Signature: rzv2m_i2c_tia_irq_handler(int this_irq,void * dev_id)
- Line: 88

### rzv2m_i2c_write_with_ack
- Return type: static int
- Signature: rzv2m_i2c_write_with_ack(struct rzv2m_i2c_priv * priv,u32 data)
- Line: 179

### rzv2m_i2c_xfer
- Return type: static int
- Signature: rzv2m_i2c_xfer(struct i2c_adapter * adap,struct i2c_msg * msgs,int num)
- Line: 349

### rzv2m_i2c_xfer_msg
- Return type: static int
- Signature: rzv2m_i2c_xfer_msg(struct rzv2m_i2c_priv * priv,struct i2c_msg * msg,int stop)
- Line: 319

## Structs (2)

### bitrate_config
- Line: 68
- Members:
  - base: void __iomem *
  - adap: i2c_adapter
  - clk: clk *
  - bus_mode: int
  - msg_tia_done: completion
  - iicb0wl: u32
  - iicb0wh: u32
  - percent_low: unsigned int
  - min_hold_time_ns: unsigned int

### rzv2m_i2c_priv
- Line: 53
- Members:
  - base: void __iomem *
  - adap: i2c_adapter
  - clk: clk *
  - bus_mode: int
  - msg_tia_done: completion
  - iicb0wl: u32
  - iicb0wh: u32
  - percent_low: unsigned int
  - min_hold_time_ns: unsigned int

## Enums (1)

### bcr_index
- Line: 63

## Variables (6)

- static **bitrate_configs** : const struct bitrate_config[] (line 73)
- static **rzv2m_i2c_algo** : const struct i2c_algorithm (line 404)
- static **rzv2m_i2c_driver** : platform_driver (line 526)
- static **rzv2m_i2c_ids** : const struct of_device_id[] (line 516)
- static **rzv2m_i2c_pm_ops** : const struct dev_pm_ops (line 522)
- static **rzv2m_i2c_quirks** : const struct i2c_adapter_quirks (line 400)

## Macros (18)

- **IICB0CTL0** (line 27)
- **IICB0CTL1** (line 30)
- **IICB0DAT** (line 26)
- **IICB0IICE** (line 35)
- **IICB0MDSC** (line 50)
- **IICB0SLAC** (line 37)
- **IICB0SLSE** (line 51)
- **IICB0SLWT** (line 36)
- **IICB0SPT** (line 42)
- **IICB0SSAC** (line 45)
- **IICB0SSBS** (line 46)
- **IICB0SSSP** (line 47)
- **IICB0STR0** (line 29)
- **IICB0STT** (line 41)
- **IICB0TRG** (line 28)
- **IICB0WH** (line 32)
- **IICB0WL** (line 31)
- **IICB0WRET** (line 40)
