# drivers/i2c/busses/i2c-mchp-pci1xxxx.c

Subsystem: drivers/i2c

## Functions (37)

### pci1xxxx_ack_high_level_intr
- Return type: static void
- Signature: pci1xxxx_ack_high_level_intr(struct pci1xxxx_i2c * i2c,u16 intr_msk)
- Line: 364

### pci1xxxx_ack_nw_layer_intr
- Return type: static void
- Signature: pci1xxxx_ack_nw_layer_intr(struct pci1xxxx_i2c * i2c,u8 ack_intr_msk)
- Line: 573

### pci1xxxx_config_nw_layer_intr
- Return type: static void
- Signature: pci1xxxx_config_nw_layer_intr(struct pci1xxxx_i2c * i2c,u8 intr_msk,bool enable)
- Line: 578

### pci1xxxx_i2c_buffer_write
- Return type: static void
- Signature: pci1xxxx_i2c_buffer_write(struct pci1xxxx_i2c * i2c,u8 slaveaddr,u8 transferlen,unsigned char * buf)
- Line: 417

### pci1xxxx_i2c_clear_flags
- Return type: static void
- Signature: pci1xxxx_i2c_clear_flags(struct pci1xxxx_i2c * i2c)
- Line: 763

### pci1xxxx_i2c_config_asr
- Return type: static void
- Signature: pci1xxxx_i2c_config_asr(struct pci1xxxx_i2c * i2c,bool enable)
- Line: 505

### pci1xxxx_i2c_config_high_level_intr
- Return type: static void
- Signature: pci1xxxx_i2c_config_high_level_intr(struct pci1xxxx_i2c * i2c,u16 intr_msk,bool enable)
- Line: 630

### pci1xxxx_i2c_config_padctrl
- Return type: static void
- Signature: pci1xxxx_i2c_config_padctrl(struct pci1xxxx_i2c * i2c,bool enable)
- Line: 593

### pci1xxxx_i2c_configure_core_reg
- Return type: static void
- Signature: pci1xxxx_i2c_configure_core_reg(struct pci1xxxx_i2c * i2c,bool enable)
- Line: 644

### pci1xxxx_i2c_configure_smbalert_pin
- Return type: static void
- Signature: pci1xxxx_i2c_configure_smbalert_pin(struct pci1xxxx_i2c * i2c,bool enable)
- Line: 369

### pci1xxxx_i2c_enable_ESO
- Return type: static void
- Signature: pci1xxxx_i2c_enable_ESO(struct pci1xxxx_i2c * i2c)
- Line: 434

### pci1xxxx_i2c_get_funcs
- Return type: static u32
- Signature: pci1xxxx_i2c_get_funcs(struct i2c_adapter * adap)
- Line: 1039

### pci1xxxx_i2c_init
- Return type: static void
- Signature: pci1xxxx_i2c_init(struct pci1xxxx_i2c * i2c)
- Line: 706

### pci1xxxx_i2c_isr
- Return type: static irqreturn_t
- Signature: pci1xxxx_i2c_isr(int irq,void * dev)
- Line: 518

### pci1xxxx_i2c_probe_pci
- Return type: static int
- Signature: pci1xxxx_i2c_probe_pci(struct pci_dev * pdev,const struct pci_device_id * ent)
- Line: 1129

### pci1xxxx_i2c_read
- Return type: static int
- Signature: pci1xxxx_i2c_read(struct pci1xxxx_i2c * i2c,u8 slaveaddr,unsigned char * buf,u16 total_len)
- Line: 778

### pci1xxxx_i2c_reset_counters
- Return type: static void
- Signature: pci1xxxx_i2c_reset_counters(struct pci1xxxx_i2c * i2c)
- Line: 439

### pci1xxxx_i2c_resume
- Return type: static int
- Signature: pci1xxxx_i2c_resume(struct device * dev)
- Line: 1099

### pci1xxxx_i2c_send_start_stop
- Return type: static void
- Signature: pci1xxxx_i2c_send_start_stop(struct pci1xxxx_i2c * i2c,bool start)
- Line: 385

### pci1xxxx_i2c_set_DMA_run
- Return type: static void
- Signature: pci1xxxx_i2c_set_DMA_run(struct pci1xxxx_i2c * i2c)
- Line: 478

### pci1xxxx_i2c_set_clear_FW_ACK
- Return type: static void
- Signature: pci1xxxx_i2c_set_clear_FW_ACK(struct pci1xxxx_i2c * i2c,bool set)
- Line: 405

