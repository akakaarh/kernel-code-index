# drivers/i2c/busses/i2c-stm32f7.c

Subsystem: drivers/i2c

## Functions (55)

### stm32f7_get_lower_rate
- Return type: static u32
- Signature: stm32f7_get_lower_rate(u32 rate)
- Line: 654

### stm32f7_get_specs
- Return type: static stm32f7_i2c_spec *
- Signature: stm32f7_get_specs(u32 rate)
- Line: 449

### stm32f7_i2c_clr_bits
- Return type: static void
- Signature: stm32f7_i2c_clr_bits(void __iomem * reg,u32 mask)
- Line: 439

### stm32f7_i2c_compute_timing
- Return type: static int
- Signature: stm32f7_i2c_compute_timing(struct stm32f7_i2c_dev * i2c_dev,struct stm32f7_i2c_setup * setup,struct stm32f7_i2c_timings * output)
- Line: 461

### stm32f7_i2c_disable_dma_req
- Return type: static void
- Signature: stm32f7_i2c_disable_dma_req(struct stm32f7_i2c_dev * i2c_dev)
- Line: 733

### stm32f7_i2c_disable_irq
- Return type: static void
- Signature: stm32f7_i2c_disable_irq(struct stm32f7_i2c_dev * i2c_dev,u32 mask)
- Line: 444

### stm32f7_i2c_disable_smbus_alert
- Return type: static void
- Signature: stm32f7_i2c_disable_smbus_alert(struct stm32f7_i2c_dev * i2c_dev)
- Line: 2124

### stm32f7_i2c_disable_smbus_host
- Return type: static void
- Signature: stm32f7_i2c_disable_smbus_host(struct stm32f7_i2c_dev * i2c_dev)
- Line: 2089

### stm32f7_i2c_dma_callback
- Return type: static void
- Signature: stm32f7_i2c_dma_callback(void * arg)
- Line: 741

### stm32f7_i2c_enable_smbus_alert
- Return type: static int
- Signature: stm32f7_i2c_enable_smbus_alert(struct stm32f7_i2c_dev * i2c_dev)
- Line: 2101

### stm32f7_i2c_enable_smbus_host
- Return type: static int
- Signature: stm32f7_i2c_enable_smbus_host(struct stm32f7_i2c_dev * i2c_dev)
- Line: 2071

### stm32f7_i2c_enable_wakeup
- Return type: static void
- Signature: stm32f7_i2c_enable_wakeup(struct stm32f7_i2c_dev * i2c_dev,bool enable)
- Line: 1876

### stm32f7_i2c_func
- Return type: static u32
- Signature: stm32f7_i2c_func(struct i2c_adapter * adap)
- Line: 2137

### stm32f7_i2c_get_free_slave_id
- Return type: static int
- Signature: stm32f7_i2c_get_free_slave_id(struct stm32f7_i2c_dev * i2c_dev,struct i2c_client * slave,int * id)
- Line: 1385

### stm32f7_i2c_get_slave_id
- Return type: static int
- Signature: stm32f7_i2c_get_slave_id(struct stm32f7_i2c_dev * i2c_dev,struct i2c_client * slave,int * id)
- Line: 1368

### stm32f7_i2c_handle_isr_errs
- Return type: static irqreturn_t
- Signature: stm32f7_i2c_handle_isr_errs(struct stm32f7_i2c_dev * i2c_dev,u32 status)
- Line: 1517

### stm32f7_i2c_hw_config
- Return type: static void
- Signature: stm32f7_i2c_hw_config(struct stm32f7_i2c_dev * i2c_dev)
- Line: 756

### stm32f7_i2c_is_addr_match
- Return type: static bool
- Signature: stm32f7_i2c_is_addr_match(struct i2c_client * slave,u32 addcode)
- Line: 1268

### stm32f7_i2c_is_slave_busy
- Return type: static bool
- Signature: stm32f7_i2c_is_slave_busy(struct stm32f7_i2c_dev * i2c_dev)
- Line: 1431

### stm32f7_i2c_is_slave_registered
- Return type: static bool
- Signature: stm32f7_i2c_is_slave_registered(struct stm32f7_i2c_dev * i2c_dev)
- Line: 1419

