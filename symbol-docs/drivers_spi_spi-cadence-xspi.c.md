# drivers/spi/spi-cadence-xspi.c

Subsystem: drivers/spi

## Functions (33)

### cdns_mrvl_xspi_setup_clock
- Return type: static bool
- Signature: cdns_mrvl_xspi_setup_clock(struct cdns_xspi_dev * cdns_xspi,int requested_clk)
- Line: 428

### cdns_xspi_adjust_mem_op_size
- Return type: static int
- Signature: cdns_xspi_adjust_mem_op_size(struct spi_mem * mem,struct spi_mem_op * op)
- Line: 829

### cdns_xspi_check_command_status
- Return type: static int
- Signature: cdns_xspi_check_command_status(struct cdns_xspi_dev * cdns_xspi)
- Line: 493

### cdns_xspi_configure_phy
- Return type: static bool
- Signature: cdns_xspi_configure_phy(struct cdns_xspi_dev * cdns_xspi)
- Line: 404

### cdns_xspi_controller_init
- Return type: static int
- Signature: cdns_xspi_controller_init(struct cdns_xspi_dev * cdns_xspi)
- Line: 559

### cdns_xspi_finish_read
- Return type: static void
- Signature: cdns_xspi_finish_read(struct cdns_xspi_dev * cdns_xspi,u8 ** buffer,u32 data_count)
- Line: 978

### cdns_xspi_irq_handler
- Return type: static irqreturn_t
- Signature: cdns_xspi_irq_handler(int this_irq,void * dev)
- Line: 851

### cdns_xspi_is_dll_locked
- Return type: static bool
- Signature: cdns_xspi_is_dll_locked(struct cdns_xspi_dev * cdns_xspi)
- Line: 394

### cdns_xspi_is_sdma_ready
- Return type: static bool
- Signature: cdns_xspi_is_sdma_ready(struct cdns_xspi_dev * cdns_xspi,bool sleep)
- Line: 1018

### cdns_xspi_is_stig_ready
- Return type: static bool
- Signature: cdns_xspi_is_stig_ready(struct cdns_xspi_dev * cdns_xspi,bool sleep)
- Line: 1006

### cdns_xspi_mem_op
- Return type: static int
- Signature: cdns_xspi_mem_op(struct cdns_xspi_dev * cdns_xspi,struct spi_mem * mem,const struct spi_mem_op * op)
- Line: 739

### cdns_xspi_mem_op_execute
- Return type: static int
- Signature: cdns_xspi_mem_op_execute(struct spi_mem * mem,const struct spi_mem_op * op)
- Line: 752

### cdns_xspi_of_get_plat_data
- Return type: static int
- Signature: cdns_xspi_of_get_plat_data(struct platform_device * pdev)
- Line: 892

### cdns_xspi_prepare_generic
- Return type: static int
- Signature: cdns_xspi_prepare_generic(int cs,const void * dout,int len,int glue,u32 * cmd_regs)
- Line: 932

### cdns_xspi_prepare_transfer
- Return type: static int
- Signature: cdns_xspi_prepare_transfer(int cs,int dir,int len,u32 * cmd_regs)
- Line: 995

### cdns_xspi_print_phy_config
- Return type: static void
- Signature: cdns_xspi_print_phy_config(struct cdns_xspi_dev * cdns_xspi)
- Line: 915

### cdns_xspi_probe
- Return type: static int
- Signature: cdns_xspi_probe(struct platform_device * pdev)
- Line: 1130

### cdns_xspi_reset_dll
- Return type: static void
- Signature: cdns_xspi_reset_dll(struct cdns_xspi_dev * cdns_xspi)
- Line: 383

### cdns_xspi_resume
- Return type: static int
- Signature: cdns_xspi_resume(struct device * dev)
- Line: 1262

### cdns_xspi_sdma_handle
- Return type: static void
- Signature: cdns_xspi_sdma_handle(struct cdns_xspi_dev * cdns_xspi)
- Line: 581

### cdns_xspi_send_stig_command
- Return type: static int
- Signature: cdns_xspi_send_stig_command(struct cdns_xspi_dev * cdns_xspi,const struct spi_mem_op * op,bool data_phase)
- Line: 675

### cdns_xspi_set_interrupts
- Return type: static void
- Signature: cdns_xspi_set_interrupts(struct cdns_xspi_dev * cdns_xspi,bool enabled)
- Line: 529

### cdns_xspi_supports_op
- Return type: static bool
- Signature: cdns_xspi_supports_op(struct spi_mem * mem,const struct spi_mem_op * op)
- Line: 778

