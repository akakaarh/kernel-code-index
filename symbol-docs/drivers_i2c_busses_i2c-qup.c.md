# drivers/i2c/busses/i2c-qup.c

Subsystem: drivers/i2c

## Functions (54)

### qup_i2c_bam_cb
- Return type: static void
- Signature: qup_i2c_bam_cb(void * data)
- Line: 617

### qup_i2c_bam_clear_tag_buffers
- Return type: static void
- Signature: qup_i2c_bam_clear_tag_buffers(struct qup_i2c_dev * qup)
- Line: 854

### qup_i2c_bam_make_desc
- Return type: static int
- Signature: qup_i2c_bam_make_desc(struct qup_i2c_dev * qup,struct i2c_msg * msg)
- Line: 675

### qup_i2c_bam_schedule_desc
- Return type: static int
- Signature: qup_i2c_bam_schedule_desc(struct qup_i2c_dev * qup)
- Line: 749

### qup_i2c_bam_xfer
- Return type: static int
- Signature: qup_i2c_bam_xfer(struct i2c_adapter * adap,struct i2c_msg * msg,int num)
- Line: 861

### qup_i2c_bus_active
- Return type: static int
- Signature: qup_i2c_bus_active(struct qup_i2c_dev * qup,int len)
- Line: 443

### qup_i2c_change_state
- Return type: static int
- Signature: qup_i2c_change_state(struct qup_i2c_dev * qup,u32 state)
- Line: 430

### qup_i2c_check_msg_len
- Return type: static bool
- Signature: qup_i2c_check_msg_len(struct i2c_msg * msg)
- Line: 542

### qup_i2c_clear_blk_v1
- Return type: static void
- Signature: qup_i2c_clear_blk_v1(struct qup_i2c_block * blk)
- Line: 1018

### qup_i2c_clear_blk_v2
- Return type: static void
- Signature: qup_i2c_clear_blk_v2(struct qup_i2c_block * blk)
- Line: 1205

### qup_i2c_conf_count_v2
- Return type: static void
- Signature: qup_i2c_conf_count_v2(struct qup_i2c_dev * qup)
- Line: 1151

### qup_i2c_conf_mode_v2
- Return type: static void
- Signature: qup_i2c_conf_mode_v2(struct qup_i2c_dev * qup)
- Line: 1182

### qup_i2c_conf_v1
- Return type: static void
- Signature: qup_i2c_conf_v1(struct qup_i2c_dev * qup)
- Line: 983

### qup_i2c_conf_xfer_v1
- Return type: static int
- Signature: qup_i2c_conf_xfer_v1(struct qup_i2c_dev * qup,bool is_rx)
- Line: 1025

### qup_i2c_conf_xfer_v2
- Return type: static int
- Signature: qup_i2c_conf_xfer_v2(struct qup_i2c_dev * qup,bool is_rx,bool is_first,bool change_pause_state)
- Line: 1372

### qup_i2c_determine_mode_v2
- Return type: static int
- Signature: qup_i2c_determine_mode_v2(struct qup_i2c_dev * qup,struct i2c_msg msgs[],int num)
- Line: 1531

### qup_i2c_disable_clocks
- Return type: static void
- Signature: qup_i2c_disable_clocks(struct qup_i2c_dev * qup)
- Line: 1666

### qup_i2c_enable_clocks
- Return type: static void
- Signature: qup_i2c_enable_clocks(struct qup_i2c_dev * qup)
- Line: 1660

### qup_i2c_flush
- Return type: static void
- Signature: qup_i2c_flush(struct qup_i2c_dev * qup)
- Line: 412

### qup_i2c_func
- Return type: static u32
- Signature: qup_i2c_func(struct i2c_adapter * adap)
- Line: 1631

### qup_i2c_get_data_len
- Return type: static int
- Signature: qup_i2c_get_data_len(struct qup_i2c_dev * qup)
- Line: 530

### qup_i2c_interrupt
- Return type: static irqreturn_t
- Signature: qup_i2c_interrupt(int irq,void * dev)
- Line: 288

### qup_i2c_pm_resume_runtime
- Return type: static int
- Signature: qup_i2c_pm_resume_runtime(struct device * device)
- Line: 1973

