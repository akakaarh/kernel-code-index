# drivers/i2c/busses/i2c-npcm7xx.c

Subsystem: drivers/i2c

## Functions (67)

### __npcm_i2c_init
- Return type: static int
- Signature: __npcm_i2c_init(struct npcm_i2c * bus,struct platform_device * pdev)
- Line: 2191

### npcm_i2c_bus_irq
- Return type: static irqreturn_t
- Signature: npcm_i2c_bus_irq(int irq,void * dev_id)
- Line: 2220

### npcm_i2c_callback
- Return type: static void
- Signature: npcm_i2c_callback(struct npcm_i2c * bus,enum i2c_state_ind op_status,u16 info)
- Line: 953

### npcm_i2c_clear_fifo_int
- Return type: static void
- Signature: npcm_i2c_clear_fifo_int(struct npcm_i2c * bus)
- Line: 741

### npcm_i2c_clear_master_status
- Return type: static void
- Signature: npcm_i2c_clear_master_status(struct npcm_i2c * bus)
- Line: 842

### npcm_i2c_clear_rx_fifo
- Return type: static void
- Signature: npcm_i2c_clear_rx_fifo(struct npcm_i2c * bus)
- Line: 759

### npcm_i2c_clear_tx_fifo
- Return type: static void
- Signature: npcm_i2c_clear_tx_fifo(struct npcm_i2c * bus)
- Line: 750

### npcm_i2c_disable
- Return type: static void
- Signature: npcm_i2c_disable(struct npcm_i2c * bus)
- Line: 667

### npcm_i2c_enable
- Return type: static void
- Signature: npcm_i2c_enable(struct npcm_i2c * bus)
- Line: 687

### npcm_i2c_eob_int
- Return type: static void
- Signature: npcm_i2c_eob_int(struct npcm_i2c * bus,bool enable)
- Line: 697

### npcm_i2c_fifo_usage
- Return type: static u8
- Signature: npcm_i2c_fifo_usage(struct npcm_i2c * bus)
- Line: 1015

### npcm_i2c_functionality
- Return type: static u32
- Signature: npcm_i2c_functionality(struct i2c_adapter * adap)
- Line: 2457

### npcm_i2c_get_SCL
- Return type: static int
- Signature: npcm_i2c_get_SCL(struct i2c_adapter * _adap)
- Line: 638

### npcm_i2c_get_SDA
- Return type: static int
- Signature: npcm_i2c_get_SDA(struct i2c_adapter * _adap)
- Line: 645

### npcm_i2c_get_index
- Return type: static u16
- Signature: npcm_i2c_get_index(struct npcm_i2c * bus)
- Line: 652

### npcm_i2c_get_slave_addr
- Return type: static u8
- Signature: npcm_i2c_get_slave_addr(struct npcm_i2c * bus,enum i2c_addr addr_type)
- Line: 1116

### npcm_i2c_init_clk
- Return type: static int
- Signature: npcm_i2c_init_clk(struct npcm_i2c * bus,u32 bus_freq_hz)
- Line: 2067

### npcm_i2c_init_debugfs
- Return type: static void
- Signature: npcm_i2c_init_debugfs(struct platform_device * pdev,struct npcm_i2c * bus)
- Line: 2481

### npcm_i2c_init_module
- Return type: static int
- Signature: npcm_i2c_init_module(struct npcm_i2c * bus,enum i2c_mode mode,u32 bus_freq_hz)
- Line: 2133

### npcm_i2c_init_params
- Return type: static void
- Signature: npcm_i2c_init_params(struct npcm_i2c * bus)
- Line: 611

### npcm_i2c_int_enable
- Return type: static void
- Signature: npcm_i2c_int_enable(struct npcm_i2c * bus,bool enable)
- Line: 768

### npcm_i2c_int_master_handler
- Return type: static int
- Signature: npcm_i2c_int_master_handler(struct npcm_i2c * bus)
- Line: 1895

### npcm_i2c_int_slave_handler
- Return type: static irqreturn_t
- Signature: npcm_i2c_int_slave_handler(struct npcm_i2c * bus)
- Line: 1310

### npcm_i2c_irq_handle_ber
- Return type: static void
- Signature: npcm_i2c_irq_handle_ber(struct npcm_i2c * bus)
- Line: 1772

