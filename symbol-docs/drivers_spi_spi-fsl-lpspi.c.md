# drivers/spi/spi-fsl-lpspi.c

Subsystem: drivers/spi

## Functions (33)

### LPSPI_BUF_TX
- Return type: static u8
- Signature: LPSPI_BUF_TX(u8)
- Line: 193

### fsl_lpspi_bytes_per_word
- Return type: static int
- Signature: fsl_lpspi_bytes_per_word(const int bpw)
- Line: 205

### fsl_lpspi_calculate_timeout
- Return type: static int
- Signature: fsl_lpspi_calculate_timeout(struct fsl_lpspi_data * fsl_lpspi,int size)
- Line: 605

### fsl_lpspi_can_dma
- Return type: static bool
- Signature: fsl_lpspi_can_dma(struct spi_controller * controller,struct spi_device * spi,struct spi_transfer * transfer)
- Line: 210

### fsl_lpspi_config
- Return type: static int
- Signature: fsl_lpspi_config(struct fsl_lpspi_data * fsl_lpspi)
- Line: 430

### fsl_lpspi_dma_configure
- Return type: static int
- Signature: fsl_lpspi_dma_configure(struct spi_controller * controller)
- Line: 383

### fsl_lpspi_dma_exit
- Return type: static void
- Signature: fsl_lpspi_dma_exit(struct spi_controller * controller)
- Line: 713

### fsl_lpspi_dma_init
- Return type: static int
- Signature: fsl_lpspi_dma_init(struct device * dev,struct fsl_lpspi_data * fsl_lpspi,struct spi_controller * controller)
- Line: 726

### fsl_lpspi_dma_rx_callback
- Return type: static void
- Signature: fsl_lpspi_dma_rx_callback(void * cookie)
- Line: 591

### fsl_lpspi_dma_transfer
- Return type: static int
- Signature: fsl_lpspi_dma_transfer(struct spi_controller * controller,struct fsl_lpspi_data * fsl_lpspi,struct spi_transfer * transfer)
- Line: 620

### fsl_lpspi_dma_tx_callback
- Return type: static void
- Signature: fsl_lpspi_dma_tx_callback(void * cookie)
- Line: 598

### fsl_lpspi_init_rpm
- Return type: static int
- Signature: fsl_lpspi_init_rpm(struct fsl_lpspi_data * fsl_lpspi)
- Line: 881

### fsl_lpspi_isr
- Return type: static irqreturn_t
- Signature: fsl_lpspi_isr(int irq,void * dev_id)
- Line: 813

### fsl_lpspi_pio_transfer
- Return type: static int
- Signature: fsl_lpspi_pio_transfer(struct spi_controller * controller,struct spi_transfer * t)
- Line: 761

### fsl_lpspi_prepare_message
- Return type: static int
- Signature: fsl_lpspi_prepare_message(struct spi_controller * controller,struct spi_message * msg)
- Line: 502

### fsl_lpspi_probe
- Return type: static int
- Signature: fsl_lpspi_probe(struct platform_device * pdev)
- Line: 892

### fsl_lpspi_read_rx_fifo
- Return type: static void
- Signature: fsl_lpspi_read_rx_fifo(struct fsl_lpspi_data * fsl_lpspi)
- Line: 283

### fsl_lpspi_remove
- Return type: static void
- Signature: fsl_lpspi_remove(struct platform_device * pdev)
- Line: 1024

### fsl_lpspi_reset
- Return type: static void
- Signature: fsl_lpspi_reset(struct fsl_lpspi_data * fsl_lpspi)
- Line: 574

### fsl_lpspi_resume
- Return type: static int
- Signature: fsl_lpspi_resume(struct device * dev)
- Line: 1043

### fsl_lpspi_runtime_resume
- Return type: static int
- Signature: fsl_lpspi_runtime_resume(struct device * dev)
- Line: 846

### fsl_lpspi_runtime_suspend
- Return type: static int
- Signature: fsl_lpspi_runtime_suspend(struct device * dev)
- Line: 867

### fsl_lpspi_set_bitrate
- Return type: static int
- Signature: fsl_lpspi_set_bitrate(struct fsl_lpspi_data * fsl_lpspi)
- Line: 338

