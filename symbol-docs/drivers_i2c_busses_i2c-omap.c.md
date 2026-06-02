# drivers/i2c/busses/i2c-omap.c

Subsystem: drivers/i2c

## Functions (37)

### __omap_i2c_init
- Return type: static void
- Signature: __omap_i2c_init(struct omap_i2c_dev * omap)
- Line: 280

### errata_omap3_i462
- Return type: static int
- Signature: errata_omap3_i462(struct omap_i2c_dev * omap)
- Line: 961

### i2c_omap_errata_i207
- Return type: static void
- Signature: i2c_omap_errata_i207(struct omap_i2c_dev * omap,u16 stat)
- Line: 867

### omap_i2c_ack_stat
- Return type: static void
- Signature: omap_i2c_ack_stat(struct omap_i2c_dev * omap,u16 stat)
- Line: 862

### omap_i2c_complete_cmd
- Return type: static void
- Signature: omap_i2c_complete_cmd(struct omap_i2c_dev * omap,u16 err)
- Line: 855

### omap_i2c_exit_driver
- Return type: static void __exit
- Signature: omap_i2c_exit_driver(void)
- Line: 1623

### omap_i2c_func
- Return type: static u32
- Signature: omap_i2c_func(struct i2c_adapter * adap)
- Line: 848

### omap_i2c_get_scl
- Return type: static int
- Signature: omap_i2c_get_scl(struct i2c_adapter * adap)
- Line: 1268

### omap_i2c_get_sda
- Return type: static int
- Signature: omap_i2c_get_sda(struct i2c_adapter * adap)
- Line: 1278

### omap_i2c_init
- Return type: static int
- Signature: omap_i2c_init(struct omap_i2c_dev * omap)
- Line: 351

### omap_i2c_init_driver
- Return type: static int __init
- Signature: omap_i2c_init_driver(void)
- Line: 1617

### omap_i2c_isr_thread
- Return type: static irqreturn_t
- Signature: omap_i2c_isr_thread(int this_irq,void * dev_id)
- Line: 1190

### omap_i2c_omap1_isr
- Return type: static irqreturn_t
- Signature: omap_i2c_omap1_isr(int this_irq,void * dev_id)
- Line: 899

### omap_i2c_prepare_recovery
- Return type: static void
- Signature: omap_i2c_prepare_recovery(struct i2c_adapter * adap)
- Line: 1301

### omap_i2c_probe
- Return type: static int
- Signature: omap_i2c_probe(struct platform_device * pdev)
- Line: 1342

### omap_i2c_read_reg
- Return type: static u16
- Signature: omap_i2c_read_reg(struct omap_i2c_dev * omap,int reg)
- Line: 274

### omap_i2c_receive_data
- Return type: static void
- Signature: omap_i2c_receive_data(struct omap_i2c_dev * omap,u8 num_bytes,bool is_rdr)
- Line: 999

### omap_i2c_recover_bus
- Return type: static int
- Signature: omap_i2c_recover_bus(struct omap_i2c_dev * omap)
- Line: 487

### omap_i2c_remove
- Return type: static void
- Signature: omap_i2c_remove(struct platform_device * pdev)
- Line: 1516

### omap_i2c_reset
- Return type: static int
- Signature: omap_i2c_reset(struct omap_i2c_dev * omap)
- Line: 311

### omap_i2c_resize_fifo
- Return type: static void
- Signature: omap_i2c_resize_fifo(struct omap_i2c_dev * omap,u8 size,bool is_rx)
- Line: 607

### omap_i2c_resume
- Return type: static int
- Signature: omap_i2c_resume(struct device * dev)
- Line: 1590

### omap_i2c_runtime_resume
- Return type: static int
- Signature: omap_i2c_runtime_resume(struct device * dev)
- Line: 1563

### omap_i2c_runtime_suspend
- Return type: static int
- Signature: omap_i2c_runtime_suspend(struct device * dev)
- Line: 1537

### omap_i2c_set_scl
- Return type: static void
- Signature: omap_i2c_set_scl(struct i2c_adapter * adap,int val)
- Line: 1288

### omap_i2c_suspend
- Return type: static int
- Signature: omap_i2c_suspend(struct device * dev)
- Line: 1577

### omap_i2c_transmit_data
- Return type: static int
- Signature: omap_i2c_transmit_data(struct omap_i2c_dev * omap,u8 num_bytes,bool is_xdr)
- Line: 1020

### omap_i2c_unprepare_recovery
- Return type: static void
- Signature: omap_i2c_unprepare_recovery(struct i2c_adapter * adap)
- Line: 1318

### omap_i2c_wait
- Return type: static void
- Signature: omap_i2c_wait(struct omap_i2c_dev * omap)
- Line: 646