### npcm_i2c_irq_handle_eob
- Return type: static void
- Signature: npcm_i2c_irq_handle_eob(struct npcm_i2c * bus)
- Line: 1793

### npcm_i2c_irq_handle_nack
- Return type: static void
- Signature: npcm_i2c_irq_handle_nack(struct npcm_i2c * bus)
- Line: 1721

### npcm_i2c_irq_handle_nmatch
- Return type: static void
- Signature: npcm_i2c_irq_handle_nmatch(struct npcm_i2c * bus)
- Line: 1712

### npcm_i2c_irq_handle_sda
- Return type: static void
- Signature: npcm_i2c_irq_handle_sda(struct npcm_i2c * bus,u8 i2cst)
- Line: 1824

### npcm_i2c_irq_handle_stall_after_start
- Return type: static void
- Signature: npcm_i2c_irq_handle_stall_after_start(struct npcm_i2c * bus)
- Line: 1801

### npcm_i2c_irq_master_handler_read
- Return type: static void
- Signature: npcm_i2c_irq_master_handler_read(struct npcm_i2c * bus)
- Line: 1664

### npcm_i2c_irq_master_handler_write
- Return type: static void
- Signature: npcm_i2c_irq_master_handler_write(struct npcm_i2c * bus)
- Line: 1603

### npcm_i2c_is_master
- Return type: static bool
- Signature: npcm_i2c_is_master(struct npcm_i2c * bus)
- Line: 948

### npcm_i2c_is_quick
- Return type: static bool
- Signature: npcm_i2c_is_quick(struct npcm_i2c * bus)
- Line: 662

### npcm_i2c_master_abort
- Return type: static void
- Signature: npcm_i2c_master_abort(struct npcm_i2c * bus)
- Line: 1104

### npcm_i2c_master_fifo_read
- Return type: static void
- Signature: npcm_i2c_master_fifo_read(struct npcm_i2c * bus)
- Line: 1569

### npcm_i2c_master_start
- Return type: static void
- Signature: npcm_i2c_master_start(struct npcm_i2c * bus)
- Line: 781

### npcm_i2c_master_start_xmit
- Return type: static bool
- Signature: npcm_i2c_master_start_xmit(struct npcm_i2c * bus,u16 nwrite,u16 nread,u8 * write_data,u8 * read_data,bool use_PEC,bool use_read_block)
- Line: 2245

### npcm_i2c_master_stop
- Return type: static void
- Signature: npcm_i2c_master_stop(struct npcm_i2c * bus)
- Line: 791

### npcm_i2c_master_xfer
- Return type: static int
- Signature: npcm_i2c_master_xfer(struct i2c_adapter * adap,struct i2c_msg * msgs,int num)
- Line: 2288

### npcm_i2c_nack
- Return type: static void
- Signature: npcm_i2c_nack(struct npcm_i2c * bus)
- Line: 832

### npcm_i2c_probe_bus
- Return type: static int
- Signature: npcm_i2c_probe_bus(struct platform_device * pdev)
- Line: 2492

### npcm_i2c_rd_byte
- Return type: static u8
- Signature: npcm_i2c_rd_byte(struct npcm_i2c * bus)
- Line: 633

### npcm_i2c_read_fifo
- Return type: static void
- Signature: npcm_i2c_read_fifo(struct npcm_i2c * bus,u8 bytes_in_fifo)
- Line: 1093

### npcm_i2c_read_fifo_slave
- Return type: static void
- Signature: npcm_i2c_read_fifo_slave(struct npcm_i2c * bus,u8 bytes_in_fifo)
- Line: 1159

### npcm_i2c_recovery_init
- Return type: static void
- Signature: npcm_i2c_recovery_init(struct i2c_adapter * _adap)
- Line: 2035

### npcm_i2c_recovery_tgclk
- Return type: static int
- Signature: npcm_i2c_recovery_tgclk(struct i2c_adapter * _adap)
- Line: 1951

### npcm_i2c_reg_slave
- Return type: static int
- Signature: npcm_i2c_reg_slave(struct i2c_client * client)
- Line: 1518

