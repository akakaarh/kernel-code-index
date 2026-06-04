# drivers/mmc/host/sunxi-mmc.c

Subsystem: drivers/mmc

## Functions (30)

### sunxi_mmc_calibrate
- Return type: static int
- Signature: sunxi_mmc_calibrate(struct sunxi_mmc_host * host,int reg_off)
- Line: 703

### sunxi_mmc_card_busy
- Return type: static int
- Signature: sunxi_mmc_card_busy(struct mmc_host * mmc)
- Line: 1105

### sunxi_mmc_card_power
- Return type: static void
- Signature: sunxi_mmc_card_power(struct sunxi_mmc_host * host,struct mmc_ios * ios)
- Line: 902

### sunxi_mmc_clk_set_phase
- Return type: static int
- Signature: sunxi_mmc_clk_set_phase(struct sunxi_mmc_host * host,struct mmc_ios * ios,u32 rate)
- Line: 722

### sunxi_mmc_clk_set_rate
- Return type: static int
- Signature: sunxi_mmc_clk_set_rate(struct sunxi_mmc_host * host,struct mmc_ios * ios)
- Line: 760

### sunxi_mmc_disable
- Return type: static void
- Signature: sunxi_mmc_disable(struct sunxi_mmc_host * host)
- Line: 1287

### sunxi_mmc_dump_errinfo
- Return type: static void
- Signature: sunxi_mmc_dump_errinfo(struct sunxi_mmc_host * host)
- Line: 483

### sunxi_mmc_enable
- Return type: static int
- Signature: sunxi_mmc_enable(struct sunxi_mmc_host * host)
- Line: 1226

### sunxi_mmc_enable_sdio_irq
- Return type: static void
- Signature: sunxi_mmc_enable_sdio_irq(struct mmc_host * mmc,int enable)
- Line: 974

### sunxi_mmc_finalize_request
- Return type: static irqreturn_t
- Signature: sunxi_mmc_finalize_request(struct sunxi_mmc_host * host)
- Line: 511

### sunxi_mmc_handle_manual_stop
- Return type: static irqreturn_t
- Signature: sunxi_mmc_handle_manual_stop(int irq,void * dev_id)
- Line: 625

### sunxi_mmc_hw_reset
- Return type: static void
- Signature: sunxi_mmc_hw_reset(struct mmc_host * mmc)
- Line: 1000

### sunxi_mmc_init_host
- Return type: static int
- Signature: sunxi_mmc_init_host(struct sunxi_mmc_host * host)
- Line: 324

### sunxi_mmc_init_idma_des
- Return type: static void
- Signature: sunxi_mmc_init_idma_des(struct sunxi_mmc_host * host,struct mmc_data * data)
- Line: 359

### sunxi_mmc_irq
- Return type: static irqreturn_t
- Signature: sunxi_mmc_irq(int irq,void * dev_id)
- Line: 568

### sunxi_mmc_map_dma
- Return type: static int
- Signature: sunxi_mmc_map_dma(struct sunxi_mmc_host * host,struct mmc_data * data)
- Line: 398

### sunxi_mmc_oclk_onoff
- Return type: static int
- Signature: sunxi_mmc_oclk_onoff(struct sunxi_mmc_host * host,u32 oclk_en)
- Line: 661

### sunxi_mmc_probe
- Return type: static int
- Signature: sunxi_mmc_probe(struct platform_device * pdev)
- Line: 1366

### sunxi_mmc_remove
- Return type: static void
- Signature: sunxi_mmc_remove(struct platform_device * pdev)
- Line: 1484

### sunxi_mmc_request
- Return type: static void
- Signature: sunxi_mmc_request(struct mmc_host * mmc,struct mmc_request * mrq)
- Line: 1009

### sunxi_mmc_reset_host
- Return type: static int
- Signature: sunxi_mmc_reset_host(struct sunxi_mmc_host * host)
- Line: 306

### sunxi_mmc_resource_request
- Return type: static int
- Signature: sunxi_mmc_resource_request(struct sunxi_mmc_host * host,struct platform_device * pdev)
- Line: 1300

### sunxi_mmc_runtime_resume
- Return type: static int
- Signature: sunxi_mmc_runtime_resume(struct device * dev)
- Line: 1498