### omap_i2c_wait_for_bb
- Return type: static int
- Signature: omap_i2c_wait_for_bb(struct omap_i2c_dev * omap)
- Line: 503

### omap_i2c_wait_for_bb_valid
- Return type: static int
- Signature: omap_i2c_wait_for_bb_valid(struct omap_i2c_dev * omap)
- Line: 545

### omap_i2c_write_reg
- Return type: static void
- Signature: omap_i2c_write_reg(struct omap_i2c_dev * omap,int reg,u16 val)
- Line: 267

### omap_i2c_xfer_common
- Return type: static int
- Signature: omap_i2c_xfer_common(struct i2c_adapter * adap,struct i2c_msg msgs[],int num,bool polling)
- Line: 793

### omap_i2c_xfer_data
- Return type: static int
- Signature: omap_i2c_xfer_data(struct omap_i2c_dev * omap)
- Line: 1052

### omap_i2c_xfer_irq
- Return type: static int
- Signature: omap_i2c_xfer_irq(struct i2c_adapter * adap,struct i2c_msg msgs[],int num)
- Line: 836

### omap_i2c_xfer_msg
- Return type: static int
- Signature: omap_i2c_xfer_msg(struct i2c_adapter * adap,struct i2c_msg * msg,int stop,bool polling)
- Line: 661

### omap_i2c_xfer_polling
- Return type: static int
- Signature: omap_i2c_xfer_polling(struct i2c_adapter * adap,struct i2c_msg msgs[],int num)
- Line: 842

## Structs (1)

### omap_i2c_dev
- Line: 179
- Members:
  - dev: device *
  - base: void __iomem *
  - irq: int
  - reg_shift: int
  - cmd_complete: completion
  - ioarea: resource *
  - latency: u32
  - set_mpu_wkup_lat: void (*)(struct device * dev,long latency)
  - speed: u32
  - flags: u32
  - scheme: u16
  - cmd_err: u16
  - buf: u8 *
  - regs: u8 *
  - buf_len: size_t
  - adapter: i2c_adapter
  - threshold: u8
  - fifo_size: u8
  - rev: u32
  - b_hw: unsigned:1
  - bb_valid: unsigned:1
  - receiver: unsigned:1
  - iestate: u16
  - pscstate: u16
  - scllstate: u16
  - sclhstate: u16
  - syscstate: u16
  - westate: u16
  - errata: u16
  - mux_state: mux_state *

## Enums (1)

### __anonad35a8970103
- Line: 54

## Variables (12)

- static **omap2420_pdata** : omap_i2c_bus_platform_data (line 1213)
- static **omap2430_pdata** : omap_i2c_bus_platform_data (line 1221)
- static **omap3_pdata** : omap_i2c_bus_platform_data (line 1227)
- static **omap4_pdata** : omap_i2c_bus_platform_data (line 1232)
- static **omap_i2c_algo** : const struct i2c_algorithm (line 1202)
- static **omap_i2c_bus_recovery_info** : i2c_bus_recovery_info (line 1332)
- static **omap_i2c_driver** : platform_driver (line 1605)
- static **omap_i2c_of_match** : const struct of_device_id[] (line 1236)
- static **omap_i2c_pm_ops** : const struct dev_pm_ops (line 1597)
- static **omap_i2c_quirks** : const struct i2c_adapter_quirks (line 1208)
- static **reg_map_ip_v1** : const u8[] (line 218)
- static **reg_map_ip_v2** : const u8[] (line 239)

## Macros (85)

