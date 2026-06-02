# drivers/i2c/busses/i2c-s3c2410.c

Subsystem: drivers/i2c

## Functions (34)

### i2c_adap_s3c_exit
- Return type: static void __exit
- Signature: i2c_adap_s3c_exit(void)
- Line: 1198

### i2c_adap_s3c_init
- Return type: static int __init
- Signature: i2c_adap_s3c_init(void)
- Line: 1192

### i2c_s3c_irq_nextbyte
- Return type: static void
- Signature: i2c_s3c_irq_nextbyte(struct s3c24xx_i2c * i2c,unsigned long iicstat)
- Line: 379

### is_ack
- Return type: static bool
- Signature: is_ack(struct s3c24xx_i2c * i2c)
- Line: 214

### is_lastmsg
- Return type: static int
- Signature: is_lastmsg(struct s3c24xx_i2c * i2c)
- Line: 347

### is_msgend
- Return type: static int
- Signature: is_msgend(struct s3c24xx_i2c * i2c)
- Line: 371

### is_msglast
- Return type: static int
- Signature: is_msglast(struct s3c24xx_i2c * i2c)
- Line: 355

### s3c24xx_get_device_quirks
- Return type: static kernel_ulong_t
- Signature: s3c24xx_get_device_quirks(struct platform_device * pdev)
- Line: 154

### s3c24xx_i2c_calcdivisor
- Return type: static int
- Signature: s3c24xx_i2c_calcdivisor(unsigned long clkin,unsigned int wanted,unsigned int * div1,unsigned int * divs)
- Line: 815

### s3c24xx_i2c_clockrate
- Return type: static int
- Signature: s3c24xx_i2c_clockrate(struct s3c24xx_i2c * i2c,unsigned int * got)
- Line: 845

### s3c24xx_i2c_disable_ack
- Return type: static void
- Signature: s3c24xx_i2c_disable_ack(struct s3c24xx_i2c * i2c)
- Line: 181

### s3c24xx_i2c_disable_bus
- Return type: static void
- Signature: s3c24xx_i2c_disable_bus(struct s3c24xx_i2c * i2c)
- Line: 597

### s3c24xx_i2c_disable_irq
- Return type: static void
- Signature: s3c24xx_i2c_disable_irq(struct s3c24xx_i2c * i2c)
- Line: 198

### s3c24xx_i2c_doxfer
- Return type: static int
- Signature: s3c24xx_i2c_doxfer(struct s3c24xx_i2c * i2c,struct i2c_msg * msgs,int num)
- Line: 689

### s3c24xx_i2c_enable_ack
- Return type: static void
- Signature: s3c24xx_i2c_enable_ack(struct s3c24xx_i2c * i2c)
- Line: 189

### s3c24xx_i2c_enable_irq
- Return type: static void
- Signature: s3c24xx_i2c_enable_irq(struct s3c24xx_i2c * i2c)
- Line: 206

### s3c24xx_i2c_func
- Return type: static u32
- Signature: s3c24xx_i2c_func(struct i2c_adapter * adap)
- Line: 799

### s3c24xx_i2c_init
- Return type: static int
- Signature: s3c24xx_i2c_init(struct s3c24xx_i2c * i2c)
- Line: 935

### s3c24xx_i2c_irq
- Return type: static irqreturn_t
- Signature: s3c24xx_i2c_irq(int irqno,void * dev_id)
- Line: 556

### s3c24xx_i2c_master_complete
- Return type: static void
- Signature: s3c24xx_i2c_master_complete(struct s3c24xx_i2c * i2c,int ret)
- Line: 166

### s3c24xx_i2c_message_start
- Return type: static void
- Signature: s3c24xx_i2c_message_start(struct s3c24xx_i2c * i2c,struct i2c_msg * msg)
- Line: 243

### s3c24xx_i2c_parse_dt
- Return type: static void
- Signature: s3c24xx_i2c_parse_dt(struct device_node * np,struct s3c24xx_i2c * i2c)
- Line: 1005

### s3c24xx_i2c_parse_dt
- Return type: static void
- Signature: s3c24xx_i2c_parse_dt(struct device_node * np,struct s3c24xx_i2c * i2c)
- Line: 974

### s3c24xx_i2c_parse_dt_gpio
- Return type: static int
- Signature: s3c24xx_i2c_parse_dt_gpio(struct s3c24xx_i2c * i2c)
- Line: 907

### s3c24xx_i2c_parse_dt_gpio
- Return type: static int
- Signature: s3c24xx_i2c_parse_dt_gpio(struct s3c24xx_i2c * i2c)
- Line: 926

### s3c24xx_i2c_probe
- Return type: static int
- Signature: s3c24xx_i2c_probe(struct platform_device * pdev)
- Line: 1008

### s3c24xx_i2c_remove
- Return type: static void
- Signature: s3c24xx_i2c_remove(struct platform_device * pdev)
- Line: 1135