### cdns_xspi_suspend
- Return type: static int
- Signature: cdns_xspi_suspend(struct device * dev)
- Line: 1255

### cdns_xspi_transfer_one_message_b0
- Return type: static int
- Signature: cdns_xspi_transfer_one_message_b0(struct spi_controller * controller,struct spi_message * m)
- Line: 1030

### cdns_xspi_trigger_command
- Return type: static void
- Signature: cdns_xspi_trigger_command(struct cdns_xspi_dev * cdns_xspi,u32 cmd_regs[6])
- Line: 482

### cdns_xspi_wait_for_controller_idle
- Return type: static int
- Signature: cdns_xspi_wait_for_controller_idle(struct cdns_xspi_dev * cdns_xspi)
- Line: 470

### m_ioreadq
- Return type: static void
- Signature: m_ioreadq(void __iomem * addr,void * buf,int len)
- Line: 603

### m_iowriteq
- Return type: static void
- Signature: m_iowriteq(void __iomem * addr,const void * buf,int len)
- Line: 629

### marvell_xspi_mem_op_execute
- Return type: static int
- Signature: marvell_xspi_mem_op_execute(struct spi_mem * mem,const struct spi_mem_op * op)
- Line: 764

### marvell_xspi_read_single_qword
- Return type: static void
- Signature: marvell_xspi_read_single_qword(struct cdns_xspi_dev * cdns_xspi,u8 ** buffer)
- Line: 961

### marvell_xspi_sdma_handle
- Return type: static void
- Signature: marvell_xspi_sdma_handle(struct cdns_xspi_dev * cdns_xspi)
- Line: 653

### marvell_xspi_set_interrupts
- Return type: static void
- Signature: marvell_xspi_set_interrupts(struct cdns_xspi_dev * cdns_xspi,bool enabled)
- Line: 542

## Structs (2)

### cdns_xspi_dev
- Line: 351
- Members:
  - mrvl_hw_overlay: bool
  - dll_phy_ctrl: u32
  - ctb_rfile_phy_ctrl: u32
  - rfile_phy_tsel: u32
  - rfile_phy_dq_timing: u32
  - rfile_phy_dqs_timing: u32
  - rfile_phy_gate_lpbk_ctrl: u32
  - rfile_phy_dll_master_ctrl: u32
  - rfile_phy_dll_slave_ctrl: u32
  - pdev: platform_device *
  - host: spi_controller *
  - dev: device *
  - iobase: void __iomem *
  - auxbase: void __iomem *
  - sdmabase: void __iomem *
  - xferbase: void __iomem *
  - irq: int
  - cur_cs: int
  - sdmasize: unsigned int
  - cmd_complete: completion
  - auto_cmd_complete: completion
  - sdma_complete: completion
  - sdma_error: bool
  - in_buffer: void *
  - out_buffer: const void *
  - hw_num_banks: u8
  - driver_data: const struct cdns_xspi_driver_data *
  - sdma_handler: void (*)(struct cdns_xspi_dev * cdns_xspi)
  - set_interrupts_handler: void (*)(struct cdns_xspi_dev * cdns_xspi,bool enabled)
  - xfer_in_progress: bool
  - current_xfer_qword: int

### cdns_xspi_driver_data
- Line: 306
- Members:
  - mrvl_hw_overlay: bool
  - dll_phy_ctrl: u32
  - ctb_rfile_phy_ctrl: u32
  - rfile_phy_tsel: u32
  - rfile_phy_dq_timing: u32
  - rfile_phy_dqs_timing: u32
  - rfile_phy_gate_lpbk_ctrl: u32
  - rfile_phy_dll_master_ctrl: u32
  - rfile_phy_dll_slave_ctrl: u32
  - pdev: platform_device *
  - host: spi_controller *
  - dev: device *
  - iobase: void __iomem *
  - auxbase: void __iomem *
  - sdmabase: void __iomem *
  - xferbase: void __iomem *
  - irq: int
  - cur_cs: int
  - sdmasize: unsigned int
  - cmd_complete: completion
  - auto_cmd_complete: completion
  - sdma_complete: completion
  - sdma_error: bool
  - in_buffer: void *
  - out_buffer: const void *
  - hw_num_banks: u8
  - driver_data: const struct cdns_xspi_driver_data *
  - sdma_handler: void (*)(struct cdns_xspi_dev * cdns_xspi)
  - set_interrupts_handler: void (*)(struct cdns_xspi_dev * cdns_xspi,bool enabled)
  - xfer_in_progress: bool
  - current_xfer_qword: int

