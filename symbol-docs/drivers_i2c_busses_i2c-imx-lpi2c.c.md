# drivers/i2c/busses/i2c-imx-lpi2c.c

Subsystem: drivers/i2c

## Functions (59)

### dma_exit
- Return type: static void
- Signature: dma_exit(struct device * dev,struct lpi2c_imx_dma * dma)
- Line: 1386

### is_use_dma
- Return type: static bool
- Signature: is_use_dma(struct lpi2c_imx_struct * lpi2c_imx,struct i2c_msg * msg)
- Line: 658

### lpi2c_SMBus_block_read_length_byte
- Return type: static unsigned int
- Signature: lpi2c_SMBus_block_read_length_byte(struct lpi2c_imx_struct * lpi2c_imx)
- Line: 548

### lpi2c_cleanup_dma
- Return type: static void
- Signature: lpi2c_cleanup_dma(struct lpi2c_imx_dma * dma)
- Line: 791

### lpi2c_cleanup_rx_cmd_dma
- Return type: static void
- Signature: lpi2c_cleanup_rx_cmd_dma(struct lpi2c_imx_dma * dma)
- Line: 784

### lpi2c_dma_callback
- Return type: static void
- Signature: lpi2c_dma_callback(void * data)
- Line: 801

### lpi2c_dma_config
- Return type: static int
- Signature: lpi2c_dma_config(struct lpi2c_imx_struct * lpi2c_imx)
- Line: 949

### lpi2c_dma_enable
- Return type: static void
- Signature: lpi2c_dma_enable(struct lpi2c_imx_struct * lpi2c_imx)
- Line: 986

### lpi2c_dma_init
- Return type: static int
- Signature: lpi2c_dma_init(struct device * dev,dma_addr_t phy_addr)
- Line: 1397

### lpi2c_dma_rx_cmd_submit
- Return type: static int
- Signature: lpi2c_dma_rx_cmd_submit(struct lpi2c_imx_struct * lpi2c_imx)
- Line: 808

### lpi2c_dma_submit
- Return type: static int
- Signature: lpi2c_dma_submit(struct lpi2c_imx_struct * lpi2c_imx)
- Line: 853

### lpi2c_dma_unmap
- Return type: static void
- Signature: lpi2c_dma_unmap(struct lpi2c_imx_dma * dma)
- Line: 773

### lpi2c_imx_alloc_rx_cmd_buf
- Return type: static int
- Signature: lpi2c_imx_alloc_rx_cmd_buf(struct lpi2c_imx_struct * lpi2c_imx)
- Line: 728

### lpi2c_imx_bus_busy
- Return type: static int
- Signature: lpi2c_imx_bus_busy(struct lpi2c_imx_struct * lpi2c_imx,bool atomic)
- Line: 226

### lpi2c_imx_config
- Return type: static int
- Signature: lpi2c_imx_config(struct lpi2c_imx_struct * lpi2c_imx)
- Line: 308

### lpi2c_imx_dma_burst_num_calculate
- Return type: static void
- Signature: lpi2c_imx_dma_burst_num_calculate(struct lpi2c_imx_struct * lpi2c_imx)
- Line: 927

### lpi2c_imx_dma_msg_complete
- Return type: static int
- Signature: lpi2c_imx_dma_msg_complete(struct lpi2c_imx_struct * lpi2c_imx)
- Line: 759

### lpi2c_imx_dma_timeout_calculate
- Return type: static int
- Signature: lpi2c_imx_dma_timeout_calculate(struct lpi2c_imx_struct * lpi2c_imx)
- Line: 715

### lpi2c_imx_dma_xfer
- Return type: static int
- Signature: lpi2c_imx_dma_xfer(struct lpi2c_imx_struct * lpi2c_imx,struct i2c_msg * msg)
- Line: 1033

### lpi2c_imx_find_max_burst_num
- Return type: static int
- Signature: lpi2c_imx_find_max_burst_num(unsigned int fifosize,unsigned int len)
- Line: 912

### lpi2c_imx_func
- Return type: static u32
- Signature: lpi2c_imx_func(struct i2c_adapter * adapter)
- Line: 1438

### lpi2c_imx_init_recovery_info
- Return type: static int
- Signature: lpi2c_imx_init_recovery_info(struct lpi2c_imx_struct * lpi2c_imx,struct platform_device * pdev)
- Line: 1372