### stm32f7_i2c_isr_error_thread
- Return type: static irqreturn_t
- Signature: stm32f7_i2c_isr_error_thread(int irq,void * data)
- Line: 1682

### stm32f7_i2c_isr_event
- Return type: static irqreturn_t
- Signature: stm32f7_i2c_isr_event(int irq,void * data)
- Line: 1574

### stm32f7_i2c_isr_event_thread
- Return type: static irqreturn_t
- Signature: stm32f7_i2c_isr_event_thread(int irq,void * data)
- Line: 1606

### stm32f7_i2c_probe
- Return type: static int
- Signature: stm32f7_i2c_probe(struct platform_device * pdev)
- Line: 2163

### stm32f7_i2c_read_rx_data
- Return type: static void
- Signature: stm32f7_i2c_read_rx_data(struct stm32f7_i2c_dev * i2c_dev)
- Line: 798

### stm32f7_i2c_reg_slave
- Return type: static int
- Signature: stm32f7_i2c_reg_slave(struct i2c_client * slave)
- Line: 1894

### stm32f7_i2c_regs_backup
- Return type: static int __maybe_unused
- Signature: stm32f7_i2c_regs_backup(struct stm32f7_i2c_dev * i2c_dev)
- Line: 2419

### stm32f7_i2c_regs_restore
- Return type: static int __maybe_unused
- Signature: stm32f7_i2c_regs_restore(struct stm32f7_i2c_dev * i2c_dev)
- Line: 2440

### stm32f7_i2c_release_bus
- Return type: static void
- Signature: stm32f7_i2c_release_bus(struct i2c_adapter * i2c_adap)
- Line: 856

### stm32f7_i2c_reload
- Return type: static void
- Signature: stm32f7_i2c_reload(struct stm32f7_i2c_dev * i2c_dev)
- Line: 812

### stm32f7_i2c_remove
- Return type: static void
- Signature: stm32f7_i2c_remove(struct platform_device * pdev)
- Line: 2361

### stm32f7_i2c_resume
- Return type: static int __maybe_unused
- Signature: stm32f7_i2c_resume(struct device * dev)
- Line: 2492

### stm32f7_i2c_runtime_resume
- Return type: static int __maybe_unused
- Signature: stm32f7_i2c_runtime_resume(struct device * dev)
- Line: 2403

### stm32f7_i2c_runtime_suspend
- Return type: static int __maybe_unused
- Signature: stm32f7_i2c_runtime_suspend(struct device * dev)
- Line: 2393

### stm32f7_i2c_set_bits
- Return type: static void
- Signature: stm32f7_i2c_set_bits(void __iomem * reg,u32 mask)
- Line: 434

### stm32f7_i2c_setup_fm_plus_bits
- Return type: static int
- Signature: stm32f7_i2c_setup_fm_plus_bits(struct platform_device * pdev,struct stm32f7_i2c_dev * i2c_dev)
- Line: 2048

### stm32f7_i2c_setup_timing
- Return type: static int
- Signature: stm32f7_i2c_setup_timing(struct stm32f7_i2c_dev * i2c_dev,struct stm32f7_i2c_setup * setup)
- Line: 665

### stm32f7_i2c_slave_addr
- Return type: static void
- Signature: stm32f7_i2c_slave_addr(struct stm32f7_i2c_dev * i2c_dev)
- Line: 1342

### stm32f7_i2c_slave_isr_event
- Return type: static irqreturn_t
- Signature: stm32f7_i2c_slave_isr_event(struct stm32f7_i2c_dev * i2c_dev,u32 status)
- Line: 1444

### stm32f7_i2c_slave_start
- Return type: static void
- Signature: stm32f7_i2c_slave_start(struct stm32f7_i2c_dev * i2c_dev)
- Line: 1294

### stm32f7_i2c_smbus_check_pec
- Return type: static int
- Signature: stm32f7_i2c_smbus_check_pec(struct stm32f7_i2c_dev * i2c_dev)
- Line: 1233

### stm32f7_i2c_smbus_reload
- Return type: static void
- Signature: stm32f7_i2c_smbus_reload(struct stm32f7_i2c_dev * i2c_dev)
- Line: 833