### fsl_lpspi_set_cmd
- Return type: static void
- Signature: fsl_lpspi_set_cmd(struct fsl_lpspi_data * fsl_lpspi)
- Line: 289

### fsl_lpspi_set_watermark
- Return type: static void
- Signature: fsl_lpspi_set_watermark(struct fsl_lpspi_data * fsl_lpspi)
- Line: 322

### fsl_lpspi_setup_transfer
- Return type: static int
- Signature: fsl_lpspi_setup_transfer(struct spi_controller * controller,struct spi_device * spi,struct spi_transfer * t)
- Line: 465

### fsl_lpspi_suspend
- Return type: static int
- Signature: fsl_lpspi_suspend(struct device * dev)
- Line: 1037

### fsl_lpspi_target_abort
- Return type: static int
- Signature: fsl_lpspi_target_abort(struct spi_controller * controller)
- Line: 537

### fsl_lpspi_transfer_one
- Return type: static int
- Signature: fsl_lpspi_transfer_one(struct spi_controller * controller,struct spi_device * spi,struct spi_transfer * t)
- Line: 784

### fsl_lpspi_wait_for_completion
- Return type: static int
- Signature: fsl_lpspi_wait_for_completion(struct spi_controller * controller)
- Line: 553

### fsl_lpspi_write_tx_fifo
- Return type: static void
- Signature: fsl_lpspi_write_tx_fifo(struct fsl_lpspi_data * fsl_lpspi)
- Line: 258

### lpspi_prepare_xfer_hardware
- Return type: static int
- Signature: lpspi_prepare_xfer_hardware(struct spi_controller * controller)
- Line: 233

### lpspi_unprepare_xfer_hardware
- Return type: static int
- Signature: lpspi_unprepare_xfer_hardware(struct spi_controller * controller)
- Line: 248

## Structs (3)

### fsl_lpspi_data
- Line: 109
- Members:
  - prescale_max: u8:3
  - query_hw_for_num_cs: bool:1
  - bpw: u8
  - chip_select: u8
  - prescale: u8
  - mode: u32
  - speed_hz: u32
  - effective_speed_hz: u32
  - dev: device *
  - base: void __iomem *
  - base_phys: unsigned long
  - clk_ipg: clk *
  - clk_per: clk *
  - is_target: bool
  - is_only_cs1: bool
  - is_first_byte: bool
  - rx_buf: void *
  - tx_buf: const void *
  - tx: void (*)(struct fsl_lpspi_data * fsl_lpspi)
  - rx: void (*)(struct fsl_lpspi_data * fsl_lpspi)
  - remain: u32
  - watermark: u8
  - txfifosize: u8
  - rxfifosize: u8
  - config: lpspi_config
  - xfer_done: completion
  - target_aborted: bool
  - usedma: bool
  - dma_rx_completion: completion
  - dma_tx_completion: completion
  - devtype_data: const struct fsl_lpspi_devtype_data *

### fsl_lpspi_devtype_data
- Line: 95
- Members:
  - prescale_max: u8:3
  - query_hw_for_num_cs: bool:1
  - bpw: u8
  - chip_select: u8
  - prescale: u8
  - mode: u32
  - speed_hz: u32
  - effective_speed_hz: u32
  - dev: device *
  - base: void __iomem *
  - base_phys: unsigned long
  - clk_ipg: clk *
  - clk_per: clk *
  - is_target: bool
  - is_only_cs1: bool
  - is_first_byte: bool
  - rx_buf: void *
  - tx_buf: const void *
  - tx: void (*)(struct fsl_lpspi_data * fsl_lpspi)
  - rx: void (*)(struct fsl_lpspi_data * fsl_lpspi)
  - remain: u32
  - watermark: u8
  - txfifosize: u8
  - rxfifosize: u8
  - config: lpspi_config
  - xfer_done: completion
  - target_aborted: bool
  - usedma: bool
  - dma_rx_completion: completion
  - dma_tx_completion: completion
  - devtype_data: const struct fsl_lpspi_devtype_data *