### pci1xxxx_i2c_set_count
- Return type: static void
- Signature: pci1xxxx_i2c_set_count(struct pci1xxxx_i2c * i2c,u8 mcucount,u8 writecount,u8 readcount)
- Line: 551

### pci1xxxx_i2c_set_freq
- Return type: static void
- Signature: pci1xxxx_i2c_set_freq(struct pci1xxxx_i2c * i2c)
- Line: 665

### pci1xxxx_i2c_set_mcu_count
- Return type: static void
- Signature: pci1xxxx_i2c_set_mcu_count(struct pci1xxxx_i2c * i2c,u8 count)
- Line: 463

### pci1xxxx_i2c_set_mode
- Return type: static void
- Signature: pci1xxxx_i2c_set_mode(struct pci1xxxx_i2c * i2c)
- Line: 616

### pci1xxxx_i2c_set_mrun_proceed
- Return type: static void
- Signature: pci1xxxx_i2c_set_mrun_proceed(struct pci1xxxx_i2c * i2c)
- Line: 488

### pci1xxxx_i2c_set_read_count
- Return type: static void
- Signature: pci1xxxx_i2c_set_read_count(struct pci1xxxx_i2c * i2c,u8 readcount)
- Line: 468

### pci1xxxx_i2c_set_readm
- Return type: static void
- Signature: pci1xxxx_i2c_set_readm(struct pci1xxxx_i2c * i2c,bool enable)
- Line: 559

### pci1xxxx_i2c_set_transfer_dir
- Return type: static void
- Signature: pci1xxxx_i2c_set_transfer_dir(struct pci1xxxx_i2c * i2c,u8 direction)
- Line: 449

### pci1xxxx_i2c_set_write_count
- Return type: static void
- Signature: pci1xxxx_i2c_set_write_count(struct pci1xxxx_i2c * i2c,u8 writecount)
- Line: 473

### pci1xxxx_i2c_shutdown
- Return type: static void
- Signature: pci1xxxx_i2c_shutdown(void * data)
- Line: 1121

### pci1xxxx_i2c_start_DMA
- Return type: static void
- Signature: pci1xxxx_i2c_start_DMA(struct pci1xxxx_i2c * i2c)
- Line: 499

### pci1xxxx_i2c_suspend
- Return type: static int
- Signature: pci1xxxx_i2c_suspend(struct device * dev)
- Line: 1066

### pci1xxxx_i2c_write
- Return type: static int
- Signature: pci1xxxx_i2c_write(struct pci1xxxx_i2c * i2c,u8 slaveaddr,unsigned char * buf,u16 total_len)
- Line: 899

### pci1xxxx_i2c_xfer
- Return type: static int
- Signature: pci1xxxx_i2c_xfer(struct i2c_adapter * adap,struct i2c_msg * msgs,int num)
- Line: 992

### release_sys_lock
- Return type: static int
- Signature: release_sys_lock(struct pci1xxxx_i2c * i2c)
- Line: 347

### set_sys_lock
- Return type: static int
- Signature: set_sys_lock(struct pci1xxxx_i2c * i2c)
- Line: 334

## Structs (1)

### pci1xxxx_i2c
- Line: 325
- Members:
  - i2c_xfer_done: completion
  - i2c_xfer_in_progress: bool
  - adap: i2c_adapter
  - i2c_base: void __iomem *
  - freq: u32
  - flags: u32

## Variables (5)

- static **pci1xxxx_i2c_algo** : const struct i2c_algorithm (line 1050)
- static **pci1xxxx_i2c_ops** : const struct i2c_adapter (line 1059)
- static **pci1xxxx_i2c_pci_driver** : pci_driver (line 1199)
- static **pci1xxxx_i2c_pci_id_table** : const struct pci_device_id[] (line 1189)
- static **pci1xxxx_i2c_quirks** : const struct i2c_adapter_quirks (line 1055)

## Macros (143)

