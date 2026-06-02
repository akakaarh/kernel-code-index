# drivers/i2c/busses/i2c-bcm-iproc.c

Subsystem: drivers/i2c

## Functions (26)

### bcm_iproc_i2c_cfg_speed
- Return type: static int
- Signature: bcm_iproc_i2c_cfg_speed(struct bcm_iproc_i2c_dev * iproc_i2c)
- Line: 1056

### bcm_iproc_i2c_check_slave_status
- Return type: static bool
- Signature: bcm_iproc_i2c_check_slave_status(struct bcm_iproc_i2c_dev * iproc_i2c,u32 status)
- Line: 327

### bcm_iproc_i2c_check_status
- Return type: static int
- Signature: bcm_iproc_i2c_check_status(struct bcm_iproc_i2c_dev * iproc_i2c,struct i2c_msg * msg)
- Line: 718

### bcm_iproc_i2c_enable_disable
- Return type: static void
- Signature: bcm_iproc_i2c_enable_disable(struct bcm_iproc_i2c_dev * iproc_i2c,bool enable)
- Line: 314

### bcm_iproc_i2c_functionality
- Return type: static u32
- Signature: bcm_iproc_i2c_functionality(struct i2c_adapter * adap)
- Line: 974

### bcm_iproc_i2c_init
- Return type: static void
- Signature: bcm_iproc_i2c_init(struct bcm_iproc_i2c_dev * iproc_i2c)
- Line: 688

### bcm_iproc_i2c_isr
- Return type: static irqreturn_t
- Signature: bcm_iproc_i2c_isr(int irq,void * data)
- Line: 657

### bcm_iproc_i2c_probe
- Return type: static int
- Signature: bcm_iproc_i2c_probe(struct platform_device * pdev)
- Line: 1088

### bcm_iproc_i2c_process_m_event
- Return type: static void
- Signature: bcm_iproc_i2c_process_m_event(struct bcm_iproc_i2c_dev * iproc_i2c,u32 status)
- Line: 638

### bcm_iproc_i2c_read
- Return type: static void
- Signature: bcm_iproc_i2c_read(struct bcm_iproc_i2c_dev * iproc_i2c)
- Line: 609

### bcm_iproc_i2c_read_valid_bytes
- Return type: static void
- Signature: bcm_iproc_i2c_read_valid_bytes(struct bcm_iproc_i2c_dev * iproc_i2c)
- Line: 549

### bcm_iproc_i2c_reg_slave
- Return type: static int
- Signature: bcm_iproc_i2c_reg_slave(struct i2c_client * slave)
- Line: 986

### bcm_iproc_i2c_remove
- Return type: static void
- Signature: bcm_iproc_i2c_remove(struct platform_device * pdev)
- Line: 1162

### bcm_iproc_i2c_resume
- Return type: static int
- Signature: bcm_iproc_i2c_resume(struct device * dev)
- Line: 1200

### bcm_iproc_i2c_send
- Return type: static void
- Signature: bcm_iproc_i2c_send(struct bcm_iproc_i2c_dev * iproc_i2c)
- Line: 568

### bcm_iproc_i2c_slave_init
- Return type: static void
- Signature: bcm_iproc_i2c_slave_init(struct bcm_iproc_i2c_dev * iproc_i2c,bool need_reset)
- Line: 262

### bcm_iproc_i2c_slave_isr
- Return type: static bool
- Signature: bcm_iproc_i2c_slave_isr(struct bcm_iproc_i2c_dev * iproc_i2c,u32 status)
- Line: 443

### bcm_iproc_i2c_slave_read
- Return type: static void
- Signature: bcm_iproc_i2c_slave_read(struct bcm_iproc_i2c_dev * iproc_i2c)
- Line: 367

### bcm_iproc_i2c_suspend
- Return type: static int
- Signature: bcm_iproc_i2c_suspend(struct device * dev)
- Line: 1180

### bcm_iproc_i2c_unreg_slave
- Return type: static int
- Signature: bcm_iproc_i2c_unreg_slave(struct i2c_client * slave)
- Line: 1006

### bcm_iproc_i2c_xfer
- Return type: static int
- Signature: bcm_iproc_i2c_xfer(struct i2c_adapter * adapter,struct i2c_msg msgs[],int num)
- Line: 949

### bcm_iproc_i2c_xfer_internal
- Return type: static int
- Signature: bcm_iproc_i2c_xfer_internal(struct bcm_iproc_i2c_dev * iproc_i2c,struct i2c_msg * msgs,bool process_call)
- Line: 829

### bcm_iproc_i2c_xfer_wait
- Return type: static int
- Signature: bcm_iproc_i2c_xfer_wait(struct bcm_iproc_i2c_dev * iproc_i2c,struct i2c_msg * msg,u32 cmd)
- Line: 766

### iproc_i2c_rd_reg
- Return type: static u32
- Signature: iproc_i2c_rd_reg(struct bcm_iproc_i2c_dev * iproc_i2c,u32 offset)
- Line: 227

### iproc_i2c_wr_reg
- Return type: static void
- Signature: iproc_i2c_wr_reg(struct bcm_iproc_i2c_dev * iproc_i2c,u32 offset,u32 val)
- Line: 246