### qup_i2c_pm_suspend_runtime
- Return type: static int
- Signature: qup_i2c_pm_suspend_runtime(struct device * device)
- Line: 1964

### qup_i2c_poll_state
- Return type: static int
- Signature: qup_i2c_poll_state(struct qup_i2c_dev * qup,u32 req_state)
- Line: 407

### qup_i2c_poll_state_i2c_master
- Return type: static int
- Signature: qup_i2c_poll_state_i2c_master(struct qup_i2c_dev * qup)
- Line: 425

### qup_i2c_poll_state_mask
- Return type: static int
- Signature: qup_i2c_poll_state_mask(struct qup_i2c_dev * qup,u32 req_state,u32 req_mask)
- Line: 384

### qup_i2c_poll_state_valid
- Return type: static int
- Signature: qup_i2c_poll_state_valid(struct qup_i2c_dev * qup)
- Line: 420

### qup_i2c_probe
- Return type: static int
- Signature: qup_i2c_probe(struct platform_device * pdev)
- Line: 1685

### qup_i2c_read_one
- Return type: static int
- Signature: qup_i2c_read_one(struct qup_i2c_dev * qup)
- Line: 1080

### qup_i2c_read_rx_fifo_v1
- Return type: static void
- Signature: qup_i2c_read_rx_fifo_v1(struct qup_i2c_dev * qup)
- Line: 946

### qup_i2c_read_rx_fifo_v2
- Return type: static void
- Signature: qup_i2c_read_rx_fifo_v2(struct qup_i2c_dev * qup)
- Line: 1263

### qup_i2c_recv_data
- Return type: static void
- Signature: qup_i2c_recv_data(struct qup_i2c_dev * qup)
- Line: 1221

### qup_i2c_recv_tags
- Return type: static void
- Signature: qup_i2c_recv_tags(struct qup_i2c_dev * qup)
- Line: 1245

### qup_i2c_rel_dma
- Return type: static void
- Signature: qup_i2c_rel_dma(struct qup_i2c_dev * qup)
- Line: 638

### qup_i2c_remove
- Return type: static void
- Signature: qup_i2c_remove(struct platform_device * pdev)
- Line: 1948

### qup_i2c_req_dma
- Return type: static int
- Signature: qup_i2c_req_dma(struct qup_i2c_dev * qup)
- Line: 648

### qup_i2c_resume
- Return type: static int
- Signature: qup_i2c_resume(struct device * device)
- Line: 1989

### qup_i2c_set_blk_data
- Return type: static void
- Signature: qup_i2c_set_blk_data(struct qup_i2c_dev * qup,struct i2c_msg * msg)
- Line: 522

### qup_i2c_set_tags
- Return type: static int
- Signature: qup_i2c_set_tags(u8 * tags,struct qup_i2c_dev * qup,struct i2c_msg * msg)
- Line: 569

### qup_i2c_set_tags_smb
- Return type: static int
- Signature: qup_i2c_set_tags_smb(u16 addr,u8 * tags,struct qup_i2c_dev * qup,struct i2c_msg * msg)
- Line: 547

### qup_i2c_suspend
- Return type: static int
- Signature: qup_i2c_suspend(struct device * device)
- Line: 1982

### qup_i2c_vote_bw
- Return type: static int
- Signature: qup_i2c_vote_bw(struct qup_i2c_dev * qup,u32 clk_freq)
- Line: 466

### qup_i2c_wait_for_complete
- Return type: static int
- Signature: qup_i2c_wait_for_complete(struct qup_i2c_dev * qup,struct i2c_msg * msg)
- Line: 928

### qup_i2c_write_blk_data
- Return type: static void
- Signature: qup_i2c_write_blk_data(struct qup_i2c_dev * qup,u8 ** data,unsigned int * len)
- Line: 1283

### qup_i2c_write_one
- Return type: static int
- Signature: qup_i2c_write_one(struct qup_i2c_dev * qup)
- Line: 1068

### qup_i2c_write_rx_tags_v1
- Return type: static void
- Signature: qup_i2c_write_rx_tags_v1(struct qup_i2c_dev * qup)
- Line: 969

