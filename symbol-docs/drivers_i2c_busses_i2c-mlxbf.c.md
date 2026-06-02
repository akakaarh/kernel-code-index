# drivers/i2c/busses/i2c-mlxbf.c

Subsystem: drivers/i2c

## Functions (48)

### mlxbf_i2c_acpi_probe
- Return type: static int
- Signature: mlxbf_i2c_acpi_probe(struct device * dev,struct mlxbf_i2c_priv * priv)
- Line: 2207

### mlxbf_i2c_calculate_corepll_freq
- Return type: static int
- Signature: mlxbf_i2c_calculate_corepll_freq(struct platform_device * pdev,struct mlxbf_i2c_priv * priv)
- Line: 1490

### mlxbf_i2c_calculate_freq_from_tyu
- Return type: static u64
- Signature: mlxbf_i2c_calculate_freq_from_tyu(struct mlxbf_i2c_resource * corepll_res)
- Line: 1431

### mlxbf_i2c_calculate_freq_from_yu
- Return type: static u64
- Signature: mlxbf_i2c_calculate_freq_from_yu(struct mlxbf_i2c_resource * corepll_res)
- Line: 1460

### mlxbf_i2c_exit
- Return type: static void __exit
- Signature: mlxbf_i2c_exit(void)
- Line: 2432

### mlxbf_i2c_functionality
- Return type: static u32
- Signature: mlxbf_i2c_functionality(struct i2c_adapter * adap)
- Line: 2149

### mlxbf_i2c_get_corepll
- Return type: static int
- Signature: mlxbf_i2c_get_corepll(struct platform_device * pdev,struct mlxbf_i2c_priv * priv)
- Line: 1310

### mlxbf_i2c_get_gpio
- Return type: static int
- Signature: mlxbf_i2c_get_gpio(struct platform_device * pdev,struct mlxbf_i2c_priv * priv)
- Line: 1246

### mlxbf_i2c_get_shared_resource
- Return type: static mlxbf_i2c_resource *
- Signature: mlxbf_i2c_get_shared_resource(struct mlxbf_i2c_priv * priv,u8 type)
- Line: 1022

### mlxbf_i2c_get_slave_from_addr
- Return type: static i2c_client *
- Signature: mlxbf_i2c_get_slave_from_addr(struct mlxbf_i2c_priv * priv,u8 addr)
- Line: 1796

### mlxbf_i2c_get_ticks
- Return type: static u32
- Signature: mlxbf_i2c_get_ticks(struct mlxbf_i2c_priv * priv,u64 nanoseconds,bool minimum)
- Line: 1065

### mlxbf_i2c_has_chip_type
- Return type: static bool
- Signature: mlxbf_i2c_has_chip_type(struct mlxbf_i2c_priv * priv,u8 type)
- Line: 1016

### mlxbf_i2c_has_coalesce
- Return type: static bool
- Signature: mlxbf_i2c_has_coalesce(struct mlxbf_i2c_priv * priv,bool * read,bool * write)
- Line: 1763

### mlxbf_i2c_init
- Return type: static int __init
- Signature: mlxbf_i2c_init(void)
- Line: 2420

### mlxbf_i2c_init_coalesce
- Return type: static int
- Signature: mlxbf_i2c_init_coalesce(struct platform_device * pdev,struct mlxbf_i2c_priv * priv)
- Line: 1649

### mlxbf_i2c_init_master
- Return type: static int
- Signature: mlxbf_i2c_init_master(struct platform_device * pdev,struct mlxbf_i2c_priv * priv)
- Line: 1374

### mlxbf_i2c_init_resource
- Return type: static int
- Signature: mlxbf_i2c_init_resource(struct platform_device * pdev,struct mlxbf_i2c_resource ** res,u8 type)
- Line: 1037

### mlxbf_i2c_init_slave
- Return type: static int
- Signature: mlxbf_i2c_init_slave(struct platform_device * pdev,struct mlxbf_i2c_priv * priv)
- Line: 1728

### mlxbf_i2c_init_timings
- Return type: static int
- Signature: mlxbf_i2c_init_timings(struct platform_device * pdev,struct mlxbf_i2c_priv * priv)
- Line: 1209

