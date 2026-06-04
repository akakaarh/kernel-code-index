# drivers/mmc/host/litex_mmc.c

Subsystem: drivers/mmc

## Functions (15)

### litex_mmc_do_dma
- Return type: static void
- Signature: litex_mmc_do_dma(struct litex_mmc_host * host,struct mmc_data * data,unsigned int * len,bool * direct,u8 * transfer)
- Line: 291

### litex_mmc_get_cd
- Return type: static int
- Signature: litex_mmc_get_cd(struct mmc_host * mmc)
- Line: 235

### litex_mmc_interrupt
- Return type: static irqreturn_t
- Signature: litex_mmc_interrupt(int irq,void * arg)
- Line: 253

### litex_mmc_irq_init
- Return type: static int
- Signature: litex_mmc_irq_init(struct platform_device * pdev,struct litex_mmc_host * host)
- Line: 470

### litex_mmc_probe
- Return type: static int
- Signature: litex_mmc_probe(struct platform_device * pdev)
- Line: 509

### litex_mmc_remove
- Return type: static void
- Signature: litex_mmc_remove(struct platform_device * pdev)
- Line: 622

### litex_mmc_request
- Return type: static void
- Signature: litex_mmc_request(struct mmc_host * mmc,struct mmc_request * mrq)
- Line: 338

### litex_mmc_response_len
- Return type: static u32
- Signature: litex_mmc_response_len(struct mmc_command * cmd)
- Line: 280

### litex_mmc_sdcard_wait_done
- Return type: static int
- Signature: litex_mmc_sdcard_wait_done(void __iomem * reg,struct device * dev)
- Line: 102

### litex_mmc_send_app_cmd
- Return type: static int
- Signature: litex_mmc_send_app_cmd(struct litex_mmc_host * host)
- Line: 190

### litex_mmc_send_cmd
- Return type: static int
- Signature: litex_mmc_send_cmd(struct litex_mmc_host * host,u8 cmd,u32 arg,u8 response_len,u8 transfer)
- Line: 123

### litex_mmc_send_set_bus_w_cmd
- Return type: static int
- Signature: litex_mmc_send_set_bus_w_cmd(struct litex_mmc_host * host,u32 width)
- Line: 196

### litex_mmc_set_bus_width
- Return type: static int
- Signature: litex_mmc_set_bus_width(struct litex_mmc_host * host)
- Line: 202

### litex_mmc_set_ios
- Return type: static void
- Signature: litex_mmc_set_ios(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 448

### litex_mmc_setclk
- Return type: static void
- Signature: litex_mmc_setclk(struct litex_mmc_host * host,unsigned int freq)
- Line: 434

## Structs (1)

### litex_mmc_host
- Line: 76
- Members:
  - mmc: mmc_host *
  - sdphy: void __iomem *
  - sdcore: void __iomem *
  - sdreader: void __iomem *
  - sdwriter: void __iomem *
  - sdirq: void __iomem *
  - buffer: void *
  - buf_size: size_t
  - dma: dma_addr_t
  - cmd_done: completion
  - irq: int
  - ref_clk: unsigned int
  - sd_clk: unsigned int
  - resp: u32[4]
  - rca: u16
  - is_bus_width_set: bool
  - app_cmd: bool

## Variables (3)

- static **litex_match** : const struct of_device_id[] (line 629)
- static **litex_mmc_driver** : platform_driver (line 635)
- static **litex_mmc_ops** : const struct mmc_host_ops (line 464)

## Macros (43)

- **LITEX_BLK2MEM_BASE** (line 39)
- **LITEX_BLK2MEM_DONE** (line 42)
- **LITEX_BLK2MEM_ENA** (line 41)
- **LITEX_BLK2MEM_LEN** (line 40)
- **LITEX_BLK2MEM_LOOP** (line 43)
- **LITEX_CORE_BLKCNT** (line 38)
- **LITEX_CORE_BLKLEN** (line 37)
- **LITEX_CORE_CMDARG** (line 31)
- **LITEX_CORE_CMDCMD** (line 32)
- **LITEX_CORE_CMDEVT** (line 35)
- **LITEX_CORE_CMDRSP** (line 34)
- **LITEX_CORE_CMDSND** (line 33)
- **LITEX_CORE_DATEVT** (line 36)
- **LITEX_IRQ_ENABLE** (line 52)
- **LITEX_IRQ_PENDING** (line 51)
- **LITEX_IRQ_STATUS** (line 50)
- **LITEX_MEM2BLK** (line 49)
- **LITEX_MEM2BLK_BASE** (line 44)
- **LITEX_MEM2BLK_DONE** (line 47)
- **LITEX_MEM2BLK_ENA** (line 46)
- **LITEX_MEM2BLK_LEN** (line 45)
- **LITEX_MEM2BLK_LOOP** (line 48)
- **LITEX_PHY_CARDDETECT** (line 27)
- **LITEX_PHY_CLOCKERDIV** (line 28)
- **LITEX_PHY_INITIALIZE** (line 29)
- **LITEX_PHY_WRITESTATUS** (line 30)
- **SDIRQ_CARD_DETECT** (line 71)
- **SDIRQ_CMD_DONE** (line 74)
- **SDIRQ_MEM_TO_SD_DONE** (line 73)
- **SDIRQ_SD_TO_MEM_DONE** (line 72)
- **SD_BIT_CRC_ERR** (line 66)
- **SD_BIT_DONE** (line 63)
- **SD_BIT_TIMEOUT** (line 65)
- **SD_BIT_WR_ERR** (line 64)
- **SD_CTL_DATA_XFER_NONE** (line 54)
- **SD_CTL_DATA_XFER_READ** (line 55)
- **SD_CTL_DATA_XFER_WRITE** (line 56)
- **SD_CTL_RESP_LONG** (line 60)
- **SD_CTL_RESP_NONE** (line 58)
- **SD_CTL_RESP_SHORT** (line 59)
- **SD_CTL_RESP_SHORT_BUSY** (line 61)
- **SD_SLEEP_US** (line 68)
- **SD_TIMEOUT_US** (line 69)
