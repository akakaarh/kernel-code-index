# drivers/i2c/busses/i2c-rcar.c

Subsystem: drivers/i2c

## Functions (36)

### rcar_i2c_bus_barrier
- Return type: static int
- Signature: rcar_i2c_bus_barrier(struct rcar_i2c_priv * priv)
- Line: 270

### rcar_i2c_cleanup_dma
- Return type: static void
- Signature: rcar_i2c_cleanup_dma(struct rcar_i2c_priv * priv,bool terminate)
- Line: 447

### rcar_i2c_clear_irq
- Return type: static void
- Signature: rcar_i2c_clear_irq(struct rcar_i2c_priv * priv,u32 val)
- Line: 187

### rcar_i2c_clock_calculate
- Return type: static int
- Signature: rcar_i2c_clock_calculate(struct rcar_i2c_priv * priv)
- Line: 286

### rcar_i2c_dma
- Return type: static bool
- Signature: rcar_i2c_dma(struct rcar_i2c_priv * priv)
- Line: 479

### rcar_i2c_dma_callback
- Return type: static void
- Signature: rcar_i2c_dma_callback(void * data)
- Line: 470

### rcar_i2c_do_reset
- Return type: static int
- Signature: rcar_i2c_do_reset(struct rcar_i2c_priv * priv)
- Line: 891

### rcar_i2c_first_msg
- Return type: static void
- Signature: rcar_i2c_first_msg(struct rcar_i2c_priv * priv,struct i2c_msg * msgs,int num)
- Line: 430

### rcar_i2c_func
- Return type: static u32
- Signature: rcar_i2c_func(struct i2c_adapter * adap)
- Line: 1067

### rcar_i2c_gen2_irq
- Return type: static irqreturn_t
- Signature: rcar_i2c_gen2_irq(int irq,void * ptr)
- Line: 779

### rcar_i2c_gen3_irq
- Return type: static irqreturn_t
- Signature: rcar_i2c_gen3_irq(int irq,void * ptr)
- Line: 796

### rcar_i2c_get_bus_free
- Return type: static int
- Signature: rcar_i2c_get_bus_free(struct i2c_adapter * adap)
- Line: 223

### rcar_i2c_get_scl
- Return type: static int
- Signature: rcar_i2c_get_scl(struct i2c_adapter * adap)
- Line: 192

### rcar_i2c_init
- Return type: static void
- Signature: rcar_i2c_init(struct rcar_i2c_priv * priv)
- Line: 238

### rcar_i2c_irq
- Return type: static irqreturn_t
- Signature: rcar_i2c_irq(int irq,struct rcar_i2c_priv * priv,u32 msr)
- Line: 732

### rcar_i2c_irq_recv
- Return type: static void
- Signature: rcar_i2c_irq_recv(struct rcar_i2c_priv * priv,u32 msr)
- Line: 601

### rcar_i2c_irq_send
- Return type: static void
- Signature: rcar_i2c_irq_send(struct rcar_i2c_priv * priv,u32 msr)
- Line: 552

### rcar_i2c_master_xfer
- Return type: static int
- Signature: rcar_i2c_master_xfer(struct i2c_adapter * adap,struct i2c_msg * msgs,int num)
- Line: 907

### rcar_i2c_master_xfer_atomic
- Return type: static int
- Signature: rcar_i2c_master_xfer_atomic(struct i2c_adapter * adap,struct i2c_msg * msgs,int num)
- Line: 968

### rcar_i2c_next_msg
- Return type: static void
- Signature: rcar_i2c_next_msg(struct rcar_i2c_priv * priv)
- Line: 439

### rcar_i2c_prepare_msg
- Return type: static void
- Signature: rcar_i2c_prepare_msg(struct rcar_i2c_priv * priv)
- Line: 411

### rcar_i2c_probe
- Return type: static int
- Signature: rcar_i2c_probe(struct platform_device * pdev)
- Line: 1118

### rcar_i2c_read
- Return type: static u32
- Signature: rcar_i2c_read(struct rcar_i2c_priv * priv,int reg)
- Line: 182

### rcar_i2c_release_dma
- Return type: static void
- Signature: rcar_i2c_release_dma(struct rcar_i2c_priv * priv)
- Line: 877

### rcar_i2c_remove
- Return type: static void
- Signature: rcar_i2c_remove(struct platform_device * pdev)
- Line: 1243

### rcar_i2c_request_dma
- Return type: static void
- Signature: rcar_i2c_request_dma(struct rcar_i2c_priv * priv,struct i2c_msg * msg)
- Line: 854

### rcar_i2c_request_dma_chan
- Return type: static dma_chan *
- Signature: rcar_i2c_request_dma_chan(struct device * dev,enum dma_transfer_direction dir,dma_addr_t port_addr)
- Line: 816

### rcar_i2c_reset_slave
- Return type: static void
- Signature: rcar_i2c_reset_slave(struct rcar_i2c_priv * priv)
- Line: 262

### rcar_i2c_resume
- Return type: static int
- Signature: rcar_i2c_resume(struct device * dev)
- Line: 1265

### rcar_i2c_set_scl
- Return type: static void
- Signature: rcar_i2c_set_scl(struct i2c_adapter * adap,int val)
- Line: 199

