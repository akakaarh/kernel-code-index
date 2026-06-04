# drivers/mmc/host/moxart-mmc.c

Subsystem: drivers/mmc

## Functions (15)

### moxart_dma_complete
- Return type: static void
- Signature: moxart_dma_complete(void * param)
- Line: 250

### moxart_get_ro
- Return type: static int
- Signature: moxart_get_ro(struct mmc_host * mmc)
- Line: 535

### moxart_init_sg
- Return type: static void
- Signature: moxart_init_sg(struct moxart_host * host,struct mmc_data * data)
- Line: 151

### moxart_irq
- Return type: static irqreturn_t
- Signature: moxart_irq(int irq,void * devid)
- Line: 461

### moxart_next_sg
- Return type: static int
- Signature: moxart_next_sg(struct moxart_host * host)
- Line: 162

### moxart_prepare_data
- Return type: static void
- Signature: moxart_prepare_data(struct moxart_host * host)
- Line: 363

### moxart_probe
- Return type: static int
- Signature: moxart_probe(struct platform_device * pdev)
- Line: 548

### moxart_remove
- Return type: static void
- Signature: moxart_remove(struct platform_device * pdev)
- Line: 684

### moxart_request
- Return type: static void
- Signature: moxart_request(struct mmc_host * mmc,struct mmc_request * mrq)
- Line: 393

### moxart_send_command
- Return type: static void
- Signature: moxart_send_command(struct moxart_host * host,struct mmc_command * cmd)
- Line: 204

### moxart_set_ios
- Return type: static void
- Signature: moxart_set_ios(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 488

### moxart_transfer_dma
- Return type: static void
- Signature: moxart_transfer_dma(struct mmc_data * data,struct moxart_host * host)
- Line: 262

### moxart_transfer_pio
- Return type: static void
- Signature: moxart_transfer_pio(struct moxart_host * host)
- Line: 310

### moxart_use_dma
- Return type: static bool
- Signature: moxart_use_dma(struct moxart_host * host)
- Line: 257

### moxart_wait_for_status
- Return type: static int
- Signature: moxart_wait_for_status(struct moxart_host * host,u32 mask,u32 * status)
- Line: 180

## Structs (1)

### moxart_host
- Line: 122
- Members:
  - lock: spinlock_t
  - base: void __iomem *
  - reg_phys: phys_addr_t
  - dma_chan_tx: dma_chan *
  - dma_chan_rx: dma_chan *
  - tx_desc: dma_async_tx_descriptor *
  - mmc: mmc_host *
  - mrq: mmc_request *
  - cur_sg: scatterlist *
  - dma_complete: completion
  - pio_complete: completion
  - num_sg: u32
  - data_remain: u32
  - data_len: u32
  - fifo_width: u32
  - timeout: u32
  - rate: u32
  - sysclk: long
  - have_dma: bool
  - is_removed: bool

## Variables (3)

- static **moxart_mmc_driver** : platform_driver (line 708)
- static **moxart_mmc_match** : const struct of_device_id[] (line 701)
- static **moxart_ops** : const struct mmc_host_ops (line 542)

## Macros (62)

- **BUS_WIDTH_1** (line 116)
- **BUS_WIDTH_4** (line 115)
- **BUS_WIDTH_4_SUPPORT** (line 114)
- **CARD_CHANGE** (line 83)
- **CARD_DETECT** (line 81)
- **CLK_DIV_MASK** (line 111)
- **CLK_HISPD** (line 108)
- **CLK_OFF** (line 109)
- **CLK_SD** (line 110)
- **CMD_APP_CMD** (line 59)
- **CMD_EN** (line 58)
- **CMD_IDX_MASK** (line 62)
- **CMD_LONG_RSP** (line 60)
- **CMD_NEED_RSP** (line 61)
- **CMD_SDC_RESET** (line 57)
- **CMD_SENT** (line 87)
- **DATA_CRC_FAIL** (line 92)
- **DATA_CRC_OK** (line 88)
- **DATA_END** (line 86)
- **DATA_LEN_MASK** (line 77)
- **DATA_TIMEOUT** (line 90)
- **DCR_BLK_SIZE** (line 74)
- **DCR_DATA_EN** (line 71)
- **DCR_DATA_FIFO_RESET** (line 69)
- **DCR_DATA_THRES** (line 70)
- **DCR_DATA_WRITE** (line 73)
- **DCR_DMA_EN** (line 72)
- **FIFO_ORUN** (line 84)
- **FIFO_URUN** (line 85)
- **MASK_DATA** (line 98)
- **MASK_INTR_PIO** (line 101)
- **MASK_RSP** (line 95)
- **MAX_RETRIES** (line 120)
- **MIN_POWER** (line 119)
- **MMC_VDD_360** (line 118)
- **REG_ARGUMENT** (line 37)
- **REG_BUS_WIDTH** (line 51)
- **REG_CLEAR** (line 47)
- **REG_CLOCK_CONTROL** (line 50)
- **REG_COMMAND** (line 36)
- **REG_DATA_CONTROL** (line 43)
- **REG_DATA_LENGTH** (line 45)
- **REG_DATA_TIMER** (line 44)
- **REG_DATA_WINDOW** (line 52)
- **REG_FEATURE** (line 53)
- **REG_INTERRUPT_MASK** (line 48)
- **REG_POWER_CONTROL** (line 49)
- **REG_RESPONSE0** (line 38)
- **REG_RESPONSE1** (line 39)
- **REG_RESPONSE2** (line 40)
- **REG_RESPONSE3** (line 41)
- **REG_RESPONSE_COMMAND** (line 42)
- **REG_REVISION** (line 54)
- **REG_STATUS** (line 46)
- **RSP_CMD_APP** (line 65)
- **RSP_CMD_IDX_MASK** (line 66)
- **RSP_CRC_FAIL** (line 93)
- **RSP_CRC_OK** (line 89)
- **RSP_TIMEOUT** (line 91)
- **SD_POWER_MASK** (line 105)
- **SD_POWER_ON** (line 104)
- **WRITE_PROT** (line 80)
