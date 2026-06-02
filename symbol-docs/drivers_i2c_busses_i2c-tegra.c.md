# drivers/i2c/busses/i2c-tegra.c

Subsystem: drivers/i2c

## Functions (48)

### dvc_readl
- Return type: static u32
- Signature: dvc_readl(struct tegra_i2c_dev * i2c_dev,unsigned int reg)
- Line: 495

### dvc_writel
- Return type: static void
- Signature: dvc_writel(struct tegra_i2c_dev * i2c_dev,u32 val,unsigned int reg)
- Line: 489

### i2c_readl
- Return type: static u32
- Signature: i2c_readl(struct tegra_i2c_dev * i2c_dev,unsigned int reg)
- Line: 511

### i2c_readsl
- Return type: static void
- Signature: i2c_readsl(struct tegra_i2c_dev * i2c_dev,void * data,unsigned int reg,unsigned int len)
- Line: 537

### i2c_writel
- Return type: static void
- Signature: i2c_writel(struct tegra_i2c_dev * i2c_dev,u32 val,unsigned int reg)
- Line: 500

### i2c_writesl
- Return type: static void
- Signature: i2c_writesl(struct tegra_i2c_dev * i2c_dev,void * data,unsigned int reg,unsigned int len)
- Line: 516

### i2c_writesl_vi
- Return type: static void
- Signature: i2c_writesl_vi(struct tegra_i2c_dev * i2c_dev,void * data,unsigned int reg,unsigned int len)
- Line: 522

### tegra_dvc_init
- Return type: static void
- Signature: tegra_dvc_init(struct tegra_i2c_dev * i2c_dev)
- Line: 747

### tegra_i2c_config_fifo_trig
- Return type: static void
- Signature: tegra_i2c_config_fifo_trig(struct tegra_i2c_dev * i2c_dev,size_t len)
- Line: 1272

### tegra_i2c_disable_packet_mode
- Return type: static int
- Signature: tegra_i2c_disable_packet_mode(struct tegra_i2c_dev * i2c_dev)
- Line: 1013

### tegra_i2c_dma_complete
- Return type: static void
- Signature: tegra_i2c_dma_complete(void * args)
- Line: 626

### tegra_i2c_dma_submit
- Return type: static int
- Signature: tegra_i2c_dma_submit(struct tegra_i2c_dev * i2c_dev,size_t len)
- Line: 633

### tegra_i2c_empty_rx_fifo
- Return type: static int
- Signature: tegra_i2c_empty_rx_fifo(struct tegra_i2c_dev * i2c_dev)
- Line: 1032

### tegra_i2c_error_recover
- Return type: static int
- Signature: tegra_i2c_error_recover(struct tegra_i2c_dev * i2c_dev,struct i2c_msg * msg)
- Line: 1487

### tegra_i2c_fill_tx_fifo
- Return type: static int
- Signature: tegra_i2c_fill_tx_fifo(struct tegra_i2c_dev * i2c_dev)
- Line: 1092

### tegra_i2c_flush_fifos
- Return type: static int
- Signature: tegra_i2c_flush_fifos(struct tegra_i2c_dev * i2c_dev)
- Line: 805

### tegra_i2c_func
- Return type: static u32
- Signature: tegra_i2c_func(struct i2c_adapter * adap)
- Line: 1719

### tegra_i2c_init
- Return type: static int
- Signature: tegra_i2c_init(struct tegra_i2c_dev * i2c_dev)
- Line: 872

### tegra_i2c_init_clocks
- Return type: static int
- Signature: tegra_i2c_init_clocks(struct tegra_i2c_dev * i2c_dev)
- Line: 2179

### tegra_i2c_init_dma
- Return type: static int
- Signature: tegra_i2c_init_dma(struct tegra_i2c_dev * i2c_dev)
- Line: 676

### tegra_i2c_init_hardware
- Return type: static int
- Signature: tegra_i2c_init_hardware(struct tegra_i2c_dev * i2c_dev)
- Line: 2230

### tegra_i2c_isr
- Return type: static irqreturn_t
- Signature: tegra_i2c_isr(int irq,void * dev_id)
- Line: 1164

### tegra_i2c_issue_bus_clear
- Return type: static int
- Signature: tegra_i2c_issue_bus_clear(struct i2c_adapter * adap)
- Line: 1396

### tegra_i2c_mask_irq
- Return type: static void
- Signature: tegra_i2c_mask_irq(struct tegra_i2c_dev * i2c_dev,u32 mask)
- Line: 610