### npcm_i2c_remove_bus
- Return type: static void
- Signature: npcm_i2c_remove_bus(struct platform_device * pdev)
- Line: 2588

### npcm_i2c_remove_slave_addr
- Return type: static int
- Signature: npcm_i2c_remove_slave_addr(struct npcm_i2c * bus,u8 slave_add)
- Line: 1124

### npcm_i2c_reset
- Return type: static void
- Signature: npcm_i2c_reset(struct npcm_i2c * bus)
- Line: 905

### npcm_i2c_rx_fifo_full
- Return type: static bool
- Signature: npcm_i2c_rx_fifo_full(struct npcm_i2c * bus)
- Line: 728

### npcm_i2c_select_bank
- Return type: static void
- Signature: npcm_i2c_select_bank(struct npcm_i2c * bus,enum i2c_bank bank)
- Line: 599

### npcm_i2c_set_fifo
- Return type: static void
- Signature: npcm_i2c_set_fifo(struct npcm_i2c * bus,int nread,int nwrite)
- Line: 1049

### npcm_i2c_slave_enable
- Return type: static int
- Signature: npcm_i2c_slave_enable(struct npcm_i2c * bus,enum i2c_addr addr_type,u8 addr,bool enable)
- Line: 866

### npcm_i2c_slave_get_wr_buf
- Return type: static int
- Signature: npcm_i2c_slave_get_wr_buf(struct npcm_i2c * bus)
- Line: 1179

### npcm_i2c_slave_int_enable
- Return type: static void
- Signature: npcm_i2c_slave_int_enable(struct npcm_i2c * bus,bool enable)
- Line: 852

### npcm_i2c_slave_rd_wr
- Return type: static void
- Signature: npcm_i2c_slave_rd_wr(struct npcm_i2c * bus)
- Line: 1284

### npcm_i2c_slave_receive
- Return type: static void
- Signature: npcm_i2c_slave_receive(struct npcm_i2c * bus,u16 nread,u8 * read_data)
- Line: 1226

### npcm_i2c_slave_send_rd_buf
- Return type: static void
- Signature: npcm_i2c_slave_send_rd_buf(struct npcm_i2c * bus)
- Line: 1203

### npcm_i2c_slave_wr_buf_sync
- Return type: static void
- Signature: npcm_i2c_slave_wr_buf_sync(struct npcm_i2c * bus)
- Line: 1264

### npcm_i2c_slave_xmit
- Return type: static void
- Signature: npcm_i2c_slave_xmit(struct npcm_i2c * bus,u16 nwrite,u8 * write_data)
- Line: 1240

### npcm_i2c_stall_after_start
- Return type: static void
- Signature: npcm_i2c_stall_after_start(struct npcm_i2c * bus,bool stall)
- Line: 819

### npcm_i2c_tx_fifo_empty
- Return type: static bool
- Signature: npcm_i2c_tx_fifo_empty(struct npcm_i2c * bus)
- Line: 715

### npcm_i2c_unreg_slave
- Return type: static int
- Signature: npcm_i2c_unreg_slave(struct i2c_client * client)
- Line: 1551

### npcm_i2c_wr_byte
- Return type: static void
- Signature: npcm_i2c_wr_byte(struct npcm_i2c * bus,u8 data)
- Line: 628

### npcm_i2c_write_fifo_slave
- Return type: static void
- Signature: npcm_i2c_write_fifo_slave(struct npcm_i2c * bus,u16 max_bytes)
- Line: 1139

### npcm_i2c_write_to_fifo_master
- Return type: static void
- Signature: npcm_i2c_write_to_fifo_master(struct npcm_i2c * bus,u16 max_bytes)
- Line: 1026

## Structs (3)

