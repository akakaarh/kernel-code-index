# drivers/i2c/busses/i2c-davinci.c

Subsystem: drivers/i2c

## Functions (30)

### davinci_i2c_exit_driver
- Return type: static void __exit
- Signature: davinci_i2c_exit_driver(void)
- Line: 907

### davinci_i2c_get_scl
- Return type: static int
- Signature: davinci_i2c_get_scl(struct i2c_adapter * adap)
- Line: 318

### davinci_i2c_get_sda
- Return type: static int
- Signature: davinci_i2c_get_sda(struct i2c_adapter * adap)
- Line: 328

### davinci_i2c_init_driver
- Return type: static int __init
- Signature: davinci_i2c_init_driver(void)
- Line: 901

### davinci_i2c_prepare_recovery
- Return type: static void
- Signature: davinci_i2c_prepare_recovery(struct i2c_adapter * adap)
- Line: 288

### davinci_i2c_probe
- Return type: static int
- Signature: davinci_i2c_probe(struct platform_device * pdev)
- Line: 740

### davinci_i2c_read_reg
- Return type: static u16
- Signature: davinci_i2c_read_reg(struct davinci_i2c_dev * i2c_dev,int reg)
- Line: 149

### davinci_i2c_remove
- Return type: static void
- Signature: davinci_i2c_remove(struct platform_device * pdev)
- Line: 836

### davinci_i2c_reset_ctrl
- Return type: static void
- Signature: davinci_i2c_reset_ctrl(struct davinci_i2c_dev * i2c_dev,int val)
- Line: 154

### davinci_i2c_resume
- Return type: static int
- Signature: davinci_i2c_resume(struct device * dev)
- Line: 866

### davinci_i2c_scl_prepare_recovery
- Return type: static void
- Signature: davinci_i2c_scl_prepare_recovery(struct i2c_adapter * adap)
- Line: 338

### davinci_i2c_scl_unprepare_recovery
- Return type: static void
- Signature: davinci_i2c_scl_unprepare_recovery(struct i2c_adapter * adap)
- Line: 352

### davinci_i2c_set_scl
- Return type: static void
- Signature: davinci_i2c_set_scl(struct i2c_adapter * adap,int val)
- Line: 306

### davinci_i2c_suspend
- Return type: static int
- Signature: davinci_i2c_suspend(struct device * dev)
- Line: 856

### davinci_i2c_unprepare_recovery
- Return type: static void
- Signature: davinci_i2c_unprepare_recovery(struct i2c_adapter * adap)
- Line: 299

### davinci_i2c_write_reg
- Return type: static void
- Signature: davinci_i2c_write_reg(struct davinci_i2c_dev * i2c_dev,int reg,u16 val)
- Line: 143

### i2c_davinci_calc_clk_dividers
- Return type: static void
- Signature: i2c_davinci_calc_clk_dividers(struct davinci_i2c_dev * dev)
- Line: 168

### i2c_davinci_cpufreq_deregister
- Return type: static void
- Signature: i2c_davinci_cpufreq_deregister(struct davinci_i2c_dev * dev)
- Line: 712

### i2c_davinci_cpufreq_deregister
- Return type: static void
- Signature: i2c_davinci_cpufreq_deregister(struct davinci_i2c_dev * dev)
- Line: 723

### i2c_davinci_cpufreq_register
- Return type: static int
- Signature: i2c_davinci_cpufreq_register(struct davinci_i2c_dev * dev)
- Line: 704

### i2c_davinci_cpufreq_register
- Return type: static int
- Signature: i2c_davinci_cpufreq_register(struct davinci_i2c_dev * dev)
- Line: 718

### i2c_davinci_cpufreq_transition
- Return type: static int
- Signature: i2c_davinci_cpufreq_transition(struct notifier_block * nb,unsigned long val,void * data)
- Line: 685

### i2c_davinci_func
- Return type: static u32
- Signature: i2c_davinci_func(struct i2c_adapter * adap)
- Line: 551

### i2c_davinci_init
- Return type: static int
- Signature: i2c_davinci_init(struct davinci_i2c_dev * dev)
- Line: 253

### i2c_davinci_isr
- Return type: static irqreturn_t
- Signature: i2c_davinci_isr(int this_irq,void * dev_id)
- Line: 582

### i2c_davinci_wait_bus_not_busy
- Return type: static int
- Signature: i2c_davinci_wait_bus_not_busy(struct davinci_i2c_dev * dev)
- Line: 374

### i2c_davinci_xfer
- Return type: static int
- Signature: i2c_davinci_xfer(struct i2c_adapter * adap,struct i2c_msg msgs[],int num)
- Line: 515

### i2c_davinci_xfer_msg
- Return type: static int
- Signature: i2c_davinci_xfer_msg(struct i2c_adapter * adap,struct i2c_msg * msg,int stop)
- Line: 402

### terminate_read
- Return type: static void
- Signature: terminate_read(struct davinci_i2c_dev * dev)
- Line: 557

### terminate_write
- Return type: static void
- Signature: terminate_write(struct davinci_i2c_dev * dev)
- Line: 568

## Structs (1)

