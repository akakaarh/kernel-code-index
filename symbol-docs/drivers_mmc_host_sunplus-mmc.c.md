# drivers/mmc/host/sunplus-mmc.c

Subsystem: drivers/mmc

## Functions (27)

### spmmc_check_error
- Return type: static int
- Signature: spmmc_check_error(struct spmmc_host * host,struct mmc_request * mrq)
- Line: 516

### spmmc_controller_init
- Return type: static void
- Signature: spmmc_controller_init(struct spmmc_host * host)
- Line: 666

### spmmc_drv_probe
- Return type: static int
- Signature: spmmc_drv_probe(struct platform_device * pdev)
- Line: 859

### spmmc_drv_remove
- Return type: static void
- Signature: spmmc_drv_remove(struct platform_device * dev)
- Line: 942

### spmmc_execute_tuning
- Return type: static int
- Signature: spmmc_execute_tuning(struct mmc_host * mmc,u32 opcode)
- Line: 803

### spmmc_find_best_delay
- Return type: static int
- Signature: spmmc_find_best_delay(u8 candidate_dly)
- Line: 609

### spmmc_finish_request
- Return type: static void
- Signature: spmmc_finish_request(struct spmmc_host * host,struct mmc_request * mrq)
- Line: 687

### spmmc_func_finish_req
- Return type: static irqreturn_t
- Signature: spmmc_func_finish_req(int irq,void * dev_id)
- Line: 850

### spmmc_get_cd
- Return type: static int
- Signature: spmmc_get_cd(struct mmc_host * mmc)
- Line: 790

### spmmc_get_rsp
- Return type: static void
- Signature: spmmc_get_rsp(struct spmmc_host * host,struct mmc_command * cmd)
- Line: 198

### spmmc_irq
- Return type: static irqreturn_t
- Signature: spmmc_irq(int irq,void * dev_id)
- Line: 713

### spmmc_pm_runtime_resume
- Return type: static int
- Signature: spmmc_pm_runtime_resume(struct device * dev)
- Line: 963

### spmmc_pm_runtime_suspend
- Return type: static int
- Signature: spmmc_pm_runtime_suspend(struct device * dev)
- Line: 953

### spmmc_prepare_cmd
- Return type: static void
- Signature: spmmc_prepare_cmd(struct spmmc_host * host,struct mmc_command * cmd)
- Line: 359

### spmmc_prepare_data
- Return type: static void
- Signature: spmmc_prepare_data(struct spmmc_host * host,struct mmc_data * data)
- Line: 401

### spmmc_request
- Return type: static void
- Signature: spmmc_request(struct mmc_host * mmc,struct mmc_request * mrq)
- Line: 727

### spmmc_send_stop_cmd
- Return type: static void
- Signature: spmmc_send_stop_cmd(struct spmmc_host * host)
- Line: 498

### spmmc_set_bus_clk
- Return type: static void
- Signature: spmmc_set_bus_clk(struct spmmc_host * host,int clk)
- Line: 231

### spmmc_set_bus_timing
- Return type: static void
- Signature: spmmc_set_bus_timing(struct spmmc_host * host,unsigned int timing)
- Line: 251

### spmmc_set_bus_width
- Return type: static void
- Signature: spmmc_set_bus_width(struct spmmc_host * host,int width)
- Line: 304