### mlxbf_i2c_irq
- Return type: static irqreturn_t
- Signature: mlxbf_i2c_irq(int irq,void * ptr)
- Line: 1967

### mlxbf_i2c_irq_recv
- Return type: static int
- Signature: mlxbf_i2c_irq_recv(struct mlxbf_i2c_priv * priv,u8 recv_bytes)
- Line: 1915

### mlxbf_i2c_irq_send
- Return type: static int
- Signature: mlxbf_i2c_irq_send(struct mlxbf_i2c_priv * priv,u8 recv_bytes)
- Line: 1816

### mlxbf_i2c_probe
- Return type: static int
- Signature: mlxbf_i2c_probe(struct platform_device * pdev)
- Line: 2233

### mlxbf_i2c_reg_slave
- Return type: static int
- Signature: mlxbf_i2c_reg_slave(struct i2c_client * slave)
- Line: 2109

### mlxbf_i2c_release_coalesce
- Return type: static int
- Signature: mlxbf_i2c_release_coalesce(struct platform_device * pdev,struct mlxbf_i2c_priv * priv)
- Line: 1702

### mlxbf_i2c_release_corepll
- Return type: static int
- Signature: mlxbf_i2c_release_corepll(struct platform_device * pdev,struct mlxbf_i2c_priv * priv)
- Line: 1349

### mlxbf_i2c_release_gpio
- Return type: static int
- Signature: mlxbf_i2c_release_gpio(struct platform_device * pdev,struct mlxbf_i2c_priv * priv)
- Line: 1284

### mlxbf_i2c_remove
- Return type: static void
- Signature: mlxbf_i2c_remove(struct platform_device * pdev)
- Line: 2368

### mlxbf_i2c_set_timer
- Return type: static u32
- Signature: mlxbf_i2c_set_timer(struct mlxbf_i2c_priv * priv,u64 nsec,bool opt,u32 mask,u8 shift)
- Line: 1090

### mlxbf_i2c_set_timings
- Return type: static void
- Signature: mlxbf_i2c_set_timings(struct mlxbf_i2c_priv * priv,const struct mlxbf_i2c_timings * timings)
- Line: 1098

### mlxbf_i2c_slave_disable
- Return type: static int
- Signature: mlxbf_i2c_slave_disable(struct mlxbf_i2c_priv * priv,u8 addr)
- Line: 1596

### mlxbf_i2c_slave_enable
- Return type: static int
- Signature: mlxbf_i2c_slave_enable(struct mlxbf_i2c_priv * priv,struct i2c_client * slave)
- Line: 1535

### mlxbf_i2c_smbus_blk_process_call_func
- Return type: static void
- Signature: mlxbf_i2c_smbus_blk_process_call_func(struct mlxbf_i2c_smbus_request * request,u8 * command,u8 * data,u8 * data_len,bool pec_check)
- Line: 985

### mlxbf_i2c_smbus_block_func
- Return type: static void
- Signature: mlxbf_i2c_smbus_block_func(struct mlxbf_i2c_smbus_request * request,u8 * command,u8 * data,u8 * data_len,bool read,bool pec_check)
- Line: 935

### mlxbf_i2c_smbus_byte_func
- Return type: static void
- Signature: mlxbf_i2c_smbus_byte_func(struct mlxbf_i2c_smbus_request * request,u8 * data,bool read,bool pec_check)
- Line: 842

### mlxbf_i2c_smbus_check_status
- Return type: static int
- Signature: mlxbf_i2c_smbus_check_status(struct mlxbf_i2c_priv * priv)
- Line: 520

### mlxbf_i2c_smbus_data_byte_func
- Return type: static void
- Signature: mlxbf_i2c_smbus_data_byte_func(struct mlxbf_i2c_smbus_request * request,u8 * command,u8 * data,bool read,bool pec_check)
- Line: 859

### mlxbf_i2c_smbus_data_word_func
- Return type: static void
- Signature: mlxbf_i2c_smbus_data_word_func(struct mlxbf_i2c_smbus_request * request,u8 * command,u8 * data,bool read,bool pec_check)
- Line: 878