### lpi2c_imx_intctrl
- Return type: static void
- Signature: lpi2c_imx_intctrl(struct lpi2c_imx_struct * lpi2c_imx,unsigned int enable)
- Line: 220

### lpi2c_imx_isr
- Return type: static irqreturn_t
- Signature: lpi2c_imx_isr(int irq,void * dev_id)
- Line: 1254

### lpi2c_imx_master_disable
- Return type: static int
- Signature: lpi2c_imx_master_disable(struct lpi2c_imx_struct * lpi2c_imx)
- Line: 394

### lpi2c_imx_master_enable
- Return type: static int
- Signature: lpi2c_imx_master_enable(struct lpi2c_imx_struct * lpi2c_imx)
- Line: 365

### lpi2c_imx_master_isr
- Return type: static irqreturn_t
- Signature: lpi2c_imx_master_isr(struct lpi2c_imx_struct * lpi2c_imx)
- Line: 1233

### lpi2c_imx_pio_msg_complete
- Return type: static int
- Signature: lpi2c_imx_pio_msg_complete(struct lpi2c_imx_struct * lpi2c_imx)
- Line: 407

### lpi2c_imx_pio_xfer
- Return type: static int
- Signature: lpi2c_imx_pio_xfer(struct lpi2c_imx_struct * lpi2c_imx,struct i2c_msg * msg)
- Line: 681

### lpi2c_imx_pio_xfer_atomic
- Return type: static int
- Signature: lpi2c_imx_pio_xfer_atomic(struct lpi2c_imx_struct * lpi2c_imx,struct i2c_msg * msg)
- Line: 700

### lpi2c_imx_probe
- Return type: static int
- Signature: lpi2c_imx_probe(struct platform_device * pdev)
- Line: 1460

### lpi2c_imx_read_atomic
- Return type: static int
- Signature: lpi2c_imx_read_atomic(struct lpi2c_imx_struct * lpi2c_imx,struct i2c_msg * msgs)
- Line: 635

### lpi2c_imx_read_chunk_atomic
- Return type: static bool
- Signature: lpi2c_imx_read_chunk_atomic(struct lpi2c_imx_struct * lpi2c_imx)
- Line: 621

### lpi2c_imx_read_init
- Return type: static int
- Signature: lpi2c_imx_read_init(struct lpi2c_imx_struct * lpi2c_imx,struct i2c_msg * msgs)
- Line: 558

### lpi2c_imx_read_rxfifo
- Return type: static bool
- Signature: lpi2c_imx_read_rxfifo(struct lpi2c_imx_struct * lpi2c_imx,bool atomic)
- Line: 485

### lpi2c_imx_register_target
- Return type: static int
- Signature: lpi2c_imx_register_target(struct i2c_client * client)
- Line: 1328

### lpi2c_imx_remove
- Return type: static void
- Signature: lpi2c_imx_remove(struct platform_device * pdev)
- Line: 1574

### lpi2c_imx_set_mode
- Return type: static void
- Signature: lpi2c_imx_set_mode(struct lpi2c_imx_struct * lpi2c_imx)
- Line: 256

### lpi2c_imx_set_rx_watermark
- Return type: static void
- Signature: lpi2c_imx_set_rx_watermark(struct lpi2c_imx_struct * lpi2c_imx)
- Line: 444

### lpi2c_imx_set_tx_watermark
- Return type: static void
- Signature: lpi2c_imx_set_tx_watermark(struct lpi2c_imx_struct * lpi2c_imx)
- Line: 439

### lpi2c_imx_start
- Return type: static int
- Signature: lpi2c_imx_start(struct lpi2c_imx_struct * lpi2c_imx,struct i2c_msg * msgs,bool atomic)
- Line: 275

### lpi2c_imx_stop
- Return type: static void
- Signature: lpi2c_imx_stop(struct lpi2c_imx_struct * lpi2c_imx,bool atomic)
- Line: 291

### lpi2c_imx_target_init
- Return type: static void
- Signature: lpi2c_imx_target_init(struct lpi2c_imx_struct * lpi2c_imx)
- Line: 1278

### lpi2c_imx_target_isr
- Return type: static irqreturn_t
- Signature: lpi2c_imx_target_isr(struct lpi2c_imx_struct * lpi2c_imx,u32 ssr,u32 sier_filter)
- Line: 1185

