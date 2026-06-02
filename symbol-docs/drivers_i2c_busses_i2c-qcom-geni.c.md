# drivers/i2c/busses/i2c-qcom-geni.c

Subsystem: drivers/i2c

## Functions (30)

### geni_i2c_abort_xfer
- Return type: static void
- Signature: geni_i2c_abort_xfer(struct geni_i2c_dev * gi2c)
- Line: 367

### geni_i2c_clk_map_idx
- Return type: static int
- Signature: geni_i2c_clk_map_idx(struct geni_i2c_dev * gi2c)
- Line: 187

### geni_i2c_err
- Return type: static void
- Signature: geni_i2c_err(struct geni_i2c_dev * gi2c,int err)
- Line: 244

### geni_i2c_err_misc
- Return type: static void
- Signature: geni_i2c_err_misc(struct geni_i2c_dev * gi2c)
- Line: 222

### geni_i2c_fifo_xfer
- Return type: static int
- Signature: geni_i2c_fifo_xfer(struct geni_i2c_dev * gi2c,struct i2c_msg msgs[],int num)
- Line: 884

### geni_i2c_func
- Return type: static u32
- Signature: geni_i2c_func(struct i2c_adapter * adap)
- Line: 938

### geni_i2c_gpi
- Return type: static int
- Signature: geni_i2c_gpi(struct geni_i2c_dev * gi2c,struct i2c_msg msgs[],struct dma_slave_config * config,dma_addr_t * dma_addr_p,void ** buf,unsigned int op,struct dma_chan * dma_chan)
- Line: 622

### geni_i2c_gpi_multi_desc_unmap
- Return type: static void
- Signature: geni_i2c_gpi_multi_desc_unmap(struct geni_i2c_dev * gi2c,struct i2c_msg msgs[],struct gpi_i2c_config * peripheral)
- Line: 563

### geni_i2c_gpi_multi_xfer_timeout_handler
- Return type: static int
- Signature: geni_i2c_gpi_multi_xfer_timeout_handler(struct device * dev,struct geni_i2c_gpi_multi_desc_xfer * multi_xfer,u32 transfer_timeout_msecs,struct completion * transfer_comp)
- Line: 599

### geni_i2c_gpi_unmap
- Return type: static void
- Signature: geni_i2c_gpi_unmap(struct geni_i2c_dev * gi2c,struct i2c_msg * msg,void * tx_buf,dma_addr_t tx_addr,void * rx_buf,dma_addr_t rx_addr)
- Line: 542

### geni_i2c_gpi_xfer
- Return type: static int
- Signature: geni_i2c_gpi_xfer(struct geni_i2c_dev * gi2c,struct i2c_msg msgs[],int num)
- Line: 766

### geni_i2c_irq
- Return type: static irqreturn_t
- Signature: geni_i2c_irq(int irq,void * dev)
- Line: 267

### geni_i2c_probe
- Return type: static int
- Signature: geni_i2c_probe(struct platform_device * pdev)
- Line: 994

### geni_i2c_remove
- Return type: static void
- Signature: geni_i2c_remove(struct platform_device * pdev)
- Line: 1176

### geni_i2c_resume_noirq
- Return type: static int __maybe_unused
- Signature: geni_i2c_resume_noirq(struct device * dev)
- Line: 1258

### geni_i2c_runtime_resume
- Return type: static int __maybe_unused
- Signature: geni_i2c_runtime_resume(struct device * dev)
- Line: 1213

### geni_i2c_runtime_suspend
- Return type: static int __maybe_unused
- Signature: geni_i2c_runtime_suspend(struct device * dev)
- Line: 1193

### geni_i2c_rx_fsm_rst
- Return type: static void
- Signature: geni_i2c_rx_fsm_rst(struct geni_i2c_dev * gi2c)
- Line: 387

### geni_i2c_rx_msg_cleanup
- Return type: static void
- Signature: geni_i2c_rx_msg_cleanup(struct geni_i2c_dev * gi2c,struct i2c_msg * cur)
- Line: 417

