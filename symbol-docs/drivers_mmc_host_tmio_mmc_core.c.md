# drivers/mmc/host/tmio_mmc_core.c

Subsystem: drivers/mmc

## Functions (49)

### __tmio_mmc_card_detect_irq
- Return type: static bool
- Signature: __tmio_mmc_card_detect_irq(struct tmio_mmc_host * host,int ireg,int status)
- Line: 662

### __tmio_mmc_sdcard_irq
- Return type: static bool
- Signature: __tmio_mmc_sdcard_irq(struct tmio_mmc_host * host,int ireg,int status)
- Line: 681

### __tmio_mmc_sdio_irq
- Return type: static bool
- Signature: __tmio_mmc_sdio_irq(struct tmio_mmc_host * host)
- Line: 712

### tmio_mmc_abort_dma
- Return type: static void
- Signature: tmio_mmc_abort_dma(struct tmio_mmc_host * host)
- Line: 90

### tmio_mmc_ack_mmc_irqs
- Return type: static void
- Signature: tmio_mmc_ack_mmc_irqs(struct tmio_mmc_host * host,u32 i)
- Line: 116

### tmio_mmc_check_bounce_buffer
- Return type: static void
- Signature: tmio_mmc_check_bounce_buffer(struct tmio_mmc_host * host)
- Line: 479

### tmio_mmc_clk_disable
- Return type: static void
- Signature: tmio_mmc_clk_disable(struct tmio_mmc_host * host)
- Line: 1298

### tmio_mmc_clk_enable
- Return type: static int
- Signature: tmio_mmc_clk_enable(struct tmio_mmc_host * host)
- Line: 1290

### tmio_mmc_cmd_irq
- Return type: static void
- Signature: tmio_mmc_cmd_irq(struct tmio_mmc_host * host,unsigned int stat)
- Line: 596

### tmio_mmc_data_irq
- Return type: static void
- Signature: tmio_mmc_data_irq(struct tmio_mmc_host * host,unsigned int stat)
- Line: 546

### tmio_mmc_dataend_dma
- Return type: static void
- Signature: tmio_mmc_dataend_dma(struct tmio_mmc_host * host)
- Line: 96

### tmio_mmc_disable_mmc_irqs
- Return type: void
- Signature: tmio_mmc_disable_mmc_irqs(struct tmio_mmc_host * host,u32 i)
- Line: 109

### tmio_mmc_do_data_irq
- Return type: void
- Signature: tmio_mmc_do_data_irq(struct tmio_mmc_host * host)
- Line: 491

### tmio_mmc_done_work
- Return type: static void
- Signature: tmio_mmc_done_work(struct work_struct * work)
- Line: 904

### tmio_mmc_enable_dma
- Return type: static void
- Signature: tmio_mmc_enable_dma(struct tmio_mmc_host * host,bool enable)
- Line: 67

### tmio_mmc_enable_mmc_irqs
- Return type: void
- Signature: tmio_mmc_enable_mmc_irqs(struct tmio_mmc_host * host,u32 i)
- Line: 102

### tmio_mmc_enable_sdio_irq
- Return type: static void
- Signature: tmio_mmc_enable_sdio_irq(struct mmc_host * mmc,int enable)
- Line: 138

### tmio_mmc_end_dma
- Return type: static void
- Signature: tmio_mmc_end_dma(struct tmio_mmc_host * host)
- Line: 61

### tmio_mmc_finish_request
- Return type: static void
- Signature: tmio_mmc_finish_request(struct tmio_mmc_host * host)
- Line: 857

### tmio_mmc_get_cd
- Return type: static int
- Signature: tmio_mmc_get_cd(struct mmc_host * mmc)
- Line: 1054

### tmio_mmc_get_ro
- Return type: static int
- Signature: tmio_mmc_get_ro(struct mmc_host * mmc)
- Line: 1046

### tmio_mmc_get_timeout_cycles
- Return type: static unsigned int
- Signature: tmio_mmc_get_timeout_cycles(struct tmio_mmc_host * host)
- Line: 952

### tmio_mmc_host_alloc
- Return type: tmio_mmc_host *
- Signature: tmio_mmc_host_alloc(struct platform_device * pdev,struct tmio_mmc_data * pdata)
- Line: 1123

### tmio_mmc_host_probe
- Return type: int
- Signature: tmio_mmc_host_probe(struct tmio_mmc_host * _host)
- Line: 1159

### tmio_mmc_host_remove
- Return type: void
- Signature: tmio_mmc_host_remove(struct tmio_mmc_host * host)
- Line: 1262

### tmio_mmc_host_runtime_resume
- Return type: int
- Signature: tmio_mmc_host_runtime_resume(struct device * dev)
- Line: 1319

