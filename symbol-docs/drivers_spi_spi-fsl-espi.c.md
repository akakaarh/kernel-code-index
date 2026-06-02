# drivers/spi/spi-fsl-espi.c

Subsystem: drivers/spi

## Functions (28)

### fsl_espi_bufs
- Return type: static int
- Signature: fsl_espi_bufs(struct spi_device * spi,struct spi_transfer * t)
- Line: 352

### fsl_espi_check_message
- Return type: static int
- Signature: fsl_espi_check_message(struct spi_message * m)
- Line: 149

### fsl_espi_check_rxskip_mode
- Return type: static unsigned int
- Signature: fsl_espi_check_rxskip_mode(struct spi_message * m)
- Line: 183

### fsl_espi_cleanup
- Return type: static void
- Signature: fsl_espi_cleanup(struct spi_device * spi)
- Line: 521

### fsl_espi_cpu_irq
- Return type: static void
- Signature: fsl_espi_cpu_irq(struct fsl_espi * espi,u32 events)
- Line: 529

### fsl_espi_do_one_msg
- Return type: static int
- Signature: fsl_espi_do_one_msg(struct spi_controller * host,struct spi_message * m)
- Line: 435

### fsl_espi_fill_tx_fifo
- Return type: static void
- Signature: fsl_espi_fill_tx_fifo(struct fsl_espi * espi,u32 events)
- Line: 214

### fsl_espi_init_regs
- Return type: static void
- Signature: fsl_espi_init_regs(struct device * dev,bool initial)
- Line: 616

### fsl_espi_irq
- Return type: static irqreturn_t
- Signature: fsl_espi_irq(s32 irq,void * context_data)
- Line: 556

### fsl_espi_max_message_size
- Return type: static size_t
- Signature: fsl_espi_max_message_size(struct spi_device * spi)
- Line: 611

### fsl_espi_probe
- Return type: static int
- Signature: fsl_espi_probe(struct device * dev,struct resource * mem,unsigned int irq,unsigned int num_cs)
- Line: 663

### fsl_espi_read_reg
- Return type: static u32
- Signature: fsl_espi_read_reg(struct fsl_espi * espi,int offset)
- Line: 116

### fsl_espi_read_reg16
- Return type: static u16
- Signature: fsl_espi_read_reg16(struct fsl_espi * espi,int offset)
- Line: 121

### fsl_espi_read_reg8
- Return type: static u8
- Signature: fsl_espi_read_reg8(struct fsl_espi * espi,int offset)
- Line: 126

### fsl_espi_read_rx_fifo
- Return type: static void
- Signature: fsl_espi_read_rx_fifo(struct fsl_espi * espi,u32 events)
- Line: 271

### fsl_espi_runtime_resume
- Return type: static int
- Signature: fsl_espi_runtime_resume(struct device * dev)
- Line: 597

### fsl_espi_runtime_suspend
- Return type: static int
- Signature: fsl_espi_runtime_suspend(struct device * dev)
- Line: 584

### fsl_espi_setup
- Return type: static int
- Signature: fsl_espi_setup(struct spi_device * spi)
- Line: 478

### fsl_espi_setup_transfer
- Return type: static void
- Signature: fsl_espi_setup_transfer(struct spi_device * spi,struct spi_transfer * t)
- Line: 323

### fsl_espi_trans
- Return type: static int
- Signature: fsl_espi_trans(struct spi_message * m,struct spi_transfer * trans)
- Line: 397

### fsl_espi_write_reg
- Return type: static void
- Signature: fsl_espi_write_reg(struct fsl_espi * espi,int offset,u32 val)
- Line: 131

### fsl_espi_write_reg16
- Return type: static void
- Signature: fsl_espi_write_reg16(struct fsl_espi * espi,int offset,u16 val)
- Line: 137

### fsl_espi_write_reg8
- Return type: static void
- Signature: fsl_espi_write_reg8(struct fsl_espi * espi,int offset,u8 val)
- Line: 143

### of_fsl_espi_get_chipselects
- Return type: static int
- Signature: of_fsl_espi_get_chipselects(struct device * dev)
- Line: 740

### of_fsl_espi_probe
- Return type: static int
- Signature: of_fsl_espi_probe(struct platform_device * ofdev)
- Line: 755