### mlxbf_i2c_smbus_enable
- Return type: static int
- Signature: mlxbf_i2c_smbus_enable(struct mlxbf_i2c_priv * priv,u8 slave,u8 len,u8 block_en,u8 pec_en,bool read,bool stop)
- Line: 635

### mlxbf_i2c_smbus_i2c_block_func
- Return type: static void
- Signature: mlxbf_i2c_smbus_i2c_block_func(struct mlxbf_i2c_smbus_request * request,u8 * command,u8 * data,u8 * data_len,bool read,bool pec_check)
- Line: 897

### mlxbf_i2c_smbus_process_call_func
- Return type: static void
- Signature: mlxbf_i2c_smbus_process_call_func(struct mlxbf_i2c_smbus_request * request,u8 * command,u8 * data,bool pec_check)
- Line: 963

### mlxbf_i2c_smbus_quick_command
- Return type: static void
- Signature: mlxbf_i2c_smbus_quick_command(struct mlxbf_i2c_smbus_request * request,u8 read)
- Line: 832

### mlxbf_i2c_smbus_read_data
- Return type: static void
- Signature: mlxbf_i2c_smbus_read_data(struct mlxbf_i2c_priv * priv,u8 * data,u8 length,u32 addr,bool is_master)
- Line: 596

### mlxbf_i2c_smbus_start_transaction
- Return type: static int
- Signature: mlxbf_i2c_smbus_start_transaction(struct mlxbf_i2c_priv * priv,struct mlxbf_i2c_smbus_request * request)
- Line: 676

### mlxbf_i2c_smbus_transaction_success
- Return type: static bool
- Signature: mlxbf_i2c_smbus_transaction_success(u32 master_status,u32 cause_status)
- Line: 495

### mlxbf_i2c_smbus_write_data
- Return type: static void
- Signature: mlxbf_i2c_smbus_write_data(struct mlxbf_i2c_priv * priv,const u8 * data,u8 length,u32 addr,bool is_master)
- Line: 570

### mlxbf_i2c_smbus_xfer
- Return type: static s32
- Signature: mlxbf_i2c_smbus_xfer(struct i2c_adapter * adap,u16 addr,unsigned short flags,char read_write,u8 command,int size,union i2c_smbus_data * data)
- Line: 2023

### mlxbf_i2c_unreg_slave
- Return type: static int
- Signature: mlxbf_i2c_unreg_slave(struct i2c_client * slave)
- Line: 2131

## Structs (6)

### mlxbf_i2c_chip_info
- Line: 397
- Members:
  - scl_high: u16
  - scl_low: u16
  - sda_rise: u8
  - sda_fall: u8
  - scl_rise: u8
  - scl_fall: u8
  - hold_start: u16
  - hold_data: u16
  - setup_start: u16
  - setup_stop: u16
  - setup_data: u16
  - pad: u16
  - buf: u16
  - thigh_max: u16
  - timeout: u32
  - flags: u32
  - length: u32
  - buffer: u8 *
  - slave: u8
  - operation_cnt: u8
  - operation: mlxbf_i2c_smbus_operation[]
  - io: void __iomem *
  - params: resource *
  - lock: mutex *
  - type: u8
  - type: mlxbf_i2c_chip_type
  - shared_res: mlxbf_i2c_resource * []
  - calculate_freq: u64 (*)(struct mlxbf_i2c_resource * corepll_res)
  - smbus_master_rs_bytes_off: u32
  - smbus_master_fsm_off: u32
  - chip: const struct mlxbf_i2c_chip_info *
  - adap: i2c_adapter
  - smbus: mlxbf_i2c_resource *
  - timer: mlxbf_i2c_resource *
  - mst: mlxbf_i2c_resource *
  - slv: mlxbf_i2c_resource *
  - mst_cause: mlxbf_i2c_resource *
  - slv_cause: mlxbf_i2c_resource *
  - coalesce: mlxbf_i2c_resource *
  - frequency: u64
  - bus: int
  - irq: int
  - slave: i2c_client * []
  - resource_version: u32