### stm32f7_i2c_smbus_rep_start
- Return type: static void
- Signature: stm32f7_i2c_smbus_rep_start(struct stm32f7_i2c_dev * i2c_dev)
- Line: 1149

### stm32f7_i2c_smbus_xfer
- Return type: static int
- Signature: stm32f7_i2c_smbus_xfer(struct i2c_adapter * adapter,u16 addr,unsigned short flags,char read_write,u8 command,int size,union i2c_smbus_data * data)
- Line: 1787

### stm32f7_i2c_smbus_xfer_msg
- Return type: static int
- Signature: stm32f7_i2c_smbus_xfer_msg(struct stm32f7_i2c_dev * i2c_dev,unsigned short flags,u8 command,union i2c_smbus_data * data)
- Line: 980

### stm32f7_i2c_suspend
- Return type: static int __maybe_unused
- Signature: stm32f7_i2c_suspend(struct device * dev)
- Line: 2471

### stm32f7_i2c_unreg_slave
- Return type: static int
- Signature: stm32f7_i2c_unreg_slave(struct i2c_client * slave)
- Line: 1983

### stm32f7_i2c_wait_free_bus
- Return type: static int
- Signature: stm32f7_i2c_wait_free_bus(struct stm32f7_i2c_dev * i2c_dev)
- Line: 866

### stm32f7_i2c_wait_polling
- Return type: static int
- Signature: stm32f7_i2c_wait_polling(struct stm32f7_i2c_dev * i2c_dev)
- Line: 1692

### stm32f7_i2c_write_fm_plus_bits
- Return type: static int
- Signature: stm32f7_i2c_write_fm_plus_bits(struct stm32f7_i2c_dev * i2c_dev,bool enable)
- Line: 2020

### stm32f7_i2c_write_tx_data
- Return type: static void
- Signature: stm32f7_i2c_write_tx_data(struct stm32f7_i2c_dev * i2c_dev)
- Line: 787

### stm32f7_i2c_xfer
- Return type: static int
- Signature: stm32f7_i2c_xfer(struct i2c_adapter * i2c_adap,struct i2c_msg msgs[],int num)
- Line: 1769

### stm32f7_i2c_xfer_atomic
- Return type: static int
- Signature: stm32f7_i2c_xfer_atomic(struct i2c_adapter * i2c_adap,struct i2c_msg msgs[],int num)
- Line: 1778

### stm32f7_i2c_xfer_core
- Return type: static int
- Signature: stm32f7_i2c_xfer_core(struct i2c_adapter * i2c_adap,struct i2c_msg msgs[],int num)
- Line: 1707

### stm32f7_i2c_xfer_msg
- Return type: static void
- Signature: stm32f7_i2c_xfer_msg(struct stm32f7_i2c_dev * i2c_dev,struct i2c_msg * msg)
- Line: 883

## Structs (7)

### stm32f7_i2c_alert
- Line: 296
- Members:
  - cr1: u32
  - cr2: u32
  - oar1: u32
  - oar2: u32
  - tmgr: u32
  - rate: u32
  - fall_max: u32
  - rise_max: u32
  - hddat_min: u32
  - vddat_max: u32
  - sudat_min: u32
  - l_min: u32
  - h_min: u32
  - speed_freq: u32
  - clock_src: u32
  - rise_time: u32
  - fall_time: u32
  - fmp_clr_offset: u32
  - single_it_line: bool
  - fmp_cr1_bit: bool
  - node: list_head
  - presc: u8
  - scldel: u8
  - sdadel: u8
  - sclh: u8
  - scll: u8
  - addr: u16
  - count: u32
  - buf: u8 *
  - result: int
  - stop: bool
  - smbus: bool
  - size: int
  - read_write: char
  - smbus_buf: u8[I2C_SMBUS_BLOCK_MAX+3]__aligned (4)
  - setup: i2c_smbus_alert_setup
  - ara: i2c_client *
  - adap: i2c_adapter
  - dev: device *
  - base: void __iomem *
  - complete: completion
  - clk: clk *
  - bus_rate: unsigned int
  - msg: i2c_msg *
  - msg_num: unsigned int
  - msg_id: unsigned int
  - f7_msg: stm32f7_i2c_msg
  - setup: stm32f7_i2c_setup
  - timing: stm32f7_i2c_timings
  - slave: i2c_client * []
  - slave_running: i2c_client *
  - backup_regs: stm32f7_i2c_regs
  - slave_dir: u32
  - master_mode: bool
  - dma: stm32_i2c_dma *
  - use_dma: bool
  - regmap: regmap *
  - fmp_sreg: u32
  - fmp_creg: u32
  - fmp_mask: u32
  - wakeup_src: bool
  - smbus_mode: bool
  - host_notify_client: i2c_client *
  - analog_filter: bool
  - dnf_dt: u32
  - dnf: u32
  - alert: stm32f7_i2c_alert *
  - atomic: bool