### lpi2c_imx_txfifo_cnt
- Return type: static u32
- Signature: lpi2c_imx_txfifo_cnt(struct lpi2c_imx_struct * lpi2c_imx)
- Line: 251

### lpi2c_imx_txfifo_empty
- Return type: static int
- Signature: lpi2c_imx_txfifo_empty(struct lpi2c_imx_struct * lpi2c_imx,bool atomic)
- Line: 416

### lpi2c_imx_unregister_target
- Return type: static int
- Signature: lpi2c_imx_unregister_target(struct i2c_client * client)
- Line: 1349

### lpi2c_imx_write
- Return type: static void
- Signature: lpi2c_imx_write(struct lpi2c_imx_struct * lpi2c_imx,struct i2c_msg * msgs)
- Line: 522

### lpi2c_imx_write_atomic
- Return type: static int
- Signature: lpi2c_imx_write_atomic(struct lpi2c_imx_struct * lpi2c_imx,struct i2c_msg * msgs)
- Line: 530

### lpi2c_imx_write_txfifo
- Return type: static bool
- Signature: lpi2c_imx_write_txfifo(struct lpi2c_imx_struct * lpi2c_imx,bool atomic)
- Line: 458

### lpi2c_imx_xfer
- Return type: static int
- Signature: lpi2c_imx_xfer(struct i2c_adapter * adapter,struct i2c_msg * msgs,int num)
- Line: 1175

### lpi2c_imx_xfer_atomic
- Return type: static int
- Signature: lpi2c_imx_xfer_atomic(struct i2c_adapter * adapter,struct i2c_msg * msgs,int num)
- Line: 1180

### lpi2c_imx_xfer_common
- Return type: static int
- Signature: lpi2c_imx_xfer_common(struct i2c_adapter * adapter,struct i2c_msg * msgs,int num,bool atomic)
- Line: 1109

### lpi2c_resume
- Return type: static int
- Signature: lpi2c_resume(struct device * dev)
- Line: 1686

### lpi2c_resume_noirq
- Return type: static int __maybe_unused
- Signature: lpi2c_resume_noirq(struct device * dev)
- Line: 1641

### lpi2c_runtime_resume
- Return type: static int __maybe_unused
- Signature: lpi2c_runtime_resume(struct device * dev)
- Line: 1602

### lpi2c_runtime_suspend
- Return type: static int __maybe_unused
- Signature: lpi2c_runtime_suspend(struct device * dev)
- Line: 1584

### lpi2c_suspend
- Return type: static int
- Signature: lpi2c_suspend(struct device * dev)
- Line: 1661

### lpi2c_suspend_noirq
- Return type: static int __maybe_unused
- Signature: lpi2c_suspend_noirq(struct device * dev)
- Line: 1636

## Structs (3)

### imx_lpi2c_hwdata
- Line: 154
- Members:
  - need_request_free_irq: bool
  - need_prepare_unprepare_clk: bool
  - using_pio_mode: bool
  - rx_cmd_buf_len: u8
  - dma_buf: u8 *
  - rx_cmd_buf: u16 *
  - dma_len: unsigned int
  - tx_burst_num: unsigned int
  - rx_burst_num: unsigned int
  - dma_msg_flag: unsigned long
  - phy_addr: resource_size_t
  - dma_tx_addr: dma_addr_t
  - dma_addr: dma_addr_t
  - dma_data_dir: dma_data_direction
  - dma_transfer_dir: dma_transfer_direction
  - chan_tx: dma_chan *
  - chan_rx: dma_chan *
  - adapter: i2c_adapter
  - num_clks: int
  - clks: clk_bulk_data *
  - base: void __iomem *
  - rx_buf: __u8 *
  - tx_buf: __u8 *
  - complete: completion
  - rate_per: unsigned long
  - msglen: unsigned int
  - delivered: unsigned int
  - block_data: unsigned int
  - bitrate: unsigned int
  - txfifosize: unsigned int
  - rxfifosize: unsigned int
  - mode: lpi2c_imx_mode
  - rinfo: i2c_bus_recovery_info
  - can_use_dma: bool
  - dma: lpi2c_imx_dma *
  - target: i2c_client *
  - irq: int
  - hwdata: const struct imx_lpi2c_hwdata *

