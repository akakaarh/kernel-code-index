# drivers/spi/spi-stm32-ospi.c

Subsystem: drivers/spi

## Functions (28)

### stm32_ospi_abort
- Return type: static int
- Signature: stm32_ospi_abort(struct stm32_ospi * ospi)
- Line: 170

### stm32_ospi_dirmap_create
- Return type: static int
- Signature: stm32_ospi_dirmap_create(struct spi_mem_dirmap_desc * desc)
- Line: 601

### stm32_ospi_dirmap_read
- Return type: static ssize_t
- Signature: stm32_ospi_dirmap_read(struct spi_mem_dirmap_desc * desc,u64 offs,size_t len,void * buf)
- Line: 618

### stm32_ospi_dma_callback
- Return type: static void
- Signature: stm32_ospi_dma_callback(void * arg)
- Line: 266

### stm32_ospi_dma_setup
- Return type: static int
- Signature: stm32_ospi_dma_setup(struct stm32_ospi * ospi,struct dma_slave_config * dma_cfg)
- Line: 292

### stm32_ospi_exec_op
- Return type: static int
- Signature: stm32_ospi_exec_op(struct spi_mem * mem,const struct spi_mem_op * op)
- Line: 578

### stm32_ospi_get_mode
- Return type: static int
- Signature: stm32_ospi_get_mode(u8 buswidth)
- Line: 452

### stm32_ospi_get_resources
- Return type: static int
- Signature: stm32_ospi_get_resources(struct platform_device * pdev)
- Line: 788

### stm32_ospi_irq
- Return type: static irqreturn_t
- Signature: stm32_ospi_irq(int irq,void * dev_id)
- Line: 273

### stm32_ospi_poll
- Return type: static int
- Signature: stm32_ospi_poll(struct stm32_ospi * ospi,void * buf,u32 len,bool read)
- Line: 190

### stm32_ospi_poll_status
- Return type: static int
- Signature: stm32_ospi_poll_status(struct spi_mem * mem,const struct spi_mem_op * op,u16 mask,u16 match,unsigned long initial_delay_us,unsigned long polling_rate_us,unsigned long timeout_ms)
- Line: 548

### stm32_ospi_probe
- Return type: static int
- Signature: stm32_ospi_probe(struct platform_device * pdev)
- Line: 879

### stm32_ospi_read_fifo
- Return type: static void
- Signature: stm32_ospi_read_fifo(void * val,void __iomem * addr,u8 len)
- Line: 142

### stm32_ospi_remove
- Return type: static void
- Signature: stm32_ospi_remove(struct platform_device * pdev)
- Line: 987

### stm32_ospi_resume
- Return type: static int
- Signature: stm32_ospi_resume(struct device * dev)
- Line: 1020

### stm32_ospi_runtime_resume
- Return type: static int
- Signature: stm32_ospi_runtime_resume(struct device * dev)
- Line: 1058

### stm32_ospi_runtime_suspend
- Return type: static int
- Signature: stm32_ospi_runtime_suspend(struct device * dev)
- Line: 1049

### stm32_ospi_send
- Return type: static int
- Signature: stm32_ospi_send(struct spi_device * spi,const struct spi_mem_op * op)
- Line: 464

### stm32_ospi_setup
- Return type: static int
- Signature: stm32_ospi_setup(struct spi_device * spi)
- Line: 741

### stm32_ospi_suspend
- Return type: static int
- Signature: stm32_ospi_suspend(struct device * dev)
- Line: 1009

### stm32_ospi_transfer_one_message
- Return type: static int
- Signature: stm32_ospi_transfer_one_message(struct spi_controller * ctrl,struct spi_message * msg)
- Line: 657

### stm32_ospi_tx_dma
- Return type: static int
- Signature: stm32_ospi_tx_dma(struct stm32_ospi * ospi,const struct spi_mem_op * op)
- Line: 339

### stm32_ospi_tx_mm
- Return type: static int
- Signature: stm32_ospi_tx_mm(struct stm32_ospi * ospi,const struct spi_mem_op * op)
- Line: 331

### stm32_ospi_wait_cmd
- Return type: static int
- Signature: stm32_ospi_wait_cmd(struct stm32_ospi * ospi)
- Line: 237

### stm32_ospi_wait_nobusy
- Return type: static int
- Signature: stm32_ospi_wait_nobusy(struct stm32_ospi * ospi)
- Line: 228

### stm32_ospi_wait_poll_status
- Return type: static int
- Signature: stm32_ospi_wait_poll_status(struct stm32_ospi * ospi,const struct spi_mem_op * op)
- Line: 428

### stm32_ospi_write_fifo
- Return type: static void
- Signature: stm32_ospi_write_fifo(void * val,void __iomem * addr,u8 len)
- Line: 156