### qup_i2c_write_rx_tags_v2
- Return type: static void
- Signature: qup_i2c_write_rx_tags_v2(struct qup_i2c_dev * qup)
- Line: 1305

### qup_i2c_write_tx_fifo_v1
- Return type: static void
- Signature: qup_i2c_write_tx_fifo_v1(struct qup_i2c_dev * qup)
- Line: 483

### qup_i2c_write_tx_fifo_v2
- Return type: static void
- Signature: qup_i2c_write_tx_fifo_v2(struct qup_i2c_dev * qup)
- Line: 1336

### qup_i2c_xfer
- Return type: static int
- Signature: qup_i2c_xfer(struct i2c_adapter * adap,struct i2c_msg msgs[],int num)
- Line: 1091

### qup_i2c_xfer_v2
- Return type: static int
- Signature: qup_i2c_xfer_v2(struct i2c_adapter * adap,struct i2c_msg msgs[],int num)
- Line: 1566

### qup_i2c_xfer_v2_msg
- Return type: static int
- Signature: qup_i2c_xfer_v2_msg(struct qup_i2c_dev * qup,int msg_id,bool is_rx)
- Line: 1456

### qup_sg_set_buf
- Return type: static int
- Signature: qup_sg_set_buf(struct scatterlist * sg,void * buf,unsigned int buflen,struct qup_i2c_dev * qup,int dir)
- Line: 624

## Structs (4)

### qup_i2c_bam
- Line: 220
- Members:
  - count: int
  - pos: int
  - tx_tag_len: int
  - rx_tag_len: int
  - data_len: int
  - cur_blk_len: int
  - total_tx_len: int
  - total_rx_len: int
  - tx_fifo_data_pos: int
  - tx_fifo_free: int
  - rx_fifo_data_pos: int
  - fifo_available: int
  - tx_fifo_data: u32
  - rx_fifo_data: u32
  - cur_data: u8 *
  - cur_tx_tags: u8 *
  - tx_tags_sent: bool
  - send_last_word: bool
  - rx_tags_fetched: bool
  - rx_bytes_read: bool
  - is_tx_blk_mode: bool
  - is_rx_blk_mode: bool
  - tags: u8[6]
  - start: u8 *
  - addr: dma_addr_t
  - tag: qup_i2c_tag
  - dma: dma_chan *
  - sg: scatterlist *
  - sg_cnt: unsigned int
  - dev: device *
  - base: void __iomem *
  - irq: int
  - clk: clk *
  - pclk: clk *
  - icc_path: icc_path *
  - adap: i2c_adapter
  - clk_ctl: int
  - out_fifo_sz: int
  - in_fifo_sz: int
  - out_blk_sz: int
  - in_blk_sz: int
  - blk_xfer_limit: int
  - one_byte_t: unsigned long
  - xfer_timeout: unsigned long
  - blk: qup_i2c_block
  - msg: i2c_msg *
  - pos: int
  - bus_err: u32
  - qup_err: u32
  - is_last: bool
  - is_smbus_read: bool
  - config_run: u32
  - src_clk_freq: u32
  - cur_bw_clk_freq: u32
  - is_dma: bool
  - use_dma: bool
  - max_xfer_sg_len: unsigned int
  - tag_buf_pos: unsigned int
  - blk_mode_threshold: unsigned int
  - dpool: dma_pool *
  - start_tag: qup_i2c_tag
  - brx: qup_i2c_bam
  - btx: qup_i2c_bam
  - xfer: completion
  - write_tx_fifo: void (*)(struct qup_i2c_dev * qup)
  - read_rx_fifo: void (*)(struct qup_i2c_dev * qup)
  - write_rx_tags: void (*)(struct qup_i2c_dev * qup)

