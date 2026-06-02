# drivers/i2c/busses/i2c-brcmstb.c

Subsystem: drivers/i2c

## Functions (21)

### bcm2711_release_bsc
- Return type: static int
- Signature: bcm2711_release_bsc(struct brcmstb_i2c_dev * dev)
- Line: 592

### brcmstb_i2c_do_addr
- Return type: static int
- Signature: brcmstb_i2c_do_addr(struct brcmstb_i2c_dev * dev,struct i2c_msg * msg)
- Line: 410

### brcmstb_i2c_enable_disable_irq
- Return type: static void
- Signature: brcmstb_i2c_enable_disable_irq(struct brcmstb_i2c_dev * dev,bool int_en)
- Line: 191

### brcmstb_i2c_functionality
- Return type: static u32
- Signature: brcmstb_i2c_functionality(struct i2c_adapter * adap)
- Line: 539

### brcmstb_i2c_get_data_regsz
- Return type: static int
- Signature: brcmstb_i2c_get_data_regsz(struct brcmstb_i2c_dev * dev)
- Line: 186

### brcmstb_i2c_get_xfersz
- Return type: static int
- Signature: brcmstb_i2c_get_xfersz(struct brcmstb_i2c_dev * dev)
- Line: 181

### brcmstb_i2c_isr
- Return type: static irqreturn_t
- Signature: brcmstb_i2c_isr(int irq,void * devid)
- Line: 206

### brcmstb_i2c_probe
- Return type: static int
- Signature: brcmstb_i2c_probe(struct platform_device * pdev)
- Line: 612

### brcmstb_i2c_remove
- Return type: static void
- Signature: brcmstb_i2c_remove(struct platform_device * pdev)
- Line: 703

### brcmstb_i2c_resume
- Return type: static int
- Signature: brcmstb_i2c_resume(struct device * dev)
- Line: 718

### brcmstb_i2c_set_bsc_reg_defaults
- Return type: static void
- Signature: brcmstb_i2c_set_bsc_reg_defaults(struct brcmstb_i2c_dev * dev)
- Line: 576

### brcmstb_i2c_set_bus_speed
- Return type: static void
- Signature: brcmstb_i2c_set_bus_speed(struct brcmstb_i2c_dev * dev)
- Line: 551

### brcmstb_i2c_suspend
- Return type: static int
- Signature: brcmstb_i2c_suspend(struct device * dev)
- Line: 710

### brcmstb_i2c_wait_for_completion
- Return type: static int
- Signature: brcmstb_i2c_wait_for_completion(struct brcmstb_i2c_dev * dev)
- Line: 239

### brcmstb_i2c_wait_if_busy
- Return type: static int
- Signature: brcmstb_i2c_wait_if_busy(struct brcmstb_i2c_dev * dev)
- Line: 226

### brcmstb_i2c_write_data_byte
- Return type: static int
- Signature: brcmstb_i2c_write_data_byte(struct brcmstb_i2c_dev * dev,u8 * buf,unsigned int nak_expected)
- Line: 398

### brcmstb_i2c_xfer
- Return type: static int
- Signature: brcmstb_i2c_xfer(struct i2c_adapter * adapter,struct i2c_msg msgs[],int num)
- Line: 443

### brcmstb_i2c_xfer_atomic
- Return type: static int
- Signature: brcmstb_i2c_xfer_atomic(struct i2c_adapter * adapter,struct i2c_msg msgs[],int num)
- Line: 522

### brcmstb_i2c_xfer_bsc_data
- Return type: static int
- Signature: brcmstb_i2c_xfer_bsc_data(struct brcmstb_i2c_dev * dev,u8 * buf,unsigned int len,struct i2c_msg * pmsg)
- Line: 324

### brcmstb_send_i2c_cmd
- Return type: static int
- Signature: brcmstb_send_i2c_cmd(struct brcmstb_i2c_dev * dev,enum bsc_xfer_cmd cmd)
- Line: 279

### brcmstb_set_i2c_start_stop
- Return type: static void
- Signature: brcmstb_set_i2c_start_stop(struct brcmstb_i2c_dev * dev,u32 cond_flag)
- Line: 270

## Structs (3)