### slave_rx_tasklet_fn
- Return type: static void
- Signature: slave_rx_tasklet_fn(unsigned long data)
- Line: 409

## Structs (1)

### bcm_iproc_i2c_dev
- Line: 176
- Members:
  - device: device *
  - type: bcm_iproc_i2c_type
  - irq: int
  - base: void __iomem *
  - idm_base: void __iomem *
  - ape_addr_mask: u32
  - idm_lock: spinlock_t
  - adapter: i2c_adapter
  - bus_speed: unsigned int
  - done: completion
  - xfer_is_done: int
  - msg: i2c_msg *
  - slave: i2c_client *
  - tx_bytes: unsigned int
  - rx_bytes: unsigned int
  - thld_bytes: unsigned int
  - slave_rx_only: bool
  - rx_start_rcvd: bool
  - slave_read_complete: bool
  - tx_underrun: u32
  - slave_int_mask: u32
  - slave_rx_tasklet: tasklet_struct

## Enums (3)

### bcm_iproc_i2c_type
- Line: 171

### bus_speed_index
- Line: 166

### i2c_slave_read_status
- Line: 159

## Variables (5)

- static **bcm_iproc_algo** : i2c_algorithm (line 1043)
- static **bcm_iproc_i2c_driver** : platform_driver (line 1239)
- static **bcm_iproc_i2c_of_match** : const struct of_device_id[] (line 1227)
- static **bcm_iproc_i2c_pm_ops** : const struct dev_pm_ops (line 1222)
- static **bcm_iproc_i2c_quirks** : const struct i2c_adapter_quirks (line 1050)

## Macros (125)