### spmmc_set_ios
- Return type: static void
- Signature: spmmc_set_ios(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 772

### spmmc_set_sdmmc_mode
- Return type: static void
- Signature: spmmc_set_sdmmc_mode(struct spmmc_host * host)
- Line: 328

### spmmc_sw_reset
- Return type: static void
- Signature: spmmc_sw_reset(struct spmmc_host * host)
- Line: 337

### spmmc_trigger_transaction
- Return type: static void
- Signature: spmmc_trigger_transaction(struct spmmc_host * host)
- Line: 490

### spmmc_wait_finish
- Return type: static int
- Signature: spmmc_wait_finish(struct spmmc_host * host)
- Line: 176

### spmmc_wait_sdstatus
- Return type: static int
- Signature: spmmc_wait_sdstatus(struct spmmc_host * host,unsigned int status_bit)
- Line: 185

### spmmc_xfer_data_pio
- Return type: static void
- Signature: spmmc_xfer_data_pio(struct spmmc_host * host,struct mmc_data * data)
- Line: 624

## Structs (2)

### spmmc_host
- Line: 163
- Members:
  - enable_tuning: int
  - need_tuning: int
  - retried: int
  - rd_crc_dly: u32:3
  - rd_dat_dly: u32:3
  - rd_rsp_dly: u32:3
  - wr_cmd_dly: u32:3
  - wr_dat_dly: u32:3
  - clk_dly: u32:3
  - base: void __iomem *
  - clk: clk *
  - rstc: reset_control *
  - mmc: mmc_host *
  - mrq: mmc_request *
  - irq: int
  - dmapio_mode: int
  - tuning_info: spmmc_tuning_info
  - dma_int_threshold: int
  - dma_use_int: int

### spmmc_tuning_info
- Line: 148
- Members:
  - enable_tuning: int
  - need_tuning: int
  - retried: int
  - rd_crc_dly: u32:3
  - rd_dat_dly: u32:3
  - rd_rsp_dly: u32:3
  - wr_cmd_dly: u32:3
  - wr_dat_dly: u32:3
  - clk_dly: u32:3
  - base: void __iomem *
  - clk: clk *
  - rstc: reset_control *
  - mmc: mmc_host *
  - mrq: mmc_request *
  - irq: int
  - dmapio_mode: int
  - tuning_info: spmmc_tuning_info
  - dma_int_threshold: int
  - dma_use_int: int

## Variables (3)

- static **spmmc_driver** : platform_driver (line 983)
- static **spmmc_of_table** : const struct of_device_id[] (line 975)
- static **spmmc_ops** : const struct mmc_host_ops (line 843)

## Macros (110)

- **SPMMC_CARD_MEDIATYPE_SRCDST_REG** (line 33)
- **SPMMC_CLOCK_DIVISION** (line 88)
- **SPMMC_CRCTOKEN_CHECK_RESULT** (line 120)
- **SPMMC_DMAIDLE** (line 45)
- **SPMMC_DMA_BASE_ADDR_REG** (line 42)
- **SPMMC_DMA_DESTINATION** (line 36)
- **SPMMC_DMA_MODE** (line 160)
- **SPMMC_DMA_SOURCE** (line 35)
- **SPMMC_DUMMY_CLOCK_TRIGGER** (line 96)
- **SPMMC_HW_DMA_CTRL_REG** (line 43)
- **SPMMC_HW_DMA_RST** (line 44)
- **SPMMC_INT_MULTI_TRIG** (line 91)
- **SPMMC_MAX_BLK_COUNT** (line 28)
- **SPMMC_MAX_CLK** (line 27)
- **SPMMC_MAX_DMA_MEMORY_SECTORS** (line 47)
- **SPMMC_MAX_RETRIES** (line 146)
- **SPMMC_MAX_TUNABLE_DLY** (line 29)
- **SPMMC_MEDIA_MS** (line 39)
- **SPMMC_MEDIA_NONE** (line 37)
- **SPMMC_MEDIA_SD** (line 38)
- **SPMMC_MEDIA_TYPE** (line 34)
- **SPMMC_MIN_CLK** (line 26)
- **SPMMC_MMC8_EN** (line 87)
- **SPMMC_NEW_COMMAND_TRIGGER** (line 95)
- **SPMMC_PIO_MODE** (line 161)
- **SPMMC_POLL_DELAY_US** (line 31)
- **SPMMC_RX4_EN** (line 85)
- **SPMMC_SDINT_SDCMP** (line 66)
- **SPMMC_SDINT_SDCMPCLR** (line 67)
- **SPMMC_SDINT_SDCMPEN** (line 65)
- **SPMMC_SDINT_SDIO** (line 69)
- **SPMMC_SDINT_SDIOCLR** (line 70)
- **SPMMC_SDINT_SDIOEN** (line 68)
- **SPMMC_SDIO_CTRL_REG** (line 90)
- **SPMMC_SDIO_MODE** (line 82)
- **SPMMC_SDRAM_SECTOR_0_SIZE_REG** (line 41)
- **SPMMC_SDRAM_SECTOR_1_ADDR_REG** (line 49)
- **SPMMC_SDRAM_SECTOR_1_LENG_REG** (line 50)
- **SPMMC_SDRAM_SECTOR_2_ADDR_REG** (line 51)
- **SPMMC_SDRAM_SECTOR_2_LENG_REG** (line 52)
- **SPMMC_SDRAM_SECTOR_3_ADDR_REG** (line 53)
- **SPMMC_SDRAM_SECTOR_3_LENG_REG** (line 54)
- **SPMMC_SDRAM_SECTOR_4_ADDR_REG** (line 55)
- **SPMMC_SDRAM_SECTOR_4_LENG_REG** (line 56)
- **SPMMC_SDRAM_SECTOR_5_ADDR_REG** (line 57)
- **SPMMC_SDRAM_SECTOR_5_LENG_REG** (line 58)
- **SPMMC_SDRAM_SECTOR_6_ADDR_REG** (line 59)
- **SPMMC_SDRAM_SECTOR_6_LENG_REG** (line 60)
- **SPMMC_SDRAM_SECTOR_7_ADDR_REG** (line 61)
- **SPMMC_SDRAM_SECTOR_7_LENG_REG** (line 62)
- **SPMMC_SDSTATE_ERROR** (line 121)
- **SPMMC_SDSTATE_FINISH** (line 122)
- **SPMMC_SDSTATUS_BOOT_ACK_ERROR** (line 117)
- **SPMMC_SDSTATUS_BOOT_ACK_TIMEOUT** (line 115)
- **SPMMC_SDSTATUS_BOOT_DATA_TIMEOUT** (line 116)
- **SPMMC_SDSTATUS_BUSY_CYCLE** (line 112)
- **SPMMC_SDSTATUS_CARD_CRC_CHECK_TIMEOUT** (line 106)
- **SPMMC_SDSTATUS_CMD_PIN_STATUS** (line 103)
- **SPMMC_SDSTATUS_CRC_TOKEN_CHECK_ERROR** (line 109)
- **SPMMC_SDSTATUS_DAT0_PIN_STATUS** (line 104)
- **SPMMC_SDSTATUS_DAT1_PIN_STATUS** (line 113)
- **SPMMC_SDSTATUS_DUMMY_READY** (line 99)
- **SPMMC_SDSTATUS_RDATA_CRC16_ERROR** (line 110)
- **SPMMC_SDSTATUS_RSP_BUF_FULL** (line 100)
- **SPMMC_SDSTATUS_RSP_CRC7_ERROR** (line 108)
- **SPMMC_SDSTATUS_RSP_TIMEOUT** (line 105)
- **SPMMC_SDSTATUS_RX_DATA_BUF_FULL** (line 102)
- **SPMMC_SDSTATUS_SD_SENSE_STATUS** (line 114)
- **SPMMC_SDSTATUS_STB_TIMEOUT** (line 107)
- **SPMMC_SDSTATUS_SUSPEND_STATE_READY** (line 111)
- **SPMMC_SDSTATUS_TX_DATA_BUF_EMPTY** (line 101)
- **SPMMC_SD_AUTO_RESPONSE** (line 79)
- **SPMMC_SD_BLOCKSIZE_REG** (line 125)
- **SPMMC_SD_CLOCK_DELAY** (line 132)
- **SPMMC_SD_CMDBUF0_3_REG** (line 141)
- **SPMMC_SD_CMDBUF4_REG** (line 142)
- **SPMMC_SD_CMD_DUMMY** (line 80)
- **SPMMC_SD_CONFIG0_REG** (line 74)
- **SPMMC_SD_CONFIG1_REG** (line 127)
- **SPMMC_SD_CTRL_REG** (line 94)
- **SPMMC_SD_DATA_WD** (line 84)
- **SPMMC_SD_DDR_MODE** (line 76)
- **SPMMC_SD_HIGH_SPEED_EN** (line 129)
- **SPMMC_SD_HW_STATE_REG** (line 124)
- **SPMMC_SD_INT_REG** (line 64)
- **SPMMC_SD_LEN_MODE** (line 77)
- **SPMMC_SD_MMC_MODE** (line 83)
- **SPMMC_SD_PAGE_NUM_REG** (line 72)
- **SPMMC_SD_PIODATARX_REG** (line 140)
- **SPMMC_SD_PIODATATX_REG** (line 139)
- **SPMMC_SD_PIO_MODE** (line 75)
- **SPMMC_SD_READ_CRC_DELAY** (line 137)
- **SPMMC_SD_READ_DATA_DELAY** (line 136)
- **SPMMC_SD_READ_RESPONSE_DELAY** (line 135)
- **SPMMC_SD_RSPBUF0_3_REG** (line 143)
- **SPMMC_SD_RSPBUF4_5_REG** (line 144)
- **SPMMC_SD_RSP_CHK_EN** (line 81)
- **SPMMC_SD_RSP_TYPE** (line 86)
- **SPMMC_SD_RST_REG** (line 93)
- **SPMMC_SD_STATE_REG** (line 119)
- **SPMMC_SD_STATUS_REG** (line 98)
- **SPMMC_SD_TIMING_CONFIG0_REG** (line 131)
- **SPMMC_SD_TRANS_MODE** (line 78)
- **SPMMC_SD_WRITE_COMMAND_DELAY** (line 134)
- **SPMMC_SD_WRITE_DATA_DELAY** (line 133)
- **SPMMC_TIMEOUT_US** (line 30)
- **SPMMC_TX_DUMMY_NUM** (line 128)
- **spmmc_wait_rspbuf_full**(host) (line 194)
- **spmmc_wait_rxbuf_full**(host) (line 195)
- **spmmc_wait_txbuf_empty**(host) (line 196)