### mlxbf_i2c_priv
- Line: 410
- Members:
  - scl_high: u16
  - scl_low: u16
  - sda_rise: u8
  - sda_fall: u8
  - scl_rise: u8
  - scl_fall: u8
  - hold_start: u16
  - hold_data: u16
  - setup_start: u16
  - setup_stop: u16
  - setup_data: u16
  - pad: u16
  - buf: u16
  - thigh_max: u16
  - timeout: u32
  - flags: u32
  - length: u32
  - buffer: u8 *
  - slave: u8
  - operation_cnt: u8
  - operation: mlxbf_i2c_smbus_operation[]
  - io: void __iomem *
  - params: resource *
  - lock: mutex *
  - type: u8
  - type: mlxbf_i2c_chip_type
  - shared_res: mlxbf_i2c_resource * []
  - calculate_freq: u64 (*)(struct mlxbf_i2c_resource * corepll_res)
  - smbus_master_rs_bytes_off: u32
  - smbus_master_fsm_off: u32
  - chip: const struct mlxbf_i2c_chip_info *
  - adap: i2c_adapter
  - smbus: mlxbf_i2c_resource *
  - timer: mlxbf_i2c_resource *
  - mst: mlxbf_i2c_resource *
  - slv: mlxbf_i2c_resource *
  - mst_cause: mlxbf_i2c_resource *
  - slv_cause: mlxbf_i2c_resource *
  - coalesce: mlxbf_i2c_resource *
  - frequency: u64
  - bus: int
  - irq: int
  - slave: i2c_client * []
  - resource_version: u32

### mlxbf_i2c_resource
- Line: 390
- Members:
  - scl_high: u16
  - scl_low: u16
  - sda_rise: u8
  - sda_fall: u8
  - scl_rise: u8
  - scl_fall: u8
  - hold_start: u16
  - hold_data: u16
  - setup_start: u16
  - setup_stop: u16
  - setup_data: u16
  - pad: u16
  - buf: u16
  - thigh_max: u16
  - timeout: u32
  - flags: u32
  - length: u32
  - buffer: u8 *
  - slave: u8
  - operation_cnt: u8
  - operation: mlxbf_i2c_smbus_operation[]
  - io: void __iomem *
  - params: resource *
  - lock: mutex *
  - type: u8
  - type: mlxbf_i2c_chip_type
  - shared_res: mlxbf_i2c_resource * []
  - calculate_freq: u64 (*)(struct mlxbf_i2c_resource * corepll_res)
  - smbus_master_rs_bytes_off: u32
  - smbus_master_fsm_off: u32
  - chip: const struct mlxbf_i2c_chip_info *
  - adap: i2c_adapter
  - smbus: mlxbf_i2c_resource *
  - timer: mlxbf_i2c_resource *
  - mst: mlxbf_i2c_resource *
  - slv: mlxbf_i2c_resource *
  - mst_cause: mlxbf_i2c_resource *
  - slv_cause: mlxbf_i2c_resource *
  - coalesce: mlxbf_i2c_resource *
  - frequency: u64
  - bus: int
  - irq: int
  - slave: i2c_client * []
  - resource_version: u32

### mlxbf_i2c_smbus_operation
- Line: 378
- Members:
  - scl_high: u16
  - scl_low: u16
  - sda_rise: u8
  - sda_fall: u8
  - scl_rise: u8
  - scl_fall: u8
  - hold_start: u16
  - hold_data: u16
  - setup_start: u16
  - setup_stop: u16
  - setup_data: u16
  - pad: u16
  - buf: u16
  - thigh_max: u16
  - timeout: u32
  - flags: u32
  - length: u32
  - buffer: u8 *
  - slave: u8
  - operation_cnt: u8
  - operation: mlxbf_i2c_smbus_operation[]
  - io: void __iomem *
  - params: resource *
  - lock: mutex *
  - type: u8
  - type: mlxbf_i2c_chip_type
  - shared_res: mlxbf_i2c_resource * []
  - calculate_freq: u64 (*)(struct mlxbf_i2c_resource * corepll_res)
  - smbus_master_rs_bytes_off: u32
  - smbus_master_fsm_off: u32
  - chip: const struct mlxbf_i2c_chip_info *
  - adap: i2c_adapter
  - smbus: mlxbf_i2c_resource *
  - timer: mlxbf_i2c_resource *
  - mst: mlxbf_i2c_resource *
  - slv: mlxbf_i2c_resource *
  - mst_cause: mlxbf_i2c_resource *
  - slv_cause: mlxbf_i2c_resource *
  - coalesce: mlxbf_i2c_resource *
  - frequency: u64
  - bus: int
  - irq: int
  - slave: i2c_client * []
  - resource_version: u32