### qup_i2c_block
- Line: 189
- Members:
  - count: int
  - pos: int
  - tx_tag_len: int
  - rx_tag_len: int
  - data_len: int
  - cur_blk_len: int
  - total_tx_len: int
  - total_rx_len: int
  - tx_fifo_data_pos: int
  - tx_fifo_free: int
  - rx_fifo_data_pos: int
  - fifo_available: int
  - tx_fifo_data: u32
  - rx_fifo_data: u32
  - cur_data: u8 *
  - cur_tx_tags: u8 *
  - tx_tags_sent: bool
  - send_last_word: bool
  - rx_tags_fetched: bool
  - rx_bytes_read: bool
  - is_tx_blk_mode: bool
  - is_rx_blk_mode: bool
  - tags: u8[6]
  - start: u8 *
  - addr: dma_addr_t
  - tag: qup_i2c_tag
  - dma: dma_chan *
  - sg: scatterlist *
  - sg_cnt: unsigned int
  - dev: device *
  - base: void __iomem *
  - irq: int
  - clk: clk *
  - pclk: clk *
  - icc_path: icc_path *
  - adap: i2c_adapter
  - clk_ctl: int
  - out_fifo_sz: int
  - in_fifo_sz: int
  - out_blk_sz: int
  - in_blk_sz: int
  - blk_xfer_limit: int
  - one_byte_t: unsigned long
  - xfer_timeout: unsigned long
  - blk: qup_i2c_block
  - msg: i2c_msg *
  - pos: int
  - bus_err: u32
  - qup_err: u32
  - is_last: bool
  - is_smbus_read: bool
  - config_run: u32
  - src_clk_freq: u32
  - cur_bw_clk_freq: u32
  - is_dma: bool
  - use_dma: bool
  - max_xfer_sg_len: unsigned int
  - tag_buf_pos: unsigned int
  - blk_mode_threshold: unsigned int
  - dpool: dma_pool *
  - start_tag: qup_i2c_tag
  - brx: qup_i2c_bam
  - btx: qup_i2c_bam
  - xfer: completion
  - write_tx_fifo: void (*)(struct qup_i2c_dev * qup)
  - read_rx_fifo: void (*)(struct qup_i2c_dev * qup)
  - write_rx_tags: void (*)(struct qup_i2c_dev * qup)

### qup_i2c_dev
- Line: 227
- Members:
  - count: int
  - pos: int
  - tx_tag_len: int
  - rx_tag_len: int
  - data_len: int
  - cur_blk_len: int
  - total_tx_len: int
  - total_rx_len: int
  - tx_fifo_data_pos: int
  - tx_fifo_free: int
  - rx_fifo_data_pos: int
  - fifo_available: int
  - tx_fifo_data: u32
  - rx_fifo_data: u32
  - cur_data: u8 *
  - cur_tx_tags: u8 *
  - tx_tags_sent: bool
  - send_last_word: bool
  - rx_tags_fetched: bool
  - rx_bytes_read: bool
  - is_tx_blk_mode: bool
  - is_rx_blk_mode: bool
  - tags: u8[6]
  - start: u8 *
  - addr: dma_addr_t
  - tag: qup_i2c_tag
  - dma: dma_chan *
  - sg: scatterlist *
  - sg_cnt: unsigned int
  - dev: device *
  - base: void __iomem *
  - irq: int
  - clk: clk *
  - pclk: clk *
  - icc_path: icc_path *
  - adap: i2c_adapter
  - clk_ctl: int
  - out_fifo_sz: int
  - in_fifo_sz: int
  - out_blk_sz: int
  - in_blk_sz: int
  - blk_xfer_limit: int
  - one_byte_t: unsigned long
  - xfer_timeout: unsigned long
  - blk: qup_i2c_block
  - msg: i2c_msg *
  - pos: int
  - bus_err: u32
  - qup_err: u32
  - is_last: bool
  - is_smbus_read: bool
  - config_run: u32
  - src_clk_freq: u32
  - cur_bw_clk_freq: u32
  - is_dma: bool
  - use_dma: bool
  - max_xfer_sg_len: unsigned int
  - tag_buf_pos: unsigned int
  - blk_mode_threshold: unsigned int
  - dpool: dma_pool *
  - start_tag: qup_i2c_tag
  - brx: qup_i2c_bam
  - btx: qup_i2c_bam
  - xfer: completion
  - write_tx_fifo: void (*)(struct qup_i2c_dev * qup)
  - read_rx_fifo: void (*)(struct qup_i2c_dev * qup)
  - write_rx_tags: void (*)(struct qup_i2c_dev * qup)

