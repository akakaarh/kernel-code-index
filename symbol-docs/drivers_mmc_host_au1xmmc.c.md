# drivers/mmc/host/au1xmmc.c

Subsystem: drivers/mmc

## Functions (32)

### FLUSH_FIFO
- Return type: static void
- Signature: FLUSH_FIFO(struct au1xmmc_host * host)
- Line: 173

### IRQ_OFF
- Return type: static void
- Signature: IRQ_OFF(struct au1xmmc_host * host,u32 mask)
- Line: 188

### IRQ_ON
- Return type: static void
- Signature: IRQ_ON(struct au1xmmc_host * host,u32 mask)
- Line: 165

### SEND_STOP
- Return type: static void
- Signature: SEND_STOP(struct au1xmmc_host * host)
- Line: 196

### au1xmmc_card_inserted
- Return type: static int
- Signature: au1xmmc_card_inserted(struct mmc_host * mmc)
- Line: 218

### au1xmmc_card_readonly
- Return type: static int
- Signature: au1xmmc_card_readonly(struct mmc_host * mmc)
- Line: 228

### au1xmmc_cmd_complete
- Return type: static void
- Signature: au1xmmc_cmd_complete(struct au1xmmc_host * host,u32 status)
- Line: 516

### au1xmmc_data_bh_work
- Return type: static void
- Signature: au1xmmc_data_bh_work(struct work_struct * t)
- Line: 367

### au1xmmc_data_complete
- Return type: static void
- Signature: au1xmmc_data_complete(struct au1xmmc_host * host,u32 status)
- Line: 316

### au1xmmc_dbdma_callback
- Return type: static void
- Signature: au1xmmc_dbdma_callback(int irq,void * dev_id)
- Line: 847

### au1xmmc_dbdma_init
- Return type: static int
- Signature: au1xmmc_dbdma_init(struct au1xmmc_host * host)
- Line: 861

### au1xmmc_dbdma_shutdown
- Return type: static void
- Signature: au1xmmc_dbdma_shutdown(struct au1xmmc_host * host)
- Line: 906

### au1xmmc_enable_sdio_irq
- Return type: static void
- Signature: au1xmmc_enable_sdio_irq(struct mmc_host * mmc,int en)
- Line: 915

### au1xmmc_exit
- Return type: static void __exit
- Signature: au1xmmc_exit(void)
- Line: 1201

### au1xmmc_finish_bh_work
- Return type: static void
- Signature: au1xmmc_finish_bh_work(struct work_struct * t)
- Line: 257

### au1xmmc_finish_request
- Return type: static void
- Signature: au1xmmc_finish_request(struct au1xmmc_host * host)
- Line: 238

### au1xmmc_init
- Return type: static int __init
- Signature: au1xmmc_init(void)
- Line: 1187

### au1xmmc_irq
- Return type: static irqreturn_t
- Signature: au1xmmc_irq(int irq,void * dev_id)
- Line: 778

### au1xmmc_prepare_data
- Return type: static int
- Signature: au1xmmc_prepare_data(struct au1xmmc_host * host,struct mmc_data * data)
- Line: 602

### au1xmmc_probe
- Return type: static int
- Signature: au1xmmc_probe(struct platform_device * pdev)
- Line: 933

### au1xmmc_receive_pio
- Return type: static void
- Signature: au1xmmc_receive_pio(struct au1xmmc_host * host)
- Line: 433

### au1xmmc_remove
- Return type: static void
- Signature: au1xmmc_remove(struct platform_device * pdev)
- Line: 1114

### au1xmmc_request
- Return type: static void
- Signature: au1xmmc_request(struct mmc_host * mmc,struct mmc_request * mrq)
- Line: 675

### au1xmmc_reset_controller
- Return type: static void
- Signature: au1xmmc_reset_controller(struct au1xmmc_host * host)
- Line: 707

### au1xmmc_resume
- Return type: static int
- Signature: au1xmmc_resume(struct device * dev)
- Line: 1166

### au1xmmc_send_command
- Return type: static int
- Signature: au1xmmc_send_command(struct au1xmmc_host * host,struct mmc_command * cmd,struct mmc_data * data)
- Line: 263

### au1xmmc_send_pio
- Return type: static void
- Signature: au1xmmc_send_pio(struct au1xmmc_host * host)
- Line: 377

### au1xmmc_set_clock
- Return type: static void
- Signature: au1xmmc_set_clock(struct au1xmmc_host * host,int rate)
- Line: 587