### mlxbf_i2c_smbus_request
- Line: 384
- Members:
  - scl_high: u16
  - scl_low: u16
  - sda_rise: u8
  - sda_fall: u8
  - scl_rise: u8
  - scl_fall: u8
  - hold_start: u16
  - hold_data: u16
  - setup_start: u16
  - setup_stop: u16
  - setup_data: u16
  - pad: u16
  - buf: u16
  - thigh_max: u16
  - timeout: u32
  - flags: u32
  - length: u32
  - buffer: u8 *
  - slave: u8
  - operation_cnt: u8
  - operation: mlxbf_i2c_smbus_operation[]
  - io: void __iomem *
  - params: resource *
  - lock: mutex *
  - type: u8
  - type: mlxbf_i2c_chip_type
  - shared_res: mlxbf_i2c_resource * []
  - calculate_freq: u64 (*)(struct mlxbf_i2c_resource * corepll_res)
  - smbus_master_rs_bytes_off: u32
  - smbus_master_fsm_off: u32
  - chip: const struct mlxbf_i2c_chip_info *
  - adap: i2c_adapter
  - smbus: mlxbf_i2c_resource *
  - timer: mlxbf_i2c_resource *
  - mst: mlxbf_i2c_resource *
  - slv: mlxbf_i2c_resource *
  - mst_cause: mlxbf_i2c_resource *
  - slv_cause: mlxbf_i2c_resource *
  - coalesce: mlxbf_i2c_resource *
  - frequency: u64
  - bus: int
  - irq: int
  - slave: i2c_client * []
  - resource_version: u32

### mlxbf_i2c_timings
- Line: 360
- Members:
  - scl_high: u16
  - scl_low: u16
  - sda_rise: u8
  - sda_fall: u8
  - scl_rise: u8
  - scl_fall: u8
  - hold_start: u16
  - hold_data: u16
  - setup_start: u16
  - setup_stop: u16
  - setup_data: u16
  - pad: u16
  - buf: u16
  - thigh_max: u16
  - timeout: u32
  - flags: u32
  - length: u32
  - buffer: u8 *
  - slave: u8
  - operation_cnt: u8
  - operation: mlxbf_i2c_smbus_operation[]
  - io: void __iomem *
  - params: resource *
  - lock: mutex *
  - type: u8
  - type: mlxbf_i2c_chip_type
  - shared_res: mlxbf_i2c_resource * []
  - calculate_freq: u64 (*)(struct mlxbf_i2c_resource * corepll_res)
  - smbus_master_rs_bytes_off: u32
  - smbus_master_fsm_off: u32
  - chip: const struct mlxbf_i2c_chip_info *
  - adap: i2c_adapter
  - smbus: mlxbf_i2c_resource *
  - timer: mlxbf_i2c_resource *
  - mst: mlxbf_i2c_resource *
  - slv: mlxbf_i2c_resource *
  - mst_cause: mlxbf_i2c_resource *
  - slv_cause: mlxbf_i2c_resource *
  - coalesce: mlxbf_i2c_resource *
  - frequency: u64
  - bus: int
  - irq: int
  - slave: i2c_client * []
  - resource_version: u32

## Enums (4)

### __anonb93a87630103
- Line: 327

### __anonb93a87630203
- Line: 346

### mlxbf_i2c_chip_type
- Line: 339

### mlxbf_i2c_timings_config
- Line: 1151

## Variables (20)