### rcar_i2c_set_sda
- Return type: static void
- Signature: rcar_i2c_set_sda(struct i2c_adapter * adap,int val)
- Line: 211

### rcar_i2c_slave_irq
- Return type: static bool
- Signature: rcar_i2c_slave_irq(struct rcar_i2c_priv * priv)
- Line: 657

### rcar_i2c_suspend
- Return type: static int
- Signature: rcar_i2c_suspend(struct device * dev)
- Line: 1257

### rcar_i2c_write
- Return type: static void
- Signature: rcar_i2c_write(struct rcar_i2c_priv * priv,int reg,u32 val)
- Line: 177

### rcar_reg_slave
- Return type: static int
- Signature: rcar_reg_slave(struct i2c_client * slave)
- Line: 1027

### rcar_unreg_slave
- Return type: static int
- Signature: rcar_unreg_slave(struct i2c_client * slave)
- Line: 1049

## Structs (1)

### rcar_i2c_priv
- Line: 142
- Members:
  - flags: u32
  - io: void __iomem *
  - adap: i2c_adapter
  - msg: i2c_msg *
  - msgs_left: int
  - clk: clk *
  - wait: wait_queue_head_t
  - pos: int
  - icccr: u32
  - schd: u16
  - scld: u16
  - smd: u8
  - recovery_icmcr: u8
  - devtype: rcar_i2c_type
  - slave: i2c_client *
  - res: resource *
  - dma_tx: dma_chan *
  - dma_rx: dma_chan *
  - sg: scatterlist
  - dma_direction: dma_data_direction
  - rstc: reset_control *
  - irq: int
  - host_notify_client: i2c_client *
  - slave_flags: u8

## Enums (1)

### rcar_i2c_type
- Line: 135

## Variables (6)

- static **rcar_i2c_algo** : const struct i2c_algorithm (line 1086)
- static **rcar_i2c_bri** : i2c_bus_recovery_info (line 230)
- static **rcar_i2c_driver** : platform_driver (line 1277)
- static **rcar_i2c_dt_ids** : const struct of_device_id[] (line 1098)
- static **rcar_i2c_pm_ops** : const struct dev_pm_ops (line 1273)
- static **rcar_i2c_quirks** : const struct i2c_adapter_quirks (line 1094)

## Macros (76)

- **CDFD** (line 93)
- **ESG** (line 65)
- **FMPE** (line 92)
- **FNA** (line 55)
- **FSB** (line 64)
- **FSCL** (line 59)
- **FSDA** (line 60)
- **GCAE** (line 54)
- **GCAR** (line 68)
- **HLSE** (line 94)
- **ICCCR** (line 40)
- **ICCCR2** (line 44)
- **ICDMAER** (line 49)
- **ICFBSCR** (line 48)
- **ICHPR** (line 46)
- **ICLPR** (line 47)
- **ICMAR** (line 42)
- **ICMCR** (line 35)
- **ICMIER** (line 39)
- **ICMPR** (line 45)
- **ICMSR** (line 37)
- **ICRXTX** (line 43)
- **ICSAR** (line 41)
- **ICSCR** (line 34)
- **ICSIER** (line 38)
- **ICSSR** (line 36)
- **ID_ARBLOST** (line 122)
- **ID_DONE** (line 121)
- **ID_EPROTO** (line 124)
- **ID_LAST_MSG** (line 119)
- **ID_NACK** (line 123)
- **ID_P_FMPLUS** (line 126)
- **ID_P_HOST_NOTIFY** (line 128)
- **ID_P_MASK** (line 131)
- **ID_P_NOT_ATOMIC** (line 127)
- **ID_P_NO_RXDMA** (line 129)
- **ID_P_PM_BLOCKED** (line 130)
- **ID_REP_AFTER_RD** (line 120)
- **ID_SLAVE_NACK** (line 133)
- **MAL** (line 78)
- **MAT** (line 83)
- **MDBS** (line 58)
- **MDE** (line 80)
- **MDR** (line 82)
- **MDT** (line 81)
- **MIE** (line 62)
- **MNR** (line 77)
- **MST** (line 79)
- **OBPC** (line 61)
- **RCAR_BUS_PHASE_DATA** (line 112)
- **RCAR_BUS_PHASE_START** (line 111)
- **RCAR_BUS_PHASE_STOP** (line 113)
- **RCAR_DEFAULT_SMD** (line 109)
- **RCAR_IRQ_RECV** (line 116)
- **RCAR_IRQ_SEND** (line 115)
- **RCAR_IRQ_STOP** (line 117)
- **RCAR_MIN_DMA_LEN** (line 100)
- **RCAR_SCHD_RATIO** (line 104)
- **RCAR_SCLD_RATIO** (line 103)
- **RMDMAE** (line 88)
- **RSDMAE** (line 86)
- **SAR** (line 74)
- **SDBS** (line 52)
- **SDE** (line 71)
- **SDR** (line 73)
- **SDT** (line 72)
- **SIE** (line 53)
- **SME** (line 95)
- **SSR** (line 70)
- **STM** (line 69)
- **TCYC17** (line 98)
- **TMDMAE** (line 89)
- **TSBE** (line 63)
- **TSDMAE** (line 87)
- **rcar_i2c_is_recv**(p) (line 175)
- **rcar_i2c_priv_to_dev**(p) (line 174)
