# drivers/mmc/host/meson-gx-mmc.c

Subsystem: drivers/mmc

## Functions (37)

### __meson_mmc_enable_sdio_irq
- Return type: static void
- Signature: __meson_mmc_enable_sdio_irq(struct mmc_host * mmc,int enable)
- Line: 921

### meson_mmc_ack_sdio_irq
- Return type: static void
- Signature: meson_mmc_ack_sdio_irq(struct mmc_host * mmc)
- Line: 1120

### meson_mmc_bounce_buf_read
- Return type: static bool
- Signature: meson_mmc_bounce_buf_read(const struct mmc_data * data)
- Line: 282

### meson_mmc_card_busy
- Return type: static int
- Signature: meson_mmc_card_busy(struct mmc_host * mmc)
- Line: 1075

### meson_mmc_cfg_init
- Return type: static void
- Signature: meson_mmc_cfg_init(struct meson_host * host)
- Line: 1060

### meson_mmc_check_resampling
- Return type: static void
- Signature: meson_mmc_check_resampling(struct meson_host * host,struct mmc_ios * ios)
- Line: 581

### meson_mmc_clk_gate
- Return type: static void
- Signature: meson_mmc_clk_gate(struct meson_host * host)
- Line: 323

### meson_mmc_clk_init
- Return type: static int
- Signature: meson_mmc_clk_init(struct meson_host * host)
- Line: 419

### meson_mmc_clk_set
- Return type: static int
- Signature: meson_mmc_clk_set(struct meson_host * host,unsigned long rate,bool ddr)
- Line: 353

### meson_mmc_clk_ungate
- Return type: static void
- Signature: meson_mmc_clk_ungate(struct meson_host * host)
- Line: 340

### meson_mmc_copy_buffer
- Return type: static void
- Signature: meson_mmc_copy_buffer(struct meson_host * host,struct mmc_data * data,size_t buflen,bool to_buffer)
- Line: 744

### meson_mmc_desc_chain_mode
- Return type: static bool
- Signature: meson_mmc_desc_chain_mode(const struct mmc_data * data)
- Line: 277

### meson_mmc_desc_chain_transfer
- Return type: static void
- Signature: meson_mmc_desc_chain_transfer(struct mmc_host * mmc,u32 cmd_cfg)
- Line: 705

### meson_mmc_disable_resampling
- Return type: static void
- Signature: meson_mmc_disable_resampling(struct meson_host * host)
- Line: 507

### meson_mmc_enable_sdio_irq
- Return type: static void
- Signature: meson_mmc_enable_sdio_irq(struct mmc_host * mmc,int enable)
- Line: 1110

### meson_mmc_get_next_command
- Return type: static mmc_command *
- Signature: meson_mmc_get_next_command(struct mmc_command * cmd)
- Line: 217

### meson_mmc_get_timeout_msecs
- Return type: static unsigned int
- Signature: meson_mmc_get_timeout_msecs(struct mmc_data * data)
- Line: 205

### meson_mmc_get_transfer_mode
- Return type: static void
- Signature: meson_mmc_get_transfer_mode(struct mmc_host * mmc,struct mmc_request * mrq)
- Line: 228

### meson_mmc_irq
- Return type: static irqreturn_t
- Signature: meson_mmc_irq(int irq,void * dev_id)
- Line: 931

### meson_mmc_irq_thread
- Return type: static irqreturn_t
- Signature: meson_mmc_irq_thread(int irq,void * dev_id)
- Line: 1023

### meson_mmc_post_req
- Return type: static void
- Signature: meson_mmc_post_req(struct mmc_host * mmc,struct mmc_request * mrq,int err)
- Line: 307

### meson_mmc_pre_req
- Return type: static void
- Signature: meson_mmc_pre_req(struct mmc_host * mmc,struct mmc_request * mrq)
- Line: 288

### meson_mmc_prepare_ios_clock
- Return type: static int
- Signature: meson_mmc_prepare_ios_clock(struct meson_host * host,struct mmc_ios * ios)
- Line: 562

### meson_mmc_probe
- Return type: static int
- Signature: meson_mmc_probe(struct platform_device * pdev)
- Line: 1138

