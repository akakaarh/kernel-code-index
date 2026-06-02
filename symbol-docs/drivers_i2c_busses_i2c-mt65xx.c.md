# drivers/i2c/busses/i2c-mt65xx.c

Subsystem: drivers/i2c

## Functions (19)

### i2c_dump_register
- Return type: static void
- Signature: i2c_dump_register(struct mtk_i2c * i2c)
- Line: 945

### mtk_i2c_calculate_speed
- Return type: static int
- Signature: mtk_i2c_calculate_speed(struct mtk_i2c * i2c,unsigned int clk_src,unsigned int target_speed,unsigned int * timing_step_cnt,unsigned int * timing_sample_cnt)
- Line: 800

### mtk_i2c_check_ac_timing
- Return type: static int
- Signature: mtk_i2c_check_ac_timing(struct mtk_i2c * i2c,unsigned int clk_src,unsigned int check_speed,unsigned int step_cnt,unsigned int sample_cnt)
- Line: 698

### mtk_i2c_do_transfer
- Return type: static int
- Signature: mtk_i2c_do_transfer(struct mtk_i2c * i2c,struct i2c_msg * msgs,int num,int left_num)
- Line: 996

### mtk_i2c_functionality
- Return type: static u32
- Signature: mtk_i2c_functionality(struct i2c_adapter * adap)
- Line: 1347

### mtk_i2c_get_clk_div_restri
- Return type: static int
- Signature: mtk_i2c_get_clk_div_restri(struct mtk_i2c * i2c,unsigned int sample_cnt)
- Line: 661

### mtk_i2c_get_spec
- Return type: static const struct i2c_spec_values *
- Signature: mtk_i2c_get_spec(unsigned int speed)
- Line: 643

### mtk_i2c_init_hw
- Return type: static void
- Signature: mtk_i2c_init_hw(struct mtk_i2c * i2c)
- Line: 554

### mtk_i2c_irq
- Return type: static irqreturn_t
- Signature: mtk_i2c_irq(int irqno,void * dev_id)
- Line: 1318

### mtk_i2c_max_step_cnt
- Return type: static int
- Signature: mtk_i2c_max_step_cnt(unsigned int target_speed)
- Line: 653

### mtk_i2c_parse_dt
- Return type: static int
- Signature: mtk_i2c_parse_dt(struct device_node * np,struct mtk_i2c * i2c)
- Line: 1361

### mtk_i2c_probe
- Return type: static int
- Signature: mtk_i2c_probe(struct platform_device * pdev)
- Line: 1385

### mtk_i2c_readw
- Return type: static u16
- Signature: mtk_i2c_readw(struct mtk_i2c * i2c,enum I2C_REGS_OFFSET reg)
- Line: 543

### mtk_i2c_remove
- Return type: static void
- Signature: mtk_i2c_remove(struct platform_device * pdev)
- Line: 1515

### mtk_i2c_resume_noirq
- Return type: static int
- Signature: mtk_i2c_resume_noirq(struct device * dev)
- Line: 1534

### mtk_i2c_set_speed
- Return type: static void
- Signature: mtk_i2c_set_speed(struct mtk_i2c * i2c,unsigned int parent_clk)
- Line: 873

### mtk_i2c_suspend_noirq
- Return type: static int
- Signature: mtk_i2c_suspend_noirq(struct device * dev)
- Line: 1524

### mtk_i2c_transfer
- Return type: static int
- Signature: mtk_i2c_transfer(struct i2c_adapter * adap,struct i2c_msg msgs[],int num)
- Line: 1240

### mtk_i2c_writew
- Return type: static void
- Signature: mtk_i2c_writew(struct mtk_i2c * i2c,u16 val,enum I2C_REGS_OFFSET reg)
- Line: 548

## Structs (4)

### i2c_spec_values
- Line: 321
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

### mtk_i2c
- Line: 288
- Members:
  - base: void __iomem *
  - dev: device *
  - adap: i2c_adapter
  - bus_freq: u32
  - clk_div: u32
  - flags: u32
  - clk: clk *
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

### mtk_i2c_ac_timing
- Line: 275
- Members:
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

### mtk_i2c_compatible
- Line: 261
- Members:
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

## Enums (5)

### DMA_REGS_OFFSET
- Line: 110

### I2C_REGS_OFFSET
- Line: 135

### i2c_mt65xx_clks
- Line: 98

### i2c_trans_st_rs
- Line: 124

### mtk_trans_op
- Line: 129

## Variables (26)