### of_fsl_espi_remove
- Return type: static void
- Signature: of_fsl_espi_remove(struct platform_device * dev)
- Line: 783

### of_fsl_espi_resume
- Return type: static int
- Signature: of_fsl_espi_resume(struct device * dev)
- Line: 809

### of_fsl_espi_suspend
- Return type: static int
- Signature: of_fsl_espi_suspend(struct device * dev)
- Line: 797

## Structs (2)

### fsl_espi
- Line: 90
- Members:
  - dev: device *
  - reg_base: void __iomem *
  - m_transfers: list_head *
  - tx_t: spi_transfer *
  - tx_pos: unsigned int
  - tx_done: bool
  - rx_t: spi_transfer *
  - rx_pos: unsigned int
  - rx_done: bool
  - swab: bool
  - rxskip: unsigned int
  - lock: spinlock_t
  - spibrg: u32
  - done: completion
  - hw_mode: u32

### fsl_espi_cs
- Line: 112
- Members:
  - dev: device *
  - reg_base: void __iomem *
  - m_transfers: list_head *
  - tx_t: spi_transfer *
  - tx_pos: unsigned int
  - tx_done: bool
  - rx_t: spi_transfer *
  - rx_pos: unsigned int
  - rx_done: bool
  - swab: bool
  - rxskip: unsigned int
  - lock: spinlock_t
  - spibrg: u32
  - done: completion
  - hw_mode: u32

## Variables (3)

- static **espi_pm** : const struct dev_pm_ops (line 824)
- static **fsl_espi_driver** : platform_driver (line 836)
- static **of_fsl_espi_match** : const struct of_device_id[] (line 830)

## Macros (49)

- **AUTOSUSPEND_TIMEOUT** (line 88)
- **CSMODE_AFT**(x) (line 48)
- **CSMODE_BEF**(x) (line 47)
- **CSMODE_CG**(x) (line 49)
- **CSMODE_CI_INACTIVEHIGH** (line 40)
- **CSMODE_CP_BEGIN_EDGECLK** (line 41)
- **CSMODE_DIV16** (line 43)
- **CSMODE_INIT_VAL** (line 56)
- **CSMODE_LEN**(x) (line 46)
- **CSMODE_PM**(x) (line 44)
- **CSMODE_POL_1** (line 45)
- **CSMODE_REV** (line 42)
- **ESPI_SPCOM** (line 26)
- **ESPI_SPIE** (line 24)
- **ESPI_SPIM** (line 25)
- **ESPI_SPIRF** (line 28)
- **ESPI_SPITF** (line 27)
- **ESPI_SPMODE** (line 23)
- **ESPI_SPMODE0** (line 29)
- **ESPI_SPMODEx**(x) (line 31)
- **FSL_ESPI_FIFO_SIZE** (line 51)
- **FSL_ESPI_RXTHR** (line 52)
- **SPCOM_CS**(x) (line 80)
- **SPCOM_DO** (line 81)
- **SPCOM_RXSKIP**(x) (line 83)
- **SPCOM_TO** (line 82)
- **SPCOM_TRANLEN**(x) (line 84)
- **SPCOM_TRANLEN_MAX** (line 86)
- **SPIE_DON** (line 63)
- **SPIE_RNE** (line 67)
- **SPIE_RXCNT**(reg) (line 60)
- **SPIE_RXF** (line 65)
- **SPIE_RXT** (line 64)
- **SPIE_TNF** (line 68)
- **SPIE_TXCNT**(reg) (line 61)
- **SPIE_TXE** (line 62)
- **SPIE_TXT** (line 66)
- **SPIM_DON** (line 72)
- **SPIM_RNE** (line 76)
- **SPIM_RXF** (line 74)
- **SPIM_RXT** (line 73)
- **SPIM_TNF** (line 77)
- **SPIM_TXE** (line 71)
- **SPIM_TXT** (line 75)
- **SPMODE_ENABLE** (line 34)
- **SPMODE_INIT_VAL** (line 55)
- **SPMODE_LOOP** (line 35)
- **SPMODE_RXTHR**(x) (line 37)
- **SPMODE_TXTHR**(x) (line 36)