### meson_mmc_read_resp
- Return type: static void
- Signature: meson_mmc_read_resp(struct mmc_host * mmc,struct mmc_command * cmd)
- Line: 907

### meson_mmc_remove
- Return type: static void
- Signature: meson_mmc_remove(struct platform_device * pdev)
- Line: 1296

### meson_mmc_request
- Return type: static void
- Signature: meson_mmc_request(struct mmc_host * mmc,struct mmc_request * mrq)
- Line: 873

### meson_mmc_request_done
- Return type: static void
- Signature: meson_mmc_request_done(struct mmc_host * mmc,struct mmc_request * mrq)
- Line: 652

### meson_mmc_resampling_tuning
- Return type: static int
- Signature: meson_mmc_resampling_tuning(struct mmc_host * mmc,u32 opcode)
- Line: 526

### meson_mmc_reset_resampling
- Return type: static void
- Signature: meson_mmc_reset_resampling(struct meson_host * host)
- Line: 515

### meson_mmc_set_blksz
- Return type: static void
- Signature: meson_mmc_set_blksz(struct mmc_host * mmc,unsigned int blksz)
- Line: 663

### meson_mmc_set_ios
- Return type: static void
- Signature: meson_mmc_set_ios(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 594

### meson_mmc_set_response_bits
- Return type: static void
- Signature: meson_mmc_set_response_bits(struct mmc_command * cmd,u32 * cmd_cfg)
- Line: 688

### meson_mmc_start_cmd
- Return type: static void
- Signature: meson_mmc_start_cmd(struct mmc_host * mmc,struct mmc_command * cmd)
- Line: 790

### meson_mmc_validate_dram_access
- Return type: static int
- Signature: meson_mmc_validate_dram_access(struct mmc_host * mmc,struct mmc_data * data)
- Line: 855

### meson_mmc_voltage_switch
- Return type: static int
- Signature: meson_mmc_voltage_switch(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 1086

### meson_mmc_wait_desc_stop
- Return type: static int
- Signature: meson_mmc_wait_desc_stop(struct meson_host * host)
- Line: 1006

## Structs (3)

### meson_host
- Line: 151
- Members:
  - tx_delay_mask: unsigned int
  - rx_delay_mask: unsigned int
  - always_on: unsigned int
  - adjust: unsigned int
  - irq_sdio_sleep: unsigned int
  - cmd_cfg: u32
  - cmd_arg: u32
  - cmd_data: u32
  - cmd_resp: u32
  - dev: device *
  - data: const struct meson_mmc_data *
  - mmc: mmc_host *
  - cmd: mmc_command *
  - regs: void __iomem *
  - mux_clk: clk *
  - mmc_clk: clk *
  - req_rate: unsigned long
  - ddr: bool
  - dram_access_quirk: bool
  - pinctrl: pinctrl *
  - pins_clk_gate: pinctrl_state *
  - bounce_buf_size: unsigned int
  - bounce_buf: void *
  - bounce_iomem_buf: void __iomem *
  - bounce_dma_addr: dma_addr_t
  - descs: sd_emmc_desc *
  - descs_dma_addr: dma_addr_t
  - irq: int
  - needs_pre_post_req: bool
  - lock: spinlock_t

### meson_mmc_data
- Line: 136
- Members:
  - tx_delay_mask: unsigned int
  - rx_delay_mask: unsigned int
  - always_on: unsigned int
  - adjust: unsigned int
  - irq_sdio_sleep: unsigned int
  - cmd_cfg: u32
  - cmd_arg: u32
  - cmd_data: u32
  - cmd_resp: u32
  - dev: device *
  - data: const struct meson_mmc_data *
  - mmc: mmc_host *
  - cmd: mmc_command *
  - regs: void __iomem *
  - mux_clk: clk *
  - mmc_clk: clk *
  - req_rate: unsigned long
  - ddr: bool
  - dram_access_quirk: bool
  - pinctrl: pinctrl *
  - pins_clk_gate: pinctrl_state *
  - bounce_buf_size: unsigned int
  - bounce_buf: void *
  - bounce_iomem_buf: void __iomem *
  - bounce_dma_addr: dma_addr_t
  - descs: sd_emmc_desc *
  - descs_dma_addr: dma_addr_t
  - irq: int
  - needs_pre_post_req: bool
  - lock: spinlock_t

### sd_emmc_desc
- Line: 144
- Members:
  - tx_delay_mask: unsigned int
  - rx_delay_mask: unsigned int
  - always_on: unsigned int
  - adjust: unsigned int
  - irq_sdio_sleep: unsigned int
  - cmd_cfg: u32
  - cmd_arg: u32
  - cmd_data: u32
  - cmd_resp: u32
  - dev: device *
  - data: const struct meson_mmc_data *
  - mmc: mmc_host *
  - cmd: mmc_command *
  - regs: void __iomem *
  - mux_clk: clk *
  - mmc_clk: clk *
  - req_rate: unsigned long
  - ddr: bool
  - dram_access_quirk: bool
  - pinctrl: pinctrl *
  - pins_clk_gate: pinctrl_state *
  - bounce_buf_size: unsigned int
  - bounce_buf: void *
  - bounce_iomem_buf: void __iomem *
  - bounce_dma_addr: dma_addr_t
  - descs: sd_emmc_desc *
  - descs_dma_addr: dma_addr_t
  - irq: int
  - needs_pre_post_req: bool
  - lock: spinlock_t

## Variables (5)

- static **meson_axg_data** : const struct meson_mmc_data (line 1317)
- static **meson_gx_data** : const struct meson_mmc_data (line 1309)
- static **meson_mmc_driver** : platform_driver (line 1335)
- static **meson_mmc_of_match** : const struct of_device_id[] (line 1325)
- static **meson_mmc_ops** : const struct mmc_host_ops (line 1125)

## Macros (107)

- **ADJUST_ADJ_DELAY_MASK** (line 58)
- **ADJUST_ADJ_EN** (line 60)
- **ADJUST_DS_EN** (line 59)
- **CFG_AUTO_CLK** (line 84)
- **CFG_BLK_LEN_MASK** (line 78)
- **CFG_BUS_WIDTH_1** (line 74)
- **CFG_BUS_WIDTH_4** (line 75)
- **CFG_BUS_WIDTH_8** (line 76)
- **CFG_BUS_WIDTH_MASK** (line 73)
- **CFG_CHK_DS** (line 83)
- **CFG_CLK_ALWAYS_ON** (line 82)
- **CFG_DDR** (line 77)
- **CFG_ERR_ABORT** (line 85)
- **CFG_RC_CC_MASK** (line 80)
- **CFG_RESP_TIMEOUT_MASK** (line 79)
- **CFG_STOP_CLOCK** (line 81)
- **CLK_ALWAYS_ON**(h) (line 53)
- **CLK_CORE_PHASE_MASK** (line 36)
- **CLK_DIV_MASK** (line 34)
- **CLK_IRQ_SDIO_SLEEP**(h) (line 54)
- **CLK_PHASE_0** (line 39)
- **CLK_PHASE_180** (line 40)
- **CLK_RX_DELAY_MASK**(h) (line 52)
- **CLK_RX_PHASE_MASK** (line 38)
- **CLK_SRC_MASK** (line 35)
- **CLK_TX_DELAY_MASK**(h) (line 51)
- **CLK_TX_PHASE_MASK** (line 37)
- **CLK_V2_ALWAYS_ON** (line 43)
- **CLK_V2_IRQ_SDIO_SLEEP** (line 44)
- **CLK_V2_RX_DELAY_MASK** (line 42)
- **CLK_V2_TX_DELAY_MASK** (line 41)
- **CLK_V3_ALWAYS_ON** (line 48)
- **CLK_V3_IRQ_SDIO_SLEEP** (line 49)
- **CLK_V3_RX_DELAY_MASK** (line 47)
- **CLK_V3_TX_DELAY_MASK** (line 46)
- **CMD_CFG_BLOCK_MODE** (line 183)
- **CMD_CFG_CMD_INDEX_MASK** (line 195)
- **CMD_CFG_DATA_IO** (line 189)
- **CMD_CFG_DATA_NUM** (line 194)
- **CMD_CFG_DATA_WR** (line 190)
- **CMD_CFG_END_OF_CHAIN** (line 185)
- **CMD_CFG_ERROR** (line 196)
- **CMD_CFG_LENGTH_MASK** (line 182)
- **CMD_CFG_NO_CMD** (line 188)
- **CMD_CFG_NO_RESP** (line 187)
- **CMD_CFG_OWNER** (line 197)
- **CMD_CFG_R1B** (line 184)
- **CMD_CFG_RESP_128** (line 192)
- **CMD_CFG_RESP_NOCRC** (line 191)
- **CMD_CFG_RESP_NUM** (line 193)
- **CMD_CFG_TIMEOUT_MASK** (line 186)
- **CMD_DATA_BIG_ENDIAN** (line 200)
- **CMD_DATA_MASK** (line 199)
- **CMD_DATA_SRAM** (line 201)
- **CMD_RESP_MASK** (line 202)
- **CMD_RESP_SRAM** (line 203)
- **DRIVER_NAME** (line 31)
- **IRQ_CRC_ERR** (line 97)
- **IRQ_DESC_ERR** (line 95)
- **IRQ_DESC_TIMEOUT** (line 100)
- **IRQ_END_OF_CHAIN** (line 103)
- **IRQ_EN_MASK** (line 106)
- **IRQ_RESP_ERR** (line 96)
- **IRQ_RESP_STATUS** (line 104)
- **IRQ_RESP_TIMEOUT** (line 99)
- **IRQ_RXD_ERR_MASK** (line 93)
- **IRQ_SDIO** (line 105)
- **IRQ_TIMEOUTS** (line 101)
- **IRQ_TXD_ERR** (line 94)
- **MUX_CLK_NUM_PARENTS** (line 134)
- **SD_EMMC_ADJUST** (line 57)
- **SD_EMMC_CALOUT** (line 66)
- **SD_EMMC_CFG** (line 72)
- **SD_EMMC_CFG_BLK_SIZE** (line 124)
- **SD_EMMC_CFG_CMD_GAP** (line 128)
- **SD_EMMC_CFG_RESP_TIMEOUT** (line 125)
- **SD_EMMC_CLOCK** (line 33)
- **SD_EMMC_CMD_ARG** (line 110)
- **SD_EMMC_CMD_CFG** (line 109)
- **SD_EMMC_CMD_DAT** (line 111)
- **SD_EMMC_CMD_RSP** (line 112)
- **SD_EMMC_CMD_RSP1** (line 113)
- **SD_EMMC_CMD_RSP2** (line 114)
- **SD_EMMC_CMD_RSP3** (line 115)
- **SD_EMMC_CMD_TIMEOUT** (line 126)
- **SD_EMMC_CMD_TIMEOUT_DATA** (line 127)
- **SD_EMMC_DELAY** (line 56)
- **SD_EMMC_DELAY1** (line 62)
- **SD_EMMC_DELAY2** (line 63)
- **SD_EMMC_DESC_BUF_LEN** (line 129)
- **SD_EMMC_DESC_CHAIN_MODE** (line 132)
- **SD_EMMC_IRQ_EN** (line 92)
- **SD_EMMC_LAST_REG** (line 119)
- **SD_EMMC_PRE_REQ_DONE** (line 131)
- **SD_EMMC_RXD** (line 117)
- **SD_EMMC_SRAM_DATA_BUF_LEN** (line 121)
- **SD_EMMC_SRAM_DATA_BUF_OFF** (line 122)
- **SD_EMMC_START** (line 67)
- **SD_EMMC_STATUS** (line 87)
- **SD_EMMC_TXD** (line 118)
- **SD_EMMC_V3_ADJUST** (line 64)
- **START_DESC_ADDR_MASK** (line 70)
- **START_DESC_BUSY** (line 69)
- **START_DESC_INIT** (line 68)
- **STATUS_BUSY** (line 88)
- **STATUS_DATI** (line 90)
- **STATUS_DESC_BUSY** (line 89)
