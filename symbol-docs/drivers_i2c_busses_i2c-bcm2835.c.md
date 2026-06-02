# drivers/i2c/busses/i2c-bcm2835.c

Subsystem: drivers/i2c

## Functions (16)

### bcm2835_drain_rxfifo
- Return type: static void
- Signature: bcm2835_drain_rxfifo(struct bcm2835_i2c_dev * i2c_dev)
- Line: 210

### bcm2835_fill_txfifo
- Return type: static void
- Signature: bcm2835_fill_txfifo(struct bcm2835_i2c_dev * i2c_dev)
- Line: 195

### bcm2835_i2c_finish_transfer
- Return type: static void
- Signature: bcm2835_i2c_finish_transfer(struct bcm2835_i2c_dev * i2c_dev)
- Line: 264

### bcm2835_i2c_func
- Return type: static u32
- Signature: bcm2835_i2c_func(struct i2c_adapter * adap)
- Line: 389

### bcm2835_i2c_isr
- Return type: static irqreturn_t
- Signature: bcm2835_i2c_isr(int this_irq,void * data)
- Line: 282

### bcm2835_i2c_probe
- Return type: static int
- Signature: bcm2835_i2c_probe(struct platform_device * pdev)
- Line: 408

### bcm2835_i2c_readl
- Return type: static u32
- Signature: bcm2835_i2c_readl(struct bcm2835_i2c_dev * i2c_dev,u32 reg)
- Line: 79

### bcm2835_i2c_register_div
- Return type: static clk *
- Signature: bcm2835_i2c_register_div(struct device * dev,struct clk * mclk,struct bcm2835_i2c_dev * i2c_dev)
- Line: 165

### bcm2835_i2c_remove
- Return type: static void
- Signature: bcm2835_i2c_remove(struct platform_device * pdev)
- Line: 505

### bcm2835_i2c_start_transfer
- Return type: static void
- Signature: bcm2835_i2c_start_transfer(struct bcm2835_i2c_dev * i2c_dev)
- Line: 238

### bcm2835_i2c_writel
- Return type: static void
- Signature: bcm2835_i2c_writel(struct bcm2835_i2c_dev * i2c_dev,u32 reg,u32 val)
- Line: 73

### bcm2835_i2c_xfer
- Return type: static int
- Signature: bcm2835_i2c_xfer(struct i2c_adapter * adap,struct i2c_msg msgs[],int num)
- Line: 347

### clk_bcm2835_i2c_calc_divider
- Return type: static int
- Signature: clk_bcm2835_i2c_calc_divider(unsigned long rate,unsigned long parent_rate)
- Line: 90

### clk_bcm2835_i2c_determine_rate
- Return type: static int
- Signature: clk_bcm2835_i2c_determine_rate(struct clk_hw * hw,struct clk_rate_request * req)
- Line: 140

### clk_bcm2835_i2c_recalc_rate
- Return type: static unsigned long
- Signature: clk_bcm2835_i2c_recalc_rate(struct clk_hw * hw,unsigned long parent_rate)
- Line: 150

### clk_bcm2835_i2c_set_rate
- Return type: static int
- Signature: clk_bcm2835_i2c_set_rate(struct clk_hw * hw,unsigned long rate,unsigned long parent_rate)
- Line: 109

## Structs (2)

### bcm2835_i2c_dev
- Line: 59
- Members:
  - dev: device *
  - regs: void __iomem *
  - irq: int
  - adapter: i2c_adapter
  - completion: completion
  - curr_msg: i2c_msg *
  - bus_clk: clk *
  - num_msgs: int
  - msg_err: u32
  - msg_buf: u8 *
  - msg_buf_remaining: size_t
  - hw: clk_hw
  - i2c_dev: bcm2835_i2c_dev *

### clk_bcm2835_i2c
- Line: 85
- Members:
  - dev: device *
  - regs: void __iomem *
  - irq: int
  - adapter: i2c_adapter
  - completion: completion
  - curr_msg: i2c_msg *
  - bus_clk: clk *
  - num_msgs: int
  - msg_err: u32
  - msg_buf: u8 *
  - msg_buf_remaining: size_t
  - hw: clk_hw
  - i2c_dev: bcm2835_i2c_dev *

## Variables (5)

- static **bcm2835_i2c_algo** : const struct i2c_algorithm (line 394)
- static **bcm2835_i2c_driver** : platform_driver (line 523)
- static **bcm2835_i2c_of_match** : const struct of_device_id[] (line 516)
- static **bcm2835_i2c_quirks** : const struct i2c_adapter_quirks (line 404)
- static **clk_bcm2835_i2c_ops** : const struct clk_ops (line 159)

## Macros (31)

- **BCM2835_I2C_A** (line 22)
- **BCM2835_I2C_C** (line 19)
- **BCM2835_I2C_CDIV_MAX** (line 57)
- **BCM2835_I2C_CDIV_MIN** (line 56)
- **BCM2835_I2C_CLKT** (line 31)
- **BCM2835_I2C_C_CLEAR** (line 34)
- **BCM2835_I2C_C_I2CEN** (line 39)
- **BCM2835_I2C_C_INTD** (line 36)
- **BCM2835_I2C_C_INTR** (line 38)
- **BCM2835_I2C_C_INTT** (line 37)
- **BCM2835_I2C_C_READ** (line 33)
- **BCM2835_I2C_C_ST** (line 35)
- **BCM2835_I2C_DEL** (line 25)
- **BCM2835_I2C_DIV** (line 24)
- **BCM2835_I2C_DLEN** (line 21)
- **BCM2835_I2C_FEDL_SHIFT** (line 53)
- **BCM2835_I2C_FIFO** (line 23)
- **BCM2835_I2C_REDL_SHIFT** (line 54)
- **BCM2835_I2C_S** (line 20)
- **BCM2835_I2C_S_CLKT** (line 50)
- **BCM2835_I2C_S_DONE** (line 42)
- **BCM2835_I2C_S_ERR** (line 49)
- **BCM2835_I2C_S_LEN** (line 51)
- **BCM2835_I2C_S_RXD** (line 46)
- **BCM2835_I2C_S_RXF** (line 48)
- **BCM2835_I2C_S_RXR** (line 44)
- **BCM2835_I2C_S_TA** (line 41)
- **BCM2835_I2C_S_TXD** (line 45)
- **BCM2835_I2C_S_TXE** (line 47)
- **BCM2835_I2C_S_TXW** (line 43)
- **to_clk_bcm2835_i2c**(_hw) (line 84)