### stm32f7_i2c_dev
- Line: 336
- Members:
  - cr1: u32
  - cr2: u32
  - oar1: u32
  - oar2: u32
  - tmgr: u32
  - rate: u32
  - fall_max: u32
  - rise_max: u32
  - hddat_min: u32
  - vddat_max: u32
  - sudat_min: u32
  - l_min: u32
  - h_min: u32
  - speed_freq: u32
  - clock_src: u32
  - rise_time: u32
  - fall_time: u32
  - fmp_clr_offset: u32
  - single_it_line: bool
  - fmp_cr1_bit: bool
  - node: list_head
  - presc: u8
  - scldel: u8
  - sdadel: u8
  - sclh: u8
  - scll: u8
  - addr: u16
  - count: u32
  - buf: u8 *
  - result: int
  - stop: bool
  - smbus: bool
  - size: int
  - read_write: char
  - smbus_buf: u8[I2C_SMBUS_BLOCK_MAX+3]__aligned (4)
  - setup: i2c_smbus_alert_setup
  - ara: i2c_client *
  - adap: i2c_adapter
  - dev: device *
  - base: void __iomem *
  - complete: completion
  - clk: clk *
  - bus_rate: unsigned int
  - msg: i2c_msg *
  - msg_num: unsigned int
  - msg_id: unsigned int
  - f7_msg: stm32f7_i2c_msg
  - setup: stm32f7_i2c_setup
  - timing: stm32f7_i2c_timings
  - slave: i2c_client * []
  - slave_running: i2c_client *
  - backup_regs: stm32f7_i2c_regs
  - slave_dir: u32
  - master_mode: bool
  - dma: stm32_i2c_dma *
  - use_dma: bool
  - regmap: regmap *
  - fmp_sreg: u32
  - fmp_creg: u32
  - fmp_mask: u32
  - wakeup_src: bool
  - smbus_mode: bool
  - host_notify_client: i2c_client *
  - analog_filter: bool
  - dnf_dt: u32
  - dnf: u32
  - alert: stm32f7_i2c_alert *
  - atomic: bool

### stm32f7_i2c_msg
- Line: 278
- Members:
  - cr1: u32
  - cr2: u32
  - oar1: u32
  - oar2: u32
  - tmgr: u32
  - rate: u32
  - fall_max: u32
  - rise_max: u32
  - hddat_min: u32
  - vddat_max: u32
  - sudat_min: u32
  - l_min: u32
  - h_min: u32
  - speed_freq: u32
  - clock_src: u32
  - rise_time: u32
  - fall_time: u32
  - fmp_clr_offset: u32
  - single_it_line: bool
  - fmp_cr1_bit: bool
  - node: list_head
  - presc: u8
  - scldel: u8
  - sdadel: u8
  - sclh: u8
  - scll: u8
  - addr: u16
  - count: u32
  - buf: u8 *
  - result: int
  - stop: bool
  - smbus: bool
  - size: int
  - read_write: char
  - smbus_buf: u8[I2C_SMBUS_BLOCK_MAX+3]__aligned (4)
  - setup: i2c_smbus_alert_setup
  - ara: i2c_client *
  - adap: i2c_adapter
  - dev: device *
  - base: void __iomem *
  - complete: completion
  - clk: clk *
  - bus_rate: unsigned int
  - msg: i2c_msg *
  - msg_num: unsigned int
  - msg_id: unsigned int
  - f7_msg: stm32f7_i2c_msg
  - setup: stm32f7_i2c_setup
  - timing: stm32f7_i2c_timings
  - slave: i2c_client * []
  - slave_running: i2c_client *
  - backup_regs: stm32f7_i2c_regs
  - slave_dir: u32
  - master_mode: bool
  - dma: stm32_i2c_dma *
  - use_dma: bool
  - regmap: regmap *
  - fmp_sreg: u32
  - fmp_creg: u32
  - fmp_mask: u32
  - wakeup_src: bool
  - smbus_mode: bool
  - host_notify_client: i2c_client *
  - analog_filter: bool
  - dnf_dt: u32
  - dnf: u32
  - alert: stm32f7_i2c_alert *
  - atomic: bool