### s3c24xx_i2c_resume_noirq
- Return type: static int
- Signature: s3c24xx_i2c_resume_noirq(struct device * dev)
- Line: 1158

### s3c24xx_i2c_set_master
- Return type: static int
- Signature: s3c24xx_i2c_set_master(struct s3c24xx_i2c * i2c)
- Line: 617

### s3c24xx_i2c_stop
- Return type: static void
- Signature: s3c24xx_i2c_stop(struct s3c24xx_i2c * i2c,int ret)
- Line: 284

### s3c24xx_i2c_suspend_noirq
- Return type: static int
- Signature: s3c24xx_i2c_suspend_noirq(struct device * dev)
- Line: 1146

### s3c24xx_i2c_wait_idle
- Return type: static void
- Signature: s3c24xx_i2c_wait_idle(struct s3c24xx_i2c * i2c)
- Line: 637

### s3c24xx_i2c_xfer
- Return type: static int
- Signature: s3c24xx_i2c_xfer(struct i2c_adapter * adap,struct i2c_msg * msgs,int num)
- Line: 754

### s3c24xx_i2c_xfer_atomic
- Return type: static int
- Signature: s3c24xx_i2c_xfer_atomic(struct i2c_adapter * adap,struct i2c_msg * msgs,int num)
- Line: 783

## Structs (1)

### s3c24xx_i2c
- Line: 96
- Members:
  - wait: wait_queue_head_t
  - quirks: kernel_ulong_t
  - msg: i2c_msg *
  - msg_num: unsigned int
  - msg_idx: unsigned int
  - msg_ptr: unsigned int
  - tx_setup: unsigned int
  - irq: unsigned int
  - state: s3c24xx_i2c_state
  - clkrate: unsigned long
  - regs: void __iomem *
  - clk: clk *
  - dev: device *
  - adap: i2c_adapter
  - pdata: s3c2410_platform_i2c *
  - gpios: gpio_desc * [2]
  - pctrl: pinctrl *
  - sysreg: regmap *
  - sys_i2c_cfg: unsigned int

## Enums (1)

### s3c24xx_i2c_state
- Line: 88

## Variables (5)

- static **s3c24xx_driver_ids** : const struct platform_device_id[] (line 123)
- static **s3c24xx_i2c_algorithm** : const struct i2c_algorithm (line 806)
- static **s3c24xx_i2c_dev_pm_ops** : const struct dev_pm_ops (line 1176)
- static **s3c24xx_i2c_driver** : platform_driver (line 1181)
- static **s3c24xx_i2c_match** : const struct of_device_id[] (line 140)

## Macros (37)

- **EXYNOS5_SYS_I2C_CFG** (line 85)
- **QUIRK_ATOMIC** (line 79)
- **QUIRK_HDMIPHY** (line 76)
- **QUIRK_NO_GPIO** (line 77)
- **QUIRK_POLL** (line 78)
- **QUIRK_S3C2440** (line 75)
- **S3C2410_IDLE_TIMEOUT** (line 82)
- **S3C2410_IICADD** (line 40)
- **S3C2410_IICCON** (line 38)
- **S3C2410_IICCON_ACKEN** (line 44)
- **S3C2410_IICCON_IRQEN** (line 47)
- **S3C2410_IICCON_IRQPEND** (line 48)
- **S3C2410_IICCON_SCALE**(x) (line 49)
- **S3C2410_IICCON_SCALEMASK** (line 50)
- **S3C2410_IICCON_TXDIV_16** (line 45)
- **S3C2410_IICCON_TXDIV_512** (line 46)
- **S3C2410_IICDS** (line 41)
- **S3C2410_IICLC_FILTER_ON** (line 72)
- **S3C2410_IICLC_SDA_DELAY0** (line 66)
- **S3C2410_IICLC_SDA_DELAY10** (line 68)
- **S3C2410_IICLC_SDA_DELAY15** (line 69)
- **S3C2410_IICLC_SDA_DELAY5** (line 67)
- **S3C2410_IICLC_SDA_DELAY_MASK** (line 70)
- **S3C2410_IICSTAT** (line 39)
- **S3C2410_IICSTAT_ADDR0** (line 63)
- **S3C2410_IICSTAT_ARBITR** (line 61)
- **S3C2410_IICSTAT_ASSLAVE** (line 62)
- **S3C2410_IICSTAT_BUSBUSY** (line 59)
- **S3C2410_IICSTAT_LASTBIT** (line 64)
- **S3C2410_IICSTAT_MASTER_RX** (line 52)
- **S3C2410_IICSTAT_MASTER_TX** (line 53)
- **S3C2410_IICSTAT_MODEMASK** (line 56)
- **S3C2410_IICSTAT_SLAVE_RX** (line 54)
- **S3C2410_IICSTAT_SLAVE_TX** (line 55)
- **S3C2410_IICSTAT_START** (line 58)
- **S3C2410_IICSTAT_TXRXEN** (line 60)
- **S3C2440_IICLC** (line 42)
