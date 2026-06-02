# drivers/spi/spi-img-spfi.c

Subsystem: drivers/spi

## Functions (26)

### img_spfi_can_dma
- Return type: static bool
- Signature: img_spfi_can_dma(struct spi_controller * host,struct spi_device * spi,struct spi_transfer * xfer)
- Line: 502

### img_spfi_config
- Return type: static void
- Signature: img_spfi_config(struct spi_controller * host,struct spi_device * spi,struct spi_transfer * xfer)
- Line: 440

### img_spfi_dma_rx_cb
- Return type: static void
- Signature: img_spfi_dma_rx_cb(void * data)
- Line: 278

### img_spfi_dma_tx_cb
- Return type: static void
- Signature: img_spfi_dma_tx_cb(void * data)
- Line: 292

### img_spfi_handle_err
- Return type: static void
- Signature: img_spfi_handle_err(struct spi_controller * host,struct spi_message * msg)
- Line: 387

### img_spfi_irq
- Return type: static irqreturn_t
- Signature: img_spfi_irq(int irq,void * dev_id)
- Line: 510

### img_spfi_prepare
- Return type: static int
- Signature: img_spfi_prepare(struct spi_controller * host,struct spi_message * msg)
- Line: 408

### img_spfi_probe
- Return type: static int
- Signature: img_spfi_probe(struct platform_device * pdev)
- Line: 525

### img_spfi_remove
- Return type: static void
- Signature: img_spfi_remove(struct platform_device * pdev)
- Line: 667

### img_spfi_resume
- Return type: static int
- Signature: img_spfi_resume(struct device * dev)
- Line: 729

### img_spfi_runtime_resume
- Return type: static int
- Signature: img_spfi_runtime_resume(struct device * dev)
- Line: 702

### img_spfi_runtime_suspend
- Return type: static int
- Signature: img_spfi_runtime_suspend(struct device * dev)
- Line: 691

### img_spfi_start_dma
- Return type: static int
- Signature: img_spfi_start_dma(struct spi_controller * host,struct spi_device * spi,struct spi_transfer * xfer)
- Line: 306

### img_spfi_start_pio
- Return type: static int
- Signature: img_spfi_start_pio(struct spi_controller * host,struct spi_device * spi,struct spi_transfer * xfer)
- Line: 224

### img_spfi_suspend
- Return type: static int
- Signature: img_spfi_suspend(struct device * dev)
- Line: 722

### img_spfi_transfer_one
- Return type: static int
- Signature: img_spfi_transfer_one(struct spi_controller * host,struct spi_device * spi,struct spi_transfer * xfer)
- Line: 479

### img_spfi_unprepare
- Return type: static int
- Signature: img_spfi_unprepare(struct spi_controller * host,struct spi_message * msg)
- Line: 430

### spfi_pio_read32
- Return type: static unsigned int
- Signature: spfi_pio_read32(struct img_spfi * spfi,u32 * buf,unsigned int max)
- Line: 186

### spfi_pio_read8
- Return type: static unsigned int
- Signature: spfi_pio_read8(struct img_spfi * spfi,u8 * buf,unsigned int max)
- Line: 205

### spfi_pio_write32
- Return type: static unsigned int
- Signature: spfi_pio_write32(struct img_spfi * spfi,const u32 * buf,unsigned int max)
- Line: 150

### spfi_pio_write8
- Return type: static unsigned int
- Signature: spfi_pio_write8(struct img_spfi * spfi,const u8 * buf,unsigned int max)
- Line: 168

### spfi_readl
- Return type: static u32
- Signature: spfi_readl(struct img_spfi * spfi,u32 reg)
- Line: 104

### spfi_reset
- Return type: static void
- Signature: spfi_reset(struct img_spfi * spfi)
- Line: 123

### spfi_start
- Return type: static void
- Signature: spfi_start(struct img_spfi * spfi)
- Line: 114

### spfi_wait_all_done
- Return type: static int
- Signature: spfi_wait_all_done(struct img_spfi * spfi)
- Line: 129

### spfi_writel
- Return type: static void
- Signature: spfi_writel(struct img_spfi * spfi,u32 val,u32 reg)
- Line: 109

## Structs (1)