### npcm_i2c
- Line: 550
- Members:
  - core_clk: u32
  - hldt: u8
  - dbcnt: u8
  - sclfrq: u16
  - scllt: u8
  - sclht: u8
  - fast_mode: bool
  - fifo_size: u8
  - segctl_init_val: u32
  - txf_sts_tx_bytes: u8
  - rxf_sts_rx_bytes: u8
  - rxf_ctl_last_pec: u8
  - adap: i2c_adapter
  - dev: device *
  - reg: unsigned char __iomem *
  - data: const struct npcm_i2c_data *
  - lock: spinlock_t
  - cmd_complete: completion
  - cmd_err: int
  - msgs: i2c_msg *
  - msgs_num: int
  - num: int
  - apb_clk: u32
  - rinfo: i2c_bus_recovery_info
  - state: i2c_state
  - operation: i2c_oper
  - master_or_slave: i2c_mode
  - stop_ind: i2c_state_ind
  - dest_addr: u8
  - rd_buf: u8 *
  - rd_size: u16
  - rd_ind: u16
  - wr_buf: u8 *
  - wr_size: u16
  - wr_ind: u16
  - fifo_use: bool
  - PEC_mask: u16
  - PEC_use: bool
  - read_block_use: bool
  - int_time_stamp: unsigned long
  - bus_freq: unsigned long
  - own_slave_addr: u8
  - slave: i2c_client *
  - slv_rd_size: int
  - slv_rd_ind: int
  - slv_wr_size: int
  - slv_wr_ind: int
  - slv_rd_buf: u8[]
  - slv_wr_buf: u8[]
  - ber_cnt: u64
  - rec_succ_cnt: u64
  - rec_fail_cnt: u64
  - nack_cnt: u64
  - timeout_cnt: u64
  - tx_complete_cnt: u64
  - ber_state: bool

### npcm_i2c_data
- Line: 525
- Members:
  - core_clk: u32
  - hldt: u8
  - dbcnt: u8
  - sclfrq: u16
  - scllt: u8
  - sclht: u8
  - fast_mode: bool
  - fifo_size: u8
  - segctl_init_val: u32
  - txf_sts_tx_bytes: u8
  - rxf_sts_rx_bytes: u8
  - rxf_ctl_last_pec: u8
  - adap: i2c_adapter
  - dev: device *
  - reg: unsigned char __iomem *
  - data: const struct npcm_i2c_data *
  - lock: spinlock_t
  - cmd_complete: completion
  - cmd_err: int
  - msgs: i2c_msg *
  - msgs_num: int
  - num: int
  - apb_clk: u32
  - rinfo: i2c_bus_recovery_info
  - state: i2c_state
  - operation: i2c_oper
  - master_or_slave: i2c_mode
  - stop_ind: i2c_state_ind
  - dest_addr: u8
  - rd_buf: u8 *
  - rd_size: u16
  - rd_ind: u16
  - wr_buf: u8 *
  - wr_size: u16
  - wr_ind: u16
  - fifo_use: bool
  - PEC_mask: u16
  - PEC_use: bool
  - read_block_use: bool
  - int_time_stamp: unsigned long
  - bus_freq: unsigned long
  - own_slave_addr: u8
  - slave: i2c_client *
  - slv_rd_size: int
  - slv_rd_ind: int
  - slv_wr_size: int
  - slv_wr_ind: int
  - slv_rd_buf: u8[]
  - slv_wr_buf: u8[]
  - ber_cnt: u64
  - rec_succ_cnt: u64
  - rec_fail_cnt: u64
  - nack_cnt: u64
  - timeout_cnt: u64
  - tx_complete_cnt: u64
  - ber_state: bool

### smb_timing_t
- Line: 266
- Members:
  - core_clk: u32
  - hldt: u8
  - dbcnt: u8
  - sclfrq: u16
  - scllt: u8
  - sclht: u8
  - fast_mode: bool
  - fifo_size: u8
  - segctl_init_val: u32
  - txf_sts_tx_bytes: u8
  - rxf_sts_rx_bytes: u8
  - rxf_ctl_last_pec: u8
  - adap: i2c_adapter
  - dev: device *
  - reg: unsigned char __iomem *
  - data: const struct npcm_i2c_data *
  - lock: spinlock_t
  - cmd_complete: completion
  - cmd_err: int
  - msgs: i2c_msg *
  - msgs_num: int
  - num: int
  - apb_clk: u32
  - rinfo: i2c_bus_recovery_info
  - state: i2c_state
  - operation: i2c_oper
  - master_or_slave: i2c_mode
  - stop_ind: i2c_state_ind
  - dest_addr: u8
  - rd_buf: u8 *
  - rd_size: u16
  - rd_ind: u16
  - wr_buf: u8 *
  - wr_size: u16
  - wr_ind: u16
  - fifo_use: bool
  - PEC_mask: u16
  - PEC_use: bool
  - read_block_use: bool
  - int_time_stamp: unsigned long
  - bus_freq: unsigned long
  - own_slave_addr: u8
  - slave: i2c_client *
  - slv_rd_size: int
  - slv_rd_ind: int
  - slv_wr_size: int
  - slv_wr_ind: int
  - slv_rd_buf: u8[]
  - slv_wr_buf: u8[]
  - ber_cnt: u64
  - rec_succ_cnt: u64
  - rec_fail_cnt: u64
  - nack_cnt: u64
  - timeout_cnt: u64
  - tx_complete_cnt: u64
  - ber_state: bool