### tegra_i2c_master_reset
- Return type: static int
- Signature: tegra_i2c_master_reset(struct tegra_i2c_dev * i2c_dev)
- Line: 852

### tegra_i2c_mutex_acquired
- Return type: static bool
- Signature: tegra_i2c_mutex_acquired(struct tegra_i2c_dev * i2c_dev)
- Line: 543

### tegra_i2c_mutex_lock
- Return type: static int
- Signature: tegra_i2c_mutex_lock(struct tegra_i2c_dev * i2c_dev)
- Line: 570

### tegra_i2c_mutex_trylock
- Return type: static bool
- Signature: tegra_i2c_mutex_trylock(struct tegra_i2c_dev * i2c_dev)
- Line: 554

### tegra_i2c_mutex_unlock
- Return type: static void
- Signature: tegra_i2c_mutex_unlock(struct tegra_i2c_dev * i2c_dev)
- Line: 592

### tegra_i2c_parse_dt
- Return type: static void
- Signature: tegra_i2c_parse_dt(struct tegra_i2c_dev * i2c_dev)
- Line: 2169

### tegra_i2c_poll_completion
- Return type: static unsigned long
- Signature: tegra_i2c_poll_completion(struct tegra_i2c_dev * i2c_dev,struct completion * complete,unsigned int timeout_ms)
- Line: 1339

### tegra_i2c_poll_register
- Return type: static int
- Signature: tegra_i2c_poll_register(struct tegra_i2c_dev * i2c_dev,u32 reg,u32 mask,u32 delay_us,u32 timeout_us)
- Line: 790

### tegra_i2c_probe
- Return type: static int
- Signature: tegra_i2c_probe(struct platform_device * pdev)
- Line: 2245

### tegra_i2c_push_packet_header
- Return type: static void
- Signature: tegra_i2c_push_packet_header(struct tegra_i2c_dev * i2c_dev,struct i2c_msg * msg,enum msg_end_type end_state)
- Line: 1433

### tegra_i2c_release_clocks
- Return type: static void
- Signature: tegra_i2c_release_clocks(struct tegra_i2c_dev * i2c_dev)
- Line: 2222

### tegra_i2c_release_dma
- Return type: static void
- Signature: tegra_i2c_release_dma(struct tegra_i2c_dev * i2c_dev)
- Line: 662

### tegra_i2c_remove
- Return type: static void
- Signature: tegra_i2c_remove(struct platform_device * pdev)
- Line: 2351

### tegra_i2c_resume
- Return type: static int __maybe_unused
- Signature: tegra_i2c_resume(struct device * dev)
- Line: 2419

### tegra_i2c_runtime_resume
- Return type: static int __maybe_unused
- Signature: tegra_i2c_runtime_resume(struct device * dev)
- Line: 2362

### tegra_i2c_runtime_suspend
- Return type: static int __maybe_unused
- Signature: tegra_i2c_runtime_suspend(struct device * dev)
- Line: 2394

### tegra_i2c_suspend
- Return type: static int __maybe_unused
- Signature: tegra_i2c_suspend(struct device * dev)
- Line: 2403

### tegra_i2c_unmask_irq
- Return type: static void
- Signature: tegra_i2c_unmask_irq(struct tegra_i2c_dev * i2c_dev,u32 mask)
- Line: 618

### tegra_i2c_vi_init
- Return type: static void
- Signature: tegra_i2c_vi_init(struct tegra_i2c_dev * i2c_dev)
- Line: 761

### tegra_i2c_wait_completion
- Return type: static unsigned long
- Signature: tegra_i2c_wait_completion(struct tegra_i2c_dev * i2c_dev,struct completion * complete,unsigned int timeout_ms)
- Line: 1365

### tegra_i2c_wait_for_config_load
- Return type: static int
- Signature: tegra_i2c_wait_for_config_load(struct tegra_i2c_dev * i2c_dev)
- Line: 833

### tegra_i2c_xfer
- Return type: static int
- Signature: tegra_i2c_xfer(struct i2c_adapter * adap,struct i2c_msg msgs[],int num)
- Line: 1652

### tegra_i2c_xfer_atomic
- Return type: static int
- Signature: tegra_i2c_xfer_atomic(struct i2c_adapter * adap,struct i2c_msg msgs[],int num)
- Line: 1706