### brcmstb_i2c_dev
- Line: 154
- Members:
  - chip_address: u32
  - data_in: u32[]
  - cnt_reg: u32
  - ctl_reg: u32
  - iic_enable: u32
  - data_out: u32[]
  - ctlhi_reg: u32
  - scl_param: u32
  - hz: u32
  - scl_mask: u32
  - div_mask: u32
  - device: device *
  - base: void __iomem *
  - irq: int
  - bsc_regmap: bsc_regs *
  - adapter: i2c_adapter
  - done: completion
  - clk_freq_hz: u32
  - data_regsz: int
  - atomic: bool

### bsc_clk_param
- Line: 80
- Members:
  - chip_address: u32
  - data_in: u32[]
  - cnt_reg: u32
  - ctl_reg: u32
  - iic_enable: u32
  - data_out: u32[]
  - ctlhi_reg: u32
  - scl_param: u32
  - hz: u32
  - scl_mask: u32
  - div_mask: u32
  - device: device *
  - base: void __iomem *
  - irq: int
  - bsc_regmap: bsc_regs *
  - adapter: i2c_adapter
  - done: completion
  - clk_freq_hz: u32
  - data_regsz: int
  - atomic: bool

### bsc_regs
- Line: 69
- Members:
  - chip_address: u32
  - data_in: u32[]
  - cnt_reg: u32
  - ctl_reg: u32
  - iic_enable: u32
  - data_out: u32[]
  - ctlhi_reg: u32
  - scl_param: u32
  - hz: u32
  - scl_mask: u32
  - div_mask: u32
  - device: device *
  - base: void __iomem *
  - irq: int
  - bsc_regmap: bsc_regs *
  - adapter: i2c_adapter
  - done: completion
  - clk_freq_hz: u32
  - data_regsz: int
  - atomic: bool

## Enums (2)

### bsc_xfer_cmd
- Line: 86

### bus_speeds
- Line: 100

## Variables (5)

- static **brcmstb_i2c_algo** : const struct i2c_algorithm (line 545)
- static **brcmstb_i2c_driver** : platform_driver (line 739)
- static **brcmstb_i2c_of_match** : const struct of_device_id[] (line 731)
- static **bsc_clk** : const struct bsc_clk_param[] (line 111)
- static **cmd_string** : char const * [] (line 93)

## Macros (38)

- **AUTOI2C_CTRL0** (line 589)
- **AUTOI2C_CTRL0_RELEASE_BSC** (line 590)
- **BSC_CNT_REG1_MASK**(nb) (line 25)
- **BSC_CNT_REG1_SHIFT** (line 26)
- **BSC_CTLHI_REG_DATAREG_SIZE_MASK** (line 46)
- **BSC_CTLHI_REG_IGNORE_ACK_MASK** (line 47)
- **BSC_CTLHI_REG_INPUT_SWITCHING_LEVEL_MASK** (line 45)
- **BSC_CTLHI_REG_WAIT_DIS_MASK** (line 48)
- **BSC_CTL_REG_DIV_CLK_MASK** (line 34)
- **BSC_CTL_REG_DTF_MASK** (line 29)
- **BSC_CTL_REG_INT_EN_MASK** (line 32)
- **BSC_CTL_REG_INT_EN_SHIFT** (line 33)
- **BSC_CTL_REG_SCL_SEL_MASK** (line 30)
- **BSC_CTL_REG_SCL_SEL_SHIFT** (line 31)
- **BSC_IIC_EN_ENABLE_MASK** (line 42)
- **BSC_IIC_EN_INTRP_MASK** (line 41)
- **BSC_IIC_EN_NOACK_MASK** (line 40)
- **BSC_IIC_EN_NOSTART_MASK** (line 38)
- **BSC_IIC_EN_NOSTOP_MASK** (line 39)
- **BSC_IIC_EN_RESTART_MASK** (line 37)
- **COND_NOSTART** (line 54)
- **COND_NOSTOP** (line 55)
- **COND_RESTART** (line 53)
- **COND_START_STOP** (line 56)
- **DTF_RD_MASK** (line 60)
- **DTF_RD_WR_MASK** (line 62)
- **DTF_WR_MASK** (line 59)
- **DTF_WR_RD_MASK** (line 63)
- **I2C_TIMEOUT** (line 50)
- **INT_DISABLE** (line 66)
- **INT_ENABLE** (line 65)
- **N_DATA_REGS** (line 16)
- **__bsc_readl**(_reg) (line 168)
- **__bsc_readl**(_reg) (line 171)
- **__bsc_writel**(_val,_reg) (line 169)
- **__bsc_writel**(_val,_reg) (line 172)
- **bsc_readl**(_dev,_reg) (line 175)
- **bsc_writel**(_dev,_val,_reg) (line 178)