- **CFG_EN_SHIFT** (line 17)
- **CFG_M_RETRY_CNT_MASK** (line 20)
- **CFG_M_RETRY_CNT_SHIFT** (line 19)
- **CFG_OFFSET** (line 15)
- **CFG_RESET_SHIFT** (line 16)
- **CFG_SLAVE_ADDR_0_SHIFT** (line 18)
- **I2C_TIMEOUT_MSEC** (line 136)
- **IDM_CTRL_DIRECT_OFFSET** (line 14)
- **IE_M_ALL_INTERRUPT_MASK** (line 144)
- **IE_M_ALL_INTERRUPT_SHIFT** (line 143)
- **IE_M_RX_FIFO_FULL_SHIFT** (line 89)
- **IE_M_RX_THLD_SHIFT** (line 90)
- **IE_M_START_BUSY_SHIFT** (line 91)
- **IE_M_TX_UNDERRUN_SHIFT** (line 92)
- **IE_OFFSET** (line 88)
- **IE_S_ALL_INTERRUPT_MASK** (line 152)
- **IE_S_ALL_INTERRUPT_SHIFT** (line 151)
- **IE_S_RD_EVENT_SHIFT** (line 98)
- **IE_S_RX_EVENT_SHIFT** (line 95)
- **IE_S_RX_FIFO_FULL_SHIFT** (line 93)
- **IE_S_RX_THLD_SHIFT** (line 94)
- **IE_S_START_BUSY_SHIFT** (line 96)
- **IE_S_TX_UNDERRUN_SHIFT** (line 97)
- **ISR_MASK** (line 219)
- **ISR_MASK_SLAVE** (line 222)
- **IS_M_RX_FIFO_FULL_SHIFT** (line 101)
- **IS_M_RX_THLD_SHIFT** (line 102)
- **IS_M_START_BUSY_SHIFT** (line 103)
- **IS_M_TX_UNDERRUN_SHIFT** (line 104)
- **IS_OFFSET** (line 100)
- **IS_S_RD_EVENT_SHIFT** (line 110)
- **IS_S_RX_EVENT_SHIFT** (line 107)
- **IS_S_RX_FIFO_FULL_SHIFT** (line 105)
- **IS_S_RX_THLD_SHIFT** (line 106)
- **IS_S_START_BUSY_SHIFT** (line 108)
- **IS_S_TX_UNDERRUN_SHIFT** (line 109)
- **MAX_SLAVE_RX_PER_INT** (line 157)
- **M_CMD_OFFSET** (line 59)
- **M_CMD_PEC_SHIFT** (line 76)
- **M_CMD_PROTOCOL_BLK_RD** (line 74)
- **M_CMD_PROTOCOL_BLK_WR** (line 73)
- **M_CMD_PROTOCOL_MASK** (line 71)
- **M_CMD_PROTOCOL_PROCESS** (line 75)
- **M_CMD_PROTOCOL_QUICK** (line 72)
- **M_CMD_PROTOCOL_SHIFT** (line 70)
- **M_CMD_RD_CNT_MASK** (line 78)
- **M_CMD_RD_CNT_SHIFT** (line 77)
- **M_CMD_START_BUSY_SHIFT** (line 60)
- **M_CMD_STATUS_FIFO_UNDERRUN** (line 68)
- **M_CMD_STATUS_LOST_ARB** (line 64)
- **M_CMD_STATUS_MASK** (line 62)
- **M_CMD_STATUS_NACK_ADDR** (line 65)
- **M_CMD_STATUS_NACK_DATA** (line 66)
- **M_CMD_STATUS_RX_FIFO_FULL** (line 69)
- **M_CMD_STATUS_SHIFT** (line 61)
- **M_CMD_STATUS_SUCCESS** (line 63)
- **M_CMD_STATUS_TIMEOUT** (line 67)
- **M_FIFO_CTRL_OFFSET** (line 43)
- **M_FIFO_RX_CNT_MASK** (line 47)
- **M_FIFO_RX_CNT_SHIFT** (line 46)
- **M_FIFO_RX_FLUSH_SHIFT** (line 44)
- **M_FIFO_RX_THLD_MASK** (line 49)
- **M_FIFO_RX_THLD_SHIFT** (line 48)
- **M_FIFO_TX_FLUSH_SHIFT** (line 45)
- **M_RX_DATA_MASK** (line 122)
- **M_RX_DATA_SHIFT** (line 121)
- **M_RX_FIFO_MAX_THLD_VALUE** (line 138)
- **M_RX_FIFO_THLD_VALUE** (line 141)
- **M_RX_MAX_READ_LEN** (line 140)
- **M_RX_OFFSET** (line 117)
- **M_RX_PEC_ERR_SHIFT** (line 120)
- **M_RX_STATUS_MASK** (line 119)
- **M_RX_STATUS_SHIFT** (line 118)
- **M_TX_DATA_MASK** (line 115)
- **M_TX_DATA_SHIFT** (line 114)
- **M_TX_OFFSET** (line 112)
- **M_TX_RX_FIFO_SIZE** (line 137)
- **M_TX_WR_STATUS_SHIFT** (line 113)
- **SLAVE_CLOCK_STRETCH_TIME** (line 149)
- **SLAVE_MAX_SIZE_TRANSACTION** (line 148)
- **SLAVE_READ_WRITE_BIT_MASK** (line 146)
- **SLAVE_READ_WRITE_BIT_SHIFT** (line 147)
- **S_CFG_EN_NIC_SMB_ADDR0_SHIFT** (line 39)
- **S_CFG_EN_NIC_SMB_ADDR1_SHIFT** (line 36)
- **S_CFG_EN_NIC_SMB_ADDR2_SHIFT** (line 33)
- **S_CFG_EN_NIC_SMB_ADDR3_SHIFT** (line 30)
- **S_CFG_NIC_SMB_ADDR0_MASK** (line 41)
- **S_CFG_NIC_SMB_ADDR0_SHIFT** (line 40)
- **S_CFG_NIC_SMB_ADDR1_MASK** (line 38)
- **S_CFG_NIC_SMB_ADDR1_SHIFT** (line 37)
- **S_CFG_NIC_SMB_ADDR2_MASK** (line 35)
- **S_CFG_NIC_SMB_ADDR2_SHIFT** (line 34)
- **S_CFG_NIC_SMB_ADDR3_MASK** (line 32)
- **S_CFG_NIC_SMB_ADDR3_SHIFT** (line 31)
- **S_CFG_SMBUS_ADDR_OFFSET** (line 29)
- **S_CMD_OFFSET** (line 80)
- **S_CMD_START_BUSY_SHIFT** (line 81)
- **S_CMD_STATUS_MASK** (line 83)
- **S_CMD_STATUS_MASTER_ABORT** (line 86)
- **S_CMD_STATUS_SHIFT** (line 82)
- **S_CMD_STATUS_SUCCESS** (line 84)
- **S_CMD_STATUS_TIMEOUT** (line 85)
- **S_FIFO_CTRL_OFFSET** (line 51)
- **S_FIFO_RX_CNT_MASK** (line 55)
- **S_FIFO_RX_CNT_SHIFT** (line 54)
- **S_FIFO_RX_FLUSH_SHIFT** (line 52)
- **S_FIFO_RX_THLD_MASK** (line 57)
- **S_FIFO_RX_THLD_SHIFT** (line 56)
- **S_FIFO_TX_FLUSH_SHIFT** (line 53)
- **S_RX_DATA_MASK** (line 134)
- **S_RX_DATA_SHIFT** (line 133)
- **S_RX_OFFSET** (line 129)
- **S_RX_PEC_ERR_SHIFT** (line 132)
- **S_RX_STATUS_MASK** (line 131)
- **S_RX_STATUS_SHIFT** (line 130)
- **S_TX_DATA_MASK** (line 127)
- **S_TX_DATA_SHIFT** (line 126)
- **S_TX_OFFSET** (line 124)
- **S_TX_WR_STATUS_SHIFT** (line 125)
- **TIM_CFG_MODE_400_SHIFT** (line 23)
- **TIM_CFG_OFFSET** (line 22)
- **TIM_PERIODIC_SLAVE_STRETCH_MASK** (line 27)
- **TIM_PERIODIC_SLAVE_STRETCH_SHIFT** (line 26)
- **TIM_RAND_SLAVE_STRETCH_MASK** (line 25)
- **TIM_RAND_SLAVE_STRETCH_SHIFT** (line 24)