### davinci_i2c_dev
- Line: 122
- Members:
  - dev: device *
  - base: void __iomem *
  - cmd_complete: completion
  - clk: clk *
  - cmd_err: int
  - buf: u8 *
  - buf_len: size_t
  - irq: int
  - stop: int
  - terminate: u8
  - adapter: i2c_adapter
  - freq_transition: notifier_block
  - bus_freq: unsigned int
  - has_pfunc: bool

## Variables (6)

- static **davinci_i2c_driver** : platform_driver (line 889)
- static **davinci_i2c_driver_ids** : const struct platform_device_id[] (line 883)
- static **davinci_i2c_of_match** : const struct of_device_id[] (line 733)
- static **davinci_i2c_pm** : const struct dev_pm_ops (line 876)
- static **davinci_i2c_scl_recovery_info** : i2c_bus_recovery_info (line 362)
- static **i2c_davinci_algo** : const struct i2c_algorithm (line 728)

## Macros (62)

- **DAVINCI_I2C_CLKH_REG** (line 46)
- **DAVINCI_I2C_CLKL_REG** (line 45)
- **DAVINCI_I2C_CNT_REG** (line 47)
- **DAVINCI_I2C_DCLR_PDCLR0** (line 113)
- **DAVINCI_I2C_DCLR_PDCLR1** (line 115)
- **DAVINCI_I2C_DCLR_REG** (line 60)
- **DAVINCI_I2C_DEFAULT_BUS_FREQ** (line 120)
- **DAVINCI_I2C_DIN_PDIN0** (line 103)
- **DAVINCI_I2C_DIN_PDIN1** (line 105)
- **DAVINCI_I2C_DIN_REG** (line 57)
- **DAVINCI_I2C_DIR_PDIR0** (line 98)
- **DAVINCI_I2C_DIR_PDIR1** (line 100)
- **DAVINCI_I2C_DIR_REG** (line 56)
- **DAVINCI_I2C_DOUT_REG** (line 58)
- **DAVINCI_I2C_DRR_REG** (line 48)
- **DAVINCI_I2C_DSET_PDSET0** (line 108)
- **DAVINCI_I2C_DSET_PDSET1** (line 110)
- **DAVINCI_I2C_DSET_REG** (line 59)
- **DAVINCI_I2C_DXR_REG** (line 50)
- **DAVINCI_I2C_EMDR_REG** (line 53)
- **DAVINCI_I2C_FUNC_PFUNC0** (line 95)
- **DAVINCI_I2C_FUNC_REG** (line 55)
- **DAVINCI_I2C_IMR_AAS** (line 86)
- **DAVINCI_I2C_IMR_AL** (line 92)
- **DAVINCI_I2C_IMR_ARDY** (line 90)
- **DAVINCI_I2C_IMR_NACK** (line 91)
- **DAVINCI_I2C_IMR_REG** (line 43)
- **DAVINCI_I2C_IMR_RRDY** (line 89)
- **DAVINCI_I2C_IMR_SCD** (line 87)
- **DAVINCI_I2C_IMR_XRDY** (line 88)
- **DAVINCI_I2C_IVR_AAS** (line 62)
- **DAVINCI_I2C_IVR_AL** (line 68)
- **DAVINCI_I2C_IVR_ARDY** (line 66)
- **DAVINCI_I2C_IVR_NACK** (line 67)
- **DAVINCI_I2C_IVR_RDR** (line 65)
- **DAVINCI_I2C_IVR_REG** (line 52)
- **DAVINCI_I2C_IVR_SCD** (line 63)
- **DAVINCI_I2C_IVR_XRDY** (line 64)
- **DAVINCI_I2C_MAX_TRIES** (line 35)
- **DAVINCI_I2C_MDR_IRS** (line 84)
- **DAVINCI_I2C_MDR_MST** (line 80)
- **DAVINCI_I2C_MDR_NACK** (line 77)
- **DAVINCI_I2C_MDR_REG** (line 51)
- **DAVINCI_I2C_MDR_RM** (line 83)
- **DAVINCI_I2C_MDR_STP** (line 79)
- **DAVINCI_I2C_MDR_STT** (line 78)
- **DAVINCI_I2C_MDR_TRX** (line 81)
- **DAVINCI_I2C_MDR_XA** (line 82)
- **DAVINCI_I2C_OAR_REG** (line 42)
- **DAVINCI_I2C_OWN_ADDRESS** (line 36)
- **DAVINCI_I2C_PM_TIMEOUT** (line 118)
- **DAVINCI_I2C_PSC_REG** (line 54)
- **DAVINCI_I2C_SAR_REG** (line 49)
- **DAVINCI_I2C_STR_AL** (line 75)
- **DAVINCI_I2C_STR_ARDY** (line 73)
- **DAVINCI_I2C_STR_BB** (line 70)
- **DAVINCI_I2C_STR_NACK** (line 74)
- **DAVINCI_I2C_STR_REG** (line 44)
- **DAVINCI_I2C_STR_RSFULL** (line 71)
- **DAVINCI_I2C_STR_SCD** (line 72)
- **DAVINCI_I2C_TIMEOUT** (line 34)
- **I2C_DAVINCI_INTR_ALL** (line 37)