### geni_i2c_rx_one_msg
- Return type: static int
- Signature: geni_i2c_rx_one_msg(struct geni_i2c_dev * gi2c,struct i2c_msg * msg,u32 m_param)
- Line: 441

### geni_i2c_shutdown
- Return type: static void
- Signature: geni_i2c_shutdown(struct platform_device * pdev)
- Line: 1185

### geni_i2c_suspend_noirq
- Return type: static int __maybe_unused
- Signature: geni_i2c_suspend_noirq(struct device * dev)
- Line: 1243

### geni_i2c_tx_fsm_rst
- Return type: static void
- Signature: geni_i2c_tx_fsm_rst(struct geni_i2c_dev * gi2c)
- Line: 402

### geni_i2c_tx_msg_cleanup
- Return type: static void
- Signature: geni_i2c_tx_msg_cleanup(struct geni_i2c_dev * gi2c,struct i2c_msg * cur)
- Line: 429

### geni_i2c_tx_one_msg
- Return type: static int
- Signature: geni_i2c_tx_one_msg(struct geni_i2c_dev * gi2c,struct i2c_msg * msg,u32 m_param)
- Line: 480

### geni_i2c_xfer
- Return type: static int
- Signature: geni_i2c_xfer(struct i2c_adapter * adap,struct i2c_msg msgs[],int num)
- Line: 907

### i2c_gpi_cb_result
- Return type: static void
- Signature: i2c_gpi_cb_result(void * cb,const struct dmaengine_result * result)
- Line: 522

### qcom_geni_i2c_conf
- Return type: static void
- Signature: qcom_geni_i2c_conf(struct geni_i2c_dev * gi2c)
- Line: 206

### release_gpi_dma
- Return type: static void
- Signature: release_gpi_dma(struct geni_i2c_dev * gi2c)
- Line: 957

### setup_gpi_dma
- Return type: static int
- Signature: setup_gpi_dma(struct geni_i2c_dev * gi2c)
- Line: 966

## Structs (5)

### geni_i2c_clk_fld
- Line: 152
- Members:
  - msg_idx_cnt: u32
  - unmap_msg_cnt: u32
  - irq_cnt: u32
  - dma_buf: void **
  - dma_addr: dma_addr_t *
  - se: geni_se
  - tx_wm: u32
  - irq: int
  - err: int
  - adap: i2c_adapter
  - done: completion
  - cur: i2c_msg *
  - cur_wr: int
  - cur_rd: int
  - lock: spinlock_t
  - core_clk: clk *
  - clk_freq_out: u32
  - clk_fld: const struct geni_i2c_clk_fld *
  - suspended: int
  - dma_buf: void *
  - xfer_len: size_t
  - dma_addr: dma_addr_t
  - tx_c: dma_chan *
  - rx_c: dma_chan *
  - no_dma: bool
  - gpi_mode: bool
  - abort_done: bool
  - is_tx_multi_desc_xfer: bool
  - num_msgs: u32
  - i2c_multi_desc_config: geni_i2c_gpi_multi_desc_xfer
  - has_core_clk: bool
  - icc_ddr: char *
  - no_dma_support: bool
  - tx_fifo_depth: unsigned int
  - err: int
  - msg: const char *
  - clk_freq_out: u32
  - clk_div: u8
  - t_high_cnt: u8
  - t_low_cnt: u8
  - t_cycle_cnt: u8

