# drivers/spi/spi-stm32-qspi.c

Subsystem: drivers/spi

## Functions (27)

### stm32_qspi_dirmap_create
- Return type: static int
- Signature: stm32_qspi_dirmap_create(struct spi_mem_dirmap_desc * desc)
- Line: 505

### stm32_qspi_dirmap_read
- Return type: static ssize_t
- Signature: stm32_qspi_dirmap_read(struct spi_mem_dirmap_desc * desc,u64 offs,size_t len,void * buf)
- Line: 522

### stm32_qspi_dma_callback
- Return type: static void
- Signature: stm32_qspi_dma_callback(void * arg)
- Line: 224

### stm32_qspi_dma_free
- Return type: static void
- Signature: stm32_qspi_dma_free(struct stm32_qspi * qspi)
- Line: 758

### stm32_qspi_dma_setup
- Return type: static int
- Signature: stm32_qspi_dma_setup(struct stm32_qspi * qspi)
- Line: 699

### stm32_qspi_exec_op
- Return type: static int
- Signature: stm32_qspi_exec_op(struct spi_mem * mem,const struct spi_mem_op * op)
- Line: 482

### stm32_qspi_get_mode
- Return type: static int
- Signature: stm32_qspi_get_mode(u8 buswidth)
- Line: 361

### stm32_qspi_irq
- Return type: static irqreturn_t
- Signature: stm32_qspi_irq(int irq,void * dev_id)
- Line: 127

### stm32_qspi_poll_status
- Return type: static int
- Signature: stm32_qspi_poll_status(struct spi_mem * mem,const struct spi_mem_op * op,u16 mask,u16 match,unsigned long initial_delay_us,unsigned long polling_rate_us,unsigned long timeout_ms)
- Line: 451

### stm32_qspi_probe
- Return type: static int
- Signature: stm32_qspi_probe(struct platform_device * pdev)
- Line: 777

### stm32_qspi_read_fifo
- Return type: static void
- Signature: stm32_qspi_read_fifo(void * val,void __iomem * addr,u8 len)
- Line: 145

### stm32_qspi_remove
- Return type: static void
- Signature: stm32_qspi_remove(struct platform_device * pdev)
- Line: 895

### stm32_qspi_resume
- Return type: static int
- Signature: stm32_qspi_resume(struct device * dev)
- Line: 935

### stm32_qspi_runtime_resume
- Return type: static int
- Signature: stm32_qspi_runtime_resume(struct device * dev)
- Line: 921

### stm32_qspi_runtime_suspend
- Return type: static int
- Signature: stm32_qspi_runtime_suspend(struct device * dev)
- Line: 912

### stm32_qspi_send
- Return type: static int
- Signature: stm32_qspi_send(struct spi_device * spi,const struct spi_mem_op * op)
- Line: 369

### stm32_qspi_setup
- Return type: static int
- Signature: stm32_qspi_setup(struct spi_device * spi)
- Line: 643

### stm32_qspi_suspend
- Return type: static int
- Signature: stm32_qspi_suspend(struct device * dev)
- Line: 928

### stm32_qspi_transfer_one_message
- Return type: static int
- Signature: stm32_qspi_transfer_one_message(struct spi_controller * ctrl,struct spi_message * msg)
- Line: 560

### stm32_qspi_tx
- Return type: static int
- Signature: stm32_qspi_tx(struct stm32_qspi * qspi,const struct spi_mem_op * op)
- Line: 295

### stm32_qspi_tx_dma
- Return type: static int
- Signature: stm32_qspi_tx_dma(struct stm32_qspi * qspi,const struct spi_mem_op * op)
- Line: 231

### stm32_qspi_tx_mm
- Return type: static int
- Signature: stm32_qspi_tx_mm(struct stm32_qspi * qspi,const struct spi_mem_op * op)
- Line: 216

### stm32_qspi_tx_poll
- Return type: static int
- Signature: stm32_qspi_tx_poll(struct stm32_qspi * qspi,const struct spi_mem_op * op)
- Line: 173

### stm32_qspi_wait_cmd
- Return type: static int
- Signature: stm32_qspi_wait_cmd(struct stm32_qspi * qspi)
- Line: 320

### stm32_qspi_wait_nobusy
- Return type: static int
- Signature: stm32_qspi_wait_nobusy(struct stm32_qspi * qspi)
- Line: 311

### stm32_qspi_wait_poll_status
- Return type: static int
- Signature: stm32_qspi_wait_poll_status(struct stm32_qspi * qspi)
- Line: 344

### stm32_qspi_write_fifo
- Return type: static void
- Signature: stm32_qspi_write_fifo(void * val,void __iomem * addr,u8 len)
- Line: 159

