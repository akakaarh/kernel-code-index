# drivers/i2c/busses/i2c-rk3x.c

Subsystem: drivers/i2c

## Functions (26)

### i2c_readl
- Return type: static u32
- Signature: i2c_readl(struct rk3x_i2c * i2c,unsigned int offset)
- Line: 233

### i2c_writel
- Return type: static void
- Signature: i2c_writel(struct rk3x_i2c * i2c,u32 value,unsigned int offset)
- Line: 227

### rk3x_i2c_adapt_div
- Return type: static void
- Signature: rk3x_i2c_adapt_div(struct rk3x_i2c * i2c,unsigned long clk_rate)
- Line: 875

### rk3x_i2c_clean_ipd
- Return type: static void
- Signature: rk3x_i2c_clean_ipd(struct rk3x_i2c * i2c)
- Line: 239

### rk3x_i2c_clk_notifier_cb
- Return type: static int
- Signature: rk3x_i2c_clk_notifier_cb(struct notifier_block * nb,unsigned long event,void * data)
- Line: 926

### rk3x_i2c_fill_transmit_buf
- Return type: static void
- Signature: rk3x_i2c_fill_transmit_buf(struct rk3x_i2c * i2c)
- Line: 340

### rk3x_i2c_func
- Return type: static u32
- Signature: rk3x_i2c_func(struct i2c_adapter * adap)
- Line: 1157

### rk3x_i2c_get_spec
- Return type: static const struct i2c_spec_values *
- Signature: rk3x_i2c_get_spec(unsigned int speed)
- Line: 546

### rk3x_i2c_handle_read
- Return type: static void
- Signature: rk3x_i2c_handle_read(struct rk3x_i2c * i2c,unsigned int ipd)
- Line: 421

### rk3x_i2c_handle_start
- Return type: static void
- Signature: rk3x_i2c_handle_start(struct rk3x_i2c * i2c,unsigned int ipd)
- Line: 374

### rk3x_i2c_handle_stop
- Return type: static void
- Signature: rk3x_i2c_handle_stop(struct rk3x_i2c * i2c,unsigned int ipd)
- Line: 455

### rk3x_i2c_handle_write
- Return type: static void
- Signature: rk3x_i2c_handle_write(struct rk3x_i2c * i2c,unsigned int ipd)
- Line: 402

### rk3x_i2c_irq
- Return type: static irqreturn_t
- Signature: rk3x_i2c_irq(int irqno,void * dev_id)
- Line: 481

### rk3x_i2c_prepare_read
- Return type: static void
- Signature: rk3x_i2c_prepare_read(struct rk3x_i2c * i2c)
- Line: 308

### rk3x_i2c_probe
- Return type: static int
- Signature: rk3x_i2c_probe(struct platform_device * pdev)
- Line: 1236

### rk3x_i2c_remove
- Return type: static void
- Signature: rk3x_i2c_remove(struct platform_device * pdev)
- Line: 1386

### rk3x_i2c_resume
- Return type: static __maybe_unused int
- Signature: rk3x_i2c_resume(struct device * dev)
- Line: 1148

### rk3x_i2c_setup
- Return type: static int
- Signature: rk3x_i2c_setup(struct rk3x_i2c * i2c,struct i2c_msg * msgs,int num)
- Line: 974

### rk3x_i2c_start
- Return type: static void
- Signature: rk3x_i2c_start(struct rk3x_i2c * i2c)
- Line: 248

### rk3x_i2c_stop
- Return type: static void
- Signature: rk3x_i2c_stop(struct rk3x_i2c * i2c,int error)
- Line: 269

### rk3x_i2c_v0_calc_timings
- Return type: static int
- Signature: rk3x_i2c_v0_calc_timings(unsigned long clk_rate,struct i2c_timings * t,struct rk3x_i2c_calced_timings * t_calc)
- Line: 566

### rk3x_i2c_v1_calc_timings
- Return type: static int
- Signature: rk3x_i2c_v1_calc_timings(unsigned long clk_rate,struct i2c_timings * t,struct rk3x_i2c_calced_timings * t_calc)
- Line: 745

### rk3x_i2c_wait_xfer_poll
- Return type: static int
- Signature: rk3x_i2c_wait_xfer_poll(struct rk3x_i2c * i2c)
- Line: 1046

### rk3x_i2c_xfer
- Return type: static int
- Signature: rk3x_i2c_xfer(struct i2c_adapter * adap,struct i2c_msg * msgs,int num)
- Line: 1136

### rk3x_i2c_xfer_common
- Return type: static int
- Signature: rk3x_i2c_xfer_common(struct i2c_adapter * adap,struct i2c_msg * msgs,int num,bool polling)
- Line: 1059