### qup_i2c_tag
- Line: 215
- Members:
  - count: int
  - pos: int
  - tx_tag_len: int
  - rx_tag_len: int
  - data_len: int
  - cur_blk_len: int
  - total_tx_len: int
  - total_rx_len: int
  - tx_fifo_data_pos: int
  - tx_fifo_free: int
  - rx_fifo_data_pos: int
  - fifo_available: int
  - tx_fifo_data: u32
  - rx_fifo_data: u32
  - cur_data: u8 *
  - cur_tx_tags: u8 *
  - tx_tags_sent: bool
  - send_last_word: bool
  - rx_tags_fetched: bool
  - rx_bytes_read: bool
  - is_tx_blk_mode: bool
  - is_rx_blk_mode: bool
  - tags: u8[6]
  - start: u8 *
  - addr: dma_addr_t
  - tag: qup_i2c_tag
  - dma: dma_chan *
  - sg: scatterlist *
  - sg_cnt: unsigned int
  - dev: device *
  - base: void __iomem *
  - irq: int
  - clk: clk *
  - pclk: clk *
  - icc_path: icc_path *
  - adap: i2c_adapter
  - clk_ctl: int
  - out_fifo_sz: int
  - in_fifo_sz: int
  - out_blk_sz: int
  - in_blk_sz: int
  - blk_xfer_limit: int
  - one_byte_t: unsigned long
  - xfer_timeout: unsigned long
  - blk: qup_i2c_block
  - msg: i2c_msg *
  - pos: int
  - bus_err: u32
  - qup_err: u32
  - is_last: bool
  - is_smbus_read: bool
  - config_run: u32
  - src_clk_freq: u32
  - cur_bw_clk_freq: u32
  - is_dma: bool
  - use_dma: bool
  - max_xfer_sg_len: unsigned int
  - tag_buf_pos: unsigned int
  - blk_mode_threshold: unsigned int
  - dpool: dma_pool *
  - start_tag: qup_i2c_tag
  - brx: qup_i2c_bam
  - btx: qup_i2c_bam
  - xfer: completion
  - write_tx_fifo: void (*)(struct qup_i2c_dev * qup)
  - read_rx_fifo: void (*)(struct qup_i2c_dev * qup)
  - write_rx_tags: void (*)(struct qup_i2c_dev * qup)

## Variables (9)

- static **qup_i2c_acpi_match** : const struct acpi_device_id[] (line 1679)
- static **qup_i2c_algo** : const struct i2c_algorithm (line 1636)
- static **qup_i2c_algo_v2** : const struct i2c_algorithm (line 1641)
- static **qup_i2c_driver** : platform_driver (line 2010)
- static **qup_i2c_dt_match** : const struct of_device_id[] (line 2002)
- static **qup_i2c_quirks** : const struct i2c_adapter_quirks (line 1651)
- static **qup_i2c_quirks_v2** : const struct i2c_adapter_quirks (line 1656)
- static **qup_i2c_qup_pm_ops** : const struct dev_pm_ops (line 1996)
- static **scl_freq** : unsigned int (line 156)

## Macros (88)