### tegra_i2c_xfer_msg
- Return type: static int
- Signature: tegra_i2c_xfer_msg(struct tegra_i2c_dev * i2c_dev,struct i2c_msg * msg,enum msg_end_type end_state)
- Line: 1513

## Structs (3)

### tegra_i2c_dev
- Line: 448
- Members:
  - cnfg: unsigned int
  - status: unsigned int
  - sl_cnfg: unsigned int
  - sl_addr1: unsigned int
  - sl_addr2: unsigned int
  - tlow_sext: unsigned int
  - tx_fifo: unsigned int
  - rx_fifo: unsigned int
  - packet_transfer_status: unsigned int
  - fifo_control: unsigned int
  - fifo_status: unsigned int
  - int_mask: unsigned int
  - int_status: unsigned int
  - clk_divisor: unsigned int
  - bus_clear_cnfg: unsigned int
  - bus_clear_status: unsigned int
  - config_load: unsigned int
  - clken_override: unsigned int
  - interface_timing_0: unsigned int
  - interface_timing_1: unsigned int
  - hs_interface_timing_0: unsigned int
  - hs_interface_timing_1: unsigned int
  - master_reset_cntrl: unsigned int
  - mst_fifo_control: unsigned int
  - mst_fifo_status: unsigned int
  - sw_mutex: unsigned int
  - has_continue_xfer_support: bool
  - has_per_pkt_xfer_complete_irq: bool
  - has_config_load_reg: bool
  - clk_divisor_hs_mode: u32
  - clk_divisor_std_mode: u32
  - clk_divisor_fast_mode: u32
  - clk_divisor_fast_plus_mode: u32
  - has_multi_master_mode: bool
  - has_slcg_override_reg: bool
  - has_mst_fifo: bool
  - has_mst_reset: bool
  - quirks: const struct i2c_adapter_quirks *
  - supports_bus_clear: bool
  - has_apb_dma: bool
  - tlow_std_mode: u32
  - thigh_std_mode: u32
  - tlow_fast_mode: u32
  - thigh_fast_mode: u32
  - tlow_fastplus_mode: u32
  - thigh_fastplus_mode: u32
  - tlow_hs_mode: u32
  - thigh_hs_mode: u32
  - setup_hold_time_std_mode: u32
  - setup_hold_time_fast_mode: u32
  - setup_hold_time_fastplus_mode: u32
  - setup_hold_time_hs_mode: u32
  - has_interface_timing_reg: bool
  - enable_hs_mode_support: bool
  - has_mutex: bool
  - variant: tegra_i2c_variant
  - regs: const struct tegra_i2c_regs *
  - dev: device *
  - adapter: i2c_adapter
  - hw: const struct tegra_i2c_hw_feature *
  - cont_id: unsigned int
  - irq: unsigned int
  - base_phys: phys_addr_t
  - base: void __iomem *
  - clocks: clk_bulk_data[2]
  - nclocks: unsigned int
  - div_clk: clk *
  - timings: i2c_timings
  - msg_complete: completion
  - msg_buf_remaining: size_t
  - msg_len: unsigned int
  - msg_err: int
  - msg_buf: u8 *
  - dma_complete: completion
  - dma_chan: dma_chan *
  - dma_buf_size: unsigned int
  - dma_dev: device *
  - dma_phys: dma_addr_t
  - dma_buf: void *
  - multimaster_mode: bool
  - atomic_mode: bool
  - dma_mode: bool
  - msg_read: bool

