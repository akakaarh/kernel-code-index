# drivers/i2c/busses/i2c-qcom-cci.c

Subsystem: drivers/i2c

## Functions (18)

### cci_disable_clocks
- Return type: static void
- Signature: cci_disable_clocks(struct cci * cci)
- Line: 470

### cci_enable_clocks
- Return type: static int
- Signature: cci_enable_clocks(struct cci * cci)
- Line: 465

### cci_func
- Return type: static u32
- Signature: cci_func(struct i2c_adapter * adap)
- Line: 455

### cci_halt
- Return type: static int
- Signature: cci_halt(struct cci * cci,u8 master_num)
- Line: 204

### cci_i2c_read
- Return type: static int
- Signature: cci_i2c_read(struct cci * cci,u16 master,u16 addr,u8 * buf,u16 len)
- Line: 331

### cci_i2c_write
- Return type: static int
- Signature: cci_i2c_write(struct cci * cci,u16 master,u16 addr,u8 * buf,u16 len)
- Line: 384

### cci_init
- Return type: static int
- Signature: cci_init(struct cci * cci)
- Line: 246

### cci_isr
- Return type: static irqreturn_t
- Signature: cci_isr(int irq,void * dev)
- Line: 133

### cci_probe
- Return type: static int
- Signature: cci_probe(struct platform_device * pdev)
- Line: 517

### cci_remove
- Return type: static void
- Signature: cci_remove(struct platform_device * pdev)
- Line: 654

### cci_reset
- Return type: static int
- Signature: cci_reset(struct cci * cci)
- Line: 228

### cci_resume
- Return type: static int __maybe_unused
- Signature: cci_resume(struct device * dev)
- Line: 504

### cci_resume_runtime
- Return type: static int __maybe_unused
- Signature: cci_resume_runtime(struct device * dev)
- Line: 483

### cci_run_queue
- Return type: static int
- Signature: cci_run_queue(struct cci * cci,u8 master,u8 queue)
- Line: 291

### cci_suspend
- Return type: static int __maybe_unused
- Signature: cci_suspend(struct device * dev)
- Line: 496

### cci_suspend_runtime
- Return type: static int __maybe_unused
- Signature: cci_suspend_runtime(struct device * dev)
- Line: 475

### cci_validate_queue
- Return type: static int
- Signature: cci_validate_queue(struct cci * cci,u8 master,u8 queue)
- Line: 314

### cci_xfer
- Return type: static int
- Signature: cci_xfer(struct i2c_adapter * adap,struct i2c_msg msgs[],int num)
- Line: 422

## Structs (4)

### cci
- Line: 123
- Members:
  - thigh: u16
  - tlow: u16
  - tsu_sto: u16
  - tsu_sta: u16
  - thd_dat: u16
  - thd_sta: u16
  - tbuf: u16
  - scl_stretch_en: u8
  - trdhld: u16
  - tsp: u16
  - adap: i2c_adapter
  - master: u16
  - mode: u8
  - status: int
  - irq_complete: completion
  - cci: cci *
  - num_masters: unsigned int
  - quirks: i2c_adapter_quirks
  - queue_size: u16[]
  - params: hw_params[3]
  - dev: device *
  - base: void __iomem *
  - irq: unsigned int
  - data: const struct cci_data *
  - clocks: clk_bulk_data *
  - nclocks: int
  - master: cci_master[]

### cci_data
- Line: 116
- Members:
  - thigh: u16
  - tlow: u16
  - tsu_sto: u16
  - tsu_sta: u16
  - thd_dat: u16
  - thd_sta: u16
  - tbuf: u16
  - scl_stretch_en: u8
  - trdhld: u16
  - tsp: u16
  - adap: i2c_adapter
  - master: u16
  - mode: u8
  - status: int
  - irq_complete: completion
  - cci: cci *
  - num_masters: unsigned int
  - quirks: i2c_adapter_quirks
  - queue_size: u16[]
  - params: hw_params[3]
  - dev: device *
  - base: void __iomem *
  - irq: unsigned int
  - data: const struct cci_data *
  - clocks: clk_bulk_data *
  - nclocks: int
  - master: cci_master[]

### cci_master
- Line: 107
- Members:
  - thigh: u16
  - tlow: u16
  - tsu_sto: u16
  - tsu_sta: u16
  - thd_dat: u16
  - thd_sta: u16
  - tbuf: u16
  - scl_stretch_en: u8
  - trdhld: u16
  - tsp: u16
  - adap: i2c_adapter
  - master: u16
  - mode: u8
  - status: int
  - irq_complete: completion
  - cci: cci *
  - num_masters: unsigned int
  - quirks: i2c_adapter_quirks
  - queue_size: u16[]
  - params: hw_params[3]
  - dev: device *
  - base: void __iomem *
  - irq: unsigned int
  - data: const struct cci_data *
  - clocks: clk_bulk_data *
  - nclocks: int
  - master: cci_master[]

### hw_params
- Line: 92
- Members:
  - thigh: u16
  - tlow: u16
  - tsu_sto: u16
  - tsu_sta: u16
  - thd_dat: u16
  - thd_sta: u16
  - tbuf: u16
  - scl_stretch_en: u8
  - trdhld: u16
  - tsp: u16
  - adap: i2c_adapter
  - master: u16
  - mode: u8
  - status: int
  - irq_complete: completion
  - cci: cci *
  - num_masters: unsigned int
  - quirks: i2c_adapter_quirks
  - queue_size: u16[]
  - params: hw_params[3]
  - dev: device *
  - base: void __iomem *
  - irq: unsigned int
  - data: const struct cci_data *
  - clocks: clk_bulk_data *
  - nclocks: int
  - master: cci_master[]