- **DEFAULT_CLK_FREQ** (line 141)
- **DEFAULT_SRC_CLK** (line 142)
- **I2C_MINI_CORE** (line 74)
- **I2C_N_VAL** (line 75)
- **I2C_N_VAL_V2** (line 76)
- **I2C_STATUS_BUS_ACTIVE** (line 116)
- **I2C_STATUS_ERROR_MASK** (line 117)
- **I2C_STATUS_WR_BUFFER_FULL** (line 115)
- **IN_BLOCK_READ_REQ** (line 69)
- **MX_BLOCKS** (line 128)
- **MX_DMA_BLOCKS** (line 131)
- **MX_DMA_TX_RX_LEN** (line 130)
- **MX_TX_RX_LEN** (line 127)
- **ONE_BYTE** (line 123)
- **OUT_BLOCK_WRITE_REQ** (line 68)
- **QUP_BAM_FLUSH_STOP** (line 104)
- **QUP_BAM_INPUT_EOT** (line 103)
- **QUP_BAM_MODE** (line 86)
- **QUP_BUS_WIDTH** (line 154)
- **QUP_CLOCK_AUTO_GATE** (line 73)
- **QUP_CONFIG** (line 27)
- **QUP_ERROR_FLAGS** (line 32)
- **QUP_ERROR_FLAGS_EN** (line 33)
- **QUP_HW_VERSION** (line 35)
- **QUP_I2C_CLK_CTL** (line 42)
- **QUP_I2C_FLUSH** (line 54)
- **QUP_I2C_MASTER_GEN** (line 44)
- **QUP_I2C_MAST_GEN** (line 53)
- **QUP_I2C_MX_CONFIG_DURING_RUN** (line 124)
- **QUP_I2C_NACK_FLAG** (line 60)
- **QUP_I2C_STATUS** (line 43)
- **QUP_I2C_STATUS_RESET** (line 57)
- **QUP_INPUT_BAM_MODE** (line 85)
- **QUP_INPUT_BLK_MODE** (line 84)
- **QUP_INPUT_BLOCK_SIZE**(x) (line 95)
- **QUP_INPUT_FIFO_SIZE**(x) (line 96)
- **QUP_IN_FIFO_BASE** (line 41)
- **QUP_IN_NOT_EMPTY** (line 62)
- **QUP_IN_SVC_FLAG** (line 65)
- **QUP_IO_MODE** (line 29)
- **QUP_MAX_TAGS_LEN** (line 148)
- **QUP_MSW_SHIFT** (line 79)
- **QUP_MX_INPUT_CNT** (line 39)
- **QUP_MX_INPUT_DONE** (line 67)
- **QUP_MX_OUTPUT_CNT** (line 36)
- **QUP_MX_OUTPUT_DONE** (line 66)
- **QUP_MX_READ_CNT** (line 40)
- **QUP_MX_WRITE_CNT** (line 38)
- **QUP_NO_INPUT** (line 72)
- **QUP_OPERATIONAL** (line 31)
- **QUP_OPERATIONAL_MASK** (line 34)
- **QUP_OPERATIONAL_RESET** (line 56)
- **QUP_OUTPUT_BAM_MODE** (line 83)
- **QUP_OUTPUT_BLK_MODE** (line 82)
- **QUP_OUTPUT_BLOCK_SIZE**(x) (line 93)
- **QUP_OUTPUT_FIFO_SIZE**(x) (line 94)
- **QUP_OUT_FIFO_BASE** (line 37)
- **QUP_OUT_FULL** (line 63)
- **QUP_OUT_NOT_EMPTY** (line 61)
- **QUP_OUT_SVC_FLAG** (line 64)
- **QUP_PACK_EN** (line 88)
- **QUP_PAUSE_STATE** (line 49)
- **QUP_READ_LIMIT** (line 120)
- **QUP_REPACK_EN** (line 90)
- **QUP_RESET_STATE** (line 47)
- **QUP_RUN_STATE** (line 48)
- **QUP_STATE** (line 28)
- **QUP_STATE_MASK** (line 50)
- **QUP_STATE_VALID** (line 52)
- **QUP_STATUS_ERROR_FLAGS** (line 118)
- **QUP_SW_RESET** (line 30)
- **QUP_TAG_DATA** (line 100)
- **QUP_TAG_REC** (line 102)
- **QUP_TAG_START** (line 99)
- **QUP_TAG_STOP** (line 101)
- **QUP_TAG_V2_DATARD** (line 110)
- **QUP_TAG_V2_DATARD_NACK** (line 111)
- **QUP_TAG_V2_DATARD_STOP** (line 112)
- **QUP_TAG_V2_DATAWR** (line 108)
- **QUP_TAG_V2_DATAWR_STOP** (line 109)
- **QUP_TAG_V2_START** (line 107)
- **QUP_UNPACK_EN** (line 87)
- **QUP_V2_TAGS_EN** (line 91)
- **READ_RX_TAGS_LEN** (line 152)
- **RECV_MAX_DATA_LEN** (line 150)
- **RESET_BIT** (line 122)
- **SET_BIT** (line 121)
- **TOUT_MIN** (line 138)