### tegra_i2c_hw_feature
- Line: 385
- Members:
  - cnfg: unsigned int
  - status: unsigned int
  - sl_cnfg: unsigned int
  - sl_addr1: unsigned int
  - sl_addr2: unsigned int
  - tlow_sext: unsigned int
  - tx_fifo: unsigned int
  - rx_fifo: unsigned int
  - packet_transfer_status: unsigned int
  - fifo_control: unsigned int
  - fifo_status: unsigned int
  - int_mask: unsigned int
  - int_status: unsigned int
  - clk_divisor: unsigned int
  - bus_clear_cnfg: unsigned int
  - bus_clear_status: unsigned int
  - config_load: unsigned int
  - clken_override: unsigned int
  - interface_timing_0: unsigned int
  - interface_timing_1: unsigned int
  - hs_interface_timing_0: unsigned int
  - hs_interface_timing_1: unsigned int
  - master_reset_cntrl: unsigned int
  - mst_fifo_control: unsigned int
  - mst_fifo_status: unsigned int
  - sw_mutex: unsigned int
  - has_continue_xfer_support: bool
  - has_per_pkt_xfer_complete_irq: bool
  - has_config_load_reg: bool
  - clk_divisor_hs_mode: u32
  - clk_divisor_std_mode: u32
  - clk_divisor_fast_mode: u32
  - clk_divisor_fast_plus_mode: u32
  - has_multi_master_mode: bool
  - has_slcg_override_reg: bool
  - has_mst_fifo: bool
  - has_mst_reset: bool
  - quirks: const struct i2c_adapter_quirks *
  - supports_bus_clear: bool
  - has_apb_dma: bool
  - tlow_std_mode: u32
  - thigh_std_mode: u32
  - tlow_fast_mode: u32
  - thigh_fast_mode: u32
  - tlow_fastplus_mode: u32
  - thigh_fastplus_mode: u32
  - tlow_hs_mode: u32
  - thigh_hs_mode: u32
  - setup_hold_time_std_mode: u32
  - setup_hold_time_fast_mode: u32
  - setup_hold_time_fastplus_mode: u32
  - setup_hold_time_hs_mode: u32
  - has_interface_timing_reg: bool
  - enable_hs_mode_support: bool
  - has_mutex: bool
  - variant: tegra_i2c_variant
  - regs: const struct tegra_i2c_regs *
  - dev: device *
  - adapter: i2c_adapter
  - hw: const struct tegra_i2c_hw_feature *
  - cont_id: unsigned int
  - irq: unsigned int
  - base_phys: phys_addr_t
  - base: void __iomem *
  - clocks: clk_bulk_data[2]
  - nclocks: unsigned int
  - div_clk: clk *
  - timings: i2c_timings
  - msg_complete: completion
  - msg_buf_remaining: size_t
  - msg_len: unsigned int
  - msg_err: int
  - msg_buf: u8 *
  - dma_complete: completion
  - dma_chan: dma_chan *
  - dma_buf_size: unsigned int
  - dma_dev: device *
  - dma_phys: dma_addr_t
  - dma_buf: void *
  - multimaster_mode: bool
  - atomic_mode: bool
  - dma_mode: bool
  - msg_read: bool

### tegra_i2c_regs
- Line: 141
- Members:
  - cnfg: unsigned int
  - status: unsigned int
  - sl_cnfg: unsigned int
  - sl_addr1: unsigned int
  - sl_addr2: unsigned int
  - tlow_sext: unsigned int
  - tx_fifo: unsigned int
  - rx_fifo: unsigned int
  - packet_transfer_status: unsigned int
  - fifo_control: unsigned int
  - fifo_status: unsigned int
  - int_mask: unsigned int
  - int_status: unsigned int
  - clk_divisor: unsigned int
  - bus_clear_cnfg: unsigned int
  - bus_clear_status: unsigned int
  - config_load: unsigned int
  - clken_override: unsigned int
  - interface_timing_0: unsigned int
  - interface_timing_1: unsigned int
  - hs_interface_timing_0: unsigned int
  - hs_interface_timing_1: unsigned int
  - master_reset_cntrl: unsigned int
  - mst_fifo_control: unsigned int
  - mst_fifo_status: unsigned int
  - sw_mutex: unsigned int
  - has_continue_xfer_support: bool
  - has_per_pkt_xfer_complete_irq: bool
  - has_config_load_reg: bool
  - clk_divisor_hs_mode: u32
  - clk_divisor_std_mode: u32
  - clk_divisor_fast_mode: u32
  - clk_divisor_fast_plus_mode: u32
  - has_multi_master_mode: bool
  - has_slcg_override_reg: bool
  - has_mst_fifo: bool
  - has_mst_reset: bool
  - quirks: const struct i2c_adapter_quirks *
  - supports_bus_clear: bool
  - has_apb_dma: bool
  - tlow_std_mode: u32
  - thigh_std_mode: u32
  - tlow_fast_mode: u32
  - thigh_fast_mode: u32
  - tlow_fastplus_mode: u32
  - thigh_fastplus_mode: u32
  - tlow_hs_mode: u32
  - thigh_hs_mode: u32
  - setup_hold_time_std_mode: u32
  - setup_hold_time_fast_mode: u32
  - setup_hold_time_fastplus_mode: u32
  - setup_hold_time_hs_mode: u32
  - has_interface_timing_reg: bool
  - enable_hs_mode_support: bool
  - has_mutex: bool
  - variant: tegra_i2c_variant
  - regs: const struct tegra_i2c_regs *
  - dev: device *
  - adapter: i2c_adapter
  - hw: const struct tegra_i2c_hw_feature *
  - cont_id: unsigned int
  - irq: unsigned int
  - base_phys: phys_addr_t
  - base: void __iomem *
  - clocks: clk_bulk_data[2]
  - nclocks: unsigned int
  - div_clk: clk *
  - timings: i2c_timings
  - msg_complete: completion
  - msg_buf_remaining: size_t
  - msg_len: unsigned int
  - msg_err: int
  - msg_buf: u8 *
  - dma_complete: completion
  - dma_chan: dma_chan *
  - dma_buf_size: unsigned int
  - dma_dev: device *
  - dma_phys: dma_addr_t
  - dma_buf: void *
  - multimaster_mode: bool
  - atomic_mode: bool
  - dma_mode: bool
  - msg_read: bool