### geni_i2c_desc
- Line: 127
- Members:
  - msg_idx_cnt: u32
  - unmap_msg_cnt: u32
  - irq_cnt: u32
  - dma_buf: void **
  - dma_addr: dma_addr_t *
  - se: geni_se
  - tx_wm: u32
  - irq: int
  - err: int
  - adap: i2c_adapter
  - done: completion
  - cur: i2c_msg *
  - cur_wr: int
  - cur_rd: int
  - lock: spinlock_t
  - core_clk: clk *
  - clk_freq_out: u32
  - clk_fld: const struct geni_i2c_clk_fld *
  - suspended: int
  - dma_buf: void *
  - xfer_len: size_t
  - dma_addr: dma_addr_t
  - tx_c: dma_chan *
  - rx_c: dma_chan *
  - no_dma: bool
  - gpi_mode: bool
  - abort_done: bool
  - is_tx_multi_desc_xfer: bool
  - num_msgs: u32
  - i2c_multi_desc_config: geni_i2c_gpi_multi_desc_xfer
  - has_core_clk: bool
  - icc_ddr: char *
  - no_dma_support: bool
  - tx_fifo_depth: unsigned int
  - err: int
  - msg: const char *
  - clk_freq_out: u32
  - clk_div: u8
  - t_high_cnt: u8
  - t_low_cnt: u8
  - t_cycle_cnt: u8

### geni_i2c_dev
- Line: 99
- Members:
  - msg_idx_cnt: u32
  - unmap_msg_cnt: u32
  - irq_cnt: u32
  - dma_buf: void **
  - dma_addr: dma_addr_t *
  - se: geni_se
  - tx_wm: u32
  - irq: int
  - err: int
  - adap: i2c_adapter
  - done: completion
  - cur: i2c_msg *
  - cur_wr: int
  - cur_rd: int
  - lock: spinlock_t
  - core_clk: clk *
  - clk_freq_out: u32
  - clk_fld: const struct geni_i2c_clk_fld *
  - suspended: int
  - dma_buf: void *
  - xfer_len: size_t
  - dma_addr: dma_addr_t
  - tx_c: dma_chan *
  - rx_c: dma_chan *
  - no_dma: bool
  - gpi_mode: bool
  - abort_done: bool
  - is_tx_multi_desc_xfer: bool
  - num_msgs: u32
  - i2c_multi_desc_config: geni_i2c_gpi_multi_desc_xfer
  - has_core_clk: bool
  - icc_ddr: char *
  - no_dma_support: bool
  - tx_fifo_depth: unsigned int
  - err: int
  - msg: const char *
  - clk_freq_out: u32
  - clk_div: u8
  - t_high_cnt: u8
  - t_low_cnt: u8
  - t_cycle_cnt: u8

### geni_i2c_err_log
- Line: 134
- Members:
  - msg_idx_cnt: u32
  - unmap_msg_cnt: u32
  - irq_cnt: u32
  - dma_buf: void **
  - dma_addr: dma_addr_t *
  - se: geni_se
  - tx_wm: u32
  - irq: int
  - err: int
  - adap: i2c_adapter
  - done: completion
  - cur: i2c_msg *
  - cur_wr: int
  - cur_rd: int
  - lock: spinlock_t
  - core_clk: clk *
  - clk_freq_out: u32
  - clk_fld: const struct geni_i2c_clk_fld *
  - suspended: int
  - dma_buf: void *
  - xfer_len: size_t
  - dma_addr: dma_addr_t
  - tx_c: dma_chan *
  - rx_c: dma_chan *
  - no_dma: bool
  - gpi_mode: bool
  - abort_done: bool
  - is_tx_multi_desc_xfer: bool
  - num_msgs: u32
  - i2c_multi_desc_config: geni_i2c_gpi_multi_desc_xfer
  - has_core_clk: bool
  - icc_ddr: char *
  - no_dma_support: bool
  - tx_fifo_depth: unsigned int
  - err: int
  - msg: const char *
  - clk_freq_out: u32
  - clk_div: u8
  - t_high_cnt: u8
  - t_low_cnt: u8
  - t_cycle_cnt: u8