## Structs (2)

### stm32_qspi
- Line: 99
- Members:
  - cs: u32
  - presc: u32
  - dev: device *
  - ctrl: spi_controller *
  - phys_base: phys_addr_t
  - io_base: void __iomem *
  - mm_base: void __iomem *
  - mm_size: resource_size_t
  - clk: clk *
  - clk_rate: u32
  - flash: stm32_qspi_flash[]
  - match_completion: completion
  - fmode: u32
  - dma_chtx: dma_chan *
  - dma_chrx: dma_chan *
  - dma_completion: completion
  - cr_reg: u32
  - dcr_reg: u32
  - status_timeout: unsigned long
  - lock: mutex

### stm32_qspi_flash
- Line: 94
- Members:
  - cs: u32
  - presc: u32
  - dev: device *
  - ctrl: spi_controller *
  - phys_base: phys_addr_t
  - io_base: void __iomem *
  - mm_base: void __iomem *
  - mm_size: resource_size_t
  - clk: clk *
  - clk_rate: u32
  - flash: stm32_qspi_flash[]
  - match_completion: completion
  - fmode: u32
  - dma_chtx: dma_chan *
  - dma_chrx: dma_chan *
  - dma_completion: completion
  - cr_reg: u32
  - dcr_reg: u32
  - status_timeout: unsigned long
  - lock: mutex

## Variables (4)

- static **stm32_qspi_driver** : platform_driver (line 969)
- static **stm32_qspi_match** : const struct of_device_id[] (line 963)
- static **stm32_qspi_mem_ops** : const struct spi_controller_mem_ops (line 770)
- static **stm32_qspi_pm_ops** : const struct dev_pm_ops (line 958)

## Macros (60)

- **CCR_ADMODE_MASK** (line 62)
- **CCR_ADSIZE_MASK** (line 63)
- **CCR_BUSWIDTH_0** (line 71)
- **CCR_BUSWIDTH_1** (line 72)
- **CCR_BUSWIDTH_2** (line 73)
- **CCR_BUSWIDTH_4** (line 74)
- **CCR_DCYC_MASK** (line 64)
- **CCR_DMODE_MASK** (line 65)
- **CCR_FMODE_APM** (line 69)
- **CCR_FMODE_INDR** (line 68)
- **CCR_FMODE_INDW** (line 67)
- **CCR_FMODE_MASK** (line 66)
- **CCR_FMODE_MM** (line 70)
- **CCR_IMODE_MASK** (line 61)
- **CCR_INST_MASK** (line 60)
- **CR_ABORT** (line 27)
- **CR_APMS** (line 37)
- **CR_DFM** (line 31)
- **CR_DMAEN** (line 28)
- **CR_EN** (line 26)
- **CR_FSEL** (line 32)
- **CR_FTHRES_SHIFT** (line 33)
- **CR_FTIE** (line 34)
- **CR_PRESC_MASK** (line 38)
- **CR_SMIE** (line 35)
- **CR_SSHIFT** (line 30)
- **CR_TCEN** (line 29)
- **CR_TOIE** (line 36)
- **DCR_FSIZE_MASK** (line 41)
- **FCR_CSMF** (line 55)
- **FCR_CTCF** (line 54)
- **FCR_CTEF** (line 53)
- **QSPI_ABR** (line 77)
- **QSPI_AR** (line 76)
- **QSPI_CCR** (line 59)
- **QSPI_CR** (line 25)
- **QSPI_DCR** (line 40)
- **QSPI_DLR** (line 57)
- **QSPI_DR** (line 78)
- **QSPI_FCR** (line 52)
- **QSPI_LPTR** (line 82)
- **QSPI_PIR** (line 81)
- **QSPI_PSMAR** (line 80)
- **QSPI_PSMKR** (line 79)
- **QSPI_SR** (line 43)
- **SR_BUSY** (line 49)
- **SR_FLEVEL_MASK** (line 50)
- **SR_FTF** (line 46)
- **SR_SMF** (line 47)
- **SR_TCF** (line 45)
- **SR_TEF** (line 44)
- **SR_TOF** (line 48)
- **STM32_ABT_TIMEOUT_US** (line 89)
- **STM32_AUTOSUSPEND_DELAY** (line 92)
- **STM32_BUSY_TIMEOUT_US** (line 88)
- **STM32_COMP_TIMEOUT_MS** (line 91)
- **STM32_FIFO_TIMEOUT_US** (line 87)
- **STM32_QSPI_MAX_MMAP_SZ** (line 84)
- **STM32_QSPI_MAX_NORCHIP** (line 85)
- **STM32_WAIT_CMD_TIMEOUT_US** (line 90)