### rk3x_i2c_xfer_polling
- Return type: static int
- Signature: rk3x_i2c_xfer_polling(struct i2c_adapter * adap,struct i2c_msg * msgs,int num)
- Line: 1142

## Structs (4)

### i2c_spec_values
- Line: 95
- Members:
  - min_hold_start_ns: unsigned long
  - min_low_ns: unsigned long
  - min_high_ns: unsigned long
  - min_setup_start_ns: unsigned long
  - max_data_hold_ns: unsigned long
  - min_data_setup_ns: unsigned long
  - min_setup_stop_ns: unsigned long
  - min_hold_buffer_ns: unsigned long
  - div_low: unsigned long
  - div_high: unsigned long
  - tuning: unsigned int
  - grf_offset: int
  - calc_timings: int (*)(unsigned long,struct i2c_timings *,struct rk3x_i2c_calced_timings *)
  - adap: i2c_adapter
  - dev: device *
  - soc_data: const struct rk3x_i2c_soc_data *
  - regs: void __iomem *
  - clk: clk *
  - pclk: clk *
  - clk_rate_nb: notifier_block
  - irq: int
  - t: i2c_timings
  - lock: spinlock_t
  - wait: wait_queue_head_t
  - busy: bool
  - msg: i2c_msg *
  - addr: u8
  - mode: unsigned int
  - is_last_msg: bool
  - state: rk3x_i2c_state
  - processed: unsigned int
  - error: int
  - quirks: const struct i2c_adapter_quirks *
  - regs: const u16 *
  - pmic_i2c: unsigned char:1
  - dcm: unsigned char:1
  - auto_restart: unsigned char:1
  - aux_len_reg: unsigned char:1
  - timing_adjust: unsigned char:1
  - dma_sync: unsigned char:1
  - ltiming_adjust: unsigned char:1
  - apdma_sync: unsigned char:1
  - max_dma_support: unsigned char
  - htiming: u16
  - ltiming: u16
  - hs: u16
  - ext: u16
  - inter_clk_div: u16
  - scl_hl_ratio: u16
  - hs_scl_hl_ratio: u16
  - sta_stop: u16
  - hs_sta_stop: u16
  - sda_timing: u16
  - adap: i2c_adapter
  - dev: device *
  - msg_complete: completion
  - timing_info: i2c_timings
  - base: void __iomem *
  - pdmabase: void __iomem *
  - clocks: clk_bulk_data[]
  - have_pmic: bool
  - use_push_pull: bool
  - irq_stat: u16
  - clk_src_div: unsigned int
  - speed_hz: unsigned int
  - op: mtk_trans_op
  - timing_reg: u16
  - high_speed_reg: u16
  - ltiming_reg: u16
  - auto_restart: unsigned char
  - ignore_restart_irq: bool
  - ac_timing: mtk_i2c_ac_timing
  - dev_comp: const struct mtk_i2c_compatible *
  - min_low_ns: unsigned int
  - min_su_sta_ns: unsigned int
  - max_hd_dat_ns: unsigned int
  - min_su_dat_ns: unsigned int

### rk3x_i2c
- Line: 195
- Members:
  - min_hold_start_ns: unsigned long
  - min_low_ns: unsigned long
  - min_high_ns: unsigned long
  - min_setup_start_ns: unsigned long
  - max_data_hold_ns: unsigned long
  - min_data_setup_ns: unsigned long
  - min_setup_stop_ns: unsigned long
  - min_hold_buffer_ns: unsigned long
  - div_low: unsigned long
  - div_high: unsigned long
  - tuning: unsigned int
  - grf_offset: int
  - calc_timings: int (*)(unsigned long,struct i2c_timings *,struct rk3x_i2c_calced_timings *)
  - adap: i2c_adapter
  - dev: device *
  - soc_data: const struct rk3x_i2c_soc_data *
  - regs: void __iomem *
  - clk: clk *
  - pclk: clk *
  - clk_rate_nb: notifier_block
  - irq: int
  - t: i2c_timings
  - lock: spinlock_t
  - wait: wait_queue_head_t
  - busy: bool
  - msg: i2c_msg *
  - addr: u8
  - mode: unsigned int
  - is_last_msg: bool
  - state: rk3x_i2c_state
  - processed: unsigned int
  - error: int