### lpi2c_imx_dma
- Line: 159
- Members:
  - need_request_free_irq: bool
  - need_prepare_unprepare_clk: bool
  - using_pio_mode: bool
  - rx_cmd_buf_len: u8
  - dma_buf: u8 *
  - rx_cmd_buf: u16 *
  - dma_len: unsigned int
  - tx_burst_num: unsigned int
  - rx_burst_num: unsigned int
  - dma_msg_flag: unsigned long
  - phy_addr: resource_size_t
  - dma_tx_addr: dma_addr_t
  - dma_addr: dma_addr_t
  - dma_data_dir: dma_data_direction
  - dma_transfer_dir: dma_transfer_direction
  - chan_tx: dma_chan *
  - chan_rx: dma_chan *
  - adapter: i2c_adapter
  - num_clks: int
  - clks: clk_bulk_data *
  - base: void __iomem *
  - rx_buf: __u8 *
  - tx_buf: __u8 *
  - complete: completion
  - rate_per: unsigned long
  - msglen: unsigned int
  - delivered: unsigned int
  - block_data: unsigned int
  - bitrate: unsigned int
  - txfifosize: unsigned int
  - rxfifosize: unsigned int
  - mode: lpi2c_imx_mode
  - rinfo: i2c_bus_recovery_info
  - can_use_dma: bool
  - dma: lpi2c_imx_dma *
  - target: i2c_client *
  - irq: int
  - hwdata: const struct imx_lpi2c_hwdata *

### lpi2c_imx_struct
- Line: 177
- Members:
  - need_request_free_irq: bool
  - need_prepare_unprepare_clk: bool
  - using_pio_mode: bool
  - rx_cmd_buf_len: u8
  - dma_buf: u8 *
  - rx_cmd_buf: u16 *
  - dma_len: unsigned int
  - tx_burst_num: unsigned int
  - rx_burst_num: unsigned int
  - dma_msg_flag: unsigned long
  - phy_addr: resource_size_t
  - dma_tx_addr: dma_addr_t
  - dma_addr: dma_addr_t
  - dma_data_dir: dma_data_direction
  - dma_transfer_dir: dma_transfer_direction
  - chan_tx: dma_chan *
  - chan_rx: dma_chan *
  - adapter: i2c_adapter
  - num_clks: int
  - clks: clk_bulk_data *
  - base: void __iomem *
  - rx_buf: __u8 *
  - tx_buf: __u8 *
  - complete: completion
  - rate_per: unsigned long
  - msglen: unsigned int
  - delivered: unsigned int
  - block_data: unsigned int
  - bitrate: unsigned int
  - txfifosize: unsigned int
  - rxfifosize: unsigned int
  - mode: lpi2c_imx_mode
  - rinfo: i2c_bus_recovery_info
  - can_use_dma: bool
  - dma: lpi2c_imx_dma *
  - target: i2c_client *
  - irq: int
  - hwdata: const struct imx_lpi2c_hwdata *

## Enums (2)

### lpi2c_imx_mode
- Line: 139

### lpi2c_imx_pincfg
- Line: 147

## Variables (7)

- static **imx7ulp_lpi2c_hwdata** : const struct imx_lpi2c_hwdata (line 201)
- static **imx8qm_lpi2c_hwdata** : const struct imx_lpi2c_hwdata (line 209)
- static **imx8qxp_lpi2c_hwdata** : const struct imx_lpi2c_hwdata (line 204)
- static **lpi2c_imx_algo** : const struct i2c_algorithm (line 1444)
- static **lpi2c_imx_driver** : platform_driver (line 1701)
- static **lpi2c_imx_of_match** : const struct of_device_id[] (line 1452)
- static **lpi2c_pm_ops** : const struct dev_pm_ops (line 1693)

## Macros (100)

