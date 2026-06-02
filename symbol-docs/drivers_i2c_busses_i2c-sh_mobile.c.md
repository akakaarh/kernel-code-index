# drivers/i2c/busses/i2c-sh_mobile.c

Subsystem: drivers/i2c

## Functions (32)

### i2c_op
- Return type: static unsigned char
- Signature: i2c_op(struct sh_mobile_i2c_data * pd,enum sh_mobile_i2c_op op)
- Line: 304

### iic_rd
- Return type: static unsigned char
- Signature: iic_rd(struct sh_mobile_i2c_data * pd,int offs)
- Line: 194

### iic_set_clr
- Return type: static void
- Signature: iic_set_clr(struct sh_mobile_i2c_data * pd,int offs,unsigned char set,unsigned char clr)
- Line: 199

### iic_wr
- Return type: static void
- Signature: iic_wr(struct sh_mobile_i2c_data * pd,int offs,unsigned char data)
- Line: 186

### poll_busy
- Return type: static int
- Signature: poll_busy(struct sh_mobile_i2c_data * pd)
- Line: 611

### poll_dte
- Return type: static int
- Signature: poll_dte(struct sh_mobile_i2c_data * pd)
- Line: 592

### sh_mobile_i2c_adap_exit
- Return type: static void __exit
- Signature: sh_mobile_i2c_adap_exit(void)
- Line: 996

### sh_mobile_i2c_adap_init
- Return type: static int __init
- Signature: sh_mobile_i2c_adap_init(void)
- Line: 990

### sh_mobile_i2c_check_timing
- Return type: static int
- Signature: sh_mobile_i2c_check_timing(struct sh_mobile_i2c_data * pd)
- Line: 239

### sh_mobile_i2c_cleanup_dma
- Return type: static void
- Signature: sh_mobile_i2c_cleanup_dma(struct sh_mobile_i2c_data * pd,bool terminate)
- Line: 446

### sh_mobile_i2c_dma_callback
- Return type: static void
- Signature: sh_mobile_i2c_dma_callback(void * data)
- Line: 461

### sh_mobile_i2c_func
- Return type: static u32
- Signature: sh_mobile_i2c_func(struct i2c_adapter * adapter)
- Line: 736

### sh_mobile_i2c_hook_irqs
- Return type: static int
- Signature: sh_mobile_i2c_hook_irqs(struct platform_device * dev,struct sh_mobile_i2c_data * pd)
- Line: 826

### sh_mobile_i2c_icch
- Return type: static u32
- Signature: sh_mobile_i2c_icch(unsigned long count_khz,u32 tHIGH,u32 tf)
- Line: 220

### sh_mobile_i2c_iccl
- Return type: static u32
- Signature: sh_mobile_i2c_iccl(unsigned long count_khz,u32 tLOW,u32 tf)
- Line: 205

### sh_mobile_i2c_init
- Return type: static int
- Signature: sh_mobile_i2c_init(struct sh_mobile_i2c_data * pd)
- Line: 265

### sh_mobile_i2c_isr
- Return type: static irqreturn_t
- Signature: sh_mobile_i2c_isr(int irq,void * dev_id)
- Line: 403

### sh_mobile_i2c_isr_rx
- Return type: static int
- Signature: sh_mobile_i2c_isr_rx(struct sh_mobile_i2c_data * pd)
- Line: 371

### sh_mobile_i2c_isr_tx
- Return type: static int
- Signature: sh_mobile_i2c_isr_tx(struct sh_mobile_i2c_data * pd)
- Line: 355

### sh_mobile_i2c_probe
- Return type: static int
- Signature: sh_mobile_i2c_probe(struct platform_device * dev)
- Line: 865

### sh_mobile_i2c_r8a7740_workaround
- Return type: static int
- Signature: sh_mobile_i2c_r8a7740_workaround(struct sh_mobile_i2c_data * pd)
- Line: 754

### sh_mobile_i2c_release_dma
- Return type: static void
- Signature: sh_mobile_i2c_release_dma(struct sh_mobile_i2c_data * pd)
- Line: 813

### sh_mobile_i2c_remove
- Return type: static void
- Signature: sh_mobile_i2c_remove(struct platform_device * dev)
- Line: 950

### sh_mobile_i2c_request_dma_chan
- Return type: static dma_chan *
- Signature: sh_mobile_i2c_request_dma_chan(struct device * dev,enum dma_transfer_direction dir,dma_addr_t port_addr)
- Line: 472

### sh_mobile_i2c_resume
- Return type: static int
- Signature: sh_mobile_i2c_resume(struct device * dev)
- Line: 967

### sh_mobile_i2c_suspend
- Return type: static int
- Signature: sh_mobile_i2c_suspend(struct device * dev)
- Line: 959

### sh_mobile_i2c_v2_init
- Return type: static int
- Signature: sh_mobile_i2c_v2_init(struct sh_mobile_i2c_data * pd)
- Line: 292