## Enums (2)

### msg_end_type
- Line: 312

### tegra_i2c_variant
- Line: 324

## Variables (25)

- static **tegra114_i2c_hw** : const struct tegra_i2c_hw_feature (line 1851)
- static **tegra124_i2c_hw** : const struct tegra_i2c_hw_feature (line 1883)
- static **tegra186_i2c_hw** : const struct tegra_i2c_hw_feature (line 1981)
- static **tegra194_i2c_hw** : const struct tegra_i2c_hw_feature (line 2013)
- static **tegra194_i2c_quirks** : const struct i2c_adapter_quirks (line 1744)
- static **tegra20_dvc_i2c_hw** : const struct tegra_i2c_hw_feature (line 1786)
- static **tegra20_dvc_i2c_regs** : const struct tegra_i2c_regs (line 198)
- static **tegra20_i2c_hw** : const struct tegra_i2c_hw_feature (line 1753)
- static **tegra20_i2c_regs** : const struct tegra_i2c_regs (line 170)
- static **tegra210_i2c_hw** : const struct tegra_i2c_hw_feature (line 1915)
- static **tegra210_vi_i2c_hw** : const struct tegra_i2c_hw_feature (line 1948)
- static **tegra210_vi_i2c_regs** : const struct tegra_i2c_regs (line 224)
- static **tegra256_i2c_hw** : const struct tegra_i2c_hw_feature (line 2047)
- static **tegra264_i2c_hw** : const struct tegra_i2c_hw_feature (line 2081)
- static **tegra264_i2c_regs** : const struct tegra_i2c_regs (line 250)
- static **tegra30_i2c_hw** : const struct tegra_i2c_hw_feature (line 1819)
- static **tegra410_i2c_hw** : const struct tegra_i2c_hw_feature (line 2115)
- static **tegra410_i2c_regs** : const struct tegra_i2c_regs (line 278)
- static **tegra_i2c_acpi_match** : const struct acpi_device_id[] (line 2458)
- static **tegra_i2c_algo** : const struct i2c_algorithm (line 1731)
- static **tegra_i2c_driver** : platform_driver (line 2467)
- static **tegra_i2c_of_match** : const struct of_device_id[] (line 2149)
- static **tegra_i2c_pm** : const struct dev_pm_ops (line 2452)
- static **tegra_i2c_quirks** : const struct i2c_adapter_quirks (line 1738)
- static **tegra_i2c_recovery_info** : i2c_bus_recovery_info (line 1749)

## Macros (79)