- static **mlxbf_i2c_acpi_ids** : const struct acpi_device_id[] (line 2198)
- static **mlxbf_i2c_algo** : const struct i2c_algorithm (line 2186)
- static **mlxbf_i2c_bus_count** : u8 (line 491)
- static **mlxbf_i2c_bus_lock** : mutex (line 493)
- static **mlxbf_i2c_chip** : mlxbf_i2c_chip_info[] (line 2154)
- static **mlxbf_i2c_coalesce_lock** : mutex (line 451)
- static **mlxbf_i2c_coalesce_res** : mlxbf_i2c_resource[] (line 455)
- static **mlxbf_i2c_coalesce_tyu_params** : resource (line 430)
- static **mlxbf_i2c_corepll_frequency** : u64 (line 428)
- static **mlxbf_i2c_corepll_lock** : mutex (line 452)
- static **mlxbf_i2c_corepll_res** : mlxbf_i2c_resource[] (line 464)
- static **mlxbf_i2c_corepll_rsh_yu_params** : resource (line 442)
- static **mlxbf_i2c_corepll_tyu_params** : resource (line 434)
- static **mlxbf_i2c_corepll_yu_params** : resource (line 438)
- static **mlxbf_i2c_driver** : platform_driver (line 2411)
- static **mlxbf_i2c_gpio_lock** : mutex (line 453)
- static **mlxbf_i2c_gpio_res** : mlxbf_i2c_resource[] (line 482)
- static **mlxbf_i2c_gpio_tyu_params** : resource (line 446)
- static **mlxbf_i2c_quirks** : i2c_adapter_quirks (line 2193)
- static **mlxbf_i2c_timings** : const struct mlxbf_i2c_timings[] (line 1158)

## Macros (126)