- **CHUNK_DATA** (line 133)
- **DRIVER_NAME** (line 30)
- **GEN_START** (line 67)
- **GEN_STOP** (line 65)
- **I2C_CLK_RATIO** (line 132)
- **I2C_DMA_THRESHOLD** (line 137)
- **I2C_PM_LONG_TIMEOUT_MS** (line 136)
- **I2C_PM_TIMEOUT** (line 135)
- **LPI2C_MCCR0** (line 41)
- **LPI2C_MCCR1** (line 42)
- **LPI2C_MCFGR0** (line 37)
- **LPI2C_MCFGR1** (line 38)
- **LPI2C_MCFGR2** (line 39)
- **LPI2C_MCFGR3** (line 40)
- **LPI2C_MCR** (line 33)
- **LPI2C_MDER** (line 36)
- **LPI2C_MFCR** (line 43)
- **LPI2C_MFSR** (line 44)
- **LPI2C_MIER** (line 35)
- **LPI2C_MRDR** (line 46)
- **LPI2C_MSR** (line 34)
- **LPI2C_MTDR** (line 45)
- **LPI2C_PARAM** (line 32)
- **LPI2C_SAMR** (line 55)
- **LPI2C_SASR** (line 56)
- **LPI2C_SCFGR0** (line 52)
- **LPI2C_SCFGR1** (line 53)
- **LPI2C_SCFGR2** (line 54)
- **LPI2C_SCR** (line 48)
- **LPI2C_SDER** (line 51)
- **LPI2C_SIER** (line 50)
- **LPI2C_SRDR** (line 59)
- **LPI2C_SRDROR** (line 60)
- **LPI2C_SSR** (line 49)
- **LPI2C_STAR** (line 57)
- **LPI2C_STDR** (line 58)
- **MCFGR1_AUTOSTOP** (line 89)
- **MCFGR1_IGNACK** (line 90)
- **MCR_DBGEN** (line 75)
- **MCR_DOZEN** (line 74)
- **MCR_MEN** (line 72)
- **MCR_RRF** (line 77)
- **MCR_RST** (line 73)
- **MCR_RTF** (line 76)
- **MDER_RDDE** (line 93)
- **MDER_TDDE** (line 92)
- **MIER_NDIE** (line 88)
- **MIER_RDIE** (line 86)
- **MIER_SDIE** (line 87)
- **MIER_TDIE** (line 85)
- **MRDR_RXEMPTY** (line 91)
- **MSR_ALF** (line 82)
- **MSR_BBF** (line 84)
- **MSR_MBF** (line 83)
- **MSR_NDF** (line 81)
- **MSR_RDF** (line 79)
- **MSR_RDF_ASSERTED**(x) (line 94)
- **MSR_SDF** (line 80)
- **MSR_TDF** (line 78)
- **RECV_DATA** (line 64)
- **RECV_DISCARD** (line 66)
- **SASR_READ_REQ** (line 128)
- **SCFGR1_RXSTALL** (line 121)
- **SCFGR1_TXDSTALL** (line 122)
- **SCFGR2_CLKHOLD**(x) (line 125)
- **SCFGR2_FILTSCL**(x) (line 127)
- **SCFGR2_FILTSCL_SHIFT** (line 124)
- **SCFGR2_FILTSDA**(x) (line 126)
- **SCFGR2_FILTSDA_SHIFT** (line 123)
- **SCR_FILTEN** (line 98)
- **SCR_RRF** (line 100)
- **SCR_RST** (line 97)
- **SCR_RTF** (line 99)
- **SCR_SEN** (line 96)
- **SIER_AM0F** (line 120)
- **SIER_AVIE** (line 114)
- **SIER_BEIE** (line 118)
- **SIER_FEIE** (line 119)
- **SIER_RDIE** (line 113)
- **SIER_RSIE** (line 116)
- **SIER_SDIE** (line 117)
- **SIER_TAIE** (line 115)
- **SIER_TDIE** (line 112)
- **SLAVE_INT_FLAG** (line 129)
- **SSR_AVF** (line 103)
- **SSR_BBF** (line 110)
- **SSR_BEF** (line 107)
- **SSR_CLEAR_BITS** (line 111)
- **SSR_FEF** (line 108)
- **SSR_RDF** (line 102)
- **SSR_RSF** (line 105)
- **SSR_SBF** (line 109)
- **SSR_SDF** (line 106)
- **SSR_TAF** (line 104)
- **SSR_TDF** (line 101)
- **START_HIGH** (line 69)
- **START_HIGH_NACK** (line 70)
- **START_NACK** (line 68)
- **TRAN_DATA** (line 63)
- **lpi2c_imx_read_msr_poll_timeout**(atomic,val,cond) (line 214)