### sunxi_mmc_runtime_suspend
- Return type: static int
- Signature: sunxi_mmc_runtime_suspend(struct device * dev)
- Line: 1516

### sunxi_mmc_send_manual_stop
- Return type: static void
- Signature: sunxi_mmc_send_manual_stop(struct sunxi_mmc_host * host,struct mmc_request * req)
- Line: 445

### sunxi_mmc_set_bus_width
- Return type: static void
- Signature: sunxi_mmc_set_bus_width(struct sunxi_mmc_host * host,unsigned char width)
- Line: 869

### sunxi_mmc_set_clk
- Return type: static void
- Signature: sunxi_mmc_set_clk(struct sunxi_mmc_host * host,struct mmc_ios * ios)
- Line: 885

### sunxi_mmc_set_ios
- Return type: static void
- Signature: sunxi_mmc_set_ios(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 948

### sunxi_mmc_start_dma
- Return type: static void
- Signature: sunxi_mmc_start_dma(struct sunxi_mmc_host * host,struct mmc_data * data)
- Line: 423

### sunxi_mmc_volt_switch
- Return type: static int
- Signature: sunxi_mmc_volt_switch(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 957

## Structs (4)

### sunxi_idma_des
- Line: 239
- Members:
  - output: u32
  - sample: u32
  - config: __le32
  - buf_size: __le32
  - buf_addr_ptr1: __le32
  - buf_addr_ptr2: __le32
  - idma_des_size_bits: u32
  - idma_des_shift: u32
  - clk_delays: const struct sunxi_mmc_clk_delay *
  - can_calibrate: bool
  - mask_data0: bool
  - needs_new_timings: bool
  - ccu_has_timings_switch: bool
  - dev: device *
  - mmc: mmc_host *
  - reset: reset_control *
  - cfg: const struct sunxi_mmc_cfg *
  - reg_base: void __iomem *
  - clk_ahb: clk *
  - clk_mmc: clk *
  - clk_sample: clk *
  - clk_output: clk *
  - lock: spinlock_t
  - irq: int
  - int_sum: u32
  - sdio_imask: u32
  - sg_dma: dma_addr_t
  - sg_cpu: void *
  - wait_dma: bool
  - mrq: mmc_request *
  - manual_stop_mrq: mmc_request *
  - ferror: int
  - vqmmc_enabled: bool
  - use_new_timings: bool

### sunxi_mmc_cfg
- Line: 246
- Members:
  - output: u32
  - sample: u32
  - config: __le32
  - buf_size: __le32
  - buf_addr_ptr1: __le32
  - buf_addr_ptr2: __le32
  - idma_des_size_bits: u32
  - idma_des_shift: u32
  - clk_delays: const struct sunxi_mmc_clk_delay *
  - can_calibrate: bool
  - mask_data0: bool
  - needs_new_timings: bool
  - ccu_has_timings_switch: bool
  - dev: device *
  - mmc: mmc_host *
  - reset: reset_control *
  - cfg: const struct sunxi_mmc_cfg *
  - reg_base: void __iomem *
  - clk_ahb: clk *
  - clk_mmc: clk *
  - clk_sample: clk *
  - clk_output: clk *
  - lock: spinlock_t
  - irq: int
  - int_sum: u32
  - sdio_imask: u32
  - sg_dma: dma_addr_t
  - sg_cpu: void *
  - wait_dma: bool
  - mrq: mmc_request *
  - manual_stop_mrq: mmc_request *
  - ferror: int
  - vqmmc_enabled: bool
  - use_new_timings: bool

### sunxi_mmc_clk_delay
- Line: 234
- Members:
  - output: u32
  - sample: u32
  - config: __le32
  - buf_size: __le32
  - buf_addr_ptr1: __le32
  - buf_addr_ptr2: __le32
  - idma_des_size_bits: u32
  - idma_des_shift: u32
  - clk_delays: const struct sunxi_mmc_clk_delay *
  - can_calibrate: bool
  - mask_data0: bool
  - needs_new_timings: bool
  - ccu_has_timings_switch: bool
  - dev: device *
  - mmc: mmc_host *
  - reset: reset_control *
  - cfg: const struct sunxi_mmc_cfg *
  - reg_base: void __iomem *
  - clk_ahb: clk *
  - clk_mmc: clk *
  - clk_sample: clk *
  - clk_output: clk *
  - lock: spinlock_t
  - irq: int
  - int_sum: u32
  - sdio_imask: u32
  - sg_dma: dma_addr_t
  - sg_cpu: void *
  - wait_dma: bool
  - mrq: mmc_request *
  - manual_stop_mrq: mmc_request *
  - ferror: int
  - vqmmc_enabled: bool
  - use_new_timings: bool

### sunxi_mmc_host
- Line: 269
- Members:
  - output: u32
  - sample: u32
  - config: __le32
  - buf_size: __le32
  - buf_addr_ptr1: __le32
  - buf_addr_ptr2: __le32
  - idma_des_size_bits: u32
  - idma_des_shift: u32
  - clk_delays: const struct sunxi_mmc_clk_delay *
  - can_calibrate: bool
  - mask_data0: bool
  - needs_new_timings: bool
  - ccu_has_timings_switch: bool
  - dev: device *
  - mmc: mmc_host *
  - reset: reset_control *
  - cfg: const struct sunxi_mmc_cfg *
  - reg_base: void __iomem *
  - clk_ahb: clk *
  - clk_mmc: clk *
  - clk_sample: clk *
  - clk_output: clk *
  - lock: spinlock_t
  - irq: int
  - int_sum: u32
  - sdio_imask: u32
  - sg_dma: dma_addr_t
  - sg_cpu: void *
  - wait_dma: bool
  - mrq: mmc_request *
  - manual_stop_mrq: mmc_request *
  - ferror: int
  - vqmmc_enabled: bool
  - use_new_timings: bool

## Variables (16)

- static **sun20i_d1_cfg** : const struct sunxi_mmc_cfg (line 1171)
- static **sun4i_a10_cfg** : const struct sunxi_mmc_cfg (line 1140)
- static **sun50i_a100_emmc_cfg** : const struct sunxi_mmc_cfg (line 1202)
- static **sun50i_a64_cfg** : const struct sunxi_mmc_cfg (line 1179)
- static **sun50i_a64_emmc_cfg** : const struct sunxi_mmc_cfg (line 1187)
- static **sun50i_h616_cfg** : const struct sunxi_mmc_cfg (line 1194)
- static **sun5i_a13_cfg** : const struct sunxi_mmc_cfg (line 1146)
- static **sun7i_a20_cfg** : const struct sunxi_mmc_cfg (line 1152)
- static **sun8i_a83t_emmc_cfg** : const struct sunxi_mmc_cfg (line 1158)
- static **sun9i_a80_cfg** : const struct sunxi_mmc_cfg (line 1165)
- static **sun9i_mmc_clk_delays** : const struct sunxi_mmc_clk_delay[] (line 1132)
- static **sunxi_mmc_clk_delays** : const struct sunxi_mmc_clk_delay[] (line 1123)
- static **sunxi_mmc_driver** : platform_driver (line 1538)
- static **sunxi_mmc_of_match** : const struct of_device_id[] (line 1210)
- static **sunxi_mmc_ops** : const struct mmc_host_ops (line 1112)
- static **sunxi_mmc_pm_ops** : const struct dev_pm_ops (line 1533)

## Macros (151)

- **SDXC_2X_TIMING_MODE** (line 223)
- **SDXC_ABORT_READ_DATA** (line 172)
- **SDXC_ACCESS_BY_AHB** (line 93)
- **SDXC_ACCESS_BY_DMA** (line 94)
- **SDXC_ACCESS_DONE_DIRECT** (line 92)
- **SDXC_ALT_BOOT_OPTIONS** (line 123)
- **SDXC_AUTO_COMMAND_DONE** (line 144)
- **SDXC_BOOT_ABORT** (line 125)
- **SDXC_BOOT_ACK_EXPIRE** (line 124)
- **SDXC_CAL_DL_MASK** (line 230)
- **SDXC_CAL_DL_SHIFT** (line 227)
- **SDXC_CAL_DL_SW_EN** (line 228)
- **SDXC_CAL_DL_SW_SHIFT** (line 229)
- **SDXC_CAL_DONE** (line 226)
- **SDXC_CAL_START** (line 225)
- **SDXC_CAL_TIMEOUT** (line 232)
- **SDXC_CARD_CLOCK_ON** (line 100)
- **SDXC_CARD_DATA_BUSY** (line 163)
- **SDXC_CARD_INSERT** (line 147)
- **SDXC_CARD_PRESENT** (line 162)
- **SDXC_CARD_REMOVE** (line 148)
- **SDXC_CCS_EXPIRE** (line 121)
- **SDXC_CEATA_DEV_IRQ_ENABLE** (line 175)
- **SDXC_CEATA_ON** (line 169)
- **SDXC_CHECK_RESPONSE_CRC** (line 111)
- **SDXC_CLK_25M** (line 218)
- **SDXC_CLK_400K** (line 217)
- **SDXC_CLK_50M** (line 219)
- **SDXC_CLK_50M_DDR** (line 220)
- **SDXC_CLK_50M_DDR_8BIT** (line 221)
- **SDXC_COMMAND_DONE** (line 132)
- **SDXC_DATA_CRC_ERROR** (line 137)
- **SDXC_DATA_EXPIRE** (line 112)
- **SDXC_DATA_FSM_BUSY** (line 164)
- **SDXC_DATA_OVER** (line 133)
- **SDXC_DATA_TIMEOUT** (line 139)
- **SDXC_DDR_MODE** (line 90)
- **SDXC_DEBOUNCE_ENABLE_BIT** (line 88)
- **SDXC_DMA_ENABLE_BIT** (line 87)
- **SDXC_DMA_REQUEST** (line 165)
- **SDXC_DMA_RESET** (line 85)
- **SDXC_ENABLE_BIT_BOOT** (line 122)
- **SDXC_END_BIT_ERROR** (line 145)
- **SDXC_FIFO_EMPTY** (line 160)
- **SDXC_FIFO_FULL** (line 161)
- **SDXC_FIFO_RESET** (line 84)
- **SDXC_FIFO_RUN_ERROR** (line 141)
- **SDXC_FIFO_SIZE** (line 166)
- **SDXC_HARDWARE_RESET** (line 95)
- **SDXC_HARD_WARE_LOCKED** (line 142)
- **SDXC_IDMAC_ABNORMAL_INTERRUPT_SUM** (line 190)
- **SDXC_IDMAC_CARD_ERROR_SUM** (line 188)
- **SDXC_IDMAC_DES0_CES** (line 214)
- **SDXC_IDMAC_DES0_CH** (line 212)
- **SDXC_IDMAC_DES0_DIC** (line 209)
- **SDXC_IDMAC_DES0_ER** (line 213)
- **SDXC_IDMAC_DES0_FD** (line 211)
- **SDXC_IDMAC_DES0_LD** (line 210)
- **SDXC_IDMAC_DES0_OWN** (line 215)
- **SDXC_IDMAC_DESC_CHECK** (line 195)
- **SDXC_IDMAC_DESC_CLOSE** (line 200)
- **SDXC_IDMAC_DESC_READ** (line 194)
- **SDXC_IDMAC_DESTINATION_INVALID** (line 187)
- **SDXC_IDMAC_FATAL_BUS_ERROR** (line 186)
- **SDXC_IDMAC_FIX_BURST** (line 179)
- **SDXC_IDMAC_HOST_ABORT_INTERRUPT** (line 191)
- **SDXC_IDMAC_IDLE** (line 192)
- **SDXC_IDMAC_IDMA_ON** (line 180)
- **SDXC_IDMAC_NORMAL_INTERRUPT_SUM** (line 189)
- **SDXC_IDMAC_READ** (line 198)
- **SDXC_IDMAC_READ_REQUEST_WAIT** (line 196)
- **SDXC_IDMAC_RECEIVE_INTERRUPT** (line 185)
- **SDXC_IDMAC_REFETCH_DES** (line 181)
- **SDXC_IDMAC_SOFT_RESET** (line 178)
- **SDXC_IDMAC_SUSPEND** (line 193)
- **SDXC_IDMAC_TRANSMIT_INTERRUPT** (line 184)
- **SDXC_IDMAC_WRITE** (line 199)
- **SDXC_IDMAC_WRITE_REQUEST_WAIT** (line 197)
- **SDXC_INTERRUPT_DONE_BIT** (line 153)
- **SDXC_INTERRUPT_ENABLE_BIT** (line 86)
- **SDXC_INTERRUPT_ERROR_BIT** (line 149)
- **SDXC_LONG_RESPONSE** (line 110)
- **SDXC_LOW_POWER_ON** (line 101)
- **SDXC_MASK_DATA0** (line 99)
- **SDXC_MEMORY_ACCESS_DONE** (line 91)
- **SDXC_POSEDGE_LATCH_DATA** (line 89)
- **SDXC_READ_CEATA_DEV** (line 120)
- **SDXC_REG_A12A** (line 71)
- **SDXC_REG_BBCR** (line 60)
- **SDXC_REG_BCNTR** (line 46)
- **SDXC_REG_BLKSZ** (line 45)
- **SDXC_REG_CARG** (line 48)
- **SDXC_REG_CBCR** (line 59)
- **SDXC_REG_CBDA** (line 68)
- **SDXC_REG_CHDA** (line 67)
- **SDXC_REG_CLKCR** (line 42)
- **SDXC_REG_CMDR** (line 47)
- **SDXC_REG_DBGC** (line 61)
- **SDXC_REG_DLBA** (line 64)
- **SDXC_REG_DMAC** (line 63)
- **SDXC_REG_DRV_DL** (line 73)
- **SDXC_REG_DS_DL_REG** (line 75)
- **SDXC_REG_FTRGL** (line 57)
- **SDXC_REG_FUNS** (line 58)
- **SDXC_REG_GCTRL** (line 41)
- **SDXC_REG_HWRST** (line 62)
- **SDXC_REG_IDIE** (line 66)
- **SDXC_REG_IDST** (line 65)
- **SDXC_REG_IMASK** (line 53)
- **SDXC_REG_MISTA** (line 54)
- **SDXC_REG_RESP0** (line 49)
- **SDXC_REG_RESP1** (line 50)
- **SDXC_REG_RESP2** (line 51)
- **SDXC_REG_RESP3** (line 52)
- **SDXC_REG_RINTR** (line 55)
- **SDXC_REG_SAMP_DL_REG** (line 74)
- **SDXC_REG_SD_NTSR** (line 72)
- **SDXC_REG_STAS** (line 56)
- **SDXC_REG_TMOUT** (line 43)
- **SDXC_REG_WIDTH** (line 44)
- **SDXC_RESP_CRC_ERROR** (line 136)
- **SDXC_RESP_ERROR** (line 131)
- **SDXC_RESP_EXPIRE** (line 109)
- **SDXC_RESP_TIMEOUT** (line 138)
- **SDXC_RXWL_FLAG** (line 158)
- **SDXC_RX_DATA_REQUEST** (line 135)
- **SDXC_SDIO_INTERRUPT** (line 146)
- **SDXC_SDIO_READ_WAIT** (line 171)
- **SDXC_SEND_AUTO_STOP** (line 115)
- **SDXC_SEND_AUTO_STOPCCSD** (line 174)
- **SDXC_SEND_CCSD** (line 173)
- **SDXC_SEND_INIT_SEQUENCE** (line 118)
- **SDXC_SEND_IRQ_RESPONSE** (line 170)
- **SDXC_SEQUENCE_MODE** (line 114)
- **SDXC_SOFT_RESET** (line 83)
- **SDXC_START** (line 128)
- **SDXC_START_BIT_ERROR** (line 143)
- **SDXC_STOP_ABORT_CMD** (line 117)
- **SDXC_TXWL_FLAG** (line 159)
- **SDXC_TX_DATA_REQUEST** (line 134)
- **SDXC_UPCLK_ONLY** (line 119)
- **SDXC_USE_HOLD_REGISTER** (line 127)
- **SDXC_VOLTAGE_CHANGE_DONE** (line 140)
- **SDXC_VOLTAGE_SWITCH** (line 126)
- **SDXC_WAIT_PRE_OVER** (line 116)
- **SDXC_WIDTH1** (line 104)
- **SDXC_WIDTH4** (line 105)
- **SDXC_WIDTH8** (line 106)
- **SDXC_WRITE** (line 113)
- **mmc_readl**(host,reg) (line 77)
- **mmc_writel**(host,reg,value) (line 79)