- **MLNXBF_I2C_COREPLL_CONST** (line 74)
- **MLXBF_I2C_CAUSE_ARBITER** (line 85)
- **MLXBF_I2C_CAUSE_CLK_TOGGLE_DONE** (line 107)
- **MLXBF_I2C_CAUSE_COALESCE_0** (line 137)
- **MLXBF_I2C_CAUSE_MASTER_ARBITER_BITS_MASK** (line 113)
- **MLXBF_I2C_CAUSE_MASTER_STATUS_ERROR** (line 115)
- **MLXBF_I2C_CAUSE_M_ARBITRATION_LOST** (line 95)
- **MLXBF_I2C_CAUSE_M_FW_TIMEOUT** (line 109)
- **MLXBF_I2C_CAUSE_M_GW_BUSY_FALL** (line 111)
- **MLXBF_I2C_CAUSE_OR_CLEAR** (line 82)
- **MLXBF_I2C_CAUSE_OR_EVTEN0** (line 81)
- **MLXBF_I2C_CAUSE_PUT_START_FAILED** (line 105)
- **MLXBF_I2C_CAUSE_PUT_STOP_FAILED** (line 103)
- **MLXBF_I2C_CAUSE_READ_WAIT_FW_RESPONSE** (line 132)
- **MLXBF_I2C_CAUSE_S_GW_BUSY_FALL** (line 134)
- **MLXBF_I2C_CAUSE_TRANSACTION_ENDED** (line 93)
- **MLXBF_I2C_CAUSE_TYU_SLAVE_BIT** (line 139)
- **MLXBF_I2C_CAUSE_UNEXPECTED_START** (line 97)
- **MLXBF_I2C_CAUSE_UNEXPECTED_STOP** (line 99)
- **MLXBF_I2C_CAUSE_WAIT_FOR_FW_DATA** (line 101)
- **MLXBF_I2C_CAUSE_WRITE_SUCCESS** (line 130)
- **MLXBF_I2C_CAUSE_YU_SLAVE_BIT** (line 140)
- **MLXBF_I2C_COALESCE_TYU_ADDR** (line 40)
- **MLXBF_I2C_COALESCE_TYU_SIZE** (line 41)
- **MLXBF_I2C_COREPLL_CORE_F_TYU_MASK** (line 175)
- **MLXBF_I2C_COREPLL_CORE_F_YU_MASK** (line 180)
- **MLXBF_I2C_COREPLL_CORE_OD_TYU_MASK** (line 176)
- **MLXBF_I2C_COREPLL_CORE_OD_YU_MASK** (line 181)
- **MLXBF_I2C_COREPLL_CORE_R_TYU_MASK** (line 177)
- **MLXBF_I2C_COREPLL_CORE_R_YU_MASK** (line 182)
- **MLXBF_I2C_COREPLL_FREQ** (line 172)
- **MLXBF_I2C_COREPLL_RSH_YU_ADDR** (line 52)
- **MLXBF_I2C_COREPLL_RSH_YU_SIZE** (line 53)
- **MLXBF_I2C_COREPLL_TYU_ADDR** (line 46)
- **MLXBF_I2C_COREPLL_TYU_SIZE** (line 47)
- **MLXBF_I2C_COREPLL_YU_ADDR** (line 49)
- **MLXBF_I2C_COREPLL_YU_SIZE** (line 50)
- **MLXBF_I2C_CORE_PLL_REG1** (line 77)
- **MLXBF_I2C_CORE_PLL_REG2** (line 78)
- **MLXBF_I2C_FUNC_ALL** (line 34)
- **MLXBF_I2C_FUNC_SMBUS_BLOCK** (line 26)
- **MLXBF_I2C_FUNC_SMBUS_DEFAULT** (line 29)
- **MLXBF_I2C_GPIO_0_FORCE_OE_EN** (line 145)
- **MLXBF_I2C_GPIO_0_FUNC_EN_0** (line 143)
- **MLXBF_I2C_GPIO_SMBUS_GW_ASSERT_PINS**(num,val) (line 163)
- **MLXBF_I2C_GPIO_SMBUS_GW_MASK**(num) (line 157)
- **MLXBF_I2C_GPIO_SMBUS_GW_PINS**(num) (line 154)
- **MLXBF_I2C_GPIO_SMBUS_GW_RESET_PINS**(num,val) (line 160)
- **MLXBF_I2C_GPIO_TYU_ADDR** (line 43)
- **MLXBF_I2C_GPIO_TYU_SIZE** (line 44)
- **MLXBF_I2C_MASK_16** (line 199)
- **MLXBF_I2C_MASK_32** (line 200)
- **MLXBF_I2C_MASK_8** (line 198)
- **MLXBF_I2C_MASTER_BUSY_BIT** (line 219)
- **MLXBF_I2C_MASTER_CTL_READ_BIT** (line 222)
- **MLXBF_I2C_MASTER_CTL_WRITE_BIT** (line 221)
- **MLXBF_I2C_MASTER_DATA_DESC_ADDR** (line 242)
- **MLXBF_I2C_MASTER_DATA_DESC_SIZE** (line 243)
- **MLXBF_I2C_MASTER_DATA_R_LENGTH** (line 246)
- **MLXBF_I2C_MASTER_DATA_W_LENGTH** (line 247)
- **MLXBF_I2C_MASTER_ENABLE** (line 225)
- **MLXBF_I2C_MASTER_ENABLE_READ** (line 232)
- **MLXBF_I2C_MASTER_ENABLE_WRITE** (line 229)
- **MLXBF_I2C_MASTER_LOCK_BIT** (line 218)
- **MLXBF_I2C_MASTER_PARSE_EXP_SHIFT** (line 237)
- **MLXBF_I2C_MASTER_READ_SHIFT** (line 239)
- **MLXBF_I2C_MASTER_SEND_PEC_SHIFT** (line 236)
- **MLXBF_I2C_MASTER_SLV_ADDR_SHIFT** (line 238)
- **MLXBF_I2C_MASTER_START_BIT** (line 220)
- **MLXBF_I2C_MASTER_STOP_BIT** (line 223)
- **MLXBF_I2C_MASTER_WRITE_SHIFT** (line 235)
- **MLXBF_I2C_MST_ADDR_OFFSET** (line 202)
- **MLXBF_I2C_PLL_IN_FREQ** (line 71)
- **MLXBF_I2C_POLL_FREQ_IN_USEC** (line 312)
- **MLXBF_I2C_RES_PARAMS**(addr,size,str) (line 320)
- **MLXBF_I2C_RSH_YU_SMBUS_MASTER_FSM** (line 215)
- **MLXBF_I2C_RSH_YU_SMBUS_RS_BYTES** (line 208)
- **MLXBF_I2C_SHARED_RES_MAX** (line 55)
- **MLXBF_I2C_SHIFT_0** (line 193)
- **MLXBF_I2C_SHIFT_16** (line 195)
- **MLXBF_I2C_SHIFT_24** (line 196)
- **MLXBF_I2C_SHIFT_8** (line 194)
- **MLXBF_I2C_SLAVE_BUSY_BIT** (line 285)
- **MLXBF_I2C_SLAVE_DATA_DESC_ADDR** (line 295)
- **MLXBF_I2C_SLAVE_DATA_DESC_SIZE** (line 296)
- **MLXBF_I2C_SLAVE_ENABLE** (line 288)
- **MLXBF_I2C_SLAVE_SEND_PEC_SHIFT** (line 292)
- **MLXBF_I2C_SLAVE_WRITE_BIT** (line 286)
- **MLXBF_I2C_SLAVE_WRITE_BYTES_SHIFT** (line 291)
- **MLXBF_I2C_SLV_ADDR_OFFSET** (line 268)
- **MLXBF_I2C_SMBUS_LOCK_POLL_TIMEOUT** (line 309)
- **MLXBF_I2C_SMBUS_MASTER_FSM_PS_STATE_MASK** (line 266)
- **MLXBF_I2C_SMBUS_MASTER_FSM_STOP_MASK** (line 265)
- **MLXBF_I2C_SMBUS_MASTER_GW** (line 205)
- **MLXBF_I2C_SMBUS_MASTER_PEC** (line 210)
- **MLXBF_I2C_SMBUS_MASTER_STATUS** (line 212)
- **MLXBF_I2C_SMBUS_MASTER_STATUS_ERROR** (line 260)
- **MLXBF_I2C_SMBUS_MASTER_STATUS_MASK** (line 258)
- **MLXBF_I2C_SMBUS_MAX_OP_CNT** (line 317)
- **MLXBF_I2C_SMBUS_OP_CNT_1** (line 314)
- **MLXBF_I2C_SMBUS_OP_CNT_2** (line 315)
- **MLXBF_I2C_SMBUS_OP_CNT_3** (line 316)
- **MLXBF_I2C_SMBUS_SCL_LOW_TIMEOUT** (line 191)
- **MLXBF_I2C_SMBUS_SLAVE_ADDR_CFG** (line 299)
- **MLXBF_I2C_SMBUS_SLAVE_ADDR_CNT** (line 300)
- **MLXBF_I2C_SMBUS_SLAVE_ADDR_EN_BIT** (line 301)
- **MLXBF_I2C_SMBUS_SLAVE_ADDR_MASK** (line 302)
- **MLXBF_I2C_SMBUS_SLAVE_FSM** (line 277)
- **MLXBF_I2C_SMBUS_SLAVE_GW** (line 271)
- **MLXBF_I2C_SMBUS_SLAVE_PEC** (line 275)
- **MLXBF_I2C_SMBUS_SLAVE_READY** (line 282)
- **MLXBF_I2C_SMBUS_SLAVE_RS_MASTER_BYTES** (line 273)
- **MLXBF_I2C_SMBUS_STATUS_BYTE_CNT_DONE** (line 250)
- **MLXBF_I2C_SMBUS_STATUS_FW_TIMEOUT** (line 256)
- **MLXBF_I2C_SMBUS_STATUS_NACK_RCV** (line 252)
- **MLXBF_I2C_SMBUS_STATUS_READ_ERR** (line 254)
- **MLXBF_I2C_SMBUS_THIGH_MAX_TBUF** (line 190)
- **MLXBF_I2C_SMBUS_TIMEOUT** (line 308)
- **MLXBF_I2C_SMBUS_TIMER_FALL_RISE_SPIKE** (line 186)
- **MLXBF_I2C_SMBUS_TIMER_SCL_LOW_SCL_HIGH** (line 185)
- **MLXBF_I2C_SMBUS_TIMER_THOLD** (line 187)
- **MLXBF_I2C_SMBUS_TIMER_TSETUP_DATA** (line 189)
- **MLXBF_I2C_SMBUS_TIMER_TSETUP_START_STOP** (line 188)
- **MLXBF_I2C_TYU_PLL_OUT_FREQ** (line 69)
- **MLXBF_I2C_YU_SMBUS_MASTER_FSM** (line 214)
- **MLXBF_I2C_YU_SMBUS_RS_BYTES** (line 207)