### lpspi_config
- Line: 100
- Members:
  - prescale_max: u8:3
  - query_hw_for_num_cs: bool:1
  - bpw: u8
  - chip_select: u8
  - prescale: u8
  - mode: u32
  - speed_hz: u32
  - effective_speed_hz: u32
  - dev: device *
  - base: void __iomem *
  - base_phys: unsigned long
  - clk_ipg: clk *
  - clk_per: clk *
  - is_target: bool
  - is_only_cs1: bool
  - is_first_byte: bool
  - rx_buf: void *
  - tx_buf: const void *
  - tx: void (*)(struct fsl_lpspi_data * fsl_lpspi)
  - rx: void (*)(struct fsl_lpspi_data * fsl_lpspi)
  - remain: u32
  - watermark: u8
  - txfifosize: u8
  - rxfifosize: u8
  - config: lpspi_config
  - xfer_done: completion
  - target_aborted: bool
  - usedma: bool
  - dma_rx_completion: completion
  - dma_tx_completion: completion
  - devtype_data: const struct fsl_lpspi_devtype_data *

## Variables (6)

- static **fsl_lpspi_driver** : platform_driver (line 1064)
- static **fsl_lpspi_dt_ids** : const struct of_device_id[] (line 159)
- static **fsl_lpspi_pm_ops** : const struct dev_pm_ops (line 1058)
- static **imx7ulp_lpspi_devtype_data** : const struct fsl_lpspi_devtype_data (line 151)
- static **imx93_lpspi_devtype_data** : const struct fsl_lpspi_devtype_data (line 146)
- static **s32g_lpspi_devtype_data** : const struct fsl_lpspi_devtype_data (line 155)

## Macros (57)

- **CFGR1_HOST** (line 77)
- **CFGR1_NOSTALL** (line 76)
- **CFGR1_PCSCFG** (line 73)
- **CFGR1_PCSPOL_MASK** (line 75)
- **CFGR1_PINCFG** (line 74)
- **CR_MEN** (line 61)
- **CR_RRF** (line 58)
- **CR_RST** (line 60)
- **CR_RTF** (line 59)
- **DER_RDDE** (line 71)
- **DER_TDDE** (line 72)
- **DRIVER_NAME** (line 31)
- **FCR_RXWATER** (line 78)
- **FCR_TXWATER** (line 79)
- **FSL_LPSPI_MAX_EDMA_BYTES** (line 36)
- **FSL_LPSPI_RPM_TIMEOUT** (line 33)
- **FSR_TXCOUNT** (line 80)
- **IER_FCIE** (line 68)
- **IER_RDIE** (line 69)
- **IER_TCIE** (line 67)
- **IER_TDIE** (line 70)
- **IMX7ULP_CCR** (line 49)
- **IMX7ULP_CFGR0** (line 45)
- **IMX7ULP_CFGR1** (line 46)
- **IMX7ULP_CR** (line 41)
- **IMX7ULP_DER** (line 44)
- **IMX7ULP_DMR0** (line 47)
- **IMX7ULP_DMR1** (line 48)
- **IMX7ULP_FCR** (line 50)
- **IMX7ULP_FSR** (line 51)
- **IMX7ULP_IER** (line 43)
- **IMX7ULP_PARAM** (line 40)
- **IMX7ULP_RDR** (line 55)
- **IMX7ULP_RSR** (line 54)
- **IMX7ULP_SR** (line 42)
- **IMX7ULP_TCR** (line 52)
- **IMX7ULP_TDR** (line 53)
- **IMX7ULP_VERID** (line 39)
- **LPSPI_BUF_RX**(type) (line 167)
- **LPSPI_BUF_TX**(type) (line 178)
- **RSR_RXEMPTY** (line 81)
- **SR_CLEAR_MASK** (line 93)
- **SR_FCF** (line 64)
- **SR_MBF** (line 62)
- **SR_RDF** (line 65)
- **SR_TCF** (line 63)
- **SR_TDF** (line 66)
- **TCR_CONT** (line 87)
- **TCR_CONTC** (line 88)
- **TCR_CPHA** (line 83)
- **TCR_CPOL** (line 82)
- **TCR_FRAMESZ** (line 91)
- **TCR_MODE** (line 84)
- **TCR_PCS** (line 86)
- **TCR_PRESCALE** (line 85)
- **TCR_RXMSK** (line 89)
- **TCR_TXMSK** (line 90)