### stm32f7_i2c_regs
- Line: 194
- Members:
  - cr1: u32
  - cr2: u32
  - oar1: u32
  - oar2: u32
  - tmgr: u32
  - rate: u32
  - fall_max: u32
  - rise_max: u32
  - hddat_min: u32
  - vddat_max: u32
  - sudat_min: u32
  - l_min: u32
  - h_min: u32
  - speed_freq: u32
  - clock_src: u32
  - rise_time: u32
  - fall_time: u32
  - fmp_clr_offset: u32
  - single_it_line: bool
  - fmp_cr1_bit: bool
  - node: list_head
  - presc: u8
  - scldel: u8
  - sdadel: u8
  - sclh: u8
  - scll: u8
  - addr: u16
  - count: u32
  - buf: u8 *
  - result: int
  - stop: bool
  - smbus: bool
  - size: int
  - read_write: char
  - smbus_buf: u8[I2C_SMBUS_BLOCK_MAX+3]__aligned (4)
  - setup: i2c_smbus_alert_setup
  - ara: i2c_client *
  - adap: i2c_adapter
  - dev: device *
  - base: void __iomem *
  - complete: completion
  - clk: clk *
  - bus_rate: unsigned int
  - msg: i2c_msg *
  - msg_num: unsigned int
  - msg_id: unsigned int
  - f7_msg: stm32f7_i2c_msg
  - setup: stm32f7_i2c_setup
  - timing: stm32f7_i2c_timings
  - slave: i2c_client * []
  - slave_running: i2c_client *
  - backup_regs: stm32f7_i2c_regs
  - slave_dir: u32
  - master_mode: bool
  - dma: stm32_i2c_dma *
  - use_dma: bool
  - regmap: regmap *
  - fmp_sreg: u32
  - fmp_creg: u32
  - fmp_mask: u32
  - wakeup_src: bool
  - smbus_mode: bool
  - host_notify_client: i2c_client *
  - analog_filter: bool
  - dnf_dt: u32
  - dnf: u32
  - alert: stm32f7_i2c_alert *
  - atomic: bool

### stm32f7_i2c_setup
- Line: 234
- Members:
  - cr1: u32
  - cr2: u32
  - oar1: u32
  - oar2: u32
  - tmgr: u32
  - rate: u32
  - fall_max: u32
  - rise_max: u32
  - hddat_min: u32
  - vddat_max: u32
  - sudat_min: u32
  - l_min: u32
  - h_min: u32
  - speed_freq: u32
  - clock_src: u32
  - rise_time: u32
  - fall_time: u32
  - fmp_clr_offset: u32
  - single_it_line: bool
  - fmp_cr1_bit: bool
  - node: list_head
  - presc: u8
  - scldel: u8
  - sdadel: u8
  - sclh: u8
  - scll: u8
  - addr: u16
  - count: u32
  - buf: u8 *
  - result: int
  - stop: bool
  - smbus: bool
  - size: int
  - read_write: char
  - smbus_buf: u8[I2C_SMBUS_BLOCK_MAX+3]__aligned (4)
  - setup: i2c_smbus_alert_setup
  - ara: i2c_client *
  - adap: i2c_adapter
  - dev: device *
  - base: void __iomem *
  - complete: completion
  - clk: clk *
  - bus_rate: unsigned int
  - msg: i2c_msg *
  - msg_num: unsigned int
  - msg_id: unsigned int
  - f7_msg: stm32f7_i2c_msg
  - setup: stm32f7_i2c_setup
  - timing: stm32f7_i2c_timings
  - slave: i2c_client * []
  - slave_running: i2c_client *
  - backup_regs: stm32f7_i2c_regs
  - slave_dir: u32
  - master_mode: bool
  - dma: stm32_i2c_dma *
  - use_dma: bool
  - regmap: regmap *
  - fmp_sreg: u32
  - fmp_creg: u32
  - fmp_mask: u32
  - wakeup_src: bool
  - smbus_mode: bool
  - host_notify_client: i2c_client *
  - analog_filter: bool
  - dnf_dt: u32
  - dnf: u32
  - alert: stm32f7_i2c_alert *
  - atomic: bool