### au1xmmc_set_ios
- Return type: static void
- Signature: au1xmmc_set_ios(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 741

### au1xmmc_set_power
- Return type: static void
- Signature: au1xmmc_set_power(struct au1xmmc_host * host,int state)
- Line: 212

### au1xmmc_suspend
- Return type: static int
- Signature: au1xmmc_suspend(struct device * dev)
- Line: 1153

### has_dbdma
- Return type: static int
- Signature: has_dbdma(void)
- Line: 154

## Structs (3)

### __anon0d6464c30108
- Line: 101
- Members:
  - mmc: mmc_host *
  - mrq: mmc_request *
  - flags: u32
  - iobase: void __iomem *
  - clock: u32
  - bus_width: u32
  - power_mode: u32
  - status: int
  - len: int
  - dir: int
  - dma: au1xmmc_host::__anon0d6464c30108
  - index: int
  - offset: int
  - len: int
  - pio: au1xmmc_host::__anon0d6464c30208
  - tx_chan: u32
  - rx_chan: u32
  - irq: int
  - finish_bh_work: work_struct
  - data_bh_work: work_struct
  - platdata: au1xmmc_platform_data *
  - pdev: platform_device *
  - ioarea: resource *
  - clk: clk *

### __anon0d6464c30208
- Line: 106
- Members:
  - mmc: mmc_host *
  - mrq: mmc_request *
  - flags: u32
  - iobase: void __iomem *
  - clock: u32
  - bus_width: u32
  - power_mode: u32
  - status: int
  - len: int
  - dir: int
  - dma: au1xmmc_host::__anon0d6464c30108
  - index: int
  - offset: int
  - len: int
  - pio: au1xmmc_host::__anon0d6464c30208
  - tx_chan: u32
  - rx_chan: u32
  - irq: int
  - finish_bh_work: work_struct
  - data_bh_work: work_struct
  - platdata: au1xmmc_platform_data *
  - pdev: platform_device *
  - ioarea: resource *
  - clk: clk *

### au1xmmc_host
- Line: 89
- Members:
  - mmc: mmc_host *
  - mrq: mmc_request *
  - flags: u32
  - iobase: void __iomem *
  - clock: u32
  - bus_width: u32
  - power_mode: u32
  - status: int
  - len: int
  - dir: int
  - dma: au1xmmc_host::__anon0d6464c30108
  - index: int
  - offset: int
  - len: int
  - pio: au1xmmc_host::__anon0d6464c30208
  - tx_chan: u32
  - rx_chan: u32
  - irq: int
  - finish_bh_work: work_struct
  - data_bh_work: work_struct
  - platdata: au1xmmc_platform_data *
  - pdev: platform_device *
  - ioarea: resource *
  - clk: clk *

## Variables (4)

- static **au1xmmc_driver** : platform_driver (line 1177)
- static **au1xmmc_mem_dbdev** : dbdev_tab_t (line 836)
- static **au1xmmc_ops** : const struct mmc_host_ops (line 925)
- static **memid** : int (line 845)

## Macros (36)

- **AU1100_MMC_DESCRIPTOR_SIZE** (line 68)
- **AU1200_MMC_DESCRIPTOR_SIZE** (line 69)
- **AU1XMMC_DESCRIPTOR_COUNT** (line 65)
- **AU1XMMC_DETECT_TIMEOUT** (line 87)
- **AU1XMMC_INTERRUPTS** (line 82)
- **AU1XMMC_MAX_TRANSFER** (line 375)
- **AU1XMMC_OCR** (line 71)
- **DBG**(fmt,idx,args...) (line 58)
- **DBG**(fmt,idx,args...) (line 61)
- **DMA_CHANNEL**(h) (line 151)
- **DRIVER_NAME** (line 52)
- **HOST_BLKSIZE**(h) (line 145)
- **HOST_CMD**(h) (line 146)
- **HOST_CMDARG**(h) (line 144)
- **HOST_CONFIG**(h) (line 140)
- **HOST_CONFIG2**(h) (line 147)
- **HOST_DEBUG**(h) (line 149)
- **HOST_ENABLE**(h) (line 141)
- **HOST_F_ACTIVE** (line 130)
- **HOST_F_DBDMA** (line 129)
- **HOST_F_DMA** (line 128)
- **HOST_F_RECV** (line 127)
- **HOST_F_STOP** (line 131)
- **HOST_F_XMIT** (line 126)
- **HOST_RXPORT**(h) (line 143)
- **HOST_STATUS**(h) (line 139)
- **HOST_S_CMD** (line 134)
- **HOST_S_DATA** (line 135)
- **HOST_S_IDLE** (line 133)
- **HOST_S_STOP** (line 136)
- **HOST_TIMEOUT**(h) (line 148)
- **HOST_TXPORT**(h) (line 142)
- **STATUS_DATA_IN** (line 775)
- **STATUS_DATA_OUT** (line 776)
- **STATUS_TIMEOUT** (line 774)
- **STOP_CMD** (line 78)