### sh_mobile_i2c_xfer
- Return type: static int
- Signature: sh_mobile_i2c_xfer(struct i2c_adapter * adapter,struct i2c_msg * msgs,int num)
- Line: 716

### sh_mobile_i2c_xfer_atomic
- Return type: static int
- Signature: sh_mobile_i2c_xfer_atomic(struct i2c_adapter * adapter,struct i2c_msg * msgs,int num)
- Line: 726

### sh_mobile_i2c_xfer_dma
- Return type: static void
- Signature: sh_mobile_i2c_xfer_dma(struct sh_mobile_i2c_data * pd)
- Line: 508

### sh_mobile_xfer
- Return type: static int
- Signature: sh_mobile_xfer(struct sh_mobile_i2c_data * pd,struct i2c_msg * msgs,int num)
- Line: 640

### start_ch
- Return type: static void
- Signature: start_ch(struct sh_mobile_i2c_data * pd,struct i2c_msg * usr_msg,bool do_init)
- Line: 562

## Structs (2)

### sh_mobile_dt_config
- Line: 143
- Members:
  - dev: device *
  - reg: void __iomem *
  - adap: i2c_adapter
  - bus_speed: unsigned long
  - clks_per_count: unsigned int
  - clk: clk *
  - icic: u_int8_t
  - flags: u_int8_t
  - iccl: u_int16_t
  - icch: u_int16_t
  - lock: spinlock_t
  - wait: wait_queue_head_t
  - msg: i2c_msg *
  - pos: int
  - sr: int
  - send_stop: bool
  - stop_after_dma: bool
  - atomic_xfer: bool
  - res: resource *
  - dma_tx: dma_chan *
  - dma_rx: dma_chan *
  - sg: scatterlist
  - dma_direction: dma_data_direction
  - dma_buf: u8 *
  - clks_per_count: int
  - setup: int (*)(struct sh_mobile_i2c_data * pd)

### sh_mobile_i2c_data
- Line: 114
- Members:
  - dev: device *
  - reg: void __iomem *
  - adap: i2c_adapter
  - bus_speed: unsigned long
  - clks_per_count: unsigned int
  - clk: clk *
  - icic: u_int8_t
  - flags: u_int8_t
  - iccl: u_int16_t
  - icch: u_int16_t
  - lock: spinlock_t
  - wait: wait_queue_head_t
  - msg: i2c_msg *
  - pos: int
  - sr: int
  - send_stop: bool
  - stop_after_dma: bool
  - atomic_xfer: bool
  - res: resource *
  - dma_tx: dma_chan *
  - dma_rx: dma_chan *
  - sg: scatterlist
  - dma_direction: dma_data_direction
  - dma_buf: u8 *
  - clks_per_count: int
  - setup: int (*)(struct sh_mobile_i2c_data * pd)

## Enums (1)

### sh_mobile_i2c_op
- Line: 103

## Variables (8)

- static **default_dt_config** : const struct sh_mobile_dt_config (line 779)
- static **fast_clock_dt_config** : const struct sh_mobile_dt_config (line 784)
- static **r8a7740_dt_config** : const struct sh_mobile_dt_config (line 789)
- static **sh_mobile_i2c_algorithm** : const struct i2c_algorithm (line 741)
- static **sh_mobile_i2c_driver** : platform_driver (line 980)
- static **sh_mobile_i2c_dt_ids** : const struct of_device_id[] (line 794)
- static **sh_mobile_i2c_pm_ops** : const struct dev_pm_ops (line 975)
- static **sh_mobile_i2c_quirks** : const struct i2c_adapter_quirks (line 747)

## Macros (30)

- **ICCH** (line 156)
- **ICCL** (line 155)
- **ICCR** (line 152)
- **ICCR_BBSY** (line 163)
- **ICCR_ICE** (line 160)
- **ICCR_RACK** (line 161)
- **ICCR_SCP** (line 164)
- **ICCR_TRS** (line 162)
- **ICDR** (line 151)
- **ICIC** (line 154)
- **ICIC_ALE** (line 179)
- **ICIC_DTEE** (line 182)
- **ICIC_ICCHB8** (line 176)
- **ICIC_ICCLB8** (line 175)
- **ICIC_RDMAE** (line 178)
- **ICIC_TACKE** (line 180)
- **ICIC_TDMAE** (line 177)
- **ICIC_WAITE** (line 181)
- **ICSR** (line 153)
- **ICSR_AL** (line 170)
- **ICSR_BUSY** (line 169)
- **ICSR_DTE** (line 173)
- **ICSR_SCLM** (line 166)
- **ICSR_SDAM** (line 167)
- **ICSR_TACK** (line 171)
- **ICSR_WAIT** (line 172)
- **ICSTART** (line 157)
- **ICSTART_ICSTART** (line 184)
- **IIC_FLAG_HAS_ICIC67** (line 148)
- **SW_DONE** (line 168)