## Enums (6)

### i2c_addr
- Line: 76

### i2c_bank
- Line: 59

### i2c_mode
- Line: 23

### i2c_oper
- Line: 52

### i2c_state
- Line: 65

### i2c_state_ind
- Line: 32

## Variables (10)

- static **npcm_i2c_algo** : const struct i2c_algorithm (line 2472)
- static **npcm_i2c_bus_driver** : platform_driver (line 2606)
- static **npcm_i2c_bus_of_table** : const struct of_device_id[] (line 2599)
- static **npcm_i2c_quirks** : const struct i2c_adapter_quirks (line 2466)
- static **npcm_i2caddr** : const int[] (line 142)
- static **npxm7xx_i2c_data** : const struct npcm_i2c_data (line 533)
- static **npxm8xx_i2c_data** : const struct npcm_i2c_data (line 541)
- static **smb_timing_1000khz** : smb_timing_t[] (line 472)
- static **smb_timing_100khz** : smb_timing_t[] (line 276)
- static **smb_timing_400khz** : smb_timing_t[] (line 384)

## Macros (108)

- **DEFAULT_STALL_COUNT** (line 256)
- **I2CCTL2_ENABLE** (line 188)
- **I2CCTL2_SCLFRQ6_0** (line 189)
- **I2CCTL3_400K_MODE** (line 195)
- **I2CCTL3_ARPMEN** (line 193)
- **I2CCTL3_BNK_SEL** (line 196)
- **I2CCTL3_IDL_START** (line 194)
- **I2CCTL3_SCLFRQ8_7** (line 192)
- **I2CCTL3_SCL_LVL** (line 198)
- **I2CCTL3_SDA_LVL** (line 197)
- **I2CCTL4_HLDT** (line 217)
- **I2CCTL4_LVL_WE** (line 218)
- **I2CCTL5_DBNCT** (line 221)
- **I2C_FREQ_MAX_HZ** (line 264)
- **I2C_FREQ_MIN_HZ** (line 263)
- **I2C_NUM_OWN_ADDR** (line 139)
- **I2C_NUM_OWN_ADDR_SUPPORTED** (line 140)
- **I2C_VER** (line 106)
- **I2C_VER_FIFO_EN** (line 253)
- **I2C_VER_VERSION** (line 252)
- **MAX_I2C_HW_FIFO_SIZE** (line 249)
- **NPCM_I2CADDR1** (line 100)
- **NPCM_I2CADDR10** (line 116)
- **NPCM_I2CADDR2** (line 102)
- **NPCM_I2CADDR3** (line 109)
- **NPCM_I2CADDR4** (line 111)
- **NPCM_I2CADDR5** (line 113)
- **NPCM_I2CADDR6** (line 115)
- **NPCM_I2CADDR7** (line 110)
- **NPCM_I2CADDR8** (line 112)
- **NPCM_I2CADDR9** (line 114)
- **NPCM_I2CADDR_A** (line 184)
- **NPCM_I2CADDR_SAEN** (line 185)
- **NPCM_I2CCST** (line 98)
- **NPCM_I2CCST2** (line 104)
- **NPCM_I2CCST2_INTSTS** (line 208)
- **NPCM_I2CCST2_MATCHA1F** (line 201)
- **NPCM_I2CCST2_MATCHA2F** (line 202)
- **NPCM_I2CCST2_MATCHA3F** (line 203)
- **NPCM_I2CCST2_MATCHA4F** (line 204)
- **NPCM_I2CCST2_MATCHA5F** (line 205)
- **NPCM_I2CCST2_MATCHA6F** (line 206)
- **NPCM_I2CCST2_MATCHA7F** (line 207)
- **NPCM_I2CCST3** (line 105)
- **NPCM_I2CCST3_EO_BUSY** (line 214)
- **NPCM_I2CCST3_MATCHA10F** (line 213)
- **NPCM_I2CCST3_MATCHA8F** (line 211)
- **NPCM_I2CCST3_MATCHA9F** (line 212)
- **NPCM_I2CCST_ARPMATCH** (line 167)
- **NPCM_I2CCST_BB** (line 161)
- **NPCM_I2CCST_BUSY** (line 160)
- **NPCM_I2CCST_GCMATCH** (line 163)
- **NPCM_I2CCST_MATCH** (line 162)
- **NPCM_I2CCST_MATCHAF** (line 166)
- **NPCM_I2CCST_TGSCL** (line 165)
- **NPCM_I2CCST_TSDA** (line 164)
- **NPCM_I2CCTL1** (line 99)
- **NPCM_I2CCTL1_ACK** (line 174)
- **NPCM_I2CCTL1_EOBINTE** (line 173)
- **NPCM_I2CCTL1_GCMEN** (line 175)
- **NPCM_I2CCTL1_INTEN** (line 172)
- **NPCM_I2CCTL1_NMINTE** (line 176)
- **NPCM_I2CCTL1_RWS** (line 180)
- **NPCM_I2CCTL1_START** (line 170)
- **NPCM_I2CCTL1_STASTRE** (line 177)
- **NPCM_I2CCTL1_STOP** (line 171)
- **NPCM_I2CCTL2** (line 101)
- **NPCM_I2CCTL3** (line 103)
- **NPCM_I2CCTL4** (line 117)
- **NPCM_I2CCTL5** (line 118)
- **NPCM_I2CFIF_CTL** (line 120)
- **NPCM_I2CFIF_CTL_FIFO_EN** (line 244)
- **NPCM_I2CFIF_CTS** (line 124)
- **NPCM_I2CFIF_CTS_CLR_FIFO** (line 226)
- **NPCM_I2CFIF_CTS_RFTE_IE** (line 225)
- **NPCM_I2CFIF_CTS_RXF_TXE** (line 224)
- **NPCM_I2CFIF_CTS_SLVRSTR** (line 227)
- **NPCM_I2CPEC** (line 127)
- **NPCM_I2CRXF_CTL** (line 130)
- **NPCM_I2CRXF_CTL_THR_RXIE** (line 247)
- **NPCM_I2CRXF_STS** (line 129)
- **NPCM_I2CRXF_STS_RX_THST** (line 241)
- **NPCM_I2CSCLHT** (line 121)
- **NPCM_I2CSCLLT** (line 119)
- **NPCM_I2CSDA** (line 96)
- **NPCM_I2CSEGCTL** (line 93)
- **NPCM_I2CST** (line 97)
- **NPCM_I2CST_BER** (line 155)
- **NPCM_I2CST_MASTER** (line 151)
- **NPCM_I2CST_NEGACK** (line 154)
- **NPCM_I2CST_NMATCH** (line 152)
- **NPCM_I2CST_SDAST** (line 156)
- **NPCM_I2CST_SLVSTP** (line 157)
- **NPCM_I2CST_STASTR** (line 153)
- **NPCM_I2CST_XMIT** (line 150)
- **NPCM_I2CTXF_CTL** (line 125)
- **NPCM_I2CTXF_CTL_THR_TXIE** (line 230)
- **NPCM_I2CTXF_STS** (line 128)
- **NPCM_I2CTXF_STS_TX_THST** (line 238)
- **NPCM_I2CT_OUT** (line 126)
- **NPCM_I2CT_OUT_TO_CKDIV** (line 233)
- **NPCM_I2CT_OUT_T_OUTIE** (line 234)
- **NPCM_I2CT_OUT_T_OUTST** (line 235)
- **SCLFRQ_0_TO_6** (line 259)
- **SCLFRQ_7_TO_8** (line 260)
- **SCLFRQ_MAX** (line 2055)
- **SCLFRQ_MIN** (line 2054)
- **clk_coef**(freq,mul) (line 2056)