- **BYTES_PER_FIFO_WORD** (line 31)
- **DVC_CTRL_REG1** (line 59)
- **DVC_CTRL_REG1_INTR_EN** (line 60)
- **DVC_CTRL_REG3** (line 61)
- **DVC_CTRL_REG3_I2C_DONE_INTR_EN** (line 63)
- **DVC_CTRL_REG3_SW_PROG** (line 62)
- **DVC_STATUS** (line 64)
- **DVC_STATUS_I2C_DONE_INTR** (line 65)
- **I2C_BC_ENABLE** (line 91)
- **I2C_BC_SCLK_THRESHOLD** (line 88)
- **I2C_BC_STATUS** (line 93)
- **I2C_BC_STOP_COND** (line 89)
- **I2C_BC_TERMINATE** (line 90)
- **I2C_CLK_DIVISOR_HSMODE** (line 57)
- **I2C_CLK_DIVISOR_STD_FAST_MODE** (line 56)
- **I2C_CNFG_DEBOUNCE_CNT** (line 33)
- **I2C_CNFG_MULTI_MASTER_MODE** (line 36)
- **I2C_CNFG_NEW_MASTER_FSM** (line 35)
- **I2C_CNFG_PACKET_MODE_EN** (line 34)
- **I2C_CONFIG_LOAD_TIMEOUT** (line 128)
- **I2C_ERR_ARBITRATION_LOST** (line 69)
- **I2C_ERR_NONE** (line 67)
- **I2C_ERR_NO_ACK** (line 68)
- **I2C_ERR_RX_BUFFER_OVERFLOW** (line 71)
- **I2C_ERR_UNKNOWN_INTERRUPT** (line 70)
- **I2C_FIFO_CONTROL_RX_FLUSH** (line 42)
- **I2C_FIFO_CONTROL_RX_TRIG**(x) (line 44)
- **I2C_FIFO_CONTROL_TX_FLUSH** (line 41)
- **I2C_FIFO_CONTROL_TX_TRIG**(x) (line 43)
- **I2C_FIFO_STATUS_RX** (line 47)
- **I2C_FIFO_STATUS_TX** (line 46)
- **I2C_HEADER_10BIT_ADDR** (line 82)
- **I2C_HEADER_CONTINUE_XFER** (line 85)
- **I2C_HEADER_CONT_ON_NAK** (line 80)
- **I2C_HEADER_HS_MODE** (line 79)
- **I2C_HEADER_IE_ENABLE** (line 83)
- **I2C_HEADER_READ** (line 81)
- **I2C_HEADER_REPEAT_START** (line 84)
- **I2C_HEADER_SLAVE_ADDR_SHIFT** (line 86)
- **I2C_HS_INTERFACE_TIMING_THD_STA** (line 109)
- **I2C_HS_INTERFACE_TIMING_THIGH** (line 106)
- **I2C_HS_INTERFACE_TIMING_TLOW** (line 107)
- **I2C_HS_INTERFACE_TIMING_TSU_STA** (line 110)
- **I2C_HS_INTERFACE_TIMING_TSU_STO** (line 108)
- **I2C_INTERFACE_TIMING_TBUF** (line 101)
- **I2C_INTERFACE_TIMING_THD_STA** (line 103)
- **I2C_INTERFACE_TIMING_THIGH** (line 99)
- **I2C_INTERFACE_TIMING_TLOW** (line 100)
- **I2C_INTERFACE_TIMING_TSU_STA** (line 104)
- **I2C_INTERFACE_TIMING_TSU_STO** (line 102)
- **I2C_INT_ARBITRATION_LOST** (line 52)
- **I2C_INT_BUS_CLR_DONE** (line 49)
- **I2C_INT_NO_ACK** (line 51)
- **I2C_INT_PACKET_XFER_COMPLETE** (line 50)
- **I2C_INT_RX_FIFO_DATA_REQ** (line 54)
- **I2C_INT_TX_FIFO_DATA_REQ** (line 53)
- **I2C_MSTR_CONFIG_LOAD** (line 95)
- **I2C_MST_CORE_CLKEN_OVR** (line 97)
- **I2C_MST_FIFO_CONTROL_RX_FLUSH** (line 112)
- **I2C_MST_FIFO_CONTROL_RX_TRIG**(x) (line 114)
- **I2C_MST_FIFO_CONTROL_TX_FLUSH** (line 113)
- **I2C_MST_FIFO_CONTROL_TX_TRIG**(x) (line 115)
- **I2C_MST_FIFO_STATUS_RX** (line 118)
- **I2C_MST_FIFO_STATUS_TX** (line 117)
- **I2C_PACKET_HEADER_SIZE** (line 131)
- **I2C_PIO_MODE_PREFERRED_LEN** (line 139)
- **I2C_SL_CNFG_NACK** (line 38)
- **I2C_SL_CNFG_NEWSL** (line 39)
- **I2C_SW_MUTEX_GRANT** (line 121)
- **I2C_SW_MUTEX_ID_CCPLEX** (line 122)
- **I2C_SW_MUTEX_REQUEST** (line 120)
- **I2C_SW_MUTEX_TIMEOUT_US** (line 125)
- **IS_DVC**(dev) (line 484)
- **IS_VI**(dev) (line 486)
- **PACKET_HEADER0_CONT_ID** (line 75)
- **PACKET_HEADER0_HEADER_SIZE** (line 73)
- **PACKET_HEADER0_PACKET_ID** (line 74)
- **PACKET_HEADER0_PROTOCOL** (line 76)
- **PACKET_HEADER0_PROTOCOL_I2C** (line 77)