### tmio_mmc_host_runtime_suspend
- Return type: int
- Signature: tmio_mmc_host_runtime_suspend(struct device * dev)
- Line: 1304

### tmio_mmc_init_ocr
- Return type: static int
- Signature: tmio_mmc_init_ocr(struct tmio_mmc_host * host)
- Line: 1082

### tmio_mmc_init_sg
- Return type: static void
- Signature: tmio_mmc_init_sg(struct tmio_mmc_host * host,struct mmc_data * data)
- Line: 121

### tmio_mmc_irq
- Return type: irqreturn_t
- Signature: tmio_mmc_irq(int irq,void * devid)
- Line: 740

### tmio_mmc_max_busy_timeout
- Return type: static void
- Signature: tmio_mmc_max_busy_timeout(struct tmio_mmc_host * host)
- Line: 960

### tmio_mmc_next_sg
- Return type: static int
- Signature: tmio_mmc_next_sg(struct tmio_mmc_host * host)
- Line: 129

### tmio_mmc_of_parse
- Return type: static void
- Signature: tmio_mmc_of_parse(struct platform_device * pdev,struct mmc_host * mmc)
- Line: 1106

### tmio_mmc_pio_irq
- Return type: static void
- Signature: tmio_mmc_pio_irq(struct tmio_mmc_host * host)
- Line: 443

### tmio_mmc_power_off
- Return type: static void
- Signature: tmio_mmc_power_off(struct tmio_mmc_host * host)
- Line: 942

### tmio_mmc_power_on
- Return type: static void
- Signature: tmio_mmc_power_on(struct tmio_mmc_host * host,unsigned short vdd)
- Line: 911

### tmio_mmc_release_dma
- Return type: static void
- Signature: tmio_mmc_release_dma(struct tmio_mmc_host * host)
- Line: 84

### tmio_mmc_request
- Return type: static void
- Signature: tmio_mmc_request(struct mmc_host * mmc,struct mmc_request * mrq)
- Line: 831

### tmio_mmc_request_dma
- Return type: static void
- Signature: tmio_mmc_request_dma(struct tmio_mmc_host * host,struct tmio_mmc_data * pdata)
- Line: 73

### tmio_mmc_reset
- Return type: static void
- Signature: tmio_mmc_reset(struct tmio_mmc_host * host,bool preserve)
- Line: 182

### tmio_mmc_reset_work
- Return type: static void
- Signature: tmio_mmc_reset_work(struct work_struct * work)
- Line: 229

### tmio_mmc_set_bus_width
- Return type: static void
- Signature: tmio_mmc_set_bus_width(struct tmio_mmc_host * host,unsigned char bus_width)
- Line: 167

### tmio_mmc_set_ios
- Return type: static void
- Signature: tmio_mmc_set_ios(struct mmc_host * mmc,struct mmc_ios * ios)
- Line: 974

### tmio_mmc_start_command
- Return type: static int
- Signature: tmio_mmc_start_command(struct tmio_mmc_host * host,struct mmc_command * cmd)
- Line: 290

### tmio_mmc_start_data
- Return type: static int
- Signature: tmio_mmc_start_data(struct tmio_mmc_host * host,struct mmc_data * data)
- Line: 763

### tmio_mmc_start_dma
- Return type: static void
- Signature: tmio_mmc_start_dma(struct tmio_mmc_host * host,struct mmc_data * data)
- Line: 54

### tmio_mmc_transfer_data
- Return type: static void
- Signature: tmio_mmc_transfer_data(struct tmio_mmc_host * host,unsigned short * buf,unsigned int count)
- Line: 342

### tmio_multi_io_quirk
- Return type: static int
- Signature: tmio_multi_io_quirk(struct mmc_card * card,unsigned int direction,int blk_size)
- Line: 1062

### tmio_process_mrq
- Return type: static void
- Signature: tmio_process_mrq(struct tmio_mmc_host * host,struct mmc_request * mrq)
- Line: 799

## Variables (1)

- static **tmio_mmc_ops** : mmc_host_ops (line 1073)

## Macros (12)

- **APP_CMD** (line 278)
- **CMDREQ_TIMEOUT** (line 136)
- **DATA_PRESENT** (line 284)
- **NO_CMD12_ISSUE** (line 288)
- **RESP_NONE** (line 279)
- **RESP_R1** (line 280)
- **RESP_R1B** (line 281)
- **RESP_R2** (line 282)
- **RESP_R3** (line 283)
- **SECURITY_CMD** (line 287)
- **TRANSFER_MULTI** (line 286)
- **TRANSFER_READ** (line 285)