## Enums (3)

### cdns_xspi_sdma_dir
- Line: 296

### cdns_xspi_stig_cmd_dir
- Line: 301

### cdns_xspi_stig_instr_type
- Line: 290

## Variables (7)

- static **cadence_xspi_mem_ops** : const struct spi_controller_mem_ops (line 839)
- static **cdns_driver_data** : cdns_xspi_driver_data (line 330)
- static **cdns_mrvl_xspi_clk_div_list** : const int[] (line 334)
- static **cdns_xspi_of_match** : const struct of_device_id[] (line 1279)
- static **cdns_xspi_platform_driver** : platform_driver (line 1292)
- static **marvell_driver_data** : cdns_xspi_driver_data (line 318)
- static **marvell_xspi_mem_ops** : const struct spi_controller_mem_ops (line 845)

## Macros (148)

- **CDNS_XSPI_CCP_PHY_DLL_SLAVE_CTRL** (line 44)
- **CDNS_XSPI_CCP_PHY_DQS_TIMING** (line 38)
- **CDNS_XSPI_CCP_PHY_DQ_TIMING** (line 35)
- **CDNS_XSPI_CCP_PHY_GATE_LPBCK_CTRL** (line 41)
- **CDNS_XSPI_CDMA_TREE_EN** (line 74)
- **CDNS_XSPI_CMD_DSEQ_R2_DCNT_L** (line 132)
- **CDNS_XSPI_CMD_DSEQ_R3_DCNT_H** (line 133)
- **CDNS_XSPI_CMD_DSEQ_R3_NUM_OF_DUMMY** (line 134)
- **CDNS_XSPI_CMD_DSEQ_R4_BANK** (line 135)
- **CDNS_XSPI_CMD_DSEQ_R4_DATA_IOS** (line 136)
- **CDNS_XSPI_CMD_DSEQ_R4_DIR** (line 137)
- **CDNS_XSPI_CMD_FLD_DSEQ_CMD_1**(op) (line 176)
- **CDNS_XSPI_CMD_FLD_DSEQ_CMD_2**(op) (line 179)
- **CDNS_XSPI_CMD_FLD_DSEQ_CMD_3**(op,dummybytes) (line 182)
- **CDNS_XSPI_CMD_FLD_DSEQ_CMD_4**(op,chipsel) (line 190)
- **CDNS_XSPI_CMD_FLD_GENERIC_DSEQ_CMD_1** (line 213)
- **CDNS_XSPI_CMD_FLD_GENERIC_DSEQ_CMD_2**(nbytes) (line 216)
- **CDNS_XSPI_CMD_FLD_GENERIC_DSEQ_CMD_3**(nbytes) (line 219)
- **CDNS_XSPI_CMD_FLD_GENERIC_DSEQ_CMD_4**(dir,chipsel) (line 222)
- **CDNS_XSPI_CMD_FLD_P1_GENERIC_CMD** (line 201)
- **CDNS_XSPI_CMD_FLD_P1_INSTR_CMD_1**(op,data_phase) (line 154)
- **CDNS_XSPI_CMD_FLD_P1_INSTR_CMD_2**(op) (line 159)
- **CDNS_XSPI_CMD_FLD_P1_INSTR_CMD_3**(op,modebytes) (line 165)
- **CDNS_XSPI_CMD_FLD_P1_INSTR_CMD_4**(op,chipsel) (line 171)
- **CDNS_XSPI_CMD_FLD_P3_GENERIC_CMD**(len) (line 205)
- **CDNS_XSPI_CMD_FLD_P4_GENERIC_CMD**(cs,glue) (line 210)
- **CDNS_XSPI_CMD_IGNRD_EN** (line 72)
- **CDNS_XSPI_CMD_INSTR_TYPE** (line 118)
- **CDNS_XSPI_CMD_P1_R1_ADDR0** (line 119)
- **CDNS_XSPI_CMD_P1_R2_ADDR1** (line 120)
- **CDNS_XSPI_CMD_P1_R2_ADDR2** (line 121)
- **CDNS_XSPI_CMD_P1_R2_ADDR3** (line 122)
- **CDNS_XSPI_CMD_P1_R2_ADDR4** (line 123)
- **CDNS_XSPI_CMD_P1_R3_ADDR5** (line 124)
- **CDNS_XSPI_CMD_P1_R3_CMD** (line 125)
- **CDNS_XSPI_CMD_P1_R3_NUM_ADDR_BYTES** (line 126)
- **CDNS_XSPI_CMD_P1_R4_ADDR_IOS** (line 127)
- **CDNS_XSPI_CMD_P1_R4_BANK** (line 129)
- **CDNS_XSPI_CMD_P1_R4_CMD_IOS** (line 128)
- **CDNS_XSPI_CMD_REG_0** (line 50)
- **CDNS_XSPI_CMD_REG_1** (line 51)
- **CDNS_XSPI_CMD_REG_2** (line 52)
- **CDNS_XSPI_CMD_REG_3** (line 53)
- **CDNS_XSPI_CMD_REG_4** (line 54)
- **CDNS_XSPI_CMD_REG_5** (line 55)
- **CDNS_XSPI_CMD_STATUS_BUS_ERROR** (line 144)
- **CDNS_XSPI_CMD_STATUS_COMPLETED** (line 140)
- **CDNS_XSPI_CMD_STATUS_CRC_ERROR** (line 143)
- **CDNS_XSPI_CMD_STATUS_DQS_ERROR** (line 142)
- **CDNS_XSPI_CMD_STATUS_FAILED** (line 141)
- **CDNS_XSPI_CMD_STATUS_INV_SEQ_ERROR** (line 145)
- **CDNS_XSPI_CMD_STATUS_REG** (line 58)
- **CDNS_XSPI_CTRL_BUSY** (line 65)
- **CDNS_XSPI_CTRL_CONFIG_REG** (line 94)
- **CDNS_XSPI_CTRL_FEATURES_REG** (line 107)
- **CDNS_XSPI_CTRL_IDLE_EN** (line 75)
- **CDNS_XSPI_CTRL_REV** (line 115)
- **CDNS_XSPI_CTRL_STATUS_REG** (line 61)
- **CDNS_XSPI_CTRL_VERSION_REG** (line 113)
- **CDNS_XSPI_CTRL_WORK_MODE** (line 95)
- **CDNS_XSPI_DATASLICE_RFILE_PHY_DLL_OBS_REG_0** (line 245)
- **CDNS_XSPI_DDMA_TERR_EN** (line 73)
- **CDNS_XSPI_DLL_LOCK** (line 248)
- **CDNS_XSPI_DLL_PHY_CTRL** (line 47)
- **CDNS_XSPI_DLL_RST_N** (line 247)
- **CDNS_XSPI_DMA_DATA_WIDTH** (line 109)
- **CDNS_XSPI_INIT_COMPLETED** (line 62)
- **CDNS_XSPI_INIT_FAIL** (line 64)
- **CDNS_XSPI_INIT_LEGACY** (line 63)
- **CDNS_XSPI_INTR_EN** (line 83)
- **CDNS_XSPI_INTR_ENABLE_REG** (line 82)
- **CDNS_XSPI_INTR_MASK** (line 88)
- **CDNS_XSPI_INTR_STATUS_REG** (line 68)
- **CDNS_XSPI_MAGIC_NUM** (line 114)
- **CDNS_XSPI_MAGIC_NUM_VALUE** (line 25)
- **CDNS_XSPI_MAX_BANKS** (line 26)
- **CDNS_XSPI_NAME** (line 27)
- **CDNS_XSPI_NUM_BANKS** (line 108)
- **CDNS_XSPI_NUM_THREADS** (line 110)
- **CDNS_XSPI_PHY_CTB_RFILE_PHY_CTRL** (line 238)
- **CDNS_XSPI_PHY_CTB_RFILE_PHY_TSEL** (line 239)
- **CDNS_XSPI_PHY_DATASLICE_RFILE_PHY_DLL_MASTER_CTRL** (line 243)
- **CDNS_XSPI_PHY_DATASLICE_RFILE_PHY_DLL_SLAVE_CTRL** (line 244)
- **CDNS_XSPI_PHY_DATASLICE_RFILE_PHY_DQS_TIMING** (line 241)
- **CDNS_XSPI_PHY_DATASLICE_RFILE_PHY_DQ_TIMING** (line 240)
- **CDNS_XSPI_PHY_DATASLICE_RFILE_PHY_GATE_LPBK_CTRL** (line 242)
- **CDNS_XSPI_RF_MINICTRL_REGS_DLL_PHY_CTRL** (line 237)
- **CDNS_XSPI_SDMA_DIR** (line 104)
- **CDNS_XSPI_SDMA_ERROR** (line 70)
- **CDNS_XSPI_SDMA_ERROR_EN** (line 85)
- **CDNS_XSPI_SDMA_SIZE_REG** (line 102)
- **CDNS_XSPI_SDMA_TRD_INFO_REG** (line 103)
- **CDNS_XSPI_SDMA_TRIGGER** (line 71)
- **CDNS_XSPI_SDMA_TRIGGER_EN** (line 86)
- **CDNS_XSPI_STIG_DONE** (line 69)
- **CDNS_XSPI_STIG_DONE_EN** (line 84)
- **CDNS_XSPI_STIG_DONE_FLAG** (line 147)
- **CDNS_XSPI_TRD_COMP_INTR_STATUS** (line 77)
- **CDNS_XSPI_TRD_ERR_INTR_EN** (line 79)
- **CDNS_XSPI_TRD_ERR_INTR_STATUS** (line 78)
- **CDNS_XSPI_TRD_STATUS** (line 148)
- **CDNS_XSPI_WORK_MODE_ACMD** (line 99)
- **CDNS_XSPI_WORK_MODE_DIRECT** (line 97)
- **CDNS_XSPI_WORK_MODE_STIG** (line 98)
- **CMD_REG_LEN** (line 199)
- **GENERIC_BANK_NUM** (line 208)
- **GENERIC_CMD_DATA_1_OFFSET**(position) (line 285)
- **GENERIC_CMD_DATA_2_OFFSET**(position) (line 284)
- **GENERIC_CMD_DATA_3_OFFSET**(position) (line 283)
- **GENERIC_CMD_DATA_INSERT**(data,pos) (line 286)
- **GENERIC_CMD_DATA_REG_1_COUNT**(len) (line 282)
- **GENERIC_CMD_DATA_REG_2_COUNT**(len) (line 281)
- **GENERIC_CMD_DATA_REG_3_COUNT**(len) (line 280)
- **GENERIC_CMD_REG_2_NEEDED**(len) (line 288)
- **GENERIC_CMD_REG_3_NEEDED**(len) (line 287)
- **GENERIC_GLUE_CMD** (line 209)
- **GENERIC_NUM_OF_BYTES** (line 204)
- **INSTRUCTION_TYPE_GENERIC** (line 200)
- **MARVELL_CTB_RFILE_PHY_CTRL** (line 228)
- **MARVELL_REGS_DLL_PHY_CTRL** (line 227)
- **MARVELL_RFILE_PHY_DLL_MASTER_CTRL** (line 233)
- **MARVELL_RFILE_PHY_DLL_SLAVE_CTRL** (line 234)
- **MARVELL_RFILE_PHY_DQS_TIMING** (line 231)
- **MARVELL_RFILE_PHY_DQ_TIMING** (line 230)
- **MARVELL_RFILE_PHY_GATE_LPBK_CTRL** (line 232)
- **MARVELL_RFILE_PHY_TSEL** (line 229)
- **MODEBYTES_COUNT** (line 151)
- **MODE_NO_OF_BYTES** (line 150)
- **MRVL_DEFAULT_CLK** (line 257)
- **MRVL_XFER_CLK_CAPTURE_POL** (line 266)
- **MRVL_XFER_CLK_DRIVE_POL** (line 267)
- **MRVL_XFER_CS_N_HOLD** (line 263)
- **MRVL_XFER_FUNC_CTRL** (line 260)
- **MRVL_XFER_FUNC_CTRL_READ_DATA**(i) (line 261)
- **MRVL_XFER_FUNC_ENABLE** (line 265)
- **MRVL_XFER_FUNC_START** (line 268)
- **MRVL_XFER_QWORD_BYTECOUNT** (line 270)
- **MRVL_XFER_QWORD_COUNT** (line 269)
- **MRVL_XFER_RECEIVE_ENABLE** (line 264)
- **MRVL_XFER_SOFT_RESET** (line 262)
- **MRVL_XSPI_CLK_CTRL_AUX_REG** (line 251)
- **MRVL_XSPI_CLK_DIV** (line 253)
- **MRVL_XSPI_CLK_ENABLE** (line 252)
- **MRVL_XSPI_CLOCK_DIVIDED**(div) (line 256)
- **MRVL_XSPI_CLOCK_IO_HZ** (line 255)
- **MRVL_XSPI_IRQ_ENABLE** (line 254)
- **MRVL_XSPI_POLL_DELAY_US** (line 273)
- **MRVL_XSPI_POLL_TIMEOUT_US** (line 272)