### stm32f7_i2c_spec
- Line: 213
- Members:
  - cr1: u32
  - cr2: u32
  - oar1: u32
  - oar2: u32
  - tmgr: u32
  - rate: u32
  - fall_max: u32
  - rise_max: u32
  - hddat_min: u32
  - vddat_max: u32
  - sudat_min: u32
  - l_min: u32
  - h_min: u32
  - speed_freq: u32
  - clock_src: u32
  - rise_time: u32
  - fall_time: u32
  - fmp_clr_offset: u32
  - single_it_line: bool
  - fmp_cr1_bit: bool
  - node: list_head
  - presc: u8
  - scldel: u8
  - sdadel: u8
  - sclh: u8
  - scll: u8
  - addr: u16
  - count: u32
  - buf: u8 *
  - result: int
  - stop: bool
  - smbus: bool
  - size: int
  - read_write: char
  - smbus_buf: u8[I2C_SMBUS_BLOCK_MAX+3]__aligned (4)
  - setup: i2c_smbus_alert_setup
  - ara: i2c_client *
  - adap: i2c_adapter
  - dev: device *
  - base: void __iomem *
  - complete: completion
  - clk: clk *
  - bus_rate: unsigned int
  - msg: i2c_msg *
  - msg_num: unsigned int
  - msg_id: unsigned int
  - f7_msg: stm32f7_i2c_msg
  - setup: stm32f7_i2c_setup
  - timing: stm32f7_i2c_timings
  - slave: i2c_client * []
  - slave_running: i2c_client *
  - backup_regs: stm32f7_i2c_regs
  - slave_dir: u32
  - master_mode: bool
  - dma: stm32_i2c_dma *
  - use_dma: bool
  - regmap: regmap *
  - fmp_sreg: u32
  - fmp_creg: u32
  - fmp_mask: u32
  - wakeup_src: bool
  - smbus_mode: bool
  - host_notify_client: i2c_client *
  - analog_filter: bool
  - dnf_dt: u32
  - dnf: u32
  - alert: stm32f7_i2c_alert *
  - atomic: bool

### stm32f7_i2c_timings
- Line: 253
- Members:
  - cr1: u32
  - cr2: u32
  - oar1: u32
  - oar2: u32
  - tmgr: u32
  - rate: u32
  - fall_max: u32
  - rise_max: u32
  - hddat_min: u32
  - vddat_max: u32
  - sudat_min: u32
  - l_min: u32
  - h_min: u32
  - speed_freq: u32
  - clock_src: u32
  - rise_time: u32
  - fall_time: u32
  - fmp_clr_offset: u32
  - single_it_line: bool
  - fmp_cr1_bit: bool
  - node: list_head
  - presc: u8
  - scldel: u8
  - sdadel: u8
  - sclh: u8
  - scll: u8
  - addr: u16
  - count: u32
  - buf: u8 *
  - result: int
  - stop: bool
  - smbus: bool
  - size: int
  - read_write: char
  - smbus_buf: u8[I2C_SMBUS_BLOCK_MAX+3]__aligned (4)
  - setup: i2c_smbus_alert_setup
  - ara: i2c_client *
  - adap: i2c_adapter
  - dev: device *
  - base: void __iomem *
  - complete: completion
  - clk: clk *
  - bus_rate: unsigned int
  - msg: i2c_msg *
  - msg_num: unsigned int
  - msg_id: unsigned int
  - f7_msg: stm32f7_i2c_msg
  - setup: stm32f7_i2c_setup
  - timing: stm32f7_i2c_timings
  - slave: i2c_client * []
  - slave_running: i2c_client *
  - backup_regs: stm32f7_i2c_regs
  - slave_dir: u32
  - master_mode: bool
  - dma: stm32_i2c_dma *
  - use_dma: bool
  - regmap: regmap *
  - fmp_sreg: u32
  - fmp_creg: u32
  - fmp_mask: u32
  - wakeup_src: bool
  - smbus_mode: bool
  - host_notify_client: i2c_client *
  - analog_filter: bool
  - dnf_dt: u32
  - dnf: u32
  - alert: stm32f7_i2c_alert *
  - atomic: bool

