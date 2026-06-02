# drivers/i2c/busses/i2c-mt7621.c

Subsystem: drivers/i2c

## Functions (12)

### mtk_i2c_check_ack
- Return type: static int
- Signature: mtk_i2c_check_ack(struct mtk_i2c * i2c,u32 expected)
- Line: 112

### mtk_i2c_cmd
- Return type: static int
- Signature: mtk_i2c_cmd(struct mtk_i2c * i2c,u32 cmd,int page_len)
- Line: 132

### mtk_i2c_dump_reg
- Return type: static void
- Signature: mtk_i2c_dump_reg(struct mtk_i2c * i2c)
- Line: 101

### mtk_i2c_func
- Return type: static u32
- Signature: mtk_i2c_func(struct i2c_adapter * a)
- Line: 240

### mtk_i2c_init
- Return type: static void
- Signature: mtk_i2c_init(struct mtk_i2c * i2c)
- Line: 257

### mtk_i2c_probe
- Return type: static int
- Signature: mtk_i2c_probe(struct platform_device * pdev)
- Line: 268

### mtk_i2c_remove
- Return type: static void
- Signature: mtk_i2c_remove(struct platform_device * pdev)
- Line: 321

### mtk_i2c_reset
- Return type: static void
- Signature: mtk_i2c_reset(struct mtk_i2c * i2c)
- Line: 84

### mtk_i2c_start
- Return type: static int
- Signature: mtk_i2c_start(struct mtk_i2c * i2c)
- Line: 120

### mtk_i2c_stop
- Return type: static int
- Signature: mtk_i2c_stop(struct mtk_i2c * i2c)
- Line: 126

### mtk_i2c_wait_idle
- Return type: static int
- Signature: mtk_i2c_wait_idle(struct mtk_i2c * i2c)
- Line: 70

### mtk_i2c_xfer
- Return type: static int
- Signature: mtk_i2c_xfer(struct i2c_adapter * adap,struct i2c_msg * msgs,int num)
- Line: 139

## Structs (1)

### mtk_i2c
- Line: 60
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

## Variables (3)

- static **i2c_mtk_dt_ids** : const struct of_device_id[] (line 250)
- static **mtk_i2c_algo** : const struct i2c_algorithm (line 245)
- static **mtk_i2c_driver** : platform_driver (line 328)

## Macros (28)

- **REG_PINTCL_REG** (line 30)
- **REG_PINTEN_REG** (line 28)
- **REG_PINTST_REG** (line 29)
- **REG_SM0CFG2_REG** (line 23)
- **REG_SM0CTL0_REG** (line 24)
- **REG_SM0CTL1_REG** (line 25)
- **REG_SM0D0_REG** (line 26)
- **REG_SM0D1_REG** (line 27)
- **SM0CFG2_IS_AUTOMODE** (line 33)
- **SM0CTL0_CLK_DIV_MASK** (line 37)
- **SM0CTL0_CLK_DIV_MAX** (line 38)
- **SM0CTL0_CS_STATUS** (line 39)
- **SM0CTL0_EN** (line 42)
- **SM0CTL0_ODRAIN** (line 36)
- **SM0CTL0_SCL_STATE** (line 40)
- **SM0CTL0_SCL_STRETCH** (line 43)
- **SM0CTL0_SDA_STATE** (line 41)
- **SM0CTL1_ACK_MASK** (line 46)
- **SM0CTL1_MODE_MASK** (line 54)
- **SM0CTL1_PGLEN**(x) (line 48)
- **SM0CTL1_PGLEN_MASK** (line 47)
- **SM0CTL1_READ** (line 49)
- **SM0CTL1_READ_LAST** (line 50)
- **SM0CTL1_START** (line 53)
- **SM0CTL1_STOP** (line 51)
- **SM0CTL1_TRI** (line 55)
- **SM0CTL1_WRITE** (line 52)
- **TIMEOUT_MS** (line 58)