### geni_i2c_gpi_multi_desc_xfer
- Line: 91
- Members:
  - msg_idx_cnt: u32
  - unmap_msg_cnt: u32
  - irq_cnt: u32
  - dma_buf: void **
  - dma_addr: dma_addr_t *
  - se: geni_se
  - tx_wm: u32
  - irq: int
  - err: int
  - adap: i2c_adapter
  - done: completion
  - cur: i2c_msg *
  - cur_wr: int
  - cur_rd: int
  - lock: spinlock_t
  - core_clk: clk *
  - clk_freq_out: u32
  - clk_fld: const struct geni_i2c_clk_fld *
  - suspended: int
  - dma_buf: void *
  - xfer_len: size_t
  - dma_addr: dma_addr_t
  - tx_c: dma_chan *
  - rx_c: dma_chan *
  - no_dma: bool
  - gpi_mode: bool
  - abort_done: bool
  - is_tx_multi_desc_xfer: bool
  - num_msgs: u32
  - i2c_multi_desc_config: geni_i2c_gpi_multi_desc_xfer
  - has_core_clk: bool
  - icc_ddr: char *
  - no_dma_support: bool
  - tx_fifo_depth: unsigned int
  - err: int
  - msg: const char *
  - clk_freq_out: u32
  - clk_div: u8
  - t_high_cnt: u8
  - t_low_cnt: u8
  - t_cycle_cnt: u8

## Enums (1)

### geni_i2c_err_code
- Line: 57

## Variables (9)

- static **geni_i2c_acpi_match** : const struct acpi_device_id[] (line 949)
- static **geni_i2c_algo** : const struct i2c_algorithm (line 943)
- static **geni_i2c_clk_map_19p2mhz** : const struct geni_i2c_clk_fld[] (line 172)
- static **geni_i2c_clk_map_32mhz** : const struct geni_i2c_clk_fld[] (line 180)
- static **geni_i2c_driver** : platform_driver (line 1286)
- static **geni_i2c_dt_match** : const struct of_device_id[] (line 1279)
- static **geni_i2c_pm_ops** : const struct dev_pm_ops (line 1266)
- static **gi2c_log** : const struct geni_i2c_err_log[] (line 139)
- static **i2c_master_hub** : const struct geni_i2c_desc (line 1272)

## Macros (35)

- **ABORT_TIMEOUT** (line 76)
- **BYPASS_ADDR_PHASE** (line 44)
- **CYCLE_COUNTER_MSK** (line 52)
- **DM_I2C_CB_ERR** (line 70)
- **HIGH_COUNTER_MSK** (line 48)
- **HIGH_COUNTER_SHFT** (line 49)
- **I2C_ADDR_ONLY** (line 33)
- **I2C_AUTO_SUSPEND_DELAY** (line 73)
- **I2C_BUS_CLEAR** (line 34)
- **I2C_PACK_RX** (line 55)
- **I2C_PACK_TX** (line 54)
- **I2C_READ** (line 31)
- **I2C_STOP_ON_BUS** (line 35)
- **I2C_WRITE** (line 30)
- **I2C_WRITE_READ** (line 32)
- **IGNORE_ADD_NACK** (line 42)
- **LOW_COUNTER_MSK** (line 50)
- **LOW_COUNTER_SHFT** (line 51)
- **PACKING_BYTES_PW** (line 74)
- **POST_COMMAND_DELAY** (line 41)
- **PRE_CMD_DELAY** (line 37)
- **QCOM_I2C_MIN_NUM_OF_MSGS_MULTI_DESC** (line 80)
- **READ_FINISHED_WITH_ACK** (line 43)
- **RST_TIMEOUT** (line 78)
- **SE_I2C_ABORT** (line 27)
- **SE_I2C_ERR** (line 25)
- **SE_I2C_RX_TRANS_LEN** (line 22)
- **SE_I2C_SCL_COUNTERS** (line 23)
- **SE_I2C_TX_TRANS_LEN** (line 21)
- **SLV_ADDR_MSK** (line 45)
- **SLV_ADDR_SHFT** (line 46)
- **STOP_STRETCH** (line 39)
- **TIMESTAMP_AFTER** (line 40)
- **TIMESTAMP_BEFORE** (line 38)
- **XFER_TIMEOUT** (line 77)