- static **fast_mode_plus_spec** : const struct i2c_spec_values (line 342)
- static **fast_mode_spec** : const struct i2c_spec_values (line 335)
- static **i2c_mt65xx_clk_ids** : const char * const[] (line 106)
- static **mt2712_compat** : const struct mtk_i2c_compatible (line 366)
- static **mt6577_compat** : const struct mtk_i2c_compatible (line 379)
- static **mt6577_i2c_quirks** : const struct i2c_adapter_quirks (line 349)
- static **mt6589_compat** : const struct mtk_i2c_compatible (line 393)
- static **mt7622_compat** : const struct mtk_i2c_compatible (line 407)
- static **mt7622_i2c_quirks** : const struct i2c_adapter_quirks (line 358)
- static **mt7981_compat** : const struct mtk_i2c_compatible (line 434)
- static **mt7986_compat** : const struct mtk_i2c_compatible (line 446)
- static **mt8168_compat** : const struct mtk_i2c_compatible (line 421)
- static **mt8173_compat** : const struct mtk_i2c_compatible (line 459)
- static **mt8183_compat** : const struct mtk_i2c_compatible (line 472)
- static **mt8183_i2c_quirks** : const struct i2c_adapter_quirks (line 362)
- static **mt8186_compat** : const struct mtk_i2c_compatible (line 486)
- static **mt8188_compat** : const struct mtk_i2c_compatible (line 499)
- static **mt8192_compat** : const struct mtk_i2c_compatible (line 512)
- static **mt_i2c_regs_v1** : const u16[] (line 170)
- static **mt_i2c_regs_v2** : const u16[] (line 203)
- static **mt_i2c_regs_v3** : const u16[] (line 232)
- static **mtk_i2c_algorithm** : const struct i2c_algorithm (line 1356)
- static **mtk_i2c_driver** : platform_driver (line 1559)
- static **mtk_i2c_of_match** : const struct of_device_id[] (line 526)
- static **mtk_i2c_pm** : const struct dev_pm_ops (line 1554)
- static **standard_mode_spec** : const struct i2c_spec_values (line 328)

## Macros (54)

- **I2C_ACKERR** (line 33)
- **I2C_ARB_LOST** (line 31)
- **I2C_CHN_CLR_FLAG** (line 52)
- **I2C_CONTROL_ACKERR_DET_EN** (line 81)
- **I2C_CONTROL_ASYNC_MODE** (line 84)
- **I2C_CONTROL_CLK_EXT_EN** (line 79)
- **I2C_CONTROL_DIR_CHANGE** (line 80)
- **I2C_CONTROL_DMAACK_EN** (line 83)
- **I2C_CONTROL_DMA_EN** (line 78)
- **I2C_CONTROL_RS** (line 77)
- **I2C_CONTROL_TRANSFER_LEN_CHANGE** (line 82)
- **I2C_CONTROL_WRAPPER** (line 85)
- **I2C_DCM_DISABLE** (line 38)
- **I2C_DELAY_LEN** (line 44)
- **I2C_DMAACK_ENABLE** (line 54)
- **I2C_DMA_ASYNC_MODE** (line 58)
- **I2C_DMA_CLR_FLAG** (line 63)
- **I2C_DMA_CON_RX** (line 57)
- **I2C_DMA_CON_TX** (line 56)
- **I2C_DMA_DIR_CHANGE** (line 60)
- **I2C_DMA_HANDSHAKE_RST** (line 66)
- **I2C_DMA_HARD_RST** (line 65)
- **I2C_DMA_INT_FLAG_NONE** (line 62)
- **I2C_DMA_SKIP_CONFIG** (line 59)
- **I2C_DMA_START_EN** (line 61)
- **I2C_DMA_WARM_RST** (line 64)
- **I2C_DRV_NAME** (line 87)
- **I2C_FAST_MODE_BUFFER** (line 74)
- **I2C_FAST_MODE_PLUS_BUFFER** (line 75)
- **I2C_FIFO_ADDR_CLR** (line 43)
- **I2C_FS_START_CON** (line 46)
- **I2C_HANDSHAKE_RST** (line 42)
- **I2C_HS_NACKERR** (line 32)
- **I2C_IO_CONFIG_OPEN_DRAIN** (line 39)
- **I2C_IO_CONFIG_PUSH_PULL** (line 40)
- **I2C_RD_TRANAC_VALUE** (line 50)
- **I2C_RELIABILITY** (line 53)
- **I2C_RS_MUL_CNFG** (line 36)
- **I2C_RS_MUL_TRIG** (line 37)
- **I2C_RS_TRANSFER** (line 30)
- **I2C_SCL_MIS_COMP_VALUE** (line 51)
- **I2C_SOFT_RST** (line 41)
- **I2C_STANDARD_MODE_BUFFER** (line 73)
- **I2C_ST_START_CON** (line 45)
- **I2C_TIME_CLR_VALUE** (line 47)
- **I2C_TIME_DEFAULT_VALUE** (line 48)
- **I2C_TRANSAC_COMP** (line 34)
- **I2C_TRANSAC_START** (line 35)
- **I2C_WRRD_TRANAC_VALUE** (line 49)
- **MAX_CLOCK_DIV_5BITS** (line 71)
- **MAX_CLOCK_DIV_8BITS** (line 70)
- **MAX_HS_STEP_CNT_DIV** (line 72)
- **MAX_SAMPLE_CNT_DIV** (line 68)
- **MAX_STEP_CNT_DIV** (line 69)