## Enums (2)

### __anona83ca8360103
- Line: 81

### cci_i2c_queue_t
- Line: 87

## Variables (8)

- static **cci_algo** : const struct i2c_algorithm (line 460)
- static **cci_dt_match** : const struct of_device_id[] (line 828)
- static **cci_msm8953_data** : const struct cci_data (line 783)
- static **cci_v1_5_data** : const struct cci_data (line 705)
- static **cci_v1_data** : const struct cci_data (line 672)
- static **cci_v2_data** : const struct cci_data (line 738)
- static **qcom_cci_driver** : platform_driver (line 847)
- static **qcom_cci_pm** : const struct dev_pm_ops (line 512)

## Macros (59)

- **CCI_HALT_REQ** (line 21)
- **CCI_HALT_REQ_I2C_M0_Q0Q1** (line 22)
- **CCI_HALT_REQ_I2C_M1_Q0Q1** (line 23)
- **CCI_HW_VERSION** (line 15)
- **CCI_I2C_Mm_MISC_CTL**(m) (line 29)
- **CCI_I2C_Mm_Qn_CUR_CMD**(m,n) (line 35)
- **CCI_I2C_Mm_Qn_CUR_WORD_CNT**(m,n) (line 34)
- **CCI_I2C_Mm_Qn_EXEC_WORD_CNT**(m,n) (line 33)
- **CCI_I2C_Mm_Qn_LOAD_DATA**(m,n) (line 37)
- **CCI_I2C_Mm_Qn_REPORT_STATUS**(m,n) (line 36)
- **CCI_I2C_Mm_READ_BUF_LEVEL**(m) (line 32)
- **CCI_I2C_Mm_READ_DATA**(m) (line 31)
- **CCI_I2C_Mm_SCL_CTL**(m) (line 25)
- **CCI_I2C_Mm_SDA_CTL_0**(m) (line 26)
- **CCI_I2C_Mm_SDA_CTL_1**(m) (line 27)
- **CCI_I2C_Mm_SDA_CTL_2**(m) (line 28)
- **CCI_I2C_READ** (line 77)
- **CCI_I2C_REPORT** (line 75)
- **CCI_I2C_REPORT_IRQ_EN** (line 79)
- **CCI_I2C_SET_PARAM** (line 74)
- **CCI_I2C_WRITE** (line 76)
- **CCI_IRQ_CLEAR_0** (line 52)
- **CCI_IRQ_GLOBAL_CLEAR_CMD** (line 39)
- **CCI_IRQ_MASK_0** (line 40)
- **CCI_IRQ_MASK_0_I2C_M0_ERROR** (line 50)
- **CCI_IRQ_MASK_0_I2C_M0_Q0Q1_HALT_ACK** (line 48)
- **CCI_IRQ_MASK_0_I2C_M0_Q0_REPORT** (line 42)
- **CCI_IRQ_MASK_0_I2C_M0_Q1_REPORT** (line 43)
- **CCI_IRQ_MASK_0_I2C_M0_RD_DONE** (line 41)
- **CCI_IRQ_MASK_0_I2C_M1_ERROR** (line 51)
- **CCI_IRQ_MASK_0_I2C_M1_Q0Q1_HALT_ACK** (line 49)
- **CCI_IRQ_MASK_0_I2C_M1_Q0_REPORT** (line 45)
- **CCI_IRQ_MASK_0_I2C_M1_Q1_REPORT** (line 46)
- **CCI_IRQ_MASK_0_I2C_M1_RD_DONE** (line 44)
- **CCI_IRQ_MASK_0_RST_DONE_ACK** (line 47)
- **CCI_IRQ_STATUS_0** (line 53)
- **CCI_IRQ_STATUS_0_I2C_M0_ERROR** (line 67)
- **CCI_IRQ_STATUS_0_I2C_M0_Q0Q1_HALT_ACK** (line 61)
- **CCI_IRQ_STATUS_0_I2C_M0_Q0_NACK_ERR** (line 63)
- **CCI_IRQ_STATUS_0_I2C_M0_Q0_REPORT** (line 55)
- **CCI_IRQ_STATUS_0_I2C_M0_Q1_NACK_ERR** (line 64)
- **CCI_IRQ_STATUS_0_I2C_M0_Q1_REPORT** (line 56)
- **CCI_IRQ_STATUS_0_I2C_M0_RD_DONE** (line 54)
- **CCI_IRQ_STATUS_0_I2C_M1_ERROR** (line 68)
- **CCI_IRQ_STATUS_0_I2C_M1_Q0Q1_HALT_ACK** (line 62)
- **CCI_IRQ_STATUS_0_I2C_M1_Q0_NACK_ERR** (line 65)
- **CCI_IRQ_STATUS_0_I2C_M1_Q0_REPORT** (line 58)
- **CCI_IRQ_STATUS_0_I2C_M1_Q1_NACK_ERR** (line 66)
- **CCI_IRQ_STATUS_0_I2C_M1_Q1_REPORT** (line 59)
- **CCI_IRQ_STATUS_0_I2C_M1_RD_DONE** (line 57)
- **CCI_IRQ_STATUS_0_RST_DONE_ACK** (line 60)
- **CCI_QUEUE_START** (line 20)
- **CCI_RESET_CMD** (line 16)
- **CCI_RESET_CMD_M0_MASK** (line 18)
- **CCI_RESET_CMD_M1_MASK** (line 19)
- **CCI_RESET_CMD_MASK** (line 17)
- **CCI_TIMEOUT** (line 70)
- **NUM_MASTERS** (line 71)
- **NUM_QUEUES** (line 72)