### stm32_ospi_xfer
- Return type: static int
- Signature: stm32_ospi_xfer(struct stm32_ospi * ospi,const struct spi_mem_op * op)
- Line: 404

## Structs (1)

### stm32_ospi
- Line: 111
- Members:
  - dev: device *
  - ctrl: spi_controller *
  - clk: clk *
  - rstc: reset_control *
  - match_completion: completion
  - dma_chtx: dma_chan *
  - dma_chrx: dma_chan *
  - dma_completion: completion
  - regs_base: void __iomem *
  - mm_base: void __iomem *
  - regs_phys_base: phys_addr_t
  - mm_size: resource_size_t
  - clk_rate: u32
  - fmode: u32
  - cr_reg: u32
  - dcr_reg: u32
  - flash_presc: u32[]
  - irq: int
  - status_timeout: unsigned long
  - lock: mutex

## Variables (4)

- static **stm32_ospi_driver** : platform_driver (line 1076)
- static **stm32_ospi_mem_ops** : const struct spi_controller_mem_ops (line 781)
- static **stm32_ospi_of_match** : const struct of_device_id[] (line 1070)
- static **stm32_ospi_pm_ops** : const struct dev_pm_ops (line 1065)

## Macros (67)

- **CCR_ADDTR** (line 80)
- **CCR_ADMODE_8LINES** (line 79)
- **CCR_ADMODE_MASK** (line 78)
- **CCR_ADSIZE_32BITS** (line 82)
- **CCR_ADSIZE_MASK** (line 81)
- **CCR_BUSWIDTH_0** (line 87)
- **CCR_BUSWIDTH_1** (line 88)
- **CCR_BUSWIDTH_2** (line 89)
- **CCR_BUSWIDTH_4** (line 90)
- **CCR_BUSWIDTH_8** (line 91)
- **CCR_DDTR** (line 86)
- **CCR_DMODE_8LINES** (line 84)
- **CCR_DMODE_MASK** (line 83)
- **CCR_DQSE** (line 85)
- **CCR_IDTR** (line 76)
- **CCR_IMODE_MASK** (line 75)
- **CCR_ISIZE_MASK** (line 77)
- **CR_ABORT** (line 34)
- **CR_APMS** (line 38)
- **CR_CSSEL** (line 39)
- **CR_DMAEN** (line 35)
- **CR_EN** (line 33)
- **CR_FMODE_APM** (line 43)
- **CR_FMODE_INDR** (line 42)
- **CR_FMODE_INDW** (line 41)
- **CR_FMODE_MASK** (line 40)
- **CR_FMODE_MM** (line 44)
- **CR_FTHRES_SHIFT** (line 36)
- **CR_SMIE** (line 37)
- **DCR1_DEVSIZE_MASK** (line 48)
- **DCR1_DLYBYP** (line 47)
- **DCR1_MTYP_HP_MEMMODE** (line 51)
- **DCR1_MTYP_MASK** (line 49)
- **DCR1_MTYP_MX_MODE** (line 50)
- **DCR2_PRESC_MASK** (line 54)
- **FCR_CSMF** (line 66)
- **FCR_CTCF** (line 65)
- **FCR_CTEF** (line 64)
- **OSPI_AR** (line 69)
- **OSPI_CCR** (line 74)
- **OSPI_CR** (line 32)
- **OSPI_DCR1** (line 46)
- **OSPI_DCR2** (line 53)
- **OSPI_DLR** (line 68)
- **OSPI_DR** (line 70)
- **OSPI_FCR** (line 63)
- **OSPI_IR** (line 98)
- **OSPI_PSMAR** (line 72)
- **OSPI_PSMKR** (line 71)
- **OSPI_SR** (line 56)
- **OSPI_TCR** (line 93)
- **SR_BUSY** (line 61)
- **SR_FTF** (line 59)
- **SR_SMF** (line 60)
- **SR_TCF** (line 58)
- **SR_TEF** (line 57)
- **STM32_ABT_TIMEOUT_US** (line 104)
- **STM32_AUTOSUSPEND_DELAY** (line 109)
- **STM32_BUSY_TIMEOUT_US** (line 106)
- **STM32_COMP_TIMEOUT_MS** (line 105)
- **STM32_FIFO_TIMEOUT_US** (line 103)
- **STM32_OSPI_MAX_MMAP_SZ** (line 100)
- **STM32_OSPI_MAX_NORCHIP** (line 101)
- **STM32_WAIT_CMD_TIMEOUT_US** (line 107)
- **TCR_DCYC_MASK** (line 94)
- **TCR_DHQC** (line 95)
- **TCR_SSHIFT** (line 96)
