# drivers/mmc/host/owl-mmc.c

Subsystem: drivers/mmc

## Functions (16)

### owl_irq_handler
- Return type: static irqreturn_t
- Signature: owl_irq_handler(int irq,void * devid)
- Line: 135

### owl_mmc_ctr_reset
- Return type: static void
- Signature: owl_mmc_ctr_reset(struct owl_mmc_host * owl_host)
- Line: 457

### owl_mmc_dma_complete
- Return type: static void
- Signature: owl_mmc_dma_complete(void * param)
- Line: 284

### owl_mmc_finish_request
- Return type: static void
- Signature: owl_mmc_finish_request(struct owl_mmc_host * owl_host)
- Line: 155

### owl_mmc_power_on
- Return type: static void
- Signature: owl_mmc_power_on(struct owl_mmc_host * owl_host)
- Line: 464

### owl_mmc_prepare_data
- Return type: static int
- Signature: owl_mmc_prepare_data(struct owl_mmc_host * owl_host,struct mmc_data * data)
- Line: 293

### owl_mmc_probe
- Return type: static int
- Signature: owl_mmc_probe(struct platform_device * pdev)
- Line: 563

### owl_mmc_remove
- Return type: static void
- Signature: owl_mmc_remove(struct platform_device * pdev)
- Line: 661

### owl_mmc_request
- Return type: static void
- Signature: owl_mmc_request(struct mmc_host * mmc,struct mmc_request * mrq)
- Line: 340

### owl_mmc_send_cmd
- Return type: static void
- Signature: owl_mmc_send_cmd(struct owl_mmc_host * owl_host,struct mmc_command * cmd,struct mmc_data * data)
- Line: 173

### owl_mmc_set_bus_width
- Return type: static void
- Signature: owl_mmc_set_bus_width(struct owl_mmc_host * owl_host,struct mmc_ios * ios)
- Line: 436

### owl_mmc_set_clk
- Return type: static void
- Signature: owl_mmc_set_clk(struct owl_mmc_host * owl_host,struct mmc_ios * ios)
- Line: 427

### owl_mmc_set_clk_rate
- Return type: static int
- Signature: owl_mmc_set_clk_rate(struct owl_mmc_host * owl_host,unsigned int rate)
- Line: 388

### owl_mmc_set_ios
- Return type: static void
- Signature: owl_mmc_set_ios(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 485

### owl_mmc_start_signal_voltage_switch
- Return type: static int
- Signature: owl_mmc_start_signal_voltage_switch(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 533

### owl_mmc_update_reg
- Return type: static void
- Signature: owl_mmc_update_reg(void __iomem * reg,unsigned int val,bool state)
- Line: 121

## Structs (1)

### owl_mmc_host
- Line: 98
- Members:
  - dev: device *
  - reset: reset_control *
  - base: void __iomem *
  - clk: clk *
  - sdc_complete: completion
  - lock: spinlock_t
  - irq: int
  - clock: u32
  - ddr_50: bool
  - dma_dir: dma_data_direction
  - dma: dma_chan *
  - desc: dma_async_tx_descriptor *
  - dma_cfg: dma_slave_config
  - dma_complete: completion
  - mmc: mmc_host *
  - mrq: mmc_request *
  - cmd: mmc_command *
  - data: mmc_data *

## Variables (3)

- static **owl_mmc_driver** : platform_driver (line 677)
- static **owl_mmc_of_match** : const struct of_device_id[] (line 671)
- static **owl_mmc_ops** : const struct mmc_host_ops (line 555)

## Macros (61)

- **OWL_CMD_TIMEOUT_MS** (line 96)
- **OWL_REG_SD_ARG** (line 32)
- **OWL_REG_SD_BLK_NUM** (line 40)
- **OWL_REG_SD_BLK_SIZE** (line 39)
- **OWL_REG_SD_BUF_SIZE** (line 41)
- **OWL_REG_SD_CMD** (line 31)
- **OWL_REG_SD_CTL** (line 29)
- **OWL_REG_SD_DAT** (line 38)
- **OWL_REG_SD_EN** (line 28)
- **OWL_REG_SD_RSPBUF0** (line 33)
- **OWL_REG_SD_RSPBUF1** (line 34)
- **OWL_REG_SD_RSPBUF2** (line 35)
- **OWL_REG_SD_RSPBUF3** (line 36)
- **OWL_REG_SD_RSPBUF4** (line 37)
- **OWL_REG_SD_STATE** (line 30)
- **OWL_SD_CTL_C7EN** (line 67)
- **OWL_SD_CTL_CMDLEN** (line 62)
- **OWL_SD_CTL_DELAY_MSK** (line 59)
- **OWL_SD_CTL_LBE** (line 66)
- **OWL_SD_CTL_RDELAY**(x) (line 60)
- **OWL_SD_CTL_SCC** (line 63)
- **OWL_SD_CTL_TCN**(x) (line 64)
- **OWL_SD_CTL_TM**(x) (line 68)
- **OWL_SD_CTL_TOUTCNT**(x) (line 58)
- **OWL_SD_CTL_TOUTEN** (line 57)
- **OWL_SD_CTL_TS** (line 65)
- **OWL_SD_CTL_WDELAY**(x) (line 61)
- **OWL_SD_DELAY_HIGH_CLK** (line 72)
- **OWL_SD_DELAY_LOW_CLK** (line 70)
- **OWL_SD_DELAY_MID_CLK** (line 71)
- **OWL_SD_ENABLE** (line 50)
- **OWL_SD_EN_BSEL** (line 51)
- **OWL_SD_EN_CLK_S** (line 49)
- **OWL_SD_EN_DAT1_S** (line 48)
- **OWL_SD_EN_DATAWID**(x) (line 54)
- **OWL_SD_EN_DDREN** (line 53)
- **OWL_SD_EN_RANE** (line 44)
- **OWL_SD_EN_RAN_SEED**(x) (line 45)
- **OWL_SD_EN_RESE** (line 47)
- **OWL_SD_EN_S18EN** (line 46)
- **OWL_SD_EN_SDIOEN** (line 52)
- **OWL_SD_RDELAY_DDR50** (line 73)
- **OWL_SD_STATE_BAEP** (line 81)
- **OWL_SD_STATE_CLC** (line 91)
- **OWL_SD_STATE_CLNR** (line 90)
- **OWL_SD_STATE_CMDS** (line 83)
- **OWL_SD_STATE_CRC7ER** (line 94)
- **OWL_SD_STATE_DAT0S** (line 87)
- **OWL_SD_STATE_DAT1AS** (line 84)
- **OWL_SD_STATE_DAT1BS** (line 77)
- **OWL_SD_STATE_MEMRDY** (line 82)
- **OWL_SD_STATE_RC16ER** (line 93)
- **OWL_SD_STATE_SDIOA_EN** (line 86)
- **OWL_SD_STATE_SDIOA_P** (line 85)
- **OWL_SD_STATE_SDIOB_EN** (line 79)
- **OWL_SD_STATE_SDIOB_P** (line 78)
- **OWL_SD_STATE_TEI** (line 89)
- **OWL_SD_STATE_TEIE** (line 88)
- **OWL_SD_STATE_TOUTE** (line 80)
- **OWL_SD_STATE_WC16ER** (line 92)
- **OWL_SD_WDELAY_DDR50** (line 74)