## Enums (1)

### __anon4f012d800103
- Line: 162

## Variables (9)

- static **stm32f7_i2c_algo** : const struct i2c_algorithm (line 2154)
- static **stm32f7_i2c_driver** : platform_driver (line 2528)
- static **stm32f7_i2c_match** : const struct of_device_id[] (line 2519)
- static **stm32f7_i2c_pm_ops** : const struct dev_pm_ops (line 2513)
- static **stm32f7_i2c_specs** : stm32f7_i2c_spec[] (line 377)
- static **stm32f7_setup** : const struct stm32f7_i2c_setup (line 410)
- static **stm32mp13_setup** : const struct stm32f7_i2c_setup (line 421)
- static **stm32mp15_setup** : const struct stm32f7_i2c_setup (line 415)
- static **stm32mp25_setup** : const struct stm32f7_i2c_setup (line 427)

## Macros (102)

- **RATE_MIN**(rate) (line 460)
- **STM32F7_AUTOSUSPEND_DELAY** (line 184)
- **STM32F7_ERR_EVENTS** (line 1572)
- **STM32F7_I2C_ALL_IRQ_MASK** (line 73)
- **STM32F7_I2C_ANALOG_FILTER_DELAY_MAX** (line 173)
- **STM32F7_I2C_ANALOG_FILTER_DELAY_MIN** (line 172)
- **STM32F7_I2C_CR1** (line 42)
- **STM32F7_I2C_CR1_ADDRIE** (line 69)
- **STM32F7_I2C_CR1_ALERTEN** (line 56)
- **STM32F7_I2C_CR1_ANFOFF** (line 62)
- **STM32F7_I2C_CR1_DNF**(n) (line 64)
- **STM32F7_I2C_CR1_DNF_MASK** (line 63)
- **STM32F7_I2C_CR1_ERRIE** (line 65)
- **STM32F7_I2C_CR1_NACKIE** (line 68)
- **STM32F7_I2C_CR1_PE** (line 72)
- **STM32F7_I2C_CR1_PECEN** (line 55)
- **STM32F7_I2C_CR1_RXDMAEN** (line 60)
- **STM32F7_I2C_CR1_RXIE** (line 70)
- **STM32F7_I2C_CR1_SBC** (line 59)
- **STM32F7_I2C_CR1_SMBHEN** (line 57)
- **STM32F7_I2C_CR1_STOPIE** (line 67)
- **STM32F7_I2C_CR1_TCIE** (line 66)
- **STM32F7_I2C_CR1_TXDMAEN** (line 61)
- **STM32F7_I2C_CR1_TXIE** (line 71)
- **STM32F7_I2C_CR1_WUPEN** (line 58)
- **STM32F7_I2C_CR2** (line 43)
- **STM32F7_I2C_CR2_ADD10** (line 94)
- **STM32F7_I2C_CR2_HEAD10R** (line 93)
- **STM32F7_I2C_CR2_NACK** (line 90)
- **STM32F7_I2C_CR2_NBYTES**(n) (line 89)
- **STM32F7_I2C_CR2_NBYTES_MASK** (line 88)
- **STM32F7_I2C_CR2_PECBYTE** (line 86)
- **STM32F7_I2C_CR2_RD_WRN** (line 95)
- **STM32F7_I2C_CR2_RELOAD** (line 87)
- **STM32F7_I2C_CR2_SADD10**(n) (line 97)
- **STM32F7_I2C_CR2_SADD10_MASK** (line 96)
- **STM32F7_I2C_CR2_SADD7**(n) (line 100)
- **STM32F7_I2C_CR2_SADD7_MASK** (line 99)
- **STM32F7_I2C_CR2_START** (line 92)
- **STM32F7_I2C_CR2_STOP** (line 91)
- **STM32F7_I2C_DMA_LEN_MIN** (line 161)
- **STM32F7_I2C_DNF_DEFAULT** (line 169)
- **STM32F7_I2C_DNF_MAX** (line 170)
- **STM32F7_I2C_FALL_TIME_DEFAULT** (line 176)
- **STM32F7_I2C_ICR** (line 49)
- **STM32F7_I2C_ICR_ADDRCF** (line 151)
- **STM32F7_I2C_ICR_ALERTCF** (line 145)
- **STM32F7_I2C_ICR_ARLOCF** (line 147)
- **STM32F7_I2C_ICR_BERRCF** (line 148)
- **STM32F7_I2C_ICR_NACKCF** (line 150)
- **STM32F7_I2C_ICR_PECCF** (line 146)
- **STM32F7_I2C_ICR_STOPCF** (line 149)
- **STM32F7_I2C_ISR** (line 48)
- **STM32F7_I2C_ISR_ADDCODE_GET**(n) (line 127)
- **STM32F7_I2C_ISR_ADDCODE_MASK** (line 126)
- **STM32F7_I2C_ISR_ADDR** (line 139)
- **STM32F7_I2C_ISR_ALERT** (line 131)
- **STM32F7_I2C_ISR_ARLO** (line 133)
- **STM32F7_I2C_ISR_BERR** (line 134)
- **STM32F7_I2C_ISR_BUSY** (line 130)
- **STM32F7_I2C_ISR_DIR** (line 129)
- **STM32F7_I2C_ISR_NACKF** (line 138)
- **STM32F7_I2C_ISR_PECERR** (line 132)
- **STM32F7_I2C_ISR_RXNE** (line 140)
- **STM32F7_I2C_ISR_STOPF** (line 137)
- **STM32F7_I2C_ISR_TC** (line 136)
- **STM32F7_I2C_ISR_TCR** (line 135)
- **STM32F7_I2C_ISR_TXE** (line 142)
- **STM32F7_I2C_ISR_TXIS** (line 141)
- **STM32F7_I2C_MAX_LEN** (line 160)
- **STM32F7_I2C_OAR1** (line 44)
- **STM32F7_I2C_OAR1_MASK** (line 110)
- **STM32F7_I2C_OAR1_OA1EN** (line 103)
- **STM32F7_I2C_OAR1_OA1MODE** (line 104)
- **STM32F7_I2C_OAR1_OA1_10**(n) (line 106)
- **STM32F7_I2C_OAR1_OA1_10_MASK** (line 105)
- **STM32F7_I2C_OAR1_OA1_7**(n) (line 109)
- **STM32F7_I2C_OAR1_OA1_7_MASK** (line 108)
- **STM32F7_I2C_OAR2** (line 45)
- **STM32F7_I2C_OAR2_MASK** (line 121)
- **STM32F7_I2C_OAR2_OA2EN** (line 116)
- **STM32F7_I2C_OAR2_OA2MSK**(n) (line 118)
- **STM32F7_I2C_OAR2_OA2MSK_MASK** (line 117)
- **STM32F7_I2C_OAR2_OA2_7**(n) (line 120)
- **STM32F7_I2C_OAR2_OA2_7_MASK** (line 119)
- **STM32F7_I2C_PECR** (line 46)
- **STM32F7_I2C_RISE_TIME_DEFAULT** (line 175)
- **STM32F7_I2C_RXDR** (line 50)
- **STM32F7_I2C_TIMINGR** (line 47)
- **STM32F7_I2C_TIMINGR_PRESC**(n) (line 154)
- **STM32F7_I2C_TIMINGR_SCLDEL**(n) (line 155)
- **STM32F7_I2C_TIMINGR_SCLH**(n) (line 157)
- **STM32F7_I2C_TIMINGR_SCLL**(n) (line 158)
- **STM32F7_I2C_TIMINGR_SDADEL**(n) (line 156)
- **STM32F7_I2C_TXDR** (line 51)
- **STM32F7_I2C_XFER_IRQ_MASK** (line 79)
- **STM32F7_PRESC_MAX** (line 178)
- **STM32F7_SCLDEL_MAX** (line 179)
- **STM32F7_SCLH_MAX** (line 181)
- **STM32F7_SCLL_MAX** (line 182)
- **STM32F7_SDADEL_MAX** (line 180)
- **STM32_I2C_CR1_FMP** (line 54)
