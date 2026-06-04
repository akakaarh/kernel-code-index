# drivers/mmc/host/omap.c

Subsystem: drivers/mmc

## Functions (40)

### mmc_omap_abort_command
- Return type: static void
- Signature: mmc_omap_abort_command(struct work_struct * work)
- Line: 608

### mmc_omap_abort_xfer
- Return type: static void
- Signature: mmc_omap_abort_xfer(struct mmc_omap_host * host,struct mmc_data * data)
- Line: 513

### mmc_omap_calc_divisor
- Return type: static int
- Signature: mmc_omap_calc_divisor(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 1155

### mmc_omap_clk_timer
- Return type: static void
- Signature: mmc_omap_clk_timer(struct timer_list * t)
- Line: 657

### mmc_omap_cmd_done
- Return type: static void
- Signature: mmc_omap_cmd_done(struct mmc_omap_host * host,struct mmc_command * cmd)
- Line: 563

### mmc_omap_cmd_timer
- Return type: static void
- Signature: mmc_omap_cmd_timer(struct timer_list * t)
- Line: 640

### mmc_omap_cover_bh_handler
- Return type: static void
- Signature: mmc_omap_cover_bh_handler(struct work_struct * t)
- Line: 887

### mmc_omap_cover_is_open
- Return type: static int
- Signature: mmc_omap_cover_is_open(struct mmc_omap_slot * slot)
- Line: 307

### mmc_omap_cover_timer
- Return type: static void
- Signature: mmc_omap_cover_timer(struct timer_list * t)
- Line: 881

### mmc_omap_dma_callback
- Return type: static void
- Signature: mmc_omap_dma_callback(void * priv)
- Line: 907

### mmc_omap_dma_done
- Return type: static void
- Signature: mmc_omap_dma_done(struct mmc_omap_host * host,struct mmc_data * data)
- Line: 546

### mmc_omap_end_of_data
- Return type: static void
- Signature: mmc_omap_end_of_data(struct mmc_omap_host * host,struct mmc_data * data)
- Line: 525

### mmc_omap_fclk_enable
- Return type: static void
- Signature: mmc_omap_fclk_enable(struct mmc_omap_host * host,unsigned int enable)
- Line: 186

### mmc_omap_fclk_offdelay
- Return type: static void
- Signature: mmc_omap_fclk_offdelay(struct mmc_omap_slot * slot)
- Line: 176

### mmc_omap_irq
- Return type: static irqreturn_t
- Signature: mmc_omap_irq(int irq,void * dev_id)
- Line: 725

### mmc_omap_new_slot
- Return type: static int
- Signature: mmc_omap_new_slot(struct mmc_omap_host * host,int id)
- Line: 1256

### mmc_omap_prepare_data
- Return type: static void
- Signature: mmc_omap_prepare_data(struct mmc_omap_host * host,struct mmc_request * req)
- Line: 950

### mmc_omap_probe
- Return type: static int
- Signature: mmc_omap_probe(struct platform_device * pdev)
- Line: 1369

### mmc_omap_release_dma
- Return type: static void
- Signature: mmc_omap_release_dma(struct mmc_omap_host * host,struct mmc_data * data,int abort)
- Line: 414

### mmc_omap_release_slot
- Return type: static void
- Signature: mmc_omap_release_slot(struct mmc_omap_slot * slot,int clk_enabled)
- Line: 264

### mmc_omap_remove
- Return type: static void
- Signature: mmc_omap_remove(struct platform_device * pdev)
- Line: 1520

### mmc_omap_remove_slot
- Return type: static void
- Signature: mmc_omap_remove_slot(struct mmc_omap_slot * slot)
- Line: 1353

### mmc_omap_report_irq
- Return type: static void
- Signature: mmc_omap_report_irq(struct mmc_omap_host * host,u16 status)
- Line: 702

### mmc_omap_report_irq
- Return type: static void
- Signature: mmc_omap_report_irq(struct mmc_omap_host * host,u16 status)
- Line: 719

### mmc_omap_request
- Return type: static void
- Signature: mmc_omap_request(struct mmc_host * mmc,struct mmc_request * req)
- Line: 1093

### mmc_omap_select_slot
- Return type: static void
- Signature: mmc_omap_select_slot(struct mmc_omap_slot * slot,int claimed)
- Line: 201

### mmc_omap_send_abort
- Return type: static void
- Signature: mmc_omap_send_abort(struct mmc_omap_host * host,int maxloops)
- Line: 484

### mmc_omap_send_stop_work
- Return type: static void
- Signature: mmc_omap_send_stop_work(struct work_struct * work)
- Line: 439

### mmc_omap_set_ios
- Return type: static void
- Signature: mmc_omap_set_ios(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 1183

### mmc_omap_set_power
- Return type: static void
- Signature: mmc_omap_set_power(struct mmc_omap_slot * slot,int power_on,int vdd)
- Line: 1112

### mmc_omap_show_cover_switch
- Return type: static ssize_t
- Signature: mmc_omap_show_cover_switch(struct device * dev,struct device_attribute * attr,char * buf)
- Line: 319

### mmc_omap_show_slot_name
- Return type: static ssize_t
- Signature: mmc_omap_show_slot_name(struct device * dev,struct device_attribute * attr,char * buf)
- Line: 332

### mmc_omap_slot_release_work
- Return type: static void
- Signature: mmc_omap_slot_release_work(struct work_struct * work)
- Line: 249

### mmc_omap_start_command
- Return type: static void
- Signature: mmc_omap_start_command(struct mmc_omap_host * host,struct mmc_command * cmd)
- Line: 344

### mmc_omap_start_request
- Return type: static void
- Signature: mmc_omap_start_request(struct mmc_omap_host * host,struct mmc_request * req)
- Line: 1075

### mmc_omap_xfer_data
- Return type: static void
- Signature: mmc_omap_xfer_data(struct mmc_omap_host * host,int write)
- Line: 666

### mmc_omap_xfer_done
- Return type: static void
- Signature: mmc_omap_xfer_done(struct mmc_omap_host * host,struct mmc_data * data)
- Line: 454

### omap_mmc_notify_cover_event
- Return type: void
- Signature: omap_mmc_notify_cover_event(struct device * dev,int num,int is_closed)
- Line: 860

### set_cmd_timeout
- Return type: static void
- Signature: set_cmd_timeout(struct mmc_omap_host * host,struct mmc_request * req)
- Line: 918

### set_data_timeout
- Return type: static void
- Signature: set_data_timeout(struct mmc_omap_host * host,struct mmc_request * req)
- Line: 929

## Structs (2)

### mmc_omap_host
- Line: 122
- Members:
  - id: int
  - vdd: unsigned int
  - saved_con: u16
  - bus_mode: u16
  - power_mode: u16
  - fclk_freq: unsigned int
  - cover_bh_work: work_struct
  - cover_timer: timer_list
  - cover_open: unsigned
  - mrq: mmc_request *
  - host: mmc_omap_host *
  - mmc: mmc_host *
  - vsd: gpio_desc *
  - vio: gpio_desc *
  - cover: gpio_desc *
  - pdata: omap_mmc_slot_data *
  - initialized: int
  - mrq: mmc_request *
  - cmd: mmc_command *
  - data: mmc_data *
  - mmc: mmc_host *
  - dev: device *
  - id: unsigned char
  - iclk: clk *
  - fclk: clk *
  - dma_rx: dma_chan *
  - dma_rx_burst: u32
  - dma_tx: dma_chan *
  - dma_tx_burst: u32
  - virt_base: void __iomem *
  - phys_base: unsigned int
  - irq: int
  - bus_mode: unsigned char
  - reg_shift: unsigned int
  - slot_switch: gpio_desc *
  - cmd_abort_work: work_struct
  - abort: unsigned:1
  - cmd_abort_timer: timer_list
  - slot_release_work: work_struct
  - next_slot: mmc_omap_slot *
  - send_stop_work: work_struct
  - stop_data: mmc_data *
  - sg_miter: sg_mapping_iter
  - sg_len: unsigned int
  - total_bytes_left: u32
  - features: unsigned
  - brs_received: unsigned:1
  - dma_done: unsigned:1
  - dma_in_use: unsigned:1
  - dma_lock: spinlock_t
  - slots: mmc_omap_slot * []
  - current_slot: mmc_omap_slot *
  - slot_lock: spinlock_t
  - slot_wq: wait_queue_head_t
  - nr_slots: int
  - clk_timer: timer_list
  - clk_lock: spinlock_t
  - fclk_enabled: unsigned int:1
  - mmc_omap_wq: workqueue_struct *
  - pdata: omap_mmc_platform_data *

### mmc_omap_slot
- Line: 101
- Members:
  - id: int
  - vdd: unsigned int
  - saved_con: u16
  - bus_mode: u16
  - power_mode: u16
  - fclk_freq: unsigned int
  - cover_bh_work: work_struct
  - cover_timer: timer_list
  - cover_open: unsigned
  - mrq: mmc_request *
  - host: mmc_omap_host *
  - mmc: mmc_host *
  - vsd: gpio_desc *
  - vio: gpio_desc *
  - cover: gpio_desc *
  - pdata: omap_mmc_slot_data *
  - initialized: int
  - mrq: mmc_request *
  - cmd: mmc_command *
  - data: mmc_data *
  - mmc: mmc_host *
  - dev: device *
  - id: unsigned char
  - iclk: clk *
  - fclk: clk *
  - dma_rx: dma_chan *
  - dma_rx_burst: u32
  - dma_tx: dma_chan *
  - dma_tx_burst: u32
  - virt_base: void __iomem *
  - phys_base: unsigned int
  - irq: int
  - bus_mode: unsigned char
  - reg_shift: unsigned int
  - slot_switch: gpio_desc *
  - cmd_abort_work: work_struct
  - abort: unsigned:1
  - cmd_abort_timer: timer_list
  - slot_release_work: work_struct
  - next_slot: mmc_omap_slot *
  - send_stop_work: work_struct
  - stop_data: mmc_data *
  - sg_miter: sg_mapping_iter
  - sg_len: unsigned int
  - total_bytes_left: u32
  - features: unsigned
  - brs_received: unsigned:1
  - dma_done: unsigned:1
  - dma_in_use: unsigned:1
  - dma_lock: spinlock_t
  - slots: mmc_omap_slot * []
  - current_slot: mmc_omap_slot *
  - slot_lock: spinlock_t
  - slot_wq: wait_queue_head_t
  - nr_slots: int
  - clk_timer: timer_list
  - clk_lock: spinlock_t
  - fclk_enabled: unsigned int:1
  - mmc_omap_wq: workqueue_struct *
  - pdata: omap_mmc_platform_data *

## Variables (3)

- static **mmc_omap_driver** : platform_driver (line 1556)
- static **mmc_omap_match** : const struct of_device_id[] (line 1549)
- static **mmc_omap_ops** : const struct mmc_host_ops (line 1251)

## Macros (53)

- **DRIVER_NAME** (line 93)
- **MMC_OMAP1_MASK** (line 77)
- **OMAP_MMC_CMDTYPE_AC** (line 90)
- **OMAP_MMC_CMDTYPE_ADTC** (line 91)
- **OMAP_MMC_CMDTYPE_BC** (line 88)
- **OMAP_MMC_CMDTYPE_BCR** (line 89)
- **OMAP_MMC_COVER_POLL_DELAY** (line 97)
- **OMAP_MMC_READ**(host,reg) (line 82)
- **OMAP_MMC_REG**(host,reg) (line 81)
- **OMAP_MMC_REG_ARGH** (line 36)
- **OMAP_MMC_REG_ARGL** (line 35)
- **OMAP_MMC_REG_BLEN** (line 43)
- **OMAP_MMC_REG_BUF** (line 45)
- **OMAP_MMC_REG_CMD** (line 34)
- **OMAP_MMC_REG_CON** (line 37)
- **OMAP_MMC_REG_CTO** (line 40)
- **OMAP_MMC_REG_DATA** (line 42)
- **OMAP_MMC_REG_DTO** (line 41)
- **OMAP_MMC_REG_IE** (line 39)
- **OMAP_MMC_REG_IOSR** (line 56)
- **OMAP_MMC_REG_NBLK** (line 44)
- **OMAP_MMC_REG_REV** (line 47)
- **OMAP_MMC_REG_RSP0** (line 48)
- **OMAP_MMC_REG_RSP1** (line 49)
- **OMAP_MMC_REG_RSP2** (line 50)
- **OMAP_MMC_REG_RSP3** (line 51)
- **OMAP_MMC_REG_RSP4** (line 52)
- **OMAP_MMC_REG_RSP5** (line 53)
- **OMAP_MMC_REG_RSP6** (line 54)
- **OMAP_MMC_REG_RSP7** (line 55)
- **OMAP_MMC_REG_SDIO** (line 46)
- **OMAP_MMC_REG_STAT** (line 38)
- **OMAP_MMC_REG_SYSC** (line 57)
- **OMAP_MMC_REG_SYSS** (line 58)
- **OMAP_MMC_STAT_A_EMPTY** (line 63)
- **OMAP_MMC_STAT_A_FULL** (line 64)
- **OMAP_MMC_STAT_CARD_BUSY** (line 71)
- **OMAP_MMC_STAT_CARD_ERR** (line 60)
- **OMAP_MMC_STAT_CARD_IRQ** (line 61)
- **OMAP_MMC_STAT_CMD_CRC** (line 65)
- **OMAP_MMC_STAT_CMD_TOUT** (line 66)
- **OMAP_MMC_STAT_DATA_CRC** (line 67)
- **OMAP_MMC_STAT_DATA_TOUT** (line 68)
- **OMAP_MMC_STAT_END_BUSY** (line 69)
- **OMAP_MMC_STAT_END_OF_CMD** (line 72)
- **OMAP_MMC_STAT_END_OF_DATA** (line 70)
- **OMAP_MMC_STAT_OCR_BUSY** (line 62)
- **OMAP_MMC_WRITE**(host,reg,val) (line 83)
- **mmc_omap1**() (line 78)
- **mmc_omap15xx**() (line 75)
- **mmc_omap16xx**() (line 76)
- **mmc_omap2**() (line 79)
- **mmc_omap7xx**() (line 74)