- **I2C_OMAP_ERRATA_I207** (line 174)
- **I2C_OMAP_ERRATA_I462** (line 175)
- **OMAP_I2C_BUF_RDMA_EN** (line 123)
- **OMAP_I2C_BUF_RXFIF_CLR** (line 124)
- **OMAP_I2C_BUF_TXFIF_CLR** (line 126)
- **OMAP_I2C_BUF_XDMA_EN** (line 125)
- **OMAP_I2C_BUS_FREE_TIMEOUT** (line 51)
- **OMAP_I2C_CON_BE** (line 130)
- **OMAP_I2C_CON_EN** (line 129)
- **OMAP_I2C_CON_MST** (line 133)
- **OMAP_I2C_CON_OPMODE_HS** (line 131)
- **OMAP_I2C_CON_RM** (line 136)
- **OMAP_I2C_CON_STB** (line 132)
- **OMAP_I2C_CON_STP** (line 137)
- **OMAP_I2C_CON_STT** (line 138)
- **OMAP_I2C_CON_TRX** (line 134)
- **OMAP_I2C_CON_XA** (line 135)
- **OMAP_I2C_IE_AL** (line 88)
- **OMAP_I2C_IE_ARDY** (line 86)
- **OMAP_I2C_IE_NACK** (line 87)
- **OMAP_I2C_IE_RDR** (line 83)
- **OMAP_I2C_IE_RRDY** (line 85)
- **OMAP_I2C_IE_XDR** (line 82)
- **OMAP_I2C_IE_XRDY** (line 84)
- **OMAP_I2C_IP_V2_INTERRUPTS_MASK** (line 177)
- **OMAP_I2C_OMAP1_REV_2** (line 36)
- **OMAP_I2C_PM_TIMEOUT** (line 48)
- **OMAP_I2C_REV_ON_2430** (line 39)
- **OMAP_I2C_REV_ON_3430_3530** (line 40)
- **OMAP_I2C_REV_ON_3630** (line 41)
- **OMAP_I2C_REV_ON_4430_PLUS** (line 42)
- **OMAP_I2C_REV_SCHEME_0_MAJOR**(rev) (line 1260)
- **OMAP_I2C_REV_SCHEME_0_MINOR**(rev) (line 1261)
- **OMAP_I2C_REV_SCHEME_1_MAJOR**(rev) (line 1263)
- **OMAP_I2C_REV_SCHEME_1_MINOR**(rev) (line 1264)
- **OMAP_I2C_SCHEME**(rev) (line 1258)
- **OMAP_I2C_SCHEME_0** (line 1265)
- **OMAP_I2C_SCHEME_1** (line 1266)
- **OMAP_I2C_SCLH_HSSCLH** (line 142)
- **OMAP_I2C_SCLL_HSSCLL** (line 141)
- **OMAP_I2C_STAT_AAS** (line 96)
- **OMAP_I2C_STAT_AL** (line 102)
- **OMAP_I2C_STAT_ARDY** (line 100)
- **OMAP_I2C_STAT_BB** (line 93)
- **OMAP_I2C_STAT_BF** (line 97)
- **OMAP_I2C_STAT_NACK** (line 101)
- **OMAP_I2C_STAT_RDR** (line 92)
- **OMAP_I2C_STAT_ROVR** (line 94)
- **OMAP_I2C_STAT_RRDY** (line 99)
- **OMAP_I2C_STAT_XDR** (line 91)
- **OMAP_I2C_STAT_XRDY** (line 98)
- **OMAP_I2C_STAT_XUDF** (line 95)
- **OMAP_I2C_SYSTEST_FREE** (line 146)
- **OMAP_I2C_SYSTEST_SCL_I** (line 155)
- **OMAP_I2C_SYSTEST_SCL_I_FUNC** (line 150)
- **OMAP_I2C_SYSTEST_SCL_O** (line 156)
- **OMAP_I2C_SYSTEST_SCL_O_FUNC** (line 151)
- **OMAP_I2C_SYSTEST_SDA_I** (line 157)
- **OMAP_I2C_SYSTEST_SDA_I_FUNC** (line 152)
- **OMAP_I2C_SYSTEST_SDA_O** (line 158)
- **OMAP_I2C_SYSTEST_SDA_O_FUNC** (line 153)
- **OMAP_I2C_SYSTEST_ST_EN** (line 145)
- **OMAP_I2C_SYSTEST_TMODE_MASK** (line 147)
- **OMAP_I2C_SYSTEST_TMODE_SHIFT** (line 148)
- **OMAP_I2C_TIMEOUT** (line 45)
- **OMAP_I2C_WE_AAS_WE** (line 107)
- **OMAP_I2C_WE_ALL** (line 116)
- **OMAP_I2C_WE_AL_WE** (line 114)
- **OMAP_I2C_WE_ARDY_WE** (line 112)
- **OMAP_I2C_WE_BF_WE** (line 108)
- **OMAP_I2C_WE_DRDY_WE** (line 111)
- **OMAP_I2C_WE_GC_WE** (line 110)
- **OMAP_I2C_WE_NACK_WE** (line 113)
- **OMAP_I2C_WE_RDR_WE** (line 106)
- **OMAP_I2C_WE_STC_WE** (line 109)
- **OMAP_I2C_WE_XDR_WE** (line 105)
- **SYSC_AUTOIDLE_MASK** (line 168)
- **SYSC_CLOCKACTIVITY_FCLK** (line 171)
- **SYSC_CLOCKACTIVITY_MASK** (line 164)
- **SYSC_ENAWAKEUP_MASK** (line 166)
- **SYSC_IDLEMODE_SMART** (line 170)
- **SYSC_SIDLEMODE_MASK** (line 165)
- **SYSC_SOFTRESET_MASK** (line 167)
- **SYSS_RESETDONE_MASK** (line 161)
- **omap_i2c_omap1_isr** (line 953)