### img_spfi
- Line: 87
- Members:
  - dev: device *
  - host: spi_controller *
  - lock: spinlock_t
  - regs: void __iomem *
  - phys: phys_addr_t
  - irq: int
  - spfi_clk: clk *
  - sys_clk: clk *
  - rx_ch: dma_chan *
  - tx_ch: dma_chan *
  - tx_dma_busy: bool
  - rx_dma_busy: bool

## Variables (3)

- static **img_spfi_driver** : platform_driver (line 757)
- static **img_spfi_of_match** : const struct of_device_id[] (line 751)
- static **img_spfi_pm_ops** : const struct dev_pm_ops (line 745)

## Macros (49)

- **SPFI_32BIT_FIFO_SIZE** (line 84)
- **SPFI_8BIT_FIFO_SIZE** (line 85)
- **SPFI_CONTROL** (line 34)
- **SPFI_CONTROL_CONTINUE** (line 35)
- **SPFI_CONTROL_GET_DMA** (line 38)
- **SPFI_CONTROL_SE** (line 39)
- **SPFI_CONTROL_SEND_DMA** (line 37)
- **SPFI_CONTROL_SOFT_RESET** (line 36)
- **SPFI_CONTROL_SPFI_EN** (line 45)
- **SPFI_CONTROL_TMODE_DUAL** (line 43)
- **SPFI_CONTROL_TMODE_MASK** (line 41)
- **SPFI_CONTROL_TMODE_QUAD** (line 44)
- **SPFI_CONTROL_TMODE_SHIFT** (line 40)
- **SPFI_CONTROL_TMODE_SINGLE** (line 42)
- **SPFI_DEVICE_PARAMETER**(x) (line 24)
- **SPFI_DEVICE_PARAMETER_BITCLK_MASK** (line 26)
- **SPFI_DEVICE_PARAMETER_BITCLK_SHIFT** (line 25)
- **SPFI_DEVICE_PARAMETER_CSDELAY_MASK** (line 32)
- **SPFI_DEVICE_PARAMETER_CSDELAY_SHIFT** (line 31)
- **SPFI_DEVICE_PARAMETER_CSHOLD_MASK** (line 30)
- **SPFI_DEVICE_PARAMETER_CSHOLD_SHIFT** (line 29)
- **SPFI_DEVICE_PARAMETER_CSSETUP_MASK** (line 28)
- **SPFI_DEVICE_PARAMETER_CSSETUP_SHIFT** (line 27)
- **SPFI_INTERRUPT_ALLDONETRIG** (line 67)
- **SPFI_INTERRUPT_CLEAR** (line 64)
- **SPFI_INTERRUPT_ENABLE** (line 63)
- **SPFI_INTERRUPT_GDEX32BIT** (line 70)
- **SPFI_INTERRUPT_GDEX8BIT** (line 66)
- **SPFI_INTERRUPT_GDFUL** (line 68)
- **SPFI_INTERRUPT_GDHF** (line 69)
- **SPFI_INTERRUPT_GDTRIG** (line 71)
- **SPFI_INTERRUPT_IACCESS** (line 65)
- **SPFI_INTERRUPT_SDE** (line 74)
- **SPFI_INTERRUPT_SDFUL** (line 72)
- **SPFI_INTERRUPT_SDHF** (line 73)
- **SPFI_INTERRUPT_SDTRIG** (line 75)
- **SPFI_INTERRUPT_STATUS** (line 62)
- **SPFI_PORT_STATE** (line 51)
- **SPFI_PORT_STATE_CK_PHASE**(x) (line 55)
- **SPFI_PORT_STATE_CK_POL**(x) (line 54)
- **SPFI_PORT_STATE_DEV_SEL_MASK** (line 53)
- **SPFI_PORT_STATE_DEV_SEL_SHIFT** (line 52)
- **SPFI_RX_32BIT_VALID_DATA** (line 59)
- **SPFI_RX_8BIT_VALID_DATA** (line 60)
- **SPFI_TRANSACTION** (line 47)
- **SPFI_TRANSACTION_TSIZE_MASK** (line 49)
- **SPFI_TRANSACTION_TSIZE_SHIFT** (line 48)
- **SPFI_TX_32BIT_VALID_DATA** (line 57)
- **SPFI_TX_8BIT_VALID_DATA** (line 58)