- **ALL_HIGH_LAYER_INTR** (line 295)
- **ALL_NW_LAYER_INTERRUPTS** (line 274)
- **BUS_CLK_1000K** (line 122)
- **BUS_CLK_1000K_HIGH_PERIOD_TICKS** (line 116)
- **BUS_CLK_1000K_LOW_PERIOD_TICKS** (line 108)
- **BUS_CLK_100K** (line 118)
- **BUS_CLK_100K_HIGH_PERIOD_TICKS** (line 114)
- **BUS_CLK_100K_LOW_PERIOD_TICKS** (line 106)
- **BUS_CLK_400K** (line 120)
- **BUS_CLK_400K_HIGH_PERIOD_TICKS** (line 115)
- **BUS_CLK_400K_LOW_PERIOD_TICKS** (line 107)
- **BUS_IDLE_MIN_1000K_TICKS** (line 195)
- **BUS_IDLE_MIN_100K_TICKS** (line 193)
- **BUS_IDLE_MIN_400K_TICKS** (line 194)
- **CLK_SYNC_1000K** (line 134)
- **CLK_SYNC_100K** (line 132)
- **CLK_SYNC_400K** (line 133)
- **CLOCK_HIGH_TIME_OUT_1000K_TICKS** (line 221)
- **CLOCK_HIGH_TIME_OUT_100K_TICKS** (line 219)
- **CLOCK_HIGH_TIME_OUT_400K_TICKS** (line 220)
- **COMPLETION_IDLE** (line 58)
- **COMPLETION_MDONE** (line 57)
- **COMPLETION_MNAKX** (line 59)
- **CTL_HOST_FIFO_ENTRY** (line 246)
- **CTL_RESET_COUNTERS** (line 244)
- **CTL_RUN** (line 247)
- **CTL_TRANSFER_DIR** (line 245)
- **CTRL_CUM_TIME_OUT_1000K_TICKS** (line 204)
- **CTRL_CUM_TIME_OUT_100K_TICKS** (line 202)
- **CTRL_CUM_TIME_OUT_400K_TICKS** (line 203)
- **DATA_HOLD_1000K_TICKS** (line 174)
- **DATA_HOLD_100K_TICKS** (line 172)
- **DATA_HOLD_400K_TICKS** (line 173)
- **DATA_TIMING_1000K** (line 182)
- **DATA_TIMING_100K** (line 176)
- **DATA_TIMING_400K** (line 179)
- **FAIR_BUS_IDLE_MIN_1000K_TICKS** (line 70)
- **FAIR_BUS_IDLE_MIN_100K_TICKS** (line 68)
- **FAIR_BUS_IDLE_MIN_400K_TICKS** (line 69)
- **FAIR_IDLE_DELAY_1000K_TICKS** (line 78)
- **FAIR_IDLE_DELAY_100K_TICKS** (line 76)
- **FAIR_IDLE_DELAY_400K_TICKS** (line 77)
- **FIRST_START_HOLD_1000K_TICKS** (line 147)
- **FIRST_START_HOLD_100K_TICKS** (line 145)
- **FIRST_START_HOLD_400K_TICKS** (line 146)
- **I2C_BUF_MSTR_INTR_MASK** (line 289)
- **I2C_BUF_MSTR_WAKE_INTR_MASK** (line 292)
- **I2C_DIRN_READ** (line 250)
- **I2C_DIRN_WRITE** (line 249)
- **I2C_FLAGS_DIRECT_MODE** (line 308)
- **I2C_FLAGS_POLLING_MODE** (line 309)
- **I2C_FLAGS_SMB_BLK_READ** (line 311)
- **I2C_FLAGS_STOP** (line 310)
- **I2C_FOD_EN** (line 236)
- **I2C_INPUT_EN** (line 239)
- **I2C_INTR_MASK** (line 290)
- **I2C_OUTPUT_EN** (line 240)
- **I2C_PULL_DOWN_EN** (line 238)
- **I2C_PULL_UP_EN** (line 237)
- **I2C_SCL_PAD_CTRL_REG_OFF** (line 233)
- **I2C_SDA_PAD_CTRL_REG_OFF** (line 234)
- **I2C_WAKE_INTR_MASK** (line 293)
- **INTR_MSK_BUF_EMPTY** (line 272)
- **INTR_MSK_BUF_FULL** (line 271)
- **INTR_MSK_DMA_TERM** (line 269)
- **INTR_MSK_THRESHOLD** (line 270)
- **INTR_STAT_BUF_EMPTY** (line 265)
- **INTR_STAT_BUF_FULL** (line 264)
- **INTR_STAT_DMA_TERM** (line 262)
- **INTR_STAT_THRESHOLD** (line 263)
- **PCI1XXXX_I2C_TIMEOUT_MS** (line 313)
- **PERI_SMBUS_D3_RESET_DIS** (line 302)
- **RESTART_SETUP_1000K_TICKS** (line 165)
- **RESTART_SETUP_100K_TICKS** (line 163)
- **RESTART_SETUP_400K_TICKS** (line 164)
- **SMBALERT_INTR_MASK** (line 288)
- **SMBALERT_MST_PAD_CTRL_REG_OFF** (line 280)
- **SMBALERT_MST_PU** (line 282)
- **SMBALERT_WAKE_INTR_MASK** (line 291)
- **SMBUS_BUF_MAX_SIZE** (line 306)
- **SMBUS_CONTROL_REG_OFF** (line 242)
- **SMBUS_GEN_INT_MASK_REG_OFF** (line 286)
- **SMBUS_GEN_INT_STAT_REG_OFF** (line 284)
- **SMBUS_INTR_MSK_REG_OFF** (line 267)
- **SMBUS_INTR_STAT_REG_OFF** (line 260)
- **SMBUS_MAST_CORE_ADDR_BASE** (line 22)
- **SMBUS_MAST_SYS_REG_ADDR_BASE** (line 23)
- **SMBUS_MCU_COUNTER_REG_OFF** (line 278)
- **SMBUS_MST_BUF** (line 304)
- **SMBUS_PERI_LOCK** (line 323)
- **SMBUS_RESET_REG** (line 300)
- **SMBUS_STATUS_REG_OFF** (line 252)
- **SMB_CONFIG1_ASR** (line 95)
- **SMB_CONFIG1_ENAB** (line 96)
- **SMB_CONFIG1_FEN** (line 98)
- **SMB_CONFIG1_RESET** (line 97)
- **SMB_CONFIG3_ENIDI** (line 90)
- **SMB_CONFIG3_ENMI** (line 89)
- **SMB_CORE_BUS_CLK_REG_OFF** (line 100)
- **SMB_CORE_CLK_SYNC_REG_OFF** (line 125)
- **SMB_CORE_CMD_M_PROCEED** (line 42)
- **SMB_CORE_CMD_M_RUN** (line 43)
- **SMB_CORE_CMD_READM** (line 36)
- **SMB_CORE_CMD_REG_OFF0** (line 40)
- **SMB_CORE_CMD_REG_OFF1** (line 34)
- **SMB_CORE_CMD_REG_OFF2** (line 33)
- **SMB_CORE_CMD_REG_OFF3** (line 32)
- **SMB_CORE_CMD_START** (line 38)
- **SMB_CORE_CMD_STOP** (line 37)
- **SMB_CORE_COMPLETION_REG_OFF3** (line 55)
- **SMB_CORE_CONFIG_REG1** (line 93)
- **SMB_CORE_CONFIG_REG2** (line 92)
- **SMB_CORE_CONFIG_REG3** (line 87)
- **SMB_CORE_CTRL_ACK** (line 30)
- **SMB_CORE_CTRL_ESO** (line 28)
- **SMB_CORE_CTRL_FW_ACK** (line 29)
- **SMB_CORE_CTRL_REG_OFF** (line 26)
- **SMB_CORE_DATA_TIMING_REG_OFF** (line 136)
- **SMB_CORE_IDLE_SCALING_REG_OFF** (line 61)
- **SMB_CORE_SR_HOLD_TIME_REG_OFF** (line 45)
- **SMB_CORE_TO_SCALING_REG_OFF** (line 186)
- **SMB_GPR_LOCK_REG** (line 320)
- **SMB_GPR_REG** (line 316)
- **SMB_IDLE_SCALING_1000K** (line 84)
- **SMB_IDLE_SCALING_100K** (line 80)
- **SMB_IDLE_SCALING_400K** (line 82)
- **SR_HOLD_TIME_1000K_TICKS** (line 53)
- **SR_HOLD_TIME_100K_TICKS** (line 51)
- **SR_HOLD_TIME_400K_TICKS** (line 52)
- **STA_BUF_EMPTY** (line 258)
- **STA_BUF_FULL** (line 257)
- **STA_DMA_REQ** (line 255)
- **STA_DMA_TERM** (line 254)
- **STA_THRESHOLD** (line 256)
- **STOP_SETUP_1000K_TICKS** (line 156)
- **STOP_SETUP_100K_TICKS** (line 154)
- **STOP_SETUP_400K_TICKS** (line 155)
- **TARGET_CUM_TIME_OUT_1000K_TICKS** (line 213)
- **TARGET_CUM_TIME_OUT_100K_TICKS** (line 211)
- **TARGET_CUM_TIME_OUT_400K_TICKS** (line 212)
- **TO_SCALING_1000K** (line 229)
- **TO_SCALING_100K** (line 223)
- **TO_SCALING_400K** (line 226)