### rk3x_i2c_calced_timings
- Line: 148
- Members:
  - min_hold_start_ns: unsigned long
  - min_low_ns: unsigned long
  - min_high_ns: unsigned long
  - min_setup_start_ns: unsigned long
  - max_data_hold_ns: unsigned long
  - min_data_setup_ns: unsigned long
  - min_setup_stop_ns: unsigned long
  - min_hold_buffer_ns: unsigned long
  - div_low: unsigned long
  - div_high: unsigned long
  - tuning: unsigned int
  - grf_offset: int
  - calc_timings: int (*)(unsigned long,struct i2c_timings *,struct rk3x_i2c_calced_timings *)
  - adap: i2c_adapter
  - dev: device *
  - soc_data: const struct rk3x_i2c_soc_data *
  - regs: void __iomem *
  - clk: clk *
  - pclk: clk *
  - clk_rate_nb: notifier_block
  - irq: int
  - t: i2c_timings
  - lock: spinlock_t
  - wait: wait_queue_head_t
  - busy: bool
  - msg: i2c_msg *
  - addr: u8
  - mode: unsigned int
  - is_last_msg: bool
  - state: rk3x_i2c_state
  - processed: unsigned int
  - error: int

### rk3x_i2c_soc_data
- Line: 167
- Members:
  - min_hold_start_ns: unsigned long
  - min_low_ns: unsigned long
  - min_high_ns: unsigned long
  - min_setup_start_ns: unsigned long
  - max_data_hold_ns: unsigned long
  - min_data_setup_ns: unsigned long
  - min_setup_stop_ns: unsigned long
  - min_hold_buffer_ns: unsigned long
  - div_low: unsigned long
  - div_high: unsigned long
  - tuning: unsigned int
  - grf_offset: int
  - calc_timings: int (*)(unsigned long,struct i2c_timings *,struct rk3x_i2c_calced_timings *)
  - adap: i2c_adapter
  - dev: device *
  - soc_data: const struct rk3x_i2c_soc_data *
  - regs: void __iomem *
  - clk: clk *
  - pclk: clk *
  - clk_rate_nb: notifier_block
  - irq: int
  - t: i2c_timings
  - lock: spinlock_t
  - wait: wait_queue_head_t
  - busy: bool
  - msg: i2c_msg *
  - addr: u8
  - mode: unsigned int
  - is_last_msg: bool
  - state: rk3x_i2c_state
  - processed: unsigned int
  - error: int

## Enums (2)

### __anonb3f7da120103
- Line: 46

### rk3x_i2c_state
- Line: 154

## Variables (13)

- static **fast_mode_plus_spec** : const struct i2c_spec_values (line 128)
- static **fast_mode_spec** : const struct i2c_spec_values (line 117)
- static **rk3066_soc_data** : const struct rk3x_i2c_soc_data (line 1178)
- static **rk3188_soc_data** : const struct rk3x_i2c_soc_data (line 1183)
- static **rk3228_soc_data** : const struct rk3x_i2c_soc_data (line 1188)
- static **rk3288_soc_data** : const struct rk3x_i2c_soc_data (line 1193)
- static **rk3399_soc_data** : const struct rk3x_i2c_soc_data (line 1198)
- static **rk3x_i2c_algorithm** : const struct i2c_algorithm (line 1162)
- static **rk3x_i2c_driver** : platform_driver (line 1399)
- static **rk3x_i2c_match** : const struct of_device_id[] (line 1203)
- static **rv1108_soc_data** : const struct rk3x_i2c_soc_data (line 1168)
- static **rv1126_soc_data** : const struct rk3x_i2c_soc_data (line 1173)
- static **standard_mode_spec** : const struct i2c_spec_values (line 106)

## Macros (33)

- **DEFAULT_SCL_RATE** (line 81)
- **REG_CLKDIV** (line 31)
- **REG_CON** (line 30)
- **REG_CON_ACTACK** (line 58)
- **REG_CON_EN** (line 45)
- **REG_CON_LASTACK** (line 57)
- **REG_CON_MOD**(mod) (line 53)
- **REG_CON_MOD_MASK** (line 54)
- **REG_CON_SDA_CFG**(cfg) (line 62)
- **REG_CON_START** (line 55)
- **REG_CON_STA_CFG**(cfg) (line 63)
- **REG_CON_STOP** (line 56)
- **REG_CON_STO_CFG**(cfg) (line 64)
- **REG_CON_TUNING_MASK** (line 60)
- **REG_FCNT** (line 38)
- **REG_IEN** (line 36)
- **REG_INT_ALL** (line 77)
- **REG_INT_BRF** (line 71)
- **REG_INT_BTF** (line 70)
- **REG_INT_MBRF** (line 73)
- **REG_INT_MBTF** (line 72)
- **REG_INT_NAKRCV** (line 76)
- **REG_INT_START** (line 74)
- **REG_INT_STOP** (line 75)
- **REG_IPD** (line 37)
- **REG_MRXADDR** (line 32)
- **REG_MRXADDR_VALID**(x) (line 67)
- **REG_MRXCNT** (line 35)
- **REG_MRXRADDR** (line 33)
- **REG_MTXCNT** (line 34)
- **RXBUFFER_BASE** (line 42)
- **TXBUFFER_BASE** (line 41)
- **WAIT_TIMEOUT** (line 80)
